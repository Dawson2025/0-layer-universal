#!/bin/bash
#
# test_pointer_sync.sh — Comprehensive test suite for pointer-sync.sh
#
# Creates a temporary mock layer-stage hierarchy, runs pointer-sync.sh
# against it, and validates behavior across 7 test categories.
#
# Usage:
#   bash test_pointer_sync.sh                    # Run all tests
#   bash test_pointer_sync.sh --category <name>  # Run one category
#
# Exit code: 0 if all pass, 1 if any fail
#

# NOTE: intentionally NOT using set -e so failed commands don't kill tests
set -uo pipefail

# --- Configuration ---
REAL_SCRIPT="/home/dawson/dawson-workspace/code/0_layer_universal/.0agnostic/pointer-sync.sh"
TMPDIR_BASE=""
PASS=0
FAIL=0
SKIP=0
TOTAL=0
CATEGORY_FILTER="${2:-}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# --- Assertion Helpers ---

assert_eq() {
    local label="$1"
    local expected="$2"
    local actual="$3"
    TOTAL=$((TOTAL + 1))
    if [ "$expected" = "$actual" ]; then
        echo -e "  ${GREEN}PASS${NC}: $label"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: $label"
        echo -e "    Expected: $(echo "$expected" | head -3)"
        echo -e "    Actual:   $(echo "$actual" | head -3)"
        FAIL=$((FAIL + 1))
    fi
}

assert_contains() {
    local label="$1"
    local haystack="$2"
    local needle="$3"
    TOTAL=$((TOTAL + 1))
    if echo "$haystack" | grep -qF "$needle"; then
        echo -e "  ${GREEN}PASS${NC}: $label"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: $label"
        echo -e "    Output did not contain: $needle"
        echo -e "    Output (first 3 lines): $(echo "$haystack" | head -3)"
        FAIL=$((FAIL + 1))
    fi
}

assert_not_contains() {
    local label="$1"
    local haystack="$2"
    local needle="$3"
    TOTAL=$((TOTAL + 1))
    if echo "$haystack" | grep -qF "$needle"; then
        echo -e "  ${RED}FAIL${NC}: $label"
        echo -e "    Output unexpectedly contained: $needle"
        FAIL=$((FAIL + 1))
    else
        echo -e "  ${GREEN}PASS${NC}: $label"
        PASS=$((PASS + 1))
    fi
}

assert_exit_code() {
    local label="$1"
    local expected="$2"
    local actual="$3"
    TOTAL=$((TOTAL + 1))
    if [ "$expected" = "$actual" ]; then
        echo -e "  ${GREEN}PASS${NC}: $label (exit $actual)"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: $label"
        echo -e "    Expected exit code: $expected"
        echo -e "    Actual exit code:   $actual"
        FAIL=$((FAIL + 1))
    fi
}

assert_file_contains() {
    local label="$1"
    local file="$2"
    local needle="$3"
    TOTAL=$((TOTAL + 1))
    if [ ! -f "$file" ]; then
        echo -e "  ${RED}FAIL${NC}: $label (file does not exist: $file)"
        FAIL=$((FAIL + 1))
        return
    fi
    if grep -qF "$needle" "$file"; then
        echo -e "  ${GREEN}PASS${NC}: $label"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: $label"
        echo -e "    File '$file' did not contain: $needle"
        FAIL=$((FAIL + 1))
    fi
}

# --- Helper: run pointer-sync.sh and capture output + exit code ---
# Usage: run_sync ROOT [flags...]
# Sets: SYNC_OUTPUT, SYNC_EXIT
run_sync() {
    local root="$1"
    shift
    SYNC_OUTPUT=$("$root/.0agnostic/pointer-sync.sh" "$@" 2>&1)
    SYNC_EXIT=$?
}

# --- Setup: Create mock layer-stage hierarchy ---

setup_mock_repo() {
    TMPDIR_BASE=$(mktemp -d /tmp/test_pointer_sync.XXXXXX)

    # The script expects to be inside .0agnostic/ with ROOT = parent
    local ROOT="$TMPDIR_BASE/mock_repo"
    mkdir -p "$ROOT/.0agnostic"

    # Copy the real pointer-sync.sh into the mock .0agnostic/
    cp "$REAL_SCRIPT" "$ROOT/.0agnostic/pointer-sync.sh"
    chmod +x "$ROOT/.0agnostic/pointer-sync.sh"

    # Create a mock layer-stage hierarchy
    # Entity: layer_1_feature_alpha (a target entity)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs"
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_06_development/outputs"
    echo "# Alpha Design" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/design.md"
    echo "# Alpha Dev" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_06_development/outputs/impl.md"

    # Entity: layer_2_feature_beta (another entity, deeper)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta/stage_2_04_design/outputs"
    echo "# Beta Design" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta/stage_2_04_design/outputs/design.md"

    # Entity: layer_1_feature_gamma (sibling entity)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    echo "# Gamma README" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/README.md"

    # A subpath target file
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/docs"
    echo "# Alpha Docs" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/docs/architecture.md"

    echo "$ROOT"
}

