# Proposal v6: Complete AI System Architecture (Final Corrections)

**Date**: 2026-02-03
**Version**: 6.0
**Status**: Proposal (Pending Review)
**Previous Versions**: v1-v5 (SUPERSEDED)
**Supersedes**: v1, v2, v3, v4, and v5

---

## What v6 Corrects Over v5

| Issue in v5 | v6 Correction |
|-------------|---------------|
| Group folders not named as groups | `layer_N_group/` and `layer_N+1_group/` naming |
| Missing sub^n naming conventions | Full depth: sub_, subx2_, subx3_, subxN_ patterns |
| Missing merge flow to system prompts | Explicit 0AGNOSTIC.md → CLAUDE.md/GEMINI.md/AGENTS.md flow |
| Stage missing system prompt variants | All stages have CLAUDE.md, GEMINI.md, AGENTS.md |
| Proposals not in subdirectories | `outputs/proposals/` subdirectory in each stage |
| Diagrams don't show context flow | AI agent entry → triggers → pointers flow |
| Missing setup-dependent sub-layers | Include sub_layer_N_05+_setup_dependant/ |

---

## Part 1: Core Architecture Principles

### 1.1 Content vs Config Separation

**CRITICAL DISTINCTION**:

| Type | Location | Examples |
|------|----------|----------|
| **Content** (knowledge, prompts, rules, principles) | `layer_N_group/layer_N_03_sub_layers/` | Rules, prompts, knowledge docs |
| **AI Config** (agents, hooks, skills, episodic) | `.0agnostic/` → `.claude/` | Agent configs, session memory |

**Why?**
- Content cascades through layer hierarchy naturally
- AI config is tool-specific infrastructure
- No duplication - single source of truth for each

### 1.2 The Two-Folder Structure (Layer Grouping)

Every entity has TWO sibling **GROUP folders** (named with `_group` suffix):

```
layer_N_<type>_<name>/              # THE ENTITY
├── layer_N_group/                  # GROUP: Entity's INTERNALS
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_01_ai_manager_system/
│   ├── layer_N_02_manager_handoff_documents/
│   ├── layer_N_03_sub_layers/      # ← CONTENT lives here
│   │   ├── sub_layer_N_00_sub_layer_registry/
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   ├── sub_layer_N_04_rules/
│   │   └── sub_layer_N_05+_setup_dependant/         # Container for 05+
│   │       ├── sub_layer_N_05_<name>/               # e.g., operating_systems
│   │       ├── sub_layer_N_06_<name>/               # e.g., ide_configs
│   │       └── sub_layer_N_XX_<name>/               # (as many as needed)
│   └── layer_N_99_stages/
│
└── layer_N+1_group/                # GROUP: CHILDREN
    ├── layer_N+1_features/         # (or sub_features if this is a feature)
    ├── layer_N+1_components/       # (or sub_components if this is a component)
    └── layer_N+1_sub_projects/     # (only if this is a project)
```

### 1.3 Naming Conventions

#### Entity Types (Depth 0)

| Entity Type | Name Pattern | Example |
|-------------|--------------|---------|
| Project | `layer_N_project_<name>` | `layer_1_project_my_app` |
| Feature | `layer_N_feature_<name>` | `layer_0_feature_ai_context_system` |
| Component | `layer_N_component_<name>` | `layer_1_component_auth` |

#### Sub-Entities (Depth 1)

| Entity Type | Name Pattern | Example |
|-------------|--------------|---------|
| Sub-project | `layer_N_sub_project_<name>` | `layer_2_sub_project_api` |
| Sub-feature | `layer_N_sub_feature_<name>` | `layer_1_sub_feature_login` |
| Sub-component | `layer_N_sub_component_<name>` | `layer_2_sub_component_button` |

#### Depth 2 Entities (subx2)

| Entity Type | Name Pattern | Example |
|-------------|--------------|---------|
| Subx2-project | `layer_N_subx2_project_<name>` | `layer_3_subx2_project_auth_api` |
| Subx2-feature | `layer_N_subx2_feature_<name>` | `layer_2_subx2_feature_oauth` |
| Subx2-component | `layer_N_subx2_component_<name>` | `layer_3_subx2_component_icon` |

