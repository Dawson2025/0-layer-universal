# System Prompt Architecture Research

**Status**: APPROVED - Ready for instructions stage
**Date**: 2026-01-26
**Approved**: 2026-01-26
**Related Needs**: rule_compliant, persistent_knowledge, discoverable
**Next Step**: Create implementation instructions in `stage_-1_03_instructions/outputs/01_instructions_in_progress/`

---

## Core Principle

**System Prompt Files (CLAUDE.md, AGNOSTIC.md)** = Content that goes into EVERY API call at that scope

**Referenced Files** = Content that AI reads via tool calls when needed (NOT in every API call)

---

## What Goes INTO System Prompt Files

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         IN SYSTEM PROMPT                                │
│                    (Every API call at this scope)                       │
├─────────────────────────────────────────────────────────────────────────┤
│ • Rules that MUST be followed for every request                         │
│ • Constraints that always apply                                         │
│ • Identity/role of the agent at this level                              │
│ • Navigation instructions (how to find other things)                    │
│ • Brief context (what is this layer/stage/feature)                      │
└─────────────────────────────────────────────────────────────────────────┘
```

## What Gets REFERENCED (Not in System Prompt)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         REFERENCED FILES                                │
│                 (AI reads when situation arises)                        │
├─────────────────────────────────────────────────────────────────────────┤
│ • Detailed documentation                                                │
│ • Knowledge that's needed sometimes, not always                         │
│ • Historical context / archives                                         │
│ • Detailed explanations of rules (canonical source)                     │
│ • Setup instructions (only needed during setup)                         │
│ • Research outputs (consulted when relevant)                            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## The Hierarchy: What Goes Where

```
0_layer_universal/CLAUDE.md
│
│  IN THIS FILE (every API call everywhere):
│  ├── Universal rules (modification protocol, commit/push, safety)
│  ├── Navigation to sub-layers and stages
│  └── Core conventions (naming, structure)
│
│  REFERENCED (not every call):
│  └── layer_0/layer_0_03_sub_layers/
│      ├── sub_layer_0_01_prompts/      → Detailed init prompts
│      ├── sub_layer_0_02_knowledge/    → Domain knowledge
│      ├── sub_layer_0_03_principles/   → Guiding principles
│      ├── sub_layer_0_04_rules/        → Canonical rule docs, detailed rules
│      └── sub_layer_0_05+_setup/       → OS/tool configuration
│
└── layer_1/layer_1_projects/layer_1_project_X/CLAUDE.md
    │
    │  IN THIS FILE (every API call in this project):
    │  ├── Project-specific rules
    │  ├── Project identity/purpose
    │  └── Navigation within project
    │
    │  REFERENCED:
    │  └── Project knowledge, docs, etc.
    │
    └── layer_2/layer_2_features/layer_2_feature_Y/CLAUDE.md
        │
        │  IN THIS FILE (every API call in this feature):
        │  ├── Feature-specific rules
        │  ├── Feature identity/purpose
        │  └── Navigation within feature
        │
        └── layer_2_99_stages/stage_02_research/CLAUDE.md
            │
            │  IN THIS FILE (every API call in this stage):
            │  ├── Stage-specific rules
            │  ├── Stage purpose and constraints
            │  └── What outputs go where
            │
            │  REFERENCED:
            │  └── outputs/, hand_off_documents/, etc.
```

---

## How Claude Code Builds the API Call

```
User is working in: stage_02_research/

Claude Code walks UP the tree, collecting CLAUDE.md files:

API Request System Prompt =
┌─────────────────────────────────────────┐
│ 0_layer_universal/CLAUDE.md             │  ← Universal rules
├─────────────────────────────────────────┤
│ layer_1_project_X/CLAUDE.md             │  ← + Project rules
├─────────────────────────────────────────┤
│ layer_2_feature_Y/CLAUDE.md             │  ← + Feature rules
├─────────────────────────────────────────┤
│ stage_02_research/CLAUDE.md             │  ← + Stage rules
└─────────────────────────────────────────┘

