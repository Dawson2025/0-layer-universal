# Layer-Stage Instantiation Understanding

**Date**: 2026-01-31
**Time**: 01:15 UTC (updated 02:45 UTC)
**Topic**: How layers and stages are instantiated in the framework
**Sources**: SYSTEM_OVERVIEW.md, layer_registry.yaml, stage_registry.yaml, USAGE_GUIDE.md, entity-creation skill, FLEXIBLE_LAYERING_SYSTEM.md

---

## Core Concept: Layers of Specificity

**The layer system is fundamentally about SPECIFICITY and ABSTRACTION.**

- **Lower layer numbers = more universal/abstract** (applies broadly)
- **Higher layer numbers = more specific** (applies narrowly)
- **Rules and context CASCADE from universal → specific**

| Layer | Name | Scope of Rules/Context |
|-------|------|------------------------|
| -1 | Research | Exploratory (outside main hierarchy) |
| 0 | Universal | **GLOBAL** - applies to ALL projects everywhere |
| 1 | Project | Applies to ONE specific project |
| 2 | Feature | Applies to ONE specific feature of that project |
| 3 | Component | Applies to ONE specific component of that feature |
| 4+ | Sub-* | Applies to increasingly specific nested entities |

**Key Principle**: Rules at Layer 0 apply EVERYWHERE. Rules at Layer 1 apply only to that project. Rules at Layer 2 apply only to that feature. And so on.

---

## Cascading Context

When an agent works at any level:
1. It inherits ALL rules/context from Layer 0 (universal)
2. Plus rules/context from Layer 1 (if in a project)
3. Plus rules/context from Layer 2 (if in a feature)
4. Plus rules/context from Layer 3 (if in a component)
5. ...and so on down the hierarchy

**This is why lower layers are "prerequisites"** - you must understand universal rules before project rules, project rules before feature rules, etc.

---

## Nesting: Same-Type vs Different-Type

### CRITICAL NAMING RULE

The **"sub" prefix ONLY applies when nesting the SAME type**:

| Nesting Pattern | Result | Why |
|-----------------|--------|-----|
| Project inside Project | **sub_project** | Same type → uses "sub" |
| Feature inside Feature | **sub_feature** | Same type → uses "sub" |
| Component inside Component | **sub_component** | Same type → uses "sub" |
| Feature inside Project | **feature** (NOT sub_feature) | Different type → no "sub" |
| Component inside Project | **component** (NOT sub_component) | Different type → no "sub" |
| Component inside Feature | **component** (NOT sub_component) | Different type → no "sub" |

### Same-Type Nesting Depth Markers

When nesting the same type multiple levels deep:
- 1 level deep: `sub_project`, `sub_feature`, `sub_component`
- 2 levels deep: `subx2_project`, `subx2_feature`, `subx2_component`
- 3 levels deep: `subx3_project`, `subx3_feature`, `subx3_component`
- N levels deep: `subxN_*`

### What Each Entity Contains

| Entity Type | Contains (in layer_N+1/) |
|-------------|--------------------------|
| Project / Sub*_project | `sub*_projects/`, `features/`, `components/` |
| Feature | `sub_features/`, `components/` |
| Component | `sub_components/` |

**Key Rules**:
- **Projects** contain `features/` and `components/` (no sub prefix) plus `sub_projects/` for same-type nesting
- **Features** contain `sub_features/` (same-type) and `components/` (different type → no sub prefix)
- **Components** only contain `sub_components/` (same-type nesting)
- **Layer N+1 can have multiple types**: At any `layer_N+1/`, you may find `sub_projects/`, `features/`, AND `components/` as siblings

### Stages Within Sub-Layers

Stages can exist WITHIN sub-layers for specialized workflows. Example location:
```
layer_0/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/
└── sub_layer_0_05_os/
    └── sub_layer_0_05_01_linux_ubuntu/
        └── layer_0_99_stages/    # Stages specific to Linux Ubuntu setup
```

This allows stage-based workflows (01-11) to be applied to specific setup contexts when needed.

---

## Layer Hierarchy (Detailed)

---

## The Two-Folder Structure (Layer Grouping)

Every entity has TWO sibling folders at its root:

