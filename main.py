import os
import argparse
from src.pipelines.model_trainer import train_sepsis_models, train_bpi_models
from src.pipelines.train_enhanced_models import EnhancedModelTrainer
from src.pipelines.compare_models import ModelComparator
from src.pipelines.causality_tests import CausalityTester
from src.analysis.process_mining import analyze_event_logs
import joblib
import pandas as pd

def setup_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        'dataset',
        'models',
        'models/sepsis',
        'models/bpi',
        'models/enhanced',
        'reports',
        'reports/sepsis',
        'reports/bpi',
        'reports/comparison',
        'results',
        'results/causality',
        'results/causality/sepsis',
        'results/causality/bpi',
        os.path.join('src', 'result', 'dataset_analysis')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    """Main entry point for the application"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process Mining and Event Prediction')
    parser.add_argument('--analyze', action='store_true', help='Run process mining analysis')
    parser.add_argument('--train', action='store_true', help='Train baseline prediction models')
    parser.add_argument('--train-enhanced', action='store_true', help='Train enhanced prediction models')
    parser.add_argument('--compare', action='store_true', help='Compare baseline and enhanced models')
    parser.add_argument('--causality', action='store_true', help='Run causality tests')
    parser.add_argument('--dataset', choices=['sepsis', 'bpi', 'all'], default='all', 
                        help='Dataset to process (sepsis, bpi, or all)')
    
    args = parser.parse_args()
    
    # Set up directories
    setup_directories()
    
    # Process Mining Analysis
    if args.analyze:
        print("Running Process Mining Analysis...")
        log_directory = "dataset"
        result_directory = os.path.join("src", "result", "dataset_analysis")
        analyze_event_logs(log_directory, result_directory)
    
    # Baseline Model Training
    if args.train:
        print("Running Baseline Model Training...")
        
        if args.dataset in ['sepsis', 'all']:
            if os.path.exists('dataset/Sepsis.xes'):
                print("\n====== Training Sepsis Models ======")
                sepsis_results = train_sepsis_models()
                print(f"Trained {len(sepsis_results['models'])} models for Sepsis dataset")
            else:
                print("Sepsis dataset not found. Skipping Sepsis model training.")
        
        if args.dataset in ['bpi', 'all']:
            # Check for any of the BPI2020 dataset files
            bpi_files = [
                'DomesticDeclarations.xes',
                'InternationalDeclarations.xes',
                'PermitLog.xes',
                'PrepaidTravelCost.xes',
                'RequestForPayment.xes'
            ]
            
            bpi_files_exist = any(os.path.exists(os.path.join('dataset', file)) for file in bpi_files)
            
            if bpi_files_exist:
                print("\n====== Training BPI Models ======")
                bpi_results = train_bpi_models()
                print(f"Trained {len(bpi_results['models'])} models for BPI dataset")
            else:
                print("BPI dataset not found. Skipping BPI model training.")
    
    # Enhanced Model Training
    if args.train_enhanced:
        print("Running Enhanced Model Training...")
        
        if args.dataset in ['sepsis', 'all']:
            if os.path.exists('dataset/Sepsis.xes'):
                print("\n====== Training Enhanced Sepsis Models ======")
                trainer = EnhancedModelTrainer(
                    log_path='dataset/Sepsis.xes',
                    dataset_type='sepsis',
                    baseline_dir='models/sepsis',
                    output_dir='models/enhanced'
                )
                trainer.train_models()
                print(f"Trained enhanced models for Sepsis dataset")
            else:
                print("Sepsis dataset not found. Skipping enhanced Sepsis model training.")
        
        if args.dataset in ['bpi', 'all']:
            # Check for any of the BPI2020 dataset files
            bpi_files = [
                'DomesticDeclarations.xes',
                'InternationalDeclarations.xes'
            ]
            
            for bpi_file in bpi_files:
                if os.path.exists(os.path.join('dataset', bpi_file)):
                    print(f"\n====== Training Enhanced BPI Models ({bpi_file}) ======")
                    trainer = EnhancedModelTrainer(
                        log_path=os.path.join('dataset', bpi_file),
                        dataset_type='bpi',
                        baseline_dir='models/bpi',
                        output_dir='models/enhanced'
                    )
                    trainer.train_models()
                    print(f"Trained enhanced models for BPI dataset ({bpi_file})")
                else:
                    print(f"BPI dataset file {bpi_file} not found. Skipping.")
    
    # Model Comparison
    if args.compare:
        print("Running Model Comparison...")
        
        if args.dataset in ['sepsis', 'all']:
            print("\n====== Comparing Sepsis Models ======")
            comparator = ModelComparator(
                dataset_type='sepsis',
                baseline_dir='models/sepsis',
                enhanced_dir='models/enhanced',
                output_dir='reports/comparison/sepsis'
            )
            comparison_results = comparator.run_comparison()
            print(f"Completed Sepsis models comparison")
        
        if args.dataset in ['bpi', 'all']:
            print("\n====== Comparing BPI Models ======")
            comparator = ModelComparator(
                dataset_type='bpi',
                baseline_dir='models/bpi',
                enhanced_dir='models/enhanced',
                output_dir='reports/comparison/bpi'
            )
            comparison_results = comparator.run_comparison()
            print(f"Completed BPI models comparison")
    
    # Causality Tests
    if args.causality:
        print("Running Causality Tests...")
        
        if args.dataset in ['sepsis', 'all']:
            print("\n====== Running Sepsis Causality Tests ======")
            try:
                # Load enhanced models and test data
                enhanced_dt_path = os.path.join('models/enhanced', f"enhanced_dt_sepsis.pkl")
                
                if os.path.exists(enhanced_dt_path):
                    enhanced_dt = joblib.load(enhanced_dt_path)
                    
                    # Load or generate test data
                    test_data_path = os.path.join('models/enhanced', f"test_data_sepsis.pkl")
                    if os.path.exists(test_data_path):
                        test_data = joblib.load(test_data_path)
                        X_test = test_data['X_test']
                        y_test = test_data['y_test']
                        feature_names = test_data['feature_names']
                    else:
                        # Create test data by running a quick feature extraction
                        print("Test data not found. Creating from dataset...")
                        trainer = EnhancedModelTrainer(
                            log_path='dataset/Sepsis.xes',
                            dataset_type='sepsis',
                            baseline_dir='models/sepsis',
                            output_dir='models/enhanced'
                        )
                        X_train, X_test, y_train, y_test, feature_names = trainer.prepare_data()
                        
                        # Save test data for future use
                        joblib.dump({
                            'X_test': X_test,
                            'y_test': y_test,
                            'feature_names': feature_names
                        }, test_data_path)
                    
                    # Run causality tester
                    causality_tester = CausalityTester(
                        models={'enhanced_dt': enhanced_dt},
                        feature_names=feature_names,
                        X_test=X_test,
                        y_test=y_test,
                        dataset_type='sepsis',
                        baseline_dir='models/sepsis',
                        output_dir='results/causality/sepsis'
                    )
                    
                    hypotheses_results = causality_tester.run_tests()
                    print(f"Completed Sepsis causality tests. Results saved to results/causality/sepsis")
                else:
                    print(f"Enhanced Sepsis model not found at {enhanced_dt_path}. Skipping causality tests.")
            except Exception as e:
                print(f"Error running Sepsis causality tests: {e}")
                import traceback
                traceback.print_exc()
        
        if args.dataset in ['bpi', 'all']:
            print("\n====== Running BPI Causality Tests ======")
            try:
                # Load enhanced models and test data
                enhanced_dt_path = os.path.join('models/enhanced', f"enhanced_dt_bpi.pkl")
                
                if os.path.exists(enhanced_dt_path):
                    enhanced_dt = joblib.load(enhanced_dt_path)
                    
                    # Load or generate test data
                    test_data_path = os.path.join('models/enhanced', f"test_data_bpi.pkl")
                    if os.path.exists(test_data_path):
                        test_data = joblib.load(test_data_path)
                        X_test = test_data['X_test']
                        y_test = test_data['y_test']
                        feature_names = test_data['feature_names']
                    else:
                        # Create test data by running a quick feature extraction
                        print("Test data not found. Creating from dataset...")
                        trainer = EnhancedModelTrainer(
                            log_path='dataset/DomesticDeclarations.xes',
                            dataset_type='bpi',
                            baseline_dir='models/bpi',
                            output_dir='models/enhanced'
                        )
                        X_train, X_test, y_train, y_test, feature_names = trainer.prepare_data()
                        
                        # Save test data for future use
                        joblib.dump({
                            'X_test': X_test,
                            'y_test': y_test,
                            'feature_names': feature_names
                        }, test_data_path)
                    
                    # Run causality tester
                    causality_tester = CausalityTester(
                        models={'enhanced_dt': enhanced_dt},
                        feature_names=feature_names,
                        X_test=X_test,
                        y_test=y_test,
                        dataset_type='bpi',
                        baseline_dir='models/bpi',
                        output_dir='results/causality/bpi'
                    )
                    
                    hypotheses_results = causality_tester.run_tests()
                    print(f"Completed BPI causality tests. Results saved to results/causality/bpi")
                else:
                    print(f"Enhanced BPI model not found at {enhanced_dt_path}. Skipping causality tests.")
            except Exception as e:
                print(f"Error running BPI causality tests: {e}")
                import traceback
                traceback.print_exc()
    
    # If no arguments provided, print help
    if not (args.analyze or args.train or args.train_enhanced or args.compare or args.causality):
        parser.print_help()

if __name__ == "__main__":
    main()