All of this goes into EVERY API call when working in that stage.
```

---

## Full Layer Entity Structure

A complete layer entity contains MORE than just sub-layers and stages:

```
layer_N_entity_name/
├── CLAUDE.md                          ← SYSTEM PROMPT for this scope
├── .claude/                           ← Claude Code configuration (see below)
│
└── layer_N/
    ├── layer_N_00_layer_registry/     ← Metadata about this layer's structure
    │
    ├── layer_N_01_ai_manager_system/  ← Manager/worker agent configurations
    │   ├── agnostic/                  ← Tool-agnostic configs
    │   └── specific/                  ← Tool-specific configs
    │
    ├── layer_N_02_manager_handoff_documents/  ← Inter-layer communication
    │   ├── layer_N_00_to_universal/   ← Handoffs to/from parent layer
    │   └── layer_N_01_to_specific/    ← Handoffs to/from child layers
    │
    ├── layer_N_03_sub_layers/         ← Content TYPES (referenced)
    │   ├── sub_layer_N_00_sub_layer_registry/
    │   ├── sub_layer_N_01_prompts/
    │   ├── sub_layer_N_02_knowledge_system/
    │   ├── sub_layer_N_03_principles/
    │   ├── sub_layer_N_04_rules/
    │   └── sub_layer_N_05+_setup_dependant/
    │
    └── layer_N_99_stages/             ← Workflow PHASES
        ├── stage_N_00_stage_registry/
        ├── stage_N_01_request_gathering/
        ├── stage_N_02_research/
        │   ├── CLAUDE.md              ← Stage-specific rules
        │   ├── .claude/               ← Stage-specific Claude Code config
        │   ├── outputs/
        │   └── hand_off_documents/
        └── ...
```

---

## Entity Components Overview

| Component | Position | Purpose | Has CLAUDE.md? |
|-----------|----------|---------|----------------|
| **Layer Registry** | 00 | Metadata about layer structure | No - referenced |
| **AI Manager System** | 01 | Manager/worker agent configs | No - referenced |
| **Manager Handoff Docs** | 02 | Inter-layer communication | No - referenced |
| **Sub-layers** | 03 | Content types (knowledge, rules, etc.) | No - referenced |
| **Stages** | 99 | Workflow phases | Yes - stage rules |

---

## .claude/ Folder Configuration

Claude Code uses `.claude/` folders for tool-specific configuration at any scope:

```
.claude/
├── settings.json         ← Permissions, context metadata
│   {
│     "context": { "stage": "...", "layer": N, "purpose": "..." },
│     "permissions": { "allow": [], "deny": [], "ask": [] },
│     "env": {},
│     "hooks": {}
│   }
│
├── agents/               ← Agent configurations
│   └── stage-agent.md
│
├── commands/             ← Slash commands
│   ├── command-status.md
│   └── command-complete.md
│
├── hooks/                ← Event-triggered actions
│   ├── hooks.json        ← PreToolUse, PostToolUse, SessionStart, etc.
│   └── scripts/
│       └── on-stage-enter.sh
│
├── scripts/              ← Utility scripts
│   └── README.md
│
└── skills/               ← Workflow definitions (SKILL.md pattern)
    └── workflow-skill/
        ├── SKILL.md
        └── references/
