# Episodic Memory Rules

## Rule: Record Significant Work

After completing significant work, create a session record:

```
.0agnostic/episodic_memory/sessions/YYYY-MM-DD_session_NNN.md
```

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

## Change Tracking

When modifying outputs, update divergence.log:

```
YYYY-MM-DDTHH:MM:SSZ | agent_id | path | ACTION | before_hash → after_hash
```

Actions: CREATED, MODIFIED, DELETED

## Why Episodic Memory

- **Prevents amnesia**: Next session knows what happened
- **Enables continuity**: Work continues seamlessly
- **Creates audit trail**: All changes tracked
- **Supports multi-agent**: Agents understand each other's work

