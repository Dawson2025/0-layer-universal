#!/bin/bash
# renumber-layers.sh v2 — Shift layer numbers in a directory tree
# Usage: renumber-layers.sh <directory> [options]
#
# Renames directories, files, and updates file contents.
# Processes from highest layer number down to lowest to avoid collisions.
#
# IMPORTANT: Does NOT change subxN_ suffixes — those track nesting depth,
# not layer number. This is intentional.
#
# Options:
#   --shift N       Shift amount (default: +1, use negative for decrement)
#   --min-layer M   Only renumber layers >= M (default: auto-detect)
#   --max-layer X   Highest layer present (default: auto-detect)
#   --dry-run       Show changes without executing
#   --verbose       Show every operation (not just summaries)

set -e

# ─── Argument parsing ───────────────────────────────────────────────

TARGET_DIR=""
SHIFT=1
MIN_LAYER=""
MAX_LAYER=""
DRY_RUN=false
VERBOSE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --shift)    SHIFT="$2"; shift 2 ;;
    --min-layer) MIN_LAYER="$2"; shift 2 ;;
    --max-layer) MAX_LAYER="$2"; shift 2 ;;
    --dry-run)  DRY_RUN=true; shift ;;
    --verbose)  VERBOSE=true; shift ;;
    -h|--help)
      cat <<'USAGE'
Usage: renumber-layers.sh <directory> [options]

Shift layer numbers in a directory tree. Renames directories, files,
and updates references inside text files.

Options:
  --shift N       Shift amount (default: +1, negative to decrement)
  --min-layer M   Only renumber layers >= M (default: auto-detect)
  --max-layer X   Highest layer present (default: auto-detect)
  --dry-run       Show changes without executing
  --verbose       Show every operation

Examples:
  # Shift layers 6-9 up by 1 (6->7, 7->8, 8->9, 9->10)
  renumber-layers.sh ./my_entity --shift 1 --min-layer 6

  # Preview what would change
  renumber-layers.sh ./my_entity --shift 1 --dry-run

  # Auto-detect range and shift up by 1
  renumber-layers.sh ./my_entity

IMPORTANT: subxN_ suffixes (subx2_, subx3_, etc.) are NEVER changed.
They track nesting depth, not layer number.
USAGE
      exit 0
      ;;
    *)
      if [ -z "$TARGET_DIR" ]; then
        TARGET_DIR="$1"
      else
        echo "ERROR: Unknown option: $1" >&2
        exit 1
      fi
      shift
      ;;
  esac
done

if [ -z "$TARGET_DIR" ] || [ ! -d "$TARGET_DIR" ]; then
  echo "ERROR: Directory required. Use --help for usage." >&2
  exit 1
fi

# Resolve to absolute path
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

# ─── Auto-detect layer range ────────────────────────────────────────

detect_layers() {
  local detected
  detected=$(find "$TARGET_DIR" \
    -path '*/.git' -prune -o \
    -path '*/venv' -prune -o \
    -path '*/.venv' -prune -o \
    -path '*/node_modules' -prune -o \
    -path '*/__pycache__' -prune -o \
    -type d -print | grep -oP 'layer_\K[0-9]+' | sort -un)

  if [ -z "$detected" ]; then
    echo "ERROR: No layer_N patterns found in $TARGET_DIR" >&2
    exit 1
  fi

  if [ -z "$MIN_LAYER" ]; then
    MIN_LAYER=$(echo "$detected" | head -1)
  fi
  if [ -z "$MAX_LAYER" ]; then
    MAX_LAYER=$(echo "$detected" | tail -1)
  fi
}

detect_layers

# ─── Validation ──────────────────────────────────────────────────────

if [ "$SHIFT" -eq 0 ]; then
  echo "Nothing to do (shift=0)."
  exit 0
fi

if [ "$SHIFT" -lt 0 ]; then
  result_min=$((MIN_LAYER + SHIFT))
  if [ "$result_min" -lt 0 ]; then
    echo "ERROR: Shift would produce negative layer numbers (layer_${MIN_LAYER} -> layer_${result_min})" >&2
    exit 1
  fi
fi

# ─── Counters (use temp files to survive subshells) ──────────────────

TMPDIR_COUNTS=$(mktemp -d)
echo 0 > "$TMPDIR_COUNTS/files"
echo 0 > "$TMPDIR_COUNTS/dirs"
trap 'rm -rf "$TMPDIR_COUNTS"' EXIT

# ─── Header ──────────────────────────────────────────────────────────

SIGN=""
[ "$SHIFT" -gt 0 ] && SIGN="+"

