#!/bin/bash
# resource_id: "92ab3def-22d7-48cd-91be-6744c3466240"
# resource_type: "script"
# resource_name: "assign-entity-uuids"
#
# assign-entity-uuids.sh — Assign entity_id UUIDs to all 0AGNOSTIC.md files
#
# Finds all 0AGNOSTIC.md files with a ## Identity section, and inserts
# entity_id: "uuid" if not already present.
#
# Usage:
#   assign-entity-uuids.sh              # Assign UUIDs to all entities
#   assign-entity-uuids.sh --dry-run    # Show what would change
#   assign-entity-uuids.sh --verbose    # Show each file processed
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DRY_RUN=false
VERBOSE=false

for arg in "$@"; do
    case "$arg" in
        --dry-run)  DRY_RUN=true ;;
        --verbose)  VERBOSE=true ;;
        --help|-h)
            echo "Usage: assign-entity-uuids.sh [--dry-run] [--verbose]"
            echo ""
            echo "  --dry-run    Show what would change without modifying files"
            echo "  --verbose    Show each file processed"
            exit 0
            ;;
        *) echo "Unknown option: $arg"; exit 1 ;;
    esac
done

# Counters
ASSIGNED=0
SKIPPED=0
TOTAL=0

vlog() {
    if $VERBOSE; then
        echo "  [verbose] $*"
    fi
}

# Generate UUID v4
generate_uuid() {
    if command -v uuidgen > /dev/null 2>&1; then
        uuidgen | tr '[:upper:]' '[:lower:]'
    elif [ -f /proc/sys/kernel/random/uuid ]; then
        cat /proc/sys/kernel/random/uuid
    else
        python3 -c "import uuid; print(uuid.uuid4())"
    fi
}

echo "Assign Entity UUIDs — scanning 0AGNOSTIC.md files in $ROOT"
echo ""

# Find all 0AGNOSTIC.md files in layer paths
while IFS= read -r file; do
    TOTAL=$((TOTAL + 1))
    RELATIVE="${file#$ROOT/}"

    # Check if file has ## Identity section
    if ! grep -q "^## Identity" "$file"; then
        vlog "SKIP (no Identity section): $RELATIVE"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Check if entity_id already exists
    if grep -q "^entity_id:" "$file"; then
        vlog "SKIP (already has entity_id): $RELATIVE"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Generate UUID
    UUID=$(generate_uuid)

    if $DRY_RUN; then
        echo "  WOULD ADD: entity_id: \"$UUID\" to $RELATIVE"
        ASSIGNED=$((ASSIGNED + 1))
    else
        # Insert entity_id on the line after ## Identity
        # Use awk to find ## Identity and insert the ID + blank line after it
        awk -v uuid="$UUID" '
        /^## Identity/ {
            print
            # Check if next line is blank
            getline nextline
            if (nextline == "") {
                print ""
                print "entity_id: \"" uuid "\""
                print ""
            } else {
                print ""
                print "entity_id: \"" uuid "\""
                print ""
                print nextline
            }
            next
        }
        { print }
        ' "$file" > "${file}.tmp"
        mv "${file}.tmp" "$file"
        echo "  ADDED: entity_id: \"$UUID\" → $RELATIVE"
        ASSIGNED=$((ASSIGNED + 1))
    fi
done < <(find "$ROOT" -name "0AGNOSTIC.md" -path "*/layer_*" -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | sort)

echo ""
echo "--- Assign Entity UUIDs Summary ---"
echo "Total 0AGNOSTIC.md files: $TOTAL"
if $DRY_RUN; then
    echo "Would assign: $ASSIGNED"
else
    echo "Assigned: $ASSIGNED"
fi
echo "Skipped (already had ID): $SKIPPED"
