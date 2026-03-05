---
resource_id: "3e41bda7-bebe-49a8-b2ab-2f3036d089d4"
resource_type: "knowledge"
resource_name: "handoff_schema"
---
# Handoff Schema

## JSON Schema
```json
{
  "handoff_id": "uuid",
  "created": "ISO timestamp",
  "from": {
    "entity": "path to source entity",
    "stage": "current stage"
  },
  "to": {
    "entity": "path to target entity",
    "stage": "target stage"
  },
  "type": "stage|layer",
  "payload": {
    "summary": "Brief description",
    "tasks": ["Task 1", "Task 2"],
    "blockers": [],
    "artifacts": ["file1.md", "file2.md"],
    "notes": "Additional context"
  }
}
```

## Required Fields
- handoff_id
- created
- from (entity)
- to (entity)
- type
- payload.summary

## Field Descriptions

### handoff_id
Unique identifier for the handoff. Use UUID v4 format.

### created
ISO 8601 timestamp when the handoff was created.

### from
Object containing source information:
- `entity`: Full path to the source entity
- `stage`: Current stage name (optional for layer handoffs)

### to
Object containing target information:
- `entity`: Full path to the target entity
- `stage`: Target stage name (optional for layer handoffs)

### type
Either "stage" or "layer":
- `stage`: Transition between stages within same entity
- `layer`: Transition between different layer levels

### payload
Contains the handoff contents:
- `summary`: Brief description of what is being handed off
- `tasks`: Array of tasks to be completed
- `blockers`: Array of blocking issues (empty if none)
- `artifacts`: Array of file paths for related documents
- `notes`: Additional context or instructions