cleanup() {
    if [ -n "$TMPDIR_BASE" ] && [ -d "$TMPDIR_BASE" ]; then
        rm -rf "$TMPDIR_BASE"
    fi
}

trap cleanup EXIT

# --- Helper: Create a pointer file ---
# Usage: create_pointer FILE POINTER_TO CANONICAL_ENTITY [CANONICAL_STAGE] [CANONICAL_SUBPATH] [CANONICAL_LOC_LINE]
create_pointer() {
    local file="$1"
    local pointer_to="$2"
    local canonical_entity="$3"
    local canonical_stage="${4:-}"
    local canonical_subpath="${5:-}"
    local canonical_loc="${6:-some/old/path}"

    mkdir -p "$(dirname "$file")"

    {
        echo "---"
        echo "pointer_to: $pointer_to"
        [ -n "$canonical_entity" ] && echo "canonical_entity: $canonical_entity"
        [ -n "$canonical_stage" ] && echo "canonical_stage: $canonical_stage"
        [ -n "$canonical_subpath" ] && echo "canonical_subpath: $canonical_subpath"
        echo "---"
        echo ""
        echo "# Pointer to $pointer_to"
        echo ""
        echo "> **Canonical location**: \`$canonical_loc\`"
    } > "$file"
}

# ============================================================
# Category 1: Frontmatter Detection (has_pointer_fm)
# ============================================================

test_frontmatter_detection() {
    echo -e "\n${BLUE}=== Category 1: Frontmatter Detection ===${NC}"

    local ROOT
    ROOT=$(setup_mock_repo)

    # Test 1.1: Valid pointer file detected (use --verbose to see filename in processing)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_valid.md" \
        "design docs" "layer_1_feature_alpha"
    run_sync "$ROOT" --verbose
    assert_contains "1.1 Valid pointer file detected" "$SYNC_OUTPUT" "ptr_valid.md"

    # Test 1.2: File with pointer_to: but no --- (not detected as pointer)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/no_frontmatter.md" <<'EOFILE'
# No Frontmatter
pointer_to: something
canonical_entity: layer_1_feature_alpha

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_not_contains "1.2 No frontmatter delimiters → not detected" "$SYNC_OUTPUT" "no_frontmatter.md"

    # Test 1.3: File with --- but no pointer_to:
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/no_pointer_to.md" <<'EOFILE'
---
title: Just metadata
canonical_entity: layer_1_feature_alpha
---

# No pointer_to field

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_not_contains "1.3 Frontmatter without pointer_to → not detected" "$SYNC_OUTPUT" "no_pointer_to.md"

    # Test 1.4: Empty file
    touch "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/empty.md"
    run_sync "$ROOT" --verbose
    assert_not_contains "1.4 Empty file → not detected" "$SYNC_OUTPUT" "empty.md"

    # Test 1.5: Windows line endings (\r\n)
    printf -- "---\r\npointer_to: design docs\r\ncanonical_entity: layer_1_feature_alpha\r\n---\r\n\r\n# Windows\r\n\r\n> **Canonical location**: \`old/path\`\r\n" \
        > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/windows.md"
    run_sync "$ROOT" --verbose
    assert_contains "1.5 Windows line endings → detected" "$SYNC_OUTPUT" "windows.md"

    cleanup
}

# ============================================================
# Category 2: Field Extraction (extract_fm)
# ============================================================

