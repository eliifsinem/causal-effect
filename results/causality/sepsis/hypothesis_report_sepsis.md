# Causality Analysis Report - SEPSIS Dataset

Generated on: 2025-04-26 18:38:32

## Summary of Hypothesis Testing

| ID | Hypothesis | Supported | Significance |
|----|-----------|-----------|--------------|
| H7 | Critical Diagnostic Tests → Specific Events | ❌ | p = 0.2132 |
| H8 | SIRS Criteria → Diagnostic Testing | ❌ | p = 0.0000 |
| H9 | Department Transitions → Outcome Events | ❌ | p = nan |
| H10 | Clinical Marker Changes → Next Events | ❌ | p = 0.0000 |

## Detailed Results

### H7: Critical Diagnostic Tests → Specific Events

**Features examined**: CRP_last, Leucocytes_last

**Target events**: Release A, Admission NC

**Result**: NOT SUPPORTED

**Justification**: Features related to Critical Diagnostic Tests showed insufficient influence on predictions for Specific Events events, with only 0.01 importance vs. 0.02 average for other features.

**Analysis Details**:

- Hypothesis Feature Importance: 0.0091
- Other Features Average Importance: 0.0177
- Statistical Significance: p-value = 0.2132

**Feature Importance Breakdown**:

| Feature | Importance |
|---------|------------|
| CRP_last | 0.0091 |
| Leucocytes_last | 0.0000 |

### H8: SIRS Criteria → Diagnostic Testing

**Features examined**: SIRSCritTemperature, SIRSCritLeucos

**Target events**: CRP, Leucocytes, LacticAcid

**Result**: NOT SUPPORTED

**Justification**: Features related to SIRS Criteria showed insufficient influence on predictions for Diagnostic Testing events, with only 0.00 importance vs. 0.02 average for other features.

**Analysis Details**:

- Hypothesis Feature Importance: 0.0000
- Other Features Average Importance: 0.0179
- Statistical Significance: p-value = 0.0000

**Feature Importance Breakdown**:

| Feature | Importance |
|---------|------------|
| SIRSCritTemperature | 0.0000 |
| SIRSCritLeucos | 0.0000 |

### H9: Department Transitions → Outcome Events

**Features examined**: dept_changes, current_dept

**Target events**: Return ER, Admission NC, Admission IC

**Result**: NOT SUPPORTED

**Justification**: Features related to Department Transitions showed insufficient influence on predictions for Outcome Events events, with only 0.00 importance vs. 0.02 average for other features.

**Analysis Details**:

- Hypothesis Feature Importance: 0.0000
- Other Features Average Importance: 0.0175
- Statistical Significance: p-value = nan

**Feature Importance Breakdown**:

| Feature | Importance |
|---------|------------|
| dept_changes | 0.0000 |

### H10: Clinical Marker Changes → Next Events

**Features examined**: CRP_change, CRP_change_rate, Leucocytes_change, Leucocytes_change_rate, LacticAcid_change, LacticAcid_change_rate

**Target events**: IV Antibiotics, IV Liquid, Release A

**Result**: NOT SUPPORTED

**Justification**: Features related to Clinical Marker Changes showed insufficient influence on predictions for Next Events events, with only 0.00 importance vs. 0.02 average for other features.

**Analysis Details**:

- Hypothesis Feature Importance: 0.0009
- Other Features Average Importance: 0.0192
- Statistical Significance: p-value = 0.0000

**Feature Importance Breakdown**:

| Feature | Importance |
|---------|------------|
| Leucocytes_change | 0.0009 |
| CRP_change | 0.0000 |
| CRP_change_rate | 0.0000 |
| Leucocytes_change_rate | 0.0000 |
| LacticAcid_change | 0.0000 |
| LacticAcid_change_rate | 0.0000 |

## Implications for Process Prediction

The following hypothesized relationships were not supported and should be reconsidered:

1. **Critical Diagnostic Tests → Specific Events**: Features related to Critical Diagnostic Tests showed insufficient influence on predictions for Specific Events events, with only 0.01 importance vs. 0.02 average for other features.

1. **SIRS Criteria → Diagnostic Testing**: Features related to SIRS Criteria showed insufficient influence on predictions for Diagnostic Testing events, with only 0.00 importance vs. 0.02 average for other features.

1. **Department Transitions → Outcome Events**: Features related to Department Transitions showed insufficient influence on predictions for Outcome Events events, with only 0.00 importance vs. 0.02 average for other features.

1. **Clinical Marker Changes → Next Events**: Features related to Clinical Marker Changes showed insufficient influence on predictions for Next Events events, with only 0.00 importance vs. 0.02 average for other features.

