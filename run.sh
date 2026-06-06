#!/bin/bash

# Simple script to run the Streamlit dashboard
# Usage: ./run.sh [port]

PORT=${1:-8501}

echo "🚀 Starting iOS Apps Analytics Dashboard on port $PORT..."
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py --server.port=$PORT