```

### .claude/ vs CLAUDE.md

| Aspect | CLAUDE.md | .claude/ |
|--------|-----------|----------|
| **Purpose** | System prompt content (rules, navigation) | Claude Code configuration |
| **In API calls?** | Yes - cascades up the tree | No - tool-level config |
| **Controls** | AI behavior, rules, constraints | Permissions, hooks, commands |
| **Format** | Markdown | JSON + Markdown |

**Key insight**: `.claude/` configures **how Claude Code operates** (permissions, hooks, commands), while `CLAUDE.md` defines **what Claude knows/follows** (rules, context, navigation).

---

## What Goes Where: Complete Picture

| Content Type | Location | In System Prompt? |
|--------------|----------|-------------------|
| **Universal rules** | `layer_0/sub_layer_0_04_rules/` (canonical) + embedded in `CLAUDE.md` | YES |
| **Scope rules** | Scope's `CLAUDE.md` | YES |
| **Navigation** | `CLAUDE.md` | YES |
| **Detailed knowledge** | `sub_layer_0_02_knowledge_system/` | Referenced |
| **Init prompts** | `sub_layer_0_01_prompts/` | Referenced |
| **Principles** | `sub_layer_0_03_principles/` | Referenced |
| **Setup instructions** | `sub_layer_0_05+_setup_dependant/` | Referenced |
| **Agent configs** | `layer_N_01_ai_manager_system/` | Referenced |
| **Handoff docs** | `layer_N_02_manager_handoff_documents/` | Referenced |
| **Stage outputs** | `stage_N_XX/outputs/` | Referenced |
| **Permissions** | `.claude/settings.json` | Tool config |
| **Hooks** | `.claude/hooks/` | Tool config |
| **Commands** | `.claude/commands/` | Tool config |
| **Skills** | `.claude/skills/` | Tool config |

---

## Sub-Layers vs Stages vs Layers (Updated)

| Concept | Purpose | Has CLAUDE.md? | Has .claude/? |
|---------|---------|----------------|---------------|
| **Sub-layers** | Content TYPES (prompts, knowledge, rules, principles, setup) | No - referenced | No |
| **Stages** | Workflow PHASES (research, design, development, etc.) | Yes - stage rules | Yes - stage config |
| **Layers** | Scope LEVELS (universal → project → feature → component) | Yes - scope rules | Yes - scope config |

---

## The Sub-Layer Pattern

```
layer_0/layer_0_03_sub_layers/
├── sub_layer_0_01_prompts/        → Referenced for detailed prompts
├── sub_layer_0_02_knowledge/      → Referenced for domain knowledge
├── sub_layer_0_03_principles/     → Referenced for guiding principles
├── sub_layer_0_04_rules/          → CANONICAL source of rules
│   │                                 (detailed docs live here)
│   │
│   │   BUT: Universal rules get COPIED INTO root CLAUDE.md
│   │        so they're in every API call
│   │
└── sub_layer_0_05+_setup/         → Referenced for setup tasks
```

**Key insight:** `sub_layer_0_04_rules/` is the AUTHORITATIVE source, but the rules that must apply everywhere get EMBEDDED into CLAUDE.md files at the appropriate scope.

---

## Current Problem

**Current State:**
- Root CLAUDE.md says "go read rules from sub_layer_0_04_rules/"
- Rules are NOT in the system prompt
- AI must choose to read them (and might not)
- Rules not enforced if session starts outside tree

**Desired State:**
- Root CLAUDE.md CONTAINS the universal rules directly
- sub_layer_0_04_rules/ remains the canonical/detailed source
- Universal rules are in EVERY API call
- Scope-specific rules in scope-specific CLAUDE.md files

---

## Proposed Implementation (Draft)

### Root CLAUDE.md Should Contain:

1. **Universal Rules (embedded)**
   - AI Context Modification Protocol (show diagram, wait for approval)
   - AI Context Commit/Push Rule (commit and push after approved changes)
   - Core safety constraints

2. **Navigation (how to find things)**
   - Sub-layer locations
   - Stage structure
   - Quick lookup table

3. **Conventions**
   - Naming patterns
   - Structure overview

### Each Layer/Stage CLAUDE.md Should Contain:

1. **Scope-specific rules** that apply to every request at that scope
2. **Brief purpose/identity** of this layer/stage
3. **Navigation** within this scope

---

## Proposed: Container-as-Manager Pattern

### Key Insight

**Every folder with a CLAUDE.md is a manager of its contents.**

The 00 position should be reserved for **registry data**, not the manager itself. The **container folder IS the manager**.

### Two Types of Managers

| Type | Purpose | Example |
|------|---------|---------|
| **Collection Manager** | Manages a group of entities | `layer_-1_99_stages/` (stages manager) |
| **Entity Manager** | Manages one entity's content | `stage_-1_02_research/` (stage manager) |

### Full Hierarchy

```
layer_-1/                              ← LAYER manager (manages this layer)
├── CLAUDE.md                          ← Layer management rules
├── .claude/                           ← Layer config
├── layer_-1_00_layer_registry/        ← Just registry DATA
│
├── layer_-1_03_sub_layers/            ← SUB_LAYERS manager (collection)
│   ├── CLAUDE.md                      ← Sub-layers collection rules
│   ├── .claude/
│   ├── sub_layer_-1_00_registry/      ← Just registry DATA
│   │
│   ├── sub_layer_-1_01_prompts/       ← SUB_LAYER manager (entity)
│   │   ├── CLAUDE.md                  ← Prompts management rules
│   │   └── ...
│   │
│   ├── sub_layer_-1_03_principles/    ← SUB_LAYER manager (entity)
│   │   ├── CLAUDE.md                  ← Principles management rules
│   │   └── ...
│   │
│   └── sub_layer_-1_05+_setup/        ← SUB_LAYER manager (entity)
│       ├── CLAUDE.md                  ← Setup management rules
│       └── ...
│
└── layer_-1_99_stages/                ← STAGES manager (collection)
    ├── CLAUDE.md                      ← Stages collection rules
    ├── .claude/                       ← Stages manager config
    ├── hand_off_documents/
    │   ├── incoming/
    │   │   ├── from_above/            ← Tasks from Layer Manager
    │   │   └── from_below/            ← Results from Stage Managers
    │   └── outgoing/
    │       ├── to_above/              ← Results to Layer Manager
    │       └── to_below/              ← Tasks to Stage Managers
    ├── stage_-1_00_registry/          ← Just registry DATA
    │
    ├── stage_-1_01_request_gathering/ ← STAGE manager (entity)
    │   ├── CLAUDE.md                  ← Stage-specific rules
    │   ├── .claude/                   ← Stage config
    │   ├── outputs/                   ← Stage deliverables
    │   └── hand_off_documents/
    │       ├── incoming/
    │       │   ├── from_above/        ← Tasks from Stages Manager
    │       │   └── from_below/        ← Results from Workers
    │       └── outgoing/
    │           ├── to_above/          ← Results to Stages Manager
    │           └── to_below/          ← Tasks to Workers
    │
    └── stage_-1_02_research/          ← STAGE manager (entity)
        ├── CLAUDE.md
        ├── .claude/
        └── ...
