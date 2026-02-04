#!/bin/bash
#
# track-change.sh - Log file changes to divergence.log
#
# Usage:
#   ./track-change.sh <path> <action> <agent_id> [before_hash] [after_hash]
#
# Actions: CREATED, MODIFIED, DELETED
#
# Example:
#   ./track-change.sh outputs/file.md CREATED agent_01
#   ./track-change.sh outputs/file.md MODIFIED agent_01 abc123 def456
#

set -e

# Configuration
DIVERGENCE_LOG="${DIVERGENCE_LOG:-outputs/episodic/changes/divergence.log}"

# Parameters
FILE_PATH="$1"
ACTION="$2"
AGENT_ID="$3"
BEFORE_HASH="${4:--}"
AFTER_HASH="${5:-$(git hash-object "$FILE_PATH" 2>/dev/null || echo "unknown")}"

if [ -z "$FILE_PATH" ] || [ -z "$ACTION" ] || [ -z "$AGENT_ID" ]; then
    echo "Usage: $0 <path> <action> <agent_id> [before_hash] [after_hash]"
    echo "Actions: CREATED, MODIFIED, DELETED"
    exit 1
fi

# Get timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Append to divergence log
echo "$TIMESTAMP | $AGENT_ID | $FILE_PATH | $ACTION | $BEFORE_HASH → $AFTER_HASH" >> "$DIVERGENCE_LOG"

echo "Logged: $ACTION $FILE_PATH by $AGENT_ID"