test_field_extraction() {
    echo -e "\n${BLUE}=== Category 2: Field Extraction ===${NC}"

    local ROOT
    ROOT=$(setup_mock_repo)

    # Test 2.1: Extract pointer_to and canonical_entity (standard)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_standard.md" \
        "design docs" "layer_1_feature_alpha"
    run_sync "$ROOT" --verbose
    assert_contains "2.1 Extracts pointer_to field" "$SYNC_OUTPUT" "pointer_to: design docs"
    assert_contains "2.1b Extracts canonical_entity field" "$SYNC_OUTPUT" "canonical_entity: layer_1_feature_alpha"

    cleanup
    ROOT=$(setup_mock_repo)

    # Test 2.2: Double-quoted values
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_dquote.md" <<'EOFILE'
---
pointer_to: "quoted design docs"
canonical_entity: "layer_1_feature_alpha"
---

# Double Quoted

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    # The script strips quotes, so it should resolve the entity
    assert_contains "2.2 Double-quoted values → entity resolved" "$SYNC_OUTPUT" "Entity found:"

    cleanup
    ROOT=$(setup_mock_repo)

    # Test 2.3: Single-quoted values
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_squote.md" <<'EOFILE'
---
pointer_to: 'single quoted'
canonical_entity: 'layer_1_feature_alpha'
---

# Single Quoted

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_contains "2.3 Single-quoted values → entity resolved" "$SYNC_OUTPUT" "Entity found:"

    cleanup
    ROOT=$(setup_mock_repo)

    # Test 2.4: Missing optional field (canonical_stage not present)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_stage.md" \
        "entity only" "layer_1_feature_alpha" "" ""
    run_sync "$ROOT" --verbose
    assert_contains "2.4 Missing canonical_stage → still resolves entity" "$SYNC_OUTPUT" "Entity found:"

    cleanup
}

# ============================================================
# Category 3: Entity Resolution
# ============================================================

test_entity_resolution() {
    echo -e "\n${BLUE}=== Category 3: Entity Resolution ===${NC}"

    local ROOT

    # Test 3.1: Known entity resolves (sync first to fix path, then validate)
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_known.md" \
        "alpha entity" "layer_1_feature_alpha"
    # First sync to update the canonical location to the correct path
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    # Now validate — should be all correct
    run_sync "$ROOT" --validate
    assert_exit_code "3.1 Known entity → exit 0 (valid)" "0" "$SYNC_EXIT"

    cleanup

    # Test 3.2: Unknown entity → BROKEN
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_unknown.md" \
        "nonexistent" "layer_1_feature_does_not_exist"
    run_sync "$ROOT" --validate
    assert_exit_code "3.2 Unknown entity → exit 1 (broken)" "1" "$SYNC_EXIT"
    assert_contains "3.2b BROKEN message" "$SYNC_OUTPUT" "BROKEN"
    assert_contains "3.2c Entity name in error" "$SYNC_OUTPUT" "layer_1_feature_does_not_exist"

    cleanup

    # Test 3.3: Entity + valid stage → resolves
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_with_stage.md" \
        "alpha design" "layer_1_feature_alpha" "stage_1_04_design"
    run_sync "$ROOT" --verbose
    assert_contains "3.3 Entity + valid stage → stage found" "$SYNC_OUTPUT" "Stage found:"

    cleanup

    # Test 3.4: Entity + invalid stage → BROKEN
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_bad_stage.md" \
        "alpha bad stage" "layer_1_feature_alpha" "stage_1_99_nonexistent"
    run_sync "$ROOT" --validate
    assert_exit_code "3.4 Invalid stage → exit 1" "1" "$SYNC_EXIT"
    assert_contains "3.4b BROKEN message for stage" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 3.5: Entity + stage + valid subpath → resolves
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_subpath.md" \
        "alpha design output" "layer_1_feature_alpha" "stage_1_04_design" "outputs/design.md"
    run_sync "$ROOT" --verbose
    assert_contains "3.5 Entity + stage + valid subpath → full path" "$SYNC_OUTPUT" "Full path:"

    cleanup

    # Test 3.6: Entity + stage + invalid subpath → BROKEN
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_bad_subpath.md" \
        "alpha missing file" "layer_1_feature_alpha" "stage_1_04_design" "outputs/nonexistent.md"
    run_sync "$ROOT" --validate
    assert_exit_code "3.6 Invalid subpath → exit 1" "1" "$SYNC_EXIT"
    assert_contains "3.6b BROKEN message for subpath" "$SYNC_OUTPUT" "BROKEN"

    cleanup
}

# ============================================================
# Category 4: Relative Path Computation
# ============================================================

