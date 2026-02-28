#!/usr/bin/env bash
#
# Run tests against REAL dev Firebase environment
# CAUTION: This creates and deletes real data in lang-trak-dev
#

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥 Running Dev Environment Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "⚠️  WARNING: This will create and delete data in lang-trak-dev Firebase project"
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

export RUN_FIREBASE_INTEGRATION_TESTS=1
export FIREBASE_TEST_ENV=development

echo ""
echo "🧪 Running dev environment verification tests..."
pytest tests/integration/real_firebase/test_dev_environment.py -v -m "real_firebase and dev"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Dev environment tests completed!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
