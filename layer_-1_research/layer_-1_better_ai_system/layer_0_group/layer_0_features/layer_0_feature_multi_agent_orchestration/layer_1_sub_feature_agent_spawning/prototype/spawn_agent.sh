#!/bin/bash
# =============================================================================
# Agent Spawning Prototype
# Layer: -1 (Research)
# Feature: Multi-Agent Orchestration > Agent Spawning
# Purpose: Demonstrates basic CLI AI agent spawning with file-based communication
# =============================================================================

set -euo pipefail

# Configuration
MAX_DEPTH=${MAX_DEPTH:-5}
MAX_CONCURRENT=${MAX_CONCURRENT:-3}
AGENT_TIMEOUT=${AGENT_TIMEOUT:-300}  # 5 minutes default
CURRENT_DEPTH=${CURRENT_DEPTH:-0}
DYNAMIC_TIMEOUT=${DYNAMIC_TIMEOUT:-false}  # Use complexity scorer for timeout
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
COMPLEXITY_SCORER="$SCRIPT_DIR/complexity_scorer.sh"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging
log() {
    echo -e "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log_info() { log "${BLUE}[INFO]${NC} $1"; }
log_success() { log "${GREEN}[SUCCESS]${NC} $1"; }
log_warn() { log "${YELLOW}[WARN]${NC} $1"; }
log_error() { log "${RED}[ERROR]${NC} $1"; }

# Usage
usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS] <agent_type> <task_file>

Spawns a CLI AI agent with a task from a JSON file.

Arguments:
    agent_type    Type of agent: claude, codex, gemini, aider
    task_file     Path to task.json file

Options:
    -d, --depth N       Current recursion depth (default: 0)
    -m, --max-depth N   Maximum recursion depth (default: 5)
    -c, --concurrent N  Max concurrent agents (default: 3)
    -t, --timeout N     Agent timeout in seconds (default: 300)
    -D, --dynamic       Use dynamic timeout based on task complexity
    -w, --work-dir DIR  Working directory (0_layer_universal root)
    -h, --help          Show this help message

Environment Variables:
    CURRENT_DEPTH       Current recursion depth
    MAX_DEPTH           Maximum recursion depth
    MAX_CONCURRENT      Maximum concurrent agents
    AGENT_TIMEOUT       Timeout per agent in seconds
    DYNAMIC_TIMEOUT     Set to 'true' to enable dynamic timeout calculation

Example:
    $(basename "$0") claude ./tasks/task_001.json
    $(basename "$0") -d 1 -m 3 codex ./subtask.json
EOF
    exit 0
}

# Parse arguments
WORK_DIR=""
while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--depth)
            CURRENT_DEPTH="$2"
            shift 2
            ;;
        -m|--max-depth)
            MAX_DEPTH="$2"
            shift 2
            ;;
        -c|--concurrent)
            MAX_CONCURRENT="$2"
            shift 2
            ;;
        -t|--timeout)
            AGENT_TIMEOUT="$2"
            shift 2
            ;;
        -D|--dynamic)
            DYNAMIC_TIMEOUT=true
            shift
            ;;
        -w|--work-dir)
            WORK_DIR="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        -*)
            log_error "Unknown option: $1"
            usage
            ;;
        *)
            break
            ;;
    esac
done

if [[ $# -lt 2 ]]; then
    log_error "Missing required arguments"
    usage
fi

AGENT_TYPE="$1"
TASK_FILE="$2"

# Validate agent type
case "$AGENT_TYPE" in
    claude|codex|gemini|aider)
        ;;
    *)
        log_error "Invalid agent type: $AGENT_TYPE"
        log_error "Valid types: claude, codex, gemini, aider"
        exit 1
        ;;
esac

# Validate task file
if [[ ! -f "$TASK_FILE" ]]; then
    log_error "Task file not found: $TASK_FILE"
    exit 1
fi

# Check depth limit (SAFEGUARD: prevent infinite recursion)
if [[ $CURRENT_DEPTH -ge $MAX_DEPTH ]]; then
    log_error "SAFEGUARD TRIGGERED: Maximum recursion depth reached ($CURRENT_DEPTH >= $MAX_DEPTH)"
    log_error "Cannot spawn agent. Task must be executed by current agent or escalated."
    exit 2
fi

# Set up working directory
if [[ -z "$WORK_DIR" ]]; then
    WORK_DIR="$(dirname "$TASK_FILE")/.."
fi
WORK_DIR="$(cd "$WORK_DIR" && pwd)"

