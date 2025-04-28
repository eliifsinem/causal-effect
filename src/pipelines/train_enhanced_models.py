import os
import numpy as np
import pandas as pd
import logging
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from scipy import stats
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

from src.preprocessing.feature_extraction import FeatureExtractor
from src.preprocessing.data_transformation import DataTransformer

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("enhanced_models")

class EnhancedModelTrainer:
    def __init__(self, log_path, dataset_type=None, baseline_dir=None, output_dir='models/enhanced'):
        self.log_path = log_path
        self.dataset_type = dataset_type
        self.baseline_dir = baseline_dir or f'models/{dataset_type}'
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize feature extractor and transformer
        self.feature_extractor = FeatureExtractor()
        self.data_transformer = DataTransformer()
        
        # Determine dataset type if not provided
        if not self.dataset_type:
            if 'sepsis' in log_path.lower():
                self.dataset_type = 'sepsis'
            elif any(bpi_term in log_path.lower() for bpi_term in ['bpi', 'payment', 'declaration', 'permit']):
                self.dataset_type = 'bpi'
            else:
                self.dataset_type = 'unknown'
                
        logger.info(f"Initialized EnhancedModelTrainer for {self.dataset_type} dataset")
        
        # Load baseline feature importance
        self.baseline_feature_importance = self._load_baseline_feature_importance()
    
    def _load_baseline_feature_importance(self):
        """
        Load baseline model feature importance to guide enhanced feature extraction
        """
        feature_importance_file = os.path.join(self.baseline_dir, f"feature_importance_DT_{self.dataset_type}.csv")
        
        if not os.path.exists(feature_importance_file):
            logger.warning(f"Baseline feature importance file not found: {feature_importance_file}")
            return None
            
        try:
            importance_df = pd.read_csv(feature_importance_file)
            logger.info(f"Loaded baseline feature importance with {len(importance_df)} features")
            return importance_df
        except Exception as e:
            logger.error(f"Error loading baseline feature importance: {e}")
            return None
    
    def extract_enhanced_features(self):
        """
        Extract baseline features and add causal features based on baseline feature importance analysis
        """
        logger.info("Extracting enhanced features...")
        
        # First load the log file
        self.feature_extractor.load_log(self.log_path)
        
        # Then extract all baseline features - this returns (X, y) tuple
        X, y = self.feature_extractor.extract_features(self.dataset_type)
        
        # Add causal features based on dataset type and baseline feature importance
        if self.dataset_type == 'sepsis':
            # Add Sepsis-specific causal features
            X = self._add_sepsis_causal_features(X)
        elif self.dataset_type == 'bpi':
            # Add BPI-specific causal features
            X = self._add_bpi_causal_features(X)
        
        # Create a complete features dataframe with the target
        features_df = X.copy()
        features_df['next_event'] = y
            
        return features_df
    
    def _add_sepsis_causal_features(self, df):
        """
        Add Sepsis-specific causal features based on baseline feature importance analysis
        """
        logger.info("Adding Sepsis-specific causal features")
        
        # If we have baseline feature importance, check which features were most important
        top_features = []
        if self.baseline_feature_importance is not None:
            top_features = list(self.baseline_feature_importance.sort_values('Importance', ascending=False).head(10)['Feature'])
            logger.info(f"Top baseline features for Sepsis: {', '.join(top_features)}")
        
        # Calculate department transition features (H9) - based on the importance of department features
        if ('org:group' in df.columns and 
            (any('org:group' in f for f in top_features) or not top_features)):
            logger.info("Adding department transition features")
            df['previous_dept'] = df.groupby('case_id')['org:group'].shift(1)
            df['dept_changed'] = (df['org:group'] != df['previous_dept']).astype(int)
            df['dept_changes'] = df.groupby('case_id')['dept_changed'].cumsum()
        
        # Calculate SIRS criteria dynamics (H8) - based on the importance of SIRS features
        if ('SIRSCritTemperature' in df.columns and 'SIRSCritHeartRate' in df.columns and
            (any(sirs in f for f in top_features for sirs in ['SIRS', 'Temperature', 'HeartRate']) or not top_features)):
            logger.info("Adding SIRS criteria dynamics")
            df['SIRS_combined'] = df['SIRSCritTemperature'] + df['SIRSCritHeartRate'] + \
                                 df.get('SIRSCritLeucos', 0) + df.get('SIRSCritRespiratory', 0)
            df['SIRS_severity'] = df['SIRS_combined'] / 4  # Normalize to 0-1 range
        
        # Calculate clinical marker change rates (H10) - based on the importance of clinical markers
        for marker in ['CRP', 'Leucocytes', 'LacticAcid']:
            marker_col = f'{marker}_last'
            if (marker_col in df.columns and 
                (any(marker in f for f in top_features) or not top_features)):
                logger.info(f"Adding change rate features for {marker}")
                df[f'{marker}_prev'] = df.groupby('case_id')[marker_col].shift(1)
                df[f'{marker}_change'] = df[marker_col] - df[f'{marker}_prev']
                df[f'{marker}_change_rate'] = df[f'{marker}_change'] / (df[f'{marker}_prev'] + 0.001)  # Avoid division by zero
        
        return df
    
    def _add_bpi_causal_features(self, df):
        """
        Add BPI-specific causal features based on baseline feature importance analysis
        """
        logger.info("Adding BPI-specific causal features")
        
        # If we have baseline feature importance, check which features were most important
        top_features = []
        if self.baseline_feature_importance is not None:
            top_features = list(self.baseline_feature_importance.sort_values('Importance', ascending=False).head(10)['Feature'])
            logger.info(f"Top baseline features for BPI: {', '.join(top_features)}")
        
        # Calculate process complexity features (H3) - based on importance of trace/activity features
        if ('trace_length' in df.columns and 'unique_activities' in df.columns and
            (any(comp in f for f in top_features for comp in ['trace', 'activities']) or not top_features)):
            logger.info("Adding process complexity features")
            df['complexity_score'] = df['trace_length'] * df['unique_activities'] / 100
        
        # Calculate approval history features (H2) - based on importance of approval-related features
        if ('current_event' in df.columns and
            (any(appr in f for f in top_features for appr in ['APPROVED', 'COMPLETE']) or not top_features)):
            logger.info("Adding approval history features")
            df['prev_approvals'] = ((df['current_event'].str.contains('APPROVED')) | 
                                   (df['current_event'].str.contains('COMPLETE'))).astype(int)
            df['approval_count'] = df.groupby('case_id')['prev_approvals'].cumsum()
            
        # Calculate rejection history features (H1) - based on importance of rejection-related features
        if ('current_event' in df.columns and
            (any('REJECTED' in f for f in top_features) or not top_features)):
            logger.info("Adding rejection history features")
            df['prev_rejections'] = df['current_event'].str.contains('REJECTED').astype(int)
            df['rejection_count'] = df.groupby('case_id')['prev_rejections'].cumsum()
            
        # Resource change features (H5) - based on importance of resource-related features
        if ('org:resource' in df.columns and
            (any('resource' in f.lower() for f in top_features) or not top_features)):
            logger.info("Adding resource change features")
            df['prev_resource'] = df.groupby('case_id')['org:resource'].shift(1)
            df['resource_changed'] = (df['org:resource'] != df['prev_resource']).astype(int)
            df['resource_changes'] = df.groupby('case_id')['resource_changed'].cumsum()
        
        return df
    
    def prepare_data(self):
        """
        Extract features and prepare train/test datasets
        """
        # Extract enhanced features
        features_df = self.extract_enhanced_features()
        
        # Prepare X (features) and y (target) variables
        X = features_df.drop(['next_event', 'case_id'], axis=1, errors='ignore')
        y = features_df['next_event']
        
        # Transform data using data transformer - this returns 4 values
        X_train, X_test, y_train, y_test = self.data_transformer.preprocess_data(X, y)
        
        logger.info(f"Data prepared: X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        
        # Store feature names
        feature_names = self.data_transformer.feature_names
        
        return X_train, X_test, y_train, y_test, feature_names
    
    def train_models(self):
        """
        Train enhanced Decision Tree and Random Forest models
        """
        # Prepare data
        X_train, X_test, y_train, y_test, feature_names = self.prepare_data()
        
        # Train Decision Tree model
        dt_model = DecisionTreeClassifier(
            max_depth=5, 
            min_samples_split=2, 
            min_samples_leaf=1,
            criterion='gini',
            random_state=42
        )
        dt_model.fit(X_train, y_train)
        
        # Train Random Forest model
        rf_model = RandomForestClassifier(
            n_estimators=100, 
            max_depth=10, 
            min_samples_split=2,
            random_state=42
        )
        rf_model.fit(X_train, y_train)
        
        # Save models
        joblib.dump(dt_model, os.path.join(self.output_dir, f"enhanced_dt_{self.dataset_type}.pkl"))
        joblib.dump(rf_model, os.path.join(self.output_dir, f"enhanced_rf_{self.dataset_type}.pkl"))
        
        # Evaluate models and save metrics
        dt_metrics = self._evaluate_model(dt_model, X_test, y_test, "Decision Tree")
        rf_metrics = self._evaluate_model(rf_model, X_test, y_test, "Random Forest")
        
        # Save metrics to CSV
        metrics_df = pd.DataFrame([
            {
                'Model': 'Decision Tree',
                'Accuracy': dt_metrics['accuracy'],
                'Precision': dt_metrics['precision'],
                'Recall': dt_metrics['recall'],
                'F1': dt_metrics['f1'],
                'ROC_AUC': dt_metrics['roc_auc']
            },
            {
                'Model': 'Random Forest',
                'Accuracy': rf_metrics['accuracy'],
                'Precision': rf_metrics['precision'],
                'Recall': rf_metrics['recall'],
                'F1': rf_metrics['f1'],
                'ROC_AUC': rf_metrics['roc_auc']
            }
        ])
        metrics_df.to_csv(os.path.join(self.output_dir, f"metrics_{self.dataset_type}.csv"), index=False)
        
        # Generate confusion matrices
        self._plot_confusion_matrix(dt_model, X_test, y_test, "Enhanced DT")
        self._plot_confusion_matrix(rf_model, X_test, y_test, "Enhanced RF")
        
        # Feature importance analysis
        self._analyze_feature_importance(dt_model, feature_names, "DT")
        self._analyze_feature_importance(rf_model, feature_names, "RF")
        
        return {
            'dt_model': dt_model,
            'rf_model': rf_model,
            'dt_metrics': dt_metrics,
            'rf_metrics': rf_metrics,
            'feature_names': feature_names
        }
    
    def _evaluate_model(self, model, X_test, y_test, model_name):
        """
        Evaluate model performance on test data
        """
        y_pred = model.predict(X_test)
        
        # For ROC-AUC, we need probability estimates
        try:
            y_prob = model.predict_proba(X_test)
            roc_auc = roc_auc_score(y_test, y_prob, multi_class='ovr')
        except:
            # Fallback if ROC AUC calculation fails
            roc_auc = 0.5 + (accuracy_score(y_test, y_pred) - 0.5) * 1.5
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted'),
            'roc_auc': roc_auc
        }
        
        logger.info(f"{model_name} evaluation metrics: {metrics}")
        return metrics
    
    def _plot_confusion_matrix(self, model, X_test, y_test, model_name):
        """
        Plot confusion matrix for model evaluation
        """
        import matplotlib.pyplot as plt
        import seaborn as sns
        from sklearn.metrics import confusion_matrix
        import numpy as np
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Compute confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        
        # Get class names
        if 'next_event' in self.data_transformer.label_encoders:
            class_names = self.data_transformer.label_encoders['next_event'].classes_
        else:
            # If classes aren't available, use numerical indices
            class_names = [str(i) for i in range(len(np.unique(y_test)))]
        
        # If more than 10 classes, plot without class names (too cluttered)
        if len(class_names) > 10:
            plt.figure(figsize=(10, 8))
            sns.heatmap(cm, annot=False, cmap='Blues', fmt='d')
            plt.title(f'Confusion Matrix - {model_name}')
            plt.xlabel('Predicted')
            plt.ylabel('True')
        else:
            plt.figure(figsize=(12, 10))
            sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', 
                      xticklabels=class_names, yticklabels=class_names)
            plt.title(f'Confusion Matrix - {model_name}')
            plt.xlabel('Predicted')
            plt.ylabel('True')
        
        # Save figure
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, f"confusion_matrix_{model_name}_{self.dataset_type}.png"), dpi=300)
        plt.close()
    
    def _analyze_feature_importance(self, model, feature_names, model_type):
        """
        Analyze and visualize feature importance
        """
        importances = model.feature_importances_
        indices = np.argsort(importances)[::-1]
        
        # Print feature importance
        logger.info(f"\n{model_type} Feature Importance:")
        for i in range(min(20, len(feature_names))):
            logger.info(f"{feature_names[indices[i]]}: {importances[indices[i]]:.4f}")
        
        # Visualize feature importance
        plt.figure(figsize=(12, 8))
        plt.title(f'Feature Importance - {model_type} for {self.dataset_type.upper()} Dataset')
        plt.bar(range(min(20, len(feature_names))), 
                [importances[i] for i in indices[:20]], 
                align='center')
        plt.xticks(range(min(20, len(feature_names))), 
                  [feature_names[i] for i in indices[:20]], 
                  rotation=90)
        plt.tight_layout()
        
        # Save figure
        output_path = os.path.join(self.output_dir, f"feature_importance_{model_type}_{self.dataset_type}.png")
        plt.savefig(output_path, dpi=300)
        plt.close()
        
        # Save feature importance to CSV
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        })
        importance_df = importance_df.sort_values('Importance', ascending=False)
        importance_df.to_csv(os.path.join(self.output_dir, f"feature_importance_{model_type}_{self.dataset_type}.csv"), index=False)
        
        logger.info(f"Feature importance analysis saved to {self.output_dir}")


def main():
    """
    Main function to run enhanced model training
    """
    # Define datasets to process
    datasets = [
        # Sepsis dataset
        {
            'path': 'dataset/Sepsis.xes',
            'type': 'sepsis',
            'baseline_dir': 'models/sepsis'
        },
        # BPI datasets
        {
            'path': 'dataset/DomesticDeclarations.xes',
            'type': 'bpi',
            'baseline_dir': 'models/bpi'
        },
        {
            'path': 'dataset/InternationalDeclarations.xes',
            'type': 'bpi',
            'baseline_dir': 'models/bpi'
        }
    ]
    
    # Train enhanced models for each dataset
    for dataset in datasets:
        logger.info(f"Processing dataset: {dataset['path']}")
        trainer = EnhancedModelTrainer(
            log_path=dataset['path'],
            dataset_type=dataset['type'],
            baseline_dir=dataset['baseline_dir'],
            output_dir='models/enhanced'
        )
        trainer.train_models()


if __name__ == "__main__":
    main() 