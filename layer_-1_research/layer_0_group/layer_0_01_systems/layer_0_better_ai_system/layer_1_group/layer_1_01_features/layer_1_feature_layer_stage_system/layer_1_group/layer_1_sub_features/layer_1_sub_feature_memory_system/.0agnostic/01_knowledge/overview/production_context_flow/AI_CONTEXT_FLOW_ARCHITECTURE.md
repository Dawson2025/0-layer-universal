---
resource_id: "6818d384-9f58-4999-aef6-1c0318cf2a10"
resource_type: "knowledge"
resource_name: "AI_CONTEXT_FLOW_ARCHITECTURE"
---
# AI Context Flow Architecture

## Complete System Overview

This document explains the full flow of how AI agents receive context, navigate the system, and access the knowledge they need.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AI AGENT SESSION START                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. TOOL-SPECIFIC SYSTEM PROMPTS LOADED (Layer Cascade)                     │
│                                                                             │
│     ~/.claude/CLAUDE.md              (Global user config)                   │
│            │                                                                │
│            ▼                                                                │
│     layer_0/CLAUDE.md                (Universal - applies to ALL)           │
│            │                                                                │
│            ▼                                                                │
│     layer_1/layer_1_project_X/CLAUDE.md    (Project-specific)              │
│            │                                                                │
│            ▼                                                                │
│     layer_2_group/layer_2_feature_Y/CLAUDE.md   (Feature-specific)         │
│            │                                                                │
│            ▼                                                                │
│     layer_3_group/layer_3_component_Z/CLAUDE.md  (Component-specific)      │
│                                                                             │
│  Each CLAUDE.md contains:                                                   │
│    - Identity (who am I at this layer)                                      │
│    - CRITICAL RULES (must follow EVERY API call at this layer or deeper)   │
│    - Triggers (when to activate)                                            │
│    - Pointers to .claude/ and sub_layers                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  2. CLAUDE.md POINTS TO .claude/ (Tool-Specific Config)                     │
│                                                                             │
│     CLAUDE.md ──────────▶ .claude/                                         │
│                           ├── settings.json     (permissions, config)       │
│                           ├── commands/         (custom commands)           │
│                           └── ...               (other Claude Code config)  │
│                                                                             │
│     Similarly for other tools:                                              │
│     .cursorrules ────────▶ Cursor-specific behavior                        │
│     GEMINI.md ───────────▶ Gemini-specific context                         │
│     AGENTS.md ───────────▶ Codex/agents context                            │
│     .github/copilot-instructions.md ──▶ Copilot context                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. .0agnostic/ IS THE SYNC SOURCE (Generates All Tool Files)               │
│                                                                             │
│     ┌────────────────────────────────────────────────────────────────┐     │
│     │                     0AGNOSTIC.md                                │     │
│     │              (Tool-agnostic source of truth)                    │     │
│     └───────────────────────────┬────────────────────────────────────┘     │
│                                 │                                           │
│                                 ▼                                           │
│     ┌────────────────────────────────────────────────────────────────┐     │
│     │                     .0agnostic/                                 │     │
│     │   ├── hooks/scripts/agnostic-sync.sh   (sync script)           │     │
│     │   ├── skills/                          (loadable skills)        │     │
│     │   ├── agents/                          (agent definitions)      │     │
│     │   ├── episodic/                        (session memory)         │     │
│     │   └── templates/                       (instantiation templates)│     │
│     └───────────────────────────┬────────────────────────────────────┘     │
│                                 │                                           │
│                                 │ agnostic-sync.sh generates:              │
│                                 ▼                                           │
│     ┌─────────────────────────────────────────────────────────────────┐    │
│     │  CLAUDE.md          (.claude/ folder)                           │    │
│     │  .cursorrules                                                    │    │
│     │  GEMINI.md                                                       │    │
│     │  AGENTS.md          (.codex/ if applicable)                     │    │
│     │  .github/copilot-instructions.md                                │    │
│     │  .aider.conf.yml                                                 │    │
│     └─────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## CRITICAL RULES: Every API Call Enforcement

