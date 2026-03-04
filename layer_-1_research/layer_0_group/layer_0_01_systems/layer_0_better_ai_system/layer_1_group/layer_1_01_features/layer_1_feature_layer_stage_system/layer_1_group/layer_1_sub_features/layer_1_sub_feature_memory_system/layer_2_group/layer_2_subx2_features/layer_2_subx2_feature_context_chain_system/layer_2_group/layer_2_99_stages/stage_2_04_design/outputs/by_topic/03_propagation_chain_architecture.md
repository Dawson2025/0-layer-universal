# Propagation Chain Architecture

**Date**: 2026-02-23
**Status**: Approved and implemented
**Scope**: How context flows from source of truth to agent action through a 4-layer propagation chain

---

## Overview

AI context flows through a **propagation chain** — a directed pipeline from canonical source material to the moment an agent acts on it. Every piece of context an agent uses has traversed this chain, whether explicitly or implicitly.

The chain has 4 layers, each with a distinct role:

```
Layer 1: KNOWLEDGE (source of truth for CONTENT)
    │
    │ referenced by
    ▼
Layer 2: AGNOSTIC SOURCE (source of truth for IDENTITY + SKILLS)
    │
    │ agnostic-sync.sh generates
    ▼
Layer 3: TOOL-SPECIFIC FILES (generated, minimal, tool-native)
    │
    │ agent loads at session start
    ▼
Layer 4: AGENT ACTION (runtime execution)
```

---

## Layer 1: Knowledge (Content Source of Truth)

The deepest layer. Content lives in `.0agnostic/` numbered directories:

```
.0agnostic/
├── 01_knowledge/       Domain knowledge, architecture docs, principles
├── 02_rules/           Behavioral constraints (static + dynamic)
│   ├── static/         Always-apply rules
│   └── dynamic/        Scenario-triggered rules
├── 03_protocols/       Step-by-step procedures
├── 04_episodic_memory/ Session history, change logs
└── 05_handoff_documents/ Cross-entity/stage communication
```

**Properties**:
- Human-authored and agent-authored
- Tool-agnostic — no tool-specific concepts
- The canonical location for all domain knowledge
- Read on-demand, not always-loaded (too large for static context)

**Key principle**: Knowledge is the deepest tier. Everything downstream derives from or references content here. Changes here propagate outward through the chain.

---

## Layer 2: Agnostic Source (Identity + Skills)

The hub layer. `0AGNOSTIC.md` is the single entry point for any entity:

```
0AGNOSTIC.md
├── STATIC (always loaded):
│   ├── Identity — who this entity is, scope, parent reference
│   ├── Key Behaviors — what this entity does, delegation model
│   ├── Triggers — when to load this context
│   ├── Navigation — how to find resources
│   └── Current Status — most distilled state summary
│
└── DYNAMIC (loaded on-demand):
    ├── Stage Management — stage-by-stage state
    ├── Entity Instantiation — how to create children
    ├── Agent Management — how to spawn agents
    └── Research History — pointers to detailed findings
```

**Adjacent structures**:

```
.0agnostic/06_context_avenue_web/   Delivery mechanisms (avenues)
├── 00_registry/                     Management hub
├── 01_file_based/ (01-08)           Deterministic transforms
└── 02_data_based/ (09-13)           Derived indexes (future)

.0agnostic/07+_setup_dependant/     Environment-specific config
```

`.claude/skills/` — procedural instructions with WHEN/WHEN NOT conditions
`.claude/rules/`  — path-scoped rules triggered by directory entry

**Properties**:
- 0AGNOSTIC.md is the single source of truth per entity
- References Layer 1 content by relative path
- Skills bridge from static triggers to dynamic knowledge loading
- This layer is where `agnostic-sync.sh` reads from

---

## Layer 3: Tool-Specific Files (Generated)

Generated files that tool runtimes auto-load:

```
agnostic-sync.sh transforms 0AGNOSTIC.md STATIC content into:

├── CLAUDE.md                        Claude Code (full static + promoted rules)
├── AGENTS.md                        AutoGen / Codex (full static + promoted rules)
├── GEMINI.md                        Google Gemini (full static + promoted rules)
├── OPENAI.md                        OpenAI (full static + promoted rules)
├── .cursorrules                     Cursor IDE (lean: Identity + Navigation)
└── .github/copilot-instructions.md  GitHub Copilot (medium)
```

