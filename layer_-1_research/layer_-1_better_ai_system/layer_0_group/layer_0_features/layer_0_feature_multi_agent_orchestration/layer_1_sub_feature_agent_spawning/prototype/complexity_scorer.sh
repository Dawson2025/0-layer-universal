#!/bin/bash
# =============================================================================
# Complexity Scorer - Dynamic Timeout Calculator
# Layer: -1 (Research)
# Feature: Multi-Agent Orchestration > Agent Spawning
# Purpose: Analyze task complexity and calculate appropriate timeout
# =============================================================================

set -uo pipefail

# Default configuration
BASE_TIMEOUT=${BASE_TIMEOUT:-30}           # Minimum timeout (seconds)
MAX_TIMEOUT=${MAX_TIMEOUT:-600}            # Maximum timeout (10 minutes)
SECONDS_PER_FILE=${SECONDS_PER_FILE:-2}    # Time allowance per file
SECONDS_PER_KB=${SECONDS_PER_KB:-1}        # Time allowance per KB of content
SECONDS_PER_DIR=${SECONDS_PER_DIR:-5}      # Time allowance per directory
COMPLEXITY_MULTIPLIER=${COMPLEXITY_MULTIPLIER:-1.5}  # Safety margin

# Task type multipliers
declare -A TASK_TYPE_MULTIPLIERS=(
    ["analyze"]=1.0
    ["summarize"]=0.8
    ["count"]=0.5
    ["search"]=0.7
    ["generate"]=2.0
    ["refactor"]=2.5
    ["test"]=1.5
    ["review"]=1.2
    ["default"]=1.0
)

usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS] <task_file_or_path>

Analyzes task complexity and outputs recommended timeout in seconds.

Arguments:
    task_file_or_path   JSON task file or directory path to analyze

Options:
    -t, --task-type TYPE    Task type hint (analyze, summarize, count, search,
                            generate, refactor, test, review)
    -b, --base SECONDS      Base timeout (default: $BASE_TIMEOUT)
    -m, --max SECONDS       Maximum timeout (default: $MAX_TIMEOUT)
    -v, --verbose           Show detailed breakdown
    -j, --json              Output as JSON
    -h, --help              Show this help

Environment Variables:
    BASE_TIMEOUT            Minimum timeout
    MAX_TIMEOUT             Maximum timeout
    SECONDS_PER_FILE        Time per file (default: 2)
    SECONDS_PER_KB          Time per KB (default: 1)
    SECONDS_PER_DIR         Time per directory (default: 5)
    COMPLEXITY_MULTIPLIER   Safety margin multiplier (default: 1.5)

Example:
    $(basename "$0") ./task.json
    $(basename "$0") -v -t analyze /path/to/directory
    $(basename "$0") --json ./task.json
EOF
    exit 0
}

# Parse arguments
TASK_TYPE="default"
VERBOSE=false
JSON_OUTPUT=false
TARGET=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -t|--task-type)
            TASK_TYPE="$2"
            shift 2
            ;;
        -b|--base)
            BASE_TIMEOUT="$2"
            shift 2
            ;;
        -m|--max)
            MAX_TIMEOUT="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -j|--json)
            JSON_OUTPUT=true
            shift
            ;;
        -h|--help)
            usage
            ;;
        -*)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
        *)
            TARGET="$1"
            shift
            ;;
    esac
done

if [[ -z "$TARGET" ]]; then
    echo "Error: No target specified" >&2
    usage
fi

