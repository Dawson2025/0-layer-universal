#!/bin/bash
#
# integration-test.sh - Test all Better AI System components
#
# Tests:
#   1. AGNOSTIC system (0AGNOSTIC.md + agnostic-sync.sh)
#   2. Episodic memory (sessions, logs, index)
#   3. Multi-agent sync (file locking)
#   4. Automated traversal (0INDEX.md + find helper)
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0

# Test directory
LAYER_0="${LAYER_0:-$(cd "$(dirname "$0")/../.." && pwd)}"
SCRIPTS_DIR="$LAYER_0/.0agnostic/scripts"

echo "=========================================="
echo "Better AI System Integration Tests"
echo "=========================================="
echo "Testing in: $LAYER_0"
echo ""

# Helper function for test results
pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    PASSED=$((PASSED + 1))
}

fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    FAILED=$((FAILED + 1))
}

warn() {
    echo -e "${YELLOW}! WARN${NC}: $1"
}

###########################################
# Test 1: AGNOSTIC System
###########################################
echo ""
echo "--- Test 1: AGNOSTIC System ---"

# Test 1.1: 0AGNOSTIC.md exists
if [ -f "$LAYER_0/0AGNOSTIC.md" ]; then
    pass "0AGNOSTIC.md exists"
else
    fail "0AGNOSTIC.md not found"
fi

# Test 1.2: .0agnostic/ folder exists
if [ -d "$LAYER_0/.0agnostic" ]; then
    pass ".0agnostic/ folder exists"
else
    fail ".0agnostic/ folder not found"
fi

# Test 1.3: agnostic-sync.sh exists and is executable
if [ -x "$LAYER_0/.0agnostic/agnostic-sync.sh" ]; then
    pass "agnostic-sync.sh is executable"
else
    fail "agnostic-sync.sh not found or not executable"
fi

# Test 1.4: Tool-specific files generated
for tool_file in CLAUDE.md AGENTS.md GEMINI.md OPENAI.md; do
    if [ -f "$LAYER_0/$tool_file" ]; then
        pass "$tool_file generated"
    else
        fail "$tool_file not found"
    fi
done

# Test 1.5: CLAUDE.md contains auto-generated marker
if grep -q "Auto-generated from 0AGNOSTIC.md" "$LAYER_0/CLAUDE.md" 2>/dev/null; then
    pass "CLAUDE.md has auto-generated marker"
else
    fail "CLAUDE.md missing auto-generated marker"
fi

###########################################
# Test 2: Episodic Memory System
###########################################
echo ""
echo "--- Test 2: Episodic Memory System ---"

# Test 2.1: Episodic folder structure
if [ -d "$LAYER_0/.0agnostic/episodic_memory/sessions" ] && [ -d "$LAYER_0/.0agnostic/episodic_memory/changes" ]; then
    pass "Episodic folder structure exists"
else
    fail "Episodic folder structure incomplete"
fi

# Test 2.2: index.md exists
if [ -f "$LAYER_0/.0agnostic/episodic_memory/index.md" ]; then
    pass "Episodic index.md exists"
else
    fail "Episodic index.md not found"
fi

# Test 2.3: divergence.log exists
if [ -f "$LAYER_0/.0agnostic/episodic_memory/changes/divergence.log" ]; then
    pass "divergence.log exists"
else
    fail "divergence.log not found"
fi

# Test 2.4: conflicts.log exists
if [ -f "$LAYER_0/.0agnostic/episodic_memory/changes/conflicts.log" ]; then
    pass "conflicts.log exists"
else
    fail "conflicts.log not found"
fi

# Test 2.5: At least one session file exists
if ls "$LAYER_0/.0agnostic/episodic_memory/sessions/"*.md >/dev/null 2>&1; then
    pass "Session files exist"
else
    fail "No session files found"
fi

###########################################
# Test 3: Multi-Agent Sync System
###########################################
echo ""
echo "--- Test 3: Multi-Agent Sync System ---"

# Test 3.1: .locks/ directory exists
if [ -d "$LAYER_0/.locks" ]; then
    pass ".locks/ directory exists"
else
    fail ".locks/ directory not found"
fi

# Test 3.2: lock-manager.sh exists and is executable
if [ -x "$SCRIPTS_DIR/lock-manager.sh" ]; then
    pass "lock-manager.sh is executable"
else
    fail "lock-manager.sh not found or not executable"
fi

