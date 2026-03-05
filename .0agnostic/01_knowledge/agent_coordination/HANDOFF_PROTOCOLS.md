---
resource_id: "70e00d0c-3727-4a30-ab7c-2fdf5841b765"
resource_type: "knowledge"
resource_name: "HANDOFF_PROTOCOLS"
---
# Handoff Protocols for Agent Communication

<!-- section_id: "fa18ef66-7d29-49c0-8271-93f3d51ae7e0" -->
## Overview

When agents delegate to or receive work from other agents, they communicate via **handoff documents**. This document defines the protocols for effective agent-to-agent communication.

---

<!-- section_id: "c1ed2061-4cb5-44ef-aa8e-ba35884d1860" -->
## Handoff Document Locations

Every entry point (layer, stage, sub-layer, sub-stage) has handoff folders:

```
<entry_point>/
└── hand_off_documents/
    ├── incoming/
    │   ├── from_above/     ← Tasks from parent layers/stages
    │   └── from_below/     ← Results from child layers/stages
    └── outgoing/
        ├── to_above/       ← Results to parent layers/stages
        └── to_below/       ← Tasks to child layers/stages
```

---

<!-- section_id: "6ff417a2-8643-44f0-9dfe-1777a9391e97" -->
## Handoff Document Structure

<!-- section_id: "52197963-ea71-41bf-8127-5c0c226463f5" -->
### Task Handoff (Outgoing)

```markdown
# Task Handoff: [Brief Title]

## Metadata
- **From**: [Agent identity and entry point]
- **To**: [Target entry point]
- **Created**: [ISO timestamp]
- **Priority**: [low/medium/high/critical]
- **Type**: task

---

## Task Description

[Clear description of what needs to be done]

## Context

### Why This Task
[Brief explanation of why this work is needed]

### Relevant Background
[Any context the receiving agent needs]

### Related Files
| File | Purpose |
|------|---------|
| [path] | [why relevant] |

## Requirements

### Must Do
- [ ] [Required outcome 1]
- [ ] [Required outcome 2]

### Must Not Do
- [ ] [Constraint 1]
- [ ] [Constraint 2]

### Acceptance Criteria
- [ ] [How to know task is complete]

## Expected Output

### Deliverables
| Output | Location | Format |
|--------|----------|--------|
| [what] | [where] | [format] |

### Result Handoff
Return results to: `[path to incoming/from_below/]`

## Additional Notes

[Any other information]

---
*Handoff created by [agent] at [entry_point]*
```

<!-- section_id: "3476fe52-b977-46f5-954e-75313f23d1d0" -->
### Result Handoff (Returning)

```markdown
# Result Handoff: [Brief Title]

## Metadata
- **From**: [Agent identity and entry point]
- **To**: [Requesting agent entry point]
- **Created**: [ISO timestamp]
- **In Response To**: [Original task handoff filename]
- **Type**: result
- **Status**: [completed/partial/blocked/failed]

---

## Summary

[Brief summary of what was done]

## Deliverables

| Output | Location | Status |
|--------|----------|--------|
| [what] | [where] | [done/partial/pending] |

## Work Completed

### Actions Taken
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Decisions Made
| Decision | Rationale |
|----------|-----------|
| [decision] | [why] |

## Issues Encountered

### Resolved Issues
| Issue | Resolution |
|-------|------------|
| [issue] | [how resolved] |

### Unresolved Issues
| Issue | Recommendation |
|-------|----------------|
| [issue] | [suggested action] |

## Recommendations

[Any suggestions for the requesting agent]

## Verification

- [ ] All required outputs created
- [ ] Acceptance criteria met
- [ ] No blocking issues remain

---
*Result from [agent] at [entry_point]*
```

---

<!-- section_id: "35239e6f-0b4f-4ad9-9170-9800aa21aecf" -->
## Communication Patterns

