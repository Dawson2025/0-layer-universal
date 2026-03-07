#!/usr/bin/env bash
# resource_id: "f4a2b3c5-d6e7-4f89-a0b1-c2d3e4f5a6b7"
# resource_type: "script"
# resource_name: "entity-find"
# entity-find.sh — Fast entity lookup from pre-built .entity-lookup.tsv
# Usage: entity-find.sh [--path|--uuid] <pattern>
# No Python dependency. ~5ms lookups via grep on flat TSV.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"  # 0_layer_universal root (tools/ → protocol/ → 03_protocols/ → .0agnostic/ → ROOT)
TSV="$ROOT/.entity-lookup.tsv"

# Auto-rebuild if TSV missing
if [ ! -f "$TSV" ]; then
    echo "Building entity index..." >&2
    bash "$SCRIPT_DIR/pointer-sync.sh" --rebuild-index >/dev/null 2>&1
    if [ ! -f "$TSV" ]; then
        echo "ERROR: Failed to generate $TSV" >&2
        exit 1
    fi
fi

MODE="full"
if [ "${1:-}" = "--path" ]; then
    MODE="path"; shift
elif [ "${1:-}" = "--uuid" ]; then
    MODE="uuid"; shift
elif [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
    echo "Usage: entity-find.sh [--path|--uuid] <pattern>"
    echo "  --path   Show only entity paths"
    echo "  --uuid   Show only entity UUIDs"
    echo "  <pattern>  Case-insensitive name pattern (grep regex)"
    exit 0
fi

PATTERN="${1:-}"
if [ -z "$PATTERN" ]; then
    echo "Usage: entity-find.sh [--path|--uuid] <pattern>" >&2
    exit 1
fi

# Skip header line, grep case-insensitive on name column (field 1)
MATCHES=$(tail -n +2 "$TSV" | grep -i "$PATTERN" || true)

if [ -z "$MATCHES" ]; then
    echo "No entities matching '$PATTERN'" >&2
    exit 1
fi

while IFS=$'\t' read -r name uuid path parent_uuid; do
    case "$MODE" in
        path) echo "$path" ;;
        uuid) echo "$uuid" ;;
        full)
            echo "name: $name"
            echo "uuid: $uuid"
            echo "path: $path"
            [ -n "$parent_uuid" ] && echo "parent: $parent_uuid"
            echo "---"
            ;;
    esac
done <<< "$MATCHES"
