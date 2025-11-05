@echo off
REM Quick start script for Apriori Recommendation System (Windows)
REM This script sets up the environment and runs the Streamlit application

echo.
echo 🚀 Apriori Recommendation System - Quick Start
echo ==============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed.
    echo Please install Python 3.7 or higher and try again.
    pause
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install/update dependencies
echo 📚 Installing dependencies...
python -m pip install --upgrade pip -q
pip install -r requirements.txt -q
echo ✅ Dependencies installed
echo.

REM Check if data file exists
if not exist "TransactionsInstacart.csv" (
    if not exist "notebooks\TransactionsInstacart.csv" (
        echo ⚠️  Warning: TransactionsInstacart.csv not found!
        echo Please ensure the data file is in the project root or notebooks directory.
        echo.
    )
)

REM Run the Streamlit app
echo 🌐 Starting Streamlit application...
echo The app will open in your browser automatically.
echo Press Ctrl+C to stop the application.
echo.
streamlit run app.py
