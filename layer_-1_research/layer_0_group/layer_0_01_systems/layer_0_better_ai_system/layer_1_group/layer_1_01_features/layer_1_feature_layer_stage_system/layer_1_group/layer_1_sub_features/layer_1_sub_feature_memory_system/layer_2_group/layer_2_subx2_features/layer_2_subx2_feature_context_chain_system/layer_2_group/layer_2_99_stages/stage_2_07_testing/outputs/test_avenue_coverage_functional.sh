#!/usr/bin/env bash
# resource_id: "479449a0-0384-4877-a2da-b13a19f77421"
# resource_type: "script"
# resource_name: "test_avenue_coverage_functional"
# test_avenue_coverage_functional.sh — Test 8 avenues are FUNCTIONALLY available
#
# Goes beyond file existence (structural validation) to check content quality.
# Reports three states per avenue:
#   PASS       — Avenue is functional (has real content)
#   SCAFFOLDED — Avenue structure exists but content is empty/minimal
#   FAIL       — Avenue structure is missing
#
# Avenues tested:
#   A1: System Prompt (CLAUDE.md)
#   A2: Path Rules (.claude/rules/)
#   A3: Skills (.0agnostic/05_skills/ or legacy .0agnostic/skills/)
#   A4: References (parent ref in 0AGNOSTIC.md)
#   A5: JSON-LD (.gab.jsonld)
#   A6: Integration (.integration.md)
#   A7: Episodic Memory (.0agnostic/07_episodic_memory/ or legacy .0agnostic/episodic_memory/)
#   A8: 0AGNOSTIC (0AGNOSTIC.md)

set -uo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"

# --- Counters ---
PASS=0
SCAFFOLDED=0
FAIL=0

pass()       { ((PASS++))       || true; printf "  \033[32mPASS\033[0m       %s\n" "$1"; }
scaffolded() { ((SCAFFOLDED++)) || true; printf "  \033[33mSCAFFOLDED\033[0m %s\n" "$1"; }
fail()       { ((FAIL++))       || true; printf "  \033[31mFAIL\033[0m       %s\n" "$1"; }

# Utility: count non-empty, non-gitkeep lines in a file
content_lines() {
    if [ -f "$1" ]; then
        grep -cvP '^\s*$' "$1" 2>/dev/null | head -1
    else
        echo "0"
    fi
}

# Utility: count non-gitkeep files in a directory
real_files() {
    if [ -d "$1" ]; then
        find "$1" -type f ! -name ".gitkeep" 2>/dev/null | wc -l
    else
        echo "0"
    fi
}

# Utility: resolve first existing directory from candidates
resolve_dir() {
    local candidate
    for candidate in "$@"; do
        if [ -d "$candidate" ]; then
            echo "$candidate"
            return 0
        fi
    done
    return 1
}

echo "=== Test: Avenue Coverage (Functional) ==="
echo "Entity: $(basename "$ENTITY_ROOT")"
echo ""

# --- A1: System Prompt (CLAUDE.md) ---
echo "--- A1: System Prompt (CLAUDE.md) ---"

if [ -f "$ENTITY_ROOT/CLAUDE.md" ]; then
    lines=$(content_lines "$ENTITY_ROOT/CLAUDE.md")
    if [ "$lines" -gt 10 ]; then
        pass "A1: CLAUDE.md has $lines lines of content"
    else
        scaffolded "A1: CLAUDE.md exists but minimal ($lines lines)"
    fi

    # Check for meaningful sections
    if grep -q "## Identity" "$ENTITY_ROOT/CLAUDE.md"; then
        pass "A1: CLAUDE.md has Identity section"
    else
        scaffolded "A1: CLAUDE.md missing Identity section"
    fi
else
    fail "A1: CLAUDE.md does not exist"
fi

# --- A2: Path Rules (.claude/rules/) ---
echo ""
echo "--- A2: Path Rules (.claude/rules/) ---"

if [ -d "$ENTITY_ROOT/.claude/rules" ]; then
    rule_files=$(find "$ENTITY_ROOT/.claude/rules" -name "*.md" -type f 2>/dev/null | wc -l)
    if [ "$rule_files" -gt 0 ]; then
        pass "A2: .claude/rules/ has $rule_files .md files"
        # Check if rules have content
        total_rule_lines=0
        while IFS= read -r rf; do
            rl=$(content_lines "$rf")
            total_rule_lines=$((total_rule_lines + rl))
        done < <(find "$ENTITY_ROOT/.claude/rules" -name "*.md" -type f 2>/dev/null)
        if [ "$total_rule_lines" -gt 5 ]; then
            pass "A2: Rules have $total_rule_lines lines of content"
        else
            scaffolded "A2: Rules exist but minimal content ($total_rule_lines lines)"
        fi
    else
        scaffolded "A2: .claude/rules/ exists but no .md files"
    fi
