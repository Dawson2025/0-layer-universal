#!/bin/bash
# =============================================================================
# Orchestrator Runner - Multi-Agent Demonstration
# Layer: 0 (Universal)
# Purpose: Demonstrates the 5-mode orchestrator flow with parallel spawning
# =============================================================================

set -uo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTEXT_AGENTS_DIR="$(dirname "$SCRIPT_DIR")"
LAYER_UNIVERSAL_DIR="$(cd "$CONTEXT_AGENTS_DIR/../../.." && pwd)"
HAND_OFF_DIR="$LAYER_UNIVERSAL_DIR/layer_0/layer_0_02_manager_handoff_documents"
SPAWN_SCRIPT="$LAYER_UNIVERSAL_DIR/layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_multi_agent_orchestration/layer_1_sub_feature_agent_spawning/prototype/spawn_agent.sh"

# Configuration
TASK_FILE="${1:-$HAND_OFF_DIR/incoming/from_above/orchestrated_task_analyze_sublayers.json}"
MAX_CONCURRENT=3
AGENT_TIMEOUT=90
USE_DYNAMIC_TIMEOUT=true  # Enable dynamic timeout by default

log_mode() { echo -e "\n${CYAN}═══════════════════════════════════════════════════════════════${NC}"; echo -e "${CYAN}  MODE: $1${NC}"; echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}\n"; }
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# State tracking (simulating state actors)
declare -A CHILDREN
declare -a CHILD_IDS
TASK_ID=""
CURRENT_DEPTH=0

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║     LAYER 0 ORCHESTRATOR - Multi-Agent Demonstration          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
log_info "Working Directory: $LAYER_UNIVERSAL_DIR"
log_info "Task File: $TASK_FILE"
echo ""

# =============================================================================
# MODE 1: RECEIVE MODE
# =============================================================================
log_mode "RECEIVE MODE - Parsing incoming task"

if [[ ! -f "$TASK_FILE" ]]; then
    log_error "Task file not found: $TASK_FILE"
    exit 1
fi

# Parse task
TASK_ID=$(jq -r '.taskId' "$TASK_FILE")
DESCRIPTION=$(jq -r '.description' "$TASK_FILE")
STRATEGY=$(jq -r '.orchestration.strategy // "sequential"' "$TASK_FILE")
SUBTASK_COUNT=$(jq -r '.orchestration.subtasks | length' "$TASK_FILE")

log_info "Task ID: $TASK_ID"
log_info "Description: $DESCRIPTION"
log_info "Strategy: $STRATEGY"
log_info "Subtasks: $SUBTASK_COUNT"

if [[ "$SUBTASK_COUNT" -eq 0 ]]; then
    log_warn "No subtasks defined - this is a leaf task, executing directly"
    exit 0
fi

log_success "Task received and parsed"

# =============================================================================
# MODE 2: DELEGATION MODE
# =============================================================================
log_mode "DELEGATION MODE - Spawning child agents"

# Check resource budget
log_info "Checking resource budget..."
log_info "  Current depth: $CURRENT_DEPTH"
log_info "  Max concurrent: $MAX_CONCURRENT"
log_info "  Subtasks to spawn: $SUBTASK_COUNT"

if [[ $SUBTASK_COUNT -gt $MAX_CONCURRENT ]]; then
    log_warn "Subtask count ($SUBTASK_COUNT) exceeds max concurrent ($MAX_CONCURRENT)"
    log_warn "Will spawn in batches"
fi

