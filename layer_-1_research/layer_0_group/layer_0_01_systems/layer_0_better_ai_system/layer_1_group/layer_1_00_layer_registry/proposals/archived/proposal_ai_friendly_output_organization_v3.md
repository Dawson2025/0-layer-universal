---
resource_id: "630a0665-9aef-4580-b158-2fcc2878638c"
resource_type: "document"
resource_name: "proposal_ai_friendly_output_organization_v3"
---
# Proposal v3: Complete AI System Architecture

**Date**: 2026-02-02
**Version**: 3.0
**Status**: ⚠️ SUPERSEDED by v4
**Superseded By**: `proposal_ai_friendly_output_organization_v4.md`
**Reason**: v4 adds complete inventory, specific file mappings, cleanup plan, reconciliation strategy
**Previous Versions**:
- v1: Nested folders within stage outputs (SUPERSEDED)
- v2: Layer-stage hierarchy with features (SUPERSEDED)
**Supersedes**: v1 and v2

---

> **Note**: This proposal has been superseded. See v4 for the complete architecture including:
> - Full inventory of 2,500+ existing files
> - Specific file-by-file distribution mapping
> - Phase 0: Cleanup plan (50+ sync conflicts)
> - Reconciliation strategy for existing feature content
> - 8-phase implementation plan

---

---

## Change Summary

| Version | Approach | What Was Missing |
|---------|----------|------------------|
| v1 | Nested folders in `by_topic/` | Didn't use layer-stage system |
| v2 | Layer-stage hierarchy + features | Missing agnostic system, sync, tool-specific |
| **v3** | **Complete architecture** | **Includes everything** |

**v3 Adds**:
- 0AGNOSTIC.md as source of truth
- Three-tier folder architecture (.0agnostic/ → .1*_merge/ → native output)
- Tool-specific configurations (Claude, Cursor, Copilot, Gemini, Aider, etc.)
- Sync system (agnostic-sync.sh)
- Episodic memory in correct location (.0agnostic/episodic/)
- Content in sub-layers (not duplicated in dot-folders)

---

## Problem Statement

### Current State

1. **Research lumped in one place** - All topics in `by_topic/` folder
2. **No agnostic layer** - Missing 0AGNOSTIC.md source of truth
3. **No tool portability** - Can't generate configs for different AI tools
4. **Episodic memory misplaced** - In `outputs/` instead of `.0agnostic/`
5. **AI agents struggle** - No entry points, discovery, or contribution guidelines
6. **No sync system** - Manual updates required for each tool

### What's Needed

| Need | Solution Component |
|------|-------------------|
| Single source of truth | `0AGNOSTIC.md` at each entity |
| Tool portability | Three-tier folder architecture |
| Agent entry points | `CLAUDE.md` with Identity/Triggers/Navigation |
| Content discovery | `0INDEX.md` at each level |
| Quick overviews | `synthesis/` folder at each level |
| Session continuity | `.0agnostic/episodic/` |
| Tool-specific configs | Generated from agnostic source |
| Automated sync | `agnostic-sync.sh` script |

---

## Proposed Architecture

### 1. Three-Tier Folder Architecture

Every entity uses this pattern:

