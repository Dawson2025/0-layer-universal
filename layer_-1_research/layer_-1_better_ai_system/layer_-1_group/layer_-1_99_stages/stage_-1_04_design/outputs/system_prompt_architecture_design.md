# System Prompt Architecture - Design

**Status**: Draft
**Date**: 2026-01-26
**Based On**: `stage_-1_03_instructions/outputs/02_finished_instructions/by_topic/system_prompt_architecture_instructions.md`

---

## Design Overview

This design implements the container-as-manager pattern across `0_layer_universal/`, enabling hierarchical agent coordination with four-directional handoff communication.

---

## Architecture Diagram

```
0_layer_universal/                              [ROOT MANAGER]
├── CLAUDE.md                                   ← Universal rules embedded
├── .claude/
├── hand_off_documents/
│   ├── incoming/from_above/                    ← User requests
│   ├── incoming/from_below/                    ← Results from all layers
│   ├── outgoing/to_above/                      ← Results to user
│   └── outgoing/to_below/                      ← Tasks to layers
│
├── layer_0_group/                                    [LAYER MANAGER - Universal]
│   ├── CLAUDE.md
│   ├── .claude/
│   ├── hand_off_documents/{4-dir}/
│   ├── layer_0_00_layer_registry/              ← Data only
│   ├── layer_0_03_sub_layers/                  [SUB_LAYERS MANAGER]
│   │   ├── CLAUDE.md
│   │   ├── hand_off_documents/{4-dir}/
│   │   ├── sub_layer_0_00_registry/            ← Data only
│   │   └── sub_layer_0_XX_*/                   [SUB_LAYER MANAGERS]
│   └── layer_0_99_stages/                      [STAGES MANAGER]
│       ├── CLAUDE.md
│       ├── hand_off_documents/{4-dir}/
│       ├── stage_0_00_registry/                ← Data only
│       └── stage_0_XX_*/                       [STAGE MANAGERS]
│
├── layer_1/                                    [LAYERS MANAGER - Projects]
│   ├── CLAUDE.md
│   ├── hand_off_documents/{4-dir}/
│   └── layer_1_projects/
│       └── layer_1_project_*/                  [LAYER MANAGERS]
│
└── layer_-1_research/                          [LAYERS MANAGER - Research]
    ├── CLAUDE.md
    ├── hand_off_documents/{4-dir}/
    └── layer_-1_*/                             [LAYER MANAGERS]
```

---

## Component Designs

### 1. Manager CLAUDE.md Template

```markdown
# [container_name]

## Role
[Collection|Entity] Manager for [scope]

## Responsibilities
- [List based on manager type]

## On Session Start
1. Check hand_off_documents/incoming/from_above/
2. Check hand_off_documents/incoming/from_below/
3. Process or await input

## Children (for collection managers)
| Name | Purpose |
|------|---------|

## Outputs (for entity managers)
- [What this produces]
```

### 2. Handoff Document Structure

```
hand_off_documents/
├── incoming/
│   ├── from_above/           # Tasks from parent
│   │   └── YYYYMMDD_task_description.md
│   └── from_below/           # Results/escalations from children
│       └── YYYYMMDD_result_description.md
└── outgoing/
    ├── to_above/             # Results to parent
    │   └── YYYYMMDD_result_description.md
    └── to_below/             # Tasks to children
        └── YYYYMMDD_task_description.md
```

### 3. Handoff Document Format

```markdown
# YYYYMMDD_brief_description

## Metadata
| Field | Value |
|-------|-------|
| From | [source path] |
| To | [target path] |
| Date | YYYY-MM-DD |
| Type | task / result / escalation |

## Content
[Description]

## Context
[Background]

## Expected Output (tasks)
[What receiver should produce]

## Actual Output (results)
[What was produced]

## Next Steps
[What happens next]
```

### 4. Registry Data Structure

```yaml
# stage_0_00_registry/stages.yaml
stages:
  - number: "01"
    name: request_gathering
    purpose: Collect and clarify requirements
  - number: "02"
    name: research
    purpose: Explore problem space
  # ...
```

