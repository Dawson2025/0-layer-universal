#!/bin/bash
#
# pointer-sync.sh — Auto-update pointer files when canonical paths change
#
# Finds all markdown files with pointer_to: in YAML frontmatter,
# resolves the canonical location, computes the relative path,
# and updates the pointer file's "Canonical location" line.
#
# Usage:
#   pointer-sync.sh                  # Update all pointers
#   pointer-sync.sh --dry-run        # Show what would change
#   pointer-sync.sh --validate       # Check all pointers resolve (exit 1 if broken)
#   pointer-sync.sh --verbose        # Show each resolution step
#
# Designed to run from any directory within 0_layer_universal.
# Integrates with agnostic-sync.sh (called at end of sync).
#

set -euo pipefail

# --- Configuration ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"  # 0_layer_universal root

DRY_RUN=false
VALIDATE=false
VERBOSE=false

for arg in "$@"; do
    case "$arg" in
        --dry-run)   DRY_RUN=true ;;
        --validate)  VALIDATE=true ;;
        --verbose)   VERBOSE=true ;;
        --help|-h)
            echo "Usage: pointer-sync.sh [--dry-run] [--validate] [--verbose]"
            echo ""
            echo "  --dry-run    Show what would change without modifying files"
            echo "  --validate   Check all pointers resolve; exit 1 if any broken"
            echo "  --verbose    Show each resolution step"
            exit 0
            ;;
        *)
            echo "Unknown option: $arg"
            exit 1
            ;;
    esac
done

# --- Counters ---
UPDATED=0
UNCHANGED=0
BROKEN=0
TOTAL=0

# --- Helper: verbose log ---
vlog() {
    if $VERBOSE; then
        echo "  [verbose] $*"
    fi
}

# --- Helper: compute relative path from $1 to $2 ---
# Both must be absolute paths
relpath() {
    local source="$1"
    local target="$2"

    # Use python for reliable relative path computation
    python3 -c "import os.path; print(os.path.relpath('$target', '$source'))"
}

# --- Helper: extract frontmatter field ---
# Usage: extract_fm "field_name" "file_path"
extract_fm() {
    local field="$1"
    local file="$2"
    # Read between --- markers, strip \r, find field, strip quotes
    # Note: || true ensures missing fields return empty string instead of
    # crashing with pipefail (grep returns 1 when no match)
    sed -n '/^---/,/^---/p' "$file" | tr -d '\r' | grep "^${field}:" | head -1 | sed "s/^${field}:[[:space:]]*//" | sed 's/^["'"'"']//;s/["'"'"']$//' || true
}

# --- Helper: check if file has pointer frontmatter ---
# Must start with --- and have pointer_to: before the closing ---
has_pointer_fm() {
    local file="$1"
    # First line must be --- (strip \r for Windows line endings)
    local first_line
    first_line=$(head -1 "$file" 2>/dev/null | tr -d '\r')
    if [ "$first_line" != "---" ]; then
        return 1
    fi
    # Check for pointer_to: between the --- markers (strip \r)
    sed -n '2,/^---/p' "$file" 2>/dev/null | tr -d '\r' | grep -q "^pointer_to:" 2>/dev/null
}

# --- Main: Find all pointer files ---
echo "Pointer Sync — scanning for pointer files in $ROOT"
echo ""

# Find all .md files with pointer_to in frontmatter
# Using grep to find candidates, then verify frontmatter
POINTER_FILES=()
while IFS= read -r file; do
    if has_pointer_fm "$file"; then
        POINTER_FILES+=("$file")
    fi
done < <(grep -rl "^pointer_to:" "$ROOT" --include="*.md" 2>/dev/null || true)