echo "=== renumber-layers.sh v2 ==="
echo "    Directory: $TARGET_DIR"
echo "    Shift: ${SIGN}${SHIFT}"
echo "    Range: layer_${MIN_LAYER} -> layer_$((MIN_LAYER + SHIFT)) ... layer_${MAX_LAYER} -> layer_$((MAX_LAYER + SHIFT))"
if $DRY_RUN; then
  echo "    Mode: DRY RUN (no changes)"
else
  echo "    Mode: LIVE"
fi
echo ""

# ─── Determine iteration order ──────────────────────────────────────
# Shifting UP: process highest first to avoid collisions
# Shifting DOWN: process lowest first to avoid collisions

build_layer_sequence() {
  if [ "$SHIFT" -gt 0 ]; then
    for ((n=MAX_LAYER; n>=MIN_LAYER; n--)); do echo "$n"; done
  else
    for ((n=MIN_LAYER; n<=MAX_LAYER; n++)); do echo "$n"; done
  fi
}

LAYER_SEQ=$(build_layer_sequence)

# ─── Step 1: Update file contents ───────────────────────────────────

echo "--- Step 1: Updating file contents ---"

for n in $LAYER_SEQ; do
  m=$((n + SHIFT))

  if $VERBOSE || $DRY_RUN; then
    echo "  layer_${n} -> layer_${m} in file contents..."
  fi

  # Build sed expressions for this layer number
  # NOTE: subxN_ is intentionally NOT included
  SED_ARGS=(
    -e "s/layer_${n}_/layer_${m}_/g"
    -e "s/stage_${n}_/stage_${m}_/g"
    -e "s/sub_layer_${n}_/sub_layer_${m}_/g"
    -e "s/status_${n}\\.json/status_${m}.json/g"
    -e "s/\*\*Layer ${n}\*\*/\*\*Layer ${m}\*\*/g"
    -e "s/(Layer ${n})/(Layer ${m})/g"
    -e "s/\"Layer ${n}\"/\"Layer ${m}\"/g"
    -e "s/Layer ${n} Manager/Layer ${m} Manager/g"
    -e "s|layer_${n}/|layer_${m}/|g"
  )

  if $DRY_RUN; then
    changed=$(find "$TARGET_DIR" \
      -path '*/.git' -prune -o \
      -path '*/venv' -prune -o \
      -path '*/.venv' -prune -o \
      -path '*/node_modules' -prune -o \
      -path '*/__pycache__' -prune -o \
      -type f \( -name "*.md" -o -name "*.json" -o -name "*.jsonld" -o -name "*.sh" -o -name "*.txt" -o -name "*.yaml" -o -name "*.yml" \) -print0 | \
      xargs -0 grep -l "layer_${n}_\|stage_${n}_\|sub_layer_${n}_\|status_${n}\.\|Layer ${n}\|layer_${n}/" 2>/dev/null | wc -l || true)
    if $VERBOSE && [ "$changed" -gt 0 ]; then
      echo "    -> $changed files contain references"
    fi
  else
    find "$TARGET_DIR" \
      -path '*/.git' -prune -o \
      -path '*/venv' -prune -o \
      -path '*/.venv' -prune -o \
      -path '*/node_modules' -prune -o \
      -path '*/__pycache__' -prune -o \
      -type f \( -name "*.md" -o -name "*.json" -o -name "*.jsonld" -o -name "*.sh" -o -name "*.txt" -o -name "*.yaml" -o -name "*.yml" \) -print0 | \
      xargs -0 -r sed -i "${SED_ARGS[@]}"
  fi
done

echo "  Content updates: done"
echo ""

# ─── Step 2: Rename files ───────────────────────────────────────────

echo "--- Step 2: Renaming files ---"

for n in $LAYER_SEQ; do
  m=$((n + SHIFT))

  find "$TARGET_DIR" \
    -path '*/.git' -prune -o \
    -path '*/venv' -prune -o \
    -path '*/.venv' -prune -o \
    -path '*/node_modules' -prune -o \
    -path '*/__pycache__' -prune -o \
    -depth -type f \( \
      -name "*layer_${n}_*" -o \
      -name "*stage_${n}_*" -o \
      -name "*sub_layer_${n}_*" -o \
      -name "status_${n}.*" \
    \) -print | while IFS= read -r file; do
    base=$(basename "$file")
    parent=$(dirname "$file")

    new_base="$base"
    new_base="${new_base//layer_${n}_/layer_${m}_}"
    new_base="${new_base//stage_${n}_/stage_${m}_}"
    new_base="${new_base//sub_layer_${n}_/sub_layer_${m}_}"
    new_base="${new_base//status_${n}./status_${m}.}"

    # NOTE: subxN_ is intentionally NOT changed — it tracks nesting depth

    if [ "$base" != "$new_base" ]; then
      if $DRY_RUN || $VERBOSE; then
        echo "  FILE: $base -> $new_base"
      fi
      if ! $DRY_RUN; then
        mv "$parent/$base" "$parent/$new_base"
      fi
      echo 1 >> "$TMPDIR_COUNTS/files"
    fi
  done