### What Are Critical Rules?

Critical rules are constraints that **MUST be followed on EVERY API call** when working at a layer or any deeper layer within it.

### How Critical Rules Cascade

```
layer_0/CLAUDE.md
├── CRITICAL RULES (apply to ALL work everywhere)
│   - "Always cite sources with research"
│   - "Show diagram before modifying AI context files"
│   - "Commit AI context changes with [AI Context] prefix"
│
└── layer_1/project/CLAUDE.md
    ├── INHERITS: All layer_0 critical rules
    ├── ADDS: Project-specific critical rules
    │   - "Follow REST API conventions"
    │   - "All endpoints require authentication"
    │
    └── layer_2_group/feature/CLAUDE.md
        ├── INHERITS: All layer_0 + layer_1 critical rules
        ├── ADDS: Feature-specific critical rules
        │   - "Validate all user input"
        │   - "Log all authentication attempts"
        │
        └── layer_3_group/component/CLAUDE.md
            ├── INHERITS: All layer_0 + layer_1 + layer_2 critical rules
            └── ADDS: Component-specific critical rules
```

### Critical Rules in System Prompt Files

Every CLAUDE.md (and equivalent files) MUST include:

```markdown
## [CRITICAL] Rules - EVERY API Call

These rules MUST be followed on EVERY output, at this layer and all deeper layers:

### Inherited from layer_0 (Universal)
- [ ] Always cite sources when doing research
- [ ] Show diagram and wait for approval before modifying AI context files
- [ ] Commit AI context changes with `[AI Context]` prefix

### Inherited from layer_1 (Project)
- [ ] Follow project coding standards
- [ ] All API endpoints require auth

### This Layer (layer_2 Feature)
- [ ] Validate all inputs before processing
- [ ] Log security-relevant events

---
Failure to follow these rules is a violation. Always verify compliance.
```

---

## Layer Cascade: Full Example

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LAYER CASCADE EXAMPLE                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  layer_0/CLAUDE.md                    UNIVERSAL LAYER                       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Identity: Universal rules manager                                    │   │
│  │ CRITICAL RULES:                                                      │   │
│  │   - Always traverse context before starting tasks                    │   │
│  │   - Document work in correct layer and stage                        │   │
│  │   - Show diagram before AI context modifications                    │   │
│  │ Points to: .claude/, layer_0_03_sub_layers/                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│         │                                                                   │
│         │ inherits + adds                                                   │
│         ▼                                                                   │
│  layer_1/layer_1_project_myapp/CLAUDE.md      PROJECT LAYER                │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Identity: Project manager for myapp                                  │   │
│  │ CRITICAL RULES:                                                      │   │
│  │   - [Inherited from layer_0]                                        │   │
│  │   - Use TypeScript for all code                                     │   │
│  │   - Follow myapp coding standards                                   │   │
│  │ Points to: .claude/, layer_1_group/layer_1_03_sub_layers/           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│         │                                                                   │
│         │ inherits + adds                                                   │
│         ▼                                                                   │
│  .../layer_2_group/layer_2_feature_auth/CLAUDE.md    FEATURE LAYER         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Identity: Auth feature developer                                     │   │
│  │ CRITICAL RULES:                                                      │   │
│  │   - [Inherited from layer_0 + layer_1]                              │   │
│  │   - Never log passwords or tokens                                   │   │
│  │   - All auth endpoints require rate limiting                        │   │
│  │ Points to: .claude/, layer_2_group/layer_2_03_sub_layers/           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│         │                                                                   │
│         │ inherits + adds                                                   │
│         ▼                                                                   │
│  .../layer_3_group/layer_3_component_jwt/CLAUDE.md   COMPONENT LAYER       │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Identity: JWT token handler                                          │   │
│  │ CRITICAL RULES:                                                      │   │
│  │   - [Inherited from layer_0 + layer_1 + layer_2]                    │   │
│  │   - Use RS256 algorithm only                                        │   │
│  │   - Tokens expire in 1 hour max                                     │   │
│  │ Points to: .claude/, layer_3_group/layer_3_03_sub_layers/           │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Complete Reference Chain

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        COMPLETE REFERENCE ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SYNC SOURCE                    GENERATED FILES              TOOL CONFIG    │
│  ───────────                    ───────────────              ───────────    │
│                                                                             │
│  ┌──────────────┐               ┌──────────────┐            ┌────────────┐ │
│  │ 0AGNOSTIC.md │───────────────│  CLAUDE.md   │───────────▶│  .claude/  │ │
│  │              │    sync       │              │  points to │            │ │
│  │ (edit this)  │               │ (generated)  │            │ (config)   │ │
│  └──────────────┘               └──────────────┘            └────────────┘ │
│         │                              │                                    │
│         │                              │                                    │
│  ┌──────────────┐               ┌──────────────┐                           │
│  │ .0agnostic/  │───────────────│ .cursorrules │                           │
│  │              │    sync       │              │                           │
│  │ - hooks      │               │ (generated)  │                           │
│  │ - skills     │               └──────────────┘                           │
│  │ - agents     │                      │                                    │
│  │ - episodic   │               ┌──────────────┐                           │
│  │ - templates  │───────────────│  GEMINI.md   │                           │
│  └──────────────┘    sync       │              │                           │
│                                 │ (generated)  │                           │
│                                 └──────────────┘                           │
│                                        │                                    │
│                                 ┌──────────────┐            ┌────────────┐ │
│                      ───────────│  AGENTS.md   │───────────▶│  .codex/   │ │
│                         sync    │              │  points to │            │ │
│                                 │ (generated)  │            │ (config)   │ │
│                                 └──────────────┘            └────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## What CLAUDE.md Points To

