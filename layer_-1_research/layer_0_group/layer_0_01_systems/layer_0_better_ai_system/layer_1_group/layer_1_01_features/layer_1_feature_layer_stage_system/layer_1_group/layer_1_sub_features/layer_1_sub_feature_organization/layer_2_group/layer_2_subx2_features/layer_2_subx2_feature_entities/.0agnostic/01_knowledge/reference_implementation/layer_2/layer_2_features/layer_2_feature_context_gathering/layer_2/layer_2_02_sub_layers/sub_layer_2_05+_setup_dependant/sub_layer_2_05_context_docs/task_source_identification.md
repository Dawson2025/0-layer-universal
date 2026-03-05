---
resource_id: "ba357d1f-311e-4f33-883c-cd195fbca6e9"
resource_type: "knowledge"
resource_name: "task_source_identification"
---
# Task Source Identification

<!-- section_id: "b78f9c58-cafe-43fa-86f5-451c2cd50cc1" -->
## Priority Order (Highest to Lowest)

1. **Current User Request** - What the user just asked
2. **status.json in_progress** - Tasks marked as in_progress
3. **Handoff Documents** - Context from previous sessions
4. **Todo Lists** - Backlog items

<!-- section_id: "f8a198c2-2148-4c98-b107-1a88fce93a3a" -->
## Source Details

<!-- section_id: "2f95f2b5-8a64-4da5-9f8f-0283083c92e0" -->
### 1. Current User Request (Priority: HIGHEST)
- Direct instruction from user in current message
- Always takes precedence over stored tasks
- May override or supersede other sources

**Identification**:
- Latest user message in conversation
- Explicit instructions or questions

<!-- section_id: "2b5639aa-f7c6-4a76-975b-af1ca6d60567" -->
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

<!-- section_id: "1305184e-b33d-4d05-af41-792fe5bbd485" -->
### 3. Handoff Documents (Priority: MEDIUM)
- Created when sessions end mid-task
- Contains context about incomplete work
- Helps maintain continuity

**Identification**:
- Files named `handoff.md` or similar
- Located in entity's documentation
- Contains session context and next steps

<!-- section_id: "0aaaaf1a-1565-4563-9095-16e32d744c5e" -->
### 4. Todo Lists (Priority: LOWEST)
- Backlog of potential work
- Not yet committed to
- May be outdated

**Identification**:
- Files named `TODO.md`, `todo.txt`
- Sections marked as backlog
- Items without status markers

<!-- section_id: "09cdbbb9-c886-41ce-a2a4-4b885d8b3200" -->
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

<!-- section_id: "748a9c1c-f881-4282-b8f8-19235fc37bd3" -->
## Conflict Resolution

When multiple sources suggest different tasks:

| Conflict | Resolution |
|----------|------------|
| User vs status.json | User wins |
| User vs handoff | User wins |
| status.json vs handoff | status.json wins |
| status.json vs todo | status.json wins |

<!-- section_id: "62f734ca-374e-4edb-9a1a-9051a5a10a84" -->
## Best Practices

1. **Always check user request first** - Don't assume stored tasks are current
2. **Validate status.json** - May be stale if sessions crashed
3. **Review handoff context** - Contains valuable session info
4. **Treat todos as suggestions** - Not committed work

<!-- section_id: "10b45a69-f704-4cbd-af89-ed8ea34e0770" -->
## Updating Task Sources

After identifying task:
1. If from user: Add to status.json as in_progress
2. If completing: Move to completed in status.json
3. If blocked: Move to blocked with reason
4. If abandoning: Remove or move to todo
