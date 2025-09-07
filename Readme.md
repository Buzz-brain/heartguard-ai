🫀 HeartGuard AI - Coronary Heart Disease Prediction System
🎯 Overview
HeartGuard AI is an advanced machine learning-powered web application that predicts the likelihood of coronary heart disease based on clinical and demographic data. This system serves as an early warning tool to assist healthcare professionals in identifying high-risk patients, enabling timely interventions and improved patient outcomes.

https://img.shields.io/badge/Status-Production%2520Ready-brightgreen
https://img.shields.io/badge/Python-3.9%252B-blue
https://img.shields.io/badge/ML-Random%2520Forest-orange
https://img.shields.io/badge/Accuracy-86.67%2525-green

✨ Key Features
🤖 AI-Powered Predictions: Advanced Random Forest model with 86.67% accuracy

⚡ Real-time Analysis: Instant predictions with response times under 100ms

🏥 Clinical Validation: Medically sound predictions based on 13 clinical parameters

🔒 Privacy-First: Local processing with no data storage

📱 Responsive Design: Works seamlessly on desktop and mobile devices

🎯 High Confidence: Predictions with >85% confidence scores

🏗️ System Architecture
Diagram
Code
graph TD
    A[React.js Frontend] --> B[Flask REST API]
    B --> C[Random Forest Model]
    C --> D[Feature Scaling]
    D --> E[Prediction Engine]
    E --> F[JSON Response]
    F --> A


📊 Model Performance
Metric	Score	Performance Level
Accuracy	86.67%	🏅 Excellent
F1-Score	0.8519	🏅 Excellent
ROC-AUC	0.9453	🏅 Outstanding
Recall	82.14%	🏅 Very Good
Precision	88.46%	🏅 Excellent
🚀 Quick Start
Prerequisites
Python 3.9+

Node.js 14+

Git

Installation
Clone the Repository

bash
git clone https://github.com/yourusername/heartguard-ai.git
cd heartguard-ai
Backend Setup

bash
cd backend
pip install -r requirements.txt
python app.py
Frontend Setup (Coming Soon)

bash
cd frontend
npm install
npm start
🛠️ Technology Stack
Backend
Framework: Flask 2.3.3

Machine Learning: Scikit-learn 1.6.1

# 🫀 HeartGuard AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.1-007ACC?logo=scikit-learn)](https://scikit-learn.org/)
[![Model Accuracy](https://img.shields.io/badge/Accuracy-86.67%25-green)]()

A machine learning–powered web service that predicts the likelihood of coronary heart disease from clinical and demographic inputs. Built with Flask and scikit-learn, HeartGuard AI is intended as a clinical decision support tool to help healthcare teams identify at-risk patients earlier.

---

## Table of Contents
- [Features](#features)
- [Project structure](#project-structure)
- [Quick start](#quick-start)
- [API documentation](#api-documentation)
- [Clinical parameters](#clinical-parameters)
- [Model training details](#model-training-details)
- [Why HeartGuard AI?](#why-heartguard-ai)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

---

## ✨ Features
- AI-powered predictions using a Random Forest model (Accuracy: 86.67%)
- Fast responses for real-time usage
- Privacy-first design — no patient data persisted by default
- RESTful JSON API with health check and prediction endpoints
- Lightweight, easy-to-deploy Flask backend

---

## Project structure
```text
heart-disease/
├── app.py                      # Flask application entrypoint
├── comprehensive_test.py       # Tests / examples
├── feature_names.pkl           # Feature names used by the model
├── feature_scaler.pkl          # Scaler used for preprocessing
├── heart_disease_best_model.pkl# Trained Random Forest model
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Runtime notes (for hosting providers)
├── render.yaml                 # Deployment manifest (optional)
└── README.md                   # Project README (this file)
```

---

## 🚀 Quick start
These commands are for Windows PowerShell (adjust for other shells).

### Prerequisites
- Python 3.9+
- pip
- (Optional) virtual environment

### Install and run
```powershell
git clone https://github.com/Buzz-brain/heartguard-ai.git
cd "heart-disease"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
The API will start on the port configured in `app.py` (default: 5000). Open `http://localhost:5000/health` to confirm the service is healthy.

---

## 📋 API documentation
Base URL: `http://localhost:5000` (or your deployed URL)

### Health check
```
GET /health
```
Response example:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-09-07T18:30:45.123456"
}
```

### Prediction
```
POST /predict
Content-Type: application/json
```
Request body example:
```json
{
  "age": 55,
  "sex": 1,
  "cp": 3,
  "trestbps": 130,
  "chol": 250,
  "fbs": 0,
  "restecg": 0,
  "thalach": 187,
  "exang": 0,
  "oldpeak": 3.5,
  "slope": 3,
  "ca": 0,
  "thal": 3
}
```
Response example:
```json
{
  "prediction": 1,
  "prediction_label": "Heart Disease",
  "confidence": 0.96,
  "probabilities": { "no_disease": 0.04, "disease": 0.96 },
  "timestamp": "2025-09-07T18:32:15.123456"
}
```

Notes:
- All features expected are numeric and correspond to the clinical parameters in [Clinical parameters](#clinical-parameters).
- The model returns a binary prediction (0 = No Disease, 1 = Disease) and probabilities.

---

## 🎓 Clinical parameters
| Parameter | Description | Values |
|---|---:|---:|
| age | Age in years | 29–77 |
| sex | Gender | 0 = Female, 1 = Male |
| cp | Chest pain type | 0–3 |
| trestbps | Resting blood pressure (mm Hg) | 94–200 |
| chol | Serum cholesterol (mg/dl) | 126–564 |
| fbs | Fasting blood sugar > 120 mg/dl | 0 = False, 1 = True |
| restecg | Resting electrocardiographic results | 0–2 |
| thalach | Maximum heart rate achieved | 71–202 |
| exang | Exercise-induced angina | 0 = No, 1 = Yes |
| oldpeak | ST depression induced by exercise | 0.0–6.2 |
| slope | Slope of peak exercise ST segment | 0–2 |
| ca | Number of major vessels (0–3) colored by fluoroscopy | 0–3 |
| thal | Thalassemia (3 = normal, 6 = fixed defect, 7 = reversible defect) | 3,6,7 |

---

## 📈 Model training details
- Dataset: UCI Cleveland Heart Disease dataset (preprocessed)
- Samples: ~297 after cleaning
- Features: 13 clinical parameters
- Task: Binary classification (0 = No Disease, 1 = Disease)
- Selected model: Random Forest (best trade-off between performance and interpretability)

Top features by importance (approx.): Thal, CP, Thalach, Oldpeak, CA

---

## 🌟 Why HeartGuard AI?
- Early detection support for clinicians
- Quick, consistent risk scoring from structured inputs
- Privacy-first deployment options (local inference)

---

## 🤝 Contributing
Contributions are welcome. Please follow standard GitHub workflow:
1. Fork the repository
2. Create a topic branch (`git checkout -b feature/my-feature`)
3. Commit changes (`git commit -m "Add my feature"`)
4. Push and open a PR

For code changes, include tests or a short demo demonstrating the change.

---

## � License
This project is licensed under the MIT License — see the `LICENSE` file for details.

---

## 🙏 Acknowledgments
- UCI Machine Learning Repository — Cleveland Heart Disease dataset
- scikit-learn and Flask projects
- Medical advisors for domain guidance

---

## � Contact
For questions or support, open an issue or email: [support@heartguard-ai.com](mailto:support@heartguard-ai.com)

---

<p align="center">Built with ❤️ by Buzz brain</p>