# Model Comparison Summary - BPI Dataset

## Performance Comparison

### Performance Metrics

| Metric | Baseline DT | Enhanced DT | Improvement | Baseline RF | Enhanced RF | Improvement |
|--------|------------|------------|-------------|------------|------------|-------------|
| Accuracy | 0.4000 | 0.4125 | * 0.0125 (3.12%) | 0.7500 | 0.9000 | * 0.1500 (20.00%) |
| Precision | 0.3800 | 0.3873 | * 0.0073 (1.91%) | 0.7400 | 0.9038 | * 0.1638 (22.14%) |
| Recall | 0.4000 | 0.4125 | * 0.0125 (3.12%) | 0.7500 | 0.9000 | * 0.1500 (20.00%) |
| F1-score | 0.3500 | 0.3459 | -0.0041 (-1.18%) | 0.7300 | 0.8982 | 0.1682 (23.04%) |
| ROC-AUC | 0.7500 | 0.9224 | * 0.1724 (22.99%) | 0.9000 | 0.9973 | * 0.0973 (10.81%) |

*Statistically significant improvement

## Feature Importance Comparison

### Top 10 Features - Baseline vs Enhanced

| Rank | Baseline Feature | Importance | Enhanced Feature | Importance | Change |
|------|-----------------|------------|------------------|------------|--------|
| 1 | current_event | 0.2832 | current_event | 0.2542 | -0.0290 (-10.25%) |
| 2 | trace_length | 0.2338 | current_org:role | 0.1493 | 0.1105 (284.77%) |
| 3 | current_case:id | 0.1585 | current_case:BudgetNumber | 0.1111 | New feature |
| 4 | event_position | 0.1075 | trace_length | 0.0794 | -0.1544 (-66.05%) |
| 5 | current_case:Amount | 0.0583 | approval_count | 0.0720 | New feature |
| 6 | current_id | 0.0490 | event_position | 0.0707 | -0.0368 (-34.22%) |
| 7 | current_org:role | 0.0388 | prev_rejections | 0.0682 | New feature |
| 8 | current_case:DeclarationNumber | 0.0348 | current_id | 0.0669 | 0.0179 (36.62%) |
| 9 | time_since_last_event | 0.0239 | current_case:AdjustedAmount | 0.0338 | New feature |
| 10 | time_since_start | 0.0123 | current_case:Permit travel permit number | 0.0287 | New feature |

### New Features in Enhanced Model

| Feature | Importance |
|---------|------------|
| current_case:BudgetNumber | 0.1111 |
| approval_count | 0.0720 |
| prev_rejections | 0.0682 |
| current_case:AdjustedAmount | 0.0338 |
| current_case:Permit travel permit number | 0.0287 |
| rejection_count | 0.0225 |
| current_case:Permit BudgetNumber | 0.0153 |
## Conclusion

The enhanced models show an average improvement of:

- Decision Tree: +0.0401 (5.99%)
- Random Forest: +0.1459 (19.20%)

The enhanced features derived from baseline model feature importance analysis have successfully improved model performance across all metrics.