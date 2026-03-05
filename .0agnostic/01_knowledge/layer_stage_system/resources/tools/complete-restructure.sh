#!/bin/bash
# resource_id: "827ca8fe-c1d0-4ac2-8beb-69200d844688"
# resource_type: "script"
# resource_name: "complete-restructure"
# complete-restructure.sh — Complete the agent_delegation_system restructuring
# Run from: ~/dawson-workspace/code/0_layer_universal/
set -e

BASE="layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features"

echo "=== Step 1: Rename memory_system to subx2 ==="
if [ -d "$BASE/layer_2_sub_feature_memory_system" ]; then
  mv "$BASE/layer_2_sub_feature_memory_system" "$BASE/layer_2_subx2_feature_memory_system"
  echo "  Renamed to layer_2_subx2_feature_memory_system"
elif [ -d "$BASE/layer_2_subx2_feature_memory_system" ]; then
  echo "  Already renamed"
else
  echo "  ERROR: memory_system not found at expected path"
  exit 1
fi

echo ""
echo "=== Step 2: Renumber multi_agent_system ==="
if [ -d "$BASE/layer_1_sub_feature_multi_agent_system" ]; then
  bash tools/renumber-layers.sh "$BASE/layer_1_sub_feature_multi_agent_system" 3
  # The script renames the top-level dir to layer_2_sub_feature_multi_agent_system
  # We need to also do the sub_feature -> subx2_feature rename
  if [ -d "$BASE/layer_2_sub_feature_multi_agent_system" ]; then
    mv "$BASE/layer_2_sub_feature_multi_agent_system" "$BASE/layer_2_subx2_feature_multi_agent_system"
    echo "  Renamed to layer_2_subx2_feature_multi_agent_system"
  fi
elif [ -d "$BASE/layer_2_subx2_feature_multi_agent_system" ]; then
  echo "  Already renumbered"
else
  echo "  ERROR: multi_agent_system not found"
  exit 1
fi

echo ""
echo "=== Step 3: Move both into agent_delegation_system ==="
ADS="$BASE/layer_1_sub_feature_agent_delegation_system"

if [ -d "$BASE/layer_2_subx2_feature_memory_system" ]; then
  mv "$BASE/layer_2_subx2_feature_memory_system" "$ADS/layer_2_group/layer_2_subx2_features/"
  echo "  Moved memory_system"
fi

if [ -d "$BASE/layer_2_subx2_feature_multi_agent_system" ]; then
  mv "$BASE/layer_2_subx2_feature_multi_agent_system" "$ADS/layer_2_group/layer_2_subx2_features/"
  echo "  Moved multi_agent_system"
fi

echo ""
echo "=== Step 4: Verify ==="
echo "Contents of $ADS/layer_2_group/layer_2_subx2_features/:"
ls "$ADS/layer_2_group/layer_2_subx2_features/"

echo ""
echo "Checking for stale layer_1_ references in memory_system:"
STALE_MEM=$(grep -rl "layer_1_sub_feature\|stage_1_" "$ADS/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/" --include="*.md" --include="*.json" --include="*.jsonld" 2>/dev/null | head -20)
if [ -z "$STALE_MEM" ]; then
  echo "  None found (good)"
else
  echo "  FOUND stale references:"
  echo "$STALE_MEM"
fi

echo ""
echo "Checking for stale layer_1_ references in multi_agent_system:"
STALE_MAS=$(grep -rl "layer_1_sub_feature\|stage_1_" "$ADS/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_multi_agent_system/" --include="*.md" --include="*.json" --include="*.jsonld" 2>/dev/null | head -20)
if [ -z "$STALE_MAS" ]; then
  echo "  None found (good)"
else
  echo "  FOUND stale references:"
  echo "$STALE_MAS"
fi

echo ""
echo "=== Restructuring complete ==="
echo "Remaining manual tasks:"
echo "  1. Update parent 0AGNOSTIC.md (layer_0_feature_layer_stage_system)"
echo "  2. Update memory_system/0AGNOSTIC.md parent pointer"
echo "  3. Update multi_agent_system/0AGNOSTIC.md parent pointer"
echo "  4. Run agnostic-sync.sh on updated 0AGNOSTIC.md files"
echo "  5. git add -A && git commit -m '[AI Context] Create agent_delegation_system'"
