#!/usr/bin/env bash
# resource_id: "e3880e72-e7c2-4119-97d9-d338c79bdab7"
# resource_type: "script"
# resource_name: "sync-handoffs"
# sync-handoffs.sh — Populate incoming handoff documents from outgoing stage/layer reports
#
# Discovers stage reports and layer reports in outgoing directories, then copies them
# to the correct incoming directories across the hierarchy:
#   - Stage reports → entity's incoming/from_below/stage_reports/
#   - Stage reports → sibling stages' incoming/from_sides/ (left/right)
#   - Layer report → each stage's incoming/from_above/
#   - Child layer reports → parent entity's incoming/from_below/layer_reports/
#   - Manager instruction templates → each stage's incoming/from_above/
#
# Usage:
#   sync-handoffs.sh [entity_dir]               # Sync one entity
#   sync-handoffs.sh --recursive [root_dir]     # Sync entity + all descendants
#   sync-handoffs.sh --dry-run [entity_dir]     # Show what would be done
#   sync-handoffs.sh --recursive --dry-run .    # Preview full tree sync
#
# Stage report naming: layer_N.stage_NN_name.stage_report.md
# Layer report naming: layer_N.entity_name.layer_report.md

set -euo pipefail

# --- Argument parsing ---

DRY_RUN=false
RECURSIVE=false
ENTITY_DIR=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run)    DRY_RUN=true; shift ;;
        --recursive|-r) RECURSIVE=true; shift ;;
        -*)           echo "Unknown option: $1" >&2; exit 1 ;;
        *)            ENTITY_DIR="$1"; shift ;;
    esac
done

ENTITY_DIR="${ENTITY_DIR:-.}"
ENTITY_DIR="$(cd "$ENTITY_DIR" && pwd)"

# --- Helpers ---

log() { echo "[sync-handoffs] $*"; }

copy_file() {
    local src="$1" dst="$2"
    if $DRY_RUN; then
        echo "  [DRY RUN] copy → $dst"
    else
        mkdir -p "$(dirname "$dst")"
        cp "$src" "$dst"
    fi
}

# Find stage report for a given stage directory (checks 3 locations in priority order)
find_stage_report() {
    local stage_dir="$1"
    local locations=(
        "$stage_dir/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md"
        "$stage_dir/outputs/reports/stage_report.md"
        "$stage_dir/outputs/stage_report.md"
    )
    for loc in "${locations[@]}"; do
        if [[ -f "$loc" ]]; then
            echo "$loc"
            return 0
        fi
    done
    return 1
}

# Extract layer number from stage dir name: stage_2_04_design → 2, stage_-1_02_research → -1
extract_layer() {
    basename "$1" | sed -E 's/^stage_([-]?[0-9]+)_.*/\1/'
}

# Extract stage number: stage_2_04_design → 04
extract_stage_num() {
    basename "$1" | sed -E 's/^stage_[-]?[0-9]+_([0-9]+)_.*/\1/'
}

# Extract stage name: stage_2_04_design → design
extract_stage_name() {
    basename "$1" | sed -E 's/^stage_[-]?[0-9]+_[0-9]+_(.*)/\1/'
}

# Build report filename: layer_2.stage_04_design.stage_report.md
report_filename() {
    local stage_dir="$1"
    local layer=$(extract_layer "$stage_dir")
    local num=$(extract_stage_num "$stage_dir")
    local name=$(extract_stage_name "$stage_dir")
    echo "layer_${layer}.stage_${num}_${name}.stage_report.md"
}

# Create manager instruction template (skips if file already exists)
create_instruction_template() {
    local stage_dir="$1" entity_name="$2"
    local target="$stage_dir/.0agnostic/05_handoff_documents/01_incoming/01_from_above/manager_instructions.md"

    [[ -f "$target" ]] && return 0

    local layer=$(extract_layer "$stage_dir")
    local num=$(extract_stage_num "$stage_dir")
    local name=$(extract_stage_name "$stage_dir")

    if $DRY_RUN; then
        echo "  [DRY RUN] create template → $target"
        return 0
    fi

    mkdir -p "$(dirname "$target")"
    cat > "$target" << TEMPLATE
# Manager Instructions for stage_${layer}_${num}_${name}

## From
${entity_name} entity manager

## Task
<!-- What this stage should work on -->

## Context
<!-- Relevant context from other stages or entity-level decisions -->

## Constraints
<!-- Any constraints, dependencies, or guidelines -->

## Expected Outputs
<!-- What the manager expects this stage to produce -->

## Last Updated
<!-- YYYY-MM-DD -->
TEMPLATE
}

