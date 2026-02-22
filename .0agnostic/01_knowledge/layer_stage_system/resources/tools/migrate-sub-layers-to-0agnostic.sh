#!/usr/bin/env bash
# migrate-sub-layers-to-0agnostic.sh — Migrate sub_layers content into numbered .0agnostic/ structure
# Usage: bash tools/migrate-sub-layers-to-0agnostic.sh <entity-path> [--dry-run]
#
# This script:
# 1. Creates the new numbered .0agnostic/ structure
# 2. Moves sub_layer content into .0agnostic/
# 3. Renames existing unnumbered .0agnostic/ dirs to numbered
# 4. Creates per-topic knowledge subdirs (principles/, docs/, resources/)
# 5. Removes the now-empty sub_layers directory
#
# Reference: @imports/entity_structure.md

set -uo pipefail

ENTITY="${1:?Usage: migrate-sub-layers-to-0agnostic.sh <entity-path> [--dry-run]}"
ENTITY="${ENTITY%/}"
DRY_RUN="${2:-}"

MOVED=0
RENAMED=0
SKIPPED=0
ERRORS=0

log()  { echo "  [INFO]  $1"; }
warn() { echo "  [WARN]  $1"; }
err()  { echo "  [ERROR] $1"; ((ERRORS++)) || true; }
dry()  { if [ "$DRY_RUN" = "--dry-run" ]; then echo "  [DRY]   $1"; return 0; else return 1; fi; }

