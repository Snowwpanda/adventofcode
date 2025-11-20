#!/bin/bash
# Startup script for Advent Must Go On (Mac/Linux)
# Make executable: chmod +x start.sh
# Run: ./start.sh

echo ""
echo "================================================"
echo "  Advent Must Go On - Coding Challenge Engine"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[1/3] Checking Python installation..."
python3 --version

# Check if Streamlit is installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo ""
    echo "[2/3] Installing dependencies..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install dependencies"
        exit 1
    fi
else
    echo "[2/3] Dependencies already installed"
fi

echo ""
echo "[3/3] Starting Advent Must Go On..."
echo ""
echo "================================================"
echo "  The app will open in your browser"
echo "  Press Ctrl+C to stop the server"
echo "================================================"
echo ""

# Start Streamlit
streamlit run app.py
