# Task Source Identification

## Priority Order (Highest to Lowest)

1. **Current User Request** - What the user just asked
2. **status.json in_progress** - Tasks marked as in_progress
3. **Handoff Documents** - Context from previous sessions
4. **Todo Lists** - Backlog items

## Source Details

### 1. Current User Request (Priority: HIGHEST)
- Direct instruction from user in current message
- Always takes precedence over stored tasks
- May override or supersede other sources

**Identification**:
- Latest user message in conversation
- Explicit instructions or questions

### 2. status.json in_progress (Priority: HIGH)
- Tasks with `"status": "in_progress"`
- Represents active, committed work
- Should be completed before new work

**Identification**:
```json
{
  "current_stage": 2,
  "tasks": {
    "in_progress": ["task description"],
    "completed": [],
    "blocked": []
  }
}
```

### 3. Handoff Documents (Priority: MEDIUM)
- Created when sessions end mid-task
- Contains context about incomplete work
- Helps maintain continuity

**Identification**:
- Files named `handoff.md` or similar
- Located in entity's documentation
- Contains session context and next steps

### 4. Todo Lists (Priority: LOWEST)
- Backlog of potential work
- Not yet committed to
- May be outdated

**Identification**:
- Files named `TODO.md`, `todo.txt`
- Sections marked as backlog
- Items without status markers

## Resolution Strategy

```
identify_current_task():
    # Check sources in priority order

    if user_request exists:
        return user_request

    if status.in_progress not empty:
        return status.in_progress[0]

    if handoff_document exists:
        return handoff_document.next_steps

    if todo_list exists:
        return todo_list.first_item

    return ask_user_for_task
```

## Conflict Resolution

When multiple sources suggest different tasks:

| Conflict | Resolution |
|----------|------------|
| User vs status.json | User wins |
| User vs handoff | User wins |
| status.json vs handoff | status.json wins |
| status.json vs todo | status.json wins |

## Best Practices

1. **Always check user request first** - Don't assume stored tasks are current
2. **Validate status.json** - May be stale if sessions crashed
3. **Review handoff context** - Contains valuable session info
4. **Treat todos as suggestions** - Not committed work

## Updating Task Sources

After identifying task:
1. If from user: Add to status.json as in_progress
2. If completing: Move to completed in status.json
3. If blocked: Move to blocked with reason
4. If abandoning: Remove or move to todo
