import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from collections import Counter

class ModelEnsemble:
    def __init__(self, models=None, voting='soft'):
        """
        Initialize the model ensemble
        
        Args:
            models: List of trained model instances
            voting: Type of voting ('hard' or 'soft')
        """
        self.models = models if models is not None else []
        self.voting = voting
        self.feature_names = None
        self.class_names = None
        self.accuracy = None
    
    def add_model(self, model):
        """Add a model to the ensemble"""
        self.models.append(model)
    
    def predict(self, X):
        """Make predictions using the ensemble"""
        if not self.models:
            raise ValueError("No models in the ensemble")
            
        if self.voting == 'hard':
            # Hard voting: majority vote
            predictions = []
            for model in self.models:
                predictions.append(model.predict(X))
            
            # Transpose to get predictions by sample
            predictions = np.array(predictions).T
            
            # Get the most common prediction for each sample
            ensemble_predictions = []
            for pred_set in predictions:
                counter = Counter(pred_set)
                ensemble_predictions.append(counter.most_common(1)[0][0])
            
            return np.array(ensemble_predictions)
        else:
            # Soft voting: average probabilities
            proba_predictions = []
            for model in self.models:
                proba_predictions.append(model.predict_proba(X))
            
            # Average the probabilities
            avg_proba = np.mean(proba_predictions, axis=0)
            
            # Return class with highest probability
            return np.argmax(avg_proba, axis=1)
    
    def predict_proba(self, X):
        """Predict class probabilities using the ensemble"""
        if not self.models:
            raise ValueError("No models in the ensemble")
            
        # Get probability predictions from each model
        proba_predictions = []
        for model in self.models:
            proba_predictions.append(model.predict_proba(X))
        
        # Average the probabilities
        avg_proba = np.mean(proba_predictions, axis=0)
        
        return avg_proba
    
    def evaluate(self, X_test, y_test):
        """Evaluate the ensemble model"""
        y_pred = self.predict(X_test)
        
        # Make sure predictions and ground truth have the same type
        # Convert prediction to match y_test type if necessary
        if isinstance(y_test.iloc[0], str) and not isinstance(y_pred[0], str):
            # Get class names from first model
            if hasattr(self.models[0], 'class_names') and self.models[0].class_names:
                class_names = self.models[0].class_names
                # Convert numeric predictions to class names
                y_pred = np.array([class_names[p] if p < len(class_names) else f"Unknown-{p}" for p in y_pred])
        
        # Calculate accuracy and metrics
        self.accuracy = accuracy_score(y_test, y_pred)
        
        try:
            report = classification_report(y_test, y_pred, output_dict=True)
            conf_matrix = confusion_matrix(y_test, y_pred)
        except Exception as e:
            print(f"Warning: Could not compute classification report: {e}")
            report = {"error": str(e)}
            conf_matrix = np.zeros((1, 1))
        
        # Store class names if not already set
        if self.class_names is None and hasattr(self.models[0], 'class_names'):
            self.class_names = self.models[0].class_names
        
        # Store feature names if not already set
        if self.feature_names is None and hasattr(self.models[0], 'feature_names'):
            self.feature_names = self.models[0].feature_names
        
        return {
            'accuracy': self.accuracy,
            'classification_report': report,
            'confusion_matrix': conf_matrix
        }
    
    def save_model(self, model_dir):
        """Save the ensemble model"""
        os.makedirs(model_dir, exist_ok=True)
        
        # Save metadata
        metadata = {
            'voting': self.voting,
            'class_names': self.class_names,
            'feature_names': self.feature_names,
            'accuracy': self.accuracy,
            'model_count': len(self.models)
        }
        
        # Save metadata
        joblib.dump(metadata, os.path.join(model_dir, 'ensemble_metadata.pkl'))
        
        # Save individual model references (not the actual models)
        model_info = []
        for i, model in enumerate(self.models):
            model_type = model.__class__.__name__
            model_info.append({
                'index': i,
                'type': model_type
            })
            
        joblib.dump(model_info, os.path.join(model_dir, 'ensemble_models.pkl'))
        
        print(f"Ensemble model metadata saved to {model_dir}")
    
    def load_models(self, models):
        """Load models into the ensemble"""
        self.models = models
    
    def load_metadata(self, model_dir):
        """Load metadata"""
        metadata_path = os.path.join(model_dir, 'ensemble_metadata.pkl')
        if os.path.exists(metadata_path):
            metadata = joblib.load(metadata_path)
            self.voting = metadata.get('voting', 'soft')
            self.class_names = metadata.get('class_names', None)
            self.feature_names = metadata.get('feature_names', None)
            self.accuracy = metadata.get('accuracy', None)
            
            print(f"Ensemble metadata loaded from {model_dir}")
            
    def visualize_confusion_matrix(self, y_test, y_pred=None):
        """Visualize the confusion matrix"""
        if y_pred is None:
            y_pred = self.predict(y_test)
        
        # Ensure types match
        if isinstance(y_test.iloc[0], str) and not isinstance(y_pred[0], str):
            # Get class names from first model
            if hasattr(self.models[0], 'class_names') and self.models[0].class_names:
                class_names = self.models[0].class_names
                # Convert numeric predictions to class names
                y_pred = np.array([class_names[p] if p < len(class_names) else f"Unknown-{p}" for p in y_pred])
        
        try:
            conf_matrix = confusion_matrix(y_test, y_pred)
            
            plt.figure(figsize=(10, 8))
            sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues',
                      xticklabels=self.class_names if self.class_names else 'auto',
                      yticklabels=self.class_names if self.class_names else 'auto')
            plt.title('Confusion Matrix - Ensemble Model')
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            plt.tight_layout()
            
            return plt.gcf()
        except Exception as e:
            print(f"Error creating confusion matrix: {e}")
            # Create an empty figure
            plt.figure(figsize=(10, 8))
            plt.text(0.5, 0.5, f"Error creating confusion matrix: {e}", 
                    horizontalalignment='center', verticalalignment='center')
            plt.tight_layout()
            return plt.gcf()
    
    def compare_models(self, X_test, y_test):
        """Compare performance of individual models vs ensemble"""
        results = {}
        
        # Evaluate individual models
        for i, model in enumerate(self.models):
            model_name = f"Model_{i+1}_{model.__class__.__name__}"
            try:
                y_pred = model.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                
                try:
                    report = classification_report(y_test, y_pred, output_dict=True)
                except Exception:
                    report = {"error": "Could not compute classification report"}
                
                results[model_name] = {
                    'accuracy': acc,
                    'report': report
                }
            except Exception as e:
                print(f"Error evaluating {model_name}: {e}")
                results[model_name] = {
                    'accuracy': 0,
                    'error': str(e)
                }
        
        # Evaluate ensemble
        try:
            ensemble_pred = self.predict(X_test)
            # Ensure types match
            if isinstance(y_test.iloc[0], str) and not isinstance(ensemble_pred[0], str):
                # Get class names from first model
                if hasattr(self.models[0], 'class_names') and self.models[0].class_names:
                    class_names = self.models[0].class_names
                    # Convert numeric predictions to class names
                    ensemble_pred = np.array([class_names[p] if p < len(class_names) else f"Unknown-{p}" for p in ensemble_pred])
                    
            ensemble_acc = accuracy_score(y_test, ensemble_pred)
            
            try:
                ensemble_report = classification_report(y_test, ensemble_pred, output_dict=True)
            except Exception:
                ensemble_report = {"error": "Could not compute classification report"}
            
            results['Ensemble'] = {
                'accuracy': ensemble_acc,
                'report': ensemble_report
            }
        except Exception as e:
            print(f"Error evaluating ensemble: {e}")
            results['Ensemble'] = {
                'accuracy': 0,
                'error': str(e)
            }
        
        # Create comparison DataFrame
        accuracy_comparison = pd.DataFrame({
            'Model': list(results.keys()),
            'Accuracy': [results[model].get('accuracy', 0) for model in results]
        })
        
        # Plot comparison
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Model', y='Accuracy', data=accuracy_comparison)
        plt.title('Model Accuracy Comparison')
        plt.ylim(0, 1)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        return results, plt.gcf()
