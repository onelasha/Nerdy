#!/bin/bash

echo "🚀 Setting up Student Risk Dashboard..."
echo ""

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Dependencies installed!"
echo ""

# Generate data
echo "📊 Generating sample student data..."
python generate_data.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the dashboard:"
echo "  streamlit run dashboard.py"
echo ""
echo "Optional: Set ANTHROPIC_API_KEY for AI-powered analysis:"
echo "  export ANTHROPIC_API_KEY='your-key-here'"
echo ""
