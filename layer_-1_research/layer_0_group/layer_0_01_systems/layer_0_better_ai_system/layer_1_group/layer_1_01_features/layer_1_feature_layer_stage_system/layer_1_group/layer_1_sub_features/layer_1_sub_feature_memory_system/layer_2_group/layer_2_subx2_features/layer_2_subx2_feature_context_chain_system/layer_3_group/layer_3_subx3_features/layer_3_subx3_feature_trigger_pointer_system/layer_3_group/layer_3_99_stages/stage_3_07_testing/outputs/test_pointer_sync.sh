#!/bin/bash
#
# test_pointer_sync.sh — Comprehensive test suite for pointer-sync.sh
#
# Creates a temporary mock layer-stage hierarchy, runs pointer-sync.sh
# against it, and validates behavior across 19 test categories.
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

    # Entity: layer_1_feature_beta (another entity, deeper)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/stage_1_04_design/outputs"
    echo "# Beta Design" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/stage_1_04_design/outputs/design.md"

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
    assert_contains "2.2 Double-quoted values → entity resolved" "$SYNC_OUTPUT" "Entity resolved"

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
    assert_contains "2.3 Single-quoted values → entity resolved" "$SYNC_OUTPUT" "Entity resolved"

    cleanup
    ROOT=$(setup_mock_repo)

    # Test 2.4: Missing optional field (canonical_stage not present)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_stage.md" \
        "entity only" "layer_1_feature_alpha" "" ""
    run_sync "$ROOT" --verbose
    assert_contains "2.4 Missing canonical_stage → still resolves entity" "$SYNC_OUTPUT" "Entity resolved"

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
    assert_contains "3.3 Entity + valid stage → stage found" "$SYNC_OUTPUT" "Stage resolved"

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
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/pointers"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/pointers/ptr_up.md" \
        "up to gamma" "layer_1_feature_gamma" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/pointers/ptr_up.md")
    # Path from beta/pointers/ up to gamma: ../../../../layer_1_feature_gamma
    # pointers -> beta -> layer_1_features -> layer_1_group -> alpha -> layer_1_features -> layer_1_feature_gamma
    # That's 5 levels up then into gamma: ../../../../../layer_1_feature_gamma
    # Actually: from beta/pointers/ the relative path to gamma is:
    # pointers -> beta -> layer_1_features -> layer_1_group -> alpha -> layer_1_features -> gamma
    # = ../../../../../../layer_1_feature_gamma
    # Let me compute: beta is at layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta
    # pointers is at .../layer_1_feature_beta/pointers
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
# Category 8: Idempotency
# ============================================================