# Create subtask files and spawn agents
for i in $(seq 0 $((SUBTASK_COUNT - 1))); do
    SUBTASK_ID=$(jq -r ".orchestration.subtasks[$i].taskId" "$TASK_FILE")
    SUBTASK_DESC=$(jq -r ".orchestration.subtasks[$i].description" "$TASK_FILE")
    TARGET_PATH=$(jq -r ".orchestration.subtasks[$i].targetPath" "$TASK_FILE")

    log_info "Spawning child for subtask: $SUBTASK_ID"
    log_info "  Description: $SUBTASK_DESC"
    log_info "  Target: $TARGET_PATH"

    # Create subtask JSON
    SUBTASK_FILE="$HAND_OFF_DIR/outgoing/to_below/subtask_${SUBTASK_ID}.json"
    cat > "$SUBTASK_FILE" << EOF
{
    "taskId": "$SUBTASK_ID",
    "parentTaskId": "$TASK_ID",
    "description": "$SUBTASK_DESC",
    "context": {
        "layer": 0,
        "targetPath": "$TARGET_PATH",
        "workingDir": "$LAYER_UNIVERSAL_DIR"
    },
    "priority": "normal"
}
EOF

    # Spawn agent (capture child ID)
    # Build spawn options based on configuration
    SPAWN_OPTS="-w $LAYER_UNIVERSAL_DIR"
    if [[ "$USE_DYNAMIC_TIMEOUT" == "true" ]]; then
        SPAWN_OPTS="$SPAWN_OPTS -D"
        log_info "  Using dynamic timeout (complexity-based)"
    else
        log_info "  Using static timeout: ${AGENT_TIMEOUT}s"
    fi

    CHILD_ID=$(CURRENT_DEPTH=$((CURRENT_DEPTH + 1)) AGENT_TIMEOUT=$AGENT_TIMEOUT \
        "$SPAWN_SCRIPT" $SPAWN_OPTS claude "$SUBTASK_FILE" 2>&1 | tail -1)

    if [[ -n "$CHILD_ID" && "$CHILD_ID" == child_* ]]; then
        log_success "Spawned child: $CHILD_ID"
        CHILDREN[$SUBTASK_ID]="$CHILD_ID"
        CHILD_IDS+=("$CHILD_ID")
    else
        log_error "Failed to spawn child for $SUBTASK_ID"
    fi

    # Small delay between spawns
    sleep 1
done

log_success "All children spawned: ${#CHILD_IDS[@]} agents"

# =============================================================================
# MODE 3: MONITORING MODE
# =============================================================================
log_mode "MONITORING MODE - Tracking child progress"

declare -A CHILDREN_DONE
COMPLETED=0
FAILED=0
TIMEOUT_COUNT=0
MAX_WAIT=180  # 3 minutes max wait
WAIT_INTERVAL=5
ELAPSED=0

