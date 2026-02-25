#!/usr/bin/env bash
# test_codex_runtime_behavior.sh — Runtime validation using Codex in dangerous bypass mode

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
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

echo "=== Test: Codex Runtime Behavior ==="
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

# Check 1: Codex can execute projection test in dangerous mode.
msg="$(run_codex_last_message "$SCRIPT_DIR" "Run ./test_codex_projection.sh and return exactly PASS or FAIL" || true)"
msg="$(normalize_line "$msg")"
if [ "$msg" = "PASS" ]; then
  pass "Codex runtime execution: projection test"
else
  fail "Codex runtime execution failed for projection test (got: ${msg:-<empty>})"
fi

# Check 2: Codex can execute condition mapping test in dangerous mode.
msg="$(run_codex_last_message "$SCRIPT_DIR" "Run ./test_codex_context_conditions.sh and return exactly PASS or FAIL" || true)"
msg="$(normalize_line "$msg")"
if [ "$msg" = "PASS" ]; then
  pass "Codex runtime execution: context conditions test"
else
  fail "Codex runtime execution failed for context conditions test (got: ${msg:-<empty>})"
fi

# Check 3: Codex discovers knowledge-contract path from AGENTS.
msg="$(run_codex_last_message "$ENTITY_ROOT" "Read AGENTS.md and return exactly the referenced path for codex_cli_context_contract.md. Return only the path." || true)"
msg="$(normalize_line "$msg")"
if [ "$msg" = ".0agnostic/01_knowledge/codex_cli_context_contract.md" ]; then
  pass "Codex discovers codex contract path from AGENTS"
else
  fail "Codex contract-path discovery mismatch (got: ${msg:-<empty>})"
fi

# Check 4: Codex discovers skill path mapping from AGENTS.
msg="$(run_codex_last_message "$ENTITY_ROOT" "Read AGENTS.md and return exactly the referenced path for chain-validate skill. Return only the path." || true)"
msg="$(normalize_line "$msg")"
if [ "$msg" = ".0agnostic/05_skills/chain-validate/SKILL.md" ]; then
  pass "Codex discovers chain-validate mapping from AGENTS"
else
  fail "Codex chain-validate mapping mismatch (got: ${msg:-<empty>})"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