#### Depth 3 Entities (subx3)

| Entity Type | Name Pattern | Example |
|-------------|--------------|---------|
| Subx3-project | `layer_N_subx3_project_<name>` | `layer_4_subx3_project_endpoints` |
| Subx3-feature | `layer_N_subx3_feature_<name>` | `layer_3_subx3_feature_token_refresh` |
| Subx3-component | `layer_N_subx3_component_<name>` | `layer_4_subx3_component_tooltip` |

#### Arbitrary Depth (Depth n) - subxN

| Depth | Prefix Pattern | Example |
|-------|----------------|---------|
| 1 | `sub_` | `layer_2_sub_feature_<name>` |
| 2 | `subx2_` | `layer_3_subx2_feature_<name>` |
| 3 | `subx3_` | `layer_4_subx3_feature_<name>` |
| 4 | `subx4_` | `layer_5_subx4_feature_<name>` |
| n | `subxN_` | `layer_M_subxN_<type>_<name>` |

**Note**: If nesting gets deep (>3), consider restructuring. Deep nesting usually indicates the parent entity is too large and should be split.

#### Group Folders

| Group Type | Name Pattern | Contains |
|------------|--------------|----------|
| Internal group | `layer_N_group/` | Entity's own internals |
| Children group | `layer_N+1_group/` | Entity's children |

**Layer numbers are ALWAYS in the name** to indicate specificity level.

---

## Part 2: .0agnostic/ Structure (AI Config Only)

### 2.1 What Goes in .0agnostic/

```
.0agnostic/                    # AI INFRASTRUCTURE (not content!)
├── agents/                    # Agent configurations
│   ├── researcher.md
│   └── implementer.md
├── episodic/                  # Session memory
│   ├── index.md
│   ├── sessions/
│   └── changes/
├── hooks/                     # Event hooks
│   └── scripts/
│       ├── agnostic-sync.sh
│       └── save-session.sh
├── skills/                    # Skill definitions
│   ├── research-workflow/
│   └── handoff-protocol/
└── sync-config.yaml           # Sync configuration
```

### 2.2 What Does NOT Go in .0agnostic/

| DON'T Put Here | Put Here Instead |
|----------------|------------------|
| Rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Prompts | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_01_prompts/` |
| Knowledge | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Principles | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_03_principles/` |

---

## Part 3: 0AGNOSTIC.md Template (Short - Pointers Only)

**CRITICAL**: 0AGNOSTIC.md should be SHORT. It contains Identity, Triggers, and **POINTERS** to resources.

```markdown
# 0AGNOSTIC.md - [Entity Name]

## Identity

You are an agent at **Layer [N]**, **[type]**: [name].

- **Role**: [Brief role description]
- **Scope**: [What's in/out of scope]
- **Parent**: `../0AGNOSTIC.md`
- **Children**: `layer_N+1_group/` contains [list or "None"]

## Triggers

Load this context when:
- User mentions: [keywords]
- Working on: [task types]
- Entering: [paths]

## Pointers

### On Entry
1. Read `0INDEX.md` for current state
2. Check `.0agnostic/episodic/index.md` for recent sessions

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Agents | `.0agnostic/agents/` |
| Skills | `.0agnostic/skills/` |

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Children | `layer_N+1_group/` |
| Stages | `layer_N_group/layer_N_99_stages/` |

## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research | `layer_N_group/layer_N_99_stages/stage_N_02_research/outputs/` |
| Instructions | `layer_N_group/layer_N_99_stages/stage_N_03_instructions/outputs/` |
| Proposals | `layer_N_group/layer_N_99_stages/stage_N_XX_*/outputs/proposals/` |
| Session notes | `.0agnostic/episodic/sessions/` |
```

---

## Part 4: System Prompt Generation Flow

