---
resource_id: "548bad0b-397e-4bc9-aaf9-70027915cad7"
resource_type: "knowledge"
resource_name: "HANDOFF_PROTOCOLS"
---
# Handoff Protocols for Agent Communication

<!-- section_id: "5a906ef1-f5ee-432e-983f-436963fcd50a" -->
## Overview

When agents delegate to or receive work from other agents, they communicate via **handoff documents**. This document defines the protocols for effective agent-to-agent communication.

---

<!-- section_id: "e2557084-210a-463b-8d73-a76f3ea0b7db" -->
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

<!-- section_id: "46492c8c-872b-4890-b748-150359c1bfbe" -->
## Handoff Document Structure

<!-- section_id: "53ebdb3b-d65e-4dfa-9f7e-8455688715a3" -->
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

<!-- section_id: "d327504b-667e-4232-8f63-67cb5cacc773" -->
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

<!-- section_id: "f2299067-4341-4f78-98ef-1016fd811d8c" -->
## Communication Patterns

<!-- section_id: "7cf61028-9b17-499c-bea9-dfa077dbe695" -->
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

<!-- section_id: "c49b1391-94cb-4b81-9fc0-6338711b396e" -->
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

<!-- section_id: "ab95ca11-010c-47e9-bda5-cd394427e815" -->
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

<!-- section_id: "39fccb8f-b5fc-423b-86f7-065159c317af" -->
## Handoff Naming Convention

```
[type]_[timestamp]_[brief_description].md

Examples:
- task_2025-02-03T14-30-00_implement_auth_service.md
- result_2025-02-03T15-45-00_auth_service_complete.md
- escalation_2025-02-03T16-00-00_blocked_by_missing_deps.md
```

---

<!-- section_id: "ee828dfa-cd20-455a-b30a-f8da27f5e3c7" -->
## Special Handoff Types

<!-- section_id: "bf81dccf-d4b7-47e6-b866-f42122bd26f2" -->
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

<!-- section_id: "e5f5c77e-8cfa-46d1-baf3-eb761fb55106" -->
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

<!-- section_id: "f6022373-fbc9-45f4-bc26-845c0f741209" -->
## Handoff Best Practices

<!-- section_id: "1b624379-de24-4673-95da-e886c9c7a2ed" -->
### For Task Senders

1. **Be specific** - Vague tasks lead to wrong results
2. **Include context** - Don't assume the agent knows your situation
3. **Define acceptance criteria** - How will you know it's done?
4. **Specify constraints** - What should NOT be done?
5. **Name files clearly** - Use the naming convention

<!-- section_id: "cf61a356-711c-411e-97d2-7183cd996ba1" -->
### For Task Receivers

1. **Read completely** - Don't start until you understand
2. **Ask for clarification** - Via escalation handoff if needed
3. **Document decisions** - Explain choices in result handoff
4. **Report issues early** - Don't wait until the end
5. **Verify before returning** - Check acceptance criteria

<!-- section_id: "f19ad416-3214-46ae-9fc8-9cf8d718d00c" -->
### For Coordinators

1. **Monitor progress** - Check for progress updates
2. **Handle escalations promptly** - Blocked agents waste resources
3. **Integrate results carefully** - Verify compatibility
4. **Clean up handoffs** - Archive completed handoffs

---

<!-- section_id: "b0bcec54-8deb-4275-9327-a371c4f50284" -->
## Self-Check Before Sending Handoff

- [ ] Is the task clearly defined?
- [ ] Is all necessary context included?
- [ ] Are acceptance criteria specific?
- [ ] Is the return location specified?
- [ ] Does the filename follow convention?

---

*See SCOPE_VS_DELEGATION.md for when to delegate*
*See MULTI_AGENT_PATTERNS.md for coordination strategies*
