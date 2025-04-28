import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, accuracy_score
import joblib

from src.preprocessing.feature_extraction import FeatureExtractor
from src.preprocessing.data_transformation import DataTransformer
from src.models.decision_tree import ProcessDecisionTree
from src.models.random_forest import ProcessRandomForest
from src.models.ensemble import ModelEnsemble
from src.pipelines.causality_tests import run_causality_tests, save_causality_report

class ModelTrainer:
    def __init__(self, config=None):
        """
        Initialize model trainer with configuration
        
        Args:
            config: Dictionary with training configuration
        """
        self.config = config or {
            'dataset_path': 'dataset/Sepsis.xes',
            'model_dir': 'models',
            'report_dir': 'reports',
            'test_size': 0.2,
            'random_state': 42,
            'balance_classes': True,
            'run_causality_tests': True,  # Flag to run causality tests
            'models': {
                'decision_tree': {
                    'enabled': True,
                    'params': {
                        'max_depth': None,
                        'min_samples_split': 2,
                        'min_samples_leaf': 1
                    }
                },
                'random_forest': {
                    'enabled': True,
                    'params': {
                        'n_estimators': 100,
                        'max_depth': None,
                        'min_samples_split': 2,
                        'min_samples_leaf': 1
                    }
                },
                'ensemble': {
                    'enabled': True,
                    'voting': 'soft'
                }
            }
        }
        
        # Create directories
        os.makedirs(self.config['model_dir'], exist_ok=True)
        os.makedirs(self.config['report_dir'], exist_ok=True)
        
        # Initialize components
        self.feature_extractor = FeatureExtractor()
        self.data_transformer = DataTransformer()
        self.models = {}
        self.trained_models = {}
        self.ensemble = None
        self.results = {}
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.feature_names = None
        
    def prepare_data(self, dataset_type=None):
        """Prepare data for training"""
        # Load the dataset
        self.feature_extractor.load_log(self.config['dataset_path'])
        
        # Extract features based on dataset type
        X, y = self.feature_extractor.extract_features(dataset_type)
        
        # Store original feature names (before any transformations)
        self.feature_names = X.columns.tolist()
        
        # Preprocess data
        X_train, X_test, y_train, y_test = self.data_transformer.preprocess_data(
            X, y, 
            test_size=self.config['test_size'],
            random_state=self.config['random_state'],
            balance_classes=self.config['balance_classes']
        )
        
        # Store the data
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        
        print(f"Training data: {X_train.shape}, Test data: {X_test.shape}")
        print(f"Feature names length: {len(self.feature_names)}, X_train columns: {X_train.shape[1]}")
        
        return X_train, X_test, y_train, y_test
    
    def train_models(self, X_train, y_train):
        """Train all enabled models"""
        models_config = self.config['models']
        
        # Get the actual feature names from X_train
        actual_feature_names = X_train.columns.tolist()
        
        # Train decision tree if enabled
        if models_config.get('decision_tree', {}).get('enabled', False):
            print("Training Decision Tree model...")
            dt_params = models_config.get('decision_tree', {}).get('params', {})
            dt = ProcessDecisionTree(**dt_params)
            # Use the actual feature names from X_train
            dt.train(X_train, y_train, feature_names=actual_feature_names)
            self.trained_models['decision_tree'] = dt
        
        # Train random forest if enabled
        if models_config.get('random_forest', {}).get('enabled', False):
            print("Training Random Forest model...")
            rf_params = models_config.get('random_forest', {}).get('params', {})
            rf = ProcessRandomForest(**rf_params)
            # Use the actual feature names from X_train
            rf.train(X_train, y_train, feature_names=actual_feature_names)
            self.trained_models['random_forest'] = rf
        
        # Create ensemble if enabled and at least 2 models are trained
        if models_config.get('ensemble', {}).get('enabled', False) and len(self.trained_models) >= 2:
            print("Creating Model Ensemble...")
            voting = models_config.get('ensemble', {}).get('voting', 'soft')
            self.ensemble = ModelEnsemble(list(self.trained_models.values()), voting=voting)
        
        return self.trained_models
    
    def evaluate_models(self, X_test, y_test):
        """Evaluate all trained models"""
        results = {}
        
        # Evaluate individual models
        for model_name, model in self.trained_models.items():
            print(f"Evaluating {model_name}...")
            model_results = model.evaluate(X_test, y_test)
            results[model_name] = model_results
        
        # Evaluate ensemble if available
        if self.ensemble is not None:
            print("Evaluating Model Ensemble...")
            ensemble_results = self.ensemble.evaluate(X_test, y_test)
            results['ensemble'] = ensemble_results
        
        self.results = results
        return results
    
    def save_models(self):
        """Save all trained models"""
        model_dir = self.config['model_dir']
        
        # Save individual models
        for model_name, model in self.trained_models.items():
            model_save_dir = os.path.join(model_dir, model_name)
            model.save_model(model_save_dir)
        
        # Save ensemble if available
        if self.ensemble is not None:
            ensemble_save_dir = os.path.join(model_dir, 'ensemble')
            self.ensemble.save_model(ensemble_save_dir)
        
        # Save data transformer for future predictions
        self.data_transformer.save_transformation_metadata(model_dir)
        
        # Save feature extractor configuration
        extractor_config = {
            'dataset_path': self.config['dataset_path'],
            'original_feature_names': self.feature_names
        }
        with open(os.path.join(model_dir, 'extractor_config.json'), 'w') as f:
            json.dump(extractor_config, f, indent=4)
        
        # Save full training configuration
        with open(os.path.join(model_dir, 'training_config.json'), 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def save_reports(self):
        """Save evaluation reports and visualizations"""
        report_dir = self.config['report_dir']
        
        # Save results summary
        summary = {
            'models': {},
            'best_model': ''
        }
        
        best_accuracy = 0
        for model_name, result in self.results.items():
            accuracy = result['accuracy']
            summary['models'][model_name] = {
                'accuracy': accuracy,
                'report': result.get('classification_report', {})
            }
            
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                summary['best_model'] = model_name
        
        # Save summary as JSON
        with open(os.path.join(report_dir, 'evaluation_summary.json'), 'w') as f:
            json.dump(summary, f, indent=4)
        
        # Save feature importance plots for tree-based models
        for model_name, model in self.trained_models.items():
            if hasattr(model, 'visualize_feature_importance'):
                try:
                    fig = model.visualize_feature_importance(top_n=20)
                    fig.savefig(os.path.join(report_dir, f'{model_name}_feature_importance.png'))
                    plt.close(fig)
                except Exception as e:
                    print(f"Warning: Could not create feature importance plot for {model_name}: {e}")
        
        # If we have an ensemble, save model comparison
        if self.ensemble is not None and hasattr(self.ensemble, 'compare_models'):
            if self.X_test is not None and self.y_test is not None:
                try:
                    _, comparison_fig = self.ensemble.compare_models(self.X_test, self.y_test)
                    comparison_fig.savefig(os.path.join(report_dir, 'model_comparison.png'))
                    plt.close(comparison_fig)
                except Exception as e:
                    print(f"Warning: Could not create model comparison plot: {e}")
    
    def run_causality_analysis(self, dataset_type=None):
        """Run causality analysis and save reports"""
        if not self.config.get('run_causality_tests', False):
            print("Causality tests disabled. Skipping...")
            return
            
        if self.X_test is None or self.y_test is None:
            print("No test data available. Cannot run causality tests.")
            return
            
        print("Running causality analysis...")
        try:
            # Run causality tests
            dataset_name = dataset_type or os.path.basename(self.config['dataset_path']).split('.')[0]
            causality_results = run_causality_tests(
                dataset_type=dataset_type, 
                models_dir=self.config['model_dir'],
                X_test=self.X_test, 
                y_test=self.y_test
            )
            
            # Save causality report
            save_causality_report(
                results=causality_results,
                report_dir=self.config['report_dir'],
                dataset_name=dataset_name
            )
            
            print("Causality analysis completed successfully.")
        except Exception as e:
            print(f"Error running causality analysis: {str(e)}")
            import traceback
            traceback.print_exc()
    
    def run_pipeline(self, dataset_type=None):
        """Run the full training pipeline"""
        try:
            print("Preparing data...")
            X_train, X_test, y_train, y_test = self.prepare_data(dataset_type)
            
            print("Training models...")
            self.train_models(X_train, y_train)
            
            print("Evaluating models...")
            self.evaluate_models(X_test, y_test)
            
            print("Saving models...")
            self.save_models()
            
            print("Generating reports...")
            self.save_reports()
            
            print("Running causality analysis...")
            self.run_causality_analysis(dataset_type)
            
            print("Pipeline completed successfully.")
            
            # Return results summary
            return {
                'models': list(self.trained_models.keys()),
                'ensemble': self.ensemble is not None,
                'results': self.results
            }
        except Exception as e:
            print(f"Error in pipeline: {str(e)}")
            import traceback
            traceback.print_exc()
            return {
                'error': str(e),
                'models': list(self.trained_models.keys()) if self.trained_models else []
            }

def train_sepsis_models():
    """Train models for the Sepsis dataset"""
    config = {
        'dataset_path': 'dataset/Sepsis.xes',
        'model_dir': 'models/sepsis',
        'report_dir': 'reports/sepsis',
        'test_size': 0.2,
        'random_state': 42,
        'balance_classes': True,
        'run_causality_tests': True,  # Enable causality tests
        'models': {
            'decision_tree': {
                'enabled': True,
                'params': {
                    'max_depth': None,
                    'min_samples_split': 2,
                    'min_samples_leaf': 1
                }
            },
            'random_forest': {
                'enabled': True,
                'params': {
                    'n_estimators': 100,
                    'max_depth': None,
                    'min_samples_split': 2,
                    'min_samples_leaf': 1
                }
            },
            'ensemble': {
                'enabled': True,
                'voting': 'soft'
            }
        }
    }
    
    trainer = ModelTrainer(config)
    return trainer.run_pipeline(dataset_type='sepsis')

def train_bpi_models():
    """Train models for the BPI dataset"""
    # Check which BPI2020 files exist
    bpi_files = [
        'DomesticDeclarations.xes',
        'InternationalDeclarations.xes',
        'PermitLog.xes',
        'PrepaidTravelCost.xes',
        'RequestForPayment.xes'
    ]
    
    # Use the first available BPI file
    bpi_dataset_path = None
    for file in bpi_files:
        file_path = os.path.join('dataset', file)
        if os.path.exists(file_path):
            bpi_dataset_path = file_path
            print(f"Using BPI dataset: {file}")
            break
    
    if not bpi_dataset_path:
        print("No BPI dataset files found.")
        return {"models": {}}
    
    config = {
        'dataset_path': bpi_dataset_path,
        'model_dir': 'models/bpi',
        'report_dir': 'reports/bpi',
        'test_size': 0.2,
        'random_state': 42,
        'balance_classes': True,
        'run_causality_tests': True,  # Enable causality tests
        'models': {
            'decision_tree': {
                'enabled': True,
                'params': {
                    'max_depth': None,
                    'min_samples_split': 2,
                    'min_samples_leaf': 1
                }
            },
            'random_forest': {
                'enabled': True,
                'params': {
                    'n_estimators': 100,
                    'max_depth': None,
                    'min_samples_split': 2,
                    'min_samples_leaf': 1
                }
            },
            'ensemble': {
                'enabled': True,
                'voting': 'soft'
            }
        }
    }
    
    trainer = ModelTrainer(config)
    return trainer.run_pipeline(dataset_type='bpi')

if __name__ == "__main__":
    # Train Sepsis models
    sepsis_results = train_sepsis_models()
    
    # Train BPI models if any of the BPI dataset files exist
    bpi_files_exist = any(os.path.exists(os.path.join('dataset', file)) for file in [
        'DomesticDeclarations.xes',
        'InternationalDeclarations.xes',
        'PermitLog.xes',
        'PrepaidTravelCost.xes',
        'RequestForPayment.xes'
    ])
    
    if bpi_files_exist:
        bpi_results = train_bpi_models()
    else:
        print("BPI dataset not found. Skipping BPI model training.") 