else
    fail "A2: .claude/rules/ directory missing"
fi

# --- A3: Skills (.0agnostic/05_skills/) ---
echo ""
echo "--- A3: Skills (.0agnostic/05_skills/) ---"

SKILLS_DIR="$(resolve_dir "$ENTITY_ROOT/.0agnostic/05_skills" "$ENTITY_ROOT/.0agnostic/skills" || true)"
if [ -n "$SKILLS_DIR" ]; then
    skill_files=$(find "$SKILLS_DIR" -name "SKILL.md" -type f 2>/dev/null | wc -l)
    if [ "$skill_files" -gt 0 ]; then
        pass "A3: $(basename "$SKILLS_DIR") has $skill_files SKILL.md files"
    else
        # Check for any files at all
        any_files=$(real_files "$SKILLS_DIR")
        if [ "$any_files" -gt 0 ]; then
            scaffolded "A3: $(basename "$SKILLS_DIR") has files but no SKILL.md"
        else
            scaffolded "A3: $(basename "$SKILLS_DIR") exists but is empty"
        fi
    fi
else
    fail "A3: skills directory missing (.0agnostic/05_skills or .0agnostic/skills)"
fi

# --- A4: References (parent ref in 0AGNOSTIC.md) ---
echo ""
echo "--- A4: References (parent chain) ---"

