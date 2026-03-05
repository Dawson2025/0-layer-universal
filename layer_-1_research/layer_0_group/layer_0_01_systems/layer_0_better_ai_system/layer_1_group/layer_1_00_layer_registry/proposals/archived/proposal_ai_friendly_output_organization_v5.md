---
resource_id: "c63f70f1-6466-4c02-82cf-77c7a66b863d"
resource_type: "document"
resource_name: "proposal_ai_friendly_output_organization_v5"
---
# Proposal v5: Complete AI System Architecture (Corrected)

**Date**: 2026-02-02
**Version**: 5.0
**Status**: ⚠️ SUPERSEDED by v6
**Superseded By**: `proposal_ai_friendly_output_organization_v6.md`
**Reason**: v6 adds group folder naming, sub^n conventions, merge flow details, stage system prompts, proposals subdirectories, context flow diagrams, setup-dependent sub-layers
**Previous Versions**:
- v1-v4: Various approaches (SUPERSEDED)
**Supersedes**: v1, v2, v3, and v4

---

> **Note**: This proposal has been superseded. See v6 for corrections:
> - Group folders named with `_group` suffix (layer_N_group/, layer_N+1_group/)
> - Sub^n naming conventions for arbitrary depth nesting
> - Explicit merge flow from 0AGNOSTIC.md to tool system prompts
> - All system prompt types in stages (CLAUDE.md, GEMINI.md, AGENTS.md, etc.)
> - Proposals subdirectories in each stage's outputs/
> - Context flow diagrams showing entry → triggers → pointers
> - Setup-dependent sub-layers (05+) in hierarchy

---

## What v5 Corrects Over v4

| Issue in v4 | v5 Correction |
|-------------|---------------|
| `.0agnostic/` had knowledge/rules/prompts | Content in **sub-layers**, config in `.0agnostic/` |
| Missing full entity structure | Complete layer_N/ + layer_N+1/ groups |
| 0AGNOSTIC.md too detailed | Short: Identity + Triggers + **Pointers** |
| Proposals in wrong location | Registry-affecting proposals go in parent registry |
| Missing layer numbering in features | Features at layer_0 have `layer_0_group/` and `layer_1/` internally |

---

## Part 1: Core Architecture Principles

### 1.1 Content vs Config Separation

**CRITICAL DISTINCTION**:

| Type | Location | Examples |
|------|----------|----------|
| **Content** (knowledge, prompts, rules, principles) | `layer_N/layer_N_03_sub_layers/` | Rules, prompts, knowledge docs |
| **AI Config** (agents, hooks, skills, episodic) | `.0agnostic/` → `.claude/` | Agent configs, session memory |

**Why?**
- Content cascades through layer hierarchy naturally
- AI config is tool-specific infrastructure
- No duplication - single source of truth for each

### 1.2 The Two-Folder Structure (Layer Grouping)

Every entity has TWO sibling **GROUP folders**:

```
layer_N_<type>_<name>/              # THE ENTITY
├── layer_N/                        # GROUP: Entity's INTERNALS
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_01_ai_manager_system/
│   ├── layer_N_02_manager_handoff_documents/
│   ├── layer_N_03_sub_layers/      # ← CONTENT lives here
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   └── sub_layer_N_04_rules/
│   └── layer_N_99_stages/
│
└── layer_N+1/                      # GROUP: CHILDREN
    ├── layer_N+1_features/         # (or sub_features if feature)
    ├── layer_N+1_components/       # (or sub_components if component)
    └── layer_N+1_sub_projects/     # (only if project)
```

### 1.3 Naming Convention