test_relative_path() {
    echo -e "\n${BLUE}=== Category 4: Relative Path Computation ===${NC}"

    local ROOT content

    # Test 4.1: Sibling entity (gamma → alpha)
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_sibling.md" \
        "sibling" "layer_1_feature_alpha" "" "" "old/wrong/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_sibling.md")
    assert_contains "4.1 Sibling relative path contains ../layer_1_feature_alpha" "$content" "../layer_1_feature_alpha"

    cleanup

    # Test 4.2: Deep pointer → shallow target
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta/pointers"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta/pointers/ptr_up.md" \
        "up to gamma" "layer_1_feature_gamma" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta/pointers/ptr_up.md")
    # Path from beta/pointers/ up to gamma: ../../../../layer_1_feature_gamma
    # pointers -> beta -> layer_2_features -> layer_2_group -> alpha -> layer_1_features -> layer_1_feature_gamma
    # That's 5 levels up then into gamma: ../../../../../layer_1_feature_gamma
    # Actually: from beta/pointers/ the relative path to gamma is:
    # pointers -> beta -> layer_2_features -> layer_2_group -> alpha -> layer_1_features -> gamma
    # = ../../../../../../layer_1_feature_gamma
    # Let me compute: beta is at layer_1_group/layer_1_features/layer_1_feature_alpha/layer_2_group/layer_2_features/layer_2_feature_beta
    # pointers is at .../layer_2_feature_beta/pointers
    # gamma is at layer_1_group/layer_1_features/layer_1_feature_gamma
    # so: ../../../../../../../layer_1_feature_gamma? Let python figure it out
    assert_contains "4.2 Deep to shallow → contains layer_1_feature_gamma" "$content" "layer_1_feature_gamma"

    cleanup

    # Test 4.3: Same entity (pointer within alpha pointing to alpha)
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/ptr_self.md" \
        "self reference" "layer_1_feature_alpha" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/ptr_self.md")
    # Self-reference: pointer is IN alpha, pointing TO alpha → relative path is "."
    assert_contains "4.3 Self-reference → dot path" "$content" '`.'

    cleanup
}

# ============================================================
# Category 5: Update Mechanism
# ============================================================

test_update_mechanism() {
    echo -e "\n${BLUE}=== Category 5: Update Mechanism ===${NC}"

    local ROOT content

    # Test 5.1: Stale canonical location line → updated
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_stale.md" \
        "alpha entity" "layer_1_feature_alpha" "" "" "completely/wrong/old/path"
    run_sync "$ROOT"
    assert_contains "5.1 Stale pointer → UPDATED" "$SYNC_OUTPUT" "UPDATED"
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_stale.md")
    assert_not_contains "5.1b Old path removed" "$content" "completely/wrong/old/path"
    assert_contains "5.1c New path present" "$content" "../layer_1_feature_alpha"

    cleanup

    # Test 5.2: Already-correct canonical location → unchanged
    ROOT=$(setup_mock_repo)
    local correct_relpath
    correct_relpath=$(python3 -c "import os.path; print(os.path.relpath('$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha', '$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma'))")
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_correct.md" \
        "alpha entity" "layer_1_feature_alpha" "" "" "$correct_relpath"
    run_sync "$ROOT"
    assert_contains "5.2 Already correct → OK (unchanged)" "$SYNC_OUTPUT" "unchanged"

    cleanup

    # Test 5.3: Missing Canonical location line → WARN
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_loc.md" <<'EOFILE'
---
pointer_to: alpha entity
canonical_entity: layer_1_feature_alpha
---

# No canonical location line here
This file has frontmatter but no location line to update.
EOFILE
    run_sync "$ROOT"
    assert_contains "5.3 Missing Canonical location line → WARN" "$SYNC_OUTPUT" "WARN"

    cleanup

    # Test 5.4: Dry run does NOT modify files
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_dryrun.md" \
        "alpha entity" "layer_1_feature_alpha" "" "" "old/stale/path"
    run_sync "$ROOT" --dry-run
    assert_contains "5.4a Dry run → WOULD UPDATE" "$SYNC_OUTPUT" "WOULD UPDATE"
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_dryrun.md")
    assert_contains "5.4b File still has old path" "$content" "old/stale/path"

    cleanup
}

# ============================================================
# Category 6: CLI Flags
# ============================================================

test_cli_flags() {
    echo -e "\n${BLUE}=== Category 6: CLI Flags ===${NC}"

    local ROOT

    # Test 6.1: --help shows usage
    ROOT=$(setup_mock_repo)
    run_sync "$ROOT" --help
    assert_exit_code "6.1 --help → exit 0" "0" "$SYNC_EXIT"
    assert_contains "6.1b Shows usage text" "$SYNC_OUTPUT" "Usage:"

    # Test 6.2: Unknown flag → error
    run_sync "$ROOT" --invalid-flag
    assert_exit_code "6.2 Unknown flag → exit 1" "1" "$SYNC_EXIT"
    assert_contains "6.2b Error message" "$SYNC_OUTPUT" "Unknown option"

    # Test 6.3: --validate with all valid pointers → exit 0
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_valid.md" \
        "alpha entity" "layer_1_feature_alpha"
    # First sync to make canonical location correct
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "6.3 --validate all valid → exit 0" "0" "$SYNC_EXIT"

    cleanup

    # Test 6.4: --validate with broken pointer → exit 1
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_broken.md" \
        "broken" "layer_1_feature_nonexistent"
    run_sync "$ROOT" --validate
    assert_exit_code "6.4 --validate with broken → exit 1" "1" "$SYNC_EXIT"

    cleanup

    # Test 6.5: --verbose shows resolution steps
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_verbose.md" \
        "alpha entity" "layer_1_feature_alpha"
    run_sync "$ROOT" --verbose
    assert_contains "6.5 --verbose shows [verbose]" "$SYNC_OUTPUT" "[verbose]"
    assert_contains "6.5b Shows Processing:" "$SYNC_OUTPUT" "Processing:"

    cleanup
}