```
layer_N_<type>_<name>/
├── layer_N/                    # This entity's INTERNALS
│   ├── layer_N_00_ai_manager_system/
│   ├── layer_N_01_manager_handoff_documents/
│   ├── layer_N_02_sub_layers/
│   └── layer_N_99_stages/
└── layer_N+1/                  # NESTED CONTENT (children)
    ├── layer_N+1_sub*_projects/   # Sub-projects (if applicable)
    ├── layer_N+1_features/        # Features (or sub_features)
    └── layer_N+1_components/      # Components (or sub_components)
```

**Key Points**:
- `layer_N/` = the entity's OWN internals (manager, handoffs, stages)
- `layer_N+1/` = the entity's CHILDREN (nested entities)
- These are SIBLINGS at the entity root, not nested within each other

---

## Layer Internal Structure

Each layer has standard components at specific positions (from `layer_registry.yaml`):

| Position | Slug | Purpose | Folder Pattern |
|----------|------|---------|----------------|
| 00 | layer_registry | Metadata for this layer | `layer_N_00_layer_registry` |
| 01 | ai_manager_system | **How the AI system works** - agent hierarchy, delegation patterns, manager/worker relationships | `layer_N_01_ai_manager_system` |
| 02 | manager_handoff_documents | Session transition state, communication between layers | `layer_N_02_manager_handoff_documents` |
| 03 | sub_layers | Knowledge, prompts, principles, rules, setup | `layer_N_03_sub_layers` |
| 99 | stages | Workflow stages (01-11) | `layer_N_99_stages` |

**Position 99** keeps stages at the end for visibility/sorting.

---

## Sub-Layer Slots (within position 03)

Sub-layers organize different types of content:

| Slot | Content |
|------|---------|
| 00 | sub_layer_registry |
| 01 | prompts |
| 02 | knowledge_system |
| 03 | principles |
| 04 | rules |
| 05+ | setup_dependant (progressively specific) |

**Setup slots** (05+) go from general to specific:
- 05: OS setup
- 06: coding app setup
- 07: environment
- 08: AI apps/tools
- 09: MCP servers and tools
- 10: AI models
- 11: universal tools
- 12: agent setup

---

## Stage System

**CORRECTED ORDER** (design before planning):

| Position | Stage | Purpose |
|----------|-------|---------|
| 00 | stage_registry | Metadata only (not a workflow stage) |
| 01 | request_gathering | Gather requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints |
| 04 | **design** | Architecture decisions |
| 05 | **planning** | Break into subtasks |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical records |

**Note**: Design (04) comes BEFORE planning (05). You design the solution first, then plan how to implement it.

### Stage Internal Structure

Each stage contains:
```
stage_N_XX_name/
├── ai_agent_system/     # Stage-specific agent guidance
├── hand_off_documents/  # Incoming/outgoing handoffs
└── outputs/             # Stage artifacts
```

---

## Entity Instantiation Patterns

### Research Project (Layer -1)

```
layer_-1_research/
└── layer_-1_<project_name>/
    ├── CLAUDE.md
    ├── layer_-1/
    │   ├── layer_-1_02_manager_handoff_documents/
    │   └── layer_-1_99_stages/
    │       ├── stage_-1_00_stage_registry/
    │       ├── stage_-1_01_request_gathering/
    │       ├── stage_-1_02_research/
    │       │   └── outputs/01_understanding_in_progress/by_topic/
    │       ├── stage_-1_03_instructions/
    │       ├── stage_-1_04_design/
    │       ├── stage_-1_05_planning/
    │       ├── stage_-1_06_development/
    │       ├── stage_-1_07_testing/
    │       ├── stage_-1_08_criticism/
    │       ├── stage_-1_09_fixing/
    │       ├── stage_-1_10_current_product/
    │       └── stage_-1_11_archives/
    └── layer_0/
        └── layer_0_features/   # Features within the research project
```

### Project (Layer 1)

```
layer_1/layer_1_projects/
└── layer_1_project_<name>/
    ├── CLAUDE.md
    ├── layer_1_00_layer_registry/
    ├── layer_1_01_ai_manager_system/
    ├── layer_1_02_manager_handoff_documents/
    │   ├── layer_1_00_to_universal/
    │   └── layer_1_01_to_specific/
    ├── layer_1_03_sub_layers/
    │   ├── sub_layer_1_01_prompts/
    │   ├── sub_layer_1_02_knowledge_system/
    │   └── ...
    └── layer_1_99_stages/
        ├── stage_1_01_request_gathering/
        ├── stage_1_02_research/
        └── ...
```

### Feature (Layer 2, nested under project)