done

COUNT_FILES=$(wc -l < "$TMPDIR_COUNTS/files" 2>/dev/null || echo 0)
echo "  Files renamed: $COUNT_FILES"
echo ""

# ─── Step 3: Rename directories ─────────────────────────────────────

echo "--- Step 3: Renaming directories ---"

for n in $LAYER_SEQ; do
  m=$((n + SHIFT))

  # Find directories matching layer_N_*, stage_N_*, sub_layer_N_*, or bare layer_N
  find "$TARGET_DIR" \
    -path '*/.git' -prune -o \
    -path '*/venv' -prune -o \
    -path '*/.venv' -prune -o \
    -path '*/node_modules' -prune -o \
    -path '*/__pycache__' -prune -o \
    -depth -type d \( \
      -name "layer_${n}_*" -o \
      -name "stage_${n}_*" -o \
      -name "sub_layer_${n}_*" -o \
      -name "layer_${n}" \
    \) -print | while IFS= read -r dir; do
    # Skip the TARGET_DIR itself — never rename the root target
    if [ "$dir" = "$TARGET_DIR" ]; then
      continue
    fi

    base=$(basename "$dir")
    parent=$(dirname "$dir")

    new_base="$base"

    # Handle bare "layer_N" directory (exact match) first
    if [ "$base" = "layer_${n}" ]; then
      new_base="layer_${m}"
    else
      new_base="${new_base//layer_${n}_/layer_${m}_}"
      new_base="${new_base//stage_${n}_/stage_${m}_}"
      new_base="${new_base//sub_layer_${n}_/sub_layer_${m}_}"
    fi

    # NOTE: subxN_ is intentionally NOT changed — it tracks nesting depth

    if [ "$base" != "$new_base" ]; then
      if $DRY_RUN || $VERBOSE; then
        echo "  DIR:  $base -> $new_base"
      fi
      if ! $DRY_RUN; then
        mv "$parent/$base" "$parent/$new_base"
      fi
      echo 1 >> "$TMPDIR_COUNTS/dirs"
    fi
  done
done

COUNT_DIRS=$(wc -l < "$TMPDIR_COUNTS/dirs" 2>/dev/null || echo 0)
echo "  Dirs renamed: $COUNT_DIRS"
echo ""

# ─── Step 4: Find 0AGNOSTIC.md files needing agnostic-sync ──────────

echo "--- Step 4: 0AGNOSTIC.md files needing agnostic-sync.sh ---"

AGNOSTIC_COUNT=0
while IFS= read -r agfile; do
  echo "  $agfile"
  AGNOSTIC_COUNT=$((AGNOSTIC_COUNT + 1))
done < <(find "$TARGET_DIR" \
  -path '*/.git' -prune -o \
  -path '*/venv' -prune -o \
  -path '*/.venv' -prune -o \
  -path '*/node_modules' -prune -o \
  -path '*/__pycache__' -prune -o \
  -name "0AGNOSTIC.md" -print 2>/dev/null)

if [ "$AGNOSTIC_COUNT" -eq 0 ]; then
  echo "  (none found)"
fi

echo ""

# ─── Summary ─────────────────────────────────────────────────────────

FINAL_FILES=$(wc -l < "$TMPDIR_COUNTS/files" 2>/dev/null || echo 0)
FINAL_DIRS=$(wc -l < "$TMPDIR_COUNTS/dirs" 2>/dev/null || echo 0)

echo "=== Summary ==="
if $DRY_RUN; then
  echo "  Mode:          DRY RUN (no changes made)"
fi
echo "  Files renamed:   $FINAL_FILES"
echo "  Dirs renamed:    $FINAL_DIRS"
echo "  0AGNOSTIC.md:    $AGNOSTIC_COUNT files need agnostic-sync.sh"
echo ""

if ! $DRY_RUN && [ "$AGNOSTIC_COUNT" -gt 0 ]; then
  echo "Next steps:"
  echo "  1. Review changes: git diff --stat"
  echo "  2. Run agnostic-sync.sh on each entity with 0AGNOSTIC.md"
  echo "  3. Commit: git add . && git commit -m '[AI Context] layer renumbering'"
fi

echo ""
echo "NOTE: The top-level entity directory name was NOT renamed."
echo "      Rename it manually if needed."
echo "NOTE: subxN_ suffixes were intentionally preserved (they track depth, not layer)."
