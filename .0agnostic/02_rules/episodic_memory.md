---
resource_id: "5bc9cf52-76aa-4b51-ad9f-ed9d2f3b7b0f"
resource_type: "rule"
resource_name: "episodic_memory"
---
# Episodic Memory Rules

<!-- section_id: "7d5f49fc-3dee-4148-800f-029f2f3ddd1e" -->
## Rule: Record Significant Work

After completing significant work, create a session record:

```
.0agnostic/episodic_memory/sessions/YYYY-MM-DD_session_NNN.md
```

<!-- section_id: "44c13bab-9d8c-4351-9575-4e864220e717" -->
## Session File Structure

```markdown
# Session YYYY-MM-DD_NNN

**Date**: YYYY-MM-DD
**Duration**: X minutes/hours
**Agent**: [agent identifier]
**Status**: COMPLETED | IN_PROGRESS | BLOCKED

## Summary
[1-2 sentence summary of what was done]

## Objectives
- [x] Objective 1
- [x] Objective 2
- [ ] Objective 3 (incomplete)

## Files Created/Modified
- path/to/file1.md
- path/to/file2.md

## Key Decisions
- Decision 1: [rationale]
- Decision 2: [rationale]

## Next Steps
- What should happen next
- Any blockers or dependencies

## Notes
[Any relevant observations or context]
```

<!-- section_id: "4fe79b37-7c69-42b5-bb46-8d191ecb8fc8" -->
## Change Tracking

When modifying outputs, update divergence.log:

```
YYYY-MM-DDTHH:MM:SSZ | agent_id | path | ACTION | before_hash → after_hash
```

Actions: CREATED, MODIFIED, DELETED

<!-- section_id: "88902606-d98e-4072-951b-3b12d3195bfe" -->
## Why Episodic Memory

- **Prevents amnesia**: Next session knows what happened
- **Enables continuity**: Work continues seamlessly
- **Creates audit trail**: All changes tracked
- **Supports multi-agent**: Agents understand each other's work