```

### Manager Responsibilities

| Manager Type | Responsibilities |
|--------------|------------------|
| **Layer Manager** | Manage layer content, coordinate sub-layers and stages |
| **Sub_Layers Manager** | Create/remove sub-layers, maintain collection consistency |
| **Sub_Layer Manager** | Manage specific content type (prompts, rules, etc.) |
| **Stages Manager** | Create/reorder/remove stages, maintain workflow consistency |
| **Stage Manager** | Execute stage work, produce outputs, hand off to next stage |

### What Each Manager Has

| Component | Collection Manager | Entity Manager |
|-----------|-------------------|----------------|
| CLAUDE.md | Collection rules | Entity rules |
| .claude/ | Collection config | Entity config |
| 00_registry/ | YES (child list) | NO |
| outputs/ | Maybe | YES (if produces) |
| hand_off_documents/ | YES | YES |

### Handoff Document Structure (Per Manager)

```
hand_off_documents/
├── incoming/
│   ├── from_above/      ← Tasks from parent manager
│   └── from_below/      ← Results/escalations from children
│
└── outgoing/
    ├── to_above/        ← Results/escalations to parent
    └── to_below/        ← Tasks delegated to children
```

This four-way structure enables:
- **Downward delegation**: Parent writes to child's `incoming/from_above/`
- **Upward results**: Child writes to own `outgoing/to_above/`, parent reads from `incoming/from_below/`
- **Skip-level escalation**: Child writes directly to ancestor's `incoming/from_below/`

### Current vs Proposed

**Current**: `stage_-1_00_stage_manager/` - Manager is a child entity at position 00

**Proposed**: `layer_-1_99_stages/` IS the stages manager, `stage_-1_00_registry/` is just data

**Benefits**:
1. CLAUDE.md at collection root naturally cascades to all children
2. Clear separation: container = manager, 00 = data
3. Consistent pattern at all levels
4. Manager can delegate tasks to child entities via handoffs

---

## Agent Hierarchy and Communication

### Agent Instantiation (Downward)

Managers can **spawn agents** for entities below them in the hierarchy:

```
Layer Manager
├── spawns → Sub_Layers Manager
│               ├── spawns → Sub_Layer Manager (prompts)
│               ├── spawns → Sub_Layer Manager (rules)
│               └── spawns → Sub_Layer Manager (setup)
│                               └── spawns → Workers
│
└── spawns → Stages Manager
                ├── spawns → Stage Manager (research)
                │               └── spawns → Workers
                └── spawns → Stage Manager (development)
                                └── spawns → Workers
```

**Mechanism**:
- Use Claude Code's `Task` tool to spawn sub-agents
- Pass context via handoff documents
- Sub-agent works within its scope (constrained by its CLAUDE.md)

### Communication (Upward - Can Skip Levels)

Agents can **communicate back** to managers multiple levels above:

```
Worker in stage_02_research
│
├── reports to → Stage Manager (direct parent)
├── reports to → Stages Manager (grandparent)
└── reports to → Layer Manager (great-grandparent)
```

**Use cases for skip-level communication**:
- Worker discovers issue affecting entire layer → escalate to Layer Manager
- Stage finds conflict with another stage → report to Stages Manager
- Sub-layer needs cross-cutting change → escalate to Sub_Layers Manager

**Mechanism**:
- Write to `hand_off_documents/outgoing/` at appropriate level
- Include `escalation: true` or `target_level: layer` in handoff
- Parent managers check for escalated handoffs from descendants

### Handoff Document Structure

Each manager has **four** handoff directions:

```
hand_off_documents/
├── incoming/
│   ├── from_above/      ← Tasks delegated FROM parent manager
│   └── from_below/      ← Results/escalations FROM child agents
│
└── outgoing/
    ├── to_above/        ← Results/escalations TO parent manager
    └── to_below/        ← Tasks delegated TO child agents