**The .1merge override system**:

```
.1merge/
├── .1claude_merge/
│   ├── 0_synced/          ← From 0AGNOSTIC (auto-generated, do not edit)
│   ├── 1_overrides/       ← Tool-specific replacements (replaces default boilerplate)
│   └── 2_additions/       ← Tool-only content (appended to generated file)
├── .1gemini_merge/
└── ...
```

The 3-tier merge ensures:
- `0_synced/` keeps tool files in sync with 0AGNOSTIC.md automatically
- `1_overrides/` allows replacing default boilerplate per tool
- `2_additions/` allows injecting tool-specific content (e.g., browser extraction capabilities only in CLAUDE.md)

**Properties**:
- Generated — never edit directly
- Minimal — only STATIC content from 0AGNOSTIC.md + promoted rules + .1merge additions
- Tool-native — each file follows the conventions of its target tool
- The primary static context surface for agents

---

## Layer 4: Agent Action (Runtime)

The agent loads context and acts:

```
Agent enters entity
    │
    ▼
1. Reads CLAUDE.md (auto-loaded by Claude Code via filesystem walk)
    │
    ▼
2. Checks .claude/rules/ (auto-loaded on directory entry)
    │
    ▼
3. Matches skills (WHEN conditions against current task)
    │
    ▼
4. Skill references knowledge in .0agnostic/ (on-demand read)
    │
    ▼
5. Agent follows rules from knowledge
    │
    ▼
6. Agent executes task correctly
```

**Properties**:
- Progressive disclosure — starts with minimal static context, loads more on demand
- Any-one-fires resilience — if one avenue fails, others provide the same context
- Token-efficient — only loads what's needed for the current task

---

## Chain Integrity Rules

1. **Single direction of authority**: Layer 1 → Layer 2 → Layer 3 → Layer 4. Never reverse.
2. **No duplication across layers**: Knowledge lives in Layer 1 only. Layer 2 references it. Layer 3 summarizes Layer 2. Layer 4 loads what it needs.
3. **Changes propagate outward**: Edit .0agnostic/ content (Layer 1), update 0AGNOSTIC.md references (Layer 1), run agnostic-sync.sh (Layer 2), agent picks it up (Layer 3).
4. **Traceability**: Every piece of runtime context must be traceable back to its canonical source path and merge tier.
5. **Reproducibility**: Generated files (Layer 2) must be exactly reproducible from Layer 1 + Layer 2 + .1merge rules.

---

## Implementation Status

| Layer | Component | Status |
|-------|-----------|--------|
| 1 | .0agnostic/ numbered dirs (01-05) | Implemented |
| 1 | Static + dynamic rules | Implemented (5 static, 4 dynamic at this entity) |
| 2 | 0AGNOSTIC.md as source of truth | Implemented |
| 2 | Skills with WHEN/WHEN NOT | Implemented (2 entity-local + 5 universal) |
| 2 | Avenue web (06_context_avenue_web/) | Implemented (01-08 file-based) |
| 3 | agnostic-sync.sh with .1merge | Implemented (6 tool files generated) |
| 3 | Hot rule promotion (frontmatter) | Implemented (promote: hot in rules) |
| 3 | PostToolUse hook | Implemented (agnostic-edit-guard.sh) |
| 4 | CLAUDE.md cascade loading | Implemented (7-level chain validated) |
| 4 | Path rule auto-loading | Implemented |
| 4 | Skill discovery chain | Validated end-to-end |

---

## Related Documents

- **Bottom-up propagation**: `04_context_propagation_funnel.md` (how work products consolidate upward)
- **Discovery temperatures**: `08_discovery_temperature_model.md` (Hot/Warm/Cold loading)
- **Sync architecture**: `07_unified_sync_architecture.md` (sync-main.sh orchestrator)
- **Avenue web design**: `01_context_chain_system_design.md` (8-avenue MVP)
- **Integration design**: `02_0agnostic_1merge_avenue_web_integration_design.md` (.0agnostic + .1merge + avenue web)
