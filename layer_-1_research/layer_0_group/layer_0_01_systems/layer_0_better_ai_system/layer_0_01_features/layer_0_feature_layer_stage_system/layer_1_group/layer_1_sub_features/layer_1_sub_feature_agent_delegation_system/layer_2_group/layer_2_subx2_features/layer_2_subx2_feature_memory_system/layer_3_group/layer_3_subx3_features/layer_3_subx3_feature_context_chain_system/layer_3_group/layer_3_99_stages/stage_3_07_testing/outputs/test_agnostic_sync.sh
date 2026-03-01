#!/usr/bin/env bash
# test_agnostic_sync.sh — Test agnostic-sync.sh transforms 0AGNOSTIC.md correctly
#
# Tests that agnostic-sync.sh:
#   1. Produces all 4 tool files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
#   2. Extracts Identity section correctly
#   3. Includes Triggers section
#   4. Has auto-generated footer in CLAUDE.md
#   5. All tool files contain the Identity section
#   6. Re-syncing after modification updates outputs
#   7. Fails gracefully on directory without 0AGNOSTIC.md

set -uo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/.0agnostic/agnostic-sync.sh"

# --- Counters ---
PASS=0
FAIL=0
SKIP=0

pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: agnostic-sync.sh ==="
echo "Entity: $(basename "$ENTITY_ROOT")"
echo "Sync script: $SYNC_SCRIPT"
echo ""

# --- Pre-check: sync script exists ---
if [ ! -f "$SYNC_SCRIPT" ]; then
    fail "agnostic-sync.sh not found at $SYNC_SCRIPT"
    echo ""
    echo "Cannot continue — sync script missing."
    exit 1
fi

if [ ! -x "$SYNC_SCRIPT" ]; then
    fail "agnostic-sync.sh is not executable"
    echo ""
    echo "Cannot continue — sync script not executable."
    exit 1
fi

pass "agnostic-sync.sh exists and is executable"