```
entity/
├── 0AGNOSTIC.md                 # 0 - SOURCE OF TRUTH
├── .0agnostic/                  # 0 - Tool-agnostic resources
│   ├── agents/
│   ├── episodic/                # Session memory (AI infrastructure)
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── hooks/
│   │   └── scripts/
│   ├── skills/
│   └── sync-config.yaml         # What to sync to which tools
│
├── .1claude_merge/              # 1 - MERGE WORKSPACE (Claude Code)
│   ├── 0_synced/                # Auto-copied from .0agnostic/
│   ├── 1_overrides/             # Claude-specific overrides
│   ├── 2_additions/             # Claude-only additions
│   └── CLAUDE.override.md       # Additions to CLAUDE.md
│
├── .1cursor_merge/              # 1 - MERGE WORKSPACE (Cursor)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── rules.override/          # Cursor-specific rules
│
├── .1copilot_merge/             # 1 - MERGE WORKSPACE (GitHub Copilot)
│   └── ...
│
├── .1gemini_merge/              # 1 - MERGE WORKSPACE (Gemini)
│   └── ...
│
├── .1aider_merge/               # 1 - MERGE WORKSPACE (Aider)
│   └── ...
│
│ ## FINAL OUTPUTS (What tools actually read)
│
├── CLAUDE.md                    # Generated: 0AGNOSTIC.md + .1claude_merge/
├── .claude/                     # Generated: .0agnostic/ + .1claude_merge/
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   ├── rules/
│   ├── skills/
│   └── settings.json
│
├── .cursorrules                 # Generated: 0AGNOSTIC.md + .1cursor_merge/
├── .cursor/
│   └── rules/*.mdc
│
├── .github/                     # Generated: 0AGNOSTIC.md + .1copilot_merge/
│   ├── copilot-instructions.md
│   └── instructions/*.instructions.md
│
├── GEMINI.md                    # Generated: 0AGNOSTIC.md + .1gemini_merge/
│
├── .aider.conf.yml              # Generated: .1aider_merge/
│
└── 0INDEX.md                    # NEW: Discovery and status
```

### 2. Generation Flow

```
                    ┌──→ .1claude_merge/   ──→ CLAUDE.md + .claude/
                    ├──→ .1cursor_merge/   ──→ .cursorrules + .cursor/rules/
.0agnostic/ ────────┼──→ .1copilot_merge/  ──→ .github/copilot-instructions.md
0AGNOSTIC.md ───────┼──→ .1gemini_merge/   ──→ GEMINI.md
                    ├──→ .1aider_merge/    ──→ .aider.conf.yml
                    └──→ .1opencode_merge/ ──→ .opencode/
```

### 3. Sorting Order (Why Numbered Prefixes)

```
.0agnostic/          # 0 - Source (sorts first)
.1aider_merge/       # 1 - Build workspaces (alphabetical)
.1claude_merge/
.1copilot_merge/
.1cursor_merge/
.1gemini_merge/
.aider.conf.yml      # Final outputs (native locations)
.claude/
.cursor/
.github/
0AGNOSTIC.md         # Source MD (sorts early due to 0)
0INDEX.md            # Discovery (sorts early due to 0)
CLAUDE.md            # Generated
GEMINI.md            # Generated
```

---

## 0AGNOSTIC.md Template

Every entity gets a `0AGNOSTIC.md` that serves as the source of truth:

```markdown
# 0AGNOSTIC.md - [Entity Name]

## Identity

You are an agent working on **[entity name]** at **Layer [N]**, **Stage [XX]**.

- **Role**: [What this agent does]
- **Scope**: [What's in/out of scope]
- **Parent**: `../0AGNOSTIC.md` ([parent name])
- **Children**: [List or "None (leaf)"]

## Triggers: When to Load This Context

Load this context when:
- User mentions: [keywords]
- Working on: [related tasks]
- Entering directory: [paths]

## On Entry

1. Read `0INDEX.md` for current state
2. Read `synthesis/` for overview
3. Check `.0agnostic/episodic/index.md` for recent sessions
4. Identify relevant child entities if diving deeper

## Navigation

- **Parent**: [relative path]
- **Children**: [list with paths]
- **Related**: [sibling entities]

## Where to Contribute

| Type of Work | Location |
|--------------|----------|
| New research | `layer_N/layer_N_99_stages/stage_N_02_research/outputs/` |
| Instructions | `layer_N/layer_N_99_stages/stage_N_03_instructions/` |
| Session notes | `.0agnostic/episodic/sessions/` |

## Behaviors

### Always
- [Rules that always apply]

### When [Condition]
- [Conditional rules]

## Tool-Specific Notes

- **Claude Code**: See `.1claude_merge/CLAUDE.override.md` for additions
- **Cursor**: See `.1cursor_merge/` for rule overrides
- **Other tools**: Check respective merge folders

---
*Source of truth for all tool-specific files*
*Edit this file, then run: `./scripts/agnostic-sync.sh`*
```

---

## 0INDEX.md Template

Every entity gets a `0INDEX.md` for discovery:

