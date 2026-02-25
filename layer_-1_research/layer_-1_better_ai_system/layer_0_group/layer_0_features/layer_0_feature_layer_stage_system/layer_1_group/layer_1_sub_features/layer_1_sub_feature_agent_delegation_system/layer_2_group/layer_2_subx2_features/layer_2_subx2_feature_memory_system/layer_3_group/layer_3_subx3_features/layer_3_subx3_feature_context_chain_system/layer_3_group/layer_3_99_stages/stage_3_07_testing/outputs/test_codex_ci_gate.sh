#!/usr/bin/env bash
# test_codex_ci_gate.sh — CI-style gate for Codex projection quality

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"

PASS=0
FAIL=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }

echo "=== Test: Codex CI Gate ==="
echo "Entity: $(basename "$ENTITY_ROOT")"

non_gitkeep_count=$(find "$ENTITY_ROOT/.1merge/.1codex_merge" -type f ! -name '.gitkeep' | wc -l | tr -d ' ')
if [ "$non_gitkeep_count" -ge 2 ]; then
    pass ".1codex_merge has non-scaffold content ($non_gitkeep_count files)"
else
    fail ".1codex_merge must contain real files (found $non_gitkeep_count)"
fi

if "$SCRIPT_DIR/test_codex_projection.sh" >/tmp/test_codex_projection.log 2>&1; then
    pass "test_codex_projection.sh passed"
else
    fail "test_codex_projection.sh failed"
    sed -n '1,120p' /tmp/test_codex_projection.log
fi

if "$SCRIPT_DIR/test_codex_discovery_chain.sh" >/tmp/test_codex_discovery.log 2>&1; then
    pass "test_codex_discovery_chain.sh passed"
else
    fail "test_codex_discovery_chain.sh failed"
    sed -n '1,120p' /tmp/test_codex_discovery.log
fi

if "$SCRIPT_DIR/test_codex_context_conditions.sh" >/tmp/test_codex_conditions.log 2>&1; then
    pass "test_codex_context_conditions.sh passed"
else
    fail "test_codex_context_conditions.sh failed"
    sed -n '1,120p' /tmp/test_codex_conditions.log
fi

if "$SCRIPT_DIR/test_codex_runtime_behavior.sh" >/tmp/test_codex_runtime.log 2>&1; then
    pass "test_codex_runtime_behavior.sh passed"
else
    fail "test_codex_runtime_behavior.sh failed"
    sed -n '1,160p' /tmp/test_codex_runtime.log
fi

rm -f /tmp/test_codex_projection.log /tmp/test_codex_discovery.log /tmp/test_codex_conditions.log /tmp/test_codex_runtime.log

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