| Entity Type | Name Pattern | Example |
|-------------|--------------|---------|
| Project | `layer_N_project_<name>` | `layer_1_project_my_app` |
| Feature | `layer_N_feature_<name>` | `layer_0_feature_ai_context_system` |
| Component | `layer_N_component_<name>` | `layer_1_component_auth` |
| Sub-* | `layer_N_sub_<type>_<name>` | `layer_2_subx2_feature_login` |

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
| Rules | `layer_N/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Prompts | `layer_N/layer_N_03_sub_layers/sub_layer_N_01_prompts/` |
| Knowledge | `layer_N/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Principles | `layer_N/layer_N_03_sub_layers/sub_layer_N_03_principles/` |

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
- **Children**: `layer_N+1/` contains [list or "None"]

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
| Rules | `layer_N/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge | `layer_N/layer_N_03_sub_layers/sub_layer_N_02_knowledge_system/` |
| Agents | `.0agnostic/agents/` |
| Skills | `.0agnostic/skills/` |

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Children | `layer_N+1/` |
| Stages | `layer_N/layer_N_99_stages/` |

## Where to Contribute

| Work Type | Location |
|-----------|----------|
| Research | `layer_N/layer_N_99_stages/stage_N_02_research/outputs/` |
| Instructions | `layer_N/layer_N_99_stages/stage_N_03_instructions/outputs/` |
| Session notes | `.0agnostic/episodic/sessions/` |
```

---

## Part 4: Full Entity Template

### 4.1 Complete Entity Structure

```
layer_N_<type>_<name>/
│
├── 0AGNOSTIC.md                    # Source of truth (short - pointers)
├── 0INDEX.md                       # Discovery and status
├── CLAUDE.md                       # Generated from 0AGNOSTIC.md
├── GEMINI.md                       # Generated
├── AGENTS.md                       # Generated (for Codex)
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
├── .1copilot_merge/                # Merge workspace (Copilot)
├── .1gemini_merge/                 # Merge workspace (Gemini)
├── .1aider_merge/                  # Merge workspace (Aider)
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
├── layer_N/                        # ENTITY INTERNALS
│   ├── layer_N_00_layer_registry/
│   │   └── registry.yaml
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
│   │   └── sub_layer_N_05+_setup_dependant/
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
└── layer_N+1/                      # CHILDREN
    ├── layer_N+1_features/         # Features of this entity
    ├── layer_N+1_components/       # Components of this entity
    └── layer_N+1_sub_projects/     # Sub-projects (if project)
```

### 4.2 Stage Internal Structure

```
stage_N_XX_name/
├── 0AGNOSTIC.md                    # Stage identity (short)
├── 0INDEX.md                       # Stage status
├── CLAUDE.md                       # Generated
│
├── .0agnostic/
│   ├── agents/                     # Stage-specific agents
│   ├── episodic/                   # Stage session memory
│   └── skills/                     # Stage-specific skills
│
├── .claude/                        # Generated
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
    └── synthesis/
```

---

## Part 5: Proposals Location Rule

### 5.1 Where Proposals Go

| Proposal Type | Location |
|---------------|----------|
| **Layer/Stage organization changes** | Parent registry that encompasses all affected entities |
| **Research proposals** | `stage_N_02_research/outputs/` |
| **Instruction proposals** | `stage_N_03_instructions/outputs/` |
| **Design proposals** | `stage_N_04_design/outputs/` |
| **Planning proposals** | `stage_N_05_planning/outputs/` |

### 5.2 This Proposal's Correct Location

This proposal (v5) affects:
- All entities in `layer_-1_better_ai_system`
- Layer registry
- Stage registry
- Entity patterns

**Correct location**: Should be in the **layer_-1 registry** or **project-level registry**, NOT in stage outputs.

Suggested move:
```
FROM: layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/by_topic/
TO:   layer_-1_group/layer_-1_00_layer_registry/proposals/
```

---

## Part 6: Visual Architecture Diagrams

