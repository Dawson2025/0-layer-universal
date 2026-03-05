#!/usr/bin/env bash
# migrate-pointers.sh — Migrate name-based pointers to UUID-based pointers
# Phase 5 of the UUID Identity System implementation
#
# Usage:
#   migrate-pointers.sh [--dry-run] [--verbose] [REPO_ROOT]
#
# What it does:
#   1. Finds all pointer files (YAML frontmatter with pointer_to:)
#   2. For each pointer with canonical_entity: but no canonical_entity_id:
#      - Looks up the entity name in .uuid-index.json
#      - Adds canonical_entity_id: field
#   3. For each pointer with canonical_stage: but no canonical_stage_id:
#      - Looks up the stage in the entity's stage_index.json
#      - Adds canonical_stage_id: field
#   4. Reports all changes

set -euo pipefail

DRY_RUN=false
VERBOSE=false
REPO_ROOT=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --verbose) VERBOSE=true; shift ;;
    *) REPO_ROOT="$1"; shift ;;
  esac
done

# Default repo root
if [[ -z "$REPO_ROOT" ]]; then
  REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo ".")
fi

INDEX_FILE="$REPO_ROOT/.uuid-index.json"

# Counters
TOTAL_POINTERS=0
MIGRATED=0
ALREADY_MIGRATED=0
SKIPPED=0
ERRORS=0

log() { echo "$@"; }
verbose() { if [[ "$VERBOSE" == true ]]; then echo "  [verbose] $*" >&2; fi; return 0; }

# Check index exists
if [[ ! -f "$INDEX_FILE" ]]; then
  log "ERROR: UUID index not found at $INDEX_FILE"
  log "Run: pointer-sync.sh --rebuild-index first"
  exit 1
fi

# Look up entity UUID by name from .uuid-index.json
lookup_entity_uuid() {
  local entity_name="$1"
  local uuid
  uuid=$(jq -r --arg name "$entity_name" '.names[$name] // empty' "$INDEX_FILE" 2>/dev/null)
  if [[ -n "$uuid" ]]; then
    # Verify it's an entity type
    local entry_type
    entry_type=$(jq -r --arg uuid "$uuid" '.uuids[$uuid].type // empty' "$INDEX_FILE" 2>/dev/null)
    if [[ "$entry_type" == "entity" ]]; then
      echo "$uuid"
      return 0
    fi
  fi
  return 1
}

# Look up entity path by name from .uuid-index.json
lookup_entity_path() {
  local entity_name="$1"
  local uuid
  uuid=$(lookup_entity_uuid "$entity_name") || return 1
  jq -r --arg uuid "$uuid" '.uuids[$uuid].path // empty' "$INDEX_FILE" 2>/dev/null
}

# Look up stage UUID from entity's stage_index.json
lookup_stage_uuid() {
  local entity_path="$1"
  local stage_name="$2"

  # Find stage_index.json in the entity's stage registry
  local index_file
  index_file=$(find "$REPO_ROOT/$entity_path" -name "stage_index.json" -path "*/stage_*_00_stage_registry/*" 2>/dev/null | head -1)

  if [[ -z "$index_file" || ! -f "$index_file" ]]; then
    verbose "No stage_index.json found for entity at $entity_path"
    return 1
  fi

  # Look up stage UUID
  local uuid
  uuid=$(jq -r --arg stage "$stage_name" '.stages[$stage] // empty' "$index_file" 2>/dev/null)
  if [[ -z "$uuid" ]]; then
    # Try with stages as array format
    uuid=$(jq -r --arg stage "$stage_name" '.stages[] | select(.directory == $stage) | .stage_id // empty' "$index_file" 2>/dev/null)
  fi

  if [[ -n "$uuid" ]]; then
    echo "$uuid"
    return 0
  fi
  return 1
}

# Extract a YAML frontmatter field value
extract_field() {
  local file="$1"
  local field="$2"
  sed -n '/^---$/,/^---$/p' "$file" | grep "^${field}:" | head -1 | sed "s/^${field}:[[:space:]]*//" | tr -d '"' | tr -d "'"
}

# Check if a field exists in YAML frontmatter
field_exists() {
  local file="$1"
  local field="$2"
  sed -n '/^---$/,/^---$/p' "$file" | grep -q "^${field}:" 2>/dev/null
}

