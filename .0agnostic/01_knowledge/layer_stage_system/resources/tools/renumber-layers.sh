#!/bin/bash
# renumber-layers.sh — Increment all layer numbers by 1 in a directory tree
# Usage: renumber-layers.sh <directory> [max_layer]
#
# Renames directories, files, and updates file contents.
# Works from highest layer number down to lowest to avoid collisions.

set -e

TARGET_DIR="$1"
MAX_LAYER="${2:-4}"

if [ -z "$TARGET_DIR" ] || [ ! -d "$TARGET_DIR" ]; then
  echo "Usage: $0 <directory> [max_layer]"
  echo "  directory: path to the entity directory to renumber"
  echo "  max_layer: highest layer number present (default: 4)"
  exit 1
fi

# Resolve to absolute path
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"

echo "=== Renumbering layers in: $TARGET_DIR ==="
echo "    Max layer: $MAX_LAYER"
echo ""

# Step 1: Update file contents (highest layer number first to avoid collisions)
echo "--- Step 1: Updating file contents ---"
for ((n=MAX_LAYER; n>=1; n--)); do
  m=$((n+1))
  echo "  layer_${n} → layer_${m} in file contents..."

  # Find all text files and do replacements
  find "$TARGET_DIR" -type f \( -name "*.md" -o -name "*.json" -o -name "*.jsonld" -o -name "*.sh" -o -name "*.txt" \) -print0 | \
    xargs -0 -r sed -i \
      -e "s/layer_${n}_/layer_${m}_/g" \
      -e "s/stage_${n}_/stage_${m}_/g" \
      -e "s/sub_layer_${n}_/sub_layer_${m}_/g" \
      -e "s/status_${n}\\.json/status_${m}.json/g" \
      -e "s/\*\*Layer ${n}\*\*/\*\*Layer ${m}\*\*/g" \
      -e "s/(Layer ${n})/(Layer ${m})/g"

  # Handle subxN feature naming in file contents
  if [ "$n" -ge 2 ]; then
    find "$TARGET_DIR" -type f \( -name "*.md" -o -name "*.json" -o -name "*.jsonld" -o -name "*.sh" -o -name "*.txt" \) -print0 | \
      xargs -0 -r sed -i \
        -e "s/subx${n}_features/subx${m}_features/g" \
        -e "s/subx${n}_feature_/subx${m}_feature_/g"
  fi
done

# Handle the special sub_feature → subx2_feature transition (layer 1 → layer 2)
echo "  sub_feature → subx2_feature in file contents..."
find "$TARGET_DIR" -type f \( -name "*.md" -o -name "*.json" -o -name "*.jsonld" -o -name "*.sh" -o -name "*.txt" \) -print0 | \
  xargs -0 -r sed -i \
    -e "s/layer_2_sub_features/layer_2_subx2_features/g" \
    -e "s/layer_2_sub_feature_/layer_2_subx2_feature_/g"

echo ""

# Step 2: Rename files with layer numbers (highest first)
echo "--- Step 2: Renaming files ---"
for ((n=MAX_LAYER; n>=1; n--)); do
  m=$((n+1))

  # Find files with layer_N, stage_N, sub_layer_N, or status_N in their name
  find "$TARGET_DIR" -depth -type f \( \
    -name "*layer_${n}_*" -o \
    -name "*stage_${n}_*" -o \
    -name "*sub_layer_${n}_*" -o \
    -name "status_${n}.*" \
  \) | while IFS= read -r file; do
    base=$(basename "$file")
    parent=$(dirname "$file")

    new_base="$base"
    new_base="${new_base//layer_${n}_/layer_${m}_}"
    new_base="${new_base//stage_${n}_/stage_${m}_}"
    new_base="${new_base//sub_layer_${n}_/sub_layer_${m}_}"
    new_base="${new_base//status_${n}./status_${m}.}"

    # Handle subxN naming
    if [ "$n" -ge 2 ]; then
      new_base="${new_base//subx${n}_/subx${m}_}"
    fi

    if [ "$base" != "$new_base" ]; then
      echo "  FILE: $base → $new_base"
      mv "$parent/$base" "$parent/$new_base"
    fi
  done
done

# Handle sub_feature → subx2_feature in file names
find "$TARGET_DIR" -depth -type f -name "*sub_feature*" | while IFS= read -r file; do
  base=$(basename "$file")
  parent=$(dirname "$file")
  # Only rename if it has layer_2_ prefix (was just renumbered from layer_1_)
  if [[ "$base" == *"layer_2_sub_feature"* ]]; then
    new_base="${base//layer_2_sub_feature/layer_2_subx2_feature}"
    if [ "$base" != "$new_base" ]; then
      echo "  FILE: $base → $new_base"
      mv "$parent/$base" "$parent/$new_base"
    fi
  fi
done

echo ""

# Step 3: Rename directories (highest layer first, deepest first within each)
echo "--- Step 3: Renaming directories ---"
for ((n=MAX_LAYER; n>=1; n--)); do
  m=$((n+1))

  # Find directories with layer_N, stage_N, or sub_layer_N in their name
  find "$TARGET_DIR" -depth -type d \( \
    -name "*layer_${n}_*" -o \
    -name "*stage_${n}_*" -o \
    -name "*sub_layer_${n}_*" \
  \) | while IFS= read -r dir; do
    base=$(basename "$dir")
    parent=$(dirname "$dir")

    new_base="$base"
    new_base="${new_base//layer_${n}_/layer_${m}_}"
    new_base="${new_base//stage_${n}_/stage_${m}_}"
    new_base="${new_base//sub_layer_${n}_/sub_layer_${m}_}"

    # Handle subxN naming in directory names
    if [ "$n" -ge 2 ]; then
      new_base="${new_base//subx${n}_/subx${m}_}"
    fi

    if [ "$base" != "$new_base" ]; then
      echo "  DIR: $base → $new_base"
      mv "$parent/$base" "$parent/$new_base"
    fi
  done
done

# Handle sub_feature → subx2_feature in directory names
# Only for directories that now have layer_2_ prefix (were layer_1_)
find "$TARGET_DIR" -depth -type d -name "*layer_2_sub_feature*" | while IFS= read -r dir; do
  base=$(basename "$dir")
  parent=$(dirname "$dir")
  new_base="${base//layer_2_sub_feature/layer_2_subx2_feature}"
  if [ "$base" != "$new_base" ]; then
    echo "  DIR: $base → $new_base"
    mv "$parent/$base" "$parent/$new_base"
  fi
done

# Also handle the plural form: sub_features → subx2_features
find "$TARGET_DIR" -depth -type d -name "*layer_2_sub_features*" | while IFS= read -r dir; do
  base=$(basename "$dir")
  parent=$(dirname "$dir")
  new_base="${base//layer_2_sub_features/layer_2_subx2_features}"
  if [ "$base" != "$new_base" ]; then
    echo "  DIR: $base → $new_base"
    mv "$parent/$base" "$parent/$new_base"
  fi
done

echo ""
echo "=== Renumbering complete ==="
echo "NOTE: The top-level entity directory name was NOT renamed."
echo "      Rename it manually if needed."
