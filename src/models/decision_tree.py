import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

class ProcessDecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1,
                 criterion='gini', random_state=42):
        self.model = DecisionTreeClassifier(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            criterion=criterion,
            random_state=random_state
        )
        self.feature_names = None
        self.class_names = None
        self.feature_importance = None
        self.accuracy = None
        self.tree_text = None
    
    def train(self, X_train, y_train, feature_names=None):
        """Train the Decision Tree model"""
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
        
        # Store tree structure as text
        self.tree_text = export_text(self.model, feature_names=self.feature_names[:len(importances)])
        
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
        model_path = os.path.join(model_dir, 'decision_tree_model.pkl')
        joblib.dump(self.model, model_path)
        
        # Save feature importance
        if self.feature_importance is not None:
            self.feature_importance.to_csv(os.path.join(model_dir, 'dt_feature_importance.csv'), index=False)
        
        # Save tree text representation
        if self.tree_text is not None:
            with open(os.path.join(model_dir, 'decision_tree_structure.txt'), 'w') as f:
                f.write(self.tree_text)
        
        # Save feature names and class names
        metadata = {
            'feature_names': self.feature_names,
            'class_names': self.class_names,
            'accuracy': self.accuracy
        }
        joblib.dump(metadata, os.path.join(model_dir, 'dt_metadata.pkl'))
        
        print(f"Decision Tree model saved to {model_dir}")
    
    def load_model(self, model_dir):
        """Load a saved model and its metadata"""
        # Load the model
        model_path = os.path.join(model_dir, 'decision_tree_model.pkl')
        self.model = joblib.load(model_path)
        
        # Load metadata
        metadata_path = os.path.join(model_dir, 'dt_metadata.pkl')
        if os.path.exists(metadata_path):
            metadata = joblib.load(metadata_path)
            self.feature_names = metadata.get('feature_names', None)
            self.class_names = metadata.get('class_names', None)
            self.accuracy = metadata.get('accuracy', None)
        
        # Load feature importance
        importance_path = os.path.join(model_dir, 'dt_feature_importance.csv')
        if os.path.exists(importance_path):
            self.feature_importance = pd.read_csv(importance_path)
        
        # Load tree text
        tree_path = os.path.join(model_dir, 'decision_tree_structure.txt')
        if os.path.exists(tree_path):
            with open(tree_path, 'r') as f:
                self.tree_text = f.read()
        
        print(f"Decision Tree model loaded from {model_dir}")
        
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
        plt.title(f'Top {top_n} Feature Importance - Decision Tree')
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
        plt.title('Confusion Matrix - Decision Tree')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.tight_layout()
        
        return plt.gcf()
    
    def export_tree_visualization(self, output_file, format='png'):
        """Export the decision tree visualization"""
        try:
            from sklearn.tree import plot_tree
            import graphviz
            
            # Create dot file
            dot_file = output_file.replace(f'.{format}', '.dot')
            export_graphviz(
                self.model,
                out_file=dot_file,
                feature_names=self.feature_names[:len(self.model.feature_importances_)],
                class_names=self.class_names,
                filled=True,
                rounded=True,
                special_characters=True
            )
            
            # Convert to requested format
            if format != 'dot':
                graph = graphviz.Source.from_file(dot_file)
                graph.format = format
                graph.render(output_file.replace(f'.{format}', ''), cleanup=True)
                
            return True
            
        except Exception as e:
            print(f"Failed to export tree visualization: {str(e)}")
            
            # Fallback to simple plot
            plt.figure(figsize=(20, 10))
            plot_tree(
                self.model, 
                feature_names=self.feature_names[:len(self.model.feature_importances_)],
                class_names=self.class_names,
                filled=True,
                rounded=True
            )
            plt.savefig(output_file, format=format, dpi=300, bbox_inches='tight')
            
            return True
    
    def analyze_decision_paths(self, X_test, y_test, top_n=5):
        """Analyze the most common decision paths in the tree"""
        node_indicator = self.model.decision_path(X_test)
        leaf_id = self.model.apply(X_test)
        
        # Count paths by leaf node
        leaf_counts = {}
        for i, leaf in enumerate(leaf_id):
            if leaf not in leaf_counts:
                leaf_counts[leaf] = {
                    'count': 0,
                    'correct': 0,
                    'samples': []
                }
            leaf_counts[leaf]['count'] += 1
            leaf_counts[leaf]['samples'].append(i)
            if self.model.predict(X_test[i:i+1])[0] == y_test.iloc[i]:
                leaf_counts[leaf]['correct'] += 1
        
        # Sort by frequency
        sorted_leafs = sorted(leaf_counts.items(), key=lambda x: x[1]['count'], reverse=True)
        
        # Analyze top N most common paths
        results = []
        for leaf, info in sorted_leafs[:top_n]:
            # Get a sample index for this leaf
            sample_idx = info['samples'][0]
            
            # Get the path
            path = node_indicator.indices[node_indicator.indptr[sample_idx]:
                                         node_indicator.indptr[sample_idx + 1]]
            
            # Extract decision rules
            rules = []
            for node_id in path:
                if node_id != leaf:  # Skip leaf node
                    # Get the feature used for this split
                    feature_idx = self.model.tree_.feature[node_id]
                    if feature_idx < len(self.feature_names):  # Check if index is valid
                        feature = self.feature_names[feature_idx]
                    else:
                        feature = f"feature_{feature_idx}"
                    
                    threshold = self.model.tree_.threshold[node_id]
                    
                    # Check if sample goes left or right
                    if X_test.iloc[sample_idx, self.model.tree_.feature[node_id]] <= threshold:
                        rules.append(f"{feature} <= {threshold:.2f}")
                    else:
                        rules.append(f"{feature} > {threshold:.2f}")
            
            # Calculate accuracy for this path
            accuracy = info['correct'] / info['count']
            
            # Get predicted class
            samples = X_test.iloc[info['samples']]
            predicted_class = self.model.predict(samples.iloc[0:1])[0]
            
            # Add to results
            results.append({
                'leaf_id': leaf,
                'count': info['count'],
                'accuracy': accuracy,
                'predicted_class': predicted_class,
                'rules': rules
            })
        
        return results
