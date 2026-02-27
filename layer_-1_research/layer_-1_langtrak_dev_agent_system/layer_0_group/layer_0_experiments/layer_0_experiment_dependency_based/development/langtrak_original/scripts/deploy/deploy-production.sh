#!/bin/bash
# Production Deployment Script for Language Tracker
# Run from project root: bash scripts/deploy/deploy-production.sh

set -e  # Exit on error

echo "🚀 Language Tracker Production Deployment"
echo "=========================================="
echo ""

# Check we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Must run from project root"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
echo "✅ Python version: $PYTHON_VERSION"

# Create necessary directories
echo "📁 Creating required directories..."
mkdir -p logs
mkdir -p data
mkdir -p uploads
mkdir -p videos
mkdir -p artifacts

# Activate virtual environment if it exists, or create it
if [ -d ".venv" ]; then
    echo "✅ Using existing virtual environment"
    source .venv/bin/activate
else
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
fi

# Install/update production dependencies
echo "📦 Installing production dependencies..."
pip install --upgrade pip
pip install -r requirements-prod.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  No .env file found"
    if [ -f ".env.production.example" ]; then
        echo "📋 Copying .env.production.example to .env"
        cp .env.production.example .env
        echo "⚠️  IMPORTANT: Edit .env and set your SECRET_KEY and Firebase credentials!"
    fi
fi

# Initialize database if needed
if [ ! -f "data/phonemes.db" ]; then
    echo "🗄️  Initializing database..."
    python3 << EOF
import sqlite3
import main
print("Database initialized")
EOF
fi

# Stop any running instances
echo "🛑 Stopping any existing instances..."
if [ -f "gunicorn.pid" ]; then
    PID=$(cat gunicorn.pid)
    if ps -p $PID > /dev/null 2>&1; then
        echo "   Stopping gunicorn (PID: $PID)..."
        kill $PID
        sleep 2
    fi
    rm -f gunicorn.pid
fi

# Kill any flask processes on port 5000
if lsof -ti:5000 > /dev/null 2>&1; then
    echo "   Killing processes on port 5000..."
    lsof -ti:5000 | xargs kill -9 2>/dev/null || true
fi

echo ""
echo "✅ Pre-deployment checks complete"
echo ""
echo "Choose deployment mode:"
echo "1) Development mode (Flask dev server)"
echo "2) Production mode (Gunicorn)"
echo "3) Production with systemd service"
echo ""
read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "🔧 Starting in development mode..."
        PORT=5000 python3 app.py
        ;;
    2)
        echo "🚀 Starting in production mode with Gunicorn..."
        gunicorn --config gunicorn.conf.py app:app
        ;;
    3)
        echo "📋 Setting up systemd service..."
        bash scripts/deploy/setup-systemd.sh
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

