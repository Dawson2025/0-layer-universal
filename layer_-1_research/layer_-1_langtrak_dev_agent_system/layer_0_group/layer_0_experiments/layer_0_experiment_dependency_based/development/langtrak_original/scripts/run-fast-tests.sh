#!/usr/bin/env bash
source .venv/bin/activate
#
# Run fast tests (unit + emulator integration)
# These should complete in ~15 seconds
#
# Usage:
#   ./run-fast-tests.sh          # Run unit tests, skip emulator if not available
#   CI_MODE=1 ./run-fast-tests.sh # Strict mode: fail if Firebase CLI missing
#

# Only fail on error in strict CI mode
if [ "$CI_MODE" = "1" ]; then
    set -e
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Running Fast Test Suite"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Step 1: Unit Tests (always run)
echo ""
echo "📦 Step 1: Unit Tests"
echo "─────────────────────────────────────────"
pytest tests/unit -v --no-cov || { echo "❌ Unit tests failed"; exit 1; }

# Step 2: Emulator Tests (optional unless CI_MODE=1)
echo ""
echo "🔥 Step 2: Integration Tests (Firebase Emulator)"
echo "─────────────────────────────────────────"

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    if [ "$CI_MODE" = "1" ]; then
        echo "❌ Firebase CLI not found in CI mode. Install with: npm install -g firebase-tools"
        exit 1
    else
        echo "⚠️  Firebase CLI not found. Skipping emulator tests."
        echo "    To install: npm install -g firebase-tools"
        echo "    To require emulator tests: CI_MODE=1 $0"
    fi
else
    firebase emulators:exec --only firestore,auth,storage --project demo-test \
        "pytest tests/integration/emulator -v -m emulator --no-cov" || {
        echo "❌ Emulator tests failed"
        exit 1
    }
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Fast tests completed!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
