import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
import os

class DataTransformer:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.feature_names = None
        self.X_test = None
        self.y_test = None
        
    def preprocess_data(self, X, y, test_size=0.2, random_state=42, balance_classes=True):
        """
        Preprocess the data by encoding categorical variables, scaling features,
        handling class imbalance, and splitting into train/test sets
        """
        # Store original feature names
        self.feature_names = X.columns.tolist()
        
        # Handle class imbalance if requested
        if balance_classes:
            X, y = self._balance_classes(X, y)
        
        # Ensure case_id is not used for training
        X_for_training = X.copy()
        if 'case_id' in X_for_training.columns:
            X_for_training = X_for_training.drop(columns=['case_id'])
        
        # Encode categorical variables
        X_for_training = self._encode_categorical_features(X_for_training)
        
        # Handle missing values
        X_for_training = self._handle_missing_values(X_for_training)
        
        # Scale numerical features
        X_for_training = self._scale_features(X_for_training)
        
        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X_for_training, y, test_size=test_size, random_state=random_state, stratify=y
        )
        
        # Store test data for later evaluation
        self.X_test = X_test
        self.y_test = y_test
        
        print(f"Data preprocessing completed. X shape: {X_for_training.shape}, categorical features encoded: {len(self.label_encoders)}")
        
        return X_train, X_test, y_train, y_test
    
    def _encode_categorical_features(self, X):
        """Encode categorical variables using label encoding"""
        X_encoded = X.copy()
        
        # Find categorical columns (excluding case_id which should remain as-is)
        categorical_columns = X.select_dtypes(include=['object']).columns
        
        for col in categorical_columns:
            if col != 'case_id':  # Skip case_id
                # Create and fit a new label encoder for this column
                self.label_encoders[col] = LabelEncoder()
                
                # Handle possible NaN values before encoding
                non_null_mask = ~X[col].isna()
                if non_null_mask.any():
                    # Fit and transform non-null values
                    self.label_encoders[col].fit(X.loc[non_null_mask, col])
                    X_encoded.loc[non_null_mask, col] = self.label_encoders[col].transform(X.loc[non_null_mask, col])
                    # Fill NA with -1 to represent missing values
                    X_encoded.loc[~non_null_mask, col] = -1
                else:
                    # If all values are null, fill with -1
                    X_encoded[col] = -1
                
                # Convert to numeric type
                X_encoded[col] = pd.to_numeric(X_encoded[col], errors='coerce')
            
        return X_encoded
    
    def _handle_missing_values(self, X):
        """Handle missing values in the dataset"""
        # Replace with mean for numeric columns
        numeric_columns = X.select_dtypes(include=['float64', 'int64']).columns
        for col in numeric_columns:
            if X[col].isnull().any():
                X[col] = X[col].fillna(X[col].mean())
        
        # Check for any remaining NaN values and replace with 0
        if X.isnull().any().any():
            X = X.fillna(0)
        
        return X
    
    def _scale_features(self, X):
        """Scale numerical features"""
        # Find columns to scale (only numeric columns)
        columns_to_scale = X.select_dtypes(include=['float64', 'int64']).columns
        
        # Scale only the numerical columns
        if len(columns_to_scale) > 0:
            X_scaled = X.copy()
            X_scaled[columns_to_scale] = self.scaler.fit_transform(X[columns_to_scale])
            return X_scaled
        else:
            return X
    
    def _balance_classes(self, X, y):
        """Handle class imbalance by upsampling minority classes"""
        # Get class distribution
        class_counts = y.value_counts()
        
        # If no imbalance or only one class, return original data
        if len(class_counts) <= 1 or class_counts.min() >= class_counts.max() * 0.5:
            return X, y
        
        # Get majority class size
        majority_class = class_counts.index[0]
        n_samples = class_counts[majority_class]
        
        # Upsample minority classes
        balanced_features = []
        balanced_events = []
        
        for event_class in class_counts.index:
            class_mask = y == event_class
            class_features = X[class_mask]
            class_events = y[class_mask]
            
            if len(class_features) < n_samples:
                # Upsample minority class
                upsampled_features, upsampled_events = resample(
                    class_features, class_events,
                    replace=True,
                    n_samples=n_samples,
                    random_state=42
                )
                balanced_features.append(upsampled_features)
                balanced_events.extend(upsampled_events)
            else:
                balanced_features.append(class_features)
                balanced_events.extend(class_events)
        
        return pd.concat(balanced_features, axis=0), pd.Series(balanced_events)
    
    def encode_for_prediction(self, X):
        """Encode new data for prediction using the fitted encoders"""
        X_encoded = X.copy()
        
        # Encode categorical variables using fitted label encoders
        for col, encoder in self.label_encoders.items():
            if col in X.columns:
                # Handle unseen categories
                X_encoded[col] = X[col].apply(
                    lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1
                )
        
        # Handle missing values
        for col in X_encoded.columns:
            if X_encoded[col].isna().any():
                if X_encoded[col].dtype in ['float64', 'int64']:
                    X_encoded[col] = X_encoded[col].fillna(0)  # Fill with 0 for prediction
                else:
                    X_encoded[col] = X_encoded[col].fillna(X_encoded[col].mode()[0])
        
        # Apply scaling to numerical features
        numeric_columns = X_encoded.select_dtypes(include=['float64', 'int64']).columns
        if 'case_id' in numeric_columns:
            numeric_columns = numeric_columns.drop('case_id')
        
        if len(numeric_columns) > 0:
            X_encoded[numeric_columns] = self.scaler.transform(X_encoded[numeric_columns])
        
        return X_encoded
    
    def save_transformation_metadata(self, save_path):
        """Save transformation metadata for later use"""
        import joblib
        os.makedirs(save_path, exist_ok=True)
        
        # Save label encoders
        joblib.dump(self.label_encoders, os.path.join(save_path, 'label_encoders.pkl'))
        
        # Save scaler
        joblib.dump(self.scaler, os.path.join(save_path, 'scaler.pkl'))
        
        # Save feature names
        joblib.dump(self.feature_names, os.path.join(save_path, 'feature_names.pkl'))
        
    def load_transformation_metadata(self, load_path):
        """Load transformation metadata"""
        import joblib
        
        # Load label encoders
        self.label_encoders = joblib.load(os.path.join(load_path, 'label_encoders.pkl'))
        
        # Load scaler
        self.scaler = joblib.load(os.path.join(load_path, 'scaler.pkl'))
        
        # Load feature names
        self.feature_names = joblib.load(os.path.join(load_path, 'feature_names.pkl'))
