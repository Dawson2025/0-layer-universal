#!/usr/bin/env bash
# Structural tests for AI_CONTEXT_MODIFICATION_PROTOCOL
# Usage: bash test_structural.sh [repo_root]

REPO_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../../.." && pwd)}"
RULE_FILE="$REPO_ROOT/.0agnostic/02_rules/0_every_api_request/AI_CONTEXT_MODIFICATION_PROTOCOL/AI_CONTEXT_MODIFICATION_PROTOCOL.md"
CLAUDE_MD="$REPO_ROOT/CLAUDE.md"
AGNOSTIC_MD="$REPO_ROOT/0AGNOSTIC.md"

PASS=0; FAIL=0

check() {
    local name="$1" result="$2"
    if [ "$result" = "0" ]; then echo "  PASS: $name"; PASS=$((PASS + 1))
    else echo "  FAIL: $name"; FAIL=$((FAIL + 1)); fi
}

# TC-ACMP-01: Rule file exists with two-tier structure
if [ -f "$RULE_FILE" ]; then
    check "TC-ACMP-01a: Rule file exists" 0
    if grep -q 'Tier 1' "$RULE_FILE" && grep -q 'Tier 2' "$RULE_FILE"; then
        check "TC-ACMP-01b: Two-tier structure present" 0
    else
        check "TC-ACMP-01b: Two-tier structure present" 1
    fi
    if grep -q 'AI Context' "$RULE_FILE" && grep -q 'General Filesystem' "$RULE_FILE"; then
        check "TC-ACMP-01c: Both tier names present" 0
    else
        check "TC-ACMP-01c: Both tier names present" 1
    fi
else
    check "TC-ACMP-01: Rule file exists" 1
fi

# TC-ACMP-02: Referenced in CLAUDE.md
if [ -f "$CLAUDE_MD" ]; then
    if grep -qi 'AI Context Modification\|Filesystem Change Visualization' "$CLAUDE_MD"; then
        check "TC-ACMP-02a: Referenced in CLAUDE.md" 0
    else
        check "TC-ACMP-02a: Referenced in CLAUDE.md" 1
    fi
fi

# TC-ACMP-03: Tier 1 scope patterns
if [ -f "$RULE_FILE" ]; then
    SCOPE_PASS=0
    for pattern in '0AGNOSTIC.md' '.0agnostic/' '.1merge/' 'CLAUDE.md' 'AGENTS.md' 'status.json'; do
        grep -q "$pattern" "$RULE_FILE" && SCOPE_PASS=$((SCOPE_PASS + 1))
    done
    if [ "$SCOPE_PASS" -ge 5 ]; then
        check "TC-ACMP-03: Tier 1 scope covers AI context patterns" 0
    else
        check "TC-ACMP-03: Tier 1 scope covers AI context patterns ($SCOPE_PASS/6)" 1
    fi
fi

# TC-ACMP-04: Tier 2 triggers
if [ -f "$RULE_FILE" ]; then
    if grep -q '2+ directories\|creating 2+' "$RULE_FILE" 2>/dev/null || grep -qi 'Creating.*director' "$RULE_FILE"; then
        check "TC-ACMP-04a: Tier 2 directory trigger" 0
    else
        check "TC-ACMP-04a: Tier 2 directory trigger" 1
    fi
    if grep -qi 'exempt\|single file' "$RULE_FILE"; then
        check "TC-ACMP-04b: Tier 2 exemptions defined" 0
    else
        check "TC-ACMP-04b: Tier 2 exemptions defined" 1
    fi
fi

# TC-ACMP-05: Diagram requirements
if [ -f "$RULE_FILE" ]; then
    if grep -qi 'Diagram Requirements\|diagram MUST' "$RULE_FILE"; then
        check "TC-ACMP-05: Diagram requirements section exists" 0
    else
        check "TC-ACMP-05: Diagram requirements section exists" 1
    fi
fi

echo ""
echo "Results: $PASS PASS, $FAIL FAIL"
[ "$FAIL" -eq 0 ]
