import os
import pandas as pd
import numpy as np
import pm4py
from datetime import datetime
from collections import defaultdict

class FeatureExtractor:
    def __init__(self, log_path=None):
        self.log_path = log_path
        self.log = None
        self.df = None
        
    def load_log(self, log_path=None):
        """Load an XES event log file"""
        if log_path:
            self.log_path = log_path
            
        if self.log_path is None:
            raise ValueError("Log path must be provided")
            
        try:
            self.log = pm4py.read_xes(self.log_path)
            self.df = pm4py.convert_to_dataframe(self.log)
            print(f"Loaded log from {self.log_path}")
            return self.df
        except Exception as e:
            print(f"Error loading log: {str(e)}")
            raise
    
    def convert_to_datetime(self, timestamp):
        """Convert timestamp to datetime while handling timezone information"""
        dt = pd.to_datetime(timestamp)
        if dt.tzinfo is not None:
            dt = dt.tz_convert('UTC').tz_localize(None)
        return dt
    
    def extract_basic_features(self):
        """Extract basic features from the event log"""
        if self.df is None:
            raise ValueError("Event log not loaded. Call load_log() first.")
            
        # Convert timestamp to datetime
        self.df['time:timestamp'] = self.df['time:timestamp'].apply(self.convert_to_datetime)
        
        # Sort by case ID and timestamp
        self.df = self.df.sort_values(['case:concept:name', 'time:timestamp'])
        
        # Create features
        features = []
        next_events = []
        
        for case_id, group in self.df.groupby('case:concept:name'):
            group = group.reset_index(drop=True)
            
            for i in range(len(group) - 1):  # -1 because we're predicting next activity
                current_row = group.iloc[i]
                next_row = group.iloc[i + 1]
                
                # Basic features
                feature_dict = {
                    'case_id': case_id,
                    'current_activity': current_row['concept:name'],
                    'time_since_start': (current_row['time:timestamp'] - group['time:timestamp'].min()).total_seconds(),
                    'time_since_last_event': 0 if i == 0 else (current_row['time:timestamp'] - group.iloc[i-1]['time:timestamp']).total_seconds(),
                    'event_position': i + 1,
                    'trace_length': len(group),
                    'repeated_activities': group['concept:name'].value_counts()[current_row['concept:name']],
                    'unique_activities_so_far': len(group.iloc[:i+1]['concept:name'].unique()),
                }
                
                # Add department/organization if available
                if 'org:group' in current_row:
                    feature_dict['department'] = current_row['org:group']
                
                # Add all other columns as features (except timestamp and case id)
                for col in group.columns:
                    if col not in ['time:timestamp', 'case:concept:name', 'concept:name', 'org:group']:
                        feature_dict[f'current_{col}'] = current_row[col]
                
                features.append(feature_dict)
                next_events.append(next_row['concept:name'])
        
        # Convert to DataFrame
        X = pd.DataFrame(features)
        y = pd.Series(next_events)
        
        return X, y
    
    def extract_sepsis_features(self):
        """Extract Sepsis-specific features"""
        if self.df is None:
            raise ValueError("Event log not loaded. Call load_log() first.")
            
        # Check if this is a Sepsis dataset by looking for specific columns
        sepsis_columns = ['CRP', 'Leucocytes', 'LacticAcid']
        if not any(col in self.df.columns for col in sepsis_columns):
            print("Warning: This does not appear to be a Sepsis dataset. Using basic feature extraction instead.")
            return self.extract_basic_features()
            
        # Convert timestamp to datetime
        self.df['time:timestamp'] = self.df['time:timestamp'].apply(self.convert_to_datetime)
        
        # Sort by case ID and timestamp
        self.df = self.df.sort_values(['case:concept:name', 'time:timestamp'])
        
        features = []
        next_events = []
        
        # Add START to possible events
        all_events = list(self.df['concept:name'].unique()) + ['START']
        
        for case_id, group in self.df.groupby('case:concept:name'):
            group = group.reset_index(drop=True)
            
            for i in range(len(group) - 1):
                current_row = group.iloc[i]
                next_row = group.iloc[i + 1]
                
                # Enhanced temporal features
                time_since_start = (current_row['time:timestamp'] - group['time:timestamp'].min()).total_seconds()
                time_since_last = 0 if i == 0 else (current_row['time:timestamp'] - group.iloc[i-1]['time:timestamp']).total_seconds()
                time_of_day = current_row['time:timestamp'].hour
                weekend = int(current_row['time:timestamp'].weekday() >= 5)
                
                # Previous events sequence (last 5 events)
                prev_events = group.iloc[max(0, i-4):i+1]['concept:name'].tolist()
                while len(prev_events) < 5:
                    prev_events.insert(0, 'START')
                
                # Event frequency features
                events_so_far = group.iloc[:i+1]['concept:name'].tolist()
                event_frequencies = pd.Series(events_so_far).value_counts()
                current_event_freq = event_frequencies[current_row['concept:name']]
                
                # Department transition patterns
                if 'org:group' in group.columns:
                    dept_sequence = group.iloc[:i+1]['org:group'].tolist()
                    dept_transitions = sum(1 for j in range(len(dept_sequence)-1) if dept_sequence[j] != dept_sequence[j+1])
                    current_dept_duration = len(group[group['org:group'] == current_row['org:group']])
                else:
                    dept_transitions = 0
                    current_dept_duration = 0
                
                # Test result patterns
                test_columns = ['CRP', 'Leucocytes', 'LacticAcid']
                test_results = {}
                test_counts = {}
                for col in test_columns:
                    if col in group.columns:
                        tests = group.iloc[:i+1][col].dropna()
                        test_results[f'{col}_last'] = tests.iloc[-1] if not tests.empty else 0
                        test_results[f'{col}_mean'] = tests.mean() if not tests.empty else 0
                        test_results[f'{col}_max'] = tests.max() if not tests.empty else 0
                        test_counts[f'{col}_count'] = len(tests)
                
                # SIRS criteria patterns
                sirs_columns = [col for col in group.columns if col.startswith('SIRS')]
                sirs_history = {}
                for col in sirs_columns:
                    sirs_values = group.iloc[:i+1][col]
                    sirs_history[f'{col}_changes'] = (sirs_values != sirs_values.shift()).sum()
                    sirs_history[f'{col}_duration'] = (sirs_values == 1).sum()
                
                # Create feature dictionary
                feature_dict = {
                    'case_id': case_id,
                    'time_since_start': time_since_start,
                    'time_since_last_event': time_since_last,
                    'time_of_day': time_of_day,
                    'weekend': weekend,
                    'event_position': i + 1,
                    'trace_length': len(group),
                    'unique_activities': len(pd.Series(events_so_far).unique()),
                    'repeated_activities': current_event_freq,
                    'current_event': current_row['concept:name'],
                    'dept_changes': dept_transitions,
                    'current_dept_duration': current_dept_duration,
                }
                
                # Add department if available
                if 'org:group' in current_row:
                    feature_dict['department'] = current_row['org:group']
                
                # Add previous events
                for j, event in enumerate(prev_events[-5:], 1):
                    feature_dict[f'prev_event_{j}'] = event
                
                # Add SIRS criteria
                feature_dict.update(sirs_history)
                
                # Add test results and counts
                feature_dict.update(test_results)
                feature_dict.update(test_counts)
                
                # Add raw SIRS values
                for col in sirs_columns:
                    feature_dict[col] = current_row[col]
                
                # Add raw test values
                for col in test_columns:
                    if col in group.columns:
                        feature_dict[col] = current_row[col]
                
                features.append(feature_dict)
                next_events.append(next_row['concept:name'])
        
        # Convert to DataFrame
        X = pd.DataFrame(features)
        y = pd.Series(next_events)
        
        return X, y
    
    def extract_bpi_features(self):
        """Extract BPI-specific features for the BPI dataset"""
        if self.df is None:
            raise ValueError("Event log not loaded. Call load_log() first.")
            
        # Check if this looks like a BPI dataset
        if 'Amount' not in self.df.columns and 'declaration' not in " ".join(self.df.columns).lower():
            print("Warning: This does not appear to be a BPI dataset. Using basic feature extraction instead.")
            return self.extract_basic_features()
            
        # Convert timestamp to datetime
        self.df['time:timestamp'] = self.df['time:timestamp'].apply(self.convert_to_datetime)
        
        # Sort by case ID and timestamp
        self.df = self.df.sort_values(['case:concept:name', 'time:timestamp'])
        
        features = []
        next_events = []
        
        for case_id, group in self.df.groupby('case:concept:name'):
            group = group.reset_index(drop=True)
            
            for i in range(len(group) - 1):
                current_row = group.iloc[i]
                next_row = group.iloc[i + 1]
                
                # Basic temporal features
                time_since_start = (current_row['time:timestamp'] - group['time:timestamp'].min()).total_seconds()
                time_since_last = 0 if i == 0 else (current_row['time:timestamp'] - group.iloc[i-1]['time:timestamp']).total_seconds()
                
                # Create base features
                feature_dict = {
                    'case_id': case_id,
                    'time_since_start': time_since_start,
                    'time_since_last_event': time_since_last,
                    'event_position': i + 1,
                    'trace_length': len(group),
                    'current_event': current_row['concept:name'],
                }
                
                # Add specific BPI features
                if 'Amount' in current_row:
                    feature_dict['amount'] = current_row['Amount']
                
                # Add approval state if available
                approval_states = [col for col in current_row.index if 'APPROVED' in col or 'REJECTED' in col]
                for state in approval_states:
                    feature_dict[f'state_{state}'] = current_row[state]
                
                # Add all other columns as features (except timestamp and case id)
                for col in group.columns:
                    if col not in ['time:timestamp', 'case:concept:name', 'concept:name'] and col not in feature_dict:
                        feature_dict[f'current_{col}'] = current_row[col]
                
                features.append(feature_dict)
                next_events.append(next_row['concept:name'])
        
        # Convert to DataFrame
        X = pd.DataFrame(features)
        y = pd.Series(next_events)
        
        return X, y
    
    def extract_features(self, dataset_type=None):
        """Extract features based on dataset type"""
        if self.df is None:
            raise ValueError("Event log not loaded. Call load_log() first.")
            
        if dataset_type is None:
            # Try to auto-detect dataset type
            if any(col.startswith('SIRS') or col in ['CRP', 'Leucocytes', 'LacticAcid'] for col in self.df.columns):
                print("Detected Sepsis dataset, using Sepsis feature extraction")
                return self.extract_sepsis_features()
            elif 'Amount' in self.df.columns or any('declaration' in col.lower() for col in self.df.columns):
                print("Detected BPI dataset, using BPI feature extraction")
                return self.extract_bpi_features()
            else:
                print("Unknown dataset type, using basic feature extraction")
                return self.extract_basic_features()
        elif dataset_type.lower() == 'sepsis':
            return self.extract_sepsis_features()
        elif dataset_type.lower() == 'bpi':
            return self.extract_bpi_features()
        else:
            return self.extract_basic_features()