### 6.1 Complete Entity Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    layer_N_<type>_<name>/ (ENTITY)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ROOT FILES & FOLDERS                              │   │
│  │                                                                      │   │
│  │   0AGNOSTIC.md     0INDEX.md      synthesis/                        │   │
│  │   ┌──────────┐     ┌──────────┐   ┌──────────┐                      │   │
│  │   │ Identity │     │ Status   │   │ Overview │                      │   │
│  │   │ Triggers │     │ Contents │   │ Findings │                      │   │
│  │   │ POINTERS │     │ X-refs   │   │          │                      │   │
│  │   └──────────┘     └──────────┘   └──────────┘                      │   │
│  │                                                                      │   │
│  │   CLAUDE.md        GEMINI.md      AGENTS.md     (all generated)     │   │
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
│  │   │ skills/        │             └───────────┘      └───────────┘   │   │
│  │   │ sync-config.yaml│                                               │   │
│  │   └────────────────┘                                                │   │
│  │                                                                      │   │
│  │   NOTE: NO knowledge/, prompts/, rules/ here!                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    layer_N/ (ENTITY INTERNALS)                       │   │
│  │                                                                      │   │
│  │   ┌──────────────────────────────────────────────────────────────┐  │   │
│  │   │ layer_N_03_sub_layers/  ← CONTENT LIVES HERE                 │  │   │
│  │   │                                                              │  │   │
│  │   │   sub_layer_N_01_prompts/                                    │  │   │
│  │   │   sub_layer_N_02_knowledge_system/                           │  │   │
│  │   │   sub_layer_N_03_principles/                                 │  │   │
│  │   │   sub_layer_N_04_rules/         ← Rules go here!             │  │   │
│  │   │   sub_layer_N_05+_setup_dependant/                           │  │   │
│  │   └──────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │   layer_N_00_layer_registry/    ← Registry-affecting proposals      │   │
│  │   layer_N_01_ai_manager_system/                                     │   │
│  │   layer_N_02_manager_handoff_documents/                             │   │
│  │   layer_N_99_stages/            ← Stage outputs                     │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    layer_N+1/ (CHILDREN)                             │   │
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

### 6.2 Content vs Config Flow

```
                         CONTENT                              CONFIG
                    (cascades through                     (tool-specific
                     layer hierarchy)                      infrastructure)
                           │                                    │
                           ▼                                    ▼
┌─────────────────────────────────────┐    ┌─────────────────────────────────┐
│      layer_N/layer_N_03_sub_layers/ │    │          .0agnostic/            │
│                                     │    │                                 │
│  sub_layer_N_01_prompts/            │    │  agents/                        │
│  sub_layer_N_02_knowledge_system/   │    │  episodic/                      │
│  sub_layer_N_03_principles/         │    │  hooks/scripts/                 │
│  sub_layer_N_04_rules/              │    │  skills/                        │
│                                     │    │  sync-config.yaml               │
│  (inherited by child layers)        │    │                                 │
└─────────────────────────────────────┘    └────────────────┬────────────────┘
                                                            │
                                               agnostic-sync.sh
                                                            │
                              ┌──────────────────┬──────────┴──────────┬─────────────────┐
                              ▼                  ▼                     ▼                 ▼
                        .1claude_merge/    .1cursor_merge/      .1copilot_merge/   .1gemini_merge/
                              │                  │                     │                 │
                              ▼                  ▼                     ▼                 ▼
                        ┌──────────┐       ┌──────────┐         ┌──────────┐      ┌──────────┐
                        │ .claude/ │       │ .cursor/ │         │ .github/ │      │GEMINI.md │
                        │CLAUDE.md │       │.cursorrules│       │copilot-*.md│    │          │
                        └──────────┘       └──────────┘         └──────────┘      └──────────┘
```

### 6.3 better_ai_system After v5 (Corrected)

