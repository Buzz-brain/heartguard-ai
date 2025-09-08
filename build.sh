#!/bin/bash
# build.sh
echo "🔧 Setting up Python environment..."
python -m venv .venv
source .venv/bin/activate

echo "📦 Upgrading pip..."
pip install --upgrade pip

echo "🚀 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Build completed successfully!"