---
resource_id: "2ebe27d8-8332-4084-a8f1-69c718037ca6"
resource_type: "document"
resource_name: "task_source_identification"
---
# Task Source Identification

<!-- section_id: "1bcfacaf-bb28-4c06-ba05-e5ea1258a9aa" -->
## Priority Order (Highest to Lowest)

1. **Current User Request** - What the user just asked
2. **status.json in_progress** - Tasks marked as in_progress
3. **Handoff Documents** - Context from previous sessions
4. **Todo Lists** - Backlog items

<!-- section_id: "81ce9c7a-6864-4aab-8736-2e5e174a3e3e" -->
## Source Details

<!-- section_id: "7dea40be-34bd-453c-b5f3-e10b619b6af0" -->
### 1. Current User Request (Priority: HIGHEST)
- Direct instruction from user in current message
- Always takes precedence over stored tasks
- May override or supersede other sources

**Identification**:
- Latest user message in conversation
- Explicit instructions or questions

<!-- section_id: "0cfb2e1b-e78d-48d5-b2d2-f869ca693201" -->
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

<!-- section_id: "ddabf47c-a34e-4719-bf5c-35091a6674a6" -->
### 3. Handoff Documents (Priority: MEDIUM)
- Created when sessions end mid-task
- Contains context about incomplete work
- Helps maintain continuity

**Identification**:
- Files named `handoff.md` or similar
- Located in entity's documentation
- Contains session context and next steps

<!-- section_id: "1dd4aa93-c4e7-42aa-9476-35e16df41ed5" -->
### 4. Todo Lists (Priority: LOWEST)
- Backlog of potential work
- Not yet committed to
- May be outdated

**Identification**:
- Files named `TODO.md`, `todo.txt`
- Sections marked as backlog
- Items without status markers

<!-- section_id: "f04585b7-3900-4f99-8144-449b044c7af6" -->
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

<!-- section_id: "8eb05642-2a37-4544-9bde-bebb7319a51d" -->
## Conflict Resolution

When multiple sources suggest different tasks:

| Conflict | Resolution |
|----------|------------|
| User vs status.json | User wins |
| User vs handoff | User wins |
| status.json vs handoff | status.json wins |
| status.json vs todo | status.json wins |

<!-- section_id: "879ead6a-6372-4824-9b7e-9d73a03266be" -->
## Best Practices

1. **Always check user request first** - Don't assume stored tasks are current
2. **Validate status.json** - May be stale if sessions crashed
3. **Review handoff context** - Contains valuable session info
4. **Treat todos as suggestions** - Not committed work

<!-- section_id: "94df4595-7a69-42b7-988b-124ceda042a2" -->
## Updating Task Sources

After identifying task:
1. If from user: Add to status.json as in_progress
2. If completing: Move to completed in status.json
3. If blocked: Move to blocked with reason
4. If abandoning: Remove or move to todo
