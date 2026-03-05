---
resource_id: "1143b78c-44af-46a4-a4b6-55d0f566705c"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: handoff-protocol
description: How to communicate via handoff documents
---

# Handoff Protocol Skill

## Purpose

This skill defines how agents communicate via handoff documents in the layer-stage system.

## When to Use

- Delegating work to a child
- Escalating to a parent
- Completing a task with results
- Reporting status or blockers

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

## Handoff Types

### Delegation (to child)
- Write to: `[child]/hand_off_documents/incoming/from_above/`
- Include: Clear task, context, acceptance criteria
- Expect: Result in `incoming/from_below/`

### Escalation (to parent)
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: What was attempted, why escalating, recommended action
- Expect: Response or new delegation

### Completion (to parent)
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: What was done, artifacts produced, any issues
- Type: completion

### Status Update
- Write to: `hand_off_documents/outgoing/to_above/`
- Include: Current progress, blockers, ETA
- Type: status

## Best Practices

1. **Be Specific**: Include exact paths to artifacts
2. **Provide Context**: Don't assume receiver knows background
3. **Clear Criteria**: Define what "done" looks like
4. **Track Status**: Update status field as work progresses
5. **One Task Per Handoff**: Don't bundle unrelated work
