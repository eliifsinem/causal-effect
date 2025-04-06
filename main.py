import os
import argparse
from src.pipelines.model_trainer import train_sepsis_models, train_bpi_models
from src.analysis.process_mining import analyze_event_logs

def setup_directories():
    """Create necessary directories if they don't exist"""
    directories = [
        'dataset',
        'models',
        'models/sepsis',
        'models/bpi',
        'reports',
        'reports/sepsis',
        'reports/bpi',
        os.path.join('src', 'result', 'dataset_analysis')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    """Main entry point for the application"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process Mining and Event Prediction')
    parser.add_argument('--analyze', action='store_true', help='Run process mining analysis')
    parser.add_argument('--train', action='store_true', help='Train prediction models')
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
    
    # Model Training
    if args.train:
        print("Running Model Training...")
        
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
    
    # If no arguments provided, print help
    if not (args.analyze or args.train):
        parser.print_help()

if __name__ == "__main__":
    main()