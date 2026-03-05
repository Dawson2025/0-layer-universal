---
resource_id: "086d142d-2e3c-45f1-9c5a-c3bb16449148"
resource_type: "knowledge"
resource_name: "agnostic_sync_system_design"
---
# Agnostic Sync System Design

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Date**: 2026-01-30
**Topic**: Sync script for AGNOSTIC.md + .agnostic/ → tool-specific formats

---

<!-- section_id: "a7718c29-0831-4fa5-bf4b-10ec16d669d5" -->
## Overview

This document describes the sync system that transforms agnostic AI context files into tool-specific formats.

<!-- section_id: "ecff5ebe-e69e-49d6-8326-42374947f6fb" -->
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

<!-- section_id: "8f1df94d-4446-4ada-ac7d-0aa4989ccdf1" -->
## Shim Templates

<!-- section_id: "2932b0b3-a030-4738-9037-684dfda052af" -->
### Claude Shim (prepended to AGNOSTIC.md)

```markdown
# CLAUDE.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

<!-- section_id: "08f3b590-9b88-419f-acb4-1e75e33de656" -->
### Codex/AGENTS.md Shim

```markdown
# AGENTS.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

<!-- section_id: "8cf374f6-1a04-40c9-ae19-0d9b2f948ec8" -->
### Gemini Shim

```markdown
# GEMINI.md - Auto-generated from AGNOSTIC.md
# DO NOT EDIT - Changes will be overwritten
# Edit AGNOSTIC.md instead, then run: agnostic-sync

```

<!-- section_id: "5646d620-ac65-44ae-9d51-6cfa31bd092d" -->
## Sync Script Behavior

<!-- section_id: "57b58a96-77d4-4750-9269-205c9d181cb8" -->
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

<!-- section_id: "e9dab4f9-634c-4003-b27b-e79c3d439e3f" -->
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

<!-- section_id: "cef57e01-51a2-48c3-a0b0-15196812021d" -->
### File Preservation Rules

Files in tool-specific folders that should NOT be overwritten:
- `settings.json` - Tool configuration
- `mcp.json` - MCP server configuration
- Any file with `# MANUAL` comment in first line

<!-- section_id: "7abcaf16-904a-4a16-bc1f-be7466b0e78b" -->
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

<!-- section_id: "90591386-2f6f-494d-897a-5ac292765e21" -->
## Implementation Plan

1. **Phase 1**: Bash script for basic sync
2. **Phase 2**: Add watch mode with inotifywait/fswatch
3. **Phase 3**: Add git hook for auto-sync on commit
4. **Phase 4**: Optional Python/Node version for complex transformations

---

<!-- section_id: "58e3a2aa-69b1-4d8d-b96d-dc9894501800" -->
## Related Files

- Template: `../agnostic_templates/AGNOSTIC.md.template`
- Script: `scripts/agnostic-sync.sh`
