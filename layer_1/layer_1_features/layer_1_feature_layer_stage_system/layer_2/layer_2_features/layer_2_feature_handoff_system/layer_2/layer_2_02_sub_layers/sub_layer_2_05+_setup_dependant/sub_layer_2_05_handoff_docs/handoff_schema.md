---
resource_id: "2721176e-2858-438e-876f-1ad17d27875f"
resource_type: "document"
resource_name: "handoff_schema"
---
# Handoff Schema

<!-- section_id: "e8170627-3681-4adc-bf72-08a10ebddd14" -->
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

<!-- section_id: "b5e8dfb8-6bba-4a9d-bac0-7f93645a5bef" -->
## Required Fields
- handoff_id
- created
- from (entity)
- to (entity)
- type
- payload.summary

<!-- section_id: "89265557-843a-4e8b-b1f2-27865f384c5f" -->
## Field Descriptions

<!-- section_id: "4d642a3f-d1cc-4c2e-93fa-7f7f50d203a2" -->
### handoff_id
Unique identifier for the handoff. Use UUID v4 format.

<!-- section_id: "2c08dbe6-061b-4f93-9c64-061d01feea4d" -->
### created
ISO 8601 timestamp when the handoff was created.

<!-- section_id: "c30e27bb-f5c5-42b5-ae02-b35516e264a7" -->
### from
Object containing source information:
- `entity`: Full path to the source entity
- `stage`: Current stage name (optional for layer handoffs)

<!-- section_id: "8febb070-2766-45eb-b57d-cd9571c84aa8" -->
### to
Object containing target information:
- `entity`: Full path to the target entity
- `stage`: Target stage name (optional for layer handoffs)

<!-- section_id: "9a98eaf6-3c94-4e56-af2b-94c4b06c33ea" -->
### type
Either "stage" or "layer":
- `stage`: Transition between stages within same entity
- `layer`: Transition between different layer levels

<!-- section_id: "19fa8861-73d9-4b26-b01a-cef662a10d88" -->
### payload
Contains the handoff contents:
- `summary`: Brief description of what is being handed off
- `tasks`: Array of tasks to be completed
- `blockers`: Array of blocking issues (empty if none)
- `artifacts`: Array of file paths for related documents
- `notes`: Additional context or instructions
