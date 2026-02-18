#!/usr/bin/env bash
# implement-0agnostic-1merge-avenue-web.sh
# Stage 2.06 development helper: enforce 0agnostic/.1merge shape and run Avenue Web MVP validation.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGE_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

# Discover better_ai_system root by walking upward until shared validator path exists.
BETTER_AI_SYSTEM_ROOT="$STAGE_ROOT"
while [[ ! -x "$BETTER_AI_SYSTEM_ROOT/.0agnostic/hooks/scripts/validate-avenue-web.sh" ]]; do
  NEXT="$(cd "$BETTER_AI_SYSTEM_ROOT/.." && pwd)"
  if [[ "$NEXT" == "$BETTER_AI_SYSTEM_ROOT" ]]; then
    echo "Could not locate better_ai_system root from: $STAGE_ROOT" >&2
    exit 1
  fi
  BETTER_AI_SYSTEM_ROOT="$NEXT"
done

FEATURE_ROOT_REL="layer_0_group/layer_0_features/layer_0_feature_layer_stage_system"
FEATURE_ROOT="$BETTER_AI_SYSTEM_ROOT/$FEATURE_ROOT_REL"

VALIDATOR="$BETTER_AI_SYSTEM_ROOT/.0agnostic/hooks/scripts/validate-avenue-web.sh"
REPORT_PATH="$FEATURE_ROOT/layer_1_group/layer_1_sub_features/layer_1_sub_feature_memory_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_context_chain_system/layer_2_group/layer_2_99_stages/stage_2_07_testing/outputs/by_topic/avenue_web_validation_report.md"

echo "[1/4] Enforcing canonical .0agnostic class directories in stage_2_06..."
mkdir -p \
  "$STAGE_ROOT/.0agnostic/knowledge" \
  "$STAGE_ROOT/.0agnostic/principles" \
  "$STAGE_ROOT/.0agnostic/rules" \
  "$STAGE_ROOT/.0agnostic/protocols"

echo "[2/4] Enforcing .1merge 3-tier directories..."
for tool in aider claude codex copilot cursor gemini; do
  mkdir -p \
    "$STAGE_ROOT/.1merge/.1${tool}_merge/0_synced" \
    "$STAGE_ROOT/.1merge/.1${tool}_merge/1_overrides" \
    "$STAGE_ROOT/.1merge/.1${tool}_merge/2_additions"
done

echo "[3/4] Verifying shared Avenue Web validator exists..."
if [[ ! -x "$VALIDATOR" ]]; then
  echo "Missing validator: $VALIDATOR" >&2
  exit 1
fi

echo "[4/4] Running Avenue Web MVP validation..."
"$VALIDATOR" "$FEATURE_ROOT" "$REPORT_PATH"
echo "Validation complete: $REPORT_PATH"
