#!/usr/bin/env bash
# manage-avenues.sh — CRUD operations for context avenue web directories
#
# Usage:
#   manage-avenues.sh [context_avenue_web_dir] <command> [args...]
#
# Commands:
#   list                          List all avenues with numbers and names
#   status                        Show population status (which have content)
#   insert <position> <name>      Insert new avenue at position, renumber others
#   delete <number>               Delete avenue at number, renumber others
#   move <from> <to>              Move avenue from one position to another
#   sync                          Regenerate registry.json from directory state
#
# If context_avenue_web_dir is omitted, uses the parent of this script's directory.
#
# Examples:
#   ./manage-avenues.sh list
#   ./manage-avenues.sh insert 03 auto_memory
#   ./manage-avenues.sh delete 03
#   ./manage-avenues.sh move 05 02
#   ./manage-avenues.sh status
#   ./manage-avenues.sh sync

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Determine base dir and command
if [[ $# -ge 2 ]] && [[ -d "$1" ]]; then
    BASE_DIR="$1"
    shift
elif [[ $# -ge 1 ]]; then
    BASE_DIR="$(dirname "$SCRIPT_DIR")"
else
    echo "Usage: manage-avenues.sh [context_avenue_web_dir] <command> [args...]"
    exit 1
fi

REGISTRY_DIR="$BASE_DIR/00_context_avenue_web_registry"
REGISTRY_JSON="$REGISTRY_DIR/registry.json"
COMMAND="${1:-}"
shift || true

# ─── Helpers ───

# Get sorted list of avenue directories (NN_name format, excluding 00_ registry)
get_avenues() {
    find "$BASE_DIR" -maxdepth 1 -mindepth 1 -type d -name '[0-9][0-9]_*' \
        | sort \
        | while read -r dir; do
            local base
            base=$(basename "$dir")
            # Skip the registry itself
            [[ "$base" == 00_* ]] && continue
            echo "$base"
        done
}

# Extract number from directory name (e.g., "03_auto_memory" → "03")
get_number() {
    echo "$1" | grep -oP '^\d{2}'
}

# Extract name from directory name (e.g., "03_auto_memory" → "auto_memory")
get_name() {
    echo "$1" | sed 's/^[0-9][0-9]_//'
}

# Check if a directory has content beyond .gitkeep
is_populated() {
    local dir="$1"
    local count
    count=$(find "$dir" -mindepth 1 -not -name '.gitkeep' | wc -l)
    [[ $count -gt 0 ]]
}

# Pad number to 2 digits
pad_num() {
    printf "%02d" "$1"
}

# ─── Commands ───

cmd_list() {
    echo "Context Avenue Web — $(basename "$BASE_DIR")"
    echo "Ordering: comprehensive → fragmented"
    echo ""
    printf "%-4s %-35s %s\n" "#" "Directory" "Name"
    printf "%-4s %-35s %s\n" "---" "-----------------------------------" "----"
    get_avenues | while read -r ave; do
        local num name
        num=$(get_number "$ave")
        name=$(get_name "$ave")
        printf "%-4s %-35s %s\n" "$num" "$ave" "$name"
    done
}

cmd_status() {
    echo "Context Avenue Web — Population Status"
    echo ""
    printf "%-4s %-35s %-10s %s\n" "#" "Directory" "Status" "File Count"
    printf "%-4s %-35s %-10s %s\n" "---" "-----------------------------------" "----------" "----------"
    get_avenues | while read -r ave; do
        local num dir count status
        num=$(get_number "$ave")
        dir="$BASE_DIR/$ave"
        count=$(find "$dir" -mindepth 1 -not -name '.gitkeep' -type f | wc -l)
        if [[ $count -gt 0 ]]; then
            status="POPULATED"
        else
            status="empty"
        fi
        printf "%-4s %-35s %-10s %s\n" "$num" "$ave" "$status" "${count} files"
    done
}

cmd_insert() {
    local position="${1:-}"
    local name="${2:-}"

    if [[ -z "$position" ]] || [[ -z "$name" ]]; then
        echo "Usage: manage-avenues.sh insert <position> <name>"
        echo "  position: 2-digit number (e.g., 03)"
        echo "  name: avenue name without number prefix (e.g., auto_memory)"
        exit 1
    fi

    local pos_int
    pos_int=$((10#$position))
    local new_dir="${position}_${name}"

    # Check if target already exists
    if [[ -d "$BASE_DIR/$new_dir" ]]; then
        echo "ERROR: $new_dir already exists"
        exit 1
    fi

    echo "Inserting $new_dir at position $position..."

    # Renumber existing avenues >= position (highest first to avoid collisions)
    get_avenues | tac | while read -r ave; do
        local num num_int new_num new_ave
        num=$(get_number "$ave")
        num_int=$((10#$num))
        if [[ $num_int -ge $pos_int ]]; then
            new_num=$(pad_num $((num_int + 1)))
            new_ave="${new_num}_$(get_name "$ave")"
            echo "  Renumber: $ave → $new_ave"
            mv "$BASE_DIR/$ave" "$BASE_DIR/$new_ave"
        fi
    done

    # Create new avenue
    mkdir -p "$BASE_DIR/$new_dir"
    touch "$BASE_DIR/$new_dir/.gitkeep"
    echo "  Created: $new_dir"

    echo ""
    echo "Done. Run 'manage-avenues.sh sync' to update registry.json"
}

cmd_delete() {
    local number="${1:-}"

    if [[ -z "$number" ]]; then
        echo "Usage: manage-avenues.sh delete <number>"
        echo "  number: 2-digit avenue number (e.g., 03)"
        exit 1
    fi

    local num_int target_dir
    num_int=$((10#$number))

    # Find the directory with this number
    target_dir=""
    get_avenues | while read -r ave; do
        if [[ "$(get_number "$ave")" == "$number" ]]; then
            echo "$ave"
            return
        fi
    done | read -r target_dir || true

    if [[ -z "$target_dir" ]]; then
        echo "ERROR: No avenue found at position $number"
        exit 1
    fi

    # Check if populated
    if is_populated "$BASE_DIR/$target_dir"; then
        echo "WARNING: $target_dir has content!"
        local count
        count=$(find "$BASE_DIR/$target_dir" -mindepth 1 -not -name '.gitkeep' -type f | wc -l)
        echo "  $count files will be deleted."
        read -rp "  Type 'yes' to confirm: " confirm
        if [[ "$confirm" != "yes" ]]; then
            echo "Aborted."
            exit 0
        fi
    fi

    echo "Deleting $target_dir..."
    rm -rf "$BASE_DIR/$target_dir"
    echo "  Removed: $target_dir"

    # Renumber avenues > number (lowest first)
    get_avenues | while read -r ave; do
        local num ave_num_int new_num new_ave
        num=$(get_number "$ave")
        ave_num_int=$((10#$num))
        if [[ $ave_num_int -gt $num_int ]]; then
            new_num=$(pad_num $((ave_num_int - 1)))
            new_ave="${new_num}_$(get_name "$ave")"
            echo "  Renumber: $ave → $new_ave"
            mv "$BASE_DIR/$ave" "$BASE_DIR/$new_ave"
        fi
    done

    echo ""
    echo "Done. Run 'manage-avenues.sh sync' to update registry.json"
}

cmd_move() {
    local from="${1:-}"
    local to="${2:-}"

    if [[ -z "$from" ]] || [[ -z "$to" ]]; then
        echo "Usage: manage-avenues.sh move <from> <to>"
        echo "  from: current 2-digit number (e.g., 05)"
        echo "  to:   target 2-digit number (e.g., 02)"
        exit 1
    fi

    local from_int to_int
    from_int=$((10#$from))
    to_int=$((10#$to))

    if [[ $from_int -eq $to_int ]]; then
        echo "Nothing to do — from and to are the same."
        exit 0
    fi

    # Find the source directory
    local source_ave source_name
    source_ave=""
    for ave in $(get_avenues); do
        if [[ "$(get_number "$ave")" == "$from" ]]; then
            source_ave="$ave"
            source_name=$(get_name "$ave")
            break
        fi
    done

    if [[ -z "$source_ave" ]]; then
        echo "ERROR: No avenue found at position $from"
        exit 1
    fi

    echo "Moving $source_ave from position $from to $to..."

    # Step 1: Move source to temp
    local tmp_dir="__tmp_move_${source_name}"
    mv "$BASE_DIR/$source_ave" "$BASE_DIR/$tmp_dir"

    # Step 2: Renumber gap
    if [[ $from_int -lt $to_int ]]; then
        # Moving down: shift avenues between (from+1..to) up by -1
        get_avenues | while read -r ave; do
            local num num_int new_num new_ave
            num=$(get_number "$ave")
            num_int=$((10#$num))
            if [[ $num_int -gt $from_int ]] && [[ $num_int -le $to_int ]]; then
                new_num=$(pad_num $((num_int - 1)))
                new_ave="${new_num}_$(get_name "$ave")"
                echo "  Renumber: $ave → $new_ave"
                mv "$BASE_DIR/$ave" "$BASE_DIR/$new_ave"
            fi
        done
    else
        # Moving up: shift avenues between (to..from-1) down by +1
        get_avenues | tac | while read -r ave; do
            local num num_int new_num new_ave
            num=$(get_number "$ave")
            num_int=$((10#$num))
            if [[ $num_int -ge $to_int ]] && [[ $num_int -lt $from_int ]]; then
                new_num=$(pad_num $((num_int + 1)))
                new_ave="${new_num}_$(get_name "$ave")"
                echo "  Renumber: $ave → $new_ave"
                mv "$BASE_DIR/$ave" "$BASE_DIR/$new_ave"
            fi
        done
    fi

    # Step 3: Place source at target
    local target_ave="${to}_${source_name}"
    mv "$BASE_DIR/$tmp_dir" "$BASE_DIR/$target_ave"
    echo "  Placed: $target_ave"

    echo ""
    echo "Done. Run 'manage-avenues.sh sync' to update registry.json"
}

cmd_sync() {
    echo "Syncing registry.json from directory state..."

    # Load existing registry for scope/description preservation
    local existing_json="{}"
    if [[ -f "$REGISTRY_JSON" ]]; then
        existing_json=$(cat "$REGISTRY_JSON")
    fi

    # Build new registry from directory state, preserving scope/description
    get_avenues | while read -r ave; do
        local num name count populated scope desc
        num=$(get_number "$ave")
        name=$(get_name "$ave")
        count=$(find "$BASE_DIR/$ave" -mindepth 1 -not -name '.gitkeep' -type f | wc -l)
        if [[ $count -gt 0 ]]; then populated="true"; else populated="false"; fi

        # Try to preserve scope and description from existing registry
        scope=$(echo "$existing_json" | jq -r --arg name "$name" '.avenues[]? | select(.name == $name) | .scope // empty' 2>/dev/null || true)
        desc=$(echo "$existing_json" | jq -r --arg name "$name" '.avenues[]? | select(.name == $name) | .description // empty' 2>/dev/null || true)

        jq -n \
            --arg num "$num" \
            --arg name "$name" \
            --arg dir "$ave" \
            --argjson pop "$populated" \
            --argjson fc "$count" \
            --arg scope "$scope" \
            --arg desc "$desc" \
            '{number: $num, name: $name, dir: $dir, scope: $scope, description: $desc, populated: $pop, file_count: $fc}
             | if .scope == "" then del(.scope) else . end
             | if .description == "" then del(.description) else . end'
    done | jq -s '{
        ordering_principle: "Most comprehensive (full agent graphs) \u2192 most fragmented (event-triggered scripts)",
        avenues: .
    }' > "$REGISTRY_JSON"

    echo "  Written: $REGISTRY_JSON"
    echo ""
    echo "Current avenues:"
    jq -r '.avenues[] | "  \(.number) \(.dir)  [\(if .populated then "POPULATED \(.file_count) files" else "empty" end)]"' "$REGISTRY_JSON"
}

# ─── Dispatch ───

case "$COMMAND" in
    list)   cmd_list ;;
    status) cmd_status ;;
    insert) cmd_insert "$@" ;;
    delete) cmd_delete "$@" ;;
    move)   cmd_move "$@" ;;
    sync)   cmd_sync ;;
    *)
        echo "Context Avenue Web Manager"
        echo ""
        echo "Usage: manage-avenues.sh [context_avenue_web_dir] <command> [args...]"
        echo ""
        echo "Commands:"
        echo "  list                    List all avenues"
        echo "  status                  Show population status"
        echo "  insert <pos> <name>     Insert new avenue, renumber others"
        echo "  delete <number>         Delete avenue, renumber others"
        echo "  move <from> <to>        Move avenue to new position"
        echo "  sync                    Regenerate registry.json from dirs"
        echo ""
        echo "Examples:"
        echo "  manage-avenues.sh list"
        echo "  manage-avenues.sh insert 03 auto_memory"
        echo "  manage-avenues.sh delete 03"
        echo "  manage-avenues.sh move 05 02"
        ;;
esac
