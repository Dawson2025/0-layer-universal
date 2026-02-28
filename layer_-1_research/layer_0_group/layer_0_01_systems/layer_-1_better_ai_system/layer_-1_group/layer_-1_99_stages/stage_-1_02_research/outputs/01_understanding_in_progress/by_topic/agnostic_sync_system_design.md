# Agnostic Sync System Design

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Date**: 2026-01-30
**Topic**: Sync script for AGNOSTIC.md + .agnostic/ → tool-specific formats

---

## Overview

This document describes the sync system that transforms agnostic AI context files into tool-specific formats.

## Source → Target Mapping

| Source | Target | Transformation |
|--------|--------|----------------|
| `AGNOSTIC.md` | `CLAUDE.md` | Add Claude shim header |
| `AGNOSTIC.md` | `AGENTS.md` | Add Codex first-message format |
| `AGNOSTIC.md` | `GEMINI.md` | Add Gemini systemInstruction format |
| `.agnostic/skills/` | `.claude/skills/` | Direct copy |
| `.agnostic/agents/` | `.claude/agents/` | Direct copy |
| `.agnostic/rules/` | `.claude/rules/` | Direct copy |
| `.agnostic/rules/` | `.cursor/rules/*.mdc` | Format conversion |
| `.agnostic/automation/` | `.claude/hooks/` | Direct copy |

## Shim Templates

### Claude Shim (prepended to AGNOSTIC.md)

```markdown
# CLAUDE.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

### Codex/AGENTS.md Shim

```markdown
# AGENTS.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

### Gemini Shim

```markdown
# GEMINI.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

## Sync Script Behavior

### Command: `agnostic-sync`

```bash
agnostic-sync [options] [path]

Options:
  --dry-run    Show what would be done without doing it
  --force      Overwrite even if target is newer
  --watch      Watch for changes and sync automatically
  --verbose    Show detailed output

Arguments:
  path         Directory to sync (default: current directory)
```

### Sync Logic

1. **Find AGNOSTIC.md** in the specified directory
2. **Generate tool-specific files**:
   - CLAUDE.md = shim + AGNOSTIC.md content
   - AGENTS.md = shim + AGNOSTIC.md content
   - GEMINI.md = shim + AGNOSTIC.md content
3. **Find .agnostic/** folder
4. **Copy/convert resources**:
   - .agnostic/skills/ → .claude/skills/
   - .agnostic/agents/ → .claude/agents/
   - .agnostic/rules/ → .claude/rules/
   - .agnostic/rules/ → .cursor/rules/ (with .mdc conversion)
   - .agnostic/automation/ → .claude/hooks/
5. **Preserve tool-specific files** that don't come from agnostic:
   - .claude/settings.json
   - .claude/mcp.json
   - .cursor/settings.json

### File Preservation Rules

Files in tool-specific folders that should NOT be overwritten:
- `settings.json` - Tool configuration
- `mcp.json` - MCP server configuration
- Any file with `# MANUAL` comment in first line

## Directory Structure After Sync

```
layer_X/
├── AGNOSTIC.md                 # SOURCE (edit this)
├── .agnostic/                  # SOURCE (edit this)
│   ├── skills/
│   ├── agents/
│   ├── rules/
│   └── automation/
│
├── CLAUDE.md                   # GENERATED (do not edit)
├── AGENTS.md                   # GENERATED (do not edit)
├── GEMINI.md                   # GENERATED (do not edit)
│
├── .claude/                    # GENERATED + tool-specific
│   ├── skills/                 # ← from .agnostic/skills/
│   ├── agents/                 # ← from .agnostic/agents/
│   ├── rules/                  # ← from .agnostic/rules/
│   ├── hooks/                  # ← from .agnostic/automation/
│   ├── settings.json           # MANUAL (preserved)
│   └── mcp.json                # MANUAL (preserved)
│
└── .cursor/                    # GENERATED + tool-specific
    ├── rules/                  # ← from .agnostic/rules/ (converted)
    └── settings.json           # MANUAL (preserved)
```

## Implementation Plan

1. **Phase 1**: Bash script for basic sync
2. **Phase 2**: Add watch mode with inotifywait/fswatch
3. **Phase 3**: Add git hook for auto-sync on commit
4. **Phase 4**: Optional Python/Node version for complex transformations

---

## Related Files

- Template: `../agnostic_templates/AGNOSTIC.md.template`
- Script: `scripts/agnostic-sync.sh`
