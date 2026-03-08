#!/bin/bash
# resource_id: "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d"
# resource_type: "script"
# resource_name: "entity-search-redirect"
#
# entity-search-redirect.sh — PostToolUse hook for Glob|Grep
#
# Fires after Glob or Grep operations. If the search pattern looks
# like entity discovery, returns additionalContext suggesting
# Grep on .entity-lookup.tsv for structured results with UUIDs.
#
# Input: JSON on stdin with tool_name, tool_input, etc.
# Output: JSON with additionalContext if entity-search pattern detected
#

INPUT=$(cat)

TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name // empty')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input // empty')

# Extract the search pattern based on tool type
if [ "$TOOL_NAME" = "Glob" ]; then
    PATTERN=$(echo "$TOOL_INPUT" | jq -r '.pattern // empty')
elif [ "$TOOL_NAME" = "Grep" ]; then
    PATTERN=$(echo "$TOOL_INPUT" | jq -r '.pattern // empty')
else
    echo '{}'
    exit 0
fi

# Empty pattern — skip
if [ -z "$PATTERN" ]; then
    echo '{}'
    exit 0
fi

# Heuristic: does this pattern look like entity discovery?
ENTITY_SEARCH=false

# Glob patterns that indicate entity discovery
if [ "$TOOL_NAME" = "Glob" ]; then
    case "$PATTERN" in
        *0AGNOSTIC.md)       ENTITY_SEARCH=true ;;
        *.entity_id*)        ENTITY_SEARCH=true ;;
        *entity_registry*)   ENTITY_SEARCH=true ;;
        *layer_*_registry*)  ENTITY_SEARCH=true ;;
        *layer_*_group/layer_*) ENTITY_SEARCH=true ;;
    esac
fi

# Grep patterns that indicate entity discovery
if [ "$TOOL_NAME" = "Grep" ]; then
    case "$PATTERN" in
        *entity_type*)    ENTITY_SEARCH=true ;;
        *resource_type*)  ENTITY_SEARCH=true ;;
        *resource_name*)  ENTITY_SEARCH=true ;;
        *entity_id*)      ENTITY_SEARCH=true ;;
    esac
fi

if [ "$ENTITY_SEARCH" = true ]; then
    cat <<'EOF'
{
  "additionalContext": "TIP: For entity discovery, Grep .entity-lookup.tsv at the repo root for structured results including UUIDs, paths, and parent UUIDs. Example: Grep pattern=\"your-search\" path=\".entity-lookup.tsv\". Each line has tab-separated fields: name, UUID, path, parent_UUID."
}
EOF
else
    echo '{}'
fi