### 4.1 How 0AGNOSTIC.md Becomes Tool-Specific System Prompts

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SYSTEM PROMPT GENERATION FLOW                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SOURCE (edit here only)                          │   │
│   │                                                                     │   │
│   │   0AGNOSTIC.md                                                      │   │
│   │   ┌──────────────────────────────────────────────────────────────┐  │   │
│   │   │ ## Identity                                                  │  │   │
│   │   │ ## Triggers                                                  │  │   │
│   │   │ ## Pointers (to .0agnostic/, sub_layers, etc.)              │  │   │
│   │   └──────────────────────────────────────────────────────────────┘  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                         agnostic-sync.sh                                    │
│                                      │                                      │
│              ┌───────────────────────┼───────────────────────┐              │
│              │                       │                       │              │
│              ▼                       ▼                       ▼              │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│   │ .1claude_merge/ │    │ .1cursor_merge/ │    │ .1gemini_merge/ │  ...   │
│   │                 │    │                 │    │                 │        │
│   │ 0_synced/       │    │ 0_synced/       │    │ 0_synced/       │        │
│   │   (from .0agnostic)  │   (from .0agnostic)  │   (from .0agnostic)      │
│   │ 1_overrides/    │    │ 1_overrides/    │    │ 1_overrides/    │        │
│   │   (tool-specific)    │   (tool-specific)    │   (tool-specific)        │
│   │ 2_additions/    │    │ 2_additions/    │    │ 2_additions/    │        │
│   │   (tool-only)        │   (tool-only)        │   (tool-only)            │
│   │ CLAUDE.override.md   │ CURSOR.override.md   │ GEMINI.override.md       │
│   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘        │
│            │                      │                      │                  │
│            ▼                      ▼                      ▼                  │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│   │  CLAUDE.md      │    │  .cursorrules   │    │  GEMINI.md      │        │
│   │  .claude/       │    │  .cursor/rules/ │    │                 │        │
│   │                 │    │                 │    │                 │        │
│   │  (Claude reads) │    │  (Cursor reads) │    │  (Gemini reads) │        │
│   └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│                                                                             │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│   │ .1copilot_merge/│    │ .1aider_merge/  │    │ .1codex_merge/  │  ...   │
│   └────────┬────────┘    └────────┬────────┘    └────────┬────────┘        │
│            │                      │                      │                  │
│            ▼                      ▼                      ▼                  │
│   ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        │
│   │ .github/        │    │ .aider.conf.yml │    │  AGENTS.md      │        │
│   │ copilot-*.md    │    │                 │    │                 │        │
│   │                 │    │                 │    │                 │        │
│   │ (Copilot reads) │    │  (Aider reads)  │    │  (Codex reads)  │        │
│   └─────────────────┘    └─────────────────┘    └─────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Generated System Prompt Files

| Tool | Generated File(s) | Merge Source |
|------|-------------------|--------------|
| Claude Code | `CLAUDE.md`, `.claude/` | `.1claude_merge/` |
| Cursor | `.cursorrules`, `.cursor/rules/` | `.1cursor_merge/` |
| Copilot | `.github/copilot-instructions.md`, `.github/instructions/` | `.1copilot_merge/` |
| Gemini | `GEMINI.md` | `.1gemini_merge/` |
| Aider | `.aider.conf.yml` | `.1aider_merge/` |
| Codex | `AGENTS.md` | `.1codex_merge/` |

---

## Part 5: Full Entity Template

### 5.1 Complete Entity Structure