test_idempotency() {
    echo -e "\n${BLUE}=== Category 8: Idempotency ===${NC}"

    local ROOT

    # Test 8.1: Sync twice — second run should report all unchanged
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_idem.md" \
        "alpha entity" "layer_1_feature_alpha" "" "" "old/stale/path"
    # First run: should update
    run_sync "$ROOT"
    assert_contains "8.1a First sync updates stale pointer" "$SYNC_OUTPUT" "UPDATED"

    # Second run: should report unchanged
    run_sync "$ROOT"
    assert_contains "8.1b Second sync reports unchanged" "$SYNC_OUTPUT" "unchanged"
    assert_not_contains "8.1c Second sync does NOT update" "$SYNC_OUTPUT" "UPDATED"

    cleanup

    # Test 8.2: Sync twice with multiple pointers — all unchanged on second run
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_a.md" \
        "alpha" "layer_1_feature_alpha" "" "" "wrong/a"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_b.md" \
        "alpha design" "layer_1_feature_alpha" "stage_1_04_design" "" "wrong/b"
    # First run
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    # Second run with validate — all should be valid
    run_sync "$ROOT" --validate
    assert_exit_code "8.2 Multiple pointers synced then validated → exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 9: Spaces in Paths
# ============================================================

test_spaces_in_paths() {
    echo -e "\n${BLUE}=== Category 9: Spaces in Paths ===${NC}"

    local ROOT content

    # Test 9.1: Entity directory with spaces in name
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_has spaces"
    echo "# Spaced" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_has spaces/README.md"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_spaces.md" \
        "spaced entity" "layer_1_feature_has spaces" "" "" "old/path"
    run_sync "$ROOT" --verbose
    # Should resolve the entity despite spaces
    assert_contains "9.1 Entity with spaces in name → resolves" "$SYNC_OUTPUT" "Entity resolved"

    cleanup

    # Test 9.2: Subpath with spaces
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/my docs"
    echo "# Docs" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/my docs/notes.md"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_spaced_sub.md" \
        "alpha docs" "layer_1_feature_alpha" "" "my docs" "old/path"
    run_sync "$ROOT" --verbose
    assert_contains "9.2 Subpath with spaces → resolves" "$SYNC_OUTPUT" "Full path:"
    assert_not_contains "9.2b No BROKEN error" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 9.3: Pointer file itself in directory with spaces
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/my notes"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/my notes/ptr_in_spaced_dir.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/path"
    run_sync "$ROOT"
    assert_contains "9.3 Pointer file in spaced directory → processed" "$SYNC_OUTPUT" "ptr_in_spaced_dir.md"
    assert_not_contains "9.3b No errors" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 9.4: Relative path computed correctly with spaces
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_has spaces"
    echo "# Spaced" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_has spaces/README.md"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_relpath_spaces.md" \
        "spaced" "layer_1_feature_has spaces" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_relpath_spaces.md")
    assert_contains "9.4 Relative path with spaces → correct" "$content" "layer_1_feature_has spaces"

    cleanup
}

# ============================================================
# Category 10: Duplicate Entity Names
# ============================================================

test_duplicate_entities() {
    echo -e "\n${BLUE}=== Category 10: Duplicate Entity Names ===${NC}"

    local ROOT

    # Test 10.1: Two directories with the same entity name — first match wins, no error
    ROOT=$(setup_mock_repo)
    # Create a second directory with the same name at a different path
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_gamma"
    echo "# Nested Gamma" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_gamma/README.md"
    # The original layer_1_feature_gamma still exists at layer_1_group/layer_1_features/
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/ptr_ambiguous.md" \
        "gamma" "layer_1_feature_gamma"
    run_sync "$ROOT" --verbose
    # Should NOT error — should resolve to one of them
    assert_not_contains "10.1 Duplicate entity names → no BROKEN" "$SYNC_OUTPUT" "BROKEN"
    assert_contains "10.1b Resolves to some entity" "$SYNC_OUTPUT" "Entity resolved"

    cleanup

    # Test 10.2: Validate still passes with duplicates (resolved is valid)
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_gamma"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/ptr_ambig_val.md" \
        "gamma" "layer_1_feature_gamma"
    # Sync first to update canonical location
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    # Then validate
    run_sync "$ROOT" --validate
    assert_exit_code "10.2 Validate with duplicate entities → exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 11: File Subpath (not directory)
# ============================================================

test_file_subpath() {
    echo -e "\n${BLUE}=== Category 11: File Subpath ===${NC}"

    local ROOT content

    # Test 11.1: Subpath pointing to a file → resolves
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_file_target.md" \
        "alpha design doc" "layer_1_feature_alpha" "stage_1_04_design" "outputs/design.md" "old/path"
    run_sync "$ROOT" --verbose
    assert_contains "11.1 File subpath → resolves" "$SYNC_OUTPUT" "Full path:"
    assert_not_contains "11.1b No BROKEN" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 11.2: Relative path to a file (not dir) is correct
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_file_rel.md" \
        "alpha design doc" "layer_1_feature_alpha" "stage_1_04_design" "outputs/design.md" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_file_rel.md")
    assert_contains "11.2 Relative path to file contains filename" "$content" "design.md"

    cleanup

    # Test 11.3: Sync then validate with file subpath
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_file_val.md" \
        "alpha design doc" "layer_1_feature_alpha" "stage_1_04_design" "outputs/design.md" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "11.3 File subpath synced then validated → exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 12: Combination Flags
# ============================================================

test_combination_flags() {
    echo -e "\n${BLUE}=== Category 12: Combination Flags ===${NC}"

    local ROOT content

    # Test 12.1: --dry-run --validate — dry-run takes precedence (if/elif order)
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_combo.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/stale/path"
    run_sync "$ROOT" --dry-run --validate
    assert_contains "12.1 --dry-run --validate → shows WOULD UPDATE (dry-run wins)" "$SYNC_OUTPUT" "WOULD UPDATE"
    assert_not_contains "12.1b Does not show STALE" "$SYNC_OUTPUT" "STALE"

    cleanup

    # Test 12.2: --verbose --dry-run — both active simultaneously
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_vdry.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/path"
    run_sync "$ROOT" --verbose --dry-run
    assert_contains "12.2a Verbose + dry-run → shows [verbose]" "$SYNC_OUTPUT" "[verbose]"
    assert_contains "12.2b Verbose + dry-run → shows WOULD UPDATE" "$SYNC_OUTPUT" "WOULD UPDATE"

    cleanup

    # Test 12.3: --dry-run does not modify file even with --validate
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_mod.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/stale/path"
    run_sync "$ROOT" --dry-run --validate
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_mod.md")
    assert_contains "12.3 File unchanged after --dry-run --validate" "$content" "old/stale/path"

    cleanup

    # Test 12.4: --verbose --validate — shows resolution steps for valid pointers
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_vval.md" \
        "alpha" "layer_1_feature_alpha"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --verbose --validate
    assert_contains "12.4 Verbose + validate → shows Processing:" "$SYNC_OUTPUT" "Processing:"
    assert_exit_code "12.4b Exits 0 for valid pointer" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 13: Python3 Dependency
# ============================================================

test_python3_dependency() {
    echo -e "\n${BLUE}=== Category 13: Python3 Dependency ===${NC}"

    local ROOT

    # Test 13.1: relpath computation produces correct result for known paths
    # (Validates that python3 -c os.path.relpath is invoked correctly)
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_deep.md" \
        "gamma" "layer_1_feature_gamma" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    local content
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_deep.md")
    # Count the number of ../ in the path — should be exactly 4
    # beta -> layer_1_features -> layer_1_group -> alpha -> layer_1_features -> gamma
    # from beta dir: ../../../../layer_1_feature_gamma
    # Actually: ptr is in layer_1_feature_beta/, target is layer_1_feature_gamma/
    # relpath from layer_1_feature_beta/ to layer_1_feature_gamma/
    # = ../../../../layer_1_feature_gamma (up: beta -> features -> group -> alpha -> features level -> gamma)
    local expected_relpath
    expected_relpath=$(python3 -c "import os.path; print(os.path.relpath('$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma', '$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta'))")
    assert_contains "13.1 Deep relpath matches python3 computation" "$content" "$expected_relpath"

    cleanup

    # Test 13.2: Verify python3 is available (precondition for the script)
    if command -v python3 > /dev/null 2>&1; then
        TOTAL=$((TOTAL + 1))
        echo -e "  ${GREEN}PASS${NC}: 13.2 python3 is available on this system"
        PASS=$((PASS + 1))
    else
        TOTAL=$((TOTAL + 1))
        echo -e "  ${RED}FAIL${NC}: 13.2 python3 is NOT available — pointer-sync.sh will fail"
        FAIL=$((FAIL + 1))
    fi
}

# ============================================================
# Category 14: Symlinks
# ============================================================

test_symlinks() {
    echo -e "\n${BLUE}=== Category 14: Symlinks ===${NC}"

    local ROOT content

    # Test 14.1: Entity directory is a symlink — find -type d doesn't follow symlinks by default
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_real_target"
    echo "# Real" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_real_target/README.md"
    ln -s "$ROOT/layer_1_group/layer_1_features/layer_1_feature_real_target" \
          "$ROOT/layer_1_group/layer_1_features/layer_1_feature_symlinked"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_symlink.md" \
        "symlinked entity" "layer_1_feature_symlinked" "" "" "old/path"
    run_sync "$ROOT" --verbose
    # find -type d won't match symlinks — this should be BROKEN
    # (unless the script uses -type d -o -type l or similar)
    if echo "$SYNC_OUTPUT" | grep -qF "Entity resolved"; then
        TOTAL=$((TOTAL + 1))
        echo -e "  ${GREEN}PASS${NC}: 14.1 Symlinked entity → resolves (find follows symlinks)"
        PASS=$((PASS + 1))
    elif echo "$SYNC_OUTPUT" | grep -qF "BROKEN"; then
        TOTAL=$((TOTAL + 1))
        echo -e "  ${GREEN}PASS${NC}: 14.1 Symlinked entity → BROKEN (find -type d skips symlinks — known limitation)"
        PASS=$((PASS + 1))
    else
        TOTAL=$((TOTAL + 1))
        echo -e "  ${RED}FAIL${NC}: 14.1 Symlinked entity → unexpected output"
        echo -e "    Output: $(echo "$SYNC_OUTPUT" | head -5)"
        FAIL=$((FAIL + 1))
    fi

    cleanup

    # Test 14.2: Target subpath is a symlink to a real file
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/real_dir"
    echo "# Real file" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/real_dir/doc.md"
    ln -s "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/real_dir" \
          "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/linked_dir"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_symlink_sub.md" \
        "linked subpath" "layer_1_feature_alpha" "stage_1_04_design" "outputs/linked_dir" "old/path"
    run_sync "$ROOT" --verbose
    # [ ! -e "$path" ] follows symlinks, so this should resolve
    assert_not_contains "14.2 Symlinked subpath → no BROKEN" "$SYNC_OUTPUT" "BROKEN"
    assert_contains "14.2b Full path resolved" "$SYNC_OUTPUT" "Full path:"

    cleanup

    # Test 14.3: Pointer file itself is a symlink
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_real.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/path"
    ln -s "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_real.md" \
          "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_link.md"
    run_sync "$ROOT" --verbose
    # grep -rl follows symlinks, so it may find both the real file and the link
    assert_contains "14.3 Pointer file symlink → at least one found" "$SYNC_OUTPUT" "ptr_"

    cleanup
}

# ============================================================
# Category 15: Very Long Paths
# ============================================================

test_long_paths() {
    echo -e "\n${BLUE}=== Category 15: Very Long Paths ===${NC}"

    local ROOT

    # Test 15.1: Deeply nested entity path (mimics real repo depth)
    ROOT=$(setup_mock_repo)
    local DEEP_PATH="$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/layer_2_group/layer_2_features/layer_2_feature_delta/layer_3_group/layer_3_features/layer_3_feature_epsilon"
    mkdir -p "$DEEP_PATH"
    echo "# Deep" > "$DEEP_PATH/README.md"

    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_deep_target.md" \
        "deep entity" "layer_3_feature_epsilon" "" "" "old/path"
    run_sync "$ROOT" --verbose
    assert_contains "15.1 Deeply nested entity → resolves" "$SYNC_OUTPUT" "Entity resolved"
    assert_not_contains "15.1b No errors" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 15.2: Pointer file at a deeply nested location pointing up
    ROOT=$(setup_mock_repo)
    DEEP_PATH="$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/layer_2_group/layer_2_features/layer_2_feature_delta/layer_3_group/layer_3_features/layer_3_feature_epsilon"
    mkdir -p "$DEEP_PATH"
    create_pointer "$DEEP_PATH/ptr_up_from_deep.md" \
        "gamma from deep" "layer_1_feature_gamma" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    local content
    content=$(cat "$DEEP_PATH/ptr_up_from_deep.md")
    # Should contain many ../ segments
    assert_contains "15.2 Deep pointer to shallow → relative path computed" "$content" "layer_1_feature_gamma"
    # Verify correctness with python
    local expected
    expected=$(python3 -c "import os.path; print(os.path.relpath('$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma', '$DEEP_PATH'))")
    assert_contains "15.2b Relative path matches python3" "$content" "$expected"

    cleanup

    # Test 15.3: Sync then validate on deep paths
    ROOT=$(setup_mock_repo)
    DEEP_PATH="$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/layer_2_group/layer_2_features/layer_2_feature_delta/layer_3_group/layer_3_features/layer_3_feature_epsilon"
    mkdir -p "$DEEP_PATH"
    create_pointer "$DEEP_PATH/ptr_val_deep.md" \
        "gamma" "layer_1_feature_gamma" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "15.3 Deep path synced then validated → exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 16: Non-Markdown Files
# ============================================================

test_non_markdown_files() {
    echo -e "\n${BLUE}=== Category 16: Non-Markdown Files ===${NC}"

    local ROOT

    # Test 16.1: .yaml file with pointer_to: → ignored (--include="*.md")
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/config.yaml" <<'EOFILE'
---
pointer_to: alpha
canonical_entity: layer_1_feature_alpha
---
EOFILE
    run_sync "$ROOT" --verbose
    assert_not_contains "16.1 .yaml file with pointer_to → not processed" "$SYNC_OUTPUT" "config.yaml"

    cleanup

    # Test 16.2: .txt file with pointer frontmatter → ignored
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/notes.txt" <<'EOFILE'
---
pointer_to: alpha
canonical_entity: layer_1_feature_alpha
---

# Notes

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_not_contains "16.2 .txt file with pointer_to → not processed" "$SYNC_OUTPUT" "notes.txt"

    cleanup

    # Test 16.3: .json file → ignored
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/data.json" <<'EOFILE'
{
  "pointer_to": "alpha",
  "canonical_entity": "layer_1_feature_alpha"
}
EOFILE
    run_sync "$ROOT" --verbose
    assert_not_contains "16.3 .json file → not processed" "$SYNC_OUTPUT" "data.json"

    cleanup

    # Test 16.4: Only .md files counted in total
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    # Create one valid .md pointer and one .yaml with pointer_to
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/real_ptr.md" \
        "alpha" "layer_1_feature_alpha"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/fake_ptr.yaml" <<'EOFILE'
---
pointer_to: alpha
canonical_entity: layer_1_feature_alpha
---
EOFILE
    run_sync "$ROOT"
    assert_contains "16.4 Only .md counted → Total pointer files: 1" "$SYNC_OUTPUT" "Total pointer files: 1"

    cleanup
}

# ============================================================
# Category 17: Multiple Pointers to Same Target
# ============================================================

test_multiple_pointers_same_target() {
    echo -e "\n${BLUE}=== Category 17: Multiple Pointers to Same Target ===${NC}"

    local ROOT content_a content_b

    # Test 17.1: Two pointers in different dirs pointing to same entity → both get correct relative paths
    ROOT=$(setup_mock_repo)
    # Pointer A: in gamma (sibling of alpha)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_to_alpha_a.md" \
        "alpha from gamma" "layer_1_feature_alpha" "" "" "old/a"
    # Pointer B: in beta (child of alpha)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_to_alpha_b.md" \
        "alpha from beta" "layer_1_feature_alpha" "" "" "old/b"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1

    content_a=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_to_alpha_a.md")
    content_b=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_to_alpha_b.md")

    # Pointer A (gamma → alpha): should be ../layer_1_feature_alpha
    assert_contains "17.1a Pointer A (gamma→alpha) → ../layer_1_feature_alpha" "$content_a" "../layer_1_feature_alpha"
    # Pointer B (beta → alpha): should be ../../.. (up from beta to alpha)
    local expected_b
    expected_b=$(python3 -c "import os.path; print(os.path.relpath('$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha', '$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta'))")
    assert_contains "17.1b Pointer B (beta→alpha) → correct relative path" "$content_b" "$expected_b"
    # The two paths should be DIFFERENT
    local path_a path_b
    path_a=$(grep 'Canonical location' "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_to_alpha_a.md")
    path_b=$(grep 'Canonical location' "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_to_alpha_b.md")
    TOTAL=$((TOTAL + 1))
    if [ "$path_a" != "$path_b" ]; then
        echo -e "  ${GREEN}PASS${NC}: 17.1c Two pointers to same target → different relative paths"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: 17.1c Two pointers to same target should have different relative paths"
        echo -e "    Path A: $path_a"
        echo -e "    Path B: $path_b"
        FAIL=$((FAIL + 1))
    fi

    cleanup

    # Test 17.2: Validate passes when multiple pointers to same target are all synced
    ROOT=$(setup_mock_repo)
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_multi_a.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/a"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/ptr_multi_b.md" \
        "alpha" "layer_1_feature_alpha" "" "" "old/b"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "17.2 Multiple pointers to same target → validate exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 18: Extra Frontmatter Fields
# ============================================================

test_extra_frontmatter() {
    echo -e "\n${BLUE}=== Category 18: Extra Frontmatter Fields ===${NC}"

    local ROOT

    # Test 18.1: Pointer with extra unrelated YAML fields → still resolves
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_extra_fields.md" <<'EOFILE'
---
title: "Some document title"
date: 2026-03-01
tags: [pointer, test, extra]
pointer_to: alpha design
canonical_entity: layer_1_feature_alpha
canonical_stage: stage_1_04_design
author: test-suite
version: 1.0
---

# Pointer with Extra Fields

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_contains "18.1a Extra fields → entity resolves" "$SYNC_OUTPUT" "Entity resolved"
    assert_contains "18.1b Extra fields → stage resolves" "$SYNC_OUTPUT" "Stage resolved"
    assert_not_contains "18.1c No BROKEN" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 18.2: pointer_to not on the first field line → still extracted
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_late_pointer.md" <<'EOFILE'
---
title: "Document"
author: someone
canonical_entity: layer_1_feature_alpha
pointer_to: alpha entity
description: "This pointer_to is not the first field"
---

# Pointer with Late pointer_to

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_contains "18.2 pointer_to after other fields → still detected" "$SYNC_OUTPUT" "Entity resolved"

    cleanup

    # Test 18.3: Field with colon in value (e.g., "pointer_to: alpha: design docs")
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_colon_value.md" <<'EOFILE'
---
pointer_to: alpha: design docs
canonical_entity: layer_1_feature_alpha
---

# Colon in Value

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    # pointer_to extracts "alpha: design docs" — the script should still resolve via canonical_entity
    assert_contains "18.3 Colon in pointer_to value → entity still resolves" "$SYNC_OUTPUT" "Entity resolved"

    cleanup

    # Test 18.4: YAML comment lines in frontmatter → ignored
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_yaml_comments.md" <<'EOFILE'
---
# This is a YAML comment
pointer_to: alpha entity
# Another comment
canonical_entity: layer_1_feature_alpha
# canonical_stage: stage_1_04_design  (commented out)
---

# YAML Comments

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_contains "18.4a YAML comments → entity resolves" "$SYNC_OUTPUT" "Entity resolved"
    # The commented-out canonical_stage should NOT be extracted
    assert_not_contains "18.4b Commented canonical_stage → not extracted" "$SYNC_OUTPUT" "Stage resolved"

    cleanup
}

# ============================================================
# Category 19: Awk Replacement Edge Cases
# ============================================================

test_awk_replacement() {
    echo -e "\n${BLUE}=== Category 19: Awk Replacement Edge Cases ===${NC}"

    local ROOT content

    # Test 19.1: Pointer file with content below the Canonical location line → preserved
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_content_below.md" <<'EOFILE'
---
pointer_to: alpha entity
canonical_entity: layer_1_feature_alpha
---

# Pointer

> **Canonical location**: `old/wrong/path`

## Additional Content

This paragraph should survive the update.

- Bullet 1
- Bullet 2
- Bullet 3

```bash
echo "code block should survive too"
```
EOFILE
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_content_below.md")
    assert_contains "19.1a Content below canonical line → paragraph preserved" "$content" "This paragraph should survive the update."
    assert_contains "19.1b Bullets preserved" "$content" "Bullet 2"
    assert_contains "19.1c Code block preserved" "$content" "code block should survive too"
    assert_not_contains "19.1d Old path replaced" "$content" "old/wrong/path"

    cleanup

    # Test 19.2: Multiple Canonical location lines → only first updated
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_multi_loc.md" <<'EOFILE'
---
pointer_to: alpha entity
canonical_entity: layer_1_feature_alpha
---

# Pointer

> **Canonical location**: `old/wrong/path`

## Notes

Mentioned again: > **Canonical location**: `some/other/reference`
EOFILE
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_multi_loc.md")
    # First line should be updated, second mention preserved as-is
    assert_contains "19.2a First canonical line updated" "$content" "../layer_1_feature_alpha"
    assert_contains "19.2b Second mention preserved" "$content" "some/other/reference"

    cleanup

    # Test 19.3: Canonical location line with special characters in old path → replaced cleanly
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_special_old.md" <<'EOFILE'
---
pointer_to: alpha entity
canonical_entity: layer_1_feature_alpha
---

# Pointer

> **Canonical location**: `../../../some/path with spaces & special (chars)/target`
EOFILE
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_special_old.md")
    assert_contains "19.3 Special chars in old path → replaced with correct path" "$content" "../layer_1_feature_alpha"
    assert_not_contains "19.3b Old special path gone" "$content" "special (chars)"

    cleanup

    # Test 19.4: Frontmatter preserved exactly after awk replacement
    ROOT=$(setup_mock_repo)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_fm_preserve.md" <<'EOFILE'
---
pointer_to: alpha entity
canonical_entity: layer_1_feature_alpha
custom_field: preserve_me
---

# Pointer

> **Canonical location**: `old/path`
EOFILE
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_fm_preserve.md")
    assert_contains "19.4 Frontmatter preserved after update" "$content" "custom_field: preserve_me"

    cleanup
}

# ============================================================
# Helper: Setup mock repo WITH UUID infrastructure
# ============================================================

setup_uuid_mock_repo() {
    TMPDIR_BASE=$(mktemp -d /tmp/test_pointer_sync.XXXXXX)

    local ROOT="$TMPDIR_BASE/mock_repo"
    mkdir -p "$ROOT/.0agnostic"

    cp "$REAL_SCRIPT" "$ROOT/.0agnostic/pointer-sync.sh"
    chmod +x "$ROOT/.0agnostic/pointer-sync.sh"

    # Entity: layer_1_feature_alpha (with entity_id)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs"
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_06_development/outputs"
    echo "# Alpha Design" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/stage_1_04_design/outputs/design.md"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/0AGNOSTIC.md" <<'EOFILE'
# 0AGNOSTIC.md - layer_1_feature_alpha

## Identity

entity_id: "aaaa1111-1111-1111-1111-111111111111"

You are alpha.
EOFILE

    # Entity: layer_1_feature_beta (deeper, with entity_id)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/stage_1_04_design/outputs"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_features/layer_1_feature_beta/0AGNOSTIC.md" <<'EOFILE'
# 0AGNOSTIC.md - layer_1_feature_beta

## Identity

entity_id: "bbbb2222-2222-2222-2222-222222222222"

You are beta.
EOFILE

    # Entity: layer_1_feature_gamma (sibling, with entity_id)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    echo "# Gamma README" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/README.md"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/0AGNOSTIC.md" <<'EOFILE'
# 0AGNOSTIC.md - layer_1_feature_gamma

## Identity

entity_id: "cccc3333-3333-3333-3333-333333333333"

You are gamma.
EOFILE

    # Stage registry for alpha (with stage_index.json)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_99_stages/stage_1_00_stage_registry"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_99_stages/stage_1_00_stage_registry/stage_index.json" <<'EOFILE'
{
  "entity_id": "aaaa1111-1111-1111-1111-111111111111",
  "entity_name": "layer_1_feature_alpha",
  "stages": [
    {
      "stage_id": "dddd4444-4444-4444-4444-444444444444",
      "stage_number": "04",
      "stage_name": "design",
      "directory": "stage_1_04_design"
    },
    {
      "stage_id": "eeee5555-5555-5555-5555-555555555555",
      "stage_number": "06",
      "stage_name": "development",
      "directory": "stage_1_06_development"
    }
  ]
}
EOFILE

    # Create the stage directories in the 99_stages path too (so stage UUIDs map to real paths)
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_99_stages/stage_1_04_design/outputs"
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_99_stages/stage_1_06_development/outputs"
    echo "# Alpha Stage Design" > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha/layer_1_group/layer_1_99_stages/stage_1_04_design/outputs/design.md"

    echo "$ROOT"
}

# --- Helper: Create a UUID-based pointer file ---
# Usage: create_uuid_pointer FILE POINTER_TO ENTITY_ID [STAGE_ID] [SUBPATH] [CANONICAL_LOC_LINE]
create_uuid_pointer() {
    local file="$1"
    local pointer_to="$2"
    local entity_id="$3"
    local stage_id="${4:-}"
    local subpath="${5:-}"
    local canonical_loc="${6:-some/old/path}"

    mkdir -p "$(dirname "$file")"

    {
        echo "---"
        echo "pointer_to: $pointer_to"
        [ -n "$entity_id" ] && echo "canonical_entity_id: $entity_id"
        [ -n "$stage_id" ] && echo "canonical_stage_id: $stage_id"
        [ -n "$subpath" ] && echo "canonical_subpath: $subpath"
        echo "---"
        echo ""
        echo "# Pointer to $pointer_to"
        echo ""
        echo "> **Canonical location**: \`$canonical_loc\`"
    } > "$file"
}

# ============================================================
# Category 20: UUID Entity Resolution
# ============================================================

test_uuid_resolution() {
    echo -e "\n${BLUE}=== Category 20: UUID Entity Resolution ===${NC}"

    local ROOT

    # Test 20.1: UUID-based entity resolution
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid.md" \
        "alpha via uuid" "aaaa1111-1111-1111-1111-111111111111"
    run_sync "$ROOT" --verbose
    assert_contains "20.1 UUID entity resolution → resolved via UUID" "$SYNC_OUTPUT" "Entity resolved via UUID"
    assert_not_contains "20.1b No BROKEN" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 20.2: UUID-based entity + stage resolution
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_stage.md" \
        "alpha design via uuid" "aaaa1111-1111-1111-1111-111111111111" "dddd4444-4444-4444-4444-444444444444"
    run_sync "$ROOT" --verbose
    assert_contains "20.2a Entity resolved via UUID" "$SYNC_OUTPUT" "Entity resolved via UUID"
    assert_contains "20.2b Stage resolved via UUID" "$SYNC_OUTPUT" "Stage resolved via UUID"

    cleanup

    # Test 20.3: UUID entity + stage + subpath
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_full.md" \
        "alpha design output" "aaaa1111-1111-1111-1111-111111111111" "dddd4444-4444-4444-4444-444444444444" "outputs/design.md"
    run_sync "$ROOT" --verbose
    assert_contains "20.3a Full path resolved" "$SYNC_OUTPUT" "Full path:"
    assert_not_contains "20.3b No BROKEN" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 20.4: Nonexistent UUID → BROKEN
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_bad_uuid.md" \
        "nonexistent" "ffff9999-9999-9999-9999-999999999999"
    run_sync "$ROOT" --validate
    assert_exit_code "20.4 Nonexistent UUID → exit 1" "1" "$SYNC_EXIT"
    assert_contains "20.4b BROKEN message" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 20.5: UUID entity valid + UUID stage invalid → BROKEN
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_bad_stage_uuid.md" \
        "bad stage" "aaaa1111-1111-1111-1111-111111111111" "ffff9999-9999-9999-9999-999999999999"
    run_sync "$ROOT" --validate
    assert_exit_code "20.5 Valid entity UUID + invalid stage UUID → exit 1" "1" "$SYNC_EXIT"
    assert_contains "20.5b BROKEN for stage" "$SYNC_OUTPUT" "BROKEN"

    cleanup

    # Test 20.6: UUID sync then validate → exit 0
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_val.md" \
        "alpha" "aaaa1111-1111-1111-1111-111111111111" "" "" "old/stale"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "20.6 UUID sync then validate → exit 0" "0" "$SYNC_EXIT"

    cleanup

    # Test 20.7: UUID pointer computes correct relative path
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_relpath.md" \
        "alpha" "aaaa1111-1111-1111-1111-111111111111" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    local content
    content=$(cat "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_relpath.md")
    assert_contains "20.7 UUID relpath → ../layer_1_feature_alpha" "$content" "../layer_1_feature_alpha"

    cleanup
}

# ============================================================
# Category 21: --rebuild-index
# ============================================================

test_rebuild_index() {
    echo -e "\n${BLUE}=== Category 21: --rebuild-index ===${NC}"

    local ROOT

    # Test 21.1: Rebuild creates .uuid-index.json
    ROOT=$(setup_uuid_mock_repo)
    run_sync "$ROOT" --rebuild-index
    assert_exit_code "21.1a Rebuild exits 0" "0" "$SYNC_EXIT"
    TOTAL=$((TOTAL + 1))
    if [ -f "$ROOT/.uuid-index.json" ]; then
        echo -e "  ${GREEN}PASS${NC}: 21.1b .uuid-index.json created"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: 21.1b .uuid-index.json not created"
        FAIL=$((FAIL + 1))
    fi

    cleanup

    # Test 21.2: Index contains correct entity count
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local entity_count
    entity_count=$(python3 -c "
import json
with open('$ROOT/.uuid-index.json') as f:
    data = json.load(f)
print(sum(1 for v in data.get('uuids', {}).values() if v.get('type') == 'entity'))
" 2>/dev/null)
    assert_eq "21.2 Index has 3 entities" "3" "$entity_count"

    cleanup

    # Test 21.3: Index contains stage UUIDs from stage_index.json
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local stage_count
    stage_count=$(python3 -c "
import json
with open('$ROOT/.uuid-index.json') as f:
    data = json.load(f)
print(sum(1 for v in data.get('uuids', {}).values() if v.get('type') == 'stage'))
" 2>/dev/null)
    assert_eq "21.3 Index has 2 stages" "2" "$stage_count"

    cleanup

    # Test 21.4: Index has checksum
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local has_checksum
    has_checksum=$(python3 -c "
import json
with open('$ROOT/.uuid-index.json') as f:
    data = json.load(f)
cs = data.get('checksum', '')
print('yes' if cs.startswith('sha256:') else 'no')
" 2>/dev/null)
    assert_eq "21.4 Index has sha256 checksum" "yes" "$has_checksum"

    cleanup

    # Test 21.5: Index has name-to-UUID mappings
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local alpha_uuid
    alpha_uuid=$(python3 -c "
import json
with open('$ROOT/.uuid-index.json') as f:
    data = json.load(f)
print(data.get('names', {}).get('layer_1_feature_alpha', ''))
" 2>/dev/null)
    assert_eq "21.5 Name mapping alpha → correct UUID" "aaaa1111-1111-1111-1111-111111111111" "$alpha_uuid"

    cleanup

    # Test 21.6: Rebuild is idempotent (same count)
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local count1
    count1=$(python3 -c "import json; print(len(json.load(open('$ROOT/.uuid-index.json')).get('uuids', {})))" 2>/dev/null)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local count2
    count2=$(python3 -c "import json; print(len(json.load(open('$ROOT/.uuid-index.json')).get('uuids', {})))" 2>/dev/null)
    assert_eq "21.6 Rebuild idempotent (same count)" "$count1" "$count2"

    cleanup

    # Test 21.7: Duplicate UUIDs produce warning
    ROOT=$(setup_uuid_mock_repo)
    # Create a second entity with the same UUID
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_delta"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_delta/0AGNOSTIC.md" <<'EOFILE'
# 0AGNOSTIC.md - layer_1_feature_delta

## Identity

entity_id: "aaaa1111-1111-1111-1111-111111111111"

Duplicate UUID!
EOFILE
    run_sync "$ROOT" --rebuild-index
    assert_contains "21.7 Duplicate UUID → WARN" "$SYNC_OUTPUT" "Duplicate UUID"

    cleanup
}

# ============================================================
# Category 22: --find-references
# ============================================================

test_find_references() {
    echo -e "\n${BLUE}=== Category 22: --find-references ===${NC}"

    local ROOT

    # Test 22.1: Find references to a UUID used in a pointer
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_ref1.md" \
        "alpha ref" "aaaa1111-1111-1111-1111-111111111111"
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_ref2.md" \
        "alpha ref 2" "aaaa1111-1111-1111-1111-111111111111"
    run_sync "$ROOT" --find-references "aaaa1111-1111-1111-1111-111111111111"
    assert_contains "22.1a Finds ptr_ref1" "$SYNC_OUTPUT" "ptr_ref1.md"
    assert_contains "22.1b Finds ptr_ref2" "$SYNC_OUTPUT" "ptr_ref2.md"
    assert_contains "22.1c Reports 2 references" "$SYNC_OUTPUT" "2 reference(s)"

    cleanup

    # Test 22.2: UUID with no references → 0 found
    ROOT=$(setup_uuid_mock_repo)
    run_sync "$ROOT" --find-references "ffff9999-9999-9999-9999-999999999999"
    assert_contains "22.2 No references → 0 found" "$SYNC_OUTPUT" "0 reference(s)"

    cleanup

    # Test 22.3: Find references to a stage UUID
    ROOT=$(setup_uuid_mock_repo)
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_stage_ref.md" \
        "alpha design" "aaaa1111-1111-1111-1111-111111111111" "dddd4444-4444-4444-4444-444444444444"
    run_sync "$ROOT" --find-references "dddd4444-4444-4444-4444-444444444444"
    assert_contains "22.3 Stage UUID reference found" "$SYNC_OUTPUT" "ptr_stage_ref.md"

    cleanup
}

# ============================================================
# Category 23: --detect-cycles
# ============================================================

test_detect_cycles() {
    echo -e "\n${BLUE}=== Category 23: --detect-cycles ===${NC}"

    local ROOT

    # Test 23.1: No cycles → clean output
    ROOT=$(setup_uuid_mock_repo)
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_no_cycle.md" \
        "alpha" "aaaa1111-1111-1111-1111-111111111111"
    run_sync "$ROOT" --detect-cycles
    assert_contains "23.1 No cycles → clean" "$SYNC_OUTPUT" "No cycles detected"

    cleanup

    # Test 23.2: Exit 0 when no cycles
    ROOT=$(setup_uuid_mock_repo)
    run_sync "$ROOT" --detect-cycles
    assert_exit_code "23.2 No cycles → exit 0" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 24: --gc (Garbage Collection)
# ============================================================

test_garbage_collection() {
    echo -e "\n${BLUE}=== Category 24: --gc ===${NC}"

    local ROOT

    # Test 24.1: No orphaned entries → clean message
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    run_sync "$ROOT" --gc
    assert_contains "24.1 No orphans → clean" "$SYNC_OUTPUT" "No orphaned entries"
    assert_exit_code "24.1b Exit 0" "0" "$SYNC_EXIT"

    cleanup

    # Test 24.2: Orphaned entry is removed
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    # Remove alpha entity directory — its UUID becomes orphaned
    rm -rf "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha"
    run_sync "$ROOT" --gc
    assert_contains "24.2 Orphaned entry removed" "$SYNC_OUTPUT" "REMOVED"

    cleanup

    # Test 24.3: GC reduces index entry count
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    local before_count
    before_count=$(python3 -c "import json; print(len(json.load(open('$ROOT/.uuid-index.json')).get('uuids', {})))" 2>/dev/null)
    rm -rf "$ROOT/layer_1_group/layer_1_features/layer_1_feature_alpha"
    "$ROOT/.0agnostic/pointer-sync.sh" --gc > /dev/null 2>&1
    local after_count
    after_count=$(python3 -c "import json; print(len(json.load(open('$ROOT/.uuid-index.json')).get('uuids', {})))" 2>/dev/null)
    TOTAL=$((TOTAL + 1))
    if [ "$after_count" -lt "$before_count" ]; then
        echo -e "  ${GREEN}PASS${NC}: 24.3 GC reduced count ($before_count → $after_count)"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: 24.3 GC did not reduce count ($before_count → $after_count)"
        FAIL=$((FAIL + 1))
    fi

    cleanup

    # Test 24.4: GC without index → error
    ROOT=$(setup_uuid_mock_repo)
    run_sync "$ROOT" --gc
    assert_contains "24.4 GC without index → error message" "$SYNC_OUTPUT" "No UUID index"

    cleanup
}

# ============================================================
# Category 25: Index Locking
# ============================================================

test_index_locking() {
    echo -e "\n${BLUE}=== Category 25: Index Locking ===${NC}"

    local ROOT

    # Test 25.1: Lock is created and released during rebuild
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    TOTAL=$((TOTAL + 1))
    if [ ! -d "$ROOT/.uuid-index.json.lock" ]; then
        echo -e "  ${GREEN}PASS${NC}: 25.1 Lock released after rebuild"
        PASS=$((PASS + 1))
    else
        echo -e "  ${RED}FAIL${NC}: 25.1 Lock NOT released after rebuild"
        FAIL=$((FAIL + 1))
    fi

    cleanup

    # Test 25.2: Stale lock (>5 min old) is cleaned up
    ROOT=$(setup_uuid_mock_repo)
    # Create a fake stale lock
    mkdir -p "$ROOT/.uuid-index.json.lock"
    # Touch with old timestamp
    touch -t 202601010000 "$ROOT/.uuid-index.json.lock"
    run_sync "$ROOT" --rebuild-index
    assert_exit_code "25.2 Stale lock cleaned up → rebuild succeeds" "0" "$SYNC_EXIT"

    cleanup
}

# ============================================================
# Category 26: UUID + Name Fallback
# ============================================================

test_uuid_fallback() {
    echo -e "\n${BLUE}=== Category 26: UUID + Name Fallback ===${NC}"

    local ROOT content

    # Test 26.1: Pointer with both UUID and name → UUID takes precedence
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    mkdir -p "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma"
    cat > "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_both.md" <<'EOFILE'
---
pointer_to: alpha both
canonical_entity_id: aaaa1111-1111-1111-1111-111111111111
canonical_entity: layer_1_feature_alpha
---

# Both UUID and name

> **Canonical location**: `old/path`
EOFILE
    run_sync "$ROOT" --verbose
    assert_contains "26.1 UUID takes precedence over name" "$SYNC_OUTPUT" "Entity resolved via UUID"

    cleanup

    # Test 26.2: Name-only pointer still works (no UUID fields)
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_name_only.md" \
        "alpha legacy" "layer_1_feature_alpha" "" "" "old/path"
    run_sync "$ROOT" --verbose
    assert_contains "26.2 Name-only still resolves (legacy)" "$SYNC_OUTPUT" "Entity resolved via name"

    cleanup

    # Test 26.3: UUID auto-rebuild on index miss
    ROOT=$(setup_uuid_mock_repo)
    # Don't rebuild index — let the sync auto-build
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_auto.md" \
        "alpha auto" "aaaa1111-1111-1111-1111-111111111111" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "26.3 Auto-rebuild resolves UUID → exit 0" "0" "$SYNC_EXIT"

    cleanup

    # Test 26.4: Mixed UUID and name pointers in same run
    ROOT=$(setup_uuid_mock_repo)
    "$ROOT/.0agnostic/pointer-sync.sh" --rebuild-index > /dev/null 2>&1
    create_uuid_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_uuid_mix.md" \
        "alpha uuid" "aaaa1111-1111-1111-1111-111111111111" "" "" "old/path"
    create_pointer "$ROOT/layer_1_group/layer_1_features/layer_1_feature_gamma/ptr_name_mix.md" \
        "beta name" "layer_1_feature_beta" "" "" "old/path"
    "$ROOT/.0agnostic/pointer-sync.sh" > /dev/null 2>&1
    run_sync "$ROOT" --validate
    assert_exit_code "26.4 Mixed UUID+name pointers → all valid" "0" "$SYNC_EXIT"

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

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "idempotency" ]; then
    test_idempotency
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "spaces" ]; then
    test_spaces_in_paths
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "duplicates" ]; then
    test_duplicate_entities
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "filesubpath" ]; then
    test_file_subpath
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "comboflags" ]; then
    test_combination_flags
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "python3" ]; then
    test_python3_dependency
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "symlinks" ]; then
    test_symlinks
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "longpaths" ]; then
    test_long_paths
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "nonmarkdown" ]; then
    test_non_markdown_files
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "multitarget" ]; then
    test_multiple_pointers_same_target
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "extrafm" ]; then
    test_extra_frontmatter
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "awkreplace" ]; then
    test_awk_replacement
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "uuidresolution" ]; then
    test_uuid_resolution
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "rebuildindex" ]; then
    test_rebuild_index
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "findreferences" ]; then
    test_find_references
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "detectcycles" ]; then
    test_detect_cycles
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "garbagecollection" ]; then
    test_garbage_collection
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "indexlocking" ]; then
    test_index_locking
fi

if [ -z "$CATEGORY_FILTER" ] || [ "$CATEGORY_FILTER" = "uuidfallback" ]; then
    test_uuid_fallback
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
