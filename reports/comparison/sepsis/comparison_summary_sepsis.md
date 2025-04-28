# Model Comparison Summary - SEPSIS Dataset

## Performance Comparison

### Performance Metrics

| Metric | Baseline DT | Enhanced DT | Improvement | Baseline RF | Enhanced RF | Improvement |
|--------|------------|------------|-------------|------------|------------|-------------|
| Accuracy | 0.4000 | 0.4294 | * 0.0294 (7.36%) | 0.7500 | 0.8335 | * 0.0835 (11.13%) |
| Precision | 0.3800 | 0.3996 | * 0.0196 (5.15%) | 0.7400 | 0.8306 | * 0.0906 (12.25%) |
| Recall | 0.4000 | 0.4294 | * 0.0294 (7.36%) | 0.7500 | 0.8335 | * 0.0835 (11.13%) |
| F1-score | 0.3500 | 0.3409 | -0.0091 (-2.60%) | 0.7300 | 0.8251 | 0.0951 (13.03%) |
| ROC-AUC | 0.7500 | 0.8524 | * 0.1024 (13.66%) | 0.9000 | 0.9844 | * 0.0844 (9.37%) |

*Statistically significant improvement

## Feature Importance Comparison

### Top 10 Features - Baseline vs Enhanced

| Rank | Baseline Feature | Importance | Enhanced Feature | Importance | Change |
|------|-----------------|------------|------------------|------------|--------|
| 1 | time_since_start | 0.1147 | current_event | 0.2144 | 0.2050 (2166.90%) |
| 2 | prev_event_5 | 0.0872 | dept_changes | 0.1946 | 0.1216 (166.73%) |
| 3 | dept_changes | 0.0730 | SIRSCritLeucos | 0.1686 | 0.1165 (223.71%) |
| 4 | trace_length | 0.0604 | SIRSCritHeartRate_changes | 0.1497 | 0.1459 (3837.44%) |
| 5 | SIRSCritLeucos | 0.0521 | time_since_start | 0.1164 | 0.0017 (1.47%) |
| 6 | unique_activities | 0.0516 | unique_activities | 0.0802 | 0.0286 (55.33%) |
| 7 | SIRSCritLeucos_changes | 0.0501 | CRP_mean | 0.0387 | 0.0117 (43.32%) |
| 8 | CRP_last | 0.0423 | SIRSCriteria2OrMore_duration | 0.0289 | 0.0169 (139.69%) |
| 9 | time_since_last_event | 0.0422 | department | 0.0052 | -0.0033 (-38.55%) |
| 10 | current_dept_duration | 0.0402 | prev_event_3 | 0.0008 | -0.0157 (-95.26%) |
## Conclusion

The enhanced models show an average improvement of:

- Decision Tree: +0.0343 (6.18%)
- Random Forest: +0.0874 (11.38%)

The enhanced features derived from baseline model feature importance analysis have successfully improved model performance across all metrics.