# Add a field after another field in YAML frontmatter
add_field_after() {
  local file="$1"
  local after_field="$2"
  local new_field="$3"
  local new_value="$4"

  if [[ "$DRY_RUN" == true ]]; then
    log "  [dry-run] Would add: ${new_field}: \"${new_value}\" after ${after_field}:"
    return 0
  fi

  # Use sed to insert after the target field line
  local tmp_file="${file}.migrate.tmp"
  sed "/^${after_field}:/a\\
${new_field}: \"${new_value}\"" "$file" > "$tmp_file"
  mv "$tmp_file" "$file"
}

log "=== Pointer Migration Tool ==="
log "Repo root: $REPO_ROOT"
log "Index: $INDEX_FILE"
[[ "$DRY_RUN" == true ]] && log "Mode: DRY RUN (no changes)"
log ""

# Find all pointer files
while IFS= read -r -d '' file; do
  # Check if file starts with YAML frontmatter
  first_line=$(head -1 "$file" 2>/dev/null) || continue
  [[ "$first_line" != "---" ]] && continue

  # Check if it has pointer_to: in frontmatter
  if ! field_exists "$file" "pointer_to"; then
    continue
  fi

  TOTAL_POINTERS=$((TOTAL_POINTERS + 1))
  rel_path="${file#$REPO_ROOT/}"
  verbose "Processing: $rel_path"

  needs_entity_id=false
  needs_stage_id=false
  entity_uuid=""
  entity_path=""
  stage_uuid=""

  # Check canonical_entity → canonical_entity_id
  canonical_entity=$(extract_field "$file" "canonical_entity")
  if [[ -n "$canonical_entity" ]]; then
    if field_exists "$file" "canonical_entity_id"; then
      verbose "Already has canonical_entity_id"
    else
      needs_entity_id=true
      entity_uuid=$(lookup_entity_uuid "$canonical_entity" 2>/dev/null) || true
      entity_path=$(lookup_entity_path "$canonical_entity" 2>/dev/null) || true

      if [[ -z "$entity_uuid" ]]; then
        log "  WARNING: Could not find UUID for entity '$canonical_entity' in $rel_path"
        ERRORS=$((ERRORS + 1))
      fi
    fi
  fi

  # Check canonical_stage → canonical_stage_id
  canonical_stage=$(extract_field "$file" "canonical_stage")
  if [[ -n "$canonical_stage" ]]; then
    if field_exists "$file" "canonical_stage_id"; then
      verbose "Already has canonical_stage_id"
    else
      needs_stage_id=true
      if [[ -n "$entity_path" ]]; then
        stage_uuid=$(lookup_stage_uuid "$entity_path" "$canonical_stage" 2>/dev/null) || true

        if [[ -z "$stage_uuid" ]]; then
          log "  WARNING: Could not find UUID for stage '$canonical_stage' in entity '$canonical_entity'"
          ERRORS=$((ERRORS + 1))
        fi
      else
        log "  WARNING: Cannot look up stage UUID without entity path for $rel_path"
        ERRORS=$((ERRORS + 1))
      fi
    fi
  fi

  # Apply changes
  if [[ "$needs_entity_id" == false && "$needs_stage_id" == false ]]; then
    ALREADY_MIGRATED=$((ALREADY_MIGRATED + 1))
    verbose "Already fully migrated"
    continue
  fi

  if [[ "$needs_entity_id" == true && -n "$entity_uuid" ]]; then
    log "  Adding canonical_entity_id: \"$entity_uuid\" to $rel_path"
    add_field_after "$file" "canonical_entity" "canonical_entity_id" "$entity_uuid"
    MIGRATED=$((MIGRATED + 1))
  fi

  if [[ "$needs_stage_id" == true && -n "$stage_uuid" ]]; then
    log "  Adding canonical_stage_id: \"$stage_uuid\" to $rel_path"
    add_field_after "$file" "canonical_stage" "canonical_stage_id" "$stage_uuid"
    # Don't double-count if entity was also migrated
    [[ "$needs_entity_id" == false || -z "$entity_uuid" ]] && MIGRATED=$((MIGRATED + 1))
  fi

done < <(find "$REPO_ROOT" -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*" -print0 2>/dev/null)

log ""
log "=== Migration Summary ==="
log "Total pointer files found: $TOTAL_POINTERS"
log "Migrated: $MIGRATED"
log "Already migrated: $ALREADY_MIGRATED"
log "Errors/warnings: $ERRORS"
[[ "$DRY_RUN" == true ]] && log "(Dry run — no files were modified)"
