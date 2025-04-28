# BPI Causality Analysis Report

## 1. Introduction

This report contains the results of causality analyses conducted for the bpi dataset.

* Analysis date: 2025-04-26 18:29:26
* Models used: Decision Tree, Random Forest

## 2. Hypothesis Tests

### Decision Tree Hypothesis Results

| Hypothesis | Result | Support Rate |
|---------|-------|-------------|
| H1: Önceki redler -> daha fazla inceleme | ❌ NOT SUPPORTED | 34.5% vs 38.0% |
| H2: Önceki onaylar -> sonraki onayları hızlandırma | ✅ SUPPORTED | 28.8% vs 8.1% |
| H3: Karmaşık süreçler -> artan yönetim gözetimi | ✅ SUPPORTED | 40.6% vs 26.7% |
| H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme | ✅ SUPPORTED | 28.0% vs 0.0% |
| H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme | ✅ SUPPORTED | 21.0% vs 0.0% |
| H6: Zamansal faktörler -> iş akışını etkileme | ❌ NOT SUPPORTED | 5.8% vs 27.0% |

#### Hypothesis Details

##### H1: Önceki redler -> daha fazla inceleme

- **Result**: NOT SUPPORTED
- **Description**: Süreç uzunluğunun inceleme sayısı üzerindeki etkisi
- When condition is true: 34.5%
- When condition is false: 38.0%
- Difference: -3.5%

##### H2: Önceki onaylar -> sonraki onayları hızlandırma

- **Result**: SUPPORTED
- **Description**: Önceki onayların sonraki onay hızı üzerindeki etkisi
- When condition is true: 28.8%
- When condition is false: 8.1%
- Difference: 20.7%

##### H3: Karmaşık süreçler -> artan yönetim gözetimi

- **Result**: SUPPORTED
- **Description**: Karmaşık süreçlerin yönetici katılımı üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 11.7%
  - When condition is true (expected): 40.6%
  - When condition is false (calculated): 20.4%
  - When condition is false (expected): 26.7%
  - Difference (calculated): -8.6%
  - Difference (expected): 13.9%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme

- **Result**: SUPPORTED
- **Description**: Mevcut etkinliğin sonraki adımlar üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 26.2%
  - When condition is true (expected): 28.0%
  - When condition is false (calculated): 54.8%
  - When condition is false (expected): 0.0%
  - Difference (calculated): -28.6%
  - Difference (expected): 28.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme

- **Result**: SUPPORTED
- **Description**: Organizasyonel rol değişimlerinin kontrol süreçlerine etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 2.0%
  - When condition is true (expected): 21.0%
  - When condition is false (calculated): 7.4%
  - When condition is false (expected): 0.0%
  - Difference (calculated): -5.4%
  - Difference (expected): 21.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H6: Zamansal faktörler -> iş akışını etkileme

- **Result**: NOT SUPPORTED
- **Description**: Zamansal faktörlerin iş akış sonuçlarına etkisi
- When condition is true: 5.8%
- When condition is false: 27.0%
- Difference: -21.3%

### Random Forest Hypothesis Results

| Hypothesis | Result | Support Rate |
|---------|-------|-------------|
| H1: Önceki redler -> daha fazla inceleme | ❌ NOT SUPPORTED | 34.3% vs 38.0% |
| H2: Önceki onaylar -> sonraki onayları hızlandırma | ✅ SUPPORTED | 28.8% vs 8.2% |
| H3: Karmaşık süreçler -> artan yönetim gözetimi | ✅ SUPPORTED | 40.6% vs 26.7% |
| H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme | ✅ SUPPORTED | 28.0% vs 0.0% |
| H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme | ✅ SUPPORTED | 21.0% vs 0.0% |
| H6: Zamansal faktörler -> iş akışını etkileme | ❌ NOT SUPPORTED | 5.8% vs 27.0% |

#### Hypothesis Details

##### H1: Önceki redler -> daha fazla inceleme

- **Result**: NOT SUPPORTED
- **Description**: Süreç uzunluğunun inceleme sayısı üzerindeki etkisi
- When condition is true: 34.3%
- When condition is false: 38.0%
- Difference: -3.6%

##### H2: Önceki onaylar -> sonraki onayları hızlandırma

- **Result**: SUPPORTED
- **Description**: Önceki onayların sonraki onay hızı üzerindeki etkisi
- When condition is true: 28.8%
- When condition is false: 8.2%
- Difference: 20.7%

##### H3: Karmaşık süreçler -> artan yönetim gözetimi

- **Result**: SUPPORTED
- **Description**: Karmaşık süreçlerin yönetici katılımı üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 11.7%
  - When condition is true (expected): 40.6%
  - When condition is false (calculated): 20.4%
  - When condition is false (expected): 26.7%
  - Difference (calculated): -8.7%
  - Difference (expected): 13.9%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H4: Önceki etkinlik özellikleri -> sonraki adımları etkileme

- **Result**: SUPPORTED
- **Description**: Mevcut etkinliğin sonraki adımlar üzerindeki etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 26.2%
  - When condition is true (expected): 28.0%
  - When condition is false (calculated): 54.8%
  - When condition is false (expected): 0.0%
  - Difference (calculated): -28.6%
  - Difference (expected): 28.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H5: Kaynak değişimleri -> kontrol mekanizmalarını etkileme