```

### Handoff Document Flow

```
Downward (task delegation):
Layer Manager
  → writes to layer_-1_99_stages/hand_off_documents/incoming/from_above/
    → Stages Manager reads, delegates to appropriate stage
      → writes to stage_-1_02_research/hand_off_documents/incoming/from_above/
        → Stage Manager reads, executes or spawns workers

Upward (results):
Worker completes task
  → writes to stage_-1_02_research/hand_off_documents/outgoing/to_above/
    → Stage Manager reads, aggregates
      → writes to stages/hand_off_documents/outgoing/to_above/
        → Stages Manager reads, aggregates
          → writes to layer/hand_off_documents/incoming/from_below/
            → Layer Manager receives final results

Skip-level escalation:
Worker finds layer-wide issue
  → writes DIRECTLY to layer_-1/hand_off_documents/incoming/from_below/
    → Layer Manager sees escalation, handles or delegates
```

### Communication Matrix

| Manager | Receives FROM | Sends TO |
|---------|---------------|----------|
| **Layer Manager** | Above: external/user | Above: external/user |
| | Below: stages, sub_layers | Below: stages, sub_layers |
| **Stages Manager** | Above: layer manager | Above: layer manager |
| | Below: individual stages | Below: individual stages |
| **Stage Manager** | Above: stages manager | Above: stages manager |
| | Below: workers | Below: workers |

### Agent Configuration Location

Each manager's agent configuration lives in its `.claude/` folder:

| Manager | Agent Config Location |
|---------|----------------------|
| Layer Manager | `layer_-1/.claude/agents/` |
| Stages Manager | `layer_-1_99_stages/.claude/agents/` |
| Stage Manager | `stage_-1_02_research/.claude/agents/` |
| Sub_Layers Manager | `layer_-1_03_sub_layers/.claude/agents/` |
| Sub_Layer Manager | `sub_layer_-1_04_rules/.claude/agents/` |

---

## Practical Usage: How to Instantiate and Use

### Scenario: User Wants Research Done

**Step 1: User starts session at Layer level**
```bash
cd /path/to/layer_-1/
claude
```

**Step 2: Layer Manager reads context**
- Claude Code loads `layer_-1/CLAUDE.md` (+ ancestors)
- Agent understands: "I am the Layer Manager for better_ai_system"
- Agent checks `hand_off_documents/incoming/from_above/` for tasks
- User provides task: "Research system prompt architecture"

**Step 3: Layer Manager delegates to Stages Manager**
```markdown
# File: layer_-1_99_stages/hand_off_documents/incoming/from_above/20260126_research_task.md

## Task
Research system prompt architecture patterns

## Constraints
- Follow research stage guidelines
- Document findings in outputs/

## Expected Output
- Research document in stage_02_research/outputs/
- Handoff when complete
```

Layer Manager then spawns Stages Manager:
```
Task tool → working directory: layer_-1_99_stages/
           prompt: "Process incoming task from from_above/"
```

**Step 4: Stages Manager delegates to Stage Manager**
- Stages Manager reads `incoming/from_above/20260126_research_task.md`
- Determines: this is research work → delegate to stage_02_research
- Writes to `stage_-1_02_research/hand_off_documents/incoming/from_above/`
- Spawns Stage Manager for research stage

**Step 5: Stage Manager executes work**
- Stage Manager reads task from `incoming/from_above/`
- Executes research within its scope
- May spawn workers for parallel subtasks
- Produces outputs in `outputs/`
- Writes results to `outgoing/to_above/`

**Step 6: Results flow back up**
```
Stage Manager writes → stage_02/outgoing/to_above/
Stages Manager reads → stages/incoming/from_below/
Stages Manager writes → stages/outgoing/to_above/
Layer Manager reads → layer/incoming/from_below/
Layer Manager reports to user
```

---

### Practical Commands

**Starting as a specific manager:**
```bash
# Start as Layer Manager
cd layer_-1/ && claude

# Start as Stages Manager
cd layer_-1/layer_-1_99_stages/ && claude

# Start as Stage Manager (research)
cd layer_-1/layer_-1_99_stages/stage_-1_02_research/ && claude
```

**Spawning a sub-agent (from within Claude Code):**
```
Use Task tool:
- subagent_type: "general-purpose"
- prompt: "You are the Stages Manager. Read incoming/from_above/ and process tasks."
- Working directory set to child's folder
```

**Writing a handoff document:**
```markdown
# File: hand_off_documents/outgoing/to_above/20260126_task_complete.md

