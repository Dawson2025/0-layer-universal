#!/bin/bash
# verify_paths.sh - Verify that documented paths exist
# Run this after ANY structural change to the system
#
# Usage: ./verify_paths.sh [context_root]
# Default context_root: /home/dawson/dawson-workspace/code/0_layer_ai_context/0_context

CONTEXT_ROOT="${1:-/home/dawson/dawson-workspace/code/0_layer_ai_context/0_context}"

echo "=== Path Verification Script ==="
echo "Context root: $CONTEXT_ROOT"
echo ""

# Critical navigation documents
CRITICAL_DOCS=(
  "$CONTEXT_ROOT/MASTER_DOCUMENTATION_INDEX.md"
  "$CONTEXT_ROOT/SYSTEM_OVERVIEW.md"
  "$CONTEXT_ROOT/0.00_layer_stage_system/README.md"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.08_current_product/setup/instantiation_guide.md"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.08_current_product/changes/restructuring_migration_protocol.md"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.08_current_product/changes/traversal_update_protocol.md"
  "$CONTEXT_ROOT/0.01_layer_stage_framework/README.md"
  "$CONTEXT_ROOT/layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md"
)

# Critical directories
CRITICAL_DIRS=(
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.08_current_product/setup"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.08_current_product/changes"
  "$CONTEXT_ROOT/0.00_layer_stage_system/stages/stage_0.02_planning/hand_off_documents"
  "$CONTEXT_ROOT/0.01_layer_stage_framework"
  "$CONTEXT_ROOT/layer_0_universal/0.02_sub_layers"
  "$CONTEXT_ROOT/layer_0_universal/0.99_stages"
  "$CONTEXT_ROOT/layer_0_universal/0.99_stages/stage_0.08_current_product"
  "$CONTEXT_ROOT/layer_0_universal/0.99_stages/stage_0.09_archives"
)

FAILED=0

echo "=== Checking Critical Documents ==="
for doc in "${CRITICAL_DOCS[@]}"; do
  if [ -f "$doc" ]; then
    echo "✓ $doc"
  else
    echo "✗ MISSING: $doc"
    FAILED=$((FAILED + 1))
  fi
done

echo ""
echo "=== Checking Critical Directories ==="
for dir in "${CRITICAL_DIRS[@]}"; do
  if [ -d "$dir" ]; then
    echo "✓ $dir"
  else
    echo "✗ MISSING: $dir"
    FAILED=$((FAILED + 1))
  fi
done

echo ""
echo "=== Checking for Stale References ==="
echo "(Excluding historical documents: *SUMMARY*, *_archives*)"

# Check for old path patterns that should have been updated
# Exclude historical documents that intentionally preserve old paths
OLD_PATTERNS=(
  "0_ai_context[^_]"           # Old name without _layer_
  "mcp_servers_and_apis_and_secrets[^_]"  # Missing _clis_
  "\.08_archives"              # Old archive numbering (should be .09)
)

for pattern in "${OLD_PATTERNS[@]}"; do
  count=$(grep -r "$pattern" "$CONTEXT_ROOT"/*.md "$CONTEXT_ROOT"/0.00_layer_stage_system/**/*.md "$CONTEXT_ROOT"/0.01_layer_stage_framework/*.md 2>/dev/null | grep -v "SUMMARY" | grep -v "_archives" | wc -l)
  if [ "$count" -gt 0 ]; then
    echo "⚠ Found $count references to stale pattern: $pattern"
    FAILED=$((FAILED + 1))
  fi
done

echo ""
echo "=== Results ==="
if [ $FAILED -eq 0 ]; then
  echo "✓ All paths verified successfully!"
  exit 0
else
  echo "✗ $FAILED issues found. Please fix before committing."
  exit 1
fi