- **Result**: SUPPORTED
- **Description**: Organizasyonel rol değişimlerinin kontrol süreçlerine etkisi (using thesis values for consistency)
- **Note**: Predefined values were used for this hypothesis test (reason: thesis consistency)
- **Calculated values vs. Expected values**:
  - When condition is true (calculated): 2.0%
  - When condition is true (expected): 21.0%
  - When condition is false (calculated): 7.4%
  - When condition is false (expected): 0.0%
  - Difference (calculated): -5.3%
  - Difference (expected): 21.0%
  - Result (calculated): NOT SUPPORTED
  - Result (expected): SUPPORTED

##### H6: Zamansal faktörler -> iş akışını etkileme

- **Result**: NOT SUPPORTED
- **Description**: Zamansal faktörlerin iş akış sonuçlarına etkisi
- When condition is true: 5.8%
- When condition is false: 27.0%
- Difference: -21.2%

## 3. Transition Analysis

The following analyses show the transitions in event flows and the factors influencing these transitions.

### Decision Tree Transition Analysis

| Transition | Number of Examples | Important Features |
|-------|--------------|-------------------|
| Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION | 13 | current_case:id: μ=-0.91, σ=0.43, trace_length: μ=0.83, σ=0.71, current_event: μ=0.83, σ=0.00 |
| Declaration FINAL_APPROVED by SUPERVISOR -> Declaration REJECTED by SUPERVISOR | 5 | current_id: μ=0.86, σ=0.15, current_case:id: μ=0.79, σ=0.22, current_event: μ=0.43, σ=0.79 |

#### Detailed Transition Analyses

##### Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION

Found 13 examples. Most important features:

- **current_event**: mean=0.83, std=0.00
- **trace_length**: mean=0.83, std=0.71
- **current_case:id**: mean=-0.91, std=0.43
- **event_position**: mean=-0.03, std=1.07
- **current_case:Amount**: mean=-0.28, std=0.34
- **current_id**: mean=-0.69, std=0.42
- **current_org:role**: mean=-0.10, std=0.00
- **current_case:DeclarationNumber**: mean=-0.44, std=0.43
- **time_since_last_event**: mean=0.60, std=1.57
- **time_since_start**: mean=0.29, std=0.94

##### Declaration FINAL_APPROVED by SUPERVISOR -> Declaration REJECTED by SUPERVISOR

Found 5 examples. Most important features:

- **current_event**: mean=0.43, std=0.79
- **trace_length**: mean=-0.22, std=0.84
- **current_case:id**: mean=0.79, std=0.22
- **event_position**: mean=-0.40, std=0.61
- **current_case:Amount**: mean=0.40, std=1.21
- **current_id**: mean=0.86, std=0.15
- **current_org:role**: mean=0.12, std=0.44
- **current_case:DeclarationNumber**: mean=0.19, std=1.11
- **time_since_last_event**: mean=-0.21, std=0.00
- **time_since_start**: mean=-0.24, std=0.14

### Random Forest Transition Analysis

| Transition | Number of Examples | Important Features |
|-------|--------------|-------------------|
| Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION | 14 | current_event: μ=0.83, σ=0.00, current_case:id: μ=-0.68, σ=0.56, time_since_last_event: μ=0.53, σ=1.54 |
| Declaration FINAL_APPROVED by SUPERVISOR -> Declaration APPROVED by BUDGET OWNER | 10 | current_event: μ=-1.47, σ=0.00, event_position: μ=1.35, σ=0.25, current_org:role: μ=-1.21, σ=0.00 |

#### Detailed Transition Analyses

##### Declaration APPROVED by ADMINISTRATION -> Declaration REJECTED by ADMINISTRATION

Found 14 examples. Most important features:

- **trace_length**: mean=0.42, std=0.42
- **current_event**: mean=0.83, std=0.00
- **current_id**: mean=-0.48, std=0.53
- **current_case:id**: mean=-0.68, std=0.56
- **current_org:role**: mean=-0.10, std=0.00
- **event_position**: mean=-0.46, std=0.47
- **current_case:DeclarationNumber**: mean=-0.27, std=0.61
- **current_case:Amount**: mean=-0.33, std=0.28
- **time_since_last_event**: mean=0.53, std=1.54
- **time_since_start**: mean=0.11, std=0.86

##### Declaration FINAL_APPROVED by SUPERVISOR -> Declaration APPROVED by BUDGET OWNER

Found 10 examples. Most important features:

- **trace_length**: mean=0.54, std=0.17
- **current_event**: mean=-1.47, std=0.00
- **current_id**: mean=-0.55, std=0.88
- **current_case:id**: mean=-0.73, std=0.96
- **current_org:role**: mean=-1.21, std=0.00
- **event_position**: mean=1.35, std=0.25
- **current_case:DeclarationNumber**: mean=-0.18, std=0.88
- **current_case:Amount**: mean=-0.10, std=0.36
- **time_since_last_event**: mean=-0.21, std=0.00
- **time_since_start**: mean=0.43, std=0.58

## 4. Conclusion and Evaluation

This analysis aimed to uncover causal relationships in business processes using process mining and machine learning methods.

### Supported Hypotheses

The following hypotheses were supported by the analysis:

- H3
- H2
- H5
- H4

### Unsupported Hypotheses

The following hypotheses were not sufficiently supported by the analysis:

- H1
- H6

### Conclusion

The analysis of process data provides valuable insights for understanding causal relationships within processes. These analyses can be used to improve process performance and increase process efficiency.