```
layer_N_<type>_<name>/
│
├── 0AGNOSTIC.md                    # Source of truth (short - pointers)
├── 0INDEX.md                       # Discovery and status
│
├── CLAUDE.md                       # Generated from 0AGNOSTIC.md
├── GEMINI.md                       # Generated
├── AGENTS.md                       # Generated (for Codex)
├── .cursorrules                    # Generated (for Cursor)
│
├── .0agnostic/                     # AI CONFIG (source)
│   ├── agents/
│   ├── episodic/
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── hooks/
│   │   └── scripts/
│   │       └── agnostic-sync.sh
│   ├── skills/
│   └── sync-config.yaml
│
├── .1claude_merge/                 # Merge workspace (Claude)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── CLAUDE.override.md
│
├── .1cursor_merge/                 # Merge workspace (Cursor)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── CURSOR.override.md
│
├── .1copilot_merge/                # Merge workspace (Copilot)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── COPILOT.override.md
│
├── .1gemini_merge/                 # Merge workspace (Gemini)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── GEMINI.override.md
│
├── .1aider_merge/                  # Merge workspace (Aider)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── AIDER.override.yaml
│
├── .1codex_merge/                  # Merge workspace (Codex)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── AGENTS.override.md
│
├── .claude/                        # Generated (Claude reads this)
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   ├── skills/
│   └── settings.json
│
├── .cursor/                        # Generated (Cursor reads this)
│   └── rules/
│
├── .github/                        # Generated (Copilot reads this)
│   ├── copilot-instructions.md
│   └── instructions/
│
├── synthesis/                      # Synthesis documents
│   └── entity_synthesis.md
│
├── layer_N_group/                  # ENTITY INTERNALS (group folder)
│   ├── layer_N_00_layer_registry/
│   │   ├── registry.yaml
│   │   └── proposals/              # Registry-affecting proposals
│   │
│   ├── layer_N_01_ai_manager_system/
│   │   └── manager_config.md
│   │
│   ├── layer_N_02_manager_handoff_documents/
│   │   ├── incoming/
│   │   │   ├── from_above/
│   │   │   └── from_below/
│   │   └── outgoing/
│   │       ├── to_above/
│   │       └── to_below/
│   │
│   ├── layer_N_03_sub_layers/      # CONTENT lives here
│   │   ├── sub_layer_N_00_sub_layer_registry/
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   │   ├── overview/
│   │   │   └── things_learned/
│   │   ├── sub_layer_N_03_principles/
│   │   ├── sub_layer_N_04_rules/
│   │   └── sub_layer_N_05+_setup_dependant/           # Container for 05+
│   │       ├── sub_layer_N_05_operating_systems/      # Example
│   │       ├── sub_layer_N_06_ide_configs/            # Example
│   │       └── sub_layer_N_XX_<name>/                 # (as needed)
│   │
│   └── layer_N_99_stages/
│       ├── hand_off_documents/
│       ├── stage_N_00_registry/
│       ├── stage_N_01_request_gathering/
│       ├── stage_N_02_research/
│       ├── stage_N_03_instructions/
│       ├── stage_N_04_design/
│       ├── stage_N_05_planning/
│       ├── stage_N_06_development/
│       ├── stage_N_07_testing/
│       ├── stage_N_08_criticism/
│       ├── stage_N_09_fixing/
│       ├── stage_N_10_current_product/
│       └── stage_N_11_archives/
│
└── layer_N+1_group/                # CHILDREN (group folder)
    ├── layer_N+1_features/         # Features of this entity
    ├── layer_N+1_components/       # Components of this entity
    └── layer_N+1_sub_projects/     # Sub-projects (if project)
```

### 5.2 Stage Internal Structure (Complete)

```
stage_N_XX_name/
│
├── 0AGNOSTIC.md                    # Stage identity (short - pointers)
├── 0INDEX.md                       # Stage status
│
├── CLAUDE.md                       # Generated
├── GEMINI.md                       # Generated
├── AGENTS.md                       # Generated (for Codex)
├── .cursorrules                    # Generated (for Cursor)
│
├── .0agnostic/
│   ├── agents/                     # Stage-specific agents
│   ├── episodic/                   # Stage session memory
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── hooks/
│   │   └── scripts/
│   └── skills/                     # Stage-specific skills
│
├── .1claude_merge/
├── .1cursor_merge/
├── .1copilot_merge/
├── .1gemini_merge/
├── .1aider_merge/
├── .1codex_merge/
│
├── .claude/                        # Generated
├── .cursor/                        # Generated
├── .github/                        # Generated
│
├── ai_agent_system/                # Legacy (migrate to .0agnostic/)
│
├── hand_off_documents/
│   ├── incoming/
│   │   ├── from_above/
│   │   └── from_below/
│   └── outgoing/
│       ├── to_above/
│       └── to_below/
│
└── outputs/                        # Stage products
    ├── by_need/
    ├── by_topic/
    ├── proposals/                  # Stage-specific proposals
    └── synthesis/
```