## Task Reference
20260126_research_task.md

## Status
Complete

## Results
- Created: outputs/01_understanding_in_progress/by_topic/system_prompt_architecture.md
- Documented: system prompt vs referenced, container-as-manager pattern, agent hierarchy

## Next Steps
Ready for user review and approval
```

---

### Agent Lifecycle

```
┌─────────────────────────────────────────────────────────────────────┐
│ 1. INITIALIZE                                                        │
│    - Claude Code loads CLAUDE.md cascade                            │
│    - Agent reads .claude/settings.json for context                  │
│    - Agent understands its role (Layer/Stages/Stage Manager)        │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 2. CHECK FOR WORK                                                    │
│    - Read hand_off_documents/incoming/from_above/                   │
│    - Read hand_off_documents/incoming/from_below/ (escalations)     │
│    - If no handoffs, wait for user input                            │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 3. PROCESS TASK                                                      │
│    Option A: Execute directly (if within scope)                     │
│    Option B: Delegate to child (spawn sub-agent)                    │
│    Option C: Escalate to parent (if beyond scope)                   │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 4. PRODUCE OUTPUT                                                    │
│    - Write deliverables to outputs/                                 │
│    - Write results to outgoing/to_above/                            │
│    - Write delegations to child's incoming/from_above/              │
└─────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────┐
│ 5. MONITOR (if delegated)                                            │
│    - Check incoming/from_below/ for child results                   │
│    - Aggregate results                                              │
│    - Continue or report completion                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Example: Skip-Level Escalation

**Worker in stage_02_research finds issue affecting entire layer:**

```markdown
# File: layer_-1/hand_off_documents/incoming/from_below/20260126_escalation.md

## Escalation
From: stage_-1_02_research (worker)
To: Layer Manager
Skip: Stages Manager

## Issue
Discovered naming inconsistency across ALL stages -
this affects layer-wide conventions, not just research stage.

## Recommendation
Layer Manager should coordinate cross-stage fix.

## Evidence
- stage_01 uses "request_gathering"
- stage_04 uses "planning"
- Inconsistent with design doc which says "04_design" before "05_planning"
```

**Layer Manager receives escalation:**
- Reads from `incoming/from_below/`
- Sees escalation flag / recognizes it skipped Stages Manager
- Handles directly or creates coordinated task for Stages Manager

---

### CLAUDE.md Content for Each Manager Role

**Layer Manager CLAUDE.md should include:**
```markdown
## Role
You are the Layer Manager for [layer_name].

## Responsibilities
- Coordinate work across sub_layers and stages
- Delegate tasks to appropriate child managers
- Receive and aggregate results from children
- Handle escalations from any descendant

## On Session Start
1. Check hand_off_documents/incoming/from_above/ for tasks
2. Check hand_off_documents/incoming/from_below/ for results/escalations
3. Process or await user input
```

**Stage Manager CLAUDE.md should include:**
```markdown
## Role
You are the Stage Manager for [stage_name].

## Responsibilities
- Execute work within this stage's scope
- Produce outputs in outputs/
- Report results to Stages Manager
- Escalate issues beyond stage scope

## On Session Start
1. Check hand_off_documents/incoming/from_above/ for tasks
2. Execute or delegate to workers
3. Write results to hand_off_documents/outgoing/to_above/
```

---

## System-Wide Implementation

### Phase 1: Establish Root Manager

**Location**: `0_layer_universal/`

```
0_layer_universal/                    ← ROOT manager (manages everything)
├── CLAUDE.md                         ← Universal rules + manager role
├── .claude/
│   ├── settings.json
│   ├── agents/
│   ├── commands/
│   └── skills/
├── hand_off_documents/
│   ├── incoming/
│   │   ├── from_above/               ← External user requests
│   │   └── from_below/               ← Results from layer_0, layer_1, layer_-1
│   └── outgoing/
│       ├── to_above/                 ← Results to external user
│       └── to_below/                 ← Tasks to child layers
│
├── layer_0/                          ← LAYER manager (universal layer)
├── layer_1/                          ← LAYERS manager (projects collection)
│   └── layer_1_projects/             ← Contains project layers
└── layer_-1_research/                ← LAYERS manager (research collection)
    └── layer_-1_better_ai_system/    ← LAYER manager (this research project)
```

### Phase 2: Standardize All Layer Containers

Every layer container becomes a manager:

