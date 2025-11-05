#!/bin/bash
# Quick start script for Apriori Recommendation System
# This script sets up the environment and runs the Streamlit application

set -e

echo "🚀 Apriori Recommendation System - Quick Start"
echo "=============================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher and try again."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✅ Dependencies installed"
echo ""

# Check if data file exists
if [ ! -f "TransactionsInstacart.csv" ] && [ ! -f "notebooks/TransactionsInstacart.csv" ]; then
    echo "⚠️  Warning: TransactionsInstacart.csv not found!"
    echo "Please ensure the data file is in the project root or notebooks directory."
    echo ""
fi

# Run the Streamlit app
echo "🌐 Starting Streamlit application..."
echo "The app will open in your browser automatically."
echo "Press Ctrl+C to stop the application."
echo ""
streamlit run app.py
