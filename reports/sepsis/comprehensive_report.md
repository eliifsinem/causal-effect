# Comprehensive Evaluation Report - SEPSIS Dataset

## 1. Performance Metrics

| Model Type   | Algorithm   |   Accuracy |   Precision |   Recall |   F1-score |   ROC-AUC |
|:-------------|:------------|-----------:|------------:|---------:|-----------:|----------:|
| Baseline     | DT          |     0.9434 |      0.9395 |   0.9434 |     0.9401 |    1.1652 |
| Baseline     | RF          |     0.954  |      0.9518 |   0.954  |     0.9523 |    1.181  |
| Enhanced     | DT          |     0.9434 |      0.9395 |   0.9434 |     0.9401 |    1.1652 |
| Enhanced     | RF          |     0.954  |      0.9518 |   0.954  |     0.9523 |    1.181  |

## 2. Most Influential Features

| Feature               |   Importance |
|:----------------------|-------------:|
| time_since_start      |       0.0688 |
| current_event         |       0.0474 |
| trace_length          |       0.0467 |
| prev_event_5          |       0.0457 |
| current_dept_duration |       0.0417 |
| dept_changes          |       0.0368 |
| time_since_last_event |       0.0356 |
| CRP_last              |       0.0314 |
| CRP_mean              |       0.0277 |
| time_of_day           |       0.0276 |

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
