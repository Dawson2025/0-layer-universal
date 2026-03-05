---
resource_id: "3e41bda7-bebe-49a8-b2ab-2f3036d089d4"
resource_type: "knowledge"
resource_name: "handoff_schema"
---
# Handoff Schema

<!-- section_id: "09427294-7947-410e-8bbd-863031bd13f7" -->
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

<!-- section_id: "09215590-c4f9-4415-ab80-6310e4907de6" -->
## Required Fields
- handoff_id
- created
- from (entity)
- to (entity)
- type
- payload.summary

<!-- section_id: "c95bb99c-fdb4-4f4e-b7f3-0037727ed0a8" -->
## Field Descriptions

<!-- section_id: "95a37819-c2b5-4e06-a0fb-47b2ec0cfdd8" -->
### handoff_id
Unique identifier for the handoff. Use UUID v4 format.

<!-- section_id: "29063a2f-2f59-4025-a9ba-fc4f8c218ffb" -->
### created
ISO 8601 timestamp when the handoff was created.

<!-- section_id: "bec4df6d-eb12-4980-ab6e-2f9f2bbaaf45" -->
### from
Object containing source information:
- `entity`: Full path to the source entity
- `stage`: Current stage name (optional for layer handoffs)

<!-- section_id: "c48bcb2f-503f-401f-860b-286ab8e393a2" -->
### to
Object containing target information:
- `entity`: Full path to the target entity
- `stage`: Target stage name (optional for layer handoffs)

<!-- section_id: "65befa37-8205-4303-8f6f-21de0b79329e" -->
### type
Either "stage" or "layer":
- `stage`: Transition between stages within same entity
- `layer`: Transition between different layer levels

<!-- section_id: "b40f1f7d-cc64-4cd3-811d-e7c159077e3c" -->
### payload
Contains the handoff contents:
- `summary`: Brief description of what is being handed off
- `tasks`: Array of tasks to be completed
- `blockers`: Array of blocking issues (empty if none)
- `artifacts`: Array of file paths for related documents
- `notes`: Additional context or instructions
