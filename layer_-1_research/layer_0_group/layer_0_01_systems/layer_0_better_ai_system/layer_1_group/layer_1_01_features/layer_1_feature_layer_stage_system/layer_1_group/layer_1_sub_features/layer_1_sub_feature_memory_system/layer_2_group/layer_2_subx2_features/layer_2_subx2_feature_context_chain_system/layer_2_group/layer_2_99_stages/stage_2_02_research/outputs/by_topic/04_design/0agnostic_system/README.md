---
resource_id: "6f90ee3f-baca-436f-9d04-37124ea8999a"
resource_type: "readme
output"
resource_name: "README"
---
# The 0Agnostic System

## Purpose

A complete, tool-agnostic context management system that stores all AI context in a single source of truth (`.0agnostic/` and `0AGNOSTIC.md`) and syncs it to every AI tool's native format — with multi-avenue redundancy ensuring context is loaded even when individual avenues fail.

---

## What It Is

The 0Agnostic System solves a fundamental problem: **AI tools each have their own context format, but you want a single source of truth.** Instead of maintaining separate CLAUDE.md, AGENTS.md, GEMINI.md, and .cursorrules files manually, you maintain one agnostic source and generate tool-specific files from it.

```
                ┌──────────────────────┐
                │    0AGNOSTIC.md      │  ← Source of truth (system prompt content)
                │    .0agnostic/       │  ← Source of truth (on-demand content)
                │    .1merge/          │  ← Tool-specific overrides
                └──────────┬───────────┘
                           │
                    agnostic-sync.sh
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
   ┌───────────┐    ┌───────────┐    ┌───────────┐
   │ .claude/   │    │ .cursor/   │    │ .codex/    │  ... (per tool)
   │ CLAUDE.md  │    │ rules/     │    │ AGENTS.md  │
   │ rules/     │    │            │    │            │
   │ skills/    │    │            │    │            │
   └───────────┘    └───────────┘    └───────────┘
```

---

## System Components

The 0Agnostic System has four components. Each is documented in a dedicated file:

### 1. [Internal Structure](internal_structure.md)
The canonical directory structure inside `.0agnostic/`:
- `knowledge/` (with `principles/` and `resources/`)
- `rules/` (with `static/` and `dynamic/`)
- `protocols/`
- Plus existing: `skills/`, `agents/`, `episodic_memory/`, `hooks/`, `scripts/`, `templates/`, `tests/`

Covers how rules inform protocols, the relationship between static rules (full protocol inline) and dynamic rules (triggers only, reference protocols), and how knowledge/resources provide supporting material.

### 2. [Sync System](sync_system.md)
How `agnostic-sync.sh` transforms agnostic content into tool-specific formats:
- `0AGNOSTIC.md` → CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md
- `rules/static/` → `.claude/rules/`, `.cursor/rules/` (format-transformed)
- `rules/dynamic/` → `.claude/rules/` (with YAML frontmatter)
- `protocols/` → `.claude/skills/` (as SKILL.md format)
- How the sync handles format differences between tools

### 3. [.1merge Override System](merge_system.md)
The three-tier merge system for tool-specific customizations:
- Tier 1: `.0agnostic/` (agnostic source)
- Tier 2: `.1merge/.1{tool}_merge/` (tool-specific overrides)
- Tier 3: `.claude/` / `.cursor/` / `.codex/` (generated output)
- When to use overrides vs agnostic content

### 4. [Multi-Avenue Redundancy](multi_avenue_redundancy.md)
How all context chaining avenues link together per tool:
- 8 avenues: system prompt, path rules, skills, @imports, JSON-LD/jq, .integration.md, episodic memory, 0AGNOSTIC.md
- Effectiveness matrix per tool (Claude Code, Codex CLI, Gemini CLI, OpenCode, Cursor, Aider)
- How AALang/GAB and JSON-LD integrate
- How the system prompt ties all avenues together
- The "any-one-fires" resilience model

---

## How It All Connects

```
0AGNOSTIC.md (Avenue 1: system prompt source)
    │
    ├──→ agnostic-sync.sh ──→ CLAUDE.md / AGENTS.md / GEMINI.md
    │                              │
    │                              ├── Trigger tables → point to skills (Avenue 3)
    │                              ├── @import refs → point to knowledge (Avenue 4)
    │                              ├── jq instructions → point to .gab.jsonld (Avenue 5)
    │                              └── Pointers → .integration.md (Avenue 6)
    │
.0agnostic/
    │
    ├── rules/static/ ──sync──→ .claude/rules/ (Avenue 2, auto-loaded)
    │     └── Include full protocol inline
    │
    ├── rules/dynamic/ ──sync──→ .claude/rules/ (Avenue 2, path-scoped)
    │     └── Triggers only → reference protocols/
    │
    ├── protocols/ ──sync──→ .claude/skills/ (Avenue 3, progressive disclosure)
    │     └── Full procedures, referenced by dynamic rules
    │
    ├── knowledge/ ──stay──→ .0agnostic/knowledge/ (Avenue 4/8, on-demand)
    │     ├── principles/
    │     └── resources/ (templates, databases, reference material)
    │
    └── skills/ ──sync──→ .claude/skills/ (Avenue 3)

.1merge/
    ├── .1claude_merge/ ──merge──→ .claude/ (tool-specific additions)
    ├── .1cursor_merge/ ──merge──→ .cursor/
    └── .1codex_merge/ ──merge──→ .codex/
```

**The design principle:** Every piece of context is reachable through multiple independent avenues. If the system prompt (Avenue 1) is ignored, path rules (Avenue 2) fire automatically. If skills (Avenue 3) don't auto-invoke, the rules name them explicitly. If @imports (Avenue 4) aren't followed, integration summaries (Avenue 6) contain the same information. **Only one avenue needs to work.**

---

## Related Documents

| Document | Location |
|----------|----------|
| Sub-layers vs dot-folders research | [sublayers_vs_dot_folders.md](../sublayers_vs_dot_folders.md) |
| Sub-layer migration map | [sub_layer_migration_map.md](../sub_layer_migration_map.md) |
| Referencing methods survey | [referencing_methods_and_skill_invocation.md](../referencing_methods_and_skill_invocation.md) |
| Skill reliability per tool | [skill_reliability_per_tool.md](../../03_obstacles/skill_reliability_per_tool.md) |
| Context system vision | [context_system_vision.md](../../01_vision/context_system_vision.md) |

---

*0Agnostic System design overview*
*Created: 2026-02-16*