---

## Part 6: Proposals Location Rule

### 6.1 Where Proposals Go

| Proposal Type | Location |
|---------------|----------|
| **Layer/Stage organization changes** | `layer_N_group/layer_N_00_layer_registry/proposals/` |
| **Research proposals** | `stage_N_02_research/outputs/proposals/` |
| **Instruction proposals** | `stage_N_03_instructions/outputs/proposals/` |
| **Design proposals** | `stage_N_04_design/outputs/proposals/` |
| **Planning proposals** | `stage_N_05_planning/outputs/proposals/` |
| **Development proposals** | `stage_N_06_development/outputs/proposals/` |

### 6.2 This Proposal's Correct Location

This proposal (v6) affects:
- All entities in `layer_-1_better_ai_system`
- Layer registry
- Stage registry
- Entity patterns

**Correct location**: `layer_-1_group/layer_-1_00_layer_registry/proposals/`

Suggested move:
```
FROM: layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/by_topic/
TO:   layer_-1_group/layer_-1_00_layer_registry/proposals/
```

---

## Part 7: Visual Architecture Diagrams

### 7.1 AI Agent Context Flow (Entry → Triggers → Pointers)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI AGENT CONTEXT LOADING FLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  STEP 1: ENTRY POINT                                                │   │
│   │                                                                     │   │
│   │  AI Agent enters directory → Reads first CLAUDE.md found            │   │
│   │  (or 0AGNOSTIC.md if tool-agnostic)                                │   │
│   │                                                                     │   │
│   │  ┌────────────────────────────────────────────────────────────┐    │   │
│   │  │ CLAUDE.md / 0AGNOSTIC.md                                   │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Identity                                                │    │   │
│   │  │ You are at Layer -1, Project: better_ai_system             │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Triggers ◄─── "When should I load more context?"        │    │   │
│   │  │ - User mentions: "memory", "context", "sessions"           │    │   │
│   │  │ - Working on: research, design, implementation             │    │   │
│   │  │ - Entering: layer_0_group/layer_0_features/               │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Pointers ◄─── "Where do I get that context?"            │    │   │
│   │  │ - Rules: layer_-1_group/layer_-1_03_sub_layers/...        │    │   │
│   │  │ - Agents: .0agnostic/agents/                              │    │   │
│   │  │ - Sessions: .0agnostic/episodic/                          │    │   │
│   │  └────────────────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  STEP 2: TRIGGER MATCHED → FOLLOW POINTER                          │   │
│   │                                                                     │   │
│   │  Example: User says "help me with memory system"                   │   │
│   │  Trigger matched: "memory"                                         │   │
│   │  Follow pointer: layer_0_group/layer_0_features/                   │   │
│   │                  layer_0_feature_ai_dynamic_memory_system/         │   │
│   │                                                                     │   │
│   │  ┌────────────────────────────────────────────────────────────┐    │   │
│   │  │ feature/0AGNOSTIC.md                                       │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Identity                                                │    │   │
│   │  │ You are at Layer 0, Feature: ai_dynamic_memory_system      │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Triggers                                                │    │   │
│   │  │ - User mentions: "episodic", "sessions", "persistence"     │    │   │
│   │  │                                                            │    │   │
│   │  │ ## Pointers                                                │    │   │
│   │  │ - Research: layer_0_group/layer_0_99_stages/stage_0_02_*/  │    │   │
│   │  │ - Knowledge: layer_0_group/layer_0_03_sub_layers/...      │    │   │
│   │  └────────────────────────────────────────────────────────────┘    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  STEP 3: LOAD ON-DEMAND RESOURCES                                  │   │
│   │                                                                     │   │
│   │  Pointer says: "Research at stage_0_02_research/outputs/"          │   │
│   │  Agent reads: specific files as needed                             │   │
│   │                                                                     │   │
│   │  ┌────────────────────────────────────────────────────────────┐    │   │
│   │  │ stage_0_02_research/outputs/by_topic/                      │    │   │
│   │  │                                                            │    │   │
│   │  │ - memory_system_recommendation.md                          │    │   │
│   │  │ - agnostic_memory_system_research.md                       │    │   │
│   │  │ - claude_code_memory_gap_analysis.md                       │    │   │
│   │  └────────────────────────────────────────────────────────────┘    │   │
│   │                                                                     │   │
│   │  Agent now has full context for the specific task!                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Complete Entity Structure Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    layer_N_<type>_<name>/ (ENTITY)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ROOT FILES                                        │   │
│  │                                                                      │   │
│  │   0AGNOSTIC.md     0INDEX.md                                        │   │
│  │   ┌──────────┐     ┌──────────┐                                     │   │
│  │   │ Identity │     │ Status   │                                     │   │
│  │   │ Triggers │     │ Contents │                                     │   │
│  │   │ POINTERS │     │ X-refs   │                                     │   │
│  │   └──────────┘     └──────────┘                                     │   │
│  │                                                                      │   │
│  │   CLAUDE.md   GEMINI.md   AGENTS.md   .cursorrules  (all generated) │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │               AI INFRASTRUCTURE (config, not content)                │   │
│  │                                                                      │   │
│  │   .0agnostic/                    .1*_merge/         .<tool>/        │   │
│  │   ┌────────────────┐             ┌───────────┐      ┌───────────┐   │   │
│  │   │ agents/        │ ──sync──→   │ 0_synced/ │ ──→  │ (final    │   │   │
│  │   │ episodic/      │             │ 1_overrides│      │  output)  │   │   │
│  │   │ hooks/scripts/ │             │ 2_additions│      │           │   │   │
│  │   │ skills/        │             │ *.override │      │           │   │   │
│  │   │ sync-config.yaml│            └───────────┘      └───────────┘   │   │
│  │   └────────────────┘                                                │   │
│  │                                                                      │   │
│  │   NOTE: NO knowledge/, prompts/, rules/ here!                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    layer_N_group/ (ENTITY INTERNALS)                 │   │
│  │                                                                      │   │
│  │   ┌──────────────────────────────────────────────────────────────┐  │   │
│  │   │ layer_N_03_sub_layers/  ← CONTENT LIVES HERE                 │  │   │
│  │   │                                                              │  │   │
│  │   │   sub_layer_N_00_sub_layer_registry/                         │  │   │
│  │   │   sub_layer_N_01_prompts/                                    │  │   │
│  │   │   sub_layer_N_02_knowledge_system/                           │  │   │
│  │   │   sub_layer_N_03_principles/                                 │  │   │
│  │   │   sub_layer_N_04_rules/         ← Rules go here!             │  │   │
│  │   │   sub_layer_N_05+_setup_dependant/           ← Container     │  │   │
│  │   │     └── sub_layer_N_05_operating_systems/    ← Inside 05+    │  │   │
│  │   │     └── sub_layer_N_06_ide_configs/          ← Inside 05+    │  │   │
│  │   │     └── sub_layer_N_XX_<name>/               ← (as needed)   │  │   │
│  │   └──────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │   layer_N_00_layer_registry/    ← Registry + org proposals          │   │
│  │   layer_N_01_ai_manager_system/                                     │   │
│  │   layer_N_02_manager_handoff_documents/                             │   │
│  │   layer_N_99_stages/            ← Stage outputs + stage proposals   │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    layer_N+1_group/ (CHILDREN)                       │   │
│  │                                                                      │   │
│  │   layer_N+1_features/       layer_N+1_components/                   │   │
│  │   ┌─────────────────┐       ┌─────────────────┐                     │   │
│  │   │ feature_a/      │       │ component_x/    │                     │   │
│  │   │ feature_b/      │       │ component_y/    │                     │   │
│  │   │ (each has full  │       │ (each has full  │                     │   │
│  │   │  entity struct) │       │  entity struct) │                     │   │
│  │   └─────────────────┘       └─────────────────┘                     │   │
│  │                                                                      │   │
│  │   layer_N+1_sub_projects/   (if this is a project)                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 better_ai_system After v6 (Corrected with Group Naming)