while [[ $((COMPLETED + FAILED + TIMEOUT_COUNT)) -lt ${#CHILD_IDS[@]} && $ELAPSED -lt $MAX_WAIT ]]; do
    log_info "Checking status... (elapsed: ${ELAPSED}s)"

    for CHILD_ID in "${CHILD_IDS[@]}"; do
        STATUS_FILE="$HAND_OFF_DIR/status/$CHILD_ID.json"
        if [[ -f "$STATUS_FILE" ]]; then
            STATUS=$(jq -r '.status' "$STATUS_FILE")
            PROGRESS=$(jq -r '.progress' "$STATUS_FILE")

            case "$STATUS" in
                completed)
                    if [[ ! "${CHILDREN_DONE[$CHILD_ID]:-}" == "yes" ]]; then
                        log_success "  $CHILD_ID: COMPLETED (progress: $PROGRESS%)"
                        CHILDREN_DONE[$CHILD_ID]="yes"
                        ((COMPLETED++))
                    fi
                    ;;
                failed)
                    if [[ ! "${CHILDREN_DONE[$CHILD_ID]:-}" == "yes" ]]; then
                        log_error "  $CHILD_ID: FAILED"
                        CHILDREN_DONE[$CHILD_ID]="yes"
                        ((FAILED++))
                    fi
                    ;;
                timeout)
                    if [[ ! "${CHILDREN_DONE[$CHILD_ID]:-}" == "yes" ]]; then
                        log_warn "  $CHILD_ID: TIMEOUT"
                        CHILDREN_DONE[$CHILD_ID]="yes"
                        ((TIMEOUT_COUNT++))
                    fi
                    ;;
                running|pending)
                    log_info "  $CHILD_ID: $STATUS (progress: $PROGRESS%)"
                    ;;
            esac
        fi
    done

    if [[ $((COMPLETED + FAILED + TIMEOUT_COUNT)) -lt ${#CHILD_IDS[@]} ]]; then
        sleep $WAIT_INTERVAL
        ((ELAPSED += WAIT_INTERVAL))
    fi
done

log_info "Monitoring complete:"
log_info "  Completed: $COMPLETED"
log_info "  Failed: $FAILED"
log_info "  Timeout: $TIMEOUT_COUNT"

# =============================================================================
# MODE 4: AGGREGATION MODE
# =============================================================================
log_mode "AGGREGATION MODE - Collecting and synthesizing results"

RESULTS=()
for CHILD_ID in "${CHILD_IDS[@]}"; do
    RESULT_FILE="$HAND_OFF_DIR/incoming/from_below/$CHILD_ID/result.json"
    if [[ -f "$RESULT_FILE" ]]; then
        log_info "Collecting result from $CHILD_ID"
        SUBTASK_ID=$(jq -r '.taskId' "$RESULT_FILE")
        SUMMARY=$(jq -r '.result.summary // "No summary"' "$RESULT_FILE")
        CONFIDENCE=$(jq -r '.result.confidence // 0' "$RESULT_FILE")
        log_info "  Subtask: $SUBTASK_ID"
        log_info "  Summary: $SUMMARY"
        log_info "  Confidence: $CONFIDENCE"
        RESULTS+=("$RESULT_FILE")
    else
        log_warn "No result file for $CHILD_ID"
    fi
done

# Calculate aggregate confidence
TOTAL_CONFIDENCE=0
for RESULT_FILE in "${RESULTS[@]}"; do
    CONF=$(jq -r '.result.confidence // 0' "$RESULT_FILE")
    TOTAL_CONFIDENCE=$(echo "$TOTAL_CONFIDENCE + $CONF" | bc)
done
if [[ ${#RESULTS[@]} -gt 0 ]]; then
    AVG_CONFIDENCE=$(echo "scale=2; $TOTAL_CONFIDENCE / ${#RESULTS[@]}" | bc)
else
    AVG_CONFIDENCE=0
fi

log_success "Aggregation complete"
log_info "  Results collected: ${#RESULTS[@]}"
log_info "  Average confidence: $AVG_CONFIDENCE"

# =============================================================================
# MODE 5: REPORT MODE
# =============================================================================
log_mode "REPORT MODE - Generating final report"

# Create aggregated result
REPORT_FILE="$HAND_OFF_DIR/outgoing/to_above/result_${TASK_ID}.json"

cat > "$REPORT_FILE" << EOF
{
    "taskId": "$TASK_ID",
    "status": "completed",
    "orchestration": {
        "strategy": "$STRATEGY",
        "childrenSpawned": ${#CHILD_IDS[@]},
        "childrenCompleted": $COMPLETED,
        "childrenFailed": $FAILED,
        "childrenTimeout": $TIMEOUT_COUNT
    },
    "result": {
        "summary": "Orchestrated analysis of ${#RESULTS[@]} sub_layers completed",
        "childResults": [
EOF

# Add child results
FIRST=true
for RESULT_FILE in "${RESULTS[@]}"; do
    if $FIRST; then
        FIRST=false
    else
        echo "," >> "$REPORT_FILE"
    fi
    jq -c '{taskId, summary: .result.summary, confidence: .result.confidence}' "$RESULT_FILE" >> "$REPORT_FILE"
done

cat >> "$REPORT_FILE" << EOF
        ],
        "confidence": $AVG_CONFIDENCE
    },
    "metadata": {
        "orchestratorType": "layer_0",
        "depth": $CURRENT_DEPTH,
        "executionTime": "${ELAPSED}s",
        "timestamp": "$(date -Iseconds)"
    }
}
EOF

log_success "Report written to: $REPORT_FILE"

# Display final report
echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                    FINAL ORCHESTRATION REPORT                  ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
jq '.' "$REPORT_FILE"

log_success "Orchestration complete!"
