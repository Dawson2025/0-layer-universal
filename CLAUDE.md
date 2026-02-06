# 0_layer_universal

## Role

**Root Manager** - Coordinates all layers in the system.

## Responsibilities

- Receive user requests via `hand_off_documents/incoming/from_above/`
- Delegate tasks to appropriate layers (layer_0, layer_1, layer_-1_research)
- Aggregate results from layers via `hand_off_documents/incoming/from_below/`
- Report final results to user via `hand_off_documents/outgoing/to_above/`
- Handle escalations from any descendant

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for user requests
2. Check `hand_off_documents/incoming/from_below/` for layer results/escalations
3. Process pending work or await user input

## Children

| Layer | Purpose | Scope |
|-------|---------|-------|
| `layer_0/` | Universal | Rules, prompts, knowledge, principles (applies to ALL) |
| `layer_1/` | Projects | Projects, features, components |
| `layer_-1_research/` | Research | Research projects, experiments |

---

## Universal Rules (ALWAYS FOLLOW)

### AI Context Modification Protocol

Before modifying AI context files (CLAUDE.md, .claude/, rules, prompts, knowledge):

1. **Show diagram** of proposed changes (full paths, before/after)
2. **Wait for user approval** - do not proceed until confirmed
3. **Execute approved changes** - follow diagram exactly

**Scope**: `CLAUDE.md`, `.claude/`, `*_rules/`, `*_prompts/`, `*_knowledge/`, `status.json`

### AI Context Commit/Push Rule

After approved AI context changes:

1. `git add [specific files]` - stage changed files
2. `git commit -m "[AI Context] description"` - descriptive message
3. `git push` - sync to remote

### Safety Governance (Key Principles)

1. **Least Privilege**: Operate with minimum permissions needed
2. **Defense in Depth**: Multiple protection layers
3. **Human Oversight**: Critical decisions require approval
4. **Fail Secure**: When in doubt, deny and escalate
5. **Audit Everything**: Log actions for review

**Full rules**: `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/`

### [CRITICAL] File Path Linking Rule

When creating or updating files, ALWAYS include the full clickable file path in the response.

**Format**: `**File**: /full/path/to/file.md`

**Full rules**: `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/FILE_PATH_LINKING_RULE.md`

---

## Detailed Rules Reference

For complete rule documentation, read from:

```
layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/
├── AI_CONTEXT_MODIFICATION_PROTOCOL.md   ← Full modification protocol
├── AI_CONTEXT_COMMIT_PUSH_RULE.md        ← Full commit/push rule
├── safety_governance.md                   ← Full security governance
├── LAYER_CONTEXT_HEADER_PROTOCOL.md      ← File header requirements
└── FILE_PATH_LINKING_RULE.md             ← [CRITICAL] Always include file paths
```

## Primary AI System

**AALang** (`sub_layer_0_01_ai_system/`) is the primary AI system used throughout the entire layer-stage framework:

- It is **how agents work** at every level
- It applies to **all layers** (0, 1, -1, etc.)
- It applies to **all stages** (01-11)
- It applies to **all sub_layers and sub_stages**

When working anywhere in this system, AALang provides the underlying AI capabilities and patterns.

**Location**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/`

---

## Navigation: How to Find Things

### Sub-Layers (layer_0/layer_0_03_sub_layers/)

| Sub-Layer | Purpose | When to Read |
|-----------|---------|--------------|
| `sub_layer_0_01_ai_system/` | **PRIMARY AI SYSTEM** - AALang (submodule) | AI language design - used for most everything |
| `sub_layer_0_02_knowledge_system/` | Domain knowledge | When context needed |
| `sub_layer_0_03_principles/` | Guiding principles | Design decisions |
| `sub_layer_0_04_rules/` | **Universal rules** | **ALWAYS** |
| `sub_layer_0_05_protocols/` | Init protocols, session start | Start of session |
| `sub_layer_0_06+_setup_dependant_hierarchy/` | OS/tool setup | Environment issues |

### Stages (layer_N/layer_N_99_stages/)

| Stage | Purpose |
|-------|---------|
| 01_request_gathering | Clarify requirements |
| 02_research | Explore, gather info |
| 03_instructions | Define constraints |
| 04_planning | Break into subtasks |
| 05_design | Architecture |
| 06_development | Implementation |
| 07_testing | Verification |
| 08_criticism | Review |
| 09_fixing | Corrections |
| 10_current_product | Deliverable |
| 11_archives | History |

### Quick Lookup

| Need | Location |
|------|----------|
| AALang AI System | `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/` |
| Universal init protocol | `layer_0/layer_0_03_sub_layers/sub_layer_0_05_protocols/universal_init_prompt.md` |
| All rules | `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| Git rules | `sub_layer_0_04_rules/0_instruction_docs/git_commit_rule.md` |
| Terminal protocol | `sub_layer_0_04_rules/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` |
| Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` |
| Research projects | `layer_-1_research/` |

## Structure Overview

```
0_layer_universal/
├── CLAUDE.md                 ← You are here (Root Manager)
├── .claude/                  ← Tool permissions, settings
├── hand_off_documents/       ← Four-directional communication
│   ├── incoming/from_above/  ← User requests
│   ├── incoming/from_below/  ← Layer results
│   ├── outgoing/to_above/    ← Results to user
│   └── outgoing/to_below/    ← Tasks to layers
├── layer_0/                  ← Universal (applies to ALL)
│   ├── layer_0_03_sub_layers/
│   │   ├── sub_layer_0_01_ai_system/    ← AALang (submodule)
│   │   ├── sub_layer_0_02_knowledge/    ← Domain knowledge
│   │   ├── sub_layer_0_03_principles/   ← Principles
│   │   ├── sub_layer_0_04_rules/        ← RULES (read first!)
│   │   ├── sub_layer_0_05_protocols/    ← Session init protocols
│   │   └── sub_layer_0_06+_setup/       ← OS/tool config
│   └── layer_0_99_stages/    ← Universal stages
├── layer_1/                  ← Projects, features
└── layer_-1_research/        ← Research projects
```

## Session Workflow

1. **Sync**: `git pull && git status`
2. **Read rules**: `sub_layer_0_04_rules/` (especially modification protocol)
3. **Read init protocol**: `sub_layer_0_05_protocols/universal_init_prompt.md`
4. **Identify context**: What layer? What stage?
5. **Do work**: Follow stage guidelines
6. **Commit/push**: Per AI_CONTEXT_COMMIT_PUSH_RULE.md

## Conventions

- **Naming**: Use underscores: `layer_0_01_name`, `stage_0_02_name`
- **Layers**: Lower numbers = more universal (Layer 0 applies to all)
- **Stages**: 01-11, workflow phases
- **Sub-layers**: 01-06+, content types (ai_system, knowledge, principles, rules, protocols, setup)
