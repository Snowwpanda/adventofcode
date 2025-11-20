@echo off
REM Startup script for Advent Must Go On
REM Double-click this file to start the app!

echo.
echo ================================================
echo   Advent Must Go On - Coding Challenge Engine
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo.
    echo [2/3] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo [2/3] Dependencies already installed
)

echo.
echo [3/3] Starting Advent Must Go On...
echo.
echo ================================================
echo   The app will open in your browser
echo   Press Ctrl+C to stop the server
echo ================================================
echo.

REM Start Streamlit
streamlit run app.py

pause
