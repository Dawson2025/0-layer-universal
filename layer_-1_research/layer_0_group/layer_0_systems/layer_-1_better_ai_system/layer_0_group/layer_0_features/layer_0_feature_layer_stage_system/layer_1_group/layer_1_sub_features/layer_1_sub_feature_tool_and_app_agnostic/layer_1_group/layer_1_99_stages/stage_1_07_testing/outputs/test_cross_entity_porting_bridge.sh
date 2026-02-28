#!/usr/bin/env bash
# test_cross_entity_porting_bridge.sh — Validate upstream/downstream bridge from tool_and_app_agnostic side

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STAGE_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TOOL_ENTITY_ROOT="$(cd "$STAGE_DIR/../../.." && pwd)"
SUB_FEATURES_ROOT="$(cd "$TOOL_ENTITY_ROOT/.." && pwd)"
CC_ENTITY_ROOT="$SUB_FEATURES_ROOT/layer_1_sub_feature_agent_delegation_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Cross-Entity Porting Bridge (tool_and_app_agnostic) ==="

UPSTREAM_BRIDGE="$TOOL_ENTITY_ROOT/.0agnostic/01_knowledge/overview/docs/agnostic_to_tool_porting_bridge_contract.md"
DOWNSTREAM_BRIDGE="$CC_ENTITY_ROOT/.0agnostic/01_knowledge/overview/docs/context_chain_porting_bridge_contract.md"
UPSTREAM_SYNC_DESIGN="$TOOL_ENTITY_ROOT/.0agnostic/01_knowledge/agnostic_sync_system_design.md"
DOWNSTREAM_CODEX_CONTRACT="$CC_ENTITY_ROOT/.0agnostic/01_knowledge/codex_cli_context_contract.md"

[ -f "$UPSTREAM_BRIDGE" ] && pass "Upstream bridge contract exists" || fail "Missing upstream bridge contract"
[ -f "$DOWNSTREAM_BRIDGE" ] && pass "Downstream bridge contract exists" || fail "Missing downstream bridge contract"
[ -f "$UPSTREAM_SYNC_DESIGN" ] && pass "Upstream agnostic sync design exists" || fail "Missing upstream agnostic sync design"
[ -f "$DOWNSTREAM_CODEX_CONTRACT" ] && pass "Downstream codex contract exists" || fail "Missing downstream codex contract"

if [ -f "$UPSTREAM_BRIDGE" ] && grep -q "context_chain_system" "$UPSTREAM_BRIDGE"; then
  pass "Upstream bridge references downstream context_chain_system"
else
  fail "Upstream bridge missing downstream reference"
fi

if [ -f "$DOWNSTREAM_BRIDGE" ] && grep -q "tool_and_app_agnostic" "$DOWNSTREAM_BRIDGE"; then
  pass "Downstream bridge references upstream tool_and_app_agnostic"
else
  fail "Downstream bridge missing upstream reference"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