```
layer_-1_better_ai_system/
│
├── 0AGNOSTIC.md                          # Project identity (SHORT - pointers only)
├── 0INDEX.md                             # Project status
├── CLAUDE.md                             # Generated
├── GEMINI.md                             # Generated
├── AGENTS.md                             # Generated
├── .cursorrules                          # Generated
│
├── .0agnostic/                           # AI config
│   ├── agents/
│   ├── episodic/
│   ├── hooks/scripts/
│   └── skills/
│
├── .1claude_merge/
├── .1cursor_merge/
├── .1copilot_merge/
├── .1gemini_merge/
├── .1aider_merge/
├── .1codex_merge/
│
├── .claude/                              # Generated
├── .cursor/                              # Generated
├── .github/                              # Generated
│
├── synthesis/
│
├── layer_-1_group/                       # PROJECT INTERNALS (group folder)
│   │
│   ├── layer_-1_00_layer_registry/
│   │   ├── registry.yaml
│   │   └── proposals/                    # ← ORGANIZATION PROPOSALS GO HERE
│   │       ├── v1.md
│   │       ├── v2.md
│   │       ├── v3.md
│   │       ├── v4.md
│   │       ├── v5.md
│   │       └── v6.md                     # (this proposal)
│   │
│   ├── layer_-1_01_ai_manager_system/
│   │
│   ├── layer_-1_02_manager_handoff_documents/
│   │
│   ├── layer_-1_03_sub_layers/           # CONTENT
│   │   ├── sub_layer_-1_00_sub_layer_registry/
│   │   ├── sub_layer_-1_01_prompts/
│   │   ├── sub_layer_-1_02_knowledge_system/
│   │   ├── sub_layer_-1_03_principles/
│   │   ├── sub_layer_-1_04_rules/
│   │   └── sub_layer_-1_05+_setup_dependant/
│   │       ├── sub_layer_-1_05_operating_systems/
│   │       └── sub_layer_-1_XX_<name>/
│   │
│   └── layer_-1_99_stages/
│       ├── hand_off_documents/
│       ├── stage_-1_00_registry/
│       ├── stage_-1_01_request_gathering/
│       ├── stage_-1_02_research/
│       │   └── outputs/
│       │       ├── cross_cutting/        # Multi-feature research
│       │       ├── by_topic/
│       │       ├── proposals/            # Research proposals
│       │       └── synthesis/
│       ├── stage_-1_03_instructions/
│       ├── stage_-1_04_design/
│       │   └── outputs/
│       │       └── proposals/            # Design proposals
│       ├── stage_-1_05_planning/
│       └── ... (other stages)
│
└── layer_0_group/                        # CHILDREN (group folder)
    └── layer_0_features/
        │
        ├── layer_0_feature_ai_dynamic_memory_system/
        │   ├── 0AGNOSTIC.md
        │   ├── 0INDEX.md
        │   ├── CLAUDE.md                 # Generated
        │   ├── GEMINI.md                 # Generated
        │   ├── AGENTS.md                 # Generated
        │   ├── .0agnostic/
        │   │   └── episodic/
        │   ├── .1claude_merge/
        │   ├── .claude/                  # Generated
        │   │
        │   ├── layer_0_group/            # Feature internals
        │   │   ├── layer_0_03_sub_layers/
        │   │   │   ├── sub_layer_0_02_knowledge_system/
        │   │   │   │   └── things_learned/  # Existing content
        │   │   │   └── sub_layer_0_05+_setup_dependant/
        │   │   │       └── sub_layer_0_05_operating_systems/
        │   │   └── layer_0_99_stages/
        │   │       └── stage_0_02_research/
        │   │           └── outputs/
        │   │               ├── by_topic/    # MOVED: 6 memory files
        │   │               └── proposals/
        │   │
        │   └── layer_1_group/            # Feature's children (if any)
        │       ├── layer_1_components/
        │       └── layer_1_sub_features/
        │
        └── ... (7 more features, each with full entity structure)
```

