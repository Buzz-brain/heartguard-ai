# # app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import joblib
# import numpy as np
# import pandas as pd
# import logging
# from datetime import datetime

# # Initialize Flask application
# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Global variables for model and scaler
# model = None
# scaler = None
# feature_names = None

# def load_artifacts():
#     """Load the trained model, scaler, and feature names"""
#     global model, scaler, feature_names
#     try:
#         model = joblib.load('heart_disease_best_model.pkl')
#         scaler = joblib.load('feature_scaler.pkl')
#         feature_names = joblib.load('feature_names.pkl')
#         logger.info("✅ Model artifacts loaded successfully")
#         return True
#     except Exception as e:
#         logger.error(f"❌ Error loading model artifacts: {e}")
#         return False

# def validate_input_data(data):
#     """Validate the input data structure and values"""
#     required_fields = [
#         'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
#         'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
#     ]
    
#     # Check if all required fields are present
#     if not all(field in data for field in required_fields):
#         return False, "Missing required fields"
    
#     # Validate data types and ranges (basic validation)
#     try:
#         # Convert to appropriate types
#         data['age'] = float(data['age'])
#         data['sex'] = int(data['sex'])
#         data['cp'] = int(data['cp'])
#         data['trestbps'] = float(data['trestbps'])
#         data['chol'] = float(data['chol'])
#         data['fbs'] = int(data['fbs'])
#         data['restecg'] = int(data['restecg'])
#         data['thalach'] = float(data['thalach'])
#         data['exang'] = int(data['exang'])
#         data['oldpeak'] = float(data['oldpeak'])
#         data['slope'] = int(data['slope'])
#         data['ca'] = int(data['ca'])
#         data['thal'] = int(data['thal'])
        
#         # Basic range validation
#         if not (0 <= data['age'] <= 120):
#             return False, "Age must be between 0 and 120"
#         if data['sex'] not in [0, 1]:
#             return False, "Sex must be 0 (female) or 1 (male)"
#         if not (0 <= data['cp'] <= 3):
#             return False, "Chest pain type must be between 0-3"
#         # Add more validations as needed
            
#     except (ValueError, TypeError) as e:
#         return False, f"Invalid data types: {e}"
    
#     return True, "Validation passed"

# @app.before_request
# # @app.before_first_request
# def initialize():
#     """Initialize the model before first request"""
#     if not load_artifacts():
#         raise RuntimeError("Failed to load model artifacts")

# @app.route('/')
# def home():
#     """Home endpoint with API information"""
#     return jsonify({
#         'message': 'Heart Disease Prediction API',
#         'version': '1.0.0',
#         'status': 'active',
#         'timestamp': datetime.now().isoformat()
#     })

# @app.route('/health', methods=['GET'])
# def health_check():
#     """Health check endpoint"""
#     return jsonify({
#         'status': 'healthy',
#         'model_loaded': model is not None,
#         'timestamp': datetime.now().isoformat()
#     })

# @app.route('/predict', methods=['POST'])
# def predict():
#     """Main prediction endpoint"""
#     try:
#         # Get JSON data from request
#         data = request.get_json()
        
#         if not data:
#             return jsonify({'error': 'No data provided'}), 400
        
#         # Validate input data
#         is_valid, message = validate_input_data(data)
#         if not is_valid:
#             return jsonify({'error': message}), 400
        
#         # Prepare features in correct order
#         features = np.array([[
#             data['age'], data['sex'], data['cp'], data['trestbps'], 
#             data['chol'], data['fbs'], data['restecg'], data['thalach'],
#             data['exang'], data['oldpeak'], data['slope'], data['ca'], 
#             data['thal']
#         ]])
        
#         # Create DataFrame with correct feature names
#         features_df = pd.DataFrame(features, columns=feature_names)
        
#         # Scale numerical features
#         numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
#         features_df[numerical_features] = scaler.transform(features_df[numerical_features])
        
#         # Make prediction
#         prediction = model.predict(features_df)
#         prediction_proba = model.predict_proba(features_df)
        
#         # Prepare response
#         result = {
#             'prediction': int(prediction[0]),
#             'prediction_label': 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease',
#             'confidence': float(np.max(prediction_proba)),
#             'probabilities': {
#                 'no_disease': float(prediction_proba[0][0]),
#                 'disease': float(prediction_proba[0][1])
#             },
#             'timestamp': datetime.now().isoformat()
#         }
        
#         logger.info(f"Prediction made: {result}")
#         return jsonify(result)
        
#     except Exception as e:
#         logger.error(f"Prediction error: {e}")
#         return jsonify({'error': 'Internal server error'}), 500

