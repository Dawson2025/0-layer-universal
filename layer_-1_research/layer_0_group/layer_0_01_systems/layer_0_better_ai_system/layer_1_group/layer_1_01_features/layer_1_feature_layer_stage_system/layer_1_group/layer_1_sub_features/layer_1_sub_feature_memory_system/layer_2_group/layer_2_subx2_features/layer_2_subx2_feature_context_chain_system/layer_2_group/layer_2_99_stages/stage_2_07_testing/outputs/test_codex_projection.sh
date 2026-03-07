#!/usr/bin/env bash
# resource_id: "44879445-c762-4582-a8d2-9abb74db6ef1"
# resource_type: "script"
# resource_name: "test_codex_projection"
# test_codex_projection.sh — Validate Codex-specific projection into AGENTS.md

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh"

CODEX_MERGE="$ENTITY_ROOT/.1merge/.1codex_merge"
OVERRIDE_FILE="$CODEX_MERGE/1_overrides/tool_boilerplate.md"
ADDITIONS_FILE="$CODEX_MERGE/2_additions/tool_additions.md"
AGENTS_FILE="$ENTITY_ROOT/AGENTS.md"
CLAUDE_FILE="$ENTITY_ROOT/CLAUDE.md"

PASS=0
FAIL=0
SKIP=0
pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Codex Projection to AGENTS.md ==="
echo "Entity: $(basename "$ENTITY_ROOT")"

if [ ! -x "$SYNC_SCRIPT" ]; then
    fail "agnostic-sync.sh missing or not executable"
    exit 1
fi

if [ -s "$OVERRIDE_FILE" ]; then
    pass "Codex override file exists and is non-empty"
else
    fail "Codex override file missing or empty"
fi

if [ -s "$ADDITIONS_FILE" ]; then
    pass "Codex additions file exists and is non-empty"
else
    fail "Codex additions file missing or empty"
fi

if "$SYNC_SCRIPT" "$ENTITY_ROOT" >/dev/null 2>&1; then
    pass "Sync succeeds"
else
    fail "Sync failed"
fi

if grep -q "## Codex CLI Configuration" "$AGENTS_FILE"; then
    pass "AGENTS.md includes Codex override section"
else
    fail "AGENTS.md missing Codex override section"
fi

if grep -q "## Codex Discovery Triggers" "$AGENTS_FILE"; then
    pass "AGENTS.md includes Codex additions section"
else
    fail "AGENTS.md missing Codex additions section"
fi

if grep -q "## Codex CLI Configuration" "$CLAUDE_FILE"; then
    fail "CLAUDE.md should not contain Codex override section"
else
    pass "CLAUDE.md does not contain Codex override section"
fi

if grep -q "Codex Merge Diagnostics" "$CLAUDE_FILE"; then
    fail "CLAUDE.md should not contain Codex additions"
else
    pass "CLAUDE.md does not contain Codex additions"
fi

# Isolation marker test: marker should project to AGENTS but not CLAUDE.
MARKER="CODEX_PROJECTION_MARKER_$(date +%s)"
BACKUP="$(mktemp)"
cp "$ADDITIONS_FILE" "$BACKUP"
restore() {
    cp "$BACKUP" "$ADDITIONS_FILE"
    "$SYNC_SCRIPT" "$ENTITY_ROOT" >/dev/null 2>&1 || true
    rm -f "$BACKUP"
}
trap restore EXIT

echo "" >> "$ADDITIONS_FILE"
echo "- $MARKER" >> "$ADDITIONS_FILE"

if "$SYNC_SCRIPT" "$ENTITY_ROOT" >/dev/null 2>&1; then
    pass "Re-sync with marker succeeds"
else
    fail "Re-sync with marker failed"
fi

if grep -q "$MARKER" "$AGENTS_FILE"; then
    pass "Marker appears in AGENTS.md"
else
    fail "Marker missing from AGENTS.md"
fi

if grep -q "$MARKER" "$CLAUDE_FILE"; then
    fail "Marker leaked into CLAUDE.md"
else
    pass "Marker does not leak into CLAUDE.md"
fi

echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
