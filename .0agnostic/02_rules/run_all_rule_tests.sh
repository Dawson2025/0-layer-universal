#!/usr/bin/env bash
# Master test runner for all rule tests
# Usage: bash .0agnostic/02_rules/run_all_rule_tests.sh [repo_root]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="${1:-$(cd "$SCRIPT_DIR/../.." && pwd)}"

TOTAL=0; PASS=0; FAIL=0; SKIP=0
DATE=$(date +%Y-%m-%d)

echo "======================================================="
echo "Rule Test Runner - $DATE"
echo "Repository: $REPO_ROOT"
echo "======================================================="
echo ""

# Run each rule's structural tests
for test_script in "$SCRIPT_DIR"/*/*/tests/test_structural.sh; do
    [ -f "$test_script" ] || continue
    rule_dir="$(dirname "$(dirname "$test_script")")"
    rule_name="$(basename "$rule_dir")"
    category="$(basename "$(dirname "$rule_dir")")"

    echo "-- [$category] $rule_name --"
    TOTAL=$((TOTAL + 1))
    if bash "$test_script" "$REPO_ROOT" 2>&1; then
        PASS=$((PASS + 1))
    else
        FAIL=$((FAIL + 1))
    fi
    echo ""
done

# Count rules without tests (SKIP)
for rule_dir in "$SCRIPT_DIR"/*/*; do
    [ -d "$rule_dir/tests" ] || continue
    rule_name="$(basename "$rule_dir")"
    [ "$rule_name" = "tests" ] && continue
    if [ ! -f "$rule_dir/tests/test_structural.sh" ]; then
        echo "-- SKIP: $rule_name (no test_structural.sh) --"
        SKIP=$((SKIP + 1))
        TOTAL=$((TOTAL + 1))
    fi
done

echo ""
echo "======================================================="
echo "SUMMARY: $TOTAL rules | $PASS PASS | $FAIL FAIL | $SKIP SKIP"
if [ "$TOTAL" -gt 0 ] && [ "$PASS" -gt 0 ]; then
    RELIABILITY=$((PASS * 100 / TOTAL))
    echo "Reliability: ${RELIABILITY}%"
else
    echo "Reliability: N/A"
    RELIABILITY="N/A"
fi
echo "======================================================="

echo "| $DATE | $TOTAL | $PASS | $FAIL | $SKIP | ${RELIABILITY}% | Auto-run |" >> "$SCRIPT_DIR/test_results_history.md"
echo "Results appended to test_results_history.md"