# Generate child ID
CHILD_ID="child_$(date +%s)_$$"

# Create directory structure
OUTGOING_DIR="$WORK_DIR/layer_0/layer_0_02_manager_handoff_documents/outgoing/to_below/$CHILD_ID"
INCOMING_DIR="$WORK_DIR/layer_0/layer_0_02_manager_handoff_documents/incoming/from_below/$CHILD_ID"
STATUS_DIR="$WORK_DIR/layer_0/layer_0_02_manager_handoff_documents/status"

mkdir -p "$OUTGOING_DIR" "$INCOMING_DIR" "$STATUS_DIR"

log_info "Spawning $AGENT_TYPE agent (depth: $CURRENT_DEPTH, max: $MAX_DEPTH)"
log_info "Child ID: $CHILD_ID"
log_info "Working directory: $WORK_DIR"

# Copy task file to outgoing directory
cp "$TASK_FILE" "$OUTGOING_DIR/task.json"

# Extract task description from JSON
TASK_DESC=$(jq -r '.description // .task // "Execute task from file"' "$TASK_FILE")

# Dynamic timeout calculation
if [[ "$DYNAMIC_TIMEOUT" == "true" || "$DYNAMIC_TIMEOUT" == "1" ]]; then
    if [[ -x "$COMPLEXITY_SCORER" ]]; then
        log_info "Calculating dynamic timeout based on task complexity..."

        # Use tuned parameters for realistic estimates
        CALCULATED_TIMEOUT=$(SECONDS_PER_FILE=0.5 SECONDS_PER_KB=0.1 SECONDS_PER_DIR=3 \
            BASE_TIMEOUT=30 MAX_TIMEOUT=600 \
            "$COMPLEXITY_SCORER" "$TASK_FILE" 2>/dev/null) || CALCULATED_TIMEOUT=""

        if [[ -n "$CALCULATED_TIMEOUT" && "$CALCULATED_TIMEOUT" =~ ^[0-9]+$ ]]; then
            log_info "Complexity scorer recommends: ${CALCULATED_TIMEOUT}s timeout"

            # Use the higher of: calculated timeout or explicit AGENT_TIMEOUT
            if [[ $CALCULATED_TIMEOUT -gt $AGENT_TIMEOUT ]]; then
                AGENT_TIMEOUT=$CALCULATED_TIMEOUT
                log_info "Using dynamic timeout: ${AGENT_TIMEOUT}s"
            else
                log_info "Keeping explicit timeout: ${AGENT_TIMEOUT}s (higher than calculated)"
            fi
        else
            log_warn "Could not calculate dynamic timeout, using default: ${AGENT_TIMEOUT}s"
        fi
    else
        log_warn "Complexity scorer not found at: $COMPLEXITY_SCORER"
        log_warn "Using static timeout: ${AGENT_TIMEOUT}s"
    fi
fi

# Initialize status file
cat > "$STATUS_DIR/$CHILD_ID.json" << EOF
{
    "childId": "$CHILD_ID",
    "agentType": "$AGENT_TYPE",
    "status": "pending",
    "depth": $CURRENT_DEPTH,
    "startedAt": null,
    "lastUpdate": "$(date -Iseconds)",
    "progress": 0,
    "pid": null
}
EOF

log_info "Task: $TASK_DESC"

# Build spawn command based on agent type
RESULT_FILE="$INCOMING_DIR/result.json"

build_spawn_command() {
    local agent="$1"
    local task_path="$2"
    local result_path="$3"
    local prompt_path="$4"
    local depth="$((CURRENT_DEPTH + 1))"

    # Write the prompt to a file (avoids shell quoting issues)
    cat > "$prompt_path" << PROMPT_EOF
You are a subagent at depth $depth (max: $MAX_DEPTH).

TASK FILE: $task_path
RESULT FILE: $result_path

Read the task from the task file, execute it, and write your result as JSON to the result file.

IMPORTANT SAFEGUARDS:
- You are at depth $depth. Max depth is $MAX_DEPTH.
- If you need to spawn subagents, you can only do so if $depth < $MAX_DEPTH
- Do NOT spawn subagents with identical tasks (infinite recursion protection)
- Write your result to: $result_path

Result format:
{
  "taskId": "from task file",
  "status": "completed|failed",
  "result": {
    "summary": "brief summary",
    "content": "full result",
    "confidence": 0.0-1.0
  },
  "metadata": {
    "agentType": "$agent",
    "depth": $depth
  }
}
PROMPT_EOF

    case "$agent" in
        claude)
            # Claude Code with --print flag for non-interactive mode
            echo "claude --print \"\$(cat '$prompt_path')\""
            ;;
        codex)
            # Codex CLI
            echo "codex \"\$(cat '$prompt_path')\""
            ;;
        gemini)
            # Gemini CLI
            echo "gemini \"\$(cat '$prompt_path')\""
            ;;
        aider)
            # Aider with --yes for non-interactive
            echo "aider --yes --message \"\$(cat '$prompt_path')\""
            ;;
    esac
}

