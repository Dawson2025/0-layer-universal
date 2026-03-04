#!/usr/bin/env bash
# test_instantiation_readiness.sh — Pre-flight checklist for entity instantiation
#
# Checks whether this entity is READY to be populated with real content.
# Reports: READY / NOT READY with specific items to fix.
#
# Pre-flight checks:
#   1. 0AGNOSTIC.md exists with required sections
#   2. agnostic-sync.sh is accessible and executable
#   3. .0agnostic/ has all required subdirectories
#   4. .1merge/ has all tool directories with 3-tier structure
#   5. .claude/, .cursor/, .gemini/, .github/, .codex/ directories exist
#   6. .gab.jsonld exists (even if minimal)
#   7. .integration.md exists (even if minimal)
#   8. Parent chain is intact (at least 2 parent 0AGNOSTIC.md files reachable)

set -uo pipefail

# --- Paths ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENTITY_ROOT="$(cd "$SCRIPT_DIR/../../../../" && pwd)"
REPO_ROOT="$(cd "$ENTITY_ROOT" && git rev-parse --show-toplevel 2>/dev/null)"
[ -z "$REPO_ROOT" ] && REPO_ROOT="$(cd "$ENTITY_ROOT/../../../../../../../../../../../" && pwd)"
SYNC_SCRIPT="$REPO_ROOT/.0agnostic/agnostic-sync.sh"

# --- Counters ---
READY=0
NOT_READY=0
WARN=0

ready()     { ((READY++))     || true; printf "  \033[32mREADY\033[0m      %s\n" "$1"; }
not_ready() { ((NOT_READY++)) || true; printf "  \033[31mNOT READY\033[0m  %s\n" "$1"; }
warn_()     { ((WARN++))      || true; printf "  \033[33mWARN\033[0m       %s\n" "$1"; }

# Return first existing directory from a set of candidates.
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

echo "=== Test: Instantiation Readiness ==="
echo "Entity: $(basename "$ENTITY_ROOT")"
echo "Path: $ENTITY_ROOT"
echo ""

# --- Check 1: 0AGNOSTIC.md ---
echo "--- Check 1: 0AGNOSTIC.md ---"

if [ -f "$ENTITY_ROOT/0AGNOSTIC.md" ]; then
    ready "0AGNOSTIC.md exists"

    # Required section: Identity
    if grep -q "## Identity" "$ENTITY_ROOT/0AGNOSTIC.md"; then
        ready "Has ## Identity section"
    else
        not_ready "Missing ## Identity section"
    fi

    # Check for parent reference
    if grep -qP '\*\*Parent\*\*:' "$ENTITY_ROOT/0AGNOSTIC.md"; then
        ready "Has parent reference"
    else
        not_ready "Missing **Parent** reference"
    fi
else
    not_ready "0AGNOSTIC.md does not exist"
fi

# --- Check 2: agnostic-sync.sh ---
echo ""
echo "--- Check 2: agnostic-sync.sh ---"

if [ -f "$SYNC_SCRIPT" ]; then
    ready "agnostic-sync.sh found at $SYNC_SCRIPT"

    if [ -x "$SYNC_SCRIPT" ]; then
        ready "agnostic-sync.sh is executable"
    else
        not_ready "agnostic-sync.sh is not executable"
    fi
else
    # Try to find it in parent chain
    found_sync=false
    check="$ENTITY_ROOT"
    while [ "${#check}" -gt 1 ]; do
        if [ -f "$check/.0agnostic/agnostic-sync.sh" ]; then
            ready "agnostic-sync.sh found at $check/.0agnostic/"
            found_sync=true
            break
        fi
        check="$(dirname "$check")"
    done
    if [ "$found_sync" = false ]; then
        not_ready "agnostic-sync.sh not found in any parent"
    fi
fi

# --- Check 3: .0agnostic/ subdirectories ---
echo ""
echo "--- Check 3: .0agnostic/ structure ---"

AGNOSTIC_DIR="$ENTITY_ROOT/.0agnostic"

