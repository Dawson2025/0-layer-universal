#!/usr/bin/env bash
# Structural tests for I0_FILE_CHANGE_REPORTING rule
# Usage: bash test_structural.sh [repo_root]

REPO_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../../.." && pwd)}"
RULE_FILE="$REPO_ROOT/.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md"
CLAUDE_MD="$REPO_ROOT/CLAUDE.md"
GLOBAL_CLAUDE="$HOME/.claude/CLAUDE.md"
HOME_RULE="$HOME/.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md"

PASS=0; FAIL=0

check() {
    local name="$1" result="$2"
    if [ "$result" = "0" ]; then
        echo "  PASS: $name"
        PASS=$((PASS + 1))
    else
        echo "  FAIL: $name"
        FAIL=$((FAIL + 1))
    fi
}

# TC-FCR-01: Rule file exists with correct frontmatter
if [ -f "$RULE_FILE" ]; then
    check "TC-FCR-01a: Rule file exists" 0
    if head -10 "$RULE_FILE" | grep -q 'promote: hot'; then
        check "TC-FCR-01b: promote: hot in frontmatter" 0
    else
        check "TC-FCR-01b: promote: hot in frontmatter" 1
    fi
    if head -10 "$RULE_FILE" | grep -q 'hot_summary:'; then
        check "TC-FCR-01c: hot_summary present" 0
    else
        check "TC-FCR-01c: hot_summary present" 1
    fi
    if head -10 "$RULE_FILE" | grep -q 'hot_trigger:'; then
        check "TC-FCR-01d: hot_trigger present" 0
    else
        check "TC-FCR-01d: hot_trigger present" 1
    fi
    if grep -q 'full absolute paths' "$RULE_FILE"; then
        check "TC-FCR-01e: mentions full absolute paths" 0
    else
        check "TC-FCR-01e: mentions full absolute paths" 1
    fi
    if grep -q 'Inline references' "$RULE_FILE" && grep -q 'End-of-turn summary' "$RULE_FILE"; then
        check "TC-FCR-01f: two-part structure (inline + summary)" 0
    else
        check "TC-FCR-01f: two-part structure (inline + summary)" 1
    fi
else
    check "TC-FCR-01: Rule file exists" 1
fi

# TC-FCR-02: Hot rule in CLAUDE.md
if [ -f "$CLAUDE_MD" ]; then
    if grep -q 'Promoted Rules' "$CLAUDE_MD" && grep -q 'modifies files' "$CLAUDE_MD"; then
        check "TC-FCR-02: Hot rule in CLAUDE.md Promoted Rules" 0
    else
        check "TC-FCR-02: Hot rule in CLAUDE.md Promoted Rules" 1
    fi
else
    check "TC-FCR-02: CLAUDE.md exists" 1
fi

# TC-FCR-04: Global CLAUDE.md reference
if [ -f "$GLOBAL_CLAUDE" ]; then
    if grep -qi 'file change reporting\|I0_FILE_CHANGE_REPORTING' "$GLOBAL_CLAUDE"; then
        check "TC-FCR-04: Global CLAUDE.md references rule" 0
    else
        check "TC-FCR-04: Global CLAUDE.md references rule" 1
    fi
else
    check "TC-FCR-04: Global CLAUDE.md exists" 1
fi

# TC-FCR-13: Home directory copy in sync
if [ -f "$HOME_RULE" ]; then
    if diff -q "$RULE_FILE" "$HOME_RULE" > /dev/null 2>&1; then
        check "TC-FCR-13: Home copy in sync with repo" 0
    else
        check "TC-FCR-13: Home copy in sync with repo" 1
    fi
else
    check "TC-FCR-13: Home copy exists" 1
fi

echo ""
echo "Results: $PASS PASS, $FAIL FAIL"
[ "$FAIL" -eq 0 ]
