# Deploy to Render:
# Create GitHub repository with all these files

# Sign up on Render.com (free tier available)

# Connect your GitHub repository

# Create new Web Service and select your repository

# Configure settings:

# Build Command: pip install -r requirements.txt

# Start Command: gunicorn app:app

# Deploy!

# Required Files for Deployment:
# text
# 📦 project-folder/
# ├── 🐍 app.py                 # Flask application
# ├── 📋 requirements.txt       # Python dependencies
# ├── ⚙️ runtime.txt            # Python version
# ├── 🤖 heart_disease_best_model.pkl  # Trained model
# ├── ⚖️ feature_scaler.pkl     # Feature scaler
# ├── 📊 feature_names.pkl     # Feature names
# ├── 🚀 deploy.sh             # Deployment script (optional)
# └── 🧪 test_api.py           # Test script (optional)
# 🎯 API Endpoints:
# GET / - API information

# GET /health - Health check

# POST /predict - Make predictions

# GET /features - Get feature information

# This deployment package is production-ready and includes:

# ✅ Proper error handling

# ✅ Input validation

# ✅ CORS support (for frontend integration)

# ✅ Logging

# ✅ Health checks

# ✅ Comprehensive documentation

# Your heart disease prediction API is now ready for deployment! 🚀