if [ -d "$AGNOSTIC_DIR" ]; then
    ready ".0agnostic/ directory exists"
    # Numbered-first with legacy fallback.
    KNOWLEDGE_DIR="$(resolve_dir "$AGNOSTIC_DIR/01_knowledge" "$AGNOSTIC_DIR/knowledge" || true)"
    RULES_DIR="$(resolve_dir "$AGNOSTIC_DIR/02_rules" "$AGNOSTIC_DIR/rules" || true)"
    PROTOCOLS_DIR="$(resolve_dir "$AGNOSTIC_DIR/03_protocols" "$AGNOSTIC_DIR/protocols" || true)"
    AGENTS_DIR="$(resolve_dir "$AGNOSTIC_DIR/04_agents" "$AGNOSTIC_DIR/agents" || true)"
    SKILLS_DIR="$(resolve_dir "$AGNOSTIC_DIR/05_skills" "$AGNOSTIC_DIR/skills" || true)"
    HOOKS_DIR="$(resolve_dir "$AGNOSTIC_DIR/06_hooks" "$AGNOSTIC_DIR/hooks" || true)"
    EPISODIC_DIR="$(resolve_dir "$AGNOSTIC_DIR/07_episodic_memory" "$AGNOSTIC_DIR/episodic_memory" || true)"

    if [ -n "$KNOWLEDGE_DIR" ]; then
        ready ".0agnostic/$(basename "$KNOWLEDGE_DIR")/"
    else
        not_ready ".0agnostic/01_knowledge (or legacy knowledge/) missing"
    fi

    if [ -n "$RULES_DIR" ]; then
        ready ".0agnostic/$(basename "$RULES_DIR")/"
    else
        not_ready ".0agnostic/02_rules (or legacy rules/) missing"
    fi

    if [ -n "$PROTOCOLS_DIR" ]; then
        ready ".0agnostic/$(basename "$PROTOCOLS_DIR")/"
    else
        warn_ ".0agnostic/03_protocols (or legacy protocols/) missing"
    fi

    if [ -n "$AGENTS_DIR" ]; then
        ready ".0agnostic/$(basename "$AGENTS_DIR")/"
    else
        not_ready ".0agnostic/04_agents (or legacy agents/) missing"
    fi

    if [ -n "$SKILLS_DIR" ]; then
        ready ".0agnostic/$(basename "$SKILLS_DIR")/"
    else
        not_ready ".0agnostic/05_skills (or legacy skills/) missing"
    fi

    if [ -n "$HOOKS_DIR" ]; then
        ready ".0agnostic/$(basename "$HOOKS_DIR")/"
    else
        not_ready ".0agnostic/06_hooks (or legacy hooks/) missing"
    fi

    if [ -n "$EPISODIC_DIR" ]; then
        ready ".0agnostic/$(basename "$EPISODIC_DIR")/"
        if [ -d "$EPISODIC_DIR/sessions" ]; then
            ready ".0agnostic/$(basename "$EPISODIC_DIR")/sessions/"
        else
            not_ready ".0agnostic/$(basename "$EPISODIC_DIR")/sessions/ missing"
        fi

        if [ -d "$EPISODIC_DIR/changes" ]; then
            ready ".0agnostic/$(basename "$EPISODIC_DIR")/changes/"
        else
            not_ready ".0agnostic/$(basename "$EPISODIC_DIR")/changes/ missing"
        fi
    else
        not_ready ".0agnostic/07_episodic_memory (or legacy episodic_memory/) missing"
    fi

    if [ -n "$HOOKS_DIR" ] && [ -d "$HOOKS_DIR/scripts" ]; then
        ready ".0agnostic/$(basename "$HOOKS_DIR")/scripts/"
    else
        not_ready ".0agnostic/06_hooks/scripts (or legacy hooks/scripts) missing"
    fi
else
    not_ready ".0agnostic/ directory does not exist"
fi

# --- Check 4: .1merge/ structure ---
echo ""
echo "--- Check 4: .1merge/ structure ---"

MERGE_DIR="$ENTITY_ROOT/.1merge"
TOOLS=(.1claude_merge .1cursor_merge .1gemini_merge .1aider_merge .1codex_merge .1copilot_merge)
TIERS=(0_synced 1_overrides 2_additions)

if [ -d "$MERGE_DIR" ]; then
    ready ".1merge/ directory exists"

    merge_ok=true
    for tool in "${TOOLS[@]}"; do
        for tier in "${TIERS[@]}"; do
            if [ ! -d "$MERGE_DIR/$tool/$tier" ]; then
                not_ready ".1merge/$tool/$tier/ missing"
                merge_ok=false
            fi
        done
    done

    if [ "$merge_ok" = true ]; then
        ready "All ${#TOOLS[@]} tools × ${#TIERS[@]} tiers present"
    fi
else
    not_ready ".1merge/ directory does not exist"
fi

# --- Check 5: Tool config directories ---
echo ""
echo "--- Check 5: Tool config directories ---"

TOOL_DIRS=(.claude .cursor .gemini .codex .github)

for td in "${TOOL_DIRS[@]}"; do
    if [ -d "$ENTITY_ROOT/$td" ]; then
        ready "$td/ exists"
    else
        not_ready "$td/ missing"
    fi
done

# Check .claude/rules specifically
if [ -d "$ENTITY_ROOT/.claude/rules" ]; then
    ready ".claude/rules/ exists"
else
    not_ready ".claude/rules/ missing"
fi

# --- Check 6: .gab.jsonld ---
echo ""
echo "--- Check 6: Orchestrator (.gab.jsonld) ---"

gab_count=$(find "$ENTITY_ROOT" -maxdepth 1 -name "*.gab.jsonld" -type f 2>/dev/null | wc -l)