# @app.route('/features', methods=['GET'])
# def get_features():
#     """Endpoint to get feature information"""
#     return jsonify({
#         'feature_names': feature_names,
#         'feature_descriptions': {
#             'age': 'Age in years',
#             'sex': 'Sex (0 = female, 1 = male)',
#             'cp': 'Chest pain type (0-3)',
#             'trestbps': 'Resting blood pressure (mm Hg)',
#             'chol': 'Serum cholesterol (mg/dl)',
#             'fbs': 'Fasting blood sugar > 120 mg/dl (0 = false, 1 = true)',
#             'restecg': 'Resting electrocardiographic results (0-2)',
#             'thalach': 'Maximum heart rate achieved',
#             'exang': 'Exercise induced angina (0 = no, 1 = yes)',
#             'oldpeak': 'ST depression induced by exercise relative to rest',
#             'slope': 'Slope of the peak exercise ST segment (0-2)',
#             'ca': 'Number of major vessels (0-3) colored by fluoroscopy',
#             'thal': 'Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)'
#         }
#     })

# if __name__ == '__main__':
#     # Load artifacts before running
#     if load_artifacts():
#         app.run(debug=True, host='0.0.0.0', port=5000)
#     else:
#         print("Failed to load model artifacts. Exiting.")



# app.py (UPDATED PREDICT FUNCTION)
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import logging
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables
model = None
scaler = None
feature_names = None

def load_artifacts():
    """Load the trained model, scaler, and feature names"""
    global model, scaler, feature_names
    try:
        model = joblib.load('heart_disease_best_model.pkl')
        scaler = joblib.load('feature_scaler.pkl')
        feature_names = joblib.load('feature_names.pkl')
        logger.info("✅ Model artifacts loaded successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Error loading model artifacts: {e}")
        return False

def validate_input_data(data):
    """Validate the input data structure and values"""
    required_fields = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
        'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]
    
    if not all(field in data for field in required_fields):
        return False, "Missing required fields"
    
    try:
        # Convert to appropriate types
        data['age'] = float(data['age'])
        data['sex'] = int(data['sex'])
        data['cp'] = int(data['cp'])
        data['trestbps'] = float(data['trestbps'])
        data['chol'] = float(data['chol'])
        data['fbs'] = int(data['fbs'])
        data['restecg'] = int(data['restecg'])
        data['thalach'] = float(data['thalach'])
        data['exang'] = int(data['exang'])
        data['oldpeak'] = float(data['oldpeak'])
        data['slope'] = int(data['slope'])
        data['ca'] = int(data['ca'])
        data['thal'] = int(data['thal'])
        
    except (ValueError, TypeError) as e:
        return False, f"Invalid data types: {e}"
    
    return True, "Validation passed"

@app.before_request
def initialize():
    """Initialize the model before first request"""
    if not load_artifacts():
        raise RuntimeError("Failed to load model artifacts")

@app.route('/')
def home():
    return jsonify({
        'message': 'Heart Disease Prediction API',
        'version': '1.0.0',
        'status': 'active',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Main prediction endpoint - FIXED VERSION"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate input data
        is_valid, message = validate_input_data(data)
        if not is_valid:
            return jsonify({'error': message}), 400
        
        # Create feature array in EXACTLY the same order as during training
        features = np.array([[
            data['age'], data['sex'], data['cp'], data['trestbps'], 
            data['chol'], data['fbs'], data['restecg'], data['thalach'],
            data['exang'], data['oldpeak'], data['slope'], data['ca'], 
            data['thal']
        ]])
        
        # Create DataFrame with correct feature names IN THE RIGHT ORDER
        features_df = pd.DataFrame(features, columns=feature_names)
        
        # Scale ONLY the numerical features (same as during training)
        numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
        
        # Extract numerical features, scale them, and put back
        numerical_data = features_df[numerical_features].values
        scaled_numerical = scaler.transform(numerical_data)
        features_df[numerical_features] = scaled_numerical
        
        # Make prediction
        prediction = model.predict(features_df)
        prediction_proba = model.predict_proba(features_df)
        
        # Prepare response
        result = {
            'prediction': int(prediction[0]),
            'prediction_label': 'Heart Disease' if prediction[0] == 1 else 'No Heart Disease',
            'confidence': float(np.max(prediction_proba)),
            'probabilities': {
                'no_disease': float(prediction_proba[0][0]),
                'disease': float(prediction_proba[0][1])
            },
            'timestamp': datetime.now().isoformat(),
            'feature_values': data  # Include original values for debugging
        }
        
        logger.info(f"Prediction made: {result}")
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500

@app.route('/features', methods=['GET'])
def get_features():
    return jsonify({
        'feature_names': feature_names,
        'feature_descriptions': {
            'age': 'Age in years',
            'sex': 'Sex (0 = female, 1 = male)',
            'cp': 'Chest pain type (0-3)',
            'trestbps': 'Resting blood pressure (mm Hg)',
            'chol': 'Serum cholesterol (mg/dl)',
            'fbs': 'Fasting blood sugar > 120 mg/dl (0 = false, 1 = true)',
            'restecg': 'Resting electrocardiographic results (0-2)',
            'thalach': 'Maximum heart rate achieved',
            'exang': 'Exercise induced angina (0 = no, 1 = yes)',
            'oldpeak': 'ST depression induced by exercise relative to rest',
            'slope': 'Slope of the peak exercise ST segment (0-2)',
            'ca': 'Number of major vessels (0-3) colored by fluoroscopy',
            'thal': 'Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect)'
        }
    })

if __name__ == '__main__':
    if load_artifacts():
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to load model artifacts. Exiting.")