# Write prompt file
PROMPT_FILE="$OUTGOING_DIR/prompt.txt"
SPAWN_CMD=$(build_spawn_command "$AGENT_TYPE" "$OUTGOING_DIR/task.json" "$RESULT_FILE" "$PROMPT_FILE")

log_info "Spawn command: $SPAWN_CMD"

# Update status to running
update_status() {
    local status="$1"
    local progress="${2:-0}"
    local pid="${3:-null}"

    jq --arg status "$status" \
       --arg update "$(date -Iseconds)" \
       --argjson progress "$progress" \
       --argjson pid "$pid" \
       '.status = $status | .lastUpdate = $update | .progress = $progress | .pid = $pid' \
       "$STATUS_DIR/$CHILD_ID.json" > "$STATUS_DIR/$CHILD_ID.json.tmp"
    mv "$STATUS_DIR/$CHILD_ID.json.tmp" "$STATUS_DIR/$CHILD_ID.json"
}

# Spawn the agent in background with timeout
spawn_with_timeout() {
    local cmd="$1"
    local timeout="$2"

    # Update status with start time
    jq --arg start "$(date -Iseconds)" '.startedAt = $start' \
       "$STATUS_DIR/$CHILD_ID.json" > "$STATUS_DIR/$CHILD_ID.json.tmp"
    mv "$STATUS_DIR/$CHILD_ID.json.tmp" "$STATUS_DIR/$CHILD_ID.json"

    update_status "running" 10

    # Run with timeout
    if timeout "$timeout" bash -c "$cmd" > "$INCOMING_DIR/stdout.log" 2> "$INCOMING_DIR/stderr.log"; then
        update_status "completed" 100
        log_success "Agent completed successfully"
        return 0
    else
        local exit_code=$?
        if [[ $exit_code -eq 124 ]]; then
            update_status "timeout" 50
            log_error "Agent timed out after ${timeout}s"
        else
            update_status "failed" 50
            log_error "Agent failed with exit code: $exit_code"
        fi
        return $exit_code
    fi
}

# Execute spawn
log_info "Starting agent with ${AGENT_TIMEOUT}s timeout..."

if spawn_with_timeout "$SPAWN_CMD" "$AGENT_TIMEOUT"; then
    # Check if result file was created
    if [[ -f "$RESULT_FILE" ]]; then
        log_success "Result written to: $RESULT_FILE"

        # Validate JSON
        if jq empty "$RESULT_FILE" 2>/dev/null; then
            log_success "Result is valid JSON"

            # Show summary
            SUMMARY=$(jq -r '.result.summary // "No summary provided"' "$RESULT_FILE" 2>/dev/null || echo "Could not extract summary")
            log_info "Summary: $SUMMARY"
        else
            log_warn "Result is not valid JSON, may need post-processing"
        fi
    else
        log_warn "No result file created at: $RESULT_FILE"

        # Create a result from stdout if available
        if [[ -f "$INCOMING_DIR/stdout.log" && -s "$INCOMING_DIR/stdout.log" ]]; then
            log_info "Creating result from stdout..."
            cat > "$RESULT_FILE" << EOF
{
    "taskId": "$(jq -r '.taskId // "unknown"' "$OUTGOING_DIR/task.json" 2>/dev/null || echo "unknown")",
    "status": "completed",
    "result": {
        "summary": "Result extracted from agent stdout",
        "content": $(jq -Rs '.' "$INCOMING_DIR/stdout.log"),
        "confidence": 0.7
    },
    "metadata": {
        "agentType": "$AGENT_TYPE",
        "depth": $CURRENT_DEPTH,
        "note": "Result reconstructed from stdout - agent did not write to result file"
    }
}
EOF
            log_success "Result reconstructed from stdout"
        fi
    fi
fi

# Final status
log_info "Status file: $STATUS_DIR/$CHILD_ID.json"
log_info "Logs: $INCOMING_DIR/stdout.log, $INCOMING_DIR/stderr.log"

# Output child ID for parent to track
echo "$CHILD_ID"
