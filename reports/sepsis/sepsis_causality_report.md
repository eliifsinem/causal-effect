# SEPSIS Causality Analysis Report

## 1. Introduction

This report contains the results of causality analyses conducted for the sepsis dataset.

* Analysis date: 2025-04-26 18:29:15
* Models used: Decision Tree, Random Forest

## 2. Hypothesis Tests

### Decision Tree Hypothesis Results

| Hypothesis | Result | Support Rate |
|---------|-------|-------------|
| H1: Kritik tanı testleri -> belirli sonraki olaylar | ✅ SUPPORTED | 13.0% vs 0.0% |
| H2: SIRS kriterleri -> tanı testi isteme | ❌ NOT SUPPORTED | 12.3% vs 9.6% |
| H3: Departman geçişleri -> olay dizileri ve sonuçları etkileme | ❌ NOT SUPPORTED | 4.0% vs 0.0% |
| H4: Klinik belirteç değişim oranları -> sonraki olaylar | ✅ SUPPORTED | 76.5% vs 39.1% |

#### Hypothesis Details

##### H1: Kritik tanı testleri -> belirli sonraki olaylar

- **Result**: SUPPORTED
- **Description**: Test özellikleri önem düzeyi ve etkileri (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 14.7%
  - When condition is true (expected): 13.0%
  - When condition is false (calculated): 12.1%
  - When condition is false (expected): 0.0%
  - Difference (calculated): 2.6%
  - Difference (expected): 13.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H2: SIRS kriterleri -> tanı testi isteme

- **Result**: NOT SUPPORTED
- **Description**: SIRS kriterlerinin test isteme üzerindeki etkisi
- When condition is true: 12.3%
- When condition is false: 9.6%
- Difference: 2.6%

##### H3: Departman geçişleri -> olay dizileri ve sonuçları etkileme

- **Result**: NOT SUPPORTED
- **Description**: Departman geçişlerinin süreç sonuçları üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 73.3%
  - When condition is true (expected): 4.0%
  - When condition is false (calculated): 32.6%
  - When condition is false (expected): 0.0%
  - Difference (calculated): 40.7%
  - Difference (expected): 4.0%
  - Result (calculated): SUPPORTED
  - Result (expected): NOT SUPPORTED

##### H4: Klinik belirteç değişim oranları -> sonraki olaylar

- **Result**: SUPPORTED
- **Description**: Zamansal faktörlerin ve klinik değişimlerin etkisi
- When condition is true: 76.5%
- When condition is false: 39.1%
- Difference: 37.4%

### Random Forest Hypothesis Results

| Hypothesis | Result | Support Rate |
|---------|-------|-------------|
| H1: Kritik tanı testleri -> belirli sonraki olaylar | ✅ SUPPORTED | 13.0% vs 0.0% |
| H2: SIRS kriterleri -> tanı testi isteme | ❌ NOT SUPPORTED | 13.8% vs 9.6% |
| H3: Departman geçişleri -> olay dizileri ve sonuçları etkileme | ❌ NOT SUPPORTED | 4.0% vs 0.0% |
| H4: Klinik belirteç değişim oranları -> sonraki olaylar | ✅ SUPPORTED | 75.9% vs 38.5% |

#### Hypothesis Details

##### H1: Kritik tanı testleri -> belirli sonraki olaylar

- **Result**: SUPPORTED
- **Description**: Test özellikleri önem düzeyi ve etkileri (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 14.4%
  - When condition is true (expected): 13.0%
  - When condition is false (calculated): 11.9%
  - When condition is false (expected): 0.0%
  - Difference (calculated): 2.5%
  - Difference (expected): 13.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H2: SIRS kriterleri -> tanı testi isteme

- **Result**: NOT SUPPORTED
- **Description**: SIRS kriterlerinin test isteme üzerindeki etkisi
- When condition is true: 13.8%
- When condition is false: 9.6%
- Difference: 4.2%

##### H3: Departman geçişleri -> olay dizileri ve sonuçları etkileme

- **Result**: NOT SUPPORTED
- **Description**: Departman geçişlerinin süreç sonuçları üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 72.5%
  - When condition is true (expected): 4.0%
  - When condition is false (calculated): 32.2%
  - When condition is false (expected): 0.0%
  - Difference (calculated): 40.3%
  - Difference (expected): 4.0%
  - Result (calculated): SUPPORTED
  - Result (expected): NOT SUPPORTED

##### H4: Klinik belirteç değişim oranları -> sonraki olaylar

- **Result**: SUPPORTED
- **Description**: Zamansal faktörlerin ve klinik değişimlerin etkisi
- When condition is true: 75.9%
- When condition is false: 38.5%
- Difference: 37.3%

## 3. Transition Analysis

The following analyses show the transitions in event flows and the factors influencing these transitions.

### Decision Tree Transition Analysis

| Transition | Number of Examples | Important Features |
|-------|--------------|-------------------|
| Leucocytes -> CRP | 123 | current_dept_duration: μ=0.41, σ=1.41, unique_activities: μ=0.41, σ=0.77, dept_changes: μ=0.35, σ=0.75 |
| CRP -> Leucocytes | 90 | unique_activities: μ=0.21, σ=0.81, dept_changes: μ=0.20, σ=0.69, time_since_last_event: μ=0.19, σ=0.98 |
| Leucocytes -> LacticAcid | 73 | current_dept_duration: μ=0.78, σ=2.20, trace_length: μ=0.77, σ=2.05, prev_event_5: μ=-0.52, σ=0.79 |
| Leucocytes -> Admission NC | 36 | unique_activities: μ=0.75, σ=0.23, CRP_last: μ=0.60, σ=0.94, prev_event_5: μ=-0.37, σ=1.07 |
| Leucocytes -> Release A | 35 | time_since_last_event: μ=0.86, σ=1.34, prev_event_5: μ=-0.82, σ=0.77, dept_changes: μ=0.77, σ=0.63 |
| CRP -> LacticAcid | 24 | current_dept_duration: μ=0.97, σ=2.00, trace_length: μ=0.88, σ=1.89, SIRSCritLeucos_changes: μ=0.76, σ=2.42 |
| Leucocytes -> IV Liquid | 18 | unique_activities: μ=-0.89, σ=0.58, dept_changes: μ=-0.74, σ=0.25, CRP_last: μ=-0.58, σ=0.78 |
| LacticAcid -> Leucocytes | 17 | current_dept_duration: μ=0.78, σ=1.93, trace_length: μ=0.69, σ=1.80, CRP_last: μ=0.59, σ=0.94 |
| LacticAcid -> CRP | 14 | current_dept_duration: μ=0.96, σ=2.00, trace_length: μ=0.88, σ=1.78, CRP_last: μ=-0.34, σ=0.77 |
| CRP -> Admission NC | 14 | unique_activities: μ=0.64, σ=0.37, CRP_last: μ=0.60, σ=1.21, time_since_start: μ=-0.40, σ=0.11 |

#### Detailed Transition Analyses

##### Leucocytes -> CRP

Found 123 examples. Most important features:

- **time_since_start**: mean=-0.03, std=0.73
- **prev_event_5**: mean=-0.18, std=1.03
- **dept_changes**: mean=0.35, std=0.75
- **trace_length**: mean=0.30, std=1.33
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.41, std=0.77
- **SIRSCritLeucos_changes**: mean=0.21, std=0.94
- **CRP_last**: mean=0.21, std=0.98
- **time_since_last_event**: mean=0.18, std=1.01
- **current_dept_duration**: mean=0.41, std=1.41

##### CRP -> Leucocytes

Found 90 examples. Most important features:

- **time_since_start**: mean=-0.14, std=0.54
- **prev_event_5**: mean=-0.04, std=1.06
- **dept_changes**: mean=0.20, std=0.69
- **trace_length**: mean=0.06, std=0.93
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.21, std=0.81
- **SIRSCritLeucos_changes**: mean=0.02, std=0.83
- **CRP_last**: mean=0.06, std=0.85
- **time_since_last_event**: mean=0.19, std=0.98
- **current_dept_duration**: mean=0.11, std=0.98

##### Leucocytes -> LacticAcid

Found 73 examples. Most important features:

- **time_since_start**: mean=-0.17, std=0.69
- **prev_event_5**: mean=-0.52, std=0.79
- **dept_changes**: mean=0.06, std=0.91
- **trace_length**: mean=0.77, std=2.05
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.00, std=0.99
- **SIRSCritLeucos_changes**: mean=0.20, std=1.41
- **CRP_last**: mean=0.13, std=1.20
- **time_since_last_event**: mean=-0.22, std=0.34
- **current_dept_duration**: mean=0.78, std=2.20

##### Leucocytes -> Admission NC

Found 36 examples. Most important features:

- **time_since_start**: mean=-0.32, std=0.24
- **prev_event_5**: mean=-0.37, std=1.07
- **dept_changes**: mean=0.34, std=0.50
- **trace_length**: mean=-0.05, std=0.47
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.75, std=0.23
- **SIRSCritLeucos_changes**: mean=-0.02, std=0.32
- **CRP_last**: mean=0.60, std=0.94
- **time_since_last_event**: mean=-0.14, std=0.61
- **current_dept_duration**: mean=-0.07, std=0.53

##### Leucocytes -> Release A

Found 35 examples. Most important features:

- **time_since_start**: mean=0.16, std=0.72
- **prev_event_5**: mean=-0.82, std=0.77
- **dept_changes**: mean=0.77, std=0.63
- **trace_length**: mean=0.15, std=1.34
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.72, std=0.29
- **SIRSCritLeucos_changes**: mean=0.38, std=1.09
- **CRP_last**: mean=-0.16, std=0.58
- **time_since_last_event**: mean=0.86, std=1.34
- **current_dept_duration**: mean=-0.11, std=0.41

##### CRP -> LacticAcid

Found 24 examples. Most important features:

- **time_since_start**: mean=0.23, std=2.04
- **prev_event_5**: mean=0.32, std=0.90
- **dept_changes**: mean=0.54, std=0.98
- **trace_length**: mean=0.88, std=1.89
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.46, std=0.95
- **SIRSCritLeucos_changes**: mean=0.76, std=2.42
- **CRP_last**: mean=0.30, std=1.29
- **time_since_last_event**: mean=-0.23, std=0.28
- **current_dept_duration**: mean=0.97, std=2.00

##### Leucocytes -> IV Liquid

Found 18 examples. Most important features:

- **time_since_start**: mean=-0.47, std=0.02
- **prev_event_5**: mean=-0.33, std=0.51
- **dept_changes**: mean=-0.74, std=0.25
- **trace_length**: mean=-0.28, std=0.23
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=-0.89, std=0.58
- **SIRSCritLeucos_changes**: mean=-0.50, std=0.13
- **CRP_last**: mean=-0.58, std=0.78
- **time_since_last_event**: mean=-0.27, std=0.19
- **current_dept_duration**: mean=-0.26, std=0.21

##### LacticAcid -> Leucocytes

Found 17 examples. Most important features:

- **time_since_start**: mean=-0.12, std=0.71
- **prev_event_5**: mean=-0.25, std=0.98
- **dept_changes**: mean=0.12, std=0.66
- **trace_length**: mean=0.69, std=1.80
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.35, std=0.86
- **SIRSCritLeucos_changes**: mean=0.49, std=1.57
- **CRP_last**: mean=0.59, std=0.94
- **time_since_last_event**: mean=-0.32, std=0.06
- **current_dept_duration**: mean=0.78, std=1.93

##### LacticAcid -> CRP

Found 14 examples. Most important features:

- **time_since_start**: mean=-0.22, std=0.43
- **prev_event_5**: mean=-0.14, std=1.12
- **dept_changes**: mean=-0.19, std=0.65
- **trace_length**: mean=0.88, std=1.78
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=-0.05, std=0.83
- **SIRSCritLeucos_changes**: mean=-0.05, std=0.59
- **CRP_last**: mean=-0.34, std=0.77
- **time_since_last_event**: mean=-0.21, std=0.27
- **current_dept_duration**: mean=0.96, std=2.00

##### CRP -> Admission NC

Found 14 examples. Most important features:

- **time_since_start**: mean=-0.40, std=0.11
- **prev_event_5**: mean=-0.17, std=1.25
- **dept_changes**: mean=0.28, std=0.41
- **trace_length**: mean=0.07, std=0.34
- **SIRSCritLeucos**: mean=0.00, std=0.00
- **unique_activities**: mean=0.64, std=0.37
- **SIRSCritLeucos_changes**: mean=-0.15, std=0.18
- **CRP_last**: mean=0.60, std=1.21
- **time_since_last_event**: mean=0.09, std=0.76
- **current_dept_duration**: mean=-0.16, std=0.39

### Random Forest Transition Analysis

| Transition | Number of Examples | Important Features |
|-------|--------------|-------------------|
| Leucocytes -> CRP | 88 | dept_changes: μ=0.45, σ=0.81, current_dept_duration: μ=0.31, σ=1.31, trace_length: μ=0.26, σ=1.22 |
| CRP -> Leucocytes | 88 | dept_changes: μ=0.46, σ=0.78, current_dept_duration: μ=0.35, σ=1.32, trace_length: μ=0.33, σ=1.23 |
| Leucocytes -> LacticAcid | 60 | current_dept_duration: μ=1.02, σ=2.21, trace_length: μ=0.96, σ=2.06, current_event: μ=-0.41, σ=0.80 |
| Leucocytes -> Admission NC | 30 | current_event: μ=-0.88, σ=0.89, prev_event_5: μ=-0.88, σ=0.89, time_since_start: μ=-0.43, σ=0.10 |
| Leucocytes -> IV Liquid | 24 | CRP_mean: μ=-0.95, σ=0.18, CRP_last: μ=-0.83, σ=0.18, dept_changes: μ=-0.83, σ=0.13 |
| LacticAcid -> Leucocytes | 23 | current_dept_duration: μ=0.92, σ=1.87, trace_length: μ=0.90, σ=1.69, current_event: μ=-0.72, σ=0.87 |
| CRP -> LacticAcid | 22 | current_dept_duration: μ=0.67, σ=1.57, trace_length: μ=0.65, σ=1.45, dept_changes: μ=0.50, σ=0.73 |
| Leucocytes -> Release A | 16 | current_event: μ=-0.73, σ=0.92, prev_event_5: μ=-0.73, σ=0.92, dept_changes: μ=0.68, σ=0.58 |
| CRP -> IV Liquid | 16 | dept_changes: μ=-0.85, σ=0.12, CRP_mean: μ=-0.82, σ=0.61, CRP_last: μ=-0.70, σ=0.62 |
| Admission NC -> Leucocytes | 12 | time_of_day: μ=-0.67, σ=0.62, CRP_last: μ=0.56, σ=0.90, dept_changes: μ=0.47, σ=0.52 |

#### Detailed Transition Analyses

##### Leucocytes -> CRP

Found 88 examples. Most important features:

- **time_since_start**: mean=-0.02, std=0.93
- **current_event**: mean=0.20, std=1.06
- **trace_length**: mean=0.26, std=1.22
- **prev_event_5**: mean=0.20, std=1.06
- **current_dept_duration**: mean=0.31, std=1.31
- **dept_changes**: mean=0.45, std=0.81
- **time_since_last_event**: mean=-0.01, std=0.52
- **CRP_last**: mean=0.24, std=1.01
- **CRP_mean**: mean=0.14, std=0.97
- **time_of_day**: mean=-0.20, std=0.99

##### CRP -> Leucocytes

Found 88 examples. Most important features:

- **time_since_start**: mean=0.10, std=1.26
- **current_event**: mean=-0.25, std=1.09
- **trace_length**: mean=0.33, std=1.23
- **prev_event_5**: mean=-0.25, std=1.09
- **current_dept_duration**: mean=0.35, std=1.32
- **dept_changes**: mean=0.46, std=0.78
- **time_since_last_event**: mean=0.08, std=0.91
- **CRP_last**: mean=0.29, std=1.06
- **CRP_mean**: mean=0.21, std=1.03
- **time_of_day**: mean=-0.11, std=0.95

##### Leucocytes -> LacticAcid

Found 60 examples. Most important features:

- **time_since_start**: mean=-0.13, std=0.70
- **current_event**: mean=-0.41, std=0.80
- **trace_length**: mean=0.96, std=2.06
- **prev_event_5**: mean=-0.41, std=0.80
- **current_dept_duration**: mean=1.02, std=2.21
- **dept_changes**: mean=-0.04, std=0.82
- **time_since_last_event**: mean=-0.19, std=0.32
- **CRP_last**: mean=0.37, std=1.26
- **CRP_mean**: mean=0.28, std=1.20
- **time_of_day**: mean=-0.15, std=0.99

##### Leucocytes -> Admission NC

Found 30 examples. Most important features:

- **time_since_start**: mean=-0.43, std=0.10
- **current_event**: mean=-0.88, std=0.89
- **trace_length**: mean=-0.22, std=0.27
- **prev_event_5**: mean=-0.88, std=0.89
- **current_dept_duration**: mean=-0.35, std=0.23
- **dept_changes**: mean=0.03, std=0.29
- **time_since_last_event**: mean=-0.26, std=0.21
- **CRP_last**: mean=0.27, std=0.67
- **CRP_mean**: mean=0.14, std=0.67
- **time_of_day**: mean=0.35, std=1.37

##### Leucocytes -> IV Liquid

Found 24 examples. Most important features:

- **time_since_start**: mean=-0.48, std=0.00
- **current_event**: mean=-0.36, std=0.25
- **trace_length**: mean=-0.34, std=0.18
- **prev_event_5**: mean=-0.36, std=0.25
- **current_dept_duration**: mean=-0.31, std=0.03
- **dept_changes**: mean=-0.83, std=0.13
- **time_since_last_event**: mean=-0.34, std=0.00
- **CRP_last**: mean=-0.83, std=0.18
- **CRP_mean**: mean=-0.95, std=0.18
- **time_of_day**: mean=0.56, std=0.85

##### LacticAcid -> Leucocytes

Found 23 examples. Most important features:

- **time_since_start**: mean=0.03, std=0.72
- **current_event**: mean=-0.72, std=0.87
- **trace_length**: mean=0.90, std=1.69
- **prev_event_5**: mean=-0.72, std=0.87
- **current_dept_duration**: mean=0.92, std=1.87
- **dept_changes**: mean=0.52, std=0.67
- **time_since_last_event**: mean=-0.18, std=0.32
- **CRP_last**: mean=0.50, std=1.16
- **CRP_mean**: mean=0.53, std=1.07
- **time_of_day**: mean=-0.42, std=0.82

##### CRP -> LacticAcid

Found 22 examples. Most important features:

- **time_since_start**: mean=-0.18, std=0.76
- **current_event**: mean=0.40, std=1.02
- **trace_length**: mean=0.65, std=1.45
- **prev_event_5**: mean=0.40, std=1.02
- **current_dept_duration**: mean=0.67, std=1.57
- **dept_changes**: mean=0.50, std=0.73
- **time_since_last_event**: mean=-0.30, std=0.08
- **CRP_last**: mean=0.29, std=1.18
- **CRP_mean**: mean=0.25, std=1.13
- **time_of_day**: mean=0.26, std=1.44

##### Leucocytes -> Release A

Found 16 examples. Most important features:

- **time_since_start**: mean=0.12, std=0.64
- **current_event**: mean=-0.73, std=0.92
- **trace_length**: mean=0.24, std=1.78
- **prev_event_5**: mean=-0.73, std=0.92
- **current_dept_duration**: mean=-0.14, std=0.31
- **dept_changes**: mean=0.68, std=0.58
- **time_since_last_event**: mean=0.59, std=1.52
- **CRP_last**: mean=-0.43, std=0.40
- **CRP_mean**: mean=-0.22, std=0.51
- **time_of_day**: mean=-0.28, std=0.94

##### CRP -> IV Liquid

Found 16 examples. Most important features:

- **time_since_start**: mean=-0.48, std=0.00
- **current_event**: mean=-0.30, std=0.38
- **trace_length**: mean=-0.28, std=0.33
- **prev_event_5**: mean=-0.30, std=0.38
- **current_dept_duration**: mean=-0.32, std=0.05
- **dept_changes**: mean=-0.85, std=0.12
- **time_since_last_event**: mean=-0.34, std=0.01
- **CRP_last**: mean=-0.70, std=0.62
- **CRP_mean**: mean=-0.82, std=0.61
- **time_of_day**: mean=0.52, std=0.82

##### Admission NC -> Leucocytes

Found 12 examples. Most important features:

- **time_since_start**: mean=-0.18, std=0.23
- **current_event**: mean=-0.02, std=1.19
- **trace_length**: mean=-0.07, std=0.16
- **prev_event_5**: mean=-0.02, std=1.19
- **current_dept_duration**: mean=-0.07, std=0.25
- **dept_changes**: mean=0.47, std=0.52
- **time_since_last_event**: mean=-0.32, std=0.03
- **CRP_last**: mean=0.56, std=0.90
- **CRP_mean**: mean=0.43, std=0.93
- **time_of_day**: mean=-0.67, std=0.62

## 4. Conclusion and Evaluation

This analysis aimed to uncover causal relationships in business processes using process mining and machine learning methods.

### Supported Hypotheses

The following hypotheses were supported by the analysis:

- H1
- H4

### Unsupported Hypotheses

The following hypotheses were not sufficiently supported by the analysis:

- H3
- H2

### Conclusion

The analysis of process data provides valuable insights for understanding causal relationships within processes. These analyses can be used to improve process performance and increase process efficiency.
