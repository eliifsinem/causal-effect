# Causality Prediction with Process Mining

This project combines process mining and machine learning to predict next events in business processes and analyze causal relationships between process elements. It supports multiple datasets, including Sepsis medical treatment processes and Business Process Intelligence (BPI) challenge datasets.

## Project Overview

The project has two main goals:
1. **Next Event Prediction**: Using machine learning to predict the next event in a business process
2. **Causality Analysis**: Identifying causal relationships between process elements and testing hypotheses about process behavior

## Project Structure

```
causality-prediction/
├── dataset/               # Event log datasets (XES files)
│   ├── Sepsis.xes         # Sepsis Cases - Medical processes
│   └── DomesticDeclarations.xes # BPI Challenge - Declaration processes
├── models/                # Trained model files
│   ├── sepsis/           # Sepsis-specific models
│   │   ├── decision_tree  # Decision Tree model for Sepsis
│   │   ├── random_forest  # Random Forest model for Sepsis
│   │   └── ensemble       # Ensemble model configuration
│   └── bpi/              # BPI-specific models
│       ├── decision_tree  # Decision Tree model for BPI
│       ├── random_forest  # Random Forest model for BPI
│       └── ensemble       # Ensemble model configuration
├── reports/               # Analysis reports and visualizations
│   ├── sepsis/           # Sepsis analysis reports
│   │   └── sepsis_causality_report.md  # Causality analysis for Sepsis
│   └── bpi/              # BPI analysis reports
│       └── bpi_causality_report.md     # Causality analysis for BPI
├── src/                   # Source code
│   ├── analysis/          # Process mining analysis code
│   │   ├── pm_analyzer.py # Process mining analyzer
│   │   └── process_mining.py # Process mining utilities
│   ├── causality/         # Causality relationship extraction
│   │   ├── bpi_hypothesis.py  # BPI-specific hypotheses
│   │   ├── causality_analyzer.py # Core causality analysis
│   │   ├── hypothesis_testing.py # Hypothesis testing framework
│   │   └── sepsis_hypothesis.py # Sepsis-specific hypotheses
│   ├── common/            # Common utilities
│   │   ├── constants.py   # Project constants
│   │   └── utils.py       # Shared utility functions
│   ├── evaluation/        # Model evaluation code
│   │   └── evaluator.py   # Model evaluation utilities
│   ├── models/            # Model definitions
│   │   ├── dt_model.py    # Decision Tree model
│   │   ├── ensemble.py    # Ensemble model
│   │   └── rf_model.py    # Random Forest model
│   ├── pipelines/         # End-to-end pipelines
│   │   ├── analysis_pipeline.py # Analysis pipeline
│   │   ├── bpi_pipeline.py # BPI-specific pipeline
│   │   ├── pipeline.py    # Base pipeline class
│   │   ├── sepsis_pipeline.py # Sepsis-specific pipeline
│   │   └── training_pipeline.py # Model training pipeline
│   └── preprocessing/     # Data preprocessing code
│       ├── feature_extraction.py # Feature extraction utilities
│       ├── preprocessor.py # Core preprocessing logic
│       └── xes_reader.py  # XES file reader
├── main.py                # Main entry point
└── requirements.txt       # Python dependencies
```

## Core Pipelines

### 1. Analysis Pipeline

The analysis pipeline performs process mining on event logs to extract patterns and insights:

1. **Data Loading**: Reads XES event logs
2. **Process Discovery**: Applies alpha miner and heuristic miner algorithms
3. **Directly Follows Graph**: Generates DFG visualization
4. **Statistics Extraction**: Calculates process metrics and statistics

### 2. Training Pipeline

The training pipeline builds and evaluates prediction models:

1. **Data Loading**: Reads XES event logs
2. **Preprocessing**: 
   - Feature extraction (temporal, sequential, domain-specific)
   - Categorical encoding
   - Data normalization
   - Train/test splitting
3. **Model Training**:
   - Decision Tree model training
   - Random Forest model training
   - Ensemble model creation
4. **Evaluation**:
   - Performance metrics calculation
   - Model saving
5. **Causality Analysis**:
   - Transition cause analysis
   - Hypothesis testing

## Dataset-Specific Pipelines

### Sepsis Pipeline

This pipeline is specialized for medical process data:

1. **Medical Feature Extraction**:
   - SIRS criteria tracking
   - Clinical markers (CRP, Leucocytes, LacticAcid)
   - Department transitions
   - Time-based patterns

2. **Sepsis Hypotheses**:
   - H1: Critical diagnostic tests affecting subsequent events
   - H2: SIRS criteria affecting diagnostic test ordering
   - H3: Department transitions affecting event sequences
   - H4: Clinical marker change rates affecting subsequent events

### BPI Pipeline

This pipeline is specialized for business declaration processes:

1. **Business Feature Extraction**:
   - Declaration amounts
   - Organizational roles
   - Approval/rejection patterns
   - Process complexity metrics

2. **BPI Hypotheses**:
   - H1: Previous rejections leading to more scrutiny
   - H2: Prior approvals speeding up subsequent approvals
   - H3: Complex processes increasing management oversight
   - H4: Previous activity features affecting next steps
   - H5: Resource changes affecting control mechanisms
   - H6: Temporal factors affecting workflow

## Causality Analysis Approach

Our causality analysis consists of two main components:

1. **Transition Cause Analysis**:
   - Identifies patterns in features that lead to specific transitions
   - Uses model feature importance to determine which factors influence transitions
   - Normalizes and aggregates feature values to find common patterns

2. **Hypothesis Testing**:
   - Tests domain-specific hypotheses about process behavior
   - Compares outcomes between groups where a condition is true vs. false
   - Calculates percentage differences to determine hypothesis support
   - Considers a difference significant if it exceeds 10%

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/causality-prediction.git
cd causality-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your XES event log files in the `dataset/` directory.

## Usage

### Process Mining Analysis

For process mining analysis on the event logs:

```bash
python main.py --analyze --dataset all --train
```

### Training and Causality Analysis

To train prediction models and run causality analysis:

```bash
python main.py --train --dataset all
```

You can specify which dataset to use:
- `--dataset sepsis`: Train on Sepsis data only
- `--dataset bpi`: Train on BPI data only
- `--dataset all`: Train on all available datasets

## Key Findings

### Sepsis Dataset
- Critical diagnostic tests (H1) and clinical marker change rates (H4) significantly influence the process flow
- Department transitions and SIRS criteria have limited impact on process outcomes
- Key transitions like Leucocytes → CRP and LacticAcid → Leucocytes show strong feature patterns

### BPI Dataset
- Prior approvals significantly speed up subsequent approvals (H2)
- Complex processes increase management oversight (H3)
- Activity features (H4) and resource changes (H5) strongly influence process flow
- Previous rejections and temporal factors have limited impact on declaration outcomes
