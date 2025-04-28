import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

class ProcessRandomForest:
    def __init__(self, n_estimators=100, max_depth=None, min_samples_split=2, 
                 min_samples_leaf=1, random_state=42, n_jobs=-1):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state,
            n_jobs=n_jobs
        )
        self.feature_names = None
        self.class_names = None
        self.feature_importance = None
        self.accuracy = None
    
    def train(self, X_train, y_train, feature_names=None):
        """Train the Random Forest model"""
        # Store feature names, ensuring they match the actual features used
        self.feature_names = X_train.columns.tolist() if feature_names is None else feature_names
        
        # If feature_names was provided but doesn't match X_train columns, adjust
        if len(self.feature_names) != X_train.shape[1]:
            print(f"Warning: Provided feature_names length ({len(self.feature_names)}) doesn't match X_train columns ({X_train.shape[1]})")
            self.feature_names = X_train.columns.tolist()
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Store class names
        self.class_names = list(sorted(set(y_train)))
        
        # Calculate feature importance
        importances = self.model.feature_importances_
        self.feature_importance = pd.DataFrame({
            'feature': self.feature_names[:len(importances)],
            'importance': importances
        }).sort_values('importance', ascending=False)
        
        return self.model
    
    def evaluate(self, X_test, y_test):
        """Evaluate the model and return performance metrics"""
        y_pred = self.model.predict(X_test)
        
        self.accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        return {
            'accuracy': self.accuracy,
            'classification_report': report,
            'confusion_matrix': conf_matrix,
            'feature_importance': self.feature_importance
        }
    
    def predict(self, X):
        """Make predictions using the trained model"""
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Return probability estimates for samples"""
        return self.model.predict_proba(X)
    
    def save_model(self, model_dir):
        """Save the model and its metadata"""
        os.makedirs(model_dir, exist_ok=True)
        
        # Save the model
        model_path = os.path.join(model_dir, 'random_forest_model.pkl')
        joblib.dump(self.model, model_path)
        
        # Save feature importance
        if self.feature_importance is not None:
            self.feature_importance.to_csv(os.path.join(model_dir, 'rf_feature_importance.csv'), index=False)
        
        # Save feature names and class names
        metadata = {
            'feature_names': self.feature_names,
            'class_names': self.class_names,
            'accuracy': self.accuracy
        }
        joblib.dump(metadata, os.path.join(model_dir, 'rf_metadata.pkl'))
        
        print(f"Random Forest model saved to {model_dir}")
    
    def load_model(self, model_dir):
        """Load a saved model and its metadata"""
        # Load the model
        model_path = os.path.join(model_dir, 'random_forest_model.pkl')
        self.model = joblib.load(model_path)
        
        # Load metadata
        metadata_path = os.path.join(model_dir, 'rf_metadata.pkl')
        if os.path.exists(metadata_path):
            metadata = joblib.load(metadata_path)
            self.feature_names = metadata.get('feature_names', None)
            self.class_names = metadata.get('class_names', None)
            self.accuracy = metadata.get('accuracy', None)
        
        # Load feature importance
        importance_path = os.path.join(model_dir, 'rf_feature_importance.csv')
        if os.path.exists(importance_path):
            self.feature_importance = pd.read_csv(importance_path)
        
        print(f"Random Forest model loaded from {model_dir}")
        
        return self.model
    
    def visualize_feature_importance(self, top_n=20):
        """Visualize the most important features"""
        if self.feature_importance is None:
            print("Feature importance not available. Train the model first.")
            return
        
        # Get top N features
        top_features = self.feature_importance.head(top_n)
        
        # Plot
        plt.figure(figsize=(10, 8))
        sns.barplot(x='importance', y='feature', data=top_features)
        plt.title(f'Top {top_n} Feature Importance - Random Forest')
        plt.tight_layout()
        
        return plt.gcf()
    
    def visualize_confusion_matrix(self, y_test, y_pred=None):
        """Visualize the confusion matrix"""
        if y_pred is None:
            y_pred = self.model.predict(y_test)
            
        conf_matrix = confusion_matrix(y_test, y_pred)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                   xticklabels=self.class_names if self.class_names else 'auto',
                   yticklabels=self.class_names if self.class_names else 'auto')
        plt.title('Confusion Matrix - Random Forest')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        return plt.gcf()
    
    def generate_transition_report(self, X_test, y_test):
        """Generate a report of event transitions and their predictive factors"""
        y_pred = self.model.predict(X_test)
        
        # Create DataFrame with actual and predicted values
        results_df = pd.DataFrame({
            'actual': y_test,
            'predicted': y_pred
        })
        
        # Add case_id if available in X_test
        if 'case_id' in X_test.columns:
            results_df['case_id'] = X_test['case_id']
        
        # Create transition report
        report = {
            'accuracy': accuracy_score(y_test, y_pred),
            'transitions': {}
        }
        
        # For each unique target event, identify key predictive features
        for event in set(y_test):
            # Filter instances where this was the target event
            event_mask = y_test == event
            event_instances = X_test[event_mask]
            
            if len(event_instances) == 0:
                continue
                
            # Calculate feature importance for this specific transition
            feature_importance = pd.DataFrame({
                'feature': self.feature_names[:len(self.model.feature_importances_)],
                'importance': self.model.feature_importances_
            })
            
            # Add to report
            report['transitions'][event] = {
                'count': len(event_instances),
                'accuracy': accuracy_score(y_test[event_mask], y_pred[event_mask]),
                'top_predictive_factors': feature_importance.sort_values('importance', ascending=False).head(5).to_dict('records')
            }
        
        return report