```
CLAUDE.md
│
├──▶ .claude/                         Tool-specific config
│    ├── settings.json                Permissions, preferences
│    ├── commands/                    Custom slash commands
│    └── ...
│
├──▶ layer_N_group/                   This layer's content
│    ├── layer_N_03_sub_layers/
│    │   ├── sub_layer_N_01_prompts/       Session init, task prompts
│    │   ├── sub_layer_N_02_knowledge/     Domain knowledge
│    │   ├── sub_layer_N_03_principles/    Guiding principles
│    │   ├── sub_layer_N_04_rules/         Mandatory rules (beyond critical)
│    │   └── sub_layer_N_05+_hierarchy/    Setup-dependent config
│    │
│    └── layer_N_99_stages/
│        ├── stage_01-11/             Workflow stages
│        └── outputs/                 Work products
│
└──▶ Parent CLAUDE.md                 Inherited context (cascade up)
```

---

## What .0agnostic/ Is For

**.0agnostic/ is NOT loaded by tools directly.** It is the **sync source** that generates all tool-specific files.

### Purpose of .0agnostic/

| Folder | Purpose |
|--------|---------|
| `hooks/scripts/agnostic-sync.sh` | Generates CLAUDE.md, .cursorrules, GEMINI.md, etc. |
| `skills/` | Skill definitions (synced to tool-specific locations) |
| `agents/` | Agent definitions (synced to tool-specific locations) |
| `episodic/` | Session memory (can be synced or referenced) |
| `templates/` | Templates for instantiating new entities |

### Sync Workflow

```
1. Edit 0AGNOSTIC.md (identity, triggers, critical rules)
2. Edit .0agnostic/* (skills, agents, templates)
3. Run: bash .0agnostic/hooks/scripts/agnostic-sync.sh all
4. Generated files are updated:
   - CLAUDE.md (points to .claude/)
   - .cursorrules
   - GEMINI.md
   - AGENTS.md
   - etc.
```

---

## Critical Rules Template for System Prompts

Every generated system prompt file should include:

