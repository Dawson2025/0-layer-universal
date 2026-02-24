#!/bin/bash
#
# agnostic-edit-guard.sh — PostToolUse hook for .0agnostic/ edits
#
# Fires after Edit or Write operations. If the file path contains
# .0agnostic/, returns additionalContext reminding the agent to
# follow the agnostic update protocol.
#
# Input: JSON on stdin with tool_name, file_path, etc.
# Output: JSON with additionalContext if .0agnostic/ path detected
#

INPUT=$(cat)

# Extract file_path from the tool input
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Check if the edited file is inside .0agnostic/
if echo "$FILE_PATH" | grep -q '\.0agnostic/'; then
    cat <<'EOF'
{
  "additionalContext": "You just modified a file inside .0agnostic/. Remember the agnostic update protocol:\n1. Update 0AGNOSTIC.md to reference this content\n2. Run agnostic-sync.sh to regenerate tool files\n3. Review sync warnings\n4. Commit both .0agnostic/ changes AND regenerated files\nFull protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md"
}
EOF
else
    echo '{}'
fi
