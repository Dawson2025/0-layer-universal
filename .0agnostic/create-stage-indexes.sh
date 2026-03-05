#!/bin/bash
# resource_id: "bcac347f-f4e3-4047-8171-ed9a20022624"
# resource_type: "script"
# resource_name: "create-stage-indexes"
#
# create-stage-indexes.sh — Create stage_index.json for all entities with stages
#
# For each entity that has a layer_N_99_stages/ directory:
# 1. Finds all stage_N_XX_* sibling directories
# 2. Assigns stage_id UUID to each stage's 0AGNOSTIC.md (if it exists)
# 3. Creates/updates stage_index.json in stage_N_00_stage_registry/
#
# Usage:
#   create-stage-indexes.sh              # Create all stage indexes
#   create-stage-indexes.sh --dry-run    # Show what would change
#   create-stage-indexes.sh --verbose    # Show each file processed
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
            echo "Usage: create-stage-indexes.sh [--dry-run] [--verbose]"
            exit 0
            ;;
        *) echo "Unknown option: $arg"; exit 1 ;;
    esac
done

INDEXES_CREATED=0
STAGES_ASSIGNED=0
STAGES_SKIPPED=0
TOTAL_ENTITIES=0

vlog() {
    if $VERBOSE; then
        echo "  [verbose] $*"
    fi
}

generate_uuid() {
    if command -v uuidgen > /dev/null 2>&1; then
        uuidgen | tr '[:upper:]' '[:lower:]'
    elif [ -f /proc/sys/kernel/random/uuid ]; then
        cat /proc/sys/kernel/random/uuid
    else
        python3 -c "import uuid; print(uuid.uuid4())"
    fi
}

# Extract entity_id from a 0AGNOSTIC.md file
get_entity_id() {
    local file="$1"
    if [ -f "$file" ]; then
        grep "^entity_id:" "$file" 2>/dev/null | head -1 | sed 's/^entity_id:[[:space:]]*//' | sed 's/^["'"'"']//;s/["'"'"']$//' || true
    fi
}

# Extract stage_id from a stage's 0AGNOSTIC.md
get_stage_id() {
    local file="$1"
    if [ -f "$file" ]; then
        grep "^stage_id:" "$file" 2>/dev/null | head -1 | sed 's/^stage_id:[[:space:]]*//' | sed 's/^["'"'"']//;s/["'"'"']$//' || true
    fi
}

echo "Create Stage Indexes — scanning for stage registries in $ROOT"
echo ""