---

## Part 8: Implementation Plan

### Phase 0: Cleanup
1. Delete ~50 sync conflict files
2. Remove empty directories
3. Commit cleanup

### Phase 1: Move Proposals
1. Create `layer_-1_group/layer_-1_00_layer_registry/proposals/`
2. Move v1-v6 proposals there
3. Update references

### Phase 2: Rename Group Folders
1. Rename `layer_-1_group/` → `layer_-1_group/`
2. Rename `layer_0_group/` → `layer_0_group/`
3. Update all references

### Phase 3: Create Agnostic Infrastructure (Project Root)
1. Create `.0agnostic/` with agents/, episodic/, hooks/, skills/
2. Create short `0AGNOSTIC.md` with pointers
3. Create `0INDEX.md`
4. Create merge workspaces (`.1claude_merge/`, etc.)
5. Create `agnostic-sync.sh`

### Phase 4: Ensure Full Entity Structure
1. Verify group folders have all required sub-folders (00-03, 99)
2. Add setup-dependent sub-layers (05+) as needed
3. Create any missing registry folders
4. Add `proposals/` subdirectory to each stage's outputs/

### Phase 5: Feature Enhancement
For each of 8 features:
1. Create `0AGNOSTIC.md` (short - pointers)
2. Create `0INDEX.md`
3. Create all system prompt files (CLAUDE.md, GEMINI.md, AGENTS.md, .cursorrules)
4. Create `.0agnostic/` (agents, episodic, hooks, skills)
5. Create merge workspaces
6. Verify `layer_0_group/` (internals) exists
7. Verify `layer_1_group/` (children) exists
8. Create `synthesis/`