if [ "$gab_count" -gt 0 ]; then
    ready "$gab_count .gab.jsonld file(s) found"

    # Validate JSON
    if command -v jq &>/dev/null; then
        for gf in "$ENTITY_ROOT"/*.gab.jsonld; do
            [ ! -f "$gf" ] && continue
            if jq empty "$gf" 2>/dev/null; then
                ready "$(basename "$gf") is valid JSON"
            else
                not_ready "$(basename "$gf") has invalid JSON"
            fi
        done
    else
        warn_ "jq not available — cannot validate JSON"
    fi
else
    not_ready "No .gab.jsonld at entity root"
fi

# --- Check 7: .integration.md ---
echo ""
echo "--- Check 7: Integration summary (.integration.md) ---"

integ_count=$(find "$ENTITY_ROOT" -maxdepth 1 -name "*.integration.md" -type f 2>/dev/null | wc -l)

if [ "$integ_count" -gt 0 ]; then
    ready "$integ_count .integration.md file(s) found"
else
    if [ "$gab_count" -gt 0 ]; then
        not_ready ".gab.jsonld exists but no matching .integration.md"
    else
        warn_ "No .integration.md (and no .gab.jsonld to match)"
    fi
fi

# --- Check 8: Parent chain integrity ---
echo ""
echo "--- Check 8: Parent chain ---"

parent_count=0
current="$ENTITY_ROOT"

while true; do
    [ ! -f "$current/0AGNOSTIC.md" ] && break
    pref=$(grep -oP '(?<=\*\*Parent\*\*: `)[^`]+' "$current/0AGNOSTIC.md" | head -1)
    [ -z "$pref" ] && break

    resolved="$(cd "$current" && cd "$(dirname "$pref")" 2>/dev/null && pwd)/$(basename "$pref")"
    if [ -f "$resolved" ]; then
        parent_count=$((parent_count + 1))
        current="$(dirname "$resolved")"
    else
        not_ready "Broken parent reference at $(basename "$current")"
        break
    fi
done

if [ $parent_count -ge 2 ]; then
    ready "Parent chain has $parent_count ancestors (>= 2)"
else
    not_ready "Parent chain has only $parent_count ancestors (need >= 2)"
fi

# --- Check 9: Internal layer_N_group ---
echo ""
echo "--- Check 9: Internal structure ---"

group_dir=$(find "$ENTITY_ROOT" -maxdepth 1 -type d -name "layer_*_group" 2>/dev/null | head -1)

if [ -n "$group_dir" ]; then
    ready "$(basename "$group_dir")/ exists"

    # Check stages
    layer_num=$(basename "$group_dir" | grep -oP 'layer_\K[0-9]+')
    stages_dir="$group_dir/layer_${layer_num}_99_stages"
    if [ -d "$stages_dir" ]; then
        ready "Stages directory exists"
        stage_count=$(find "$stages_dir" -maxdepth 1 -type d -name "stage_*" 2>/dev/null | wc -l)
        if [ "$stage_count" -ge 12 ]; then
            ready "$stage_count stages present (>= 12)"
        else
            warn_ "$stage_count stages (expected >= 12)"
        fi
    else
        not_ready "Stages directory missing"
    fi
else
    not_ready "No layer_N_group/ directory"
fi

# --- Check 10: Generated tool files ---
echo ""
echo "--- Check 10: Generated tool files ---"

for f in CLAUDE.md AGENTS.md GEMINI.md OPENAI.md; do
    if [ -f "$ENTITY_ROOT/$f" ]; then
        ready "$f exists"
    else
        warn_ "$f not yet generated (run agnostic-sync.sh)"
    fi
done

# --- Final Verdict ---
echo ""
echo "================================"
printf "  \033[32mREADY\033[0m:      %d\n" "$READY"
printf "  \033[31mNOT READY\033[0m:  %d\n" "$NOT_READY"
printf "  \033[33mWARN\033[0m:       %d\n" "$WARN"
echo "================================"

if [ "$NOT_READY" -eq 0 ]; then
    echo ""
    printf "  \033[32m>>> ENTITY IS READY FOR INSTANTIATION <<<\033[0m\n"
    echo ""
    echo "  Next steps:"
    echo "    1. Populate .0agnostic/ with rules, knowledge, skills"
    echo "    2. Create .claude/rules/ path rules"
    echo "    3. Flesh out .gab.jsonld with modes, actors, personas"
    echo "    4. Generate .integration.md from .gab.jsonld"
    echo "    5. Run agnostic-sync.sh to regenerate tool files"
    echo "    6. Re-run this test to verify PASS on all checks"
    exit 0
else
    echo ""
    printf "  \033[31m>>> ENTITY IS NOT READY — %d items need fixing <<<\033[0m\n" "$NOT_READY"
    echo ""
    echo "  Fix all NOT READY items before attempting instantiation."
    exit 1
fi
