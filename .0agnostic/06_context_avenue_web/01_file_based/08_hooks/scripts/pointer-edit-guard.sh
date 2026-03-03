#!/bin/bash
#
# pointer-edit-guard.sh — PostToolUse hook for pointer file edits
#
# Fires after Edit or Write operations. If the file contains
# pointer_to: frontmatter, returns additionalContext reminding
# the agent to validate the pointer.
#
# Input: JSON on stdin with tool_name, file_path, etc.
# Output: JSON with additionalContext if pointer file detected
#

INPUT=$(cat)

# Extract file_path from the tool input
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only check .md files
if ! echo "$FILE_PATH" | grep -q '\.md$'; then
    echo '{}'
    exit 0
fi

# Check if file exists and has pointer frontmatter
if [ -f "$FILE_PATH" ] && head -20 "$FILE_PATH" 2>/dev/null | grep -q "^pointer_to:"; then
    cat <<'EOF'
{
  "additionalContext": "You just modified a pointer file (contains pointer_to: frontmatter). Run `pointer-sync.sh --validate` to verify the pointer resolves correctly. Script location: .0agnostic/pointer-sync.sh. Protocol: .0agnostic/03_protocols/pointer_sync_protocol.md"
}
EOF
else
    echo '{}'
fi