# --- Find stages directory for an entity ---
# Handles both layer_N_group/ and layer_N/ patterns

find_stages_dir() {
    local entity_dir="$1"
    # Standard pattern: layer_*_group/layer_*_99_stages
    for d in "$entity_dir"/layer_*_group/layer_*_99_stages; do
        [[ -d "$d" ]] && echo "$d" && return 0
    done
    # Non-standard pattern: layer_*/layer_*_99_stages (e.g., learning_simulation_system)
    for d in "$entity_dir"/layer_*/layer_*_99_stages; do
        [[ -d "$d" ]] && echo "$d" && return 0
    done
    return 1
}

# --- Process a single entity ---

process_entity() {
    local entity_dir="$1"
    local entity_name
    entity_name="$(basename "$entity_dir")"
    local handoff_dir="$entity_dir/.0agnostic/05_handoff_documents"

    # Must have handoff documents directory
    if [[ ! -d "$handoff_dir" ]]; then
        return 0
    fi

    # Find stages
    local stages_dir
    if ! stages_dir=$(find_stages_dir "$entity_dir"); then
        log "No stages in: $entity_name (skipping)"
        return 0
    fi

    log "Processing: $entity_name"

    # Collect stage directories
    local stage_dirs=()
    for sd in "$stages_dir"/stage_*_*/; do
        [[ -d "$sd" ]] || continue
        stage_dirs+=("${sd%/}")
    done

    local num_stages=${#stage_dirs[@]}
    if [[ $num_stages -eq 0 ]]; then
        log "  No stage directories found"
        return 0
    fi

    # Ensure entity incoming subdirectories exist
    if ! $DRY_RUN; then
        mkdir -p "$handoff_dir/01_incoming/03_from_below/stage_reports"
        mkdir -p "$handoff_dir/01_incoming/03_from_below/layer_reports"
    fi

    # Find entity's layer report (for distributing to stages' from_above)
    local entity_layer_report="$handoff_dir/02_outgoing/01_to_above/layer_report.md"

    # Count reports found
    local reports_distributed=0
    local templates_created=0

    # --- Per-stage processing ---
    for ((i=0; i<num_stages; i++)); do
        local stage_dir="${stage_dirs[$i]}"
        local stage_handoff="$stage_dir/.0agnostic/05_handoff_documents"

        # Ensure stage incoming directories exist
        if ! $DRY_RUN; then
            mkdir -p "$stage_handoff/01_incoming/01_from_above"
            mkdir -p "$stage_handoff/01_incoming/02_from_sides/01_from_left"
            mkdir -p "$stage_handoff/01_incoming/02_from_sides/02_from_right"
            mkdir -p "$stage_handoff/01_incoming/03_from_below"
        fi

        # 1. Manager instruction template
        create_instruction_template "$stage_dir" "$entity_name"
        ((templates_created++)) || true

        # 2. Entity layer report → stage's from_above
        if [[ -f "$entity_layer_report" ]]; then
            copy_file "$entity_layer_report" "$stage_handoff/01_incoming/01_from_above/layer_report.md"
        fi

        # 3. Find this stage's report
        local stage_report=""
        stage_report=$(find_stage_report "$stage_dir") || true

        if [[ -n "$stage_report" ]]; then
            local fname
            fname=$(report_filename "$stage_dir")
            log "  Distributing: $fname"
            ((reports_distributed++)) || true

            # Copy to entity's from_below/stage_reports/
            copy_file "$stage_report" "$handoff_dir/01_incoming/03_from_below/stage_reports/$fname"

            # Copy to all sibling stages' from_sides/
            local this_num
            this_num=$(extract_stage_num "$stage_dir")

            for ((j=0; j<num_stages; j++)); do
                [[ $i -eq $j ]] && continue
                local sibling_dir="${stage_dirs[$j]}"
                local sibling_handoff="$sibling_dir/.0agnostic/05_handoff_documents"
                local sibling_num
                sibling_num=$(extract_stage_num "$sibling_dir")

                # Determine direction relative to the SIBLING
                if (( 10#$this_num < 10#$sibling_num )); then
                    # This stage has a lower number → it's to the LEFT of the sibling
                    copy_file "$stage_report" "$sibling_handoff/01_incoming/02_from_sides/01_from_left/$fname"
                else
                    # This stage has a higher number → it's to the RIGHT of the sibling
                    copy_file "$stage_report" "$sibling_handoff/01_incoming/02_from_sides/02_from_right/$fname"
                fi
            done
        fi
    done

    # --- Child entity layer reports → this entity's from_below/layer_reports/ ---
    process_child_reports "$entity_dir"

    log "  Done: $reports_distributed reports distributed, $templates_created instruction templates"
}

# --- Copy child entities' layer reports to parent ---

process_child_reports() {
    local parent_dir="$1"
    local parent_handoff="$parent_dir/.0agnostic/05_handoff_documents"
    local seen_children=()

    # Search for child entities — try _group pattern first, then bare layer_*
    local child_patterns=(
        "$parent_dir/layer_*_group/layer_*_*features/layer_*_*/"
        "$parent_dir/layer_*/layer_*_*features/layer_*_*/"
    )

    for pattern in "${child_patterns[@]}"; do
        for child_dir in $pattern; do
            [[ -d "$child_dir" ]] || continue
            child_dir="${child_dir%/}"
            local child_name
            child_name="$(basename "$child_dir")"

            # Dedup (both patterns can match the same dir)
            local skip=false
            for s in "${seen_children[@]+"${seen_children[@]}"}"; do
                [[ "$s" == "$child_dir" ]] && skip=true && break
            done
            $skip && continue
            seen_children+=("$child_dir")

            local child_report="$child_dir/.0agnostic/05_handoff_documents/02_outgoing/01_to_above/layer_report.md"
            if [[ -f "$child_report" ]]; then
                # Extract layer number from child's entity name
                local child_layer
                child_layer=$(echo "$child_name" | sed -E 's/^layer_([-]?[0-9]+)_.*/\1/')

                local fname="layer_${child_layer}.${child_name}.layer_report.md"
                log "  Child report: $fname"
                copy_file "$child_report" "$parent_handoff/01_incoming/03_from_below/layer_reports/$fname"
            fi
        done
    done
}

# --- Recursive: find and process all entities in the tree ---

process_recursive() {
    local root_dir="$1"
    local processed=()

    log "Recursive scan from: $root_dir"
    echo ""

    # Find all *_99_stages directories → derive entity roots
    while IFS= read -r stages_dir; do
        # Skip school submodule
        [[ "$stages_dir" == *"layer_1_project_school"* ]] && continue

        # Entity is grandparent of stages dir (parent of layer_*_group/)
        local group_dir
        group_dir="$(dirname "$stages_dir")"
        local entity_dir
        entity_dir="$(dirname "$group_dir")"

        # Dedup
        local skip=false
        for p in "${processed[@]+"${processed[@]}"}"; do
            [[ "$p" == "$entity_dir" ]] && skip=true && break
        done
        $skip && continue

        processed+=("$entity_dir")
        process_entity "$entity_dir"
        echo ""
    done < <(find "$root_dir" -type d -name "*_99_stages" ! -path "*/layer_1_project_school/*" 2>/dev/null | sort)

    log "Processed ${#processed[@]} entities total"
}

# --- Main ---

echo "=== sync-handoffs.sh ==="
echo "  Target:    $ENTITY_DIR"
echo "  Recursive: $RECURSIVE"
echo "  Dry run:   $DRY_RUN"
echo ""

if $RECURSIVE; then
    process_recursive "$ENTITY_DIR"
else
    process_entity "$ENTITY_DIR"
fi

echo ""
log "Complete!"