```markdown
# Index: [Entity Name]

## Overview

[Brief description of this entity]

## Contents

| Item | Type | Status | Description |
|------|------|--------|-------------|
| `0AGNOSTIC.md` | file | ✅ | Source of truth |
| `CLAUDE.md` | file | 🔄 | Generated from 0AGNOSTIC.md |
| `.0agnostic/` | folder | ✅ | Tool-agnostic resources |
| `.claude/` | folder | 🔄 | Generated Claude config |
| `layer_N/` | folder | ⚠️ | Entity internals |
| `layer_N+1/` | folder | ❌ | Children (empty) |

## Status Legend

- ✅ Complete - Ready for use
- ⚠️ Partial - Has content, needs work
- 🔄 Generated - Auto-generated from source
- ❌ Empty - Placeholder only

## Stage Progress (if applicable)

| Stage | Status | Notes |
|-------|--------|-------|
| 01 Request Gathering | ✅ | Requirements defined |
| 02 Research | 🔄 | In progress |
| 03 Instructions | ❌ | Not started |
| ... | ... | ... |

## Cross-References

| This Entity | Relates To | Why |
|-------------|------------|-----|
| [entity] | [related entity] | [relationship] |

## Open Questions

- [ ] Question 1
- [ ] Question 2

## Last Sync

- **Date**: [YYYY-MM-DD]
- **Tool**: [which tool ran agnostic-sync.sh]
- **Session**: [session ID if applicable]
```

---

## .0agnostic/ Folder Structure

```
.0agnostic/
├── agents/                      # Agent configurations
│   └── default.md               # Default agent prompt
│
├── episodic/                    # Session memory (AI infrastructure)
│   ├── index.md                 # Session overview
│   ├── sessions/                # Per-session logs
│   │   └── session_YYYY-MM-DD_topic.md
│   ├── changes/                 # Change tracking
│   │   └── YYYY-MM-DD_changes.md
│   └── divergence.log           # Cross-tool divergence tracking
│
├── hooks/                       # Event hooks (tool-agnostic)
│   ├── SessionStart.sh          # Run on session start
│   ├── PreCompact.sh            # Run before context compaction
│   └── scripts/                 # Supporting scripts
│       └── agnostic-sync.sh     # Main sync script
│
├── skills/                      # Reusable procedures
│   └── research/
│       └── skill.md
│
├── rules/                       # Modular rules
│   ├── always/                  # Always-apply rules
│   │   └── security.md
│   └── conditional/             # Glob-based rules
│       ├── typescript.md
│       └── python.md
│
└── sync-config.yaml             # Sync configuration
```

### sync-config.yaml

```yaml
# .0agnostic/sync-config.yaml
sync:
  version: "1.0"

tools:
  claude:
    enabled: true
    merge_folder: ".1claude_merge"
    output:
      md_file: "CLAUDE.md"
      folder: ".claude"
    include:
      - "agents/"
      - "episodic/"
      - "hooks/"
      - "skills/"
    transform:
      rules: "to_claude_rules"  # Convert to .claude/rules/ format

  cursor:
    enabled: true
    merge_folder: ".1cursor_merge"
    output:
      folder: ".cursor/rules"
    transform:
      rules: "to_mdc_format"  # Convert to MDC with frontmatter

  copilot:
    enabled: true
    merge_folder: ".1copilot_merge"
    output:
      md_file: ".github/copilot-instructions.md"
      scoped_rules: ".github/instructions/"
    transform:
      rules: "to_applyTo_format"  # Convert to applyTo frontmatter

  gemini:
    enabled: true
    merge_folder: ".1gemini_merge"
    output:
      md_file: "GEMINI.md"
    transform:
      rules: "to_import_format"  # Convert to @import syntax

  aider:
    enabled: true
    merge_folder: ".1aider_merge"
    output:
      file: ".aider.conf.yml"
    # No rules transformation - Aider uses config only
```

---

## Merge Folder Structure (.1*_merge/)

Each tool gets a merge folder with this structure:

