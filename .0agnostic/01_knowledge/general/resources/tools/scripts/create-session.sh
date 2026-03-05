#!/bin/bash
# resource_id: "e273436b-d52a-499f-8140-4dc3102b7ea7"
# resource_type: "script"
# resource_name: "create-session"
#
# create-session.sh - Create an episodic session file
#
# Usage:
#   ./create-session.sh <agent_id> <summary> [status]
#
# Example:
#   ./create-session.sh "claude_opus" "Implemented AGNOSTIC system" "COMPLETED"
#
# Creates:
#   - Session file: .0agnostic/episodic_memory/sessions/YYYY-MM-DD_session_NNN.md
#   - Updates: .0agnostic/episodic_memory/index.md
#

set -e

# Configuration
EPISODIC_DIR="${EPISODIC_DIR:-.0agnostic/episodic_memory}"
SESSIONS_DIR="$EPISODIC_DIR/sessions"
INDEX_FILE="$EPISODIC_DIR/index.md"

# Parameters
AGENT_ID="${1:-unknown_agent}"
SUMMARY="${2:-No summary provided}"
STATUS="${3:-COMPLETED}"

# Get current date
DATE=$(date +"%Y-%m-%d")
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Calculate session number for today
SESSION_NUM=1
while [ -f "$SESSIONS_DIR/${DATE}_session_$(printf '%03d' $SESSION_NUM).md" ]; do
    SESSION_NUM=$((SESSION_NUM + 1))
done
SESSION_NUM_STR=$(printf '%03d' $SESSION_NUM)

# Session file path
SESSION_FILE="$SESSIONS_DIR/${DATE}_session_${SESSION_NUM_STR}.md"

# Ensure directories exist
mkdir -p "$SESSIONS_DIR"

# Create session file
cat > "$SESSION_FILE" << EOF
# Session ${DATE}_${SESSION_NUM_STR}

**Date**: $DATE
**Timestamp**: $TIMESTAMP
**Agent**: $AGENT_ID
**Status**: $STATUS

---

## Summary

$SUMMARY

---

## Objectives

- [ ] List objectives here

---

## Files Created/Modified

- List files here

---

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| - | - |

---

## Next Steps

- List next steps here

---

*Session created by create-session.sh*

EOF

echo "Created session file: $SESSION_FILE"

# Update index.md if it exists
if [ -f "$INDEX_FILE" ]; then
    # Add entry to Recent Sessions table
    # Find the line after "| Date | Session | Summary | Status |" header row
    # and insert new entry

    # Create temp file with new entry
    NEW_ENTRY="| $DATE | [${SESSION_NUM_STR}](sessions/${DATE}_session_${SESSION_NUM_STR}.md) | $SUMMARY | $STATUS |"

    # Simple append to Recent Sessions section
    # Note: More sophisticated index updating would require a proper parser
    echo ""
    echo "To update index.md, add this entry to 'Recent Sessions' table:"
    echo "$NEW_ENTRY"
    echo ""
    echo "Index file: $INDEX_FILE"
fi

echo ""
echo "Session created successfully!"
echo "Edit the session file to add details: $SESSION_FILE"

