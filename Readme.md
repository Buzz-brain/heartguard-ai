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

Validation: Custom input validation

API: RESTful JSON API

CORS: Flask-CORS for cross-origin requests

Frontend (Upcoming)
Framework: React.js 18+

UI Library: Material-UI

Charts: Chart.js for visualization

HTTP Client: Axios for API calls

Deployment
Backend: Render.com

Frontend: Vercel/Netlify

Model Storage: GitHub LFS

📋 API Documentation
Base URL
https://heartguard-api.onrender.com

Endpoints
1. Health Check
http
GET /health
Response:

json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-09-07T18:30:45.123456"
}
2. Prediction Endpoint
http
POST /predict
Content-Type: application/json
Request Body:

json
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
Success Response:

json
{
  "prediction": 1,
  "prediction_label": "Heart Disease",
  "confidence": 0.96,
  "probabilities": {
    "no_disease": 0.04,
    "disease": 0.96
  },
  "timestamp": "2025-09-07T18:32:15.123456"
}
🎓 Clinical Parameters
Parameter	Description	Values
age	Age in years	29-77
sex	Gender	0=Female, 1=Male
cp	Chest pain type	0-3
trestbps	Resting BP (mm Hg)	94-200
chol	Cholesterol (mg/dl)	126-564
fbs	Fasting blood sugar	0=False, 1=True
restecg	Resting ECG	0-2
thalach	Max heart rate	71-202
exang	Exercise angina	0=No, 1=Yes
oldpeak	ST depression	0.0-6.2
slope	ST segment slope	0-2
ca	Major vessels	0-3
thal	Thalassemia	3,6,7
📈 Model Training Details
Dataset
Source: UCI Cleveland Heart Disease Dataset

Samples: 297 patients after cleaning

Features: 13 clinical parameters

Target: Binary classification (0=No Disease, 1=Disease)

Algorithms Evaluated
Random Forest (Selected) 🥇

Support Vector Machine 🥈

Logistic Regression 🥉

XGBoost

K-Nearest Neighbors

Decision Tree

Feature Importance
Thal (13.5%) - Thalassemia

CP (13.4%) - Chest pain type

Thalach (11.7%) - Max heart rate

Oldpeak (10.5%) - ST depression

CA (9.6%) - Major vessels

🌟 Why HeartGuard AI?
For Healthcare Providers
Early Detection: Identify at-risk patients before symptoms worsen

Decision Support: Second opinion for clinical assessments

Time Efficiency: Rapid analysis of patient data

Consistency: Objective, data-driven predictions

For Patients
Awareness: Understand personal heart disease risk factors

Prevention: Motivation for lifestyle changes

Accessibility: Remote health assessment capability

🚨 Important Disclaimer
HeartGuard AI is a decision support tool, not a diagnostic replacement.

Always consult qualified healthcare professionals for medical diagnosis

Predictions should be used as supplementary information only

System accuracy is 86.67% - false positives/negatives are possible

Not intended for emergency medical situations

🤝 Contributing
We welcome contributions! Please see our Contributing Guidelines for details.

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit changes (git commit -m 'Add amazing feature')

Push to branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
UCI Machine Learning Repository for the Cleveland Heart Disease dataset

Scikit-learn team for excellent machine learning tools

Flask team for the lightweight web framework

Medical professionals who provided clinical validation

📞 Support
For support, please open an issue on GitHub or contact our team at support@heartguard-ai.com

🏥 Ethical Considerations
Patient privacy protection through data anonymization

Transparent model decision-making process

Regular model audits for bias detection

Compliance with healthcare data regulations

Built with ❤️ for better heart health worldwide.

https://img.shields.io/badge/HeartGuard-AI%2520for%2520Health-red