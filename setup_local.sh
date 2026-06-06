#!/bin/bash

# Local Setup Script for iOS Apps Analytics Dashboard
# This script helps you set up the project locally

echo "🚀 Setting up iOS Apps Analytics Dashboard..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment (optional but recommended)
read -p "Do you want to create a virtual environment? (recommended) [y/N]: " create_venv
if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv

    echo "📦 Activating virtual environment..."
    source venv/bin/activate

    echo "✅ Virtual environment created and activated!"
    echo ""
fi

# Install requirements
echo "📦 Installing required packages..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All packages installed successfully!"
else
    echo "❌ Failed to install packages. Please check requirements.txt"
    exit 1
fi

echo ""

# Check for .env file
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "📝 Creating .env file from template..."
    cp .env.example .env

    echo ""
    echo "🔑 Please edit .env file and add your GitHub token:"
    echo "   1. Go to https://github.com/settings/tokens"
    echo "   2. Generate new token with 'public_repo' or 'repo' scope"
    echo "   3. Copy the token"
    echo "   4. Edit .env file and paste your token"
    echo ""

    read -p "Press Enter when you've added your token to .env..."
else
    echo "✅ .env file found!"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To run the dashboard:"
echo "   streamlit run app.py"
echo ""

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "Note: Virtual environment is active. To deactivate later, run: deactivate"
    echo ""
fi

# Ask if user wants to run the app now
read -p "Do you want to start the dashboard now? [y/N]: " run_now
if [[ $run_now =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Starting Streamlit dashboard..."
    echo ""
    streamlit run app.py
fi