if [ ${#POINTER_FILES[@]} -eq 0 ]; then
    echo "No pointer files found (files with pointer_to: in YAML frontmatter)"
    exit 0
fi

echo "Found ${#POINTER_FILES[@]} pointer file(s)"
echo ""

# --- Process each pointer file ---
for POINTER_FILE in "${POINTER_FILES[@]}"; do
    TOTAL=$((TOTAL + 1))
    RELATIVE_POINTER="${POINTER_FILE#$ROOT/}"
    vlog "Processing: $RELATIVE_POINTER"

    # Extract frontmatter fields
    POINTER_TO=$(extract_fm "pointer_to" "$POINTER_FILE")
    CANONICAL_ENTITY=$(extract_fm "canonical_entity" "$POINTER_FILE")
    CANONICAL_STAGE=$(extract_fm "canonical_stage" "$POINTER_FILE")
    CANONICAL_SUBPATH=$(extract_fm "canonical_subpath" "$POINTER_FILE")

    vlog "  pointer_to: $POINTER_TO"
    vlog "  canonical_entity: $CANONICAL_ENTITY"
    vlog "  canonical_stage: $CANONICAL_STAGE"
    vlog "  canonical_subpath: $CANONICAL_SUBPATH"

    if [ -z "$POINTER_TO" ]; then
        echo "  SKIP: $RELATIVE_POINTER — missing pointer_to field"
        continue
    fi

    # --- Resolve canonical path ---
    CANONICAL_PATH=""

    if [ -n "$CANONICAL_ENTITY" ]; then
        # Find the entity directory
        ENTITY_DIR=$(find "$ROOT" -type d -name "$CANONICAL_ENTITY" -path "*/layer_*" 2>/dev/null | head -1)

        if [ -z "$ENTITY_DIR" ]; then
            echo "  BROKEN: $RELATIVE_POINTER — entity '$CANONICAL_ENTITY' not found"
            BROKEN=$((BROKEN + 1))
            continue
        fi

        vlog "  Entity found: ${ENTITY_DIR#$ROOT/}"
        CANONICAL_PATH="$ENTITY_DIR"

        # Append stage if specified
        if [ -n "$CANONICAL_STAGE" ]; then
            STAGE_DIR=$(find "$ENTITY_DIR" -type d -name "$CANONICAL_STAGE" 2>/dev/null | head -1)
            if [ -z "$STAGE_DIR" ]; then
                echo "  BROKEN: $RELATIVE_POINTER — stage '$CANONICAL_STAGE' not found in entity"
                BROKEN=$((BROKEN + 1))
                continue
            fi
            CANONICAL_PATH="$STAGE_DIR"
            vlog "  Stage found: ${STAGE_DIR#$ROOT/}"
        fi

        # Append subpath if specified
        if [ -n "$CANONICAL_SUBPATH" ]; then
            CANONICAL_PATH="$CANONICAL_PATH/$CANONICAL_SUBPATH"
            if [ ! -e "$CANONICAL_PATH" ]; then
                echo "  BROKEN: $RELATIVE_POINTER — subpath '$CANONICAL_SUBPATH' does not exist"
                BROKEN=$((BROKEN + 1))
                continue
            fi
            vlog "  Full path: ${CANONICAL_PATH#$ROOT/}"
        fi
    else
        echo "  SKIP: $RELATIVE_POINTER — no canonical_entity (required for resolution)"
        continue
    fi

    # --- Compute relative path from pointer file's directory to canonical ---
    POINTER_DIR=$(dirname "$POINTER_FILE")
    REL_PATH=$(relpath "$POINTER_DIR" "$CANONICAL_PATH")
    vlog "  Relative path: $REL_PATH"

    # --- Update the pointer file ---
    # Find and update the "Canonical location" line
    if grep -q '> \*\*Canonical location\*\*:' "$POINTER_FILE"; then
        CURRENT_LINE=$(grep '> \*\*Canonical location\*\*:' "$POINTER_FILE")
        NEW_LINE="> **Canonical location**: \`$REL_PATH\`"

        if [ "$CURRENT_LINE" = "$NEW_LINE" ]; then
            if ! $VALIDATE; then
                echo "  OK: $RELATIVE_POINTER (unchanged)"
            fi
            UNCHANGED=$((UNCHANGED + 1))
        else
            if $DRY_RUN; then
                echo "  WOULD UPDATE: $RELATIVE_POINTER"
                echo "    Old: $CURRENT_LINE"
                echo "    New: $NEW_LINE"
                UPDATED=$((UPDATED + 1))
            elif $VALIDATE; then
                echo "  STALE: $RELATIVE_POINTER"
                echo "    Current: $CURRENT_LINE"
                echo "    Should be: $NEW_LINE"
                BROKEN=$((BROKEN + 1))
            else
                # Perform the update: find the line number and replace it
                LINE_NUM=$(grep -n '> \*\*Canonical location\*\*:' "$POINTER_FILE" | head -1 | cut -d: -f1)
                if [ -n "$LINE_NUM" ]; then
                    # Use awk to replace the specific line
                    awk -v line="$LINE_NUM" -v newtext="$NEW_LINE" 'NR==line{print newtext;next}{print}' "$POINTER_FILE" > "${POINTER_FILE}.tmp"
                    mv "${POINTER_FILE}.tmp" "$POINTER_FILE"
                fi
                echo "  UPDATED: $RELATIVE_POINTER"
                echo "    -> $REL_PATH"
                UPDATED=$((UPDATED + 1))
            fi
        fi
    else
        echo "  WARN: $RELATIVE_POINTER — no 'Canonical location' line found to update"
        UNCHANGED=$((UNCHANGED + 1))
    fi
done

# --- Summary ---
echo ""
echo "--- Pointer Sync Summary ---"
echo "Total pointer files: $TOTAL"
if $DRY_RUN; then
    echo "Would update: $UPDATED"
elif $VALIDATE; then
    echo "Valid: $UNCHANGED"
    echo "Broken/stale: $BROKEN"
else
    echo "Updated: $UPDATED"
    echo "Unchanged: $UNCHANGED"
fi
echo "Broken: $BROKEN"

# Exit code
if [ "$BROKEN" -gt 0 ]; then
    exit 1
fi
exit 0
