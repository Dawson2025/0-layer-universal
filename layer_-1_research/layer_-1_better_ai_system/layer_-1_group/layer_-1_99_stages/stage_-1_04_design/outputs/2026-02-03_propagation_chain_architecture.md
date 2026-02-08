# Propagation Chain Architecture - 2026-02-03

## Source

User requirements from session 2026-02-03.

---

## Overview

AI context flows through a propagation chain from source of truth to agent action.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROPAGATION CHAIN ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER 1: KNOWLEDGE (Source of truth for CONTENT)                          │
│  ─────────────────────────────────────────────────                          │
│                                                                             │
│  sub_layer_0_02_knowledge_system/                                          │
│  ├── layer_stage_system/STAGES_EXPLAINED.md    ← Stage Completeness Rule   │
│  ├── AI_CONTEXT_FLOW_ARCHITECTURE.md           ← This architecture         │
│  └── agent_coordination/                       ← Multi-agent patterns      │
│                                                                             │
│  sub_layer_0_04_rules/                                                     │
│  └── AI_CONTEXT_PROPOSAL_REQUIREMENTS.md       ← Diagram requirements      │
│                                                                             │
│       │                                                                     │
│       │ referenced by                                                      │
│       ▼                                                                     │
│                                                                             │
│  LAYER 2: AGNOSTIC SOURCE (Source of truth for SKILLS)                     │
│  ─────────────────────────────────────────────────────                      │
│                                                                             │
│  0AGNOSTIC.md                     ← Identity, critical rules, triggers     │
│                                                                             │
│  .0agnostic/                                                               │
│  ├── skills/                                                               │
│  │   ├── SKILLS.md                ← Index of skills                        │
│  │   ├── entity-creation/                                                  │
│  │   │   ├── SKILL.md             ← Protocol                               │
│  │   │   └── references/          ← Pointers to knowledge                  │
│  │   └── stage-workflow/                                                   │
│  │       ├── SKILL.md                                                      │
│  │       └── references/                                                   │
│  ├── hooks/scripts/               ← agnostic-sync.sh                       │
│  ├── agents/                                                               │
│  └── episodic/                                                             │
│                                                                             │
│       │                                                                     │
│       │ agnostic-sync.sh generates                                         │
│       ▼                                                                     │
│                                                                             │
│  LAYER 3: TOOL-SPECIFIC FILES (Generated, minimal)                         │
│  ─────────────────────────────────────────────────                          │
│                                                                             │
│  CLAUDE.md ─────────────▶ .claude/                                         │
│  │ - Identity                     ├── settings.json                        │
│  │ - Critical rules               ├── commands/                            │
│  │ - Triggers                     └── skills/                              │
│  │ - Pointers                         ├── SKILLS.md                        │
│  │                                    ├── entity-creation/SKILL.md         │
│  │                                    └── stage-workflow/SKILL.md          │
│  │                                                                         │
│  GEMINI.md ────────────▶ .gemini/                                          │
│  AGENTS.md ────────────▶ .codex/                                           │
│  .cursorrules                                                              │
│                                                                             │
│       │                                                                     │
│       │ agent loads                                                        │
│       ▼                                                                     │
│                                                                             │
│  LAYER 4: AGENT ACTION                                                     │
│  ─────────────────────                                                      │
│                                                                             │
│  Agent reads CLAUDE.md                                                     │
│       │                                                                     │
│       ▼                                                                     │
│  Agent loads skill from .claude/skills/                                    │
│       │                                                                     │
│       ▼                                                                     │
│  Skill references knowledge in sub_layers                                  │
│       │                                                                     │
│       ▼                                                                     │
│  Agent follows rules from knowledge                                        │
│       │                                                                     │
│       ▼                                                                     │
│  Agent executes task correctly                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Design Decisions

### 1. Knowledge is Source of Truth

- Rules and content live in `sub_layer_0_02_knowledge_system/` and `sub_layer_0_04_rules/`
- Skills reference this knowledge, don't duplicate
- Changes in one place propagate everywhere

### 2. Skills are the Bridge

- Skills contain protocols (how to do a task)
- Skills have `references/` pointing to knowledge
- Agents load skills based on task triggers

### 3. CLAUDE.md is Minimal

- Only identity, critical rules, triggers, pointers
- Points to `.claude/skills/` for detailed instructions
- Generated from `0AGNOSTIC.md` via sync

### 4. .1merge Consolidation

- All tool-specific merge folders under single `.1merge/`
- Original names preserved (`.1claude_merge/`, `.1gemini_merge/`, etc.)
- Cleaner root directory

```
.1merge/
├── .1aider_merge/
├── .1claude_merge/
├── .1codex_merge/
├── .1copilot_merge/
├── .1cursor_merge/
└── .1gemini_merge/
```

---

## Implementation Status

| Component | Status | Location |
|-----------|--------|----------|
| STAGES_EXPLAINED.md | ✅ Created | `layer_0/.../layer_stage_system/` |
| AI_CONTEXT_FLOW_ARCHITECTURE.md | ✅ Updated | `layer_0/.../sub_layer_0_02_knowledge_system/` |
| 0AGNOSTIC.md | ✅ Created | `0_layer_universal/` |
| .0agnostic/skills/ | ✅ Created | `0_layer_universal/` |
| .claude/skills/ | ✅ Updated | `0_layer_universal/` |
| .1merge/ consolidation | ✅ Done | `layer_-1_better_ai_system/` |

---

## Related Documents

- [../stage_-1_01_request_gathering/outputs/2026-02-03_user_requirements.md](../stage_-1_01_request_gathering/outputs/2026-02-03_user_requirements.md)
- [../stage_-1_03_instructions/outputs/2026-02-03_context_flow_constraints.md](../stage_-1_03_instructions/outputs/2026-02-03_context_flow_constraints.md)