# --- Pre-check: 0AGNOSTIC.md exists at entity ---
if [ ! -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    fail "0AGNOSTIC.md not found at entity root"
    echo ""
    echo "Cannot continue — no source file."
    exit 1
fi

pass "0AGNOSTIC.md exists at entity root"

# --- Test 1: Run sync and check all 4 files produced ---
echo ""
echo "--- Test 1: Sync produces all 4 tool files ---"

# Back up existing tool files
BACKUP_DIR=$(mktemp -d)
for f in CLAUDE.md AGENTS.md GEMINI.md OPENAI.md; do
    [ -f "$ENTITY_ROOT/$f" ] && cp "$ENTITY_ROOT/$f" "$BACKUP_DIR/$f"
done

# Run sync
SYNC_OUTPUT=$("$SYNC_SCRIPT" "$ENTITY_ROOT" 2>&1)
SYNC_EXIT=$?

if [ $SYNC_EXIT -eq 0 ]; then
    pass "agnostic-sync.sh exited with code 0"
else
    fail "agnostic-sync.sh exited with code $SYNC_EXIT"
fi

for f in CLAUDE.md AGENTS.md GEMINI.md OPENAI.md; do
    if [ -f "$ENTITY_ROOT/$f" ]; then
        pass "$f generated"
    else
        fail "$f NOT generated"
    fi
done

# --- Test 2: CLAUDE.md contains Identity section ---
echo ""
echo "--- Test 2: CLAUDE.md contains Identity section ---"

if [ -f "$ENTITY_ROOT/CLAUDE.md" ]; then
    if grep -q "## Identity" "$ENTITY_ROOT/CLAUDE.md"; then
        pass "CLAUDE.md contains ## Identity"
    else
        fail "CLAUDE.md missing ## Identity"
    fi

    # Check Identity content is meaningful (not just the header)
    identity_lines=$(sed -n '/^## Identity/,/^## [^#]/p' "$ENTITY_ROOT/CLAUDE.md" | wc -l)
    if [ "$identity_lines" -gt 2 ]; then
        pass "Identity section has content ($identity_lines lines)"
    else
        fail "Identity section is empty or header-only ($identity_lines lines)"
    fi
else
    skip "CLAUDE.md does not exist (cannot check Identity)"
fi

# --- Test 3: CLAUDE.md contains Triggers section ---
echo ""
echo "--- Test 3: CLAUDE.md contains Triggers section ---"

if [ -f "$ENTITY_ROOT/CLAUDE.md" ]; then
    if grep -q "## Triggers" "$ENTITY_ROOT/CLAUDE.md"; then
        pass "CLAUDE.md contains ## Triggers"
    else
        # Triggers is optional in agnostic-sync.sh, so check 0AGNOSTIC.md
        if grep -q "## Triggers" "$ENTITY_ROOT/0AGNOSTIC.md"; then
            fail "0AGNOSTIC.md has Triggers but CLAUDE.md doesn't — sync error"
        else
            skip "No Triggers section in source (optional)"
        fi
    fi
else
    skip "CLAUDE.md does not exist"
fi

# --- Test 4: CLAUDE.md has auto-generated footer ---
echo ""
echo "--- Test 4: CLAUDE.md has auto-generated footer ---"

if [ -f "$ENTITY_ROOT/CLAUDE.md" ]; then
    if grep -q "Auto-generated from 0AGNOSTIC.md" "$ENTITY_ROOT/CLAUDE.md"; then
        pass "CLAUDE.md has auto-generated footer"
    else
        fail "CLAUDE.md missing auto-generated footer"
    fi

    if grep -q "agnostic-sync.sh" "$ENTITY_ROOT/CLAUDE.md"; then
        pass "CLAUDE.md references agnostic-sync.sh"
    else
        fail "CLAUDE.md doesn't reference agnostic-sync.sh"
    fi
else
    skip "CLAUDE.md does not exist"
fi

# --- Test 5: All tool files contain Identity section ---
echo ""
echo "--- Test 5: All tool files contain Identity section ---"

for f in AGENTS.md GEMINI.md OPENAI.md; do
    if [ -f "$ENTITY_ROOT/$f" ]; then
        if grep -q "## Identity" "$ENTITY_ROOT/$f"; then
            pass "$f contains ## Identity"
        else
            fail "$f missing ## Identity"
        fi

        if grep -q "Auto-generated from 0AGNOSTIC.md" "$ENTITY_ROOT/$f"; then
            pass "$f has auto-generated footer"
        else
            fail "$f missing auto-generated footer"
        fi
    else
        fail "$f does not exist"
    fi
done

# --- Test 6: Re-sync after modification updates output ---
echo ""
echo "--- Test 6: Re-sync reflects modifications ---"

# Save original 0AGNOSTIC.md
cp "$ENTITY_ROOT/0AGNOSTIC.md" "$BACKUP_DIR/0AGNOSTIC.md.orig"

# Add a unique marker to 0AGNOSTIC.md (in Identity section)
MARKER="TEST_SYNC_MARKER_$(date +%s)"
sed -i "/^## Identity/a - **Test Marker**: $MARKER" "$ENTITY_ROOT/0AGNOSTIC.md"

# Re-run sync
"$SYNC_SCRIPT" "$ENTITY_ROOT" > /dev/null 2>&1

# Check marker appears in generated files
if grep -q "$MARKER" "$ENTITY_ROOT/CLAUDE.md" 2>/dev/null; then
    pass "CLAUDE.md updated with new content after re-sync"
else
    fail "CLAUDE.md did NOT update after re-sync"
fi

if grep -q "$MARKER" "$ENTITY_ROOT/AGENTS.md" 2>/dev/null; then
    pass "AGENTS.md updated with new content after re-sync"
else
    fail "AGENTS.md did NOT update after re-sync"
fi

# Restore original 0AGNOSTIC.md and re-sync to clean state
cp "$BACKUP_DIR/0AGNOSTIC.md.orig" "$ENTITY_ROOT/0AGNOSTIC.md"
"$SYNC_SCRIPT" "$ENTITY_ROOT" > /dev/null 2>&1

# --- Test 7: Graceful failure on missing 0AGNOSTIC.md ---
echo ""
echo "--- Test 7: Graceful failure on missing 0AGNOSTIC.md ---"

EMPTY_DIR=$(mktemp -d)
FAIL_OUTPUT=$("$SYNC_SCRIPT" "$EMPTY_DIR" 2>&1)
FAIL_EXIT=$?

if [ $FAIL_EXIT -ne 0 ]; then
    pass "Sync fails with non-zero exit on missing 0AGNOSTIC.md (exit=$FAIL_EXIT)"
else
    fail "Sync should fail on missing 0AGNOSTIC.md but exited 0"
fi

if echo "$FAIL_OUTPUT" | grep -qi "error\|not found"; then
    pass "Error message mentions missing file"
else
    fail "No meaningful error message on missing 0AGNOSTIC.md"
fi

rmdir "$EMPTY_DIR" 2>/dev/null

# --- Cleanup ---
rm -rf "$BACKUP_DIR"

# --- Summary ---
echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
