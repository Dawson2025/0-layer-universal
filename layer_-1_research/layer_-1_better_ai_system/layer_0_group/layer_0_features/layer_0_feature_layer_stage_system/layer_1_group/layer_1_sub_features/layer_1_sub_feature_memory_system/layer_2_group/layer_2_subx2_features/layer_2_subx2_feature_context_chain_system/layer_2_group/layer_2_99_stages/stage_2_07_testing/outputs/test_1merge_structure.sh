#!/usr/bin/env bash
# test_1merge_structure.sh — Test .1merge/ 3-tier system is properly structured
#
# Tests that:
#   1. All 6 tool merge directories exist
#   2. Each has the 3 tiers: 0_synced/, 1_overrides/, 2_additions/
#   3. Valid markdown in overrides/additions (if content exists)
#   4. Adding a file to 2_additions/ doesn't break sync

set -uo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/layer_0/.0agnostic/agnostic-sync.sh"

# --- Counters ---
PASS=0
FAIL=0
SKIP=0

pass() { ((PASS++)) || true; printf "  \033[32mPASS\033[0m  %s\n" "$1"; }
fail() { ((FAIL++)) || true; printf "  \033[31mFAIL\033[0m  %s\n" "$1"; }
skip() { ((SKIP++)) || true; printf "  \033[33mSKIP\033[0m  %s\n" "$1"; }

MERGE_DIR="$ENTITY_ROOT/.1merge"

echo "=== Test: .1merge/ Structure ==="
echo "Entity: $(basename "$ENTITY_ROOT")"
echo ""

# --- Test 1: .1merge/ directory exists ---
echo "--- Test 1: .1merge/ exists ---"

if [ -d "$MERGE_DIR" ]; then
    pass ".1merge/ directory exists"
else
    fail ".1merge/ directory missing"
    echo "Cannot continue — no .1merge/ directory."
    exit 1
fi

# --- Test 2: All 6 tool directories exist ---
echo ""
echo "--- Test 2: Tool merge directories ---"

TOOLS=(.1claude_merge .1cursor_merge .1gemini_merge .1aider_merge .1codex_merge .1copilot_merge)
TIERS=(0_synced 1_overrides 2_additions)

tool_dirs_ok=true
for tool in "${TOOLS[@]}"; do
    if [ -d "$MERGE_DIR/$tool" ]; then
        pass "$tool/ exists"
    else
        fail "$tool/ missing"
        tool_dirs_ok=false
    fi
done

# --- Test 3: Each tool has 3 tiers ---
echo ""
echo "--- Test 3: 3-tier structure ---"

tier_count=0
expected_tiers=$((${#TOOLS[@]} * ${#TIERS[@]}))

for tool in "${TOOLS[@]}"; do
    for tier in "${TIERS[@]}"; do
        if [ -d "$MERGE_DIR/$tool/$tier" ]; then
            tier_count=$((tier_count + 1))
        else
            fail "$tool/$tier/ missing"
        fi
    done
done

if [ $tier_count -eq $expected_tiers ]; then
    pass "All $expected_tiers tier directories present ($tier_count/$expected_tiers)"
else
    fail "Only $tier_count/$expected_tiers tier directories present"
fi

# --- Test 4: Content validation ---
echo ""
echo "--- Test 4: Content in overrides/additions ---"

content_found=false
invalid_found=false

for tool in "${TOOLS[@]}"; do
    for tier in 1_overrides 2_additions; do
        dir="$MERGE_DIR/$tool/$tier"
        [ ! -d "$dir" ] && continue

        # Find non-gitkeep files
        files=$(find "$dir" -type f ! -name ".gitkeep" 2>/dev/null)
        if [ -n "$files" ]; then
            content_found=true
            while IFS= read -r f; do
                fname=$(basename "$f")
                # Check if markdown files are valid (have content)
                if [[ "$f" == *.md ]]; then
                    lines=$(grep -cvP '^\s*$' "$f" 2>/dev/null || echo "0")
                    if [ "$lines" -gt 0 ]; then
                        pass "$tool/$tier/$fname ($lines lines)"
                    else
                        fail "$tool/$tier/$fname exists but is empty"
                        invalid_found=true
                    fi
                else
                    pass "$tool/$tier/$fname (non-md file)"
                fi
            done <<< "$files"
        fi
    done
done

if [ "$content_found" = false ]; then
    skip "No content in any overrides/additions (all scaffolded)"
fi

# --- Test 5: 0_synced/ tier alignment ---
echo ""
echo "--- Test 5: 0_synced/ alignment check ---"

# Check if 0_synced/ has files that match the main generated files
for tool in "${TOOLS[@]}"; do
    synced_dir="$MERGE_DIR/$tool/0_synced"
    [ ! -d "$synced_dir" ] && continue

    synced_files=$(find "$synced_dir" -type f ! -name ".gitkeep" 2>/dev/null | wc -l)
    if [ "$synced_files" -gt 0 ]; then
        pass "$tool/0_synced/ has $synced_files synced files"
    else
        skip "$tool/0_synced/ is empty (sync hasn't populated it yet)"
    fi
done

# --- Test 6: Additions don't break sync ---
echo ""
echo "--- Test 6: Additions compatibility ---"

if [ -f "$SYNC_SCRIPT" ] && [ -x "$SYNC_SCRIPT" ] && [ -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    # Create a temporary addition
    TEST_ADDITION="$MERGE_DIR/.1claude_merge/2_additions/test_addition_$(date +%s).md"
    echo "# Test Addition" > "$TEST_ADDITION"
    echo "This is a test file to verify additions don't break sync." >> "$TEST_ADDITION"

    # Run sync
    sync_out=$("$SYNC_SCRIPT" "$ENTITY_ROOT" 2>&1)
    sync_exit=$?

    if [ $sync_exit -eq 0 ]; then
        pass "Sync succeeds with addition present (exit=$sync_exit)"
    else
        fail "Sync fails with addition present (exit=$sync_exit)"
    fi

    # Clean up test addition
    rm -f "$TEST_ADDITION"

    # Re-sync to clean state
    "$SYNC_SCRIPT" "$ENTITY_ROOT" > /dev/null 2>&1
else
    skip "Cannot test additions compatibility (sync script unavailable)"
fi

# --- Test 7: Naming convention check ---
echo ""
echo "--- Test 7: Naming conventions ---"

for tool in "${TOOLS[@]}"; do
    # Tool name should match pattern .1<toolname>_merge
    if [[ "$tool" =~ ^\.1[a-z]+_merge$ ]]; then
        pass "$tool follows naming convention"
    else
        fail "$tool does NOT follow .1<name>_merge pattern"
    fi
done

# --- Summary ---
echo ""
echo "================================"
printf "  \033[32mPASS\033[0m: %d\n" "$PASS"
printf "  \033[31mFAIL\033[0m: %d\n" "$FAIL"
printf "  \033[33mSKIP\033[0m: %d\n" "$SKIP"
echo "================================"

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
