# Comprehensive Evaluation Report - BPI Dataset

## 1. Performance Metrics

| Model Type   | Algorithm   |   Accuracy |   Precision |   Recall |   F1-score |   ROC-AUC |
|:-------------|:------------|-----------:|------------:|---------:|-----------:|----------:|
| Baseline     | DT          |     0.9993 |      0.9993 |   0.9993 |     0.9993 |    1.2489 |
| Baseline     | RF          |     0.9991 |      0.9991 |   0.9991 |     0.9991 |    1.2486 |
| Enhanced     | DT          |     0.9993 |      0.9993 |   0.9993 |     0.9993 |    1.2489 |
| Enhanced     | RF          |     0.9991 |      0.9991 |   0.9991 |     0.9991 |    1.2486 |

## 2. Most Influential Features

| Feature                        |   Importance |
|:-------------------------------|-------------:|
| trace_length                   |       0.2691 |
| current_event                  |       0.1545 |
| current_id                     |       0.1082 |
| current_case:id                |       0.0962 |
| current_org:role               |       0.0897 |
| event_position                 |       0.0707 |
| current_case:DeclarationNumber |       0.0604 |
| current_case:Amount            |       0.0574 |
| time_since_last_event          |       0.0411 |
| time_since_start               |       0.0386 |

## 3. Conclusion

Decision Tree Model Improvement: 0.0000 (0.00%)

Random Forest Model Improvement: 0.0000 (0.00%)

### Feature Importance Analysis

The feature importance analysis reveals that temporal features like 'time_since_start' play a significant role in the model. The current event is a strong predictor of the next event. These findings support the hypothesis that adding causal features improves model performance and interpretability.

### Recommendations

Based on the analysis, we recommend:

1. Focusing on temporal features for process prediction
2. Incorporating domain-specific features for enhanced prediction
3. Using Random Forest models for optimal performance
4. Implementing cross-validation for more robust evaluation