# Extract target path from task file if JSON
TARGET_PATH="$TARGET"
if [[ -f "$TARGET" && "$TARGET" == *.json ]]; then
    # Try to extract targetPath or paths from task JSON
    EXTRACTED_PATH=$(jq -r '.context.targetPath // .context.paths[0] // .targetPath // empty' "$TARGET" 2>/dev/null)
    if [[ -n "$EXTRACTED_PATH" ]]; then
        # Make path absolute if relative
        if [[ "$EXTRACTED_PATH" != /* ]]; then
            WORK_DIR=$(jq -r '.context.workingDir // empty' "$TARGET" 2>/dev/null)
            if [[ -n "$WORK_DIR" ]]; then
                TARGET_PATH="$WORK_DIR/$EXTRACTED_PATH"
            fi
        else
            TARGET_PATH="$EXTRACTED_PATH"
        fi
    fi

    # Try to infer task type from description
    DESCRIPTION=$(jq -r '.description // empty' "$TARGET" 2>/dev/null | tr '[:upper:]' '[:lower:]')
    if [[ -n "$DESCRIPTION" && "$TASK_TYPE" == "default" ]]; then
        for type in "${!TASK_TYPE_MULTIPLIERS[@]}"; do
            if [[ "$DESCRIPTION" == *"$type"* ]]; then
                TASK_TYPE="$type"
                break
            fi
        done
    fi
fi

# Validate target path exists
if [[ ! -e "$TARGET_PATH" ]]; then
    # Try without working dir
    if [[ -d "$TARGET" ]]; then
        TARGET_PATH="$TARGET"
    else
        echo "Warning: Target path not found: $TARGET_PATH" >&2
        # Return base timeout as fallback
        echo "$BASE_TIMEOUT"
        exit 0
    fi
fi

# Calculate complexity metrics
FILE_COUNT=0
TOTAL_SIZE_KB=0
DIR_COUNT=0
MAX_DEPTH=0

if [[ -d "$TARGET_PATH" ]]; then
    # Count files
    FILE_COUNT=$(find "$TARGET_PATH" -type f 2>/dev/null | wc -l)

    # Count directories
    DIR_COUNT=$(find "$TARGET_PATH" -type d 2>/dev/null | wc -l)

    # Calculate total size in KB
    TOTAL_SIZE_KB=$(du -sk "$TARGET_PATH" 2>/dev/null | cut -f1)

    # Calculate max depth
    MAX_DEPTH=$(find "$TARGET_PATH" -type d -printf '%d\n' 2>/dev/null | sort -rn | head -1)

elif [[ -f "$TARGET_PATH" ]]; then
    FILE_COUNT=1
    TOTAL_SIZE_KB=$(du -sk "$TARGET_PATH" 2>/dev/null | cut -f1)
    DIR_COUNT=0
    MAX_DEPTH=0
fi

# Get task type multiplier
TYPE_MULTIPLIER=${TASK_TYPE_MULTIPLIERS[$TASK_TYPE]:-1.0}

# Calculate base time components
FILE_TIME=$(echo "$FILE_COUNT * $SECONDS_PER_FILE" | bc)
SIZE_TIME=$(echo "$TOTAL_SIZE_KB * $SECONDS_PER_KB" | bc)
DIR_TIME=$(echo "$DIR_COUNT * $SECONDS_PER_DIR" | bc)

# Depth penalty (deeper = more complex navigation)
DEPTH_PENALTY=$(echo "1 + ($MAX_DEPTH * 0.1)" | bc)

# Calculate raw timeout
RAW_TIMEOUT=$(echo "($BASE_TIMEOUT + $FILE_TIME + $SIZE_TIME + $DIR_TIME) * $TYPE_MULTIPLIER * $DEPTH_PENALTY * $COMPLEXITY_MULTIPLIER" | bc)

# Clamp to min/max
FINAL_TIMEOUT=$(echo "if ($RAW_TIMEOUT < $BASE_TIMEOUT) $BASE_TIMEOUT else if ($RAW_TIMEOUT > $MAX_TIMEOUT) $MAX_TIMEOUT else $RAW_TIMEOUT" | bc)

# Round to integer
FINAL_TIMEOUT=$(printf "%.0f" "$FINAL_TIMEOUT")

# Output
if $JSON_OUTPUT; then
    cat << EOF
{
    "recommendedTimeout": $FINAL_TIMEOUT,
    "metrics": {
        "fileCount": $FILE_COUNT,
        "totalSizeKB": $TOTAL_SIZE_KB,
        "directoryCount": $DIR_COUNT,
        "maxDepth": $MAX_DEPTH
    },
    "calculation": {
        "baseTimeout": $BASE_TIMEOUT,
        "fileTime": $FILE_TIME,
        "sizeTime": $SIZE_TIME,
        "dirTime": $DIR_TIME,
        "taskType": "$TASK_TYPE",
        "typeMultiplier": $TYPE_MULTIPLIER,
        "depthPenalty": $DEPTH_PENALTY,
        "complexityMultiplier": $COMPLEXITY_MULTIPLIER,
        "rawTimeout": $RAW_TIMEOUT,
        "maxTimeout": $MAX_TIMEOUT
    },
    "targetPath": "$TARGET_PATH"
}
EOF
elif $VERBOSE; then
    echo "=== Complexity Analysis ==="
    echo "Target: $TARGET_PATH"
    echo ""
    echo "Metrics:"
    echo "  Files: $FILE_COUNT"
    echo "  Size: ${TOTAL_SIZE_KB}KB"
    echo "  Directories: $DIR_COUNT"
    echo "  Max Depth: $MAX_DEPTH"
    echo ""
    echo "Calculation:"
    echo "  Base timeout: ${BASE_TIMEOUT}s"
    echo "  File time: ${FILE_TIME}s ($FILE_COUNT files × ${SECONDS_PER_FILE}s)"
    echo "  Size time: ${SIZE_TIME}s (${TOTAL_SIZE_KB}KB × ${SECONDS_PER_KB}s)"
    echo "  Dir time: ${DIR_TIME}s ($DIR_COUNT dirs × ${SECONDS_PER_DIR}s)"
    echo "  Task type: $TASK_TYPE (×$TYPE_MULTIPLIER)"
    echo "  Depth penalty: ×$DEPTH_PENALTY"
    echo "  Safety margin: ×$COMPLEXITY_MULTIPLIER"
    echo "  Raw total: ${RAW_TIMEOUT}s"
    echo ""
    echo "=== Recommended Timeout: ${FINAL_TIMEOUT}s ==="
else
    echo "$FINAL_TIMEOUT"
fi
