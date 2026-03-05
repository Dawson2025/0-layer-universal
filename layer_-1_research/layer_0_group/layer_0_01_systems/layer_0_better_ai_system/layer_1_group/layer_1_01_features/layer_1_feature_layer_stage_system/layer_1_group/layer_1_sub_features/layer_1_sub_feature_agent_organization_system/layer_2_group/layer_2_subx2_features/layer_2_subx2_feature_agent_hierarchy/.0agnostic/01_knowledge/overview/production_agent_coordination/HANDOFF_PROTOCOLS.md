---
resource_id: "548bad0b-397e-4bc9-aaf9-70027915cad7"
resource_type: "knowledge"
resource_name: "HANDOFF_PROTOCOLS"
---
# Handoff Protocols for Agent Communication

## Overview

When agents delegate to or receive work from other agents, they communicate via **handoff documents**. This document defines the protocols for effective agent-to-agent communication.

---

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

## Handoff Document Structure

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

## Communication Patterns

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

## Handoff Naming Convention

```
[type]_[timestamp]_[brief_description].md

Examples:
- task_2025-02-03T14-30-00_implement_auth_service.md
- result_2025-02-03T15-45-00_auth_service_complete.md
- escalation_2025-02-03T16-00-00_blocked_by_missing_deps.md
```

---

## Special Handoff Types

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

## Handoff Best Practices

### For Task Senders

1. **Be specific** - Vague tasks lead to wrong results
2. **Include context** - Don't assume the agent knows your situation
3. **Define acceptance criteria** - How will you know it's done?
4. **Specify constraints** - What should NOT be done?
5. **Name files clearly** - Use the naming convention

### For Task Receivers

1. **Read completely** - Don't start until you understand
2. **Ask for clarification** - Via escalation handoff if needed
3. **Document decisions** - Explain choices in result handoff
4. **Report issues early** - Don't wait until the end
5. **Verify before returning** - Check acceptance criteria

### For Coordinators

1. **Monitor progress** - Check for progress updates
2. **Handle escalations promptly** - Blocked agents waste resources
3. **Integrate results carefully** - Verify compatibility
4. **Clean up handoffs** - Archive completed handoffs

---

## Self-Check Before Sending Handoff

- [ ] Is the task clearly defined?
- [ ] Is all necessary context included?
- [ ] Are acceptance criteria specific?
- [ ] Is the return location specified?
- [ ] Does the filename follow convention?

---

*See SCOPE_VS_DELEGATION.md for when to delegate*
*See MULTI_AGENT_PATTERNS.md for coordination strategies*
