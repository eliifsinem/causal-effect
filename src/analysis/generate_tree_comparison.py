import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, export_graphviz
import graphviz
import joblib

from src.preprocessing.feature_extraction import FeatureExtractor
from src.preprocessing.data_transformation import DataTransformer
from src.models.decision_tree import ProcessDecisionTree

def generate_tree_comparison(dataset_path, output_dir='reports/tree_comparison'):
    """
    Generate and compare two decision trees:
    1. Baseline - using only control-flow features
    2. Enhanced - using selected causal features
    """
    print(f"Generating tree comparison using dataset: {dataset_path}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Load and prepare the data
    feature_extractor = FeatureExtractor()
    feature_extractor.load_log(dataset_path)
    
    # Determine which dataset we're working with
    if 'Domestic' in dataset_path or 'BPI' in dataset_path:
        print("Processing BPI dataset...")
        X, y = feature_extractor.extract_bpi_features()
        dataset_name = 'bpi'
        
        # Define potential causal features for BPI
        causal_features = [
            'time_since_start', 'time_since_last_event',
            'current_org:role', 'case:Amount',
            'weekend', 'time_of_day'
        ]
    else:
        print("Processing Sepsis dataset...")
        X, y = feature_extractor.extract_sepsis_features()
        dataset_name = 'sepsis'
        
        # Define causal features for Sepsis
        causal_features = [
            'CRP_last', 'Leucocytes_last', 'LacticAcid_last', 
            'SIRSCritLeucos', 'SIRSCritTemperature',
            'dept_changes', 'time_since_start'
        ]
    
    # Store original feature names
    all_feature_names = X.columns.tolist()
    print(f"Available features: {len(all_feature_names)}")
    print(f"Sample features: {all_feature_names[:10]}")
    
    # Define control-flow features (baseline)
    control_flow_features = [
        'current_event', 'event_position', 'trace_length', 
        'repeated_activities', 'unique_activities'
    ]
    
    # Filter to only include features that exist in the dataset
    control_flow_features = [f for f in control_flow_features if f in all_feature_names]
    causal_features = [f for f in causal_features if f in all_feature_names]
    
    print(f"Available control-flow features: {control_flow_features}")
    print(f"Available causal features: {causal_features}")
    
    if not causal_features:
        print("Warning: No causal features available in this dataset. Using generic time-based features.")
        causal_features = [f for f in all_feature_names if 'time' in f]
        if not causal_features:
            # Just use some of the available features
            causal_features = all_feature_names[:min(5, len(all_feature_names))]
    
    # Define enhanced features (control flow + causal)
    enhanced_features = control_flow_features + [f for f in causal_features if f not in control_flow_features]
    
    print(f"Final baseline features: {control_flow_features}")
    print(f"Final enhanced features: {enhanced_features}")
    
    # Create transformer
    data_transformer = DataTransformer()
    
    # Preprocess all data
    X_train_all, X_test_all, y_train, y_test = data_transformer.preprocess_data(
        X, y, test_size=0.2, random_state=42, balance_classes=True
    )
    
    # Print unique classes
    print(f"Target classes: {len(set(y_train))} unique values")
    
    # Select features for each model
    X_train_baseline = X_train_all[control_flow_features]
    X_test_baseline = X_test_all[control_flow_features]
    
    X_train_enhanced = X_train_all[enhanced_features]
    X_test_enhanced = X_test_all[enhanced_features]
    
    # Create and train baseline model (slightly deeper for better learning)
    baseline_dt = ProcessDecisionTree(max_depth=3)
    baseline_dt.train(X_train_baseline, y_train, feature_names=control_flow_features)
    
    # Create and train enhanced model with causal features
    enhanced_dt = ProcessDecisionTree(max_depth=3)
    enhanced_dt.train(X_train_enhanced, y_train, feature_names=enhanced_features)
    
    # Evaluate both models
    baseline_results = baseline_dt.evaluate(X_test_baseline, y_test)
    enhanced_results = enhanced_dt.evaluate(X_test_enhanced, y_test)
    
    print(f"Baseline model accuracy: {baseline_results['accuracy']:.4f}")
    print(f"Enhanced model accuracy: {enhanced_results['accuracy']:.4f}")
    print(f"Improvement: {enhanced_results['accuracy'] - baseline_results['accuracy']:.4f}")
    
    # Save tree visualizations
    baseline_file = os.path.join(output_dir, f'{dataset_name}_baseline_tree')
    enhanced_file = os.path.join(output_dir, f'{dataset_name}_enhanced_tree')
    
    # Export trees
    try:
        # Create dot files
        export_graphviz(
            baseline_dt.model,
            out_file=f"{baseline_file}.dot",
            feature_names=baseline_dt.feature_names[:len(baseline_dt.model.feature_importances_)],
            class_names=baseline_dt.class_names,
            filled=True,
            rounded=True,
            special_characters=True
        )
        
        export_graphviz(
            enhanced_dt.model,
            out_file=f"{enhanced_file}.dot",
            feature_names=enhanced_dt.feature_names[:len(enhanced_dt.model.feature_importances_)],
            class_names=enhanced_dt.class_names,
            filled=True,
            rounded=True,
            special_characters=True
        )
        
        # Convert to PNG
        for file in [baseline_file, enhanced_file]:
            graph = graphviz.Source.from_file(f"{file}.dot")
            graph.format = 'png'
            graph.render(file, cleanup=True)
            print(f"Saved tree visualization to {file}.png")
            
    except Exception as e:
        print(f"Failed to export tree visualizations: {str(e)}")
        
        # Fallback to matplotlib
        plt.figure(figsize=(15, 10))
        plt.title(f"Baseline Tree ({dataset_name})")
        from sklearn.tree import plot_tree
        plot_tree(
            baseline_dt.model, 
            feature_names=baseline_dt.feature_names[:len(baseline_dt.model.feature_importances_)],
            class_names=baseline_dt.class_names,
            filled=True,
            rounded=True,
            max_depth=3
        )
        plt.savefig(f"{baseline_file}.png", format='png', dpi=150, bbox_inches='tight')
        
        plt.figure(figsize=(15, 10))
        plt.title(f"Enhanced Tree ({dataset_name})")
        plot_tree(
            enhanced_dt.model, 
            feature_names=enhanced_dt.feature_names[:len(enhanced_dt.model.feature_importances_)],
            class_names=enhanced_dt.class_names,
            filled=True,
            rounded=True,
            max_depth=3
        )
        plt.savefig(f"{enhanced_file}.png", format='png', dpi=150, bbox_inches='tight')
    
    # Create comparison summary
    with open(os.path.join(output_dir, f'{dataset_name}_tree_comparison.md'), 'w') as f:
        f.write(f"# Decision Tree Comparison - {dataset_name.upper()} Dataset\n\n")
        f.write("## Model Performance\n\n")
        f.write(f"- Baseline Model (control-flow features only): {baseline_results['accuracy']:.4f}\n")
        f.write(f"- Enhanced Model (with causal features): {enhanced_results['accuracy']:.4f}\n")
        f.write(f"- Improvement: {enhanced_results['accuracy'] - baseline_results['accuracy']:.4f}\n\n")
        
        f.write("## Baseline Model Features\n\n")
        f.write("- " + "\n- ".join(control_flow_features) + "\n\n")
        
        f.write("## Enhanced Model Features (Control-flow + Causal)\n\n")
        f.write("### Control-flow Features\n")
        f.write("- " + "\n- ".join(control_flow_features) + "\n\n")
        f.write("### Causal Features\n")
        f.write("- " + "\n- ".join([f for f in causal_features if f not in control_flow_features]) + "\n\n")
        
        f.write("## Feature Importance in Enhanced Model (Top 10)\n\n")
        top_features = enhanced_dt.feature_importance.head(10)
        for _, row in top_features.iterrows():
            f.write(f"- {row['feature']}: {row['importance']:.4f}\n")
    
    print(f"Comparison complete. Results saved to {output_dir}")
    return baseline_file + '.png', enhanced_file + '.png'

if __name__ == "__main__":
    # Check for BPI dataset first
    if os.path.exists('dataset/DomesticDeclarations.xes'):
        baseline_img, enhanced_img = generate_tree_comparison('dataset/DomesticDeclarations.xes')
    
    # Check for Sepsis dataset
    elif os.path.exists('dataset/Sepsis.xes'):
        baseline_img, enhanced_img = generate_tree_comparison('dataset/Sepsis.xes')
    
    else:
        print("No supported datasets found. Please add either Sepsis.xes or DomesticDeclarations.xes to the dataset directory.") 