```bash
# For each layer container, ensure:
layer_X/
├── CLAUDE.md                         # Manager rules for this layer
├── .claude/                          # Manager config
├── hand_off_documents/
│   ├── incoming/from_above/
│   ├── incoming/from_below/
│   ├── outgoing/to_above/
│   └── outgoing/to_below/
├── layer_X_00_layer_registry/        # Just data (rename from layer_manager if exists)
├── layer_X_03_sub_layers/            # Sub_layers manager
└── layer_X_99_stages/                # Stages manager
```

### Phase 3: Standardize All Stages Containers

Every `layer_X_99_stages/` folder becomes a stages manager:

```bash
layer_X_99_stages/                    # STAGES manager
├── CLAUDE.md                         # Stages collection rules
├── .claude/
├── hand_off_documents/
│   ├── incoming/from_above/
│   ├── incoming/from_below/
│   ├── outgoing/to_above/
│   └── outgoing/to_below/
├── stage_X_00_registry/              # Just data (rename from stage_manager)
├── stage_X_01_request_gathering/     # Stage manager
├── stage_X_02_research/              # Stage manager
└── ...
```

### Phase 4: Standardize All Stage Folders

Every individual stage becomes a stage manager:

```bash
stage_X_02_research/                  # STAGE manager
├── CLAUDE.md                         # Stage-specific rules
├── .claude/
├── hand_off_documents/
│   ├── incoming/from_above/
│   ├── incoming/from_below/
│   ├── outgoing/to_above/
│   └── outgoing/to_below/
└── outputs/
```

### Phase 5: Standardize Sub_layers

Every `layer_X_03_sub_layers/` and each sub_layer becomes a manager:

```bash
layer_X_03_sub_layers/                # SUB_LAYERS manager
├── CLAUDE.md
├── .claude/
├── hand_off_documents/...
├── sub_layer_X_00_registry/          # Just data
├── sub_layer_X_01_prompts/           # Sub_layer manager
├── sub_layer_X_02_knowledge_system/  # Sub_layer manager
├── sub_layer_X_03_principles/        # Sub_layer manager
├── sub_layer_X_04_rules/             # Sub_layer manager
└── sub_layer_X_05+_setup/            # Sub_layer manager
```

---

### Migration Script Outline

```bash
#!/bin/bash
# migrate_to_manager_pattern.sh

# For each layer, stages container, stage, sub_layers container, sub_layer:

create_manager_structure() {
    local path=$1

    # Create hand_off_documents structure
    mkdir -p "$path/hand_off_documents/incoming/from_above"
    mkdir -p "$path/hand_off_documents/incoming/from_below"
    mkdir -p "$path/hand_off_documents/outgoing/to_above"
    mkdir -p "$path/hand_off_documents/outgoing/to_below"

    # Create .claude structure if not exists
    mkdir -p "$path/.claude/agents"
    mkdir -p "$path/.claude/commands"
    mkdir -p "$path/.claude/skills"

    # Ensure CLAUDE.md exists
    if [ ! -f "$path/CLAUDE.md" ]; then
        echo "# $(basename $path)" > "$path/CLAUDE.md"
        echo "" >> "$path/CLAUDE.md"
        echo "## Role" >> "$path/CLAUDE.md"
        echo "Manager for $(basename $path)" >> "$path/CLAUDE.md"
    fi
}

# Rename 00_stage_manager → 00_registry
rename_manager_to_registry() {
    local stages_path=$1
    if [ -d "$stages_path/stage_*_00_stage_manager" ]; then
        # Move CLAUDE.md and .claude/ content up to stages_path
        # Rename folder to registry
        # Keep only data files in registry
    fi
}
```

---

### Verification Checklist

After migration, verify:

- [ ] Every layer has: CLAUDE.md, .claude/, hand_off_documents/
- [ ] Every stages container has: CLAUDE.md, .claude/, hand_off_documents/, 00_registry/
- [ ] Every stage has: CLAUDE.md, .claude/, hand_off_documents/, outputs/
- [ ] Every sub_layers container has: CLAUDE.md, .claude/, hand_off_documents/, 00_registry/
- [ ] Every sub_layer has: CLAUDE.md, .claude/, hand_off_documents/
- [ ] All 00 positions are registries (data only), not managers
- [ ] All hand_off_documents/ have four subdirectories

---

### Testing the System

**Test 1: Simple delegation**
```bash
# Start at root
cd 0_layer_universal && claude

# User: "Create a new principle about code quality"
# Expected: Root → layer_0 → sub_layers → principles sub_layer
# Verify: handoff docs created at each level
```

**Test 2: Skip-level escalation**
```bash
# Start at a stage
cd layer_-1/layer_-1_99_stages/stage_-1_02_research && claude

# Discover issue affecting all stages
# Write escalation directly to layer_-1/hand_off_documents/incoming/from_below/
# Verify: Layer Manager sees escalation
```

