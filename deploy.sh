# deploy.sh
#!/bin/bash

echo "🚀 Starting Heart Disease API Deployment..."

# Check if required files exist
if [ ! -f "heart_disease_best_model.pkl" ]; then
    echo "❌ Error: Model file not found!"
    exit 1
fi

if [ ! -f "feature_scaler.pkl" ]; then
    echo "❌ Error: Scaler file not found!"
    exit 1
fi

if [ ! -f "feature_names.pkl" ]; then
    echo "❌ Error: Feature names file not found!"
    exit 1
fi

echo "✅ All required files found"
echo "📦 Preparing deployment package..."

# Create necessary files if they don't exist
if [ ! -f "requirements.txt" ]; then
    echo "Creating requirements.txt..."
    cat > requirements.txt << EOL
flask==2.3.3
flask-cors==4.0.0
joblib==1.3.2
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
gunicorn==21.2.0
EOL
fi

if [ ! -f "runtime.txt" ]; then
    echo "Creating runtime.txt..."
    echo "python-3.9.18" > runtime.txt
fi

echo "✅ Deployment package ready!"
echo "📋 Files to deploy:"
echo "   - app.py"
echo "   - requirements.txt"
echo "   - runtime.txt"
echo "   - heart_disease_best_model.pkl"
echo "   - feature_scaler.pkl"
echo "   - feature_names.pkl"
echo ""
echo "📚 Next steps:"
echo "   1. Push these files to your GitHub repository"
echo "   2. Connect repository to Render.com"
echo "   3. Deploy as Python web service"
echo ""
echo "🎉 Ready for deployment!"