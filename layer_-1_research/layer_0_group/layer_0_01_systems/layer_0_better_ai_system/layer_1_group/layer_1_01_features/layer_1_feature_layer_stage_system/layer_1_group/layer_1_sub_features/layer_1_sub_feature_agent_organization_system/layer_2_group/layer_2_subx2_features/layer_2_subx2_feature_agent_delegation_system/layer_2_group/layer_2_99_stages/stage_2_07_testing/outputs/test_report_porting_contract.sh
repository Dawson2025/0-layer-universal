#!/usr/bin/env bash
# resource_id: "2dfed501-c014-48bb-93d2-a41461352989"
# resource_type: "script"
# resource_name: "test_report_porting_contract"
# test_report_porting_contract.sh — Validate stage report + handoff contract for active stages

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGES_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

PASS=0
FAIL=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }

echo "=== Test: Report Porting Contract (agent_delegation_system) ==="

ACTIVE_STAGES=(
  "stage_1_01_request_gathering"
  "stage_1_02_research"
  "stage_1_04_design"
  "stage_1_06_development"
)

for stage in "${ACTIVE_STAGES[@]}"; do
  d="$STAGES_ROOT/$stage"
  canon="$d/outputs/reports/stage_report.md"
  legacy="$d/outputs/stage_report.md"
  up="$d/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md"
  down="$d/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md"
  overview="$d/outputs/reports/output_report.md"

  [ -f "$canon" ] && pass "$stage canonical stage_report exists" || fail "$stage missing canonical stage_report"
  [ -f "$up" ] && pass "$stage to_above stage_report exists" || fail "$stage missing to_above stage_report"
  [ -f "$down" ] && pass "$stage to_below stage_report exists" || fail "$stage missing to_below stage_report"
  [ -f "$legacy" ] && pass "$stage legacy stage_report exists" || fail "$stage missing legacy compatibility stage_report"

  if [ -f "$canon" ] && [ -f "$up" ] && cmp -s "$canon" "$up"; then
    pass "$stage canonical == to_above"
  else
    fail "$stage canonical != to_above"
  fi

  if [ -f "$canon" ] && [ -f "$down" ] && cmp -s "$canon" "$down"; then
    pass "$stage canonical == to_below"
  else
    fail "$stage canonical != to_below"
  fi

  if [ -f "$overview" ]; then
    pass "$stage output_report exists"
  else
    fail "$stage missing output_report"
  fi
done

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
