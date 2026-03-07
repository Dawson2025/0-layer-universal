#!/usr/bin/env bash
# resource_id: "0f59cfab-961b-4976-886a-a1294868b4f5"
# resource_type: "script"
# resource_name: "test_codex_context_conditions"
# test_codex_context_conditions.sh — Validate Codex static context and conditional discovery mappings

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh"

AGENTS_FILE="$ENTITY_ROOT/AGENTS.md"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Codex Context Conditions ==="
echo "Entity: $(basename "$ENTITY_ROOT")"

if "$SYNC_SCRIPT" "$ENTITY_ROOT" >/dev/null 2>&1; then
    pass "Sync succeeds"
else
    fail "Sync failed"
fi

if [ -f "$AGENTS_FILE" ]; then
    pass "AGENTS.md exists"
else
    fail "AGENTS.md missing"
    exit 1
fi

# Static hot-context checks.
for section in "## Identity" "## Codex CLI Configuration" "## Codex Discovery Triggers"; do
    if grep -q "$section" "$AGENTS_FILE"; then
        pass "AGENTS.md contains $section"
    else
        fail "AGENTS.md missing $section"
    fi
done

# Rule ordering and conditional trigger framing.
if grep -q "When requests mention context-chain operations" "$AGENTS_FILE"; then
    pass "Conditional trigger framing exists"
else
    fail "Conditional trigger framing missing"
fi

if grep -q '.0agnostic/02_rules/static/' "$AGENTS_FILE" && grep -q '.0agnostic/02_rules/dynamic/' "$AGENTS_FILE"; then
    pass "Static + dynamic rules are both discoverable from AGENTS.md"
else
    fail "Rules discovery paths are incomplete in AGENTS.md"
fi

# Condition -> required context mapping assertions.
# Format: trigger_keyword|expected_reference_path
MAPS=(
  "context chain|.0agnostic/01_knowledge/codex_cli_context_contract.md"
  "agnostic-sync|.0agnostic/03_protocols/chain_validation_protocol.md"
  "chain-validate|.0agnostic/05_skills/chain-validate/SKILL.md"
  "avenue-check|.0agnostic/05_skills/avenue-check/SKILL.md"
)

for map in "${MAPS[@]}"; do
    trigger="${map%%|*}"
    ref="${map#*|}"

    if grep -qi "$trigger" "$AGENTS_FILE"; then
        pass "Trigger token present: $trigger"
    else
        fail "Trigger token missing: $trigger"
    fi

    if grep -q "$ref" "$AGENTS_FILE"; then
        pass "Mapped reference present in AGENTS.md: $ref"
    else
        fail "Mapped reference missing in AGENTS.md: $ref"
    fi

    if [ -f "$ENTITY_ROOT/$ref" ]; then
        pass "Mapped file exists: $ref"
    else
        fail "Mapped file does not exist: $ref"
    fi
done

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