### Phase 6: Research Distribution
1. Move memory files → `ai_dynamic_memory_system`
2. Move context files → `ai_context_system`
3. Move multi-agent files → `ai_manager_hierarchy_system`
4. Move layer-stage files → `better_layer_stage_system`
5. Move automation files → `ai_automation_system`
6. Keep cross-cutting files at project level

### Phase 7: Content Migration
1. Verify content is in sub-layers, not .0agnostic/
2. Move any misplaced content to correct sub-layer
3. Add setup-dependent content to appropriate sub_layer_N_05+ folders

### Phase 8: Sync Testing
1. Run `agnostic-sync.sh all`
2. Verify all generated files (CLAUDE.md, GEMINI.md, AGENTS.md, etc.)
3. Test context flow from entry point through triggers and pointers

### Phase 9: Registry Updates
1. Update layer_registry.yaml
2. Update stage_registry.yaml
3. Update entity patterns with new group folder naming

---

## Part 9: Metrics

| Metric | Count |
|--------|-------|
| Entities needing full structure | ~12 (project + 8 features + stages manager + ...) |
| Group folders to rename | ~20+ (layer_N → layer_N_group) |
| Proposals to move | 6 (v1-v6) |
| Sync conflicts to delete | ~50 |
| Files to move to features | ~25 |
| Sub-layer folders to verify | ~40 |
| System prompt files per entity | 4+ (CLAUDE.md, GEMINI.md, AGENTS.md, .cursorrules) |

---

## Part 10: Success Criteria

- [ ] All sync conflicts deleted
- [ ] Group folders named with `_group` suffix
- [ ] Proposals in `layer_-1_group/layer_-1_00_layer_registry/proposals/`
- [ ] Every entity has full structure (layer_N_group/ + layer_N+1_group/)
- [ ] Content in sub-layers, config in .0agnostic/
- [ ] Setup-dependent sub-layers (05+) present where needed
- [ ] 0AGNOSTIC.md files are SHORT (identity + triggers + pointers)
- [ ] All system prompt files generated (CLAUDE.md, GEMINI.md, AGENTS.md, etc.)
- [ ] agnostic-sync.sh works and generates all tool-specific files
- [ ] Research distributed to features
- [ ] Proposals/ subdirectory in each stage's outputs/
- [ ] Registries updated with new group folder naming
- [ ] Context flow works: entry → triggers → pointers → resources

---

*Created: 2026-02-03*
*Corrects: v5 missing group folder naming, sub^n conventions, merge flow, stage system prompts, proposals subdirectories, context flow diagrams, setup-dependent sub-layers*
