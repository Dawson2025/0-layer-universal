#!/usr/bin/env bash
# resource_id: "c7d8e9f0-1a2b-4c3d-e4f5-6a7b8c9d0e1f"
# resource_type: "script"
# resource_name: "assign-dir-uuids"
#
# Assigns a UUID v4 to every directory under 0_layer_universal/ via .dir-id files.
# Replaces empty .gitkeep files (which only existed to keep dirs in git).
# Non-empty .gitkeep files are preserved.
#
# Usage: assign-dir-uuids.sh [--dry-run] [ROOT_DIR]

set -euo pipefail

DRY_RUN=false
ROOT_DIR=""

for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=true ;;
        *) ROOT_DIR="$arg" ;;
    esac
done

if [[ -z "$ROOT_DIR" ]]; then
    ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fi

created=0
skipped=0
gitkeep_removed=0

while IFS= read -r dir; do
    dir_id_file="$dir/.dir-id"

    # Skip if .dir-id already exists
    if [[ -f "$dir_id_file" ]]; then
        ((skipped++))
        continue
    fi

    uuid=$(cat /proc/sys/kernel/random/uuid)

    if $DRY_RUN; then
        echo "[dry-run] Would create $dir_id_file with $uuid"
    else
        echo "$uuid" > "$dir_id_file"
    fi
    ((created++))

    # Remove empty .gitkeep if present
    gitkeep="$dir/.gitkeep"
    if [[ -f "$gitkeep" ]] && [[ ! -s "$gitkeep" ]]; then
        if $DRY_RUN; then
            echo "[dry-run] Would remove empty $gitkeep"
        else
            rm "$gitkeep"
        fi
        ((gitkeep_removed++))
    fi
done < <(find "$ROOT_DIR" -type d -not -path '*/.git' -not -path '*/.git/*')

echo ""
echo "=== Directory UUID Assignment Complete ==="
echo "Created:         $created"
echo "Skipped (exist): $skipped"
echo "Gitkeep removed: $gitkeep_removed"
if $DRY_RUN; then
    echo "(dry run — no files modified)"
fi
