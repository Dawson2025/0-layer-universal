---
resource_id: "fde0b69a-87c7-4a8d-a48d-a7d647b7948f"
resource_type: "output"
resource_name: "sync_system"
---
# Sync System — agnostic-sync.sh

## Purpose

How `agnostic-sync.sh` transforms agnostic source content into tool-specific formats. The sync system is the bridge between the single source of truth (`.0agnostic/` + `0AGNOSTIC.md`) and the tool-specific dot folders that each AI tool reads natively.

---

## What Gets Synced

```
Source (agnostic)                    Target (tool-specific)
─────────────────                    ──────────────────────

0AGNOSTIC.md                    ──→  CLAUDE.md
                                ──→  AGENTS.md
                                ──→  GEMINI.md
                                ──→  OPENAI.md

.0agnostic/rules/static/*.md   ──→  .claude/rules/*.md          (copy, auto-loaded)
                                ──→  .cursor/rules/*.mdc         (transform to .mdc)
                                ──→  Appended to AGENTS.md       (inline rules section)

.0agnostic/rules/dynamic/*.md  ──→  .claude/rules/*.md          (copy, keep paths: frontmatter)
                                ──→  .cursor/rules/*.mdc         (transform, add glob metadata)

.0agnostic/protocols/*.md      ──→  .claude/skills/*/SKILL.md   (transform to skill format)
                                ──→  .codex/.agents/skills/      (copy to Codex skill location)

.0agnostic/skills/             ──→  .claude/skills/             (copy)
                                ──→  .codex/.agents/skills/      (copy)

.0agnostic/knowledge/          ──→  NOT SYNCED (stays in .0agnostic/, accessed on-demand)

.0agnostic/agents/             ──→  .claude/agents/             (copy)

.1merge/.1claude_merge/        ──→  Merged INTO .claude/        (tool-specific overrides)
.1merge/.1cursor_merge/        ──→  Merged INTO .cursor/
.1merge/.1codex_merge/         ──→  Merged INTO .codex/
.1merge/.1gemini_merge/        ──→  Merged INTO .gemini/
```

---

## 0AGNOSTIC.md → Tool-Specific System Prompt Files

### What the Script Does

The current `agnostic-sync.sh` reads `0AGNOSTIC.md` and extracts key sections:

1. **Identity** — Role, scope, parent/child context
2. **Navigation** — Key locations and references
3. **Critical Rules** — Must-follow constraints (if section exists)
4. **Key Behaviors** — Agent behavior patterns
5. **Triggers** — Situation → action mappings

Each tool file gets the same core sections, plus tool-specific additions:

| Tool File | Core Sections | Tool-Specific Additions |
|-----------|--------------|------------------------|
| `CLAUDE.md` | All | `## Claude-Specific Rules` (CLAUDE.md integration notes, tool usage, session continuity) |
| `AGENTS.md` | All | Agent registration config format |
| `GEMINI.md` | All | Resource loading hints |
| `OPENAI.md` | All | Function calling notes |

### Required Sections

- **Identity** and **Navigation** are required — sync fails without them
- **Critical Rules**, **Key Behaviors**, **Triggers** are optional but warned if missing

### Section Extraction

The script uses sed to match h2 headings (`^## [^#]`) — this pattern deliberately avoids matching h3+ headings, allowing subsections within each section.

---

## Rules Sync: Static → .claude/rules/

### Current Behavior (Needs Extension)

Currently, `agnostic-sync.sh` only generates system prompt files. It needs to be extended to also sync rules.

### Target Behavior

**Static rules** are copied directly:
```
.0agnostic/rules/static/context_modification.md
  ──copy──→ .claude/rules/context_modification.md
```

No transformation needed — Claude Code reads `.md` files in `.claude/rules/` as-is.

**For Cursor**, the `.md` is transformed to `.mdc` format:
```
.0agnostic/rules/static/context_modification.md
  ──transform──→ .cursor/rules/context_modification.mdc
```

The `.mdc` transformation adds Cursor-specific metadata headers.

### Static Rules Include Full Protocol

Because static rules include their protocol inline (see [internal_structure.md](internal_structure.md)), the synced file in `.claude/rules/` contains both the constraint AND the procedure. The agent sees the complete instruction when the rule auto-loads.

---

## Rules Sync: Dynamic → .claude/rules/ (with paths:)

**Dynamic rules** must have YAML frontmatter with `paths:` to enable path-scoping:

```yaml
---
paths: layer_-1_research/**
---
# Trigger: Research Stage Workflow
...
```

If the source file in `.0agnostic/rules/dynamic/` already has `paths:` frontmatter, it's copied as-is. If not, the sync script should warn that a dynamic rule is missing path scoping.

**For Cursor**, dynamic rules become auto-attach `.mdc` files with glob patterns in their metadata.

---

## Protocols Sync: → .claude/skills/

Protocols are transformed into the Claude Code skill format:

**Source** (`.0agnostic/protocols/entity_creation.md`):
```markdown
# Protocol: Entity Creation

## Prerequisites
- Current layer and stage identified

## Steps
1. Read entity structure template
2. Create directory structure
3. Create 0AGNOSTIC.md
...
```

**Target** (`.claude/skills/entity-creation/SKILL.md`):
```markdown
---
description: |
  Create new entities (projects, features, sub-features) with proper
  directory structure, 0AGNOSTIC.md, and agnostic sync.
  WHEN: Creating new projects, features, sub-features, or components.
  WHEN NOT: Modifying existing entities. Use stage-workflow instead.
---

# Entity Creation Protocol

## Prerequisites
- Current layer and stage identified

## Steps
1. Read entity structure template
...
```

The transformation:
1. Creates a directory named after the protocol (kebab-case)
2. Adds YAML frontmatter with `description:`, `WHEN:`, `WHEN NOT:`
3. Keeps the protocol content as the skill body
4. The skill description loads at session start; full content loads on invocation

**For Codex CLI**, protocols are copied to `.agents/skills/` in Codex's expected format.

---

## .1merge Application (Post-Sync)

After syncing from `.0agnostic/`, the script applies `.1merge/` overrides. See [merge_system.md](merge_system.md) for details.

---

## Sync Workflow

```
Developer edits 0AGNOSTIC.md or files in .0agnostic/
    │
    ▼
Runs: agnostic-sync.sh [directory]
    │
    ├── 1. Read 0AGNOSTIC.md → Generate CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md
    ├── 2. Copy rules/static/ → .claude/rules/ (+ transform for other tools)
    ├── 3. Copy rules/dynamic/ → .claude/rules/ (verify paths: frontmatter)
    ├── 4. Transform protocols/ → .claude/skills/ (add YAML frontmatter)
    ├── 5. Copy skills/ → .claude/skills/ (if not already synced)
    ├── 6. Copy agents/ → .claude/agents/
    └── 7. Apply .1merge/ overrides
    │
    ▼
Developer commits generated files alongside source files
```

### When to Sync

- After editing `0AGNOSTIC.md`
- After adding, modifying, or removing files in `.0agnostic/rules/`, `.0agnostic/protocols/`, or `.0agnostic/skills/`
- After modifying `.1merge/` overrides
- Before committing (can be enforced via pre-commit hook)

### Sync Validation

The script should validate:
- All dynamic rules have `paths:` frontmatter
- No broken @import references in generated files
- Skill descriptions fit within the ~16K char budget
- Generated files are not newer than their sources (no stale state)

---

*Sync system documentation for the 0Agnostic System*
*Created: 2026-02-16*
