#!/bin/bash
# resource_id: "781698fa-f580-4606-80e4-dc73fb30e3f7"
# resource_type: "script"
# resource_name: "agnostic-sync"
#
# agnostic-sync.sh v2 — Transform 0AGNOSTIC.md into tool-specific context files
#
# Usage: ./agnostic-sync.sh [directory]
#        If no directory specified, uses current directory
#
# Generates:
#   - CLAUDE.md      (Claude Code — full STATIC content)
#   - AGENTS.md      (AutoGen / Codex — full STATIC content)
#   - GEMINI.md      (Google Gemini — full STATIC content)
#   - OPENAI.md      (OpenAI — full STATIC content)
#   - .cursorrules   (Cursor IDE — lean: Identity + Navigation)
#   - .github/copilot-instructions.md (GitHub Copilot — medium)
#
# Supports three 0AGNOSTIC.md formats:
#   - New: Has # ═══ STATIC CONTEXT / # ═══ DYNAMIC CONTEXT markers
#   - Old: Has ## sections but no markers
#   - Minimal: Short container files
#
# Integrates .1merge/ for tool-specific overrides:
#   - .1merge/.1{tool}_merge/1_overrides/tool_boilerplate.md → replaces default
#   - .1merge/.1{tool}_merge/2_additions/tool_additions.md → appended
#

set -e

DIR="${1:-.}"

if [ ! -f "$DIR/0AGNOSTIC.md" ]; then
    echo "Error: 0AGNOSTIC.md not found in $DIR"
    exit 1
fi

echo "Processing 0AGNOSTIC.md in $DIR..."

# ═══════════════════════════════════════════════
# Format Detection
# ═══════════════════════════════════════════════

FORMAT="minimal"
if grep -q '^# ═══ STATIC CONTEXT' "$DIR/0AGNOSTIC.md"; then
    FORMAT="new"
elif grep -q '^## ' "$DIR/0AGNOSTIC.md"; then
    FORMAT="old"
fi
echo "Detected format: $FORMAT"

# ═══════════════════════════════════════════════
# Content Extraction
# ═══════════════════════════════════════════════

# Extract ALL STATIC content from 0AGNOSTIC.md
# - New format: everything between STATIC and DYNAMIC markers
#   Strips: title line, marker lines, sub-group markers (# ── ... ──)
#   Keeps: ALL ## sections (Identity, Key Behaviors, Inputs, Outputs, Triggers, Current Status, etc.)
# - Old format: everything except title line
# - Minimal: entire file
case "$FORMAT" in
    new)
        STATIC_CONTENT=$(awk '
            /^# ═══ STATIC CONTEXT/ { in_static=1; next }
            /^# ═══ DYNAMIC CONTEXT/ { exit }
            in_static && /^# ── .* ──/ { next }
            in_static { print }
        ' "$DIR/0AGNOSTIC.md")
        ;;
    old)
        STATIC_CONTENT=$(awk 'NR==1 && /^# / { next } { print }' "$DIR/0AGNOSTIC.md")
        ;;
    minimal)
        STATIC_CONTENT=$(cat "$DIR/0AGNOSTIC.md")
        ;;
esac

# Trim leading blank lines from STATIC_CONTENT
STATIC_CONTENT=$(echo "$STATIC_CONTENT" | sed '/./,$!d')

# ═══════════════════════════════════════════════
# Hot Rule Promotion
# ═══════════════════════════════════════════════
# Rules with `promote: hot` frontmatter get a summary pointer injected
# into ALL generated tool files. Full rule stays in cold storage.
# See: .0agnostic/02_rules/static/agnostic_update_protocol.md