```markdown
## [CRITICAL] Rules - Enforced Every API Call

⚠️ These rules MUST be followed on EVERY output at this layer and deeper.

### Universal (from layer_0)
1. **Context Traversal**: Read CLAUDE.md files from root to current before starting
2. **AI Context Modification**: Show diagram, wait for approval before changes
3. **Documentation**: Document work in correct layer and stage
4. **Sources**: Include sources with all research

### Project (from layer_1) [if applicable]
1. [Project-specific critical rule]
2. [Project-specific critical rule]

### Feature (from layer_2) [if applicable]
1. [Feature-specific critical rule]
2. [Feature-specific critical rule]

### This Layer
1. [This layer's specific critical rule]
2. [This layer's specific critical rule]

---

**Self-Check Before Every Response:**
- [ ] Did I read relevant CLAUDE.md files?
- [ ] Am I following ALL inherited critical rules?
- [ ] Am I following this layer's critical rules?
```

---

## Summary: The Complete Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                    COMPLETE CONTEXT FLOW                          │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   0AGNOSTIC.md          Source of truth (edit this)              │
│        │                                                         │
│        │ syncs via agnostic-sync.sh                              │
│        ▼                                                         │
│   CLAUDE.md             Tool-specific (auto-generated)           │
│   + CRITICAL RULES      Enforced every API call                  │
│        │                                                         │
│        │ cascades through layers                                 │
│        ▼                                                         │
│   layer_0/CLAUDE.md     Universal critical rules                 │
│        │                                                         │
│        ▼                                                         │
│   layer_1/CLAUDE.md     + Project critical rules                 │
│        │                                                         │
│        ▼                                                         │
│   layer_1/CLAUDE.md     + Feature critical rules                 │
│        │                                                         │
│        │ points to                                               │
│        ▼                                                         │
│   .claude/              Tool-specific config                     │
│   sub_layers/           Knowledge, rules, prompts, setup         │
│   99_stages/            Current work, outputs                    │
│        │                                                         │
│        │ enables                                                 │
│        ▼                                                         │
│   AGENT ACTION          With all critical rules enforced         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Sub-Layers as Entry Points

Sub-layers can also be agent entry points with their own context cascade:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SUB-LAYER CONTEXT CASCADE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  layer_0/CLAUDE.md                           (Universal)                    │
│       │                                                                     │
│       ▼                                                                     │
│  layer_0_03_sub_layers/CLAUDE.md             (Sub-layers root)             │
│       │                                                                     │
│       ▼                                                                     │
│  sub_layer_0_02_knowledge_system/CLAUDE.md   (Specific sub-layer)          │
│       │                                                                     │
│       │ points to                                                           │
│       ▼                                                                     │
│  .claude/                                    (tool config)                  │
│  .0agnostic/                                 (sync source)                  │
│                                                                             │
│  CRITICAL RULES INHERITED:                                                  │
│  - All layer_0 rules                                                        │
│  - Sub_layers root rules (if any)                                          │
│  - This sub-layer's specific rules                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**See**: `layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md` for full details.

---

## Nested Depth Naming (subxN)

When sub-layers contain nested sub-layers, use depth indicators:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    NESTED SUB-LAYER DEPTH                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Depth 1:  sub_layer_0_05_operating_systems/                               │
│                 │                                                           │
│                 ▼                                                           │
│  Depth 2:  subx2_layer_0_05_linux_ubuntu/                                  │
│                 │                                                           │
│                 ▼                                                           │
│  Depth 3:  subx2_layer_0_06_local/                                         │
│                 │                                                           │
│                 ▼                                                           │
│  Depth 4:  subx3_layer_0_07_cursor/                                        │
│                                                                             │
│  Pattern: subx{N}_layer_{layer}_{seq}_{name}/                              │
│                                                                             │
│  Context cascades through each depth level:                                 │
│  layer_0 → depth_1 → depth_2 → depth_3 → depth_4                           │
│                                                                             │
│  Each depth can have CLAUDE.md and add critical rules.                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**See**: `layer_stage_system/NESTED_DEPTH_NAMING.md` for full details.

---

## Sub-Stages within Stages