<!-- section_id: "fd0b4ebf-5aa6-4406-b087-31fb3da77980" -->
### Pattern 1: Simple Delegation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIMPLE DELEGATION FLOW                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Parent Agent                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │ 1. Create task handoff document                                  │       │
│  │ 2. Place in: child/hand_off_documents/incoming/from_above/      │       │
│  │ 3. Spawn child agent at entry point                             │       │
│  │ 4. Wait for result or continue other work                       │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                          │                                                  │
│                          ▼                                                  │
│  Child Agent                                                                │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │ 1. Check: hand_off_documents/incoming/from_above/               │       │
│  │ 2. Read task handoff, understand requirements                   │       │
│  │ 3. Do the work                                                  │       │
│  │ 4. Create result handoff document                               │       │
│  │ 5. Place in: hand_off_documents/outgoing/to_above/              │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                          │                                                  │
│                          ▼                                                  │
│  Parent Agent                                                               │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │ 1. Check: hand_off_documents/incoming/from_below/               │       │
│  │ 2. Read result, integrate into own work                         │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "531526d7-9f0d-43cc-a4a5-e81d06047538" -->
### Pattern 2: Parallel Delegation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARALLEL DELEGATION FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Coordinating Agent                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │ 1. Create multiple task handoffs (Task A, Task B, Task C)       │       │
│  │ 2. Place each in respective entry point's incoming/from_above/  │       │
│  │ 3. Spawn agents at each entry point                             │       │
│  │ 4. Continue own work while waiting                              │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                   │          │          │                                   │
│                   ▼          ▼          ▼                                   │
│             ┌─────────┐ ┌─────────┐ ┌─────────┐                            │
│             │ Agent A │ │ Agent B │ │ Agent C │  (parallel execution)      │
│             └────┬────┘ └────┬────┘ └────┬────┘                            │
│                  │          │          │                                   │
│                  ▼          ▼          ▼                                   │
│             (Result A)  (Result B)  (Result C)                             │
│                   │          │          │                                   │
│                   └──────────┼──────────┘                                   │
│                              ▼                                              │
│  Coordinating Agent                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │ 1. Collect results from all hand_off_documents/incoming/        │       │
│  │ 2. Integrate results into unified output                        │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "c36d7362-980f-4355-add1-50326a8071ce" -->
### Pattern 3: Chain Delegation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHAIN DELEGATION FLOW                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Agent 1 ──task──▶ Agent 2 ──task──▶ Agent 3 ──task──▶ Agent 4            │
│     │                  │                  │                  │              │
│     │                  │                  │                  │              │
│     │◀──result────────│◀──result────────│◀──result────────│              │
│                                                                             │
│  Each agent:                                                                │
│  1. Receives task from previous agent                                       │
│  2. Does their part                                                         │
│  3. Passes task+progress to next agent OR returns result up the chain     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "8ac541fa-df95-487b-9ed5-18f900ca7ac4" -->
## Handoff Naming Convention

```
[type]_[timestamp]_[brief_description].md

Examples:
- task_2025-02-03T14-30-00_implement_auth_service.md
- result_2025-02-03T15-45-00_auth_service_complete.md
- escalation_2025-02-03T16-00-00_blocked_by_missing_deps.md
```

---

<!-- section_id: "54f92519-1e1f-49ec-93b8-18e7360d1ea5" -->
## Special Handoff Types

<!-- section_id: "912b3e4d-1736-4d6b-a27d-fc2d03fb23d5" -->
### Escalation Handoff

When an agent cannot complete a task:

```markdown
# Escalation Handoff: [Issue Title]

## Metadata
- **From**: [Agent identity and entry point]
- **To**: [Parent or coordinator entry point]
- **Created**: [ISO timestamp]
- **Type**: escalation
- **Severity**: [low/medium/high/critical]

---

## Issue Description

[What the problem is]

## What Was Attempted

1. [Attempt 1 and result]
2. [Attempt 2 and result]

## Why Escalating

[Why this agent cannot resolve it]

## Recommended Actions

1. [Suggested resolution 1]
2. [Suggested resolution 2]

## Partial Work Completed

| Work | Status | Location |
|------|--------|----------|
| [work] | [status] | [where] |

---
*Escalation from [agent] at [entry_point]*
```

<!-- section_id: "702d7540-7a5f-455a-86ce-0190264bdfdb" -->
### Progress Update Handoff

For long-running tasks:

```markdown
# Progress Update: [Task Title]

## Metadata
- **From**: [Agent identity]
- **Regarding**: [Original task handoff filename]
- **Created**: [ISO timestamp]
- **Type**: progress
- **Completion**: [X%]

---

## Status

[Brief current status]

## Completed So Far

- [x] [Completed item 1]
- [x] [Completed item 2]
- [ ] [In progress item]
- [ ] [Pending item]

## Estimated Remaining

[Time or effort estimate if possible]

## Issues

[Any issues encountered but resolved or being worked on]

---
*Progress update from [agent]*
```

---

<!-- section_id: "ec969810-8559-4038-8271-bd588dcde402" -->
## Handoff Best Practices

<!-- section_id: "2e58974c-f88a-4cb2-893b-8ca6ea7ade71" -->
### For Task Senders

1. **Be specific** - Vague tasks lead to wrong results
2. **Include context** - Don't assume the agent knows your situation
3. **Define acceptance criteria** - How will you know it's done?
4. **Specify constraints** - What should NOT be done?
5. **Name files clearly** - Use the naming convention

<!-- section_id: "4e0fff8c-ff71-4610-a6f9-a80afcbeb4a4" -->
### For Task Receivers

1. **Read completely** - Don't start until you understand
2. **Ask for clarification** - Via escalation handoff if needed
3. **Document decisions** - Explain choices in result handoff
4. **Report issues early** - Don't wait until the end
5. **Verify before returning** - Check acceptance criteria

<!-- section_id: "d572108c-ec8e-4beb-b2d3-73f76df3e2f9" -->
### For Coordinators

1. **Monitor progress** - Check for progress updates
2. **Handle escalations promptly** - Blocked agents waste resources
3. **Integrate results carefully** - Verify compatibility
4. **Clean up handoffs** - Archive completed handoffs

---

<!-- section_id: "df333f95-6471-4ea9-9376-8051b0db7265" -->
## Self-Check Before Sending Handoff

- [ ] Is the task clearly defined?
- [ ] Is all necessary context included?
- [ ] Are acceptance criteria specific?
- [ ] Is the return location specified?
- [ ] Does the filename follow convention?

---

*See SCOPE_VS_DELEGATION.md for when to delegate*
*See MULTI_AGENT_PATTERNS.md for coordination strategies*
