# System Prompt Architecture - Implementation Instructions

**Status**: APPROVED - Ready for design/planning
**Date**: 2026-01-26
**Approved**: 2026-01-26
**Based On**: `stage_-1_02_research/outputs/02_finished_understanding/by_topic/system_prompt_architecture.md`
**Related Needs**: rule_compliant, persistent_knowledge, discoverable
**Next Step**: Create design in `stage_-1_04_design/` and plan in `stage_-1_05_planning/`

---

## Overview

These instructions define how to implement the container-as-manager pattern, four-directional handoff system, and agent hierarchy across the entire `0_layer_universal/` codebase.

---

## Instruction 1: Rename 00 Managers to Registries

**Scope**: All `*_00_stage_manager/` and `*_00_layer_manager/` folders

**Action**: Rename to `*_00_registry/` (data only)

**Steps**:
1. For each `stage_X_00_stage_manager/`:
   - Move CLAUDE.md content UP to parent `layer_X_99_stages/CLAUDE.md`
   - Move `.claude/` content UP to parent `layer_X_99_stages/.claude/`
   - Rename folder to `stage_X_00_registry/`
   - Keep only data files (registry.yaml, etc.)

2. For each `layer_X_00_layer_manager/`:
   - Move CLAUDE.md content UP to parent layer's CLAUDE.md
   - Rename folder to `layer_X_00_layer_registry/`
   - Keep only data files

**Verification**:
- [ ] No folders named `*_manager` at position 00
- [ ] All 00 folders contain only data files
- [ ] Parent containers have the manager content

---

## Instruction 2: Create Manager Structure at Containers

**Scope**: Every layer, stages container, sub_layers container

**Action**: Ensure each container has manager structure

**Required structure**:
```
container/
├── CLAUDE.md                 # Manager rules
├── .claude/
│   ├── settings.json
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   └── skills/
└── hand_off_documents/
    ├── incoming/
    │   ├── from_above/
    │   └── from_below/
    └── outgoing/
        ├── to_above/
        └── to_below/
```

**Apply to**:
- [ ] `0_layer_universal/`
- [ ] `layer_0/`
- [ ] `layer_1/`
- [ ] `layer_-1_research/`
- [ ] Every `layer_X_99_stages/`
- [ ] Every `layer_X_03_sub_layers/`
- [ ] Every individual stage folder
- [ ] Every individual sub_layer folder

---

## Instruction 3: Standardize CLAUDE.md Content

**Scope**: All CLAUDE.md files

**Template for Collection Managers** (stages, sub_layers):
```markdown
# [container_name]

## Role
[Collection] Manager for [what it manages]

## Responsibilities
- Create/remove/reorder children
- Delegate tasks to appropriate child
- Aggregate results from children
- Handle escalations from descendants

## On Session Start
1. Check hand_off_documents/incoming/from_above/ for tasks
2. Check hand_off_documents/incoming/from_below/ for results/escalations
3. Process or await user input

## Children
| Name | Purpose |
|------|---------|
| ... | ... |

## Navigation
- Parent: [path]
- Registry: [00_registry path]
```

**Template for Entity Managers** (individual stage, sub_layer):
```markdown
# [entity_name]

## Role
[Entity] Manager for [purpose]

## Responsibilities
- Execute work within this scope
- Produce outputs in outputs/
- Report results to parent
- Escalate issues beyond scope

## On Session Start
1. Check hand_off_documents/incoming/from_above/ for tasks
2. Execute or delegate to workers
3. Write results to hand_off_documents/outgoing/to_above/

## Outputs
- [what this entity produces]

## Navigation
- Parent: [path]
```

---

## Instruction 4: Update Root CLAUDE.md with Universal Rules

**Scope**: `0_layer_universal/CLAUDE.md`

**Action**: Embed universal rules directly (not just reference them)

**Rules to embed**:
1. AI Context Modification Protocol (summary + diagram)
2. AI Context Commit/Push Rule (summary)
3. Safety governance (key constraints)
4. Layer Context Header Protocol (brief)

**Format**:
```markdown
## Universal Rules (ALWAYS FOLLOW)

### AI Context Modification Protocol
Before modifying CLAUDE.md, .claude/, rules, prompts, knowledge:
1. Show proposed change diagram
2. Wait for user approval
3. Only then make changes

### AI Context Commit/Push Rule
After approved AI context changes:
1. git add [specific files]
2. git commit -m "descriptive message"
3. git push

### [Additional rules...]
```

**Keep reference to canonical source**:
```markdown
## Detailed Rules
For full rule documentation: `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/`
```

---

## Instruction 5: Implement Handoff Document Protocol

**Scope**: All managers

**Handoff document format**:
```markdown
# [DATE]_[brief_description].md

## Metadata
- From: [source manager path]
- To: [target manager path]
- Date: YYYY-MM-DD
- Type: task | result | escalation

## Task/Result/Escalation
[Description of what's being handed off]

## Context
[Relevant background]

## Expected Output (for tasks)
[What the receiver should produce]

## Actual Output (for results)
[What was produced, where it is]

## Next Steps
[What should happen next]
```

**Flow rules**:
1. Downward delegation: Write to child's `incoming/from_above/`
2. Upward results: Write to own `outgoing/to_above/`
3. Skip-level escalation: Write directly to ancestor's `incoming/from_below/`

---

## Instruction 6: Configure .claude/settings.json

**Scope**: All managers

**Standard format**:
```json
{
  "context": {
    "type": "collection_manager | entity_manager",
    "name": "[manager name]",
    "layer": N,
    "purpose": "[brief purpose]"
  },
  "permissions": {
    "allow": [],
    "deny": [],
    "ask": []
  }
}
```

---

## Instruction 7: Create Standard Skills

**Scope**: Collection managers

**Stages Manager skill** (`.claude/skills/stages-workflow/SKILL.md`):
```markdown
---
name: stages-workflow
description: Manage stage collection
---

## Operations
- Add stage
- Remove stage
- Reorder stages
- Check stage status
```

**Sub_layers Manager skill** (`.claude/skills/sublayers-workflow/SKILL.md`):
```markdown
---
name: sublayers-workflow
description: Manage sub_layer collection
---

## Operations
- Add sub_layer
- Remove sub_layer
- Update sub_layer registry
```

---

## Execution Order

1. **Phase 1**: Rename 00 managers to registries (Instruction 1)
2. **Phase 2**: Create manager structure at all containers (Instruction 2)
3. **Phase 3**: Standardize CLAUDE.md files (Instruction 3)
4. **Phase 4**: Update root CLAUDE.md with embedded rules (Instruction 4)
5. **Phase 5**: Implement handoff protocol (Instruction 5)
6. **Phase 6**: Configure settings.json files (Instruction 6)
7. **Phase 7**: Create standard skills (Instruction 7)

---

## Verification Checklist

After implementation:

- [ ] All 00 positions are registries (data only)
- [ ] All containers have CLAUDE.md with manager role
- [ ] All containers have .claude/ folder
- [ ] All containers have hand_off_documents/ with 4 subdirs
- [ ] Root CLAUDE.md contains embedded universal rules
- [ ] Can demonstrate: delegation flows down, results flow up
- [ ] Can demonstrate: skip-level escalation works

---

## Open Items

1. Which existing projects/features to migrate first?
2. Should migration be incremental or all-at-once?
3. Testing strategy for verifying agent communication?
