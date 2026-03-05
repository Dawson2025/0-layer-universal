#!/usr/bin/env bash
# resource_id: "52987c55-7b25-4f0b-9a99-3a0f8614ecef"
# resource_type: "script"
# resource_name: "test_codex_discovery_chain"
# test_codex_discovery_chain.sh — Validate Codex discovery chain checkpoints

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/.0agnostic/agnostic-sync.sh"

AGENTS_FILE="$ENTITY_ROOT/AGENTS.md"
CONTRACT_FILE="$ENTITY_ROOT/.0agnostic/01_knowledge/codex_cli_context_contract.md"
CODEX_DIR="$ENTITY_ROOT/.codex"
CODEX_MERGE="$ENTITY_ROOT/.1merge/.1codex_merge"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Codex Discovery Chain ==="
echo "Entity: $(basename "$ENTITY_ROOT")"

if "$SYNC_SCRIPT" "$ENTITY_ROOT" >/dev/null 2>&1; then
    pass "Sync succeeds"
else
    fail "Sync failed"
fi

if [ -d "$CODEX_DIR" ]; then
    pass ".codex/ directory exists"
else
    fail ".codex/ directory missing"
fi

non_gitkeep_count=$(find "$CODEX_MERGE" -type f ! -name '.gitkeep' | wc -l | tr -d ' ')
if [ "$non_gitkeep_count" -ge 2 ]; then
    pass ".1codex_merge has non-scaffold content ($non_gitkeep_count files)"
else
    fail ".1codex_merge is still scaffold-only"
fi

if [ -s "$CONTRACT_FILE" ]; then
    pass "Codex contract file exists"
else
    fail "Codex contract file missing"
fi

for section in "## Discovery Temperatures" "### Hot context" "### Warm context" "### Cold context" "## Trigger Contract" "## Validation Contract"; do
    if grep -q "$section" "$CONTRACT_FILE"; then
        pass "Contract contains: $section"
    else
        fail "Contract missing section: $section"
    fi
done

if grep -q "## Codex Discovery Triggers" "$AGENTS_FILE"; then
    pass "AGENTS.md has Codex trigger section"
else
    fail "AGENTS.md missing Codex trigger section"
fi

# Checkpoints for a simple prompt-to-context path simulation.
checkpoint_hits=0
for token in "context chain" "agnostic-sync" "chain-validate" "avenue-check"; do
    if grep -qi "$token" "$AGENTS_FILE"; then
        checkpoint_hits=$((checkpoint_hits + 1))
    fi
done

if [ "$checkpoint_hits" -ge 3 ]; then
    pass "Discovery prompt simulation hits >=3 trigger tokens ($checkpoint_hits/4)"
else
    fail "Discovery prompt simulation too weak ($checkpoint_hits/4 trigger tokens)"
fi

if grep -q "Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh" "$AGENTS_FILE"; then
    pass "AGENTS.md has sync footer"
else
    fail "AGENTS.md missing sync footer"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