# Test 3.3: Lock acquire/release cycle works
cd "$LAYER_0"
if bash "$SCRIPTS_DIR/lock-manager.sh" acquire test_integration test_agent 1 >/dev/null 2>&1; then
    if bash "$SCRIPTS_DIR/lock-manager.sh" release test_integration test_agent >/dev/null 2>&1; then
        pass "Lock acquire/release cycle works"
    else
        fail "Lock release failed"
    fi
else
    fail "Lock acquire failed"
fi

# Test 3.4: atomic-write.sh exists
if [ -x "$SCRIPTS_DIR/atomic-write.sh" ]; then
    pass "atomic-write.sh is executable"
else
    fail "atomic-write.sh not found or not executable"
fi

# Test 3.5: track-change.sh exists
if [ -x "$SCRIPTS_DIR/track-change.sh" ]; then
    pass "track-change.sh is executable"
else
    fail "track-change.sh not found or not executable"
fi

###########################################
# Test 4: Automated Traversal System
###########################################
echo ""
echo "--- Test 4: Automated Traversal System ---"

ROOT_DIR="$(dirname "$LAYER_0")"

# Test 4.1: Root 0INDEX.md exists
if [ -f "$ROOT_DIR/0INDEX.md" ]; then
    pass "Root 0INDEX.md exists"
else
    fail "Root 0INDEX.md not found"
fi

# Test 4.2: layer_0 0INDEX.md exists
if [ -f "$LAYER_0/0INDEX.md" ]; then
    pass "layer_0 0INDEX.md exists"
else
    fail "layer_0 0INDEX.md not found"
fi

# Test 4.3: find-helper.sh exists and works
if [ -x "$SCRIPTS_DIR/find-helper.sh" ]; then
    if bash "$SCRIPTS_DIR/find-helper.sh" all >/dev/null 2>&1; then
        pass "find-helper.sh works"
    else
        fail "find-helper.sh execution failed"
    fi
else
    fail "find-helper.sh not found or not executable"
fi

# Test 4.4: /find skill documentation exists
if [ -f "$LAYER_0/.0agnostic/skills/find.md" ]; then
    pass "/find skill documentation exists"
else
    fail "/find skill documentation not found"
fi

# Test 4.5: At least 3 0INDEX.md files exist
INDEX_COUNT=$(find "$ROOT_DIR" -name "0INDEX.md" 2>/dev/null | wc -l)
if [ "$INDEX_COUNT" -ge 3 ]; then
    pass "$INDEX_COUNT 0INDEX.md files found (minimum 3)"
else
    fail "Only $INDEX_COUNT 0INDEX.md files found (need at least 3)"
fi

###########################################
# Test 5: Integration - All Systems Together
###########################################
echo ""
echo "--- Test 5: Integration Tests ---"

# Test 5.1: Rules files exist in .0agnostic/rules/
RULES_COUNT=$(find "$LAYER_0/.0agnostic/rules" -name "*.md" 2>/dev/null | wc -l)
if [ "$RULES_COUNT" -ge 3 ]; then
    pass "$RULES_COUNT rule files found in .0agnostic/rules/"
else
    fail "Only $RULES_COUNT rule files found (need at least 3)"
fi

# Test 5.2: Episodic index references session files
if grep -q "sessions/" "$LAYER_0/.0agnostic/episodic_memory/index.md" 2>/dev/null; then
    pass "Episodic index references session files"
else
    fail "Episodic index doesn't reference sessions"
fi

# Test 5.3: 0AGNOSTIC.md mentions episodic memory
if grep -qi "episodic" "$LAYER_0/0AGNOSTIC.md" 2>/dev/null; then
    pass "0AGNOSTIC.md mentions episodic memory"
else
    warn "0AGNOSTIC.md doesn't mention episodic memory"
fi

# Test 5.4: 0INDEX.md children table format correct
if grep -qE "^\| [a-zA-Z0-9_.-]+ \| (dir|file) \|" "$LAYER_0/0INDEX.md" 2>/dev/null; then
    pass "0INDEX.md children table format correct"
else
    fail "0INDEX.md children table format incorrect"
fi

###########################################
# Summary
###########################################
echo ""
echo "=========================================="
echo "Test Summary"
echo "=========================================="
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ "$FAILED" -eq 0 ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    echo "Better AI System is fully operational."
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    echo "Please review and fix the failing components."
    exit 1
fi