```
.1claude_merge/
├── 0_synced/                    # AUTO-GENERATED from .0agnostic/ (don't edit!)
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   └── skills/
│
├── 1_overrides/                 # Claude-specific OVERRIDES (edit here)
│   ├── agents/
│   │   └── researcher.md        # Overrides .0agnostic/agents/researcher.md
│   └── rules/
│       └── claude_specific.md   # Override agnostic rules
│
├── 2_additions/                 # Claude-ONLY items (not in .0agnostic)
│   ├── agents/
│   │   └── claude_only_agent.md
│   └── skills/
│       └── claude_only_skill/
│
├── CLAUDE.override.md           # Additions to CLAUDE.md (appended)
│
└── exclude.yaml                 # Items from .0agnostic to NOT include
```

### exclude.yaml

```yaml
# .1claude_merge/exclude.yaml
exclude:
  - "agents/gemini_specific.md"  # Don't sync this agent
  - "skills/cursor_only/"        # Skip entire folder
```

---

## Tool-Specific Output Mappings

| Source (.0agnostic/) | Claude Code | Cursor | Copilot | Gemini |
|---------------------|-------------|--------|---------|--------|
| `0AGNOSTIC.md` | `CLAUDE.md` | `.cursorrules` | `copilot-instructions.md` | `GEMINI.md` |
| `agents/` | `.claude/agents/` | N/A | N/A | N/A |
| `skills/` | `.claude/skills/` | N/A | N/A | N/A |
| `hooks/` | `.claude/settings.json` | N/A | N/A | N/A |
| `rules/always/` | `.claude/rules/` (alwaysApply: true) | `.cursor/rules/` (alwaysApply: true) | Main instructions | Main `GEMINI.md` |
| `rules/conditional/` | `.claude/rules/` (with globs) | `.cursor/rules/` (with globs) | `.github/instructions/` (applyTo) | `@import` files |
| `episodic/` | `.claude/episodic/` | N/A | N/A | N/A |

---

## Content Location: Sub-Layers vs Dot-Folders

**IMPORTANT**: Content (knowledge, prompts, rules, principles) lives in **sub-layers**, not dot-folders:

```
entity/
├── layer_N/
│   └── layer_N_03_sub_layers/
│       ├── sub_layer_N_01_prompts/           ← Prompts live HERE
│       ├── sub_layer_N_02_knowledge_system/  ← Knowledge lives HERE
│       ├── sub_layer_N_03_principles/        ← Principles live HERE
│       └── sub_layer_N_04_rules/             ← Rules live HERE
│
└── .0agnostic/                               ← Tool CONFIG only
    ├── agents/                               ← Agent configs
    ├── episodic/                             ← Session memory
    ├── hooks/                                ← Event hooks
    ├── skills/                               ← Skill definitions
    └── rules/                                ← Rule REFERENCES
        └── README.md → "See layer_N_03_sub_layers/sub_layer_N_04_rules/"
```

**Why this split?**
1. **No duplication**: Content in one place (sub-layers), config in another (dot-folders)
2. **Layer cascade**: Content inherits naturally through layer hierarchy
3. **Tool flexibility**: Dot-folders reference sub-layers, transform as needed per tool
4. **Single source of truth**: Sub-layers for content, `.0agnostic/` for AI config

---

## Episodic Memory Location (CORRECTED)