Stages can contain sub-stages for finer workflow phases:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SUB-STAGE CONTEXT CASCADE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  layer_1/CLAUDE.md                           (Project)                      │
│       │                                                                     │
│       ▼                                                                     │
│  layer_1_99_stages/CLAUDE.md                 (Stages root)                 │
│       │                                                                     │
│       ▼                                                                     │
│  stage_06_development/CLAUDE.md              (Parent stage)                │
│       │                                                                     │
│       ▼                                                                     │
│  sub_stage_06_02_implementation/CLAUDE.md    (Sub-stage depth 1)           │
│       │                                                                     │
│       ▼                                                                     │
│  subx2_stage_06_02_02_services/CLAUDE.md     (Sub-stage depth 2)           │
│                                                                             │
│  Pattern: subx{N}_stage_{layer}_{parent}_{seq}_{name}/                     │
│                                                                             │
│  Each sub-stage:                                                            │
│  - Inherits parent stage rules                                             │
│  - Has own outputs/ and hand_off_documents/                                │
│  - Can add specific critical rules                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**See**: `layer_stage_system/SUB_STAGES_EXPLAINED.md` for full details.

---

## [CRITICAL] Propagation Chain Requirement

**When modifying AI context (rules, knowledge, skills, CLAUDE.md, etc.), you MUST show a propagation chain diagram.**

### What is a Propagation Chain?

Changes to AI context flow through multiple layers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROPAGATION CHAIN                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. KNOWLEDGE (Source of truth for CONTENT)                                │
│     sub_layer_0_02_knowledge_system/                                       │
│     sub_layer_0_04_rules/                                                  │
│          │                                                                  │
│          │ referenced by                                                   │
│          ▼                                                                  │
│  2. AGNOSTIC SOURCE (Source of truth for SKILLS)                           │
│     0AGNOSTIC.md                                                           │
│     .0agnostic/skills/                                                     │
│          │                                                                  │
│          │ agnostic-sync.sh generates                                      │
│          ▼                                                                  │
│  3. TOOL-SPECIFIC FILES (Generated, minimal)                               │
│     CLAUDE.md → points to .claude/                                         │
│     GEMINI.md → points to .gemini/                                         │
│     AGENTS.md → points to .codex/                                          │
│          │                                                                  │
│          │ contain                                                          │
│          ▼                                                                  │
│  4. TOOL FOLDERS (Skills with references)                                  │
│     .claude/skills/SKILLS.md                                               │
│     .claude/skills/skill-X/SKILL.md                                        │
│     .claude/skills/skill-X/references/ → points to knowledge               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Required Diagram for AI Context Changes

Before modifying AI context, show:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROPAGATION CHAIN DIAGRAM (Required for AI Context Changes)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER 1: Knowledge (what file?)                                           │
│  ─────────────────────────────────                                          │
│  File: [path to knowledge doc]                                             │
│  Change: [what content is being added/modified]                            │
│                                                                             │
│  LAYER 2: Skills (which skills reference this?)                            │
│  ──────────────────────────────────────────────                             │
│  Skill: [skill name]                                                       │
│  Reference: [how skill points to knowledge]                                │
│                                                                             │
│  LAYER 3: Tool Files (what gets regenerated?)                              │
│  ─────────────────────────────────────────────                              │
│  Files: CLAUDE.md, GEMINI.md, AGENTS.md (if affected)                      │
│                                                                             │
│  LAYER 4: How Agents Use It                                                │
│  ──────────────────────────────                                             │
│  Agent loads skill → skill loads references → agent learns [what]          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why This Matters

1. **Traceability**: Know where content lives and how it flows
2. **Consistency**: Ensure all tools get the update
3. **No Amnesia**: Agents always find the knowledge through skills
4. **Maintainability**: Clear update path when things change

---

## Skills Architecture