### 5. .claude/settings.json Structure

```json
{
  "context": {
    "type": "collection_manager",
    "name": "layer_0_99_stages",
    "layer": 0,
    "purpose": "Manage workflow stages"
  },
  "permissions": {
    "allow": [],
    "deny": [],
    "ask": []
  }
}
```

---

## Communication Flow Design

### Downward Delegation

```
Parent Manager
    │
    ├─1─► Writes task to: child/hand_off_documents/incoming/from_above/
    │
    └─2─► Spawns child agent (Task tool)
              │
              └─3─► Child reads from: incoming/from_above/
                    │
                    └─4─► Child executes or further delegates
```

### Upward Results

```
Child Manager completes work
    │
    ├─1─► Writes to own: outgoing/to_above/
    │
    └─2─► Terminates (returns to parent)
              │
              └─3─► Parent reads from: incoming/from_below/
                    │
                    └─4─► Parent aggregates, continues or reports up
```

### Skip-Level Escalation

```
Grandchild discovers layer-wide issue
    │
    └─1─► Writes DIRECTLY to: grandparent/hand_off_documents/incoming/from_below/
              │
              └─2─► Grandparent sees escalation
                    │
                    └─3─► Grandparent handles or coordinates fix
```

---

## Migration Design

### Phase 1: Registry Conversion
```
BEFORE                          AFTER
stage_0_00_stage_manager/  →    stage_0_00_registry/
├── CLAUDE.md              →    (move to parent)
├── .claude/               →    (move to parent)
└── registry.yaml          →    └── stages.yaml (keep)
```

### Phase 2: Container Enhancement
```
BEFORE                          AFTER
layer_0_99_stages/              layer_0_99_stages/
└── (stages only)               ├── CLAUDE.md (from 00)
                                ├── .claude/ (from 00)
                                ├── hand_off_documents/
                                │   ├── incoming/from_above/
                                │   ├── incoming/from_below/
                                │   ├── outgoing/to_above/
                                │   └── outgoing/to_below/
                                ├── stage_0_00_registry/
                                └── stage_0_XX_*/
```

---

## Root CLAUDE.md Design

The root `0_layer_universal/CLAUDE.md` will contain:

```markdown
# 0_layer_universal

## Role
Root Manager - coordinates all layers

## Universal Rules (ALWAYS FOLLOW)

### AI Context Modification Protocol
Before modifying AI context files (CLAUDE.md, .claude/, rules, prompts):
1. Show proposed changes
2. Wait for explicit user approval
3. Only then execute changes

**Scope**: CLAUDE.md, .claude/, *_rules/, *_prompts/, *_knowledge/

### AI Context Commit/Push Rule
After approved AI context changes:
1. Stage specific files (not git add -A)
2. Commit with descriptive message
3. Push to remote

### [Other universal rules...]

## Navigation
[Quick lookup table]

## On Session Start
1. Check hand_off_documents/incoming/from_above/ (user requests)
2. Check hand_off_documents/incoming/from_below/ (layer results)
3. Process or await input
```

---

## Verification Design

### Test Case 1: Simple Delegation
1. Start at root
2. Issue task: "Add a principle"
3. Verify: handoff flows root → layer_0 → sub_layers → principles
4. Verify: result flows back up

### Test Case 2: Skip-Level Escalation
1. Start at stage level
2. Discover issue affecting all stages
3. Write directly to layer's incoming/from_below/
4. Verify: layer manager receives escalation

### Test Case 3: Multi-Level Aggregation
1. Issue task requiring work in multiple stages
2. Verify: stages manager coordinates
3. Verify: results aggregated correctly

---

## Open Design Decisions

1. **Naming**: Use `registry` or `_registry`? (Proposed: without underscore)
2. **Empty handoff folders**: Include .gitkeep or README.md?
3. **Handoff cleanup**: Archive old handoffs or delete after processing?