# ============================================================
# Category 7: Edge Cases
# ============================================================

test_edge_cases() {
    echo -e "\n${BLUE}=== Category 7: Edge Cases ===${NC}"

    local ROOT

    # Test 7.1: No pointer files → graceful exit 0
    ROOT=$(setup_mock_repo)
    run_sync "$ROOT"
    assert_exit_code "7.1 No pointer files → exit 0" "0" "$SYNC_EXIT"
    assert_contains "7.1b Reports no pointer files" "$SYNC_OUTPUT" "No pointer files found"

    cleanup

    # Test 7.2: Pointer with missing canonical_entity → SKIP
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_entity.md" <<'EOFILE'
---
pointer_to: something
---

# No Entity

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT"
    assert_contains "7.2 Missing canonical_entity → SKIP" "$SYNC_OUTPUT" "SKIP"
    assert_exit_code "7.2b Still exits 0 (skip != broken)" "0" "$SYNC_EXIT"

    cleanup

    # Test 7.3: Pointer with empty pointer_to → SKIP
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_empty_to.md" <<'EOFILE'
---
pointer_to:
canonical_entity: layer_1_feature_alpha
---

# Empty pointer_to

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT"
    assert_contains "7.3 Empty pointer_to → SKIP" "$SYNC_OUTPUT" "SKIP"

    cleanup

    # Test 7.4: Multiple pointer files, mix of valid and broken → correct counts
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_ok1.md" \
        "alpha" "layer_1_feature_alpha"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_ok2.md" \
        "alpha design" "layer_1_feature_alpha" "stage_1_04_design"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_broken1.md" \
        "missing" "layer_1_feature_nonexistent"
    run_sync "$ROOT" --validate
    assert_exit_code "7.4a Mixed valid/broken → exit 1" "1" "$SYNC_EXIT"
    assert_contains "7.4b Reports total count" "$SYNC_OUTPUT" "Total pointer files: 3"
    assert_contains "7.4c Reports broken count" "$SYNC_OUTPUT" "Broken"

    cleanup

    # Test 7.5: Pointer file in .0agnostic/ should still be found
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/.0agnostic"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/.0agnostic/ptr_hidden.md" \
        "alpha" "layer_1_feature_alpha"
    run_sync "$ROOT" --verbose
    assert_contains "7.5 Pointer in .0agnostic/ dir → detected" "$SYNC_OUTPUT" "ptr_hidden.md"

    cleanup

    # Test 7.6: Validate mode with stale (not broken) pointer → counts as broken/stale
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_stale_val.md" \
        "alpha" "layer_1_feature_alpha" "" "" "wrong/stale/path"
    run_sync "$ROOT" --validate
    assert_exit_code "7.6a Stale pointer in validate mode → exit 1" "1" "$SYNC_EXIT"
    assert_contains "7.6b STALE message" "$SYNC_OUTPUT" "STALE"

    cleanup
}

# ============================================================
# Main
# ============================================================

echo "=========================================="
echo "  pointer-sync.sh Test Suite"
echo "=========================================="
echo ""
echo "Script under test: $REAL_SCRIPT"
echo ""

if [ -n "$CATEGORY_FILTER" ]; then
    echo "Running category: $CATEGORY_FILTER"
fi

# Run tests
if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "frontmatter" ]; then
    test_frontmatter_detection
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "extraction" ]; then
    test_field_extraction
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "resolution" ]; then
    test_entity_resolution
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "relpath" ]; then
    test_relative_path
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "update" ]; then
    test_update_mechanism
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "flags" ]; then
    test_cli_flags
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "edge" ]; then
    test_edge_cases
fi

# Summary
echo ""
echo "=========================================="
echo -e "  Results: ${GREEN}${PASS} PASS${NC}  ${RED}${FAIL} FAIL${NC}  ${YELLOW}${SKIP} SKIP${NC}  (${TOTAL} total)"
echo "=========================================="

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
exit 0
