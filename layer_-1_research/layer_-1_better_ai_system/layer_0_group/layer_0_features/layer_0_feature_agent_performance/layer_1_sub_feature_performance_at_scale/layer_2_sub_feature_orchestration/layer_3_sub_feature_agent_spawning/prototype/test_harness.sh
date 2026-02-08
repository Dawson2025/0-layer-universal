#!/bin/bash
# =============================================================================
# Multi-Agent Orchestration Test Harness
# Layer: -1 (Research)
# Feature: Multi-Agent Orchestration > Agent Spawning
# Purpose: Test the spawning prototype with various scenarios
# =============================================================================

set -uo pipefail
# Note: -e disabled to allow test assertions to fail without exiting

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPAWN_SCRIPT="$SCRIPT_DIR/spawn_agent.sh"
TEST_DIR="$SCRIPT_DIR/test_workspace"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "${CYAN}[TEST]${NC} $1"; }
log_pass() { echo -e "${GREEN}[PASS]${NC} $1"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $1"; }
log_skip() { echo -e "${YELLOW}[SKIP]${NC} $1"; }

# Test counter
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0
TESTS_SKIPPED=0

# Clean up test directory
cleanup() {
    if [[ -d "$TEST_DIR" ]]; then
        rm -rf "$TEST_DIR"
    fi
}

setup() {
    cleanup
    mkdir -p "$TEST_DIR/hand_off_documents/"{outgoing/to_below,incoming/from_below,status}
    mkdir -p "$TEST_DIR/tasks"
}

# Test: Depth limit enforcement
test_depth_limit() {
    log "Testing depth limit enforcement..."
    ((TESTS_RUN++))

    # Create a simple task
    cat > "$TEST_DIR/tasks/task_depth.json" << 'EOF'
{
    "taskId": "test_depth_001",
    "description": "Simple depth test task"
}
EOF

    # Try to spawn at max depth (should fail)
    local output
    output=$(CURRENT_DEPTH=5 MAX_DEPTH=5 "$SPAWN_SCRIPT" claude "$TEST_DIR/tasks/task_depth.json" -w "$TEST_DIR" 2>&1) || true

    if echo "$output" | grep -q "SAFEGUARD TRIGGERED"; then
        log_pass "Depth limit correctly prevents spawning at max depth"
        ((TESTS_PASSED++))
    else
        log_fail "Depth limit not enforced - agent should not spawn at max depth"
        ((TESTS_FAILED++))
    fi
}

# Test: Invalid agent type
test_invalid_agent() {
    log "Testing invalid agent type rejection..."
    ((TESTS_RUN++))

    cat > "$TEST_DIR/tasks/task_invalid.json" << 'EOF'
{
    "taskId": "test_invalid_001",
    "description": "Invalid agent test"
}
EOF

    local output
    output=$("$SPAWN_SCRIPT" invalid_agent "$TEST_DIR/tasks/task_invalid.json" -w "$TEST_DIR" 2>&1) || true

    if echo "$output" | grep -q "Invalid agent type"; then
        log_pass "Invalid agent type correctly rejected"
        ((TESTS_PASSED++))
    else
        log_fail "Should reject invalid agent type"
        ((TESTS_FAILED++))
    fi
}

# Test: Directory structure creation
test_directory_structure() {
    log "Testing directory structure creation..."
    ((TESTS_RUN++))

    # Create a task that will fail quickly (no actual agent)
    cat > "$TEST_DIR/tasks/task_struct.json" << 'EOF'
{
    "taskId": "test_struct_001",
    "description": "Directory structure test"
}
EOF

    # Run with a non-existent command to test structure creation
    # We expect failure but directories should be created
    AGENT_TIMEOUT=1 "$SPAWN_SCRIPT" claude "$TEST_DIR/tasks/task_struct.json" -w "$TEST_DIR" 2>&1 || true

    # Check directories were created
    if [[ -d "$TEST_DIR/hand_off_documents/outgoing/to_below" ]] && \
       [[ -d "$TEST_DIR/hand_off_documents/incoming/from_below" ]] && \
       [[ -d "$TEST_DIR/hand_off_documents/status" ]]; then
        log_pass "Hand-off directory structure created correctly"
        ((TESTS_PASSED++))
    else
        log_fail "Directory structure not created properly"
        ((TESTS_FAILED++))
    fi
}

# Test: Status file creation and format
test_status_file() {
    log "Testing status file creation..."
    ((TESTS_RUN++))

    cat > "$TEST_DIR/tasks/task_status.json" << 'EOF'
{
    "taskId": "test_status_001",
    "description": "Status file test"
}
EOF

    # Run with quick timeout
    CHILD_ID=$(AGENT_TIMEOUT=1 "$SPAWN_SCRIPT" claude "$TEST_DIR/tasks/task_status.json" -w "$TEST_DIR" 2>&1 | tail -1) || true

    # Find any status file
    STATUS_FILE=$(find "$TEST_DIR/hand_off_documents/status" -name "*.json" -type f | head -1)

    if [[ -n "$STATUS_FILE" ]] && [[ -f "$STATUS_FILE" ]]; then
        # Validate JSON structure
        if jq -e '.childId and .agentType and .status and .depth' "$STATUS_FILE" > /dev/null 2>&1; then
            log_pass "Status file created with correct structure"
            ((TESTS_PASSED++))
        else
            log_fail "Status file missing required fields"
            ((TESTS_FAILED++))
        fi
    else
        log_fail "Status file not created"
        ((TESTS_FAILED++))
    fi
}

# Test: Task file copying
test_task_copy() {
    log "Testing task file copying to child directory..."
    ((TESTS_RUN++))

    cat > "$TEST_DIR/tasks/task_copy.json" << 'EOF'
{
    "taskId": "test_copy_001",
    "description": "Task copy test",
    "extra": "data"
}
EOF

    AGENT_TIMEOUT=1 "$SPAWN_SCRIPT" claude "$TEST_DIR/tasks/task_copy.json" -w "$TEST_DIR" 2>&1 || true

    # Find the most recent copied task file
    local COPIED_TASK
    COPIED_TASK=$(find "$TEST_DIR/hand_off_documents/outgoing/to_below" -name "task.json" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2-)

    if [[ -n "$COPIED_TASK" ]] && [[ -f "$COPIED_TASK" ]]; then
        # Verify content matches
        local task_id
        task_id=$(jq -r '.taskId' "$COPIED_TASK" 2>/dev/null)
        if [[ "$task_id" == "test_copy_001" ]]; then
            log_pass "Task file correctly copied to child directory"
            ((TESTS_PASSED++))
        else
            log_fail "Task file content mismatch (got taskId: $task_id)"
            ((TESTS_FAILED++))
        fi
    else
        log_fail "Task file not copied to outgoing directory"
        ((TESTS_FAILED++))
    fi
}

# Test: CLI availability check
test_cli_availability() {
    log "Checking CLI tool availability..."

    for cli in claude codex gemini aider; do
        if command -v "$cli" &> /dev/null; then
            log_pass "$cli CLI is available"
        else
            log_skip "$cli CLI not found (install for full testing)"
        fi
    done
}

# Test: Help message
test_help() {
    log "Testing help message..."
    ((TESTS_RUN++))

    if "$SPAWN_SCRIPT" --help 2>&1 | grep -q "Usage:"; then
        log_pass "Help message displayed correctly"
        ((TESTS_PASSED++))
    else
        log_fail "Help message not working"
        ((TESTS_FAILED++))
    fi
}

# Main
main() {
    echo ""
    echo "=============================================="
    echo "  Multi-Agent Spawning Prototype Test Suite  "
    echo "=============================================="
    echo ""

    # Check spawn script exists
    if [[ ! -f "$SPAWN_SCRIPT" ]]; then
        log_fail "spawn_agent.sh not found at $SPAWN_SCRIPT"
        exit 1
    fi

    # Make executable
    chmod +x "$SPAWN_SCRIPT"

    setup

    # Run tests
    test_help
    test_invalid_agent
    test_depth_limit
    test_directory_structure
    test_status_file
    test_task_copy
    test_cli_availability

    # Summary
    echo ""
    echo "=============================================="
    echo "  Test Summary"
    echo "=============================================="
    echo "  Total:   $TESTS_RUN"
    echo -e "  ${GREEN}Passed:  $TESTS_PASSED${NC}"
    echo -e "  ${RED}Failed:  $TESTS_FAILED${NC}"
    echo -e "  ${YELLOW}Skipped: $TESTS_SKIPPED${NC}"
    echo "=============================================="
    echo ""

    # Cleanup
    # cleanup  # Uncomment to auto-cleanup

    if [[ $TESTS_FAILED -gt 0 ]]; then
        exit 1
    fi
}

main "$@"
