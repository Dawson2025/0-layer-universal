#!/bin/bash
#
# edge-case-tests.sh - Test edge cases and stress scenarios
#

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASSED=0
FAILED=0
WARNINGS=0

LAYER_0="${LAYER_0:-$(cd "$(dirname "$0")/../.." && pwd)}"
SCRIPTS_DIR="$LAYER_0/.0agnostic/scripts"

echo "=========================================="
echo "Edge Case & Stress Tests"
echo "=========================================="
echo ""

pass() { echo -e "${GREEN}✓ PASS${NC}: $1"; PASSED=$((PASSED + 1)); }
fail() { echo -e "${RED}✗ FAIL${NC}: $1"; FAILED=$((FAILED + 1)); }
warn() { echo -e "${YELLOW}! WARN${NC}: $1"; WARNINGS=$((WARNINGS + 1)); }

cd "$LAYER_0"

###########################################
# Edge Case 1: Lock Contention
###########################################
echo "--- Edge Case 1: Lock Contention ---"

# Test: Second agent cannot acquire same scope lock
bash "$SCRIPTS_DIR/lock-manager.sh" acquire contention_test agent_A 1 >/dev/null 2>&1
if bash "$SCRIPTS_DIR/lock-manager.sh" acquire contention_test agent_B 1 >/dev/null 2>&1; then
    fail "Second agent should not acquire lock held by first"
    bash "$SCRIPTS_DIR/lock-manager.sh" release contention_test agent_B >/dev/null 2>&1 || true
else
    pass "Lock contention correctly prevented"
fi
bash "$SCRIPTS_DIR/lock-manager.sh" release contention_test agent_A >/dev/null 2>&1

# Test: Same agent can refresh own lock
bash "$SCRIPTS_DIR/lock-manager.sh" acquire refresh_test agent_A 1 >/dev/null 2>&1
if bash "$SCRIPTS_DIR/lock-manager.sh" acquire refresh_test agent_A 1 >/dev/null 2>&1; then
    pass "Agent can refresh own lock"
else
    fail "Agent should be able to refresh own lock"
fi
bash "$SCRIPTS_DIR/lock-manager.sh" release refresh_test agent_A >/dev/null 2>&1

###########################################
# Edge Case 2: Atomic Write Safety
###########################################
echo ""
echo "--- Edge Case 2: Atomic Write Safety ---"

# Test: Atomic write creates file
TEST_FILE="$LAYER_0/.test_atomic_$$"
echo "test content" | bash "$SCRIPTS_DIR/atomic-write.sh" "$TEST_FILE" >/dev/null 2>&1
if [ -f "$TEST_FILE" ] && grep -q "test content" "$TEST_FILE"; then
    pass "Atomic write creates file correctly"
    rm -f "$TEST_FILE"
else
    fail "Atomic write failed"
fi

# Test: No temp files left behind
TEMP_FILES=$(find "$LAYER_0" -name ".atomic_*" 2>/dev/null | wc -l)
if [ "$TEMP_FILES" -eq 0 ]; then
    pass "No orphaned temp files"
else
    warn "$TEMP_FILES orphaned temp files found"
fi

###########################################
# Edge Case 3: 0INDEX.md Format Validation
###########################################
echo ""
echo "--- Edge Case 3: 0INDEX.md Format Validation ---"

ROOT_DIR="$(dirname "$LAYER_0")"

# Test: All 0INDEX.md files have Children table
ALL_VALID=true
for index_file in $(find "$ROOT_DIR" -name "0INDEX.md" 2>/dev/null); do
    if ! grep -q "## Children" "$index_file"; then
        fail "Missing Children section in $index_file"
        ALL_VALID=false
    fi
done
if $ALL_VALID; then
    pass "All 0INDEX.md files have Children section"
fi

# Test: All 0INDEX.md files have proper table format
ALL_VALID=true
for index_file in $(find "$ROOT_DIR" -name "0INDEX.md" 2>/dev/null); do
    if ! grep -qE "^\| [a-zA-Z0-9_.-]+ \| (dir|file) \|" "$index_file"; then
        warn "Table format issue in $index_file"
        ALL_VALID=false
    fi
done
if $ALL_VALID; then
    pass "All 0INDEX.md files have valid table format"
fi

###########################################
# Edge Case 4: Episodic Memory Integrity
###########################################
echo ""
echo "--- Edge Case 4: Episodic Memory Integrity ---"

# Test: divergence.log is append-only format
if head -1 "$LAYER_0/.0agnostic/episodic_memory/changes/divergence.log" | grep -q "^#"; then
    pass "divergence.log has header comment"
else
    warn "divergence.log missing header"
fi

# Test: Session files follow naming convention
INVALID_SESSIONS=$(find "$LAYER_0/.0agnostic/episodic_memory/sessions" -name "*.md" ! -name "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]_session_*.md" 2>/dev/null | wc -l)
if [ "$INVALID_SESSIONS" -eq 0 ]; then
    pass "All session files follow naming convention"
else
    warn "$INVALID_SESSIONS session files don't follow convention"
fi

# Test: index.md references existing sessions
if [ -f "$LAYER_0/.0agnostic/episodic_memory/index.md" ]; then
    pass "Episodic index exists and is readable"
else
    fail "Episodic index missing"
fi

###########################################
# Edge Case 5: Cross-Layer Consistency
###########################################
echo ""
echo "--- Edge Case 5: Cross-Layer Consistency ---"

# Test: All layers have 0AGNOSTIC.md
for layer in layer_0 layer_1 layer_-1_research; do
    if [ -f "$ROOT_DIR/$layer/0AGNOSTIC.md" ]; then
        pass "$layer has 0AGNOSTIC.md"
    else
        fail "$layer missing 0AGNOSTIC.md"
    fi
done

# Test: All layers have .locks directory
for layer in layer_0 layer_1 layer_-1_research; do
    if [ -d "$ROOT_DIR/$layer/.locks" ]; then
        pass "$layer has .locks/ directory"
    else
        fail "$layer missing .locks/ directory"
    fi
done

# Test: All layers have episodic structure
for layer in layer_0 layer_1 layer_-1_research; do
    if [ -d "$ROOT_DIR/$layer/.0agnostic/episodic_memory" ]; then
        pass "$layer has episodic memory structure"
    else
        fail "$layer missing episodic structure"
    fi
done

###########################################
# Edge Case 6: Script Robustness
###########################################
echo ""
echo "--- Edge Case 6: Script Robustness ---"

# Test: lock-manager.sh handles missing args gracefully
if bash "$SCRIPTS_DIR/lock-manager.sh" 2>&1 | grep -q "Usage"; then
    pass "lock-manager.sh shows usage on no args"
else
    fail "lock-manager.sh doesn't handle missing args"
fi

# Test: find-helper.sh handles missing args
if bash "$SCRIPTS_DIR/find-helper.sh" 2>&1 | grep -q "Usage"; then
    pass "find-helper.sh shows usage on no args"
else
    fail "find-helper.sh doesn't handle missing args"
fi

# Test: agnostic-sync.sh handles missing 0AGNOSTIC.md
if bash "$LAYER_0/.0agnostic/agnostic-sync.sh" /nonexistent 2>&1 | grep -qi "error\|not found"; then
    pass "agnostic-sync.sh handles missing file"
else
    warn "agnostic-sync.sh error handling unclear"
fi

###########################################
# Summary
###########################################
echo ""
echo "=========================================="
echo "Edge Case Test Summary"
echo "=========================================="
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ "$FAILED" -eq 0 ]; then
    echo -e "${GREEN}All edge case tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    exit 1
fi

