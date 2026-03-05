#!/usr/bin/env bash
# resource_id: "531be5e4-e202-4c4a-aa9f-4d3d65ca47e6"
# resource_type: "script"
# resource_name: "test_codex_governance_runtime"
# test_codex_governance_runtime.sh — Runtime validation for knowledge/principles/rules/protocols behavior

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
CODEx_BIN="$(command -v codex || true)"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

run_codex_last_message() {
  local workdir="$1"
  local prompt="$2"
  local out_file
  out_file="$(mktemp)"

  if ! "$CODEx_BIN" exec \
    --dangerously-bypass-approvals-and-sandbox \
    --cd "$workdir" \
    -o "$out_file" \
    "$prompt" >/dev/null 2>&1; then
    rm -f "$out_file"
    return 1
  fi

  cat "$out_file"
  rm -f "$out_file"
  return 0
}

normalize_line() {
  echo "$1" | tr -d '\r' | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//' | tr -d '`"'
}

normalize_path() {
  echo "$1" | sed -E 's#^(\./)+##; s#^(\.\./)+##'
}

echo "=== Test: Codex Governance Runtime ==="
echo "Entity: $(basename "$ENTITY_ROOT")"

if [ -z "$CODEx_BIN" ]; then
  skip "codex binary not found"
  echo ""
  echo "================================"
  printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
  printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
  printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
  echo "================================"
  exit 0
fi

TESTS=(
  "Principle single source of truth|Read AGENTS.md and .0agnostic. Return only the relative path to the principle document that states there should be one canonical source of truth.|.0agnostic/01_knowledge/principles/single_source_of_truth.md"
  "Principle lean static context|Read AGENTS.md and .0agnostic. Return only the relative path to the principle document about keeping static context lean.|.0agnostic/01_knowledge/principles/lean_static_context.md"
  "Knowledge static vs dynamic|Return only the relative path to the knowledge doc describing static vs dynamic context.|.0agnostic/01_knowledge/static_dynamic_context.md"
  "Static rule traversal|Return only the relative path to the static rule governing context traversal.|.0agnostic/02_rules/static/context_traversal.md"
  "Dynamic rule after agnostic edits|You edited files under .0agnostic and need regenerated outputs. Return only the relative path to the dynamic rule that applies.|.0agnostic/02_rules/dynamic/sync_after_agnostic_edit.md"
  "Protocol stage report|Return only the relative path to the protocol that defines stage report format and canonical/mirror locations.|.0agnostic/03_protocols/stage_report_protocol.md"
)

for t in "${TESTS[@]}"; do
  label="${t%%|*}"
  rest="${t#*|}"
  prompt="${rest%%|*}"
  expected="${rest#*|}"

  msg="$(run_codex_last_message "$ENTITY_ROOT" "$prompt" || true)"
  msg="$(normalize_line "$msg")"
  msg="$(normalize_path "$msg")"

  if [ "$msg" = "$expected" ]; then
    pass "$label"
  else
    fail "$label (expected: $expected, got: ${msg:-<empty>})"
  fi
done

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