**Move episodic from outputs/ to .0agnostic/**:

| Before (Wrong) | After (Correct) |
|----------------|-----------------|
| `outputs/episodic/` | `.0agnostic/episodic/` |

**Why?**
- Episodic memory is AI system infrastructure, not stage output
- It's used by ANY AI tool (Claude, Cursor, Gemini, etc.)
- Keeping it in `.0agnostic/` makes it tool-agnostic
- Stage `outputs/` should only contain actual stage products

---

## Full Proposed Entity Structure

```
layer_N_<type>_<name>/
│
│ ## SOURCE OF TRUTH
│
├── 0AGNOSTIC.md                              # Main agnostic context
├── 0INDEX.md                                 # Discovery and status
│
├── .0agnostic/                               # Tool-agnostic resources
│   ├── agents/
│   ├── episodic/                             # Session memory (MOVED HERE)
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── hooks/
│   │   ├── SessionStart.sh
│   │   └── scripts/
│   │       └── agnostic-sync.sh
│   ├── skills/
│   ├── rules/
│   │   ├── always/
│   │   └── conditional/
│   └── sync-config.yaml
│
│ ## MERGE WORKSPACES
│
├── .1claude_merge/
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── CLAUDE.override.md
│
├── .1cursor_merge/
│   └── ...
│
├── .1copilot_merge/
│   └── ...
│
├── .1gemini_merge/
│   └── ...
│
├── .1aider_merge/
│   └── ...
│
│ ## GENERATED OUTPUTS (What tools read)
│
├── CLAUDE.md                                 # Generated
├── .claude/                                  # Generated
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   ├── rules/
│   ├── skills/
│   └── settings.json
│
├── .cursorrules                              # Generated (legacy)
├── .cursor/
│   └── rules/*.mdc                           # Generated
│
├── .github/
│   ├── copilot-instructions.md               # Generated
│   └── instructions/                         # Generated
│
├── GEMINI.md                                 # Generated
├── .aider.conf.yml                           # Generated
│
│ ## SYNTHESIS (AI-Friendly)
│
├── synthesis/
│   └── <entity>_synthesis.md
│
│ ## ENTITY INTERNALS
│
├── layer_N/                                  # Entity's own internals
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_01_ai_manager_system/
│   ├── layer_N_02_manager_handoff_documents/
│   ├── layer_N_03_sub_layers/                # Content lives here!
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   └── sub_layer_N_04_rules/
│   └── layer_N_99_stages/
│       ├── stage_N_00_stage_registry/
│       ├── stage_N_01_request_gathering/
│       ├── stage_N_02_research/
│       │   ├── 0AGNOSTIC.md
│       │   ├── 0INDEX.md
│       │   ├── .0agnostic/
│       │   │   └── episodic/                 # Stage-level session memory
│       │   ├── outputs/                      # Stage products only
│       │   │   ├── by_need/
│       │   │   ├── by_topic/
│       │   │   └── synthesis/
│       │   └── ...
│       └── ... (stages 03-11)
│
└── layer_N+1/                                # Entity's children
    ├── layer_N+1_features/
    └── layer_N+1_components/
```

---

## agnostic-sync.sh Script

```bash
#!/bin/bash
# .0agnostic/hooks/scripts/agnostic-sync.sh

set -e

ENTITY_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
AGNOSTIC_DIR="$ENTITY_ROOT/.0agnostic"
CONFIG="$AGNOSTIC_DIR/sync-config.yaml"

usage() {
    echo "Usage: agnostic-sync.sh [tool|all]"
    echo "  tool: claude, cursor, copilot, gemini, aider"
    echo "  all:  Sync all enabled tools"
    exit 1
}

sync_claude() {
    local merge_dir="$ENTITY_ROOT/.1claude_merge"
    local output_dir="$ENTITY_ROOT/.claude"

    echo "Syncing Claude Code..."

    # 1. Copy .0agnostic/ to merge/0_synced/
    rm -rf "$merge_dir/0_synced"
    mkdir -p "$merge_dir/0_synced"
    cp -r "$AGNOSTIC_DIR"/* "$merge_dir/0_synced/" 2>/dev/null || true
    rm -f "$merge_dir/0_synced/sync-config.yaml"

    # 2. Apply excludes
    if [ -f "$merge_dir/exclude.yaml" ]; then
        # Parse exclude.yaml and remove excluded items
        # (simplified - real implementation would use yq)
        echo "Applying excludes..."
    fi

    # 3. Generate .claude/ from merged content
    rm -rf "$output_dir"
    mkdir -p "$output_dir"

    # Copy synced content
    cp -r "$merge_dir/0_synced"/* "$output_dir/" 2>/dev/null || true

    # Apply overrides (replace matching files)
    if [ -d "$merge_dir/1_overrides" ]; then
        cp -r "$merge_dir/1_overrides"/* "$output_dir/" 2>/dev/null || true
    fi

    # Add additions
    if [ -d "$merge_dir/2_additions" ]; then
        cp -r "$merge_dir/2_additions"/* "$output_dir/" 2>/dev/null || true
    fi

    # 4. Generate CLAUDE.md
    echo "Generating CLAUDE.md..."

    # Start with auto-generated header
    cat > "$ENTITY_ROOT/CLAUDE.md" << 'EOF'
# CLAUDE.md - Auto-generated from 0AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit 0AGNOSTIC.md instead, then run: agnostic-sync.sh claude
# Generated: $(date -Iseconds)

EOF

    # Append 0AGNOSTIC.md content
    cat "$ENTITY_ROOT/0AGNOSTIC.md" >> "$ENTITY_ROOT/CLAUDE.md"

    # Append override content if exists
    if [ -f "$merge_dir/CLAUDE.override.md" ]; then
        echo "" >> "$ENTITY_ROOT/CLAUDE.md"
        echo "---" >> "$ENTITY_ROOT/CLAUDE.md"
        echo "## Claude-Specific Additions" >> "$ENTITY_ROOT/CLAUDE.md"
        echo "" >> "$ENTITY_ROOT/CLAUDE.md"
        cat "$merge_dir/CLAUDE.override.md" >> "$ENTITY_ROOT/CLAUDE.md"
    fi

    # Add footer
    cat >> "$ENTITY_ROOT/CLAUDE.md" << 'EOF'

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
EOF

    echo "Claude sync complete."
}

sync_cursor() {
    local merge_dir="$ENTITY_ROOT/.1cursor_merge"
    local output_dir="$ENTITY_ROOT/.cursor"

    echo "Syncing Cursor..."

    mkdir -p "$output_dir/rules"

    # Convert agnostic rules to MDC format
    for rule in "$AGNOSTIC_DIR/rules/always"/*.md; do
        [ -f "$rule" ] || continue
        local name=$(basename "$rule" .md)

        # Add MDC frontmatter for always-apply
        cat > "$output_dir/rules/$name.mdc" << EOF
---
description: "$(head -1 "$rule" | sed 's/^# //')"
alwaysApply: true
---
$(cat "$rule")
EOF
    done

    for rule in "$AGNOSTIC_DIR/rules/conditional"/*.md; do
        [ -f "$rule" ] || continue
        local name=$(basename "$rule" .md)

        # Parse glob from rule metadata or filename
        local glob="**/*"
        if grep -q "^globs:" "$rule"; then
            glob=$(grep "^globs:" "$rule" | sed 's/^globs: //')
        fi

        cat > "$output_dir/rules/$name.mdc" << EOF
