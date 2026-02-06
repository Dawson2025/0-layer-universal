#!/bin/bash
# =============================================================================
# Orchestrator Integration Test
# Layer: 0 (Universal)
# Purpose: Test layer_0_orchestrator.gab.jsonld integration with spawn system
# =============================================================================

set -uo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTEXT_AGENTS_DIR="$(dirname "$SCRIPT_DIR")"
# Path: personal -> ai_manager_system -> layer_0 -> 0_layer_universal (3 levels)
LAYER_UNIVERSAL_DIR="$(cd "$CONTEXT_AGENTS_DIR/../../.." && pwd)"
HAND_OFF_DIR="$LAYER_UNIVERSAL_DIR/layer_0/layer_0_02_manager_handoff_documents"
SPAWN_SCRIPT="$LAYER_UNIVERSAL_DIR/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_multi_agent_orchestration/layer_1_sub_feature_agent_spawning/prototype/spawn_agent.sh"

# Test counters
TESTS_PASSED=0
TESTS_FAILED=0

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_pass() { echo -e "${GREEN}[PASS]${NC} $1"; }
log_fail() { echo -e "${RED}[FAIL]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }

echo "=============================================="
echo "  Orchestrator Integration Test Suite"
echo "=============================================="
echo ""
log_info "Context Agents Dir: $CONTEXT_AGENTS_DIR"
log_info "Layer Universal Dir: $LAYER_UNIVERSAL_DIR"
log_info "Hand-off Dir: $HAND_OFF_DIR"
log_info "Spawn Script: $SPAWN_SCRIPT"
echo ""

# Test 1: Verify orchestrator JSON-LD files exist and are valid
test_orchestrator_files() {
    log_info "[TEST 1] Verifying orchestrator files..."

    local orchestrator="$CONTEXT_AGENTS_DIR/layer_0_orchestrator.gab.jsonld"
    local runtime="$CONTEXT_AGENTS_DIR/runtime/orchestrator_runtime.jsonld"

    if [[ -f "$orchestrator" ]]; then
        if jq empty "$orchestrator" 2>/dev/null; then
            log_pass "layer_0_orchestrator.gab.jsonld exists and is valid JSON"
            ((TESTS_PASSED++))
        else
            log_fail "layer_0_orchestrator.gab.jsonld is invalid JSON"
            ((TESTS_FAILED++))
        fi
    else
        log_fail "layer_0_orchestrator.gab.jsonld not found"
        ((TESTS_FAILED++))
    fi

    if [[ -f "$runtime" ]]; then
        if jq empty "$runtime" 2>/dev/null; then
            log_pass "orchestrator_runtime.jsonld exists and is valid JSON"
            ((TESTS_PASSED++))
        else
            log_fail "orchestrator_runtime.jsonld is invalid JSON"
            ((TESTS_FAILED++))
        fi
    else
        log_fail "orchestrator_runtime.jsonld not found"
        ((TESTS_FAILED++))
    fi
}

# Test 2: Verify hand_off_documents structure
test_handoff_structure() {
    log_info "[TEST 2] Verifying hand_off_documents structure..."

    local dirs=(
        "$HAND_OFF_DIR/incoming/from_above"
        "$HAND_OFF_DIR/incoming/from_below"
        "$HAND_OFF_DIR/outgoing/to_above"
        "$HAND_OFF_DIR/outgoing/to_below"
        "$HAND_OFF_DIR/status"
    )

    local all_exist=true
    for dir in "${dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            log_warn "Missing directory: $dir"
            all_exist=false
        fi
    done

    if $all_exist; then
        log_pass "All hand_off_documents directories exist"
        ((TESTS_PASSED++))
    else
        log_fail "Some hand_off_documents directories missing"
        ((TESTS_FAILED++))
    fi
}

# Test 3: Verify spawn script exists and has required safeguards
test_spawn_script() {
    log_info "[TEST 3] Verifying spawn script safeguards..."

    if [[ ! -f "$SPAWN_SCRIPT" ]]; then
        log_fail "spawn_agent.sh not found at: $SPAWN_SCRIPT"
        ((TESTS_FAILED++))
        return
    fi

    # Check for depth limit safeguard
    if grep -q "MAX_DEPTH" "$SPAWN_SCRIPT" && grep -q "SAFEGUARD" "$SPAWN_SCRIPT"; then
        log_pass "Spawn script has depth limit safeguard"
        ((TESTS_PASSED++))
    else
        log_fail "Spawn script missing depth limit safeguard"
        ((TESTS_FAILED++))
    fi
}

# Test 4: Verify orchestrator has required modes
test_orchestrator_modes() {
    log_info "[TEST 4] Verifying orchestrator modes..."

    local orchestrator="$CONTEXT_AGENTS_DIR/layer_0_orchestrator.gab.jsonld"

    local modes=("ReceiveMode" "DelegationMode" "MonitoringMode" "AggregationMode" "ReportMode")
    local all_modes=true

    for mode in "${modes[@]}"; do
        if ! jq -e ".\"@graph\"[] | select(.\"@id\" | contains(\"$mode\"))" "$orchestrator" > /dev/null 2>&1; then
            log_warn "Missing mode: $mode"
            all_modes=false
        fi
    done

    if $all_modes; then
        log_pass "All 5 orchestrator modes defined"
        ((TESTS_PASSED++))
    else
        log_fail "Some orchestrator modes missing"
        ((TESTS_FAILED++))
    fi
}

# Test 5: Verify orchestrator has required state actors
test_orchestrator_state_actors() {
    log_info "[TEST 5] Verifying orchestrator state actors..."

    local orchestrator="$CONTEXT_AGENTS_DIR/layer_0_orchestrator.gab.jsonld"

    local actors=("LayerStateActor" "ChildRegistryStateActor" "TaskStateActor" "ResourceBudgetStateActor" "StageStateActor")
    local all_actors=true

    for actor in "${actors[@]}"; do
        if ! jq -e ".\"@graph\"[] | select(.\"@id\" | contains(\"$actor\"))" "$orchestrator" > /dev/null 2>&1; then
            log_warn "Missing state actor: $actor"
            all_actors=false
        fi
    done

    if $all_actors; then
        log_pass "All 5 state actors defined"
        ((TESTS_PASSED++))
    else
        log_fail "Some state actors missing"
        ((TESTS_FAILED++))
    fi
}

# Test 6: Verify orchestrator prohibitions include depth and similarity safeguards
test_orchestrator_prohibitions() {
    log_info "[TEST 6] Verifying orchestrator prohibitions..."

    local orchestrator="$CONTEXT_AGENTS_DIR/layer_0_orchestrator.gab.jsonld"

    # Check for depth limit prohibition
    if jq -e '.prohibitions[] | select(.action | contains("recursion depth"))' "$orchestrator" > /dev/null 2>&1; then
        log_pass "Depth limit prohibition defined"
        ((TESTS_PASSED++))
    else
        log_fail "Depth limit prohibition missing"
        ((TESTS_FAILED++))
    fi

    # Check for task similarity prohibition
    if jq -e '.prohibitions[] | select(.action | contains("identical task"))' "$orchestrator" > /dev/null 2>&1; then
        log_pass "Task similarity prohibition defined"
        ((TESTS_PASSED++))
    else
        log_fail "Task similarity prohibition missing"
        ((TESTS_FAILED++))
    fi
}

# Test 7: Create and validate a test task
test_task_creation() {
    log_info "[TEST 7] Testing task creation in hand_off_documents..."

    local test_task_file="$HAND_OFF_DIR/incoming/from_above/test_task_$(date +%s).json"

    cat > "$test_task_file" << 'EOF'
{
    "taskId": "integration_test_001",
    "description": "Integration test task for orchestrator verification",
    "agentType": "claude",
    "context": {
        "layer": 0,
        "stage": "07",
        "paths": ["."],
        "constraints": {
            "maxRecursionDepth": 2,
            "timeout": "30s"
        }
    },
    "priority": "normal",
    "expectedOutcome": "Write a simple result file to verify the flow"
}
EOF

    if [[ -f "$test_task_file" ]] && jq empty "$test_task_file" 2>/dev/null; then
        log_pass "Test task created and is valid JSON"
        ((TESTS_PASSED++))

        # Clean up
        rm -f "$test_task_file"
    else
        log_fail "Failed to create valid test task"
        ((TESTS_FAILED++))
    fi
}

# Test 8: Verify runtime protocols are defined
test_runtime_protocols() {
    log_info "[TEST 8] Verifying runtime protocols..."

    local runtime="$CONTEXT_AGENTS_DIR/runtime/orchestrator_runtime.jsonld"

    local protocols=("SpawnProtocol" "HandoffDocumentProtocol" "ErrorHandlingProtocol" "CircuitBreakerProtocol")
    local all_protocols=true

    for protocol in "${protocols[@]}"; do
        if ! jq -e ".\"@graph\"[] | select(.\"@id\" | contains(\"$protocol\"))" "$runtime" > /dev/null 2>&1; then
            log_warn "Missing protocol: $protocol"
            all_protocols=false
        fi
    done

    if $all_protocols; then
        log_pass "All runtime protocols defined"
        ((TESTS_PASSED++))
    else
        log_fail "Some runtime protocols missing"
        ((TESTS_FAILED++))
    fi
}

# Test 9: End-to-end spawn test (dry run - checks structure only)
test_spawn_dry_run() {
    log_info "[TEST 9] Spawn script dry run (help output)..."

    if [[ ! -f "$SPAWN_SCRIPT" ]]; then
        log_warn "Skipping - spawn script not found"
        return
    fi

    local help_output
    help_output=$("$SPAWN_SCRIPT" --help 2>&1) || true

    if echo "$help_output" | grep -q "agent_type"; then
        log_pass "Spawn script help works correctly"
        ((TESTS_PASSED++))
    else
        log_fail "Spawn script help not working"
        ((TESTS_FAILED++))
    fi
}

# Test 10: Verify project orchestrator template
test_project_template() {
    log_info "[TEST 10] Verifying project orchestrator template..."

    local template="$LAYER_UNIVERSAL_DIR/layer_1/layer_1_projects/layer_1_project_default/project_orchestrator.gab.jsonld"

    if [[ -f "$template" ]]; then
        if jq empty "$template" 2>/dev/null; then
            # Check for template placeholders
            if jq -e '.\"@graph\"[] | select(.projectId == "TEMPLATE_PROJECT_ID")' "$template" > /dev/null 2>&1; then
                log_pass "Project orchestrator template exists with placeholders"
                ((TESTS_PASSED++))
            else
                log_warn "Project orchestrator exists but may already be customized"
                ((TESTS_PASSED++))
            fi
        else
            log_fail "Project orchestrator template is invalid JSON"
            ((TESTS_FAILED++))
        fi
    else
        log_fail "Project orchestrator template not found"
        ((TESTS_FAILED++))
    fi
}

# Run all tests
test_orchestrator_files
test_handoff_structure
test_spawn_script
test_orchestrator_modes
test_orchestrator_state_actors
test_orchestrator_prohibitions
test_task_creation
test_runtime_protocols
test_spawn_dry_run
test_project_template

# Summary
echo ""
echo "=============================================="
echo "  Test Summary"
echo "=============================================="
echo -e "  ${GREEN}Passed${NC}: $TESTS_PASSED"
echo -e "  ${RED}Failed${NC}: $TESTS_FAILED"
echo "=============================================="

if [[ $TESTS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    exit 1
fi