```
layer_1_project_<name>/
└── layer_2/
    └── layer_2_features/
        └── layer_2_feature_<name>/
            ├── CLAUDE.md
            ├── layer_1/   # Feature's internal workings
            └── layer_2/   # Child features/components
```

### Component (Layer 3)

```
layer_2_feature_<name>/
└── layer_3/
    └── layer_3_components/
        └── layer_3_component_<name>/
```

---

## Entity Creation Process

From the `entity-creation` skill:

1. **Determine entity type and parent** (project/feature/component)
2. **Calculate next available number** (XX)
3. **Create directory structure**
4. **Initialize CLAUDE.md** with context
5. **Create initial status file** (status_N.json)
6. **Update parent's children list**

### Required Structure for New Entity

Every new entity MUST have the two-folder structure with ALL possible child types:

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md              # Tool-agnostic foundational context (source of truth)
├── CLAUDE.md                 # Generated from 0AGNOSTIC.md (Claude-specific)
├── .0agnostic/               # Resources for agnostic system
│   ├── rules/
│   ├── prompts/
│   ├── knowledge/
│   └── scripts/
├── .claude/                  # Claude-specific settings
├── status_N.json             # Current state tracking
├── layer_N/                  # Entity's OWN internals
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_01_ai_manager_system/
│   ├── layer_N_02_manager_handoff_documents/
│   ├── layer_N_03_sub_layers/
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   └── sub_layer_N_04_rules/
│   └── layer_N_99_stages/
│       ├── stage_N_00_stage_registry/
│       ├── stage_N_01_request_gathering/
│       └── ... (all 11 stages)
└── layer_N+1/                # Entity's CHILDREN (ALL types, even if empty)
    ├── layer_N+1_sub*_<types>/   # Same-type nesting
    ├── layer_N+1_features/       # Features
    └── layer_N+1_components/     # Components
```

**Key Points**:
- Always include `0AGNOSTIC.md` as the source of truth
- Tool-specific files (`CLAUDE.md`, `AGENTS.md`, etc.) are generated from `0AGNOSTIC.md`
- Include `.0agnostic/` and `.claude/` folders for tool support
- Always create ALL child type folders in `layer_N+1/` even if empty

---

## Handoff System

Entities communicate via handoff documents in **four directions**:

### Handoff Directions

| Direction | Purpose | Folder |
|-----------|---------|--------|
| **UP** | Escalate to parent, return results | `hand_off_documents/outgoing/to_above/` |
| **DOWN** | Delegate to children | `hand_off_documents/outgoing/to_below/` |
| **SIDEWAYS** | Coordinate with siblings | `hand_off_documents/outgoing/to_siblings/` |
| **INCOMING** | Receive from any direction | `hand_off_documents/incoming/from_above/`, `from_below/`, `from_siblings/` |

### Handoff Document Structure

```json
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-auth-impl",
  "layer": 2,
  "stage": "development",
  "from": "layer_2/auth/design",
  "to": "layer_2/auth/development",
  "direction": "sideways",
  "task": "Implement login component",
  "constraints": ["TypeScript", "React"],
  "artifacts": {"files": ["src/components/LoginForm.tsx"]},
  "status": "pending"
}
```

### Handoff Workflow
1. **Read incoming** from `hand_off_documents/incoming/`
2. **Process** the task
3. **Write outgoing** to appropriate direction folder
4. **Track status** in status.json

---

## AGNOSTIC System (Subcomponent of Layer-Stage)

The AGNOSTIC system is a **subcomponent** of the layer-stage system, providing tool portability and session management at each layer:

### Structure at Each Entity

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md          # SOURCE OF TRUTH - Tool-agnostic context
├── CLAUDE.md             # Generated from 0AGNOSTIC.md (Claude Code)
├── AGENTS.md             # Generated from 0AGNOSTIC.md (Cursor Agents)
├── GEMINI.md             # Generated from 0AGNOSTIC.md (Gemini)
├── OPENAI.md             # Generated from 0AGNOSTIC.md (OpenAI)
├── .0agnostic/           # Shared resources for all tools
│   ├── rules/
│   ├── prompts/
│   ├── knowledge/
│   ├── scripts/
│   └── skills/
├── .claude/              # Claude-specific settings
├── outputs/episodic/     # Session memory (episodic memory system)
│   ├── index.md
│   ├── sessions/
│   ├── changes/
│   └── divergence.log
└── .locks/               # Multi-agent file locking
```

