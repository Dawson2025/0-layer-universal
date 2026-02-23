#!/bin/bash
#
# user-level-sync.sh — Sync universal .0agnostic/ content to ~/.0agnostic/
#
# Usage: ./user-level-sync.sh [--dry-run]
#
# Syncs content from 0_layer_universal/.0agnostic/ to ~/.0agnostic/
# Only syncs: rules, protocols, knowledge, and 0AGNOSTIC.md status
# Does NOT sync: episodic memory, handoff documents, setup-dependant (those are repo-specific)
#
# Direction: Universal layer (source of truth) → User level (cascade target)
#

set -e

DRY_RUN=false
if [ "$1" = "--dry-run" ]; then
    DRY_RUN=true
    echo "DRY RUN — showing what would be synced"
    echo ""
fi

# Resolve paths
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
UNIVERSAL_AGNOSTIC="$SCRIPT_DIR"
USER_AGNOSTIC="$HOME/.0agnostic"

if [ ! -d "$USER_AGNOSTIC" ]; then
    echo "Error: ~/.0agnostic/ does not exist. Create it first."
    exit 1
fi

echo "Syncing: $UNIVERSAL_AGNOSTIC → $USER_AGNOSTIC"
echo ""

SYNCED=0
SKIPPED=0

# Helper: sync a directory's .md files
sync_dir() {
    local src="$1"
    local dst="$2"
    local label="$3"

    if [ ! -d "$src" ]; then
        return
    fi

    for file in "$src"/*.md; do
        [ -f "$file" ] || continue
        local fname=$(basename "$file")
        local dst_file="$dst/$fname"

        # Check if file differs
        if [ -f "$dst_file" ] && diff -q "$file" "$dst_file" > /dev/null 2>&1; then
            SKIPPED=$((SKIPPED + 1))
            continue
        fi

        if [ "$DRY_RUN" = true ]; then
            if [ -f "$dst_file" ]; then
                echo "  WOULD UPDATE: $label/$fname"
            else
                echo "  WOULD ADD: $label/$fname"
            fi
        else
            mkdir -p "$dst"
            cp "$file" "$dst_file"
            if [ -f "$dst_file" ]; then
                echo "  Updated: $label/$fname"
            else
                echo "  Added: $label/$fname"
            fi
        fi
        SYNCED=$((SYNCED + 1))
    done
}

# 1. Sync static rules
echo "Rules (static):"
sync_dir "$UNIVERSAL_AGNOSTIC/02_rules/static" "$USER_AGNOSTIC/02_rules/static" "02_rules/static"
[ "$SYNCED" -eq 0 ] && echo "  (all up to date)"

PREV=$SYNCED

# 2. Sync dynamic rules
echo "Rules (dynamic):"
sync_dir "$UNIVERSAL_AGNOSTIC/02_rules/dynamic" "$USER_AGNOSTIC/02_rules/dynamic" "02_rules/dynamic"
[ "$SYNCED" -eq "$PREV" ] && echo "  (all up to date)"

PREV=$SYNCED

# 3. Sync protocols
echo "Protocols:"
sync_dir "$UNIVERSAL_AGNOSTIC/03_protocols" "$USER_AGNOSTIC/03_protocols" "03_protocols"
[ "$SYNCED" -eq "$PREV" ] && echo "  (all up to date)"

PREV=$SYNCED

# 4. Sync knowledge (recursively — each topic dir)
echo "Knowledge:"
if [ -d "$UNIVERSAL_AGNOSTIC/01_knowledge" ]; then
    for topic_dir in "$UNIVERSAL_AGNOSTIC"/01_knowledge/*/; do
        [ -d "$topic_dir" ] || continue
        local_topic=$(basename "$topic_dir")
        # Recurse into subdirs (principles/, docs/, resources/)
        find "$topic_dir" -name "*.md" -type f | while read -r src_file; do
            rel_path="${src_file#$UNIVERSAL_AGNOSTIC/}"
            dst_file="$USER_AGNOSTIC/$rel_path"
            dst_dir=$(dirname "$dst_file")

            if [ -f "$dst_file" ] && diff -q "$src_file" "$dst_file" > /dev/null 2>&1; then
                SKIPPED=$((SKIPPED + 1))
                continue
            fi

            if [ "$DRY_RUN" = true ]; then
                if [ -f "$dst_file" ]; then
                    echo "  WOULD UPDATE: $rel_path"
                else
                    echo "  WOULD ADD: $rel_path"
                fi
            else
                mkdir -p "$dst_dir"
                cp "$src_file" "$dst_file"
                echo "  Synced: $rel_path"
            fi
            # Note: SYNCED counter doesn't update in pipe subshell — cosmetic only
        done
    done
fi

echo ""
echo "Sync complete!"
echo "  Files synced/updated: $SYNCED"
echo "  Files already current: $SKIPPED"
echo ""
echo "Note: Episodic memory, handoff documents, and setup-dependant content are NOT synced"
echo "      (those are repo-specific, not user-level)"