---
description: "$(head -1 "$rule" | sed 's/^# //')"
globs: "$glob"
alwaysApply: false
---
$(cat "$rule")
EOF
    done

    echo "Cursor sync complete."
}

sync_copilot() {
    local merge_dir="$ENTITY_ROOT/.1copilot_merge"
    local output_dir="$ENTITY_ROOT/.github"

    echo "Syncing GitHub Copilot..."

    mkdir -p "$output_dir/instructions"

    # Generate main instructions file from 0AGNOSTIC.md
    cat "$ENTITY_ROOT/0AGNOSTIC.md" > "$output_dir/copilot-instructions.md"

    # Append always-apply rules
    for rule in "$AGNOSTIC_DIR/rules/always"/*.md; do
        [ -f "$rule" ] || continue
        echo "" >> "$output_dir/copilot-instructions.md"
        cat "$rule" >> "$output_dir/copilot-instructions.md"
    done

    # Convert conditional rules to scoped instruction files
    for rule in "$AGNOSTIC_DIR/rules/conditional"/*.md; do
        [ -f "$rule" ] || continue
        local name=$(basename "$rule" .md)

        # Parse glob for applyTo frontmatter
        local glob="**/*"
        if grep -q "^globs:" "$rule"; then
            glob=$(grep "^globs:" "$rule" | sed 's/^globs: //')
        fi

        cat > "$output_dir/instructions/$name.instructions.md" << EOF
---
applyTo: "$glob"
---
$(cat "$rule")
EOF
    done

    echo "Copilot sync complete."
}

