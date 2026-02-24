#!/usr/bin/env bash
# Structural tests for STAGE_REPORT_RULE
# Usage: bash test_structural.sh [repo_root]

REPO_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../../.." && pwd)}"
RULE_FILE="$REPO_ROOT/.0agnostic/02_rules/static/STAGE_REPORT_RULE/STAGE_REPORT_RULE.md"
PROTOCOL="$REPO_ROOT/.0agnostic/03_protocols/stage_report_protocol.md"

PASS=0; FAIL=0

check() {
    local name="$1" result="$2"
    if [ "$result" = "0" ]; then echo "  PASS: $name"; PASS=$((PASS + 1))
    else echo "  FAIL: $name"; FAIL=$((FAIL + 1)); fi
}

if [ -f "$RULE_FILE" ]; then
    check "TC-SRR-01a: Rule file exists" 0
    if grep -q 'stage_report' "$RULE_FILE"; then
        check "TC-SRR-01b: References stage_report" 0
    else
        check "TC-SRR-01b: References stage_report" 1
    fi
else
    check "TC-SRR-01: Rule file exists" 1
fi

if [ -f "$PROTOCOL" ]; then
    check "TC-SRR-02a: Protocol exists" 0
    if grep -q '01_to_above' "$PROTOCOL" && grep -q '03_to_below' "$PROTOCOL"; then
        check "TC-SRR-02b: Protocol has both directions" 0
    else
        check "TC-SRR-02b: Protocol has both directions" 1
    fi
    if grep -q '30 lines\|under 30' "$PROTOCOL"; then
        check "TC-SRR-02c: Protocol mentions line limit" 0
    else
        check "TC-SRR-02c: Protocol mentions line limit" 1
    fi
else
    check "TC-SRR-02: Protocol exists" 1
fi

echo ""
echo "Results: $PASS PASS, $FAIL FAIL"
[ "$FAIL" -eq 0 ]
