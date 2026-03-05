#!/bin/bash
# resource_id: "ff1bb900-ae58-401a-9b9f-c0f935ee4eaf"
# resource_type: "script"
# resource_name: "start_dev"
# Start development environment with Firebase emulators

echo "🚀 Starting Language Tracker Development Environment"
echo "=" * 50

# Set environment variables
export FIRESTORE_EMULATOR_HOST=127.0.0.1:8081
export FIREBASE_AUTH_EMULATOR_HOST=127.0.0.1:9099
export FIREBASE_STORAGE_EMULATOR_HOST=127.0.0.1:9199

echo "Environment variables set:"
echo "  FIREBASE_AUTH_EMULATOR_HOST: $FIREBASE_AUTH_EMULATOR_HOST"
echo "  FIRESTORE_EMULATOR_HOST: $FIRESTORE_EMULATOR_HOST"
echo "  FIREBASE_STORAGE_EMULATOR_HOST: $FIREBASE_STORAGE_EMULATOR_HOST"
echo ""

# Activate virtual environment
source venv/bin/activate 2>/dev/null || source .venv/bin/activate 2>/dev/null

# Start Flask app
echo "Starting Flask app..."
PORT="${PORT:-5000}" python app.py