sync_gemini() {
    local merge_dir="$ENTITY_ROOT/.1gemini_merge"

    echo "Syncing Gemini CLI..."

    # Generate GEMINI.md with @imports
    cat > "$ENTITY_ROOT/GEMINI.md" << EOF
# GEMINI.md - Auto-generated from 0AGNOSTIC.md
# Generated: $(date -Iseconds)

$(cat "$ENTITY_ROOT/0AGNOSTIC.md")

## Imported Rules

EOF

    # Add @imports for conditional rules
    for rule in "$AGNOSTIC_DIR/rules/always"/*.md; do
        [ -f "$rule" ] || continue
        echo "@.0agnostic/rules/always/$(basename "$rule")" >> "$ENTITY_ROOT/GEMINI.md"
    done

    echo "Gemini sync complete."
}

sync_aider() {
    local merge_dir="$ENTITY_ROOT/.1aider_merge"

    echo "Syncing Aider..."

    # Aider doesn't have instruction files - just copy config if present
    if [ -f "$merge_dir/aider-config.yml" ]; then
        cp "$merge_dir/aider-config.yml" "$ENTITY_ROOT/.aider.conf.yml"
    fi

    echo "Aider sync complete."
}

sync_all() {
    sync_claude
    sync_cursor
    sync_copilot
    sync_gemini
    sync_aider
}

# Main
case "${1:-all}" in
    claude)  sync_claude ;;
    cursor)  sync_cursor ;;
    copilot) sync_copilot ;;
    gemini)  sync_gemini ;;
    aider)   sync_aider ;;
    all)     sync_all ;;
    *)       usage ;;
esac

echo "Sync complete. Run 'git status' to see changes."
```

---

## SessionStart Hook Integration

```json
// .claude/settings.json
{
  "hooks": {
    "SessionStart": [{
      "type": "command",
      "command": "./.0agnostic/hooks/scripts/agnostic-sync.sh claude",
      "description": "Sync agnostic config to Claude-specific files"
    }],
    "PreCompact": [{
      "type": "command",
      "command": "./.0agnostic/hooks/scripts/save-session.sh",
      "description": "Save session summary before compaction"
    }]
  }
}
```

---

## Integration with v2 Features

v3 includes ALL v2 AI-friendly improvements:

| v2 Feature | v3 Location | Notes |
|------------|-------------|-------|
| CLAUDE.md with triggers | Generated from `0AGNOSTIC.md` | Triggers section in agnostic |
| 0INDEX.md discovery | Same location, enhanced | Includes sync status |
| synthesis/ folders | Same pattern | At every level |
| Cross-references | `_crossref.md` at project root | Links features |
| Contribution templates | `_templates/` at project root | For new files |
| Status tracking | In 0INDEX.md | ✅/⚠️/🔄/❌ |

---

## Research File Distribution (Same as v2)

| Current File | → Feature | Location |
|--------------|-----------|----------|
| Memory research files (6) | `ai_dynamic_memory_system` | `stage_0_02_research/outputs/` |
| Context research files (6) | `ai_context_system` | `stage_0_02_research/outputs/` |
| Multi-agent files (3) | `ai_manager_hierarchy_system` | `stage_0_02_research/outputs/` |
| Layer-stage files (4) | `better_layer_stage_system` | `stage_0_02_research/outputs/` |
| Automation files (1) | `ai_automation_system` | `stage_0_02_research/outputs/` |
| Cross-cutting files (6) | Project level | `layer_-1_group/.../cross_cutting/` |

---

## Registry Updates Required

### 1. Entity Registry (NEW)

```yaml
# entity_registry.yaml
entity_patterns:
  required_files:
    - "0AGNOSTIC.md"              # Source of truth
    - "0INDEX.md"                 # Discovery
  required_folders:
    - ".0agnostic/"               # Tool-agnostic resources
    - "synthesis/"                # Synthesis documents
  optional_folders:
    - ".1*_merge/"                # Tool merge workspaces
    - ".claude/"                  # Generated (if using Claude)
    - ".cursor/"                  # Generated (if using Cursor)
    - ".github/"                  # Generated (if using Copilot)
```

### 2. Stage Registry Updates

```yaml
# stage_registry.yaml updates
stage_patterns:
  ai_infrastructure:
    location: ".0agnostic/"       # NOT in outputs/
    contents:
      - "episodic/"               # Session memory
      - "agents/"                 # Agent configs
      - "hooks/"                  # Event hooks
      - "skills/"                 # Skills
  outputs:
    location: "outputs/"          # Stage products only
    contents:
      - "by_need/"
      - "by_topic/"
      - "synthesis/"              # Stage synthesis
```

### 3. Layer Registry Updates

```yaml
# layer_registry.yaml updates
layer_conventions:
  agnostic_system:
    source_file: "0AGNOSTIC.md"
    source_folder: ".0agnostic/"
    merge_pattern: ".1<tool>_merge/"
    output_pattern: ".<tool>/ or <TOOL>.md"
    sync_script: ".0agnostic/hooks/scripts/agnostic-sync.sh"
```

---

## Implementation Steps

### Phase 1: Agnostic Infrastructure
1. Create `.0agnostic/` folder structure at project root
2. Create `0AGNOSTIC.md` template
3. Create `sync-config.yaml`
4. Create `agnostic-sync.sh` script

### Phase 2: Merge Workspaces
1. Create `.1claude_merge/` structure
2. Create `.1cursor_merge/` structure
3. Create `.1copilot_merge/` structure
4. Create other merge folders as needed

### Phase 3: Move Episodic Memory
1. Move `outputs/episodic/` to `.0agnostic/episodic/`
2. Update all references
3. Update session tracking scripts

### Phase 4: Feature Enhancement (from v2)
1. Add `0AGNOSTIC.md` to each feature
2. Add `0INDEX.md` to each feature
3. Add `synthesis/` to each feature
4. Ensure `.0agnostic/` exists at each feature

### Phase 5: Research Distribution (from v2)
1. Move research files to appropriate features
2. Split large files
3. Create cross-cutting folder for multi-feature research

### Phase 6: Sync Testing
1. Run `agnostic-sync.sh all`
2. Verify generated files match expected output
3. Test each tool reads its generated config correctly

### Phase 7: Registry Updates
1. Update `entity_registry.yaml`
2. Update `stage_registry.yaml`
3. Update `layer_registry.yaml`

---

## Benefits Summary

| Benefit | How Achieved |
|---------|--------------|
| **Single source of truth** | `0AGNOSTIC.md` + `.0agnostic/` |
| **Tool portability** | Three-tier architecture with sync script |
| **No manual sync** | SessionStart hook runs sync automatically |
| **Clear overrides** | Separate `1_overrides/` folder per tool |
| **Tool-only additions** | Separate `2_additions/` folder per tool |
| **Agent entry points** | `0AGNOSTIC.md` with Identity/Triggers/Navigation |
| **Easy discovery** | `0INDEX.md` with status tracking |
| **Session continuity** | `.0agnostic/episodic/` at each entity |
| **Content in one place** | Sub-layers for content, dot-folders for config |

---

## Metrics

| Metric | Count |
|--------|-------|
| Entities needing agnostic setup | ~30 (project + features + stages) |
| Files to create per entity | ~8 (0AGNOSTIC, 0INDEX, .0agnostic/*, sync script) |
| Merge folders per tool | 5 (Claude, Cursor, Copilot, Gemini, Aider) |
| Registry files to update | 3 |
| Episodic folders to move | ~10 |

---

## Open Questions

1. Should `agnostic-sync.sh` be at project root or in each entity's `.0agnostic/hooks/scripts/`?
2. How to handle merge conflicts when multiple tools have diverged?
3. Should generated files (CLAUDE.md, .claude/) be gitignored or committed?
4. How to version the sync-config.yaml schema?

---

## Decision Needed

- [ ] Approve v3 proposal
- [ ] Approve with modifications (specify)
- [ ] Request v4 with additional changes
- [ ] Reject and return to v2 approach

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-02 | Nested folders within stage outputs |
| v2 | 2026-02-02 | Layer-stage hierarchy with features + AI-friendly enhancements |
| v3 | 2026-02-02 | Complete architecture: agnostic system, three-tier folders, sync script, tool mappings |