# Find all stage registry directories
while IFS= read -r registry_dir; do
    TOTAL_ENTITIES=$((TOTAL_ENTITIES + 1))

    # The stages directory is the parent of the registry
    stages_dir="$(dirname "$registry_dir")"
    # The entity directory is the grandparent's parent (stages_dir is layer_N_99_stages, parent is layer_N_group)
    layer_group_dir="$(dirname "$stages_dir")"
    entity_dir="$(dirname "$layer_group_dir")"

    relative_entity="${entity_dir#$ROOT/}"
    entity_name="$(basename "$entity_dir")"
    vlog "Processing entity: $relative_entity"

    # Get entity_id from the entity's 0AGNOSTIC.md
    entity_agnostic="$entity_dir/0AGNOSTIC.md"
    entity_id=$(get_entity_id "$entity_agnostic")
    if [ -z "$entity_id" ]; then
        echo "  WARN: No entity_id in $relative_entity/0AGNOSTIC.md — skipping"
        continue
    fi

    # Determine stage prefix from registry dir name (e.g., stage_3_00 -> stage_3_)
    registry_basename="$(basename "$registry_dir")"
    # Extract prefix: stage_N_ from stage_N_00_stage_registry
    stage_prefix="${registry_basename%%00_stage_registry}"

    # Find all stage directories (siblings of registry in stages_dir)
    stages_json="["
    first=true

    while IFS= read -r stage_dir; do
        stage_basename="$(basename "$stage_dir")"
        # Skip if it's not a stage dir (must match stage_N_XX_*)
        if [[ ! "$stage_basename" =~ ^${stage_prefix}[0-9]{2}_ ]]; then
            continue
        fi

        # Extract stage number and name
        # e.g., stage_3_04_design -> number=04, name=design
        stage_number=$(echo "$stage_basename" | sed "s/^${stage_prefix}//" | cut -c1-2)
        stage_name=$(echo "$stage_basename" | sed "s/^${stage_prefix}[0-9][0-9]_//")

        # Check for existing stage_id in stage's 0AGNOSTIC.md
        stage_agnostic="$stage_dir/0AGNOSTIC.md"
        stage_id=""
        if [ -f "$stage_agnostic" ]; then
            stage_id=$(get_stage_id "$stage_agnostic")
        fi

        # Assign stage_id if missing
        if [ -z "$stage_id" ]; then
            stage_id=$(generate_uuid)

            if [ -f "$stage_agnostic" ]; then
                if $DRY_RUN; then
                    vlog "WOULD ADD stage_id: \"$stage_id\" to $stage_basename/0AGNOSTIC.md"
                else
                    # Insert stage_id after ## Identity line
                    if grep -q "^## Identity" "$stage_agnostic"; then
                        awk -v uuid="$stage_id" '
                        /^## Identity/ {
                            print
                            getline nextline
                            if (nextline == "") {
                                print ""
                                print "stage_id: \"" uuid "\""
                                print ""
                            } else {
                                print ""
                                print "stage_id: \"" uuid "\""
                                print ""
                                print nextline
                            }
                            next
                        }
                        { print }
                        ' "$stage_agnostic" > "${stage_agnostic}.tmp"
                        mv "${stage_agnostic}.tmp" "$stage_agnostic"
                    fi
                fi
                STAGES_ASSIGNED=$((STAGES_ASSIGNED + 1))
            fi
        else
            STAGES_SKIPPED=$((STAGES_SKIPPED + 1))
        fi

        # Build JSON entry
        if ! $first; then
            stages_json+=","
        fi
        first=false

        stages_json+="
    {
      \"stage_id\": \"$stage_id\",
      \"stage_number\": \"$stage_number\",
      \"stage_name\": \"$stage_name\",
      \"directory\": \"$stage_basename\"
    }"
    done < <(find "$stages_dir" -maxdepth 1 -mindepth 1 -type d 2>/dev/null | sort)

    stages_json+="
  ]"

    # Build the full index JSON
    index_json="{
  \"entity_id\": \"$entity_id\",
  \"entity_name\": \"$entity_name\",
  \"stages\": $stages_json
}"

    index_file="$registry_dir/stage_index.json"

    if $DRY_RUN; then
        echo "  WOULD CREATE: ${index_file#$ROOT/}"
        INDEXES_CREATED=$((INDEXES_CREATED + 1))
    else
        echo "$index_json" > "${index_file}.tmp"
        mv "${index_file}.tmp" "$index_file"
        echo "  CREATED: ${index_file#$ROOT/}"
        INDEXES_CREATED=$((INDEXES_CREATED + 1))
    fi
done < <(find "$ROOT" -type d -name "stage_*_00_stage_registry" -not -path "*/node_modules/*" -not -path "*/.git/*" 2>/dev/null | sort)

echo ""
echo "--- Create Stage Indexes Summary ---"
echo "Total entities with stages: $TOTAL_ENTITIES"
if $DRY_RUN; then
    echo "Would create indexes: $INDEXES_CREATED"
    echo "Would assign stage_ids: $STAGES_ASSIGNED"
else
    echo "Indexes created: $INDEXES_CREATED"
    echo "Stage IDs assigned: $STAGES_ASSIGNED"
fi
echo "Stage IDs already existed: $STAGES_SKIPPED"