Skills are the bridge between CLAUDE.md and knowledge:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SKILLS ARCHITECTURE                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CLAUDE.md (minimal)                                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ - Identity                                                          │   │
│  │ - Critical Rules                                                    │   │
│  │ - Triggers                                                          │   │
│  │ - Pointer: "Load skills from .claude/skills/"                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       │ points to                                                          │
│       ▼                                                                     │
│  .claude/skills/SKILLS.md (index)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ | Skill | Trigger | Folder |                                       │   │
│  │ | entity-creation | creating entities | entity-creation/ |         │   │
│  │ | stage-workflow | working with stages | stage-workflow/ |         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       │ agent loads relevant skill                                         │
│       ▼                                                                     │
│  .claude/skills/entity-creation/SKILL.md                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ## References (MUST READ)                                          │   │
│  │ - layer_0/.../STAGES_EXPLAINED.md    ← Stage Completeness Rule    │   │
│  │ - layer_0/.../LAYERS_EXPLAINED.md                                  │   │
│  │                                                                     │   │
│  │ ## Protocol                                                         │   │
│  │ 1. Read references                                                  │   │
│  │ 2. Follow rules from knowledge docs                                │   │
│  │ 3. Execute task                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│       │ skill references knowledge                                         │
│       ▼                                                                     │
│  layer_0/.../STAGES_EXPLAINED.md (knowledge)                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ## Stage Completeness Rule                                          │   │
│  │ ALL 11 stages MUST exist. Empty is valid. Missing is NOT.          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  FLOW: Agent → CLAUDE.md → skills/ → SKILL.md → references → knowledge    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Principles

1. **CLAUDE.md is minimal** - Identity, critical rules, triggers, pointers only
2. **Skills contain protocols** - How to do specific tasks
3. **Skills reference knowledge** - Point to sub_layer docs, don't duplicate
4. **Knowledge is source of truth** - Rules and content live in sub_layers

---

## Proposal Requirement: Context Flow Diagrams

**[CRITICAL] All proposals that modify AI context architecture MUST include:**

1. **Propagation Chain Diagram** - How the change flows through the system
2. **Before Diagram** - Current state of context flow
3. **After Diagram** - Proposed state with changes highlighted
4. **Agent Workflow Diagram** - How agents will work with the change

**See**: `sub_layer_0_04_rules/AI_CONTEXT_PROPOSAL_REQUIREMENTS.md` for full template.

---

## [CRITICAL] Stage Completeness Rule

**ALL 11 stages MUST be created when an entity uses stages.**

```
entity_99_stages/
├── stage_XX_01_request_gathering/outputs/    ← REQUIRED
├── stage_XX_02_research/outputs/             ← REQUIRED
├── stage_XX_03_instructions/outputs/         ← REQUIRED
├── stage_XX_04_planning/outputs/             ← REQUIRED
├── stage_XX_05_design/outputs/               ← REQUIRED
├── stage_XX_06_development/outputs/          ← REQUIRED
├── stage_XX_07_testing/outputs/              ← REQUIRED
├── stage_XX_08_criticism/outputs/            ← REQUIRED
├── stage_XX_09_fixing/outputs/               ← REQUIRED
├── stage_XX_10_current_product/outputs/      ← REQUIRED
└── stage_XX_11_archives/outputs/             ← REQUIRED
```

**Empty stages are valid. Missing stages are NOT.**

**See**: `layer_stage_system/STAGES_EXPLAINED.md` for full details.

---

## Related Documentation

| Document | Location |
|----------|----------|
| **Stages explained** | `layer_stage_system/STAGES_EXPLAINED.md` |
| Sub-layers as entry points | `layer_stage_system/SUB_LAYERS_AS_ENTRY_POINTS.md` |
| Nested depth naming (subxN) | `layer_stage_system/NESTED_DEPTH_NAMING.md` |
| Sub-stages explained | `layer_stage_system/SUB_STAGES_EXPLAINED.md` |
| Layers explained | `layer_stage_system/LAYERS_EXPLAINED.md` |
| Proposal requirements | `../sub_layer_0_04_rules/AI_CONTEXT_PROPOSAL_REQUIREMENTS.md` |
| Hierarchy naming | `naming_conventions/HIERARCHY_NAMING_CONVENTION.md` |
| Skills index | `.claude/skills/SKILLS.md` |

---

*This architecture ensures AI agents always have context loaded through
the layer cascade, with CRITICAL RULES enforced on every API call,
and .0agnostic/ serving as the sync source for all tool-specific files.*