### Key Functions

| Function | Component | Purpose |
|----------|-----------|---------|
| Tool Portability | `0AGNOSTIC.md` → tool-specific files | Same context works across Claude, Cursor, Gemini, etc. |
| Episodic Memory | `outputs/episodic/` | Solves agent amnesia across sessions |
| Multi-Agent Sync | `.locks/` | Prevents conflicts when multiple agents work in parallel |
| Session Continuity | `divergence.log` | Tracks changes made during sessions |

### Integration with Layer-Stage

- **0AGNOSTIC.md** defines Identity, Navigation, Behaviors for each entity
- Generated files (CLAUDE.md, etc.) inherit the layer-stage context automatically
- Episodic memory folders exist at each layer level
- The agnostic-sync.sh script regenerates tool-specific files from 0AGNOSTIC.md

---

## Key Observations

### Inconsistencies in Existing Structure

1. **Stage numbering varies**: Some older projects use stages 00-09, newer ones use 01-11
2. **Component positions vary**: Some use 01/02, others use 00/01/02/03/99
3. **Design/Planning order**: Stage registry says planning=04, design=05, but the decision is design=04, planning=05

### System Integration

The AGNOSTIC system is a **subcomponent** of the layer-stage system:
- Layer-stage provides the organizational hierarchy and workflow structure
- AGNOSTIC provides tool portability and session continuity within that structure
- Both work together - entities have layer-stage structure AND agnostic files

### Nesting Capability

Features can contain their own layer structure:
- `layer_-1_better_ai_system/layer_0/layer_0_features/layer_0_feature_*/` shows features with internal layers

---

## Status Tracking

Each layer tracks status in `layer_N_99_stages/status.json`:

```json
{
  "current_stage": "development",
  "stages": {
    "request_gathering": "done",
    "research": "done",
    "instructions": "done",
    "design": "done",
    "planning": "done",
    "development": "in_progress",
    "testing": "not_started"
  }
}
```

---

## Summary

**Layer instantiation**:
1. Create directory with pattern `layer_N_entity_name/`
2. Add components at positions 00, 01, 02, 03, 99
3. Initialize CLAUDE.md and status.json
4. Create sub-layers as needed in position 03
5. Create stages in position 99

**Stage instantiation**:
1. Create directories 01-11 in `layer_N_99_stages/`
2. Each stage gets: ai_agent_system/, hand_off_documents/, outputs/
3. Position 00 reserved for stage_registry (metadata only)
4. **Design (04) before Planning (05)**

**Workflow**:
- Enter via handoff documents
- Work within current stage
- Output to outputs/ and outgoing handoff
- Track status in status.json

---

## Key Source Documents

| Document | Location | What It Explains |
|----------|----------|------------------|
| **FLEXIBLE_LAYERING_SYSTEM.md** | `layer_1/.../sub_layer_1_05_framework_docs/` | Authoritative guide on nesting, naming, specificity |
| **SYSTEM_OVERVIEW.md** | `0_layer_universal/` | Big picture of layer + stage system |
| **layer_registry.yaml** | `layer_0/layer_0_00_layer_registry/` | Layer internal structure definition |
| **stage_registry.yaml** | `layer_0/layer_0_99_stages/layer_0_00_stage_registry/` | Stage workflow definition |

---

## Summary

1. **Layers = Specificity**: Universal (0) → Project (1) → Feature (2) → Component (3) → deeper
2. **Rules CASCADE**: Lower layer rules apply to all higher layers
3. **Same-type nesting uses "sub"**: project→sub_project, feature→sub_feature, component→sub_component
4. **Different-type nesting does NOT use "sub"**: project→feature, project→component, feature→component (no sub prefix)
5. **Two-folder structure**: `layer_N/` (internals) + `layer_N+1/` (children with ALL types even if empty)
6. **Design before Planning**: Stage 04 = design, Stage 05 = planning
7. **AGNOSTIC is a subcomponent**: Tool portability + episodic memory integrated into layer-stage structure
8. **Handoffs go 4 directions**: UP (to parent), DOWN (to children), SIDEWAYS (to siblings), INCOMING (receive)
9. **Stages can exist in sub-layers**: For specialized workflows like OS-specific setup
10. **Entity structure requires**: 0AGNOSTIC.md (source), tool-specific files, .0agnostic/, .claude/, layer_N/, layer_N+1/
