# Decision Tree Comparison - BPI Dataset

## Model Performance

- Baseline Model (control-flow features only): 0.2506
- Enhanced Model (with causal features): 0.2505
- Improvement: -0.0001

## Baseline Model Features

- current_event
- event_position
- trace_length

## Enhanced Model Features (Control-flow + Causal)

### Control-flow Features
- current_event
- event_position
- trace_length

### Causal Features
- time_since_start
- time_since_last_event
- current_org:role

## Feature Importance in Enhanced Model (Top 10)

- current_event: 0.6451
- event_position: 0.3341
- time_since_last_event: 0.0127
- time_since_start: 0.0061
- current_org:role: 0.0020
- trace_length: 0.0000
