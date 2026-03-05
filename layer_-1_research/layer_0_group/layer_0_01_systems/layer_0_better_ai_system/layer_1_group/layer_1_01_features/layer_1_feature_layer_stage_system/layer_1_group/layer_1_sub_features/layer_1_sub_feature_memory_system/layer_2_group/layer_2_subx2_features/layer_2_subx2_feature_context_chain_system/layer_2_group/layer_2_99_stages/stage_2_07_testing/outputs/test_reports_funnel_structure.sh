#!/usr/bin/env bash
# resource_id: "4fc08955-c1be-414c-bd60-8d05969d0ca9"
# resource_type: "script"
# resource_name: "test_reports_funnel_structure"
# test_reports_funnel_structure.sh — Validate canonical reports + handoff mirror structure

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ENTITY_DIR="$(cd "$STAGE_DIR/../../.." && pwd)"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Reports Funnel Structure ==="

action_paths=(
  "$STAGE_DIR/outputs/reports"
  "$STAGE_DIR/outputs/reports/stage_report.md"
  "$STAGE_DIR/outputs/reports/output_report.md"
  "$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md"
  "$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md"
  "$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md"
  "$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/overview_report.md"
  "$ENTITY_DIR/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md"
  "$ENTITY_DIR/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/layer_report.md"
)

for p in "${action_paths[@]}"; do
  if [ -e "$p" ]; then
    pass "Exists: ${p#${STAGE_DIR}/}"
  else
    fail "Missing: $p"
  fi
done

# Canonical report should match handoff mirrors exactly.
canon="$STAGE_DIR/outputs/reports/stage_report.md"
up="$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md"
down="$STAGE_DIR/.0agnostic/05_handoff_documents/02_outgoing/03_to_below/stage_report.md"

if cmp -s "$canon" "$up"; then
  pass "Canonical stage_report matches to_above handoff copy"
else
  fail "Mismatch between canonical stage_report and to_above handoff copy"
fi

if cmp -s "$canon" "$down"; then
  pass "Canonical stage_report matches to_below handoff copy"
else
  fail "Mismatch between canonical stage_report and to_below handoff copy"
fi

# Legacy compatibility file should exist for transition.
if [ -f "$STAGE_DIR/outputs/stage_report.md" ]; then
  pass "Legacy stage_report exists for compatibility"
else
  skip "Legacy stage_report not present (allowed if migration completed)"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
