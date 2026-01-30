---
name: handoff-protocol
description: How to communicate via handoff documents at this stage
---

# Handoff Protocol Skill

## Purpose

This skill defines how this research stage communicates via handoff documents.

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

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Status
**Current**: [pending | in_progress | blocked | complete]
```

## This Stage's Handoffs

### Incoming (from Stage Manager)
- Location: `hand_off_documents/incoming/from_above/`
- Contains: Research tasks, needs to investigate

### Outgoing (to Stage Manager)
- Location: `hand_off_documents/outgoing/to_above/`
- Contains: Research completion, escalations

## When to Write Outgoing Handoff

1. **Research Complete**: All needs researched, ready for Stage 03
2. **Blocked**: Cannot proceed, need guidance
3. **Status Update**: Progress report on long research

## Handoff Completion Template

```markdown
# Handoff: Research Complete - [Topic]

**From**: stage_-1_02_research
**To**: stage_-1_99_stages (Stages Manager)
**Date**: YYYY-MM-DD
**Type**: completion

---

## Task
Research on [topic] complete.

## Artifacts
| Artifact | Location | Description |
|----------|----------|-------------|
| Options Analysis | outputs/by_need/[need]/options_analysis.md | All options compared |
| Recommendation | outputs/by_need/[need]/recommended_approach.md | Selected approach |
| Sketch | outputs/by_need/[need]/implementation_sketch.md | High-level design |

## Status
**Current**: complete
**Ready for**: Stage 03 (Instructions)
```
