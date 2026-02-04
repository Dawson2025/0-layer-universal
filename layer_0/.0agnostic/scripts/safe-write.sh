#!/bin/bash
#
# safe-write.sh - Atomic write with automatic change tracking
#
# Combines:
#   1. Lock acquisition (optional)
#   2. Atomic write (temp file → rename)
#   3. Change tracking (divergence.log update)
#   4. Lock release (if acquired)
#
# Usage:
#   echo "content" | ./safe-write.sh <target_file> <agent_id> [--lock <scope>]
#   cat data.txt | ./safe-write.sh output.md my_agent --lock outputs
#
# Examples:
#   echo "new content" | ./safe-write.sh outputs/file.md agent_01
#   echo "new content" | ./safe-write.sh outputs/file.md agent_01 --lock outputs
#

set -e

# Get script directory for relative imports
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Configuration
DIVERGENCE_LOG="${DIVERGENCE_LOG:-outputs/episodic/changes/divergence.log}"

# Parse arguments
TARGET_FILE="$1"
AGENT_ID="$2"
USE_LOCK=false
LOCK_SCOPE=""

shift 2 || true

while [[ $# -gt 0 ]]; do
    case "$1" in
        --lock)
            USE_LOCK=true
            LOCK_SCOPE="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate inputs
if [ -z "$TARGET_FILE" ] || [ -z "$AGENT_ID" ]; then
    echo "Usage: $0 <target_file> <agent_id> [--lock <scope>]"
    echo ""
    echo "Options:"
    echo "  --lock <scope>  Acquire lock before writing"
    echo ""
    echo "Examples:"
    echo "  echo 'content' | $0 output.md my_agent"
    echo "  echo 'content' | $0 output.md my_agent --lock outputs"
    exit 1
fi

# Get hash of existing file (if any)
BEFORE_HASH="-"
ACTION="CREATED"
if [ -f "$TARGET_FILE" ]; then
    BEFORE_HASH=$(git hash-object "$TARGET_FILE" 2>/dev/null || md5sum "$TARGET_FILE" | cut -d' ' -f1)
    ACTION="MODIFIED"
fi

# Acquire lock if requested
if [ "$USE_LOCK" = true ]; then
    if [ -z "$LOCK_SCOPE" ]; then
        LOCK_SCOPE=$(dirname "$TARGET_FILE" | tr '/' '_')
    fi
    echo "Acquiring lock: $LOCK_SCOPE"
    bash "$SCRIPT_DIR/lock-manager.sh" acquire "$LOCK_SCOPE" "$AGENT_ID" 5
fi

# Cleanup function
cleanup() {
    local exit_code=$?
    if [ "$USE_LOCK" = true ]; then
        bash "$SCRIPT_DIR/lock-manager.sh" release "$LOCK_SCOPE" "$AGENT_ID" 2>/dev/null || true
    fi
    exit $exit_code
}
trap cleanup EXIT

# Ensure target directory exists
mkdir -p "$(dirname "$TARGET_FILE")"

# Atomic write
TEMP_FILE=$(mktemp "$(dirname "$TARGET_FILE")/.safe_write_XXXXXX")
cat > "$TEMP_FILE"
mv "$TEMP_FILE" "$TARGET_FILE"

# Get new hash
AFTER_HASH=$(git hash-object "$TARGET_FILE" 2>/dev/null || md5sum "$TARGET_FILE" | cut -d' ' -f1)

# Track change
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Ensure divergence log directory exists
mkdir -p "$(dirname "$DIVERGENCE_LOG")"

# Append to divergence log
echo "$TIMESTAMP | $AGENT_ID | $TARGET_FILE | $ACTION | $BEFORE_HASH → $AFTER_HASH" >> "$DIVERGENCE_LOG"

echo "Safe write complete: $TARGET_FILE"
echo "  Action: $ACTION"
echo "  Hash: $BEFORE_HASH → $AFTER_HASH"
echo "  Logged to: $DIVERGENCE_LOG"

