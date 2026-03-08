#!/bin/bash
# resource_id: "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d"
# resource_type: "script"
# resource_name: "entity-search-redirect"
#
# entity-search-redirect.sh — PostToolUse hook for Glob|Grep
#
# Fires after Glob or Grep operations. If the search pattern looks
# like entity discovery, returns additionalContext redirecting the
# agent to use entity-find.sh instead.
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
  "additionalContext": "ENTITY SEARCH DETECTED: You used Glob/Grep for what appears to be entity discovery. entity-find.sh provides better results — it searches nested registries, parent chains, and UUID relationships that Glob/Grep miss.\n\nUse this instead:\n```\nROOT=$(git rev-parse --show-toplevel)\nENTITY_FIND=\"$ROOT/$(jq -r '.uuids[\"f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7\"].path // empty' \"$ROOT/.uuid-index.json\")\"\n$ENTITY_FIND <your-search-term>\n```\n\nThis is Critical Rule #5 — entity-find.sh is MANDATORY for entity discovery."
}
EOF
else
    echo '{}'
fi