if [ -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    parent_ref=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$ENTITY_ROOT/0AGNOSTIC.md" | head -1)
    if [ -n "$parent_ref" ]; then
        # Resolve the reference
        resolved="$(cd "$ENTITY_ROOT" && cd "$(dirname "$parent_ref")" 2>/dev/null && pwd)/$(basename "$parent_ref")"
        if [ -f "$resolved" ]; then
            pass "A4: Parent reference resolves ($parent_ref)"
        else
            fail "A4: Parent reference broken ($parent_ref)"
        fi
    else
        fail "A4: No **Parent** reference in 0AGNOSTIC.md"
    fi

    # Check for children references
    if grep -q "\*\*Children\*\*:" "$ENTITY_ROOT/0AGNOSTIC.md"; then
        pass "A4: Children references documented"
    else
        scaffolded "A4: No Children references"
    fi
else
    fail "A4: 0AGNOSTIC.md missing (cannot check references)"
fi

# --- A5: JSON-LD (.gab.jsonld) ---
echo ""
echo "--- A5: JSON-LD (.gab.jsonld) ---"

gab_files=$(find "$ENTITY_ROOT" -maxdepth 1 -name "*.gab.jsonld" -type f 2>/dev/null)
gab_count=$(echo "$gab_files" | grep -c . 2>/dev/null || echo "0")

if [ "$gab_count" -gt 0 ]; then
    pass "A5: $gab_count .gab.jsonld file(s) found"

    # Validate JSON structure
    while IFS= read -r gf; do
        [ -z "$gf" ] && continue
        gf_name=$(basename "$gf")
        if command -v jq &>/dev/null; then
            if jq empty "$gf" 2>/dev/null; then
                pass "A5: $gf_name is valid JSON"

                # Check for GAB structure (@graph)
                has_graph=$(jq 'has("@graph")' "$gf" 2>/dev/null)
                if [ "$has_graph" = "true" ]; then
                    pass "A5: $gf_name has @graph (GAB-compliant)"

                    # Check for Mode definitions
                    mode_count=$(jq '[."@graph"[] | select(."@type" == "gab:Mode")] | length' "$gf" 2>/dev/null || echo "0")
                    if [ "$mode_count" -gt 0 ]; then
                        pass "A5: $gf_name has $mode_count modes"
                    else
                        scaffolded "A5: $gf_name has no modes defined"
                    fi
                else
                    scaffolded "A5: $gf_name missing @graph (stub, not full GAB)"
                fi
            else
                fail "A5: $gf_name is NOT valid JSON"
            fi
        else
            scaffolded "A5: jq not available — cannot validate JSON structure"
        fi
    done <<< "$gab_files"
else
    fail "A5: No .gab.jsonld files at entity root"
fi

# --- A6: Integration (.integration.md) ---
echo ""
echo "--- A6: Integration (.integration.md) ---"

integ_files=$(find "$ENTITY_ROOT" -maxdepth 1 -name "*.integration.md" -type f 2>/dev/null)
integ_count=$(echo "$integ_files" | grep -c . 2>/dev/null || echo "0")

if [ "$integ_count" -gt 0 ]; then
    while IFS= read -r inf; do
        [ -z "$inf" ] && continue
        inf_name=$(basename "$inf")
        lines=$(content_lines "$inf")
        if [ "$lines" -gt 5 ]; then
            pass "A6: $inf_name has $lines lines of content"
        else
            scaffolded "A6: $inf_name exists but minimal ($lines lines)"
        fi
    done <<< "$integ_files"
else
    # Check if there's a matching .gab.jsonld that should have an integration
    if [ "$gab_count" -gt 0 ]; then
        fail "A6: .gab.jsonld exists but no matching .integration.md"
    else
        scaffolded "A6: No .integration.md (and no .gab.jsonld to match)"
    fi
fi

# --- A7: Episodic Memory (.0agnostic/07_episodic_memory/) ---
echo ""
echo "--- A7: Episodic Memory ---"

EPISODIC_DIR="$(resolve_dir "$ENTITY_ROOT/.0agnostic/07_episodic_memory" "$ENTITY_ROOT/.0agnostic/episodic_memory" || true)"
if [ -n "$EPISODIC_DIR" ]; then
    pass "A7: $(basename "$EPISODIC_DIR") exists"

    # Check sessions subdirectory
    if [ -d "$EPISODIC_DIR/sessions" ]; then
        session_files=$(real_files "$EPISODIC_DIR/sessions")
        if [ "$session_files" -gt 0 ]; then
            pass "A7: sessions/ has $session_files files"
        else
            scaffolded "A7: sessions/ exists but is empty"
        fi
    else
        fail "A7: sessions/ subdirectory missing"
    fi

    # Check changes subdirectory
    if [ -d "$EPISODIC_DIR/changes" ]; then
        change_files=$(real_files "$EPISODIC_DIR/changes")
        if [ "$change_files" -gt 0 ]; then
            pass "A7: changes/ has $change_files files"
        else
            scaffolded "A7: changes/ exists but is empty"
        fi
    else
        fail "A7: changes/ subdirectory missing"
    fi
else
    fail "A7: episodic memory directory missing (.0agnostic/07_episodic_memory or .0agnostic/episodic_memory)"
fi

# --- A8: 0AGNOSTIC (0AGNOSTIC.md) ---
echo ""
echo "--- A8: 0AGNOSTIC Source ---"

if [ -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    lines=$(content_lines "$ENTITY_ROOT/0AGNOSTIC.md")
    if [ "$lines" -gt 5 ]; then
        pass "A8: 0AGNOSTIC.md has $lines lines of content"
    else
        scaffolded "A8: 0AGNOSTIC.md exists but minimal ($lines lines)"
    fi

    # Check for required Identity section
    if grep -q "## Identity" "$ENTITY_ROOT/0AGNOSTIC.md"; then
        pass "A8: 0AGNOSTIC.md has Identity section"
    else
        fail "A8: 0AGNOSTIC.md missing Identity section"
    fi

    # Check for Navigation or Pointers section
    if grep -qP "## (Navigation|Pointers)" "$ENTITY_ROOT/0AGNOSTIC.md"; then
        pass "A8: 0AGNOSTIC.md has Navigation/Pointers section"
    else
        scaffolded "A8: 0AGNOSTIC.md missing Navigation/Pointers"
    fi
else
    fail "A8: 0AGNOSTIC.md does not exist"
fi

# --- Summary ---
echo ""
echo "================================"
printf "  \033[32mPASS\033[0m:       %d\n" "$PASS"
printf "  \033[33mSCAFFOLDED\033[0m: %d\n" "$SCAFFOLDED"
printf "  \033[31mFAIL\033[0m:       %d\n" "$FAIL"
echo "================================"

TOTAL=$((PASS + SCAFFOLDED + FAIL))
if [ "$TOTAL" -gt 0 ]; then
    PCT=$((PASS * 100 / TOTAL))
    echo "  Functional coverage: ${PCT}%"
    echo "  (PASS=$PASS, SCAFFOLDED=$SCAFFOLDED need content, FAIL=$FAIL need fixing)"
fi

[ "$FAIL" -eq 0 ] && exit 0 || exit 1
