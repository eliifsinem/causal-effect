# Decision Tree Comparison - SEPSIS Dataset

## Model Performance

- Baseline Model (control-flow features only): 0.3973
- Enhanced Model (with causal features): 0.3535
- Improvement: -0.0438

## Baseline Model Features

- current_event
- event_position
- trace_length
- repeated_activities
- unique_activities

## Enhanced Model Features (Control-flow + Causal)

### Control-flow Features
- current_event
- event_position
- trace_length
- repeated_activities
- unique_activities

### Causal Features
- CRP_last
- Leucocytes_last
- LacticAcid_last
- SIRSCritLeucos
- SIRSCritTemperature
- dept_changes
- time_since_start

## Feature Importance in Enhanced Model (Top 10)

- current_event: 0.2487
- dept_changes: 0.2257
- SIRSCritLeucos: 0.2147
- event_position: 0.1732
- time_since_start: 0.1335
- Leucocytes_last: 0.0041
- trace_length: 0.0002
- repeated_activities: 0.0000
- unique_activities: 0.0000
- CRP_last: 0.0000
