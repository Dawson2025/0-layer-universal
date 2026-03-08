---
resource_id: "1143b78c-44af-46a4-a4b6-55d0f566705c"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: handoff-protocol
description: How to communicate via handoff documents
---

# Handoff Protocol Skill

<!-- section_id: "37e5aa6f-e796-41e8-a7dd-94d0f542bdc0" -->
## Purpose

This skill defines how agents communicate via handoff documents in the layer-stage system.

<!-- section_id: "419f685d-6da8-4afe-b387-8fcf645d3bd5" -->
## When to Use

- Delegating work to a child
- Escalating to a parent
- Completing a task with results
- Reporting status or blockers

<!-- section_id: "74ab9b71-b22c-465c-82e9-20188660614c" -->
## Handoff Schema

```markdown
# Handoff: [Task Name]

**From**: [Source location]
**To**: [Target location]
**Date**: YYYY-MM-DD
**Type**: [delegation | escalation | completion | status]

---

## Task

[Clear description of what needs to be done]

## Context

[Relevant background, constraints, decisions made]

## Artifacts

| Artifact | Location | Description |
|----------|----------|-------------|
| [name] | [path] | [what it is] |

## Acceptance Criteria

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Status

**Current**: [pending | in_progress | blocked | complete]
**Blockers**: [If any]
**Notes**: [Additional context]
```

<!-- section_id: "3e78d337-95ae-4a28-8fd6-5aaf42454e89" -->
## Directory Structure

```
hand_off_documents/
├── incoming/
│   ├── from_above/    # Tasks from parent
│   └── from_below/    # Results from children
└── outgoing/
    ├── to_above/      # Escalations/completions to parent
    └── to_below/      # Delegations to children
```

<!-- section_id: "eb3fae99-6b6a-4ebf-a1a2-d2b8abf1c6e7" -->
## Handoff Types

<!-- section_id: "b673220c-8853-4918-8bec-a1c789fa93e5" -->
### Delegation (to child)
- Write to: `[child]/hand_off_documents/incoming/from_above/`
- Include: Clear task, context, acceptance criteria
- Expect: Result in `incoming/from_below/`

<!-- section_id: "951caa61-e84c-4dc8-91b7-f0b12a802774" -->
### Escalation (to parent)
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: What was attempted, why escalating, recommended action
- Expect: Response or new delegation

<!-- section_id: "c04ef647-dbae-41f3-a07c-f559bf846cfb" -->
### Completion (to parent)
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: What was done, artifacts produced, any issues
- Type: completion

<!-- section_id: "dd6830d0-8f72-413d-a2d3-16b1ca793828" -->
### Status Update
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: Current progress, blockers, ETA
- Type: status

<!-- section_id: "6525c7e3-7ad8-4936-8a6a-f88eeb108190" -->
## Best Practices

1. **Be Specific**: Include exact paths to artifacts
2. **Provide Context**: Don't assume receiver knows background
3. **Clear Criteria**: Define what "done" looks like
4. **Track Status**: Update status field as work progresses
5. **One Task Per Handoff**: Don't bundle unrelated work