```
layer_-1_better_ai_system/
│
├── 0AGNOSTIC.md                          # Project identity (SHORT - pointers only)
├── 0INDEX.md                             # Project status
├── CLAUDE.md                             # Generated
├── .0agnostic/                           # AI config
│   ├── agents/
│   ├── episodic/
│   ├── hooks/scripts/
│   └── skills/
├── .1claude_merge/
├── .claude/                              # Generated
├── synthesis/
│
├── layer_-1_group/                             # PROJECT INTERNALS
│   │
│   ├── layer_-1_00_layer_registry/
│   │   ├── registry.yaml
│   │   └── proposals/                    # ← ORGANIZATION PROPOSALS GO HERE
│   │       ├── v1.md
│   │       ├── v2.md
│   │       ├── v3.md
│   │       ├── v4.md
│   │       └── v5.md                     # (this proposal)
│   │
│   ├── layer_-1_03_sub_layers/           # CONTENT
│   │   ├── sub_layer_-1_01_prompts/
│   │   ├── sub_layer_-1_02_knowledge_system/
│   │   ├── sub_layer_-1_03_principles/
│   │   └── sub_layer_-1_04_rules/
│   │
│   └── layer_-1_99_stages/
│       ├── stage_-1_02_research/
│       │   └── outputs/
│       │       ├── cross_cutting/        # Multi-feature research
│       │       │   └── (6 files)
│       │       └── synthesis/
│       │           └── research_synthesis.md
│       └── ... (other stages)
│
└── layer_0_group/                              # CHILDREN (features)
    └── layer_0_features/
        │
        ├── layer_0_feature_ai_dynamic_memory_system/
        │   ├── 0AGNOSTIC.md
        │   ├── 0INDEX.md
        │   ├── .0agnostic/
        │   │   └── episodic/
        │   ├── layer_0_group/                  # Feature internals
        │   │   ├── layer_0_03_sub_layers/
        │   │   │   └── sub_layer_0_02_knowledge_system/
        │   │   │       └── things_learned/  # Existing content
        │   │   └── layer_0_99_stages/
        │   │       └── stage_0_02_research/
        │   │           └── outputs/
        │   │               └── by_topic/    # MOVED: 6 memory files
        │   └── layer_1/                  # Feature's children (if any)
        │       ├── layer_1_components/
        │       └── layer_1_sub_features/
        │
        ├── layer_0_feature_ai_context_system/
        │   ├── 0AGNOSTIC.md
        │   ├── layer_0_group/
        │   │   └── layer_0_99_stages/
        │   │       └── stage_0_02_research/
        │   │           └── outputs/
        │   │               └── by_topic/    # MOVED: 7 context files
        │   └── layer_1/
        │
        └── ... (6 more features, each with full entity structure)
```

---

## Part 7: Implementation Plan

### Phase 0: Cleanup
1. Delete ~50 sync conflict files
2. Remove empty directories
3. Commit cleanup

### Phase 1: Move Proposals
1. Create `layer_-1_group/layer_-1_00_layer_registry/proposals/`
2. Move v1-v5 proposals there
3. Update references

### Phase 2: Create Agnostic Infrastructure (Project Root)
1. Create `.0agnostic/` with agents/, episodic/, hooks/, skills/
2. Create short `0AGNOSTIC.md` with pointers
3. Create `0INDEX.md`
4. Create `agnostic-sync.sh`

### Phase 3: Ensure Full Entity Structure
1. Verify `layer_-1_group/` has all required folders (00-03, 99)
2. Verify `layer_0_group/` has `layer_0_features/`
3. Create any missing registry folders

### Phase 4: Feature Enhancement
For each of 8 features:
1. Create `0AGNOSTIC.md` (short - pointers)
2. Create `0INDEX.md`
3. Create `.0agnostic/` (agents, episodic, hooks, skills)
4. Verify `layer_0_group/` (internals) exists
5. Verify `layer_1/` (children) exists
6. Create `synthesis/`

### Phase 5: Research Distribution
1. Move memory files → `ai_dynamic_memory_system`
2. Move context files → `ai_context_system`
3. Move multi-agent files → `ai_manager_hierarchy_system`
4. Move layer-stage files → `better_layer_stage_system`
5. Move automation files → `ai_automation_system`
6. Keep cross-cutting files at project level

### Phase 6: Content Migration
1. Verify content is in sub-layers, not .0agnostic/
2. Move any misplaced content to correct sub-layer

### Phase 7: Sync Testing
1. Run `agnostic-sync.sh all`
2. Verify generated files

### Phase 8: Registry Updates
1. Update layer_registry.yaml
2. Update stage_registry.yaml
3. Update entity patterns

---

## Part 8: Metrics

| Metric | Count |
|--------|-------|
| Entities needing full structure | ~12 (project + 8 features + stages manager + ...) |
| Proposals to move | 5 (v1-v5) |
| Sync conflicts to delete | ~50 |
| Files to move to features | ~25 |
| Sub-layer folders to verify | ~40 |

---

## Part 9: Success Criteria

- [ ] All sync conflicts deleted
- [ ] Proposals in `layer_-1_00_layer_registry/proposals/`
- [ ] Every entity has full structure (layer_N/ + layer_N+1/)
- [ ] Content in sub-layers, config in .0agnostic/
- [ ] 0AGNOSTIC.md files are SHORT (identity + triggers + pointers)
- [ ] agnostic-sync.sh works
- [ ] Research distributed to features
- [ ] Registries updated

---

*Created: 2026-02-02*
*Corrects: v4 missing full entity structure, content/config separation*