PROMOTED_RULES=""
if [ -d "$DIR/.0agnostic/02_rules" ]; then
    RULE_ENTRIES=""
    for rule_file in "$DIR"/.0agnostic/02_rules/static/*/*.md "$DIR"/.0agnostic/02_rules/dynamic/*/*.md "$DIR"/.0agnostic/02_rules/0_every_api_request/*/*.md; do
        [ -f "$rule_file" ] || continue
        if head -10 "$rule_file" | grep -q 'promote: hot'; then
            HOT_SUMMARY=$(head -10 "$rule_file" | sed -n 's/^hot_summary: *"\(.*\)"/\1/p')
            HOT_TRIGGER=$(head -10 "$rule_file" | sed -n 's/^hot_trigger: *"\(.*\)"/\1/p')
            if [ -n "$HOT_SUMMARY" ] && [ -n "$HOT_TRIGGER" ]; then
                RULE_ENTRIES="${RULE_ENTRIES}| ${HOT_TRIGGER} | ${HOT_SUMMARY} |
"
            fi
        fi
    done
    if [ -n "$RULE_ENTRIES" ]; then
        PROMOTED_RULES="
## Promoted Rules

| When | Rule |
|------|------|
${RULE_ENTRIES}"
    fi
fi

# ═══════════════════════════════════════════════
# Validation
# ═══════════════════════════════════════════════

STATIC_LEN=${#STATIC_CONTENT}
if [ "$STATIC_LEN" -lt 20 ]; then
    echo "WARNING: STATIC content is very short ($STATIC_LEN chars). Check 0AGNOSTIC.md format."
fi

if [ "$FORMAT" != "minimal" ] && ! echo "$STATIC_CONTENT" | grep -q '^## Identity'; then
    echo "WARNING: ## Identity section not found in STATIC content"
fi

# ═══════════════════════════════════════════════
# Section Extraction (for lean/medium formats)
# ═══════════════════════════════════════════════

# Extract specific named ## sections from content
# Usage: extract_named_sections "$content" "Identity|Navigation|Triggers"
# Section names are pipe-separated to support multi-word names like "Key Behaviors"
extract_named_sections() {
    local content="$1"
    local names="$2"

    echo "$content" | awk -v names="$names" '
        BEGIN { n = split(names, arr, "|") }
        /^## [^#]/ {
            printing = 0
            section = substr($0, 4)
            for (i = 1; i <= n; i++) {
                if (section == arr[i]) { printing = 1; break }
            }
        }
        printing { print }
    '
}

# ═══════════════════════════════════════════════
# .1merge Integration
# ═══════════════════════════════════════════════

# Return candidate merge directories for a tool.
# AGENTS.md is consumed by Codex and AutoGen, so it supports both
# .1agents_merge and .1codex_merge (in that precedence order).
get_tool_merge_dirs() {
    local tool="$1"
    if [ "$tool" = "agents" ]; then
        echo "$DIR/.1merge/.1agents_merge"
        echo "$DIR/.1merge/.1codex_merge"
    else
        echo "$DIR/.1merge/.1${tool}_merge"
    fi
}

# Check for tool-specific boilerplate override.
# Returns 0 and prints content if override exists, returns 1 otherwise.
get_tool_boilerplate() {
    local tool="$1"
    local merge_dir=""
    while IFS= read -r merge_dir; do
        [ -z "$merge_dir" ] && continue
        if [ -f "$merge_dir/1_overrides/tool_boilerplate.md" ]; then
            cat "$merge_dir/1_overrides/tool_boilerplate.md"
            return 0
        fi
    done < <(get_tool_merge_dirs "$tool")
    return 1
}

# Check for tool-specific additions (always appended).
get_tool_additions() {
    local tool="$1"
    local merge_dir=""
    while IFS= read -r merge_dir; do
        [ -z "$merge_dir" ] && continue
        if [ -f "$merge_dir/2_additions/tool_additions.md" ]; then
            echo ""
            cat "$merge_dir/2_additions/tool_additions.md"
            return 0
        fi
    done < <(get_tool_merge_dirs "$tool")
}

# ═══════════════════════════════════════════════
# Generation Functions
# ═══════════════════════════════════════════════

# Generate a full context file (all STATIC content + tool boilerplate)
# Used for: CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md
generate_full() {
    local file="$1"
    local title="$2"
    local tool="$3"
    local default_bp="$4"

    {
        echo "# $title"
        echo ""
        echo "$STATIC_CONTENT"
        # Promoted rules (from hot frontmatter)
        if [ -n "$PROMOTED_RULES" ]; then
            echo "$PROMOTED_RULES"
        fi
        echo ""
        # Tool-specific boilerplate (from .1merge override or default)
        if ! get_tool_boilerplate "$tool" 2>/dev/null; then
            echo "$default_bp"
        fi
        # Tool-specific additions (from .1merge, if any)
        get_tool_additions "$tool" 2>/dev/null
        echo ""
        echo "---"
        echo "*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*"
        echo "*Do not edit directly - edit 0AGNOSTIC.md instead*"
    } > "$file"

    echo "Generated: $file"
}

# Generate a lean context file (selected sections only + tool boilerplate)
# Used for: .cursorrules, .github/copilot-instructions.md
generate_lean() {
    local file="$1"
    local title="$2"
    local tool="$3"
    local sections="$4"  # pipe-separated, e.g. "Identity|Navigation"

    {
        echo "# $title"
        echo ""
        extract_named_sections "$STATIC_CONTENT" "$sections"
        # Promoted rules (from hot frontmatter)
        if [ -n "$PROMOTED_RULES" ]; then
            echo "$PROMOTED_RULES"
        fi
        echo ""
        # Tool-specific boilerplate
        get_tool_boilerplate "$tool" 2>/dev/null || true
        # Tool-specific additions
        get_tool_additions "$tool" 2>/dev/null
        echo ""
        echo "---"
        echo "*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*"
        echo "*Do not edit directly - edit 0AGNOSTIC.md instead*"
    } > "$file"

    echo "Generated: $file"
}

# ═══════════════════════════════════════════════
# Default Boilerplates (used when no .1merge override exists)
# ═══════════════════════════════════════════════

read -r -d '' CLAUDE_BP << 'BPEOF' || true

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs
BPEOF

read -r -d '' AGENTS_BP << 'BPEOF' || true

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work
BPEOF

read -r -d '' GEMINI_BP << 'BPEOF' || true

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index
BPEOF

read -r -d '' OPENAI_BP << 'BPEOF' || true

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront
BPEOF

# ═══════════════════════════════════════════════
# Generate All Files
# ═══════════════════════════════════════════════

# Full context files (all STATIC content + tool boilerplate)
generate_full "$DIR/CLAUDE.md" "Claude Code Context" "claude" "$CLAUDE_BP"
generate_full "$DIR/AGENTS.md" "AutoGen Agent Context" "agents" "$AGENTS_BP"
generate_full "$DIR/GEMINI.md" "Gemini Context" "gemini" "$GEMINI_BP"
generate_full "$DIR/OPENAI.md" "OpenAI Context" "openai" "$OPENAI_BP"

# Lean context files (selected sections only)
generate_lean "$DIR/.cursorrules" "Cursor Rules" "cursor" "Identity|Navigation"

# Copilot needs .github/ directory
mkdir -p "$DIR/.github"
generate_lean "$DIR/.github/copilot-instructions.md" "GitHub Copilot Instructions" "copilot" "Identity|Triggers|Navigation"

# ═══════════════════════════════════════════════
# .0agnostic/ Content Validation
# ═══════════════════════════════════════════════
# Warns about .0agnostic/ content not referenced in 0AGNOSTIC.md
# Per: .0agnostic/02_rules/static/agnostic_update_protocol.md

WARN_COUNT=0

if [ -d "$DIR/.0agnostic" ]; then
    echo ""
    echo "Validating .0agnostic/ references in 0AGNOSTIC.md..."

    AGNOSTIC_TEXT=$(cat "$DIR/0AGNOSTIC.md")

    # Check knowledge topics (directories in 01_knowledge/)
    if [ -d "$DIR/.0agnostic/01_knowledge" ]; then
        for topic_dir in "$DIR"/.0agnostic/01_knowledge/*/; do
            [ -d "$topic_dir" ] || continue
            topic=$(basename "$topic_dir")
            # Skip if topic dir only has .gitkeep
            real_files=$(find "$topic_dir" -type f ! -name '.gitkeep' 2>/dev/null | head -1)
            [ -z "$real_files" ] && continue
            if ! echo "$AGNOSTIC_TEXT" | grep -qi "$topic"; then
                echo "  WARNING: Knowledge topic '$topic' has content but is not referenced in 0AGNOSTIC.md"
                WARN_COUNT=$((WARN_COUNT + 1))
            fi
        done
    fi

    # Check rules (files in 02_rules/{category}/{rule}/ subdirectories)
    for rules_subdir in static dynamic 0_every_api_request 1_scenario_based; do
        if [ -d "$DIR/.0agnostic/02_rules/$rules_subdir" ]; then
            for rule_file in "$DIR"/.0agnostic/02_rules/$rules_subdir/*/*.md; do
                [ -f "$rule_file" ] || continue
                rule_name=$(basename "$rule_file")
                # Skip test files and READMEs
                case "$rule_name" in test_*|README*) continue ;; esac
                if ! echo "$AGNOSTIC_TEXT" | grep -qi "$rule_name"; then
                    # Also check without .md extension and with underscores as spaces
                    rule_stem="${rule_name%.md}"
                    rule_words=$(echo "$rule_stem" | tr '_' ' ')
                    if ! echo "$AGNOSTIC_TEXT" | grep -qi "$rule_stem" && ! echo "$AGNOSTIC_TEXT" | grep -qi "$rule_words"; then
                        echo "  WARNING: Rule '$rules_subdir/$rule_name' is not referenced in 0AGNOSTIC.md"
                        WARN_COUNT=$((WARN_COUNT + 1))
                    fi
                fi
            done
        fi
    done

    # Check protocols (files in 03_protocols/)
    if [ -d "$DIR/.0agnostic/03_protocols" ]; then
        for proto_file in "$DIR"/.0agnostic/03_protocols/*.md; do
            [ -f "$proto_file" ] || continue
            proto_name=$(basename "$proto_file")
            if ! echo "$AGNOSTIC_TEXT" | grep -qi "$proto_name"; then
                proto_stem="${proto_name%.md}"
                proto_words=$(echo "$proto_stem" | tr '_' ' ')
                if ! echo "$AGNOSTIC_TEXT" | grep -qi "$proto_stem" && ! echo "$AGNOSTIC_TEXT" | grep -qi "$proto_words"; then
                    echo "  WARNING: Protocol '$proto_name' is not referenced in 0AGNOSTIC.md"
                    WARN_COUNT=$((WARN_COUNT + 1))
                fi
            fi
        done
    fi

    # Check skills (in 06_context_avenue_web/01_file_based/05_skills/)
    SKILLS_DIR="$DIR/.0agnostic/06_context_avenue_web/01_file_based/05_skills"
    if [ -d "$SKILLS_DIR" ]; then
        for skill_file in "$SKILLS_DIR"/*.md; do
            [ -f "$skill_file" ] || continue
            skill_name=$(basename "$skill_file" .md)
            if ! echo "$AGNOSTIC_TEXT" | grep -qi "$skill_name"; then
                echo "  WARNING: Skill '$skill_name' is not referenced in 0AGNOSTIC.md"
                WARN_COUNT=$((WARN_COUNT + 1))
            fi
        done
    fi

    if [ "$WARN_COUNT" -gt 0 ]; then
        echo ""
        echo "⚠ Found $WARN_COUNT unreferenced .0agnostic/ item(s)."
        echo "  Update 0AGNOSTIC.md to reference them (see: .0agnostic/02_rules/static/agnostic_update_protocol.md)"
    else
        echo "  All .0agnostic/ content is referenced in 0AGNOSTIC.md ✓"
    fi
fi

# --- Pointer Sync Validation ---
# Find pointer-sync.sh in its protocol directory (cross-protocol reference)
_SYNC_SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POINTER_SYNC="$_SYNC_SCRIPT_DIR/../../pointer_sync_protocol/tools/pointer-sync.sh"
if [ -x "$POINTER_SYNC" ]; then
    echo ""
    echo "--- Pointer Validation ---"
    if "$POINTER_SYNC" --validate 2>/dev/null; then
        echo "  All pointers valid ✓"
    else
        echo "  ⚠ Some pointers are broken or stale. Run: pointer-sync.sh --verbose"
    fi
fi

echo ""
echo "Sync complete! Generated tool-specific files from 0AGNOSTIC.md"
echo "Format detected: $FORMAT"
echo "STATIC content: $STATIC_LEN chars"
echo "Files created:"
echo "  - CLAUDE.md"
echo "  - AGENTS.md"
echo "  - GEMINI.md"
echo "  - OPENAI.md"
echo "  - .cursorrules"
echo "  - .github/copilot-instructions.md"
if [ "$WARN_COUNT" -gt 0 ]; then
    echo ""
    echo "Warnings: $WARN_COUNT (see above)"
fi
