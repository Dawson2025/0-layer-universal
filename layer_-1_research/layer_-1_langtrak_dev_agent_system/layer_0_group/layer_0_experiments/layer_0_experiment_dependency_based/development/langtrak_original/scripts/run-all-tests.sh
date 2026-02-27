#!/usr/bin/env bash
#
# Run ALL tests (fast tests + dev environment tests)
# This is what runs in CI/CD on main branch
#
# Usage:
#   ./run-all-tests.sh           # Run all available tests
#   CI_MODE=1 ./run-all-tests.sh # Strict mode for CI
#

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 Running COMPLETE Test Suite"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Run fast tests (unit + emulator)
# Pass through CI_MODE if set
if [ "$CI_MODE" = "1" ]; then
    CI_MODE=1 ./scripts/run-fast-tests.sh
else
    ./scripts/run-fast-tests.sh
fi

# Run real Firebase dev tests (if credentials available)
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔥 Real Firebase Integration Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ -f "firebase-admin-config.json" ]; then
    export RUN_FIREBASE_INTEGRATION_TESTS=1
    export FIREBASE_TEST_ENV=development

    pytest tests/integration/real_firebase/test_dev_environment.py -v -m "real_firebase and dev" --no-cov || {
        echo "❌ Real Firebase tests failed"
        exit 1
    }
    echo "✅ Real Firebase tests passed"
else
    if [ "$CI_MODE" = "1" ] && [ "$REQUIRE_FIREBASE_TESTS" = "1" ]; then
        echo "❌ Firebase credentials required in CI mode with REQUIRE_FIREBASE_TESTS=1"
        echo "    Expected: firebase-admin-config.json"
        exit 1
    else
        echo "⚠️  Skipping real Firebase tests (no credentials found)"
        echo "    To test with real Firebase: add firebase-admin-config.json"
    fi
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ ALL TESTS COMPLETED!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