# Move directory contents, handling conflicts
# Usage: move_contents <src> <dst>
move_contents() {
  local src="$1" dst="$2"
  if [ ! -d "$src" ]; then return; fi
  mkdir -p "$dst"

  for item in "$src"/* "$src"/.*; do
    [ -e "$item" ] || continue
    local base
    base=$(basename "$item")
    # Skip . and ..
    [ "$base" = "." ] || [ "$base" = ".." ] && continue
    # Skip .gitkeep if destination already has content
    if [ "$base" = ".gitkeep" ]; then
      local dst_count
      dst_count=$(find "$dst" -maxdepth 1 -not -name "." -not -name ".." -not -name ".gitkeep" 2>/dev/null | wc -l)
      if [ "$dst_count" -gt 0 ]; then
        continue
      fi
    fi

    if [ -e "$dst/$base" ]; then
      if [ -d "$item" ] && [ -d "$dst/$base" ]; then
        # Both are directories — recurse
        move_contents "$item" "$dst/$base"
      else
        warn "Conflict: $dst/$base already exists, keeping destination version"
        ((SKIPPED++)) || true
      fi
    else
      if dry "Would move: $item -> $dst/$base"; then true; else
        mv "$item" "$dst/$base"
        ((MOVED++)) || true
      fi
    fi
  done
}

# Rename an unnumbered .0agnostic/ dir to its numbered equivalent
# Usage: rename_dir <old_name> <new_name>
rename_dir() {
  local agnostic="$ENTITY/.0agnostic"
  local old="$agnostic/$1"
  local new="$agnostic/$2"

  if [ -d "$old" ] && [ ! -d "$new" ]; then
    if dry "Would rename: $old -> $new"; then true; else
      mv "$old" "$new"
      log "Renamed: $1 -> $2"
      ((RENAMED++)) || true
    fi
  elif [ -d "$old" ] && [ -d "$new" ]; then
    # Both exist — merge old into new
    log "Merging: $1 -> $2 (both exist)"
    move_contents "$old" "$new"
    rmdir "$old" 2>/dev/null || warn "Could not remove $old after merge (not empty)"
  fi
}

# Create per-topic knowledge subdirs for a topic directory
# Usage: create_topic_subdirs <topic_dir>
create_topic_subdirs() {
  local topic_dir="$1"
  for tdir in principles docs resources/templates resources/tools/scripts; do
    if [ ! -d "$topic_dir/$tdir" ]; then
      if dry "Would create topic subdir: $topic_dir/$tdir"; then true; else
        mkdir -p "$topic_dir/$tdir"
      fi
    fi
  done
}

echo "=== Sub-Layers Migration: $(basename "$ENTITY") ==="
echo "Path: $ENTITY"
[ "$DRY_RUN" = "--dry-run" ] && echo "Mode: DRY RUN (no changes will be made)"
echo ""

# --- Verify entity exists ---
if [ ! -d "$ENTITY" ]; then
  err "Entity directory does not exist: $ENTITY"
  exit 1
fi

if [ ! -d "$ENTITY/.0agnostic" ]; then
  err "No .0agnostic/ directory found in entity"
  exit 1
fi

# --- Find sub_layers directory ---
# Could be layer_N_03_sub_layers or layer_N_04_sub_layers (layer_0 special case)
SUB_LAYERS=""
GROUP_DIR=""

for gdir in "$ENTITY"/layer_*_group; do
  [ -d "$gdir" ] || continue
  GROUP_DIR="$gdir"
  for sdir in "$gdir"/layer_*_sub_layers "$gdir"/*_sub_layers; do
    if [ -d "$sdir" ]; then
      SUB_LAYERS="$sdir"
      break 2
    fi
  done
done

if [ -z "$SUB_LAYERS" ]; then
  log "No sub_layers directory found — only renaming existing .0agnostic/ dirs"
fi

# --- Step 1: Create numbered .0agnostic/ structure ---
echo "--- Step 1: Ensure numbered .0agnostic/ structure ---"

AGNOSTIC="$ENTITY/.0agnostic"

# Create numbered dirs (01_knowledge is empty — topics created per-content)
for dir in \
  "01_knowledge" \
  "02_rules" "02_rules/static" "02_rules/dynamic" \
  "03_protocols" \
  "04_episodic_memory" "04_episodic_memory/sessions" "04_episodic_memory/changes" \
  "05_handoff_documents" \
  "05_handoff_documents/01_incoming/01_from_above" \
  "05_handoff_documents/01_incoming/02_from_sides/01_from_left" \
  "05_handoff_documents/01_incoming/02_from_sides/02_from_right" \
  "05_handoff_documents/01_incoming/03_from_below" \
  "05_handoff_documents/02_outgoing/01_to_above" \
  "05_handoff_documents/02_outgoing/02_to_sides/01_to_left" \
  "05_handoff_documents/02_outgoing/02_to_sides/02_to_right" \
  "05_handoff_documents/02_outgoing/03_to_below" \
  "06_context_avenue_web/01_file_based/05_skills" \
  "06_context_avenue_web/01_file_based/06_agents" \
  "06_context_avenue_web/01_file_based/08_hooks" "06_context_avenue_web/01_file_based/08_hooks/scripts" \
  "07+_setup_dependant"; do
  if [ ! -d "$AGNOSTIC/$dir" ]; then
    if dry "Would create: .0agnostic/$dir"; then true; else
      mkdir -p "$AGNOSTIC/$dir"
    fi
  fi
done

# --- Step 2: Rename existing unnumbered dirs to numbered ---
echo "--- Step 2: Rename unnumbered dirs to numbered ---"

rename_dir "knowledge"        "01_knowledge"
rename_dir "rules"            "02_rules"
rename_dir "protocols"        "03_protocols"
rename_dir "episodic_memory"  "04_episodic_memory"
rename_dir "agents"           "06_context_avenue_web/01_file_based/06_agents"
rename_dir "skills"           "06_context_avenue_web/01_file_based/05_skills"
rename_dir "hooks"            "06_context_avenue_web/01_file_based/08_hooks"

# Migrate old numbered dirs to new convention
rename_dir "04_agents"        "06_context_avenue_web/01_file_based/06_agents"
rename_dir "05_skills"        "06_context_avenue_web/01_file_based/05_skills"
rename_dir "06_hooks"         "06_context_avenue_web/01_file_based/08_hooks"
rename_dir "07_episodic_memory" "04_episodic_memory"
rename_dir "08_episodic_memory" "04_episodic_memory"
rename_dir "04+_setup_dependant" "07+_setup_dependant"

# Handle layer_0 extras — fold into numbered structure
rename_dir "prompts"          "01_knowledge/prompts"
rename_dir "scripts"          "01_knowledge/general/resources/tools/scripts"
rename_dir "templates"        "01_knowledge/general/resources/templates"
rename_dir "tests"            "01_knowledge/general/resources/tests"

# --- Step 3: Move sub_layers content into .0agnostic/ ---
if [ -n "$SUB_LAYERS" ]; then
  echo "--- Step 3: Move sub_layers content ---"
  echo "Source: $SUB_LAYERS"

  # Find knowledge_system dir (sub_layer_N_01_knowledge_system)
  for ks in "$SUB_LAYERS"/sub_layer_*_knowledge_system "$SUB_LAYERS"/*_knowledge_system; do
    if [ -d "$ks" ]; then
      log "Moving knowledge_system: $(basename "$ks")"
      # Move each subdir of knowledge_system as a topic into 01_knowledge/
      for subdir in "$ks"/*/; do
        [ -d "$subdir" ] || continue
        local_name=$(basename "$subdir")
        move_contents "$subdir" "$AGNOSTIC/01_knowledge/$local_name"
        # Create per-topic canonical subdirs
        if ! dry "Would create topic subdirs for: 01_knowledge/$local_name"; then
          create_topic_subdirs "$AGNOSTIC/01_knowledge/$local_name"
        fi
      done
      # Move loose files into 01_knowledge/ root
      for f in "$ks"/*; do
        [ -f "$f" ] || continue
        base=$(basename "$f")
        if [ "$base" != ".gitkeep" ]; then
          if dry "Would move file: $f -> $AGNOSTIC/01_knowledge/$base"; then true; else
            mv "$f" "$AGNOSTIC/01_knowledge/$base" 2>/dev/null || true
            ((MOVED++)) || true
          fi
        fi
      done
      break
    fi
  done

  # Find rules dir (sub_layer_N_02_rules)
  for rd in "$SUB_LAYERS"/sub_layer_*_rules "$SUB_LAYERS"/*_rules; do
    if [ -d "$rd" ]; then
      log "Moving rules: $(basename "$rd")"
      move_contents "$rd" "$AGNOSTIC/02_rules"
      break
    fi
  done

  # Find protocols dir (sub_layer_N_03_protocols)
  for pd in "$SUB_LAYERS"/sub_layer_*_protocols "$SUB_LAYERS"/*_protocols; do
    if [ -d "$pd" ]; then
      log "Moving protocols: $(basename "$pd")"
      move_contents "$pd" "$AGNOSTIC/03_protocols"
      break
    fi
  done

  # Find setup_dependant dir (sub_layer_N_04+_setup_dependant)
  for sd in "$SUB_LAYERS"/sub_layer_*_setup_dependant "$SUB_LAYERS"/*_setup_dependant; do
    if [ -d "$sd" ]; then
      log "Moving setup_dependant: $(basename "$sd")"
      move_contents "$sd" "$AGNOSTIC/07+_setup_dependant"
      break
    fi
  done

  # Skip registry (sub_layer_N_00_sub_layer_registry) — no longer needed
  for reg in "$SUB_LAYERS"/sub_layer_*_registry "$SUB_LAYERS"/*_registry; do
    if [ -d "$reg" ]; then
      log "Skipping registry: $(basename "$reg") (no longer needed)"
      break
    fi
  done

  # Remove loose files from sub_layers root (0AGNOSTIC.md, CLAUDE.md, etc.)
  for f in "$SUB_LAYERS"/*.md; do
    [ -f "$f" ] || continue
    log "Removing sub_layers context file: $(basename "$f")"
    if ! dry "Would remove: $f"; then
      rm "$f"
    fi
  done

  # --- Step 4: Create per-topic subdirs for any existing knowledge topics ---
  echo "--- Step 4: Ensure per-topic knowledge structure ---"

  if [ -d "$AGNOSTIC/01_knowledge" ]; then
    for topic_dir in "$AGNOSTIC/01_knowledge"/*/; do
      [ -d "$topic_dir" ] || continue
      topic_name=$(basename "$topic_dir")
      # Skip non-topic dirs (resources at root level from old structure)
      if ! dry "Would ensure topic subdirs for: 01_knowledge/$topic_name"; then
        create_topic_subdirs "$topic_dir"
        log "Ensured per-topic subdirs: 01_knowledge/$topic_name"
      fi
    done
  fi

  # --- Step 5: Remove empty sub_layers directory ---
  echo "--- Step 5: Clean up empty sub_layers ---"

  # Try to remove the sub_layers dir tree (only works if empty)
  if dry "Would remove: $SUB_LAYERS"; then true; else
    # Remove all .gitkeep files first
    find "$SUB_LAYERS" -name ".gitkeep" -delete 2>/dev/null || true
    # Remove empty dirs bottom-up
    find "$SUB_LAYERS" -type d -empty -delete 2>/dev/null || true

    if [ -d "$SUB_LAYERS" ]; then
      remaining=$(find "$SUB_LAYERS" -type f 2>/dev/null | wc -l)
      if [ "$remaining" -gt 0 ]; then
        warn "Sub_layers not fully removed — $remaining files remain"
        find "$SUB_LAYERS" -type f 2>/dev/null | head -5
      else
        rmdir "$SUB_LAYERS" 2>/dev/null || warn "Could not remove $SUB_LAYERS"
      fi
    else
      log "Sub_layers directory removed"
    fi
  fi
else
  echo "--- Step 3: No sub_layers to migrate ---"

  # Still ensure per-topic subdirs for existing knowledge topics
  echo "--- Step 4: Ensure per-topic knowledge structure ---"
  if [ -d "$AGNOSTIC/01_knowledge" ]; then
    for topic_dir in "$AGNOSTIC/01_knowledge"/*/; do
      [ -d "$topic_dir" ] || continue
      topic_name=$(basename "$topic_dir")
      if ! dry "Would ensure topic subdirs for: 01_knowledge/$topic_name"; then
        create_topic_subdirs "$topic_dir"
        log "Ensured per-topic subdirs: 01_knowledge/$topic_name"
      fi
    done
  fi
fi

echo ""
echo "================================"
echo "  Moved:   $MOVED items"
echo "  Renamed: $RENAMED dirs"
echo "  Skipped: $SKIPPED (conflicts)"
echo "  Errors:  $ERRORS"
echo "================================"

if [ "$ERRORS" -gt 0 ]; then
  echo "Migration had errors — review output above."
  exit 1
else
  echo "Migration complete."
  exit 0
fi
