#!/usr/bin/env bash
# run_all_tests.sh — run bridge and taxonomy tests for tool_and_app_agnostic stage_1_07_testing

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TESTS=(
  "test_outputs_purpose_taxonomy.sh"
  "test_cross_entity_porting_bridge.sh"
)

TOTAL_PASS=0
TOTAL_FAIL=0
TOTAL_SKIP=0

for test in "${TESTS[@]}"; do
  out=$("$SCRIPT_DIR/$test" 2>&1)
  code=$?
  p=$(echo "$out" | grep -oP 'PASS.*?:\s*\K[0-9]+' | tail -1 || echo 0)
  f=$(echo "$out" | grep -oP 'FAIL.*?:\s*\K[0-9]+' | tail -1 || echo 0)
  s=$(echo "$out" | grep -oP 'SKIP.*?:\s*\K[0-9]+' | tail -1 || echo 0)
  p=${p:-0}; f=${f:-0}; s=${s:-0}
  TOTAL_PASS=$((TOTAL_PASS + p))
  TOTAL_FAIL=$((TOTAL_FAIL + f))
  TOTAL_SKIP=$((TOTAL_SKIP + s))
  status="PASS"; [ "$code" -ne 0 ] && status="FAIL"
  echo ">>> $test: $status (pass=$p fail=$f skip=$s)"
done

echo "================================"
echo "  TOTAL PASS: $TOTAL_PASS"
echo "  TOTAL FAIL: $TOTAL_FAIL"
echo "  TOTAL SKIP: $TOTAL_SKIP"
echo "================================"

[ "$TOTAL_FAIL" -eq 0 ] && exit 0 || exit 1
