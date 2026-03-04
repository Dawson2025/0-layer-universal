#!/usr/bin/env bash
# test_context_chain_traversal.sh — Test parent reference chain resolves to root
#
# Tests that:
#   1. 0AGNOSTIC.md exists at this entity
#   2. Parent reference resolves correctly
#   3. Grandparent and further ancestors resolve
#   4. CLAUDE.md files exist at each level in the chain
#   5. Each CLAUDE.md has auto-generated footer (proving sync ran)
#   6. No broken parent references

set -uo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"

# --- Counters ---
PASS=0
FAIL=0
SKIP=0

pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

echo "=== Test: Context Chain Traversal ==="
echo "Entity: $(basename "$ENTITY_ROOT")"
echo ""

# --- Test 1: 0AGNOSTIC.md exists at this entity ---
echo "--- Test 1: Source file exists ---"

if [ -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    pass "0AGNOSTIC.md exists at entity root"
else
    fail "0AGNOSTIC.md missing at entity root"
    echo "Cannot continue — no source file to trace."
    exit 1
fi

# --- Test 2: Extract and resolve parent reference ---
echo ""
echo "--- Test 2: Parent reference resolves ---"

# Extract parent path from 0AGNOSTIC.md
PARENT_REF=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$ENTITY_ROOT/0AGNOSTIC.md" | head -1)

if [ -z "$PARENT_REF" ]; then
    fail "No **Parent** reference found in 0AGNOSTIC.md"
    echo "Cannot trace chain without parent reference."
    exit 1
fi

pass "Parent reference found: $PARENT_REF"

# Resolve relative to entity root
PARENT_PATH="$(cd "$ENTITY_ROOT" && cd "$(dirname "$PARENT_REF")" 2>/dev/null && pwd)/$(basename "$PARENT_REF")"

if [ -f "$PARENT_PATH" ]; then
    pass "Parent resolves to: $PARENT_PATH"
    PARENT_DIR="$(dirname "$PARENT_PATH")"
    PARENT_NAME="$(basename "$PARENT_DIR")"
    pass "Parent entity: $PARENT_NAME"
else
    fail "Parent reference does NOT resolve: $PARENT_REF"
    PARENT_DIR=""
fi

# --- Test 3: Trace full chain to root ---
echo ""
echo "--- Test 3: Full chain traversal ---"

CHAIN_DEPTH=0
MAX_DEPTH=20
CURRENT_DIR="$ENTITY_ROOT"
CHAIN_BROKEN=false

# Collect chain for display
declare -a CHAIN_ENTITIES=()
CHAIN_ENTITIES+=("$(basename "$CURRENT_DIR")")

while [ $CHAIN_DEPTH -lt $MAX_DEPTH ]; do
    # Check if current has 0AGNOSTIC.md
    if [ ! -f "$CURRENT_DIR/0AGNOSTIC.md" ]; then
        break
    fi

    # Extract parent reference
    PREF=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$CURRENT_DIR/0AGNOSTIC.md" | head -1)

    if [ -z "$PREF" ]; then
        # No parent — might be root level
        break
    fi

    # Resolve parent
    RESOLVED="$(cd "$CURRENT_DIR" && cd "$(dirname "$PREF")" 2>/dev/null && pwd)/$(basename "$PREF")"

    if [ ! -f "$RESOLVED" ]; then
        fail "Broken parent reference at depth $CHAIN_DEPTH: $PREF (from $(basename "$CURRENT_DIR"))"
        CHAIN_BROKEN=true
        break
    fi

    CURRENT_DIR="$(dirname "$RESOLVED")"
    CHAIN_DEPTH=$((CHAIN_DEPTH + 1))
    CHAIN_ENTITIES+=("$(basename "$CURRENT_DIR")")
done

if [ "$CHAIN_BROKEN" = false ]; then
    pass "Chain traversal complete — no broken references"
fi

pass "Chain depth: $CHAIN_DEPTH levels above entity"

echo ""
echo "  Chain (bottom → top):"
for ((i=0; i<${#CHAIN_ENTITIES[@]}; i++)); do
    indent=""
    for ((j=0; j<i; j++)); do indent="  $indent"; done
    echo "    ${indent}└── ${CHAIN_ENTITIES[$i]}"
done

# --- Test 4: CLAUDE.md files exist at each level ---
echo ""
echo "--- Test 4: CLAUDE.md at each chain level ---"

CURRENT_DIR="$ENTITY_ROOT"
LEVEL=0
CLAUDE_COUNT=0

# Check entity root
if [ -f "$CURRENT_DIR/CLAUDE.md" ]; then
    pass "CLAUDE.md at entity root (level 0)"
    CLAUDE_COUNT=$((CLAUDE_COUNT + 1))
else
    fail "CLAUDE.md missing at entity root (level 0)"
fi

# Traverse up through the filesystem checking for CLAUDE.md at each entity
CURRENT_DIR="$ENTITY_ROOT"
for ((i=1; i<${#CHAIN_ENTITIES[@]}; i++)); do
    # Extract parent and move up
    PREF=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$CURRENT_DIR/0AGNOSTIC.md" 2>/dev/null | head -1)
    [ -z "$PREF" ] && break
    RESOLVED="$(cd "$CURRENT_DIR" && cd "$(dirname "$PREF")" 2>/dev/null && pwd)/$(basename "$PREF")"
    [ ! -f "$RESOLVED" ] && break
    CURRENT_DIR="$(dirname "$RESOLVED")"

    if [ -f "$CURRENT_DIR/CLAUDE.md" ]; then
        pass "CLAUDE.md at ${CHAIN_ENTITIES[$i]} (level $i)"
        CLAUDE_COUNT=$((CLAUDE_COUNT + 1))
    else
        fail "CLAUDE.md missing at ${CHAIN_ENTITIES[$i]} (level $i)"
    fi
done

pass "Total CLAUDE.md files in chain: $CLAUDE_COUNT"

# --- Test 5: Each CLAUDE.md has auto-generated footer ---
echo ""
echo "--- Test 5: Auto-generated footers ---"

CURRENT_DIR="$ENTITY_ROOT"
for ((i=0; i<${#CHAIN_ENTITIES[@]}; i++)); do
    if [ -f "$CURRENT_DIR/CLAUDE.md" ]; then
        if grep -q "Auto-generated from 0AGNOSTIC.md" "$CURRENT_DIR/CLAUDE.md"; then
            pass "${CHAIN_ENTITIES[$i]}/CLAUDE.md has sync footer"
        else
            fail "${CHAIN_ENTITIES[$i]}/CLAUDE.md missing sync footer — may be hand-crafted"
        fi
    fi

    # Move to next parent
    PREF=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$CURRENT_DIR/0AGNOSTIC.md" 2>/dev/null | head -1)
    [ -z "$PREF" ] && break
    RESOLVED="$(cd "$CURRENT_DIR" && cd "$(dirname "$PREF")" 2>/dev/null && pwd)/$(basename "$PREF")"
    [ ! -f "$RESOLVED" ] && break
    CURRENT_DIR="$(dirname "$RESOLVED")"
done

# --- Test 6: Count total 0AGNOSTIC.md in filesystem path ---
echo ""
echo "--- Test 6: 0AGNOSTIC.md density in filesystem path ---"

# Count all 0AGNOSTIC.md between entity and repo root
AGNOSTIC_COUNT=0
CHECK_DIR="$ENTITY_ROOT"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"

while [ "${#CHECK_DIR}" -ge "${#REPO_ROOT}" ]; do
    if [ -f "$CHECK_DIR/0AGNOSTIC.md" ]; then
        AGNOSTIC_COUNT=$((AGNOSTIC_COUNT + 1))
    fi
    CHECK_DIR="$(dirname "$CHECK_DIR")"
done

pass "Total 0AGNOSTIC.md in filesystem path to root: $AGNOSTIC_COUNT"

if [ $AGNOSTIC_COUNT -ge 3 ]; then
    pass "Sufficient chain density (>= 3 files)"
else
    fail "Low chain density ($AGNOSTIC_COUNT files — expected >= 3)"
fi

# --- Summary ---
echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