**Test 3: Results aggregation**
```bash
# Complete work in stage
# Write to outgoing/to_above/
# Verify: Stages Manager aggregates
# Verify: Layer Manager receives final result
```

---

## Open Questions

### System Prompt Content

1. **What specific rules should be IN the root CLAUDE.md?**
   - AI Context Modification Protocol? (full or summary?)
   - AI Context Commit/Push Rule? (full or summary?)
   - Safety governance? (which parts?)
   - Layer Context Header Protocol?
   - Others?

2. **How to handle duplication between CLAUDE.md and sub_layer_0_04_rules/?**
   - Accept duplication, keep both in sync?
   - CLAUDE.md has summary, sub_layer has full detail?
   - Single source of truth approach?
   - Automated sync mechanism?

### .claude/ Folder Questions

3. **How should .claude/settings.json context be used?**
   - Currently has `context` field with stage/layer/purpose
   - Should this influence AI behavior beyond permissions?
   - Could this be used for semantic layer identification?

4. **What is the intended hierarchy for .claude/ folders?**
   - Should they cascade like CLAUDE.md files?
   - Or are they strictly local to each scope?
   - How do root `.claude/` permissions interact with nested ones?

5. **How should hooks be utilized?**
   - `SessionStart` for stage initialization?
   - `PreToolUse` / `PostToolUse` for rule enforcement?
   - What belongs in hooks vs in system prompt?

6. **Should skills/commands be standardized?**
   - Stage-specific workflows in `skills/`?
   - Common commands across all stages?
   - Naming conventions for commands?

### Entity Structure Questions

7. **How should ai_manager_system/ influence sessions?**
   - Should managers read from this before starting work?
   - How do manager/worker roles map to actual sessions?
   - Integration with handoff documents?

8. **How should handoff_documents/ be used in practice?**
   - When does AI read incoming handoffs?
   - When does AI write outgoing handoffs?
   - Should this be in CLAUDE.md navigation?

### Container-as-Manager Pattern Questions

9. **Should ALL containers have CLAUDE.md files?**
   - Every sub_layer folder?
   - Every nested setup folder?
   - Where is the line for "too much"?

10. **What goes in a collection manager vs entity manager CLAUDE.md?**
    - Collection: rules for adding/removing/ordering children?
    - Entity: rules for working within that entity?
    - How much overlap?

11. **Migration path from current structure?**
    - Move `stage_-1_00_stage_manager/` content to `layer_-1_99_stages/`?
    - Rename `stage_-1_00_stage_manager/` to `stage_-1_00_registry/`?
    - What about existing references?

### Agent Hierarchy Questions

12. **How does skip-level communication work in practice?**
    - Special `escalations/` folder in hand_off_documents?
    - Metadata in handoff (target_level, escalation flag)?
    - How does parent know to check for grandchild messages?

13. **How are sub-agents spawned?**
    - Claude Code `Task` tool with specific working directory?
    - Pass handoff document path as context?
    - How does spawned agent know its role/scope?

14. **How do agents know their position in hierarchy?**
    - From CLAUDE.md context?
    - From `.claude/settings.json` metadata?
    - Explicitly passed when spawned?

15. **What prevents infinite spawning loops?**
    - Max depth limit?
    - Budget/token limits?
    - Explicit "leaf node" designation for workers?

### Practical Questions

12. **What about sessions starting outside the tree?**
    - Still a problem even with embedded rules
    - Alias approach? Global settings?
    - User education?

13. **How to test rule propagation?**
    - Verification that rules are actually in API calls?
    - Testing across different entry points?

---

## Related Research

### In This Research Stage
- `rule_propagation_problem.md` - Documents the original issue
- `memory_systems.md` - CLAUDE.md as navigation guide discussion
- `existing_solutions.md` - Clawdbot's SKILL.md pattern

### Key Source Files Examined
- `layer_0/layer_0_00_layer_registry/README.md` - Layer entity structure definition
- `layer_0/layer_0_01_ai_manager_system/README.md` - Manager/worker patterns
- `layer_0/layer_0_02_manager_handoff_documents/README.md` - Handoff protocol
- `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` - Canonical rules location
- Various `.claude/` folders - Claude Code configuration patterns

---

## Next Steps

1. User to clarify/correct understanding
2. User to specify which rules to embed
3. User to approve approach
4. Move to `stage_-1_03_instructions/` when ready
5. Create detailed implementation instructions
6. Execute changes following modification protocol
