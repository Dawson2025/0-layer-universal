---
resource_id: "bdc38836-b777-4687-88dc-7b741eee3e53"
resource_type: "document"
resource_name: "to_specific_pattern"
---
# To Specific Pattern

<!-- section_id: "7cfd0262-40a5-4d83-af47-5fd95d3f9351" -->
## Overview
Pattern for handing off from a universal (parent) layer to a specific (child) layer.

<!-- section_id: "af4049b3-a68f-4f33-974a-bb5556949e2c" -->
## When to Use
- Delegating tasks to specialized child layers
- Providing instructions for implementation
- Passing context and requirements down
- Initiating new work streams

<!-- section_id: "2299d5c9-fec4-4fb9-8837-e75f4e3bf996" -->
## Pattern Structure

<!-- section_id: "d6e62b26-f409-43ad-89d5-edacd6b323e4" -->
### Direction
`layer_N` -> `layer_N+1` (more specific)

<!-- section_id: "0815c89d-c497-46dc-abf6-c597766c98ef" -->
### Location
`layer_N_01_manager_handoff_documents/layer_N_01_to_specific/`

<!-- section_id: "7b0666af-09f3-4a19-ad52-50137f9ab1b8" -->
### Template
```json
{
  "handoff_id": "uuid",
  "created": "ISO timestamp",
  "from": {
    "entity": "layer_N_parent",
    "stage": "delegating"
  },
  "to": {
    "entity": "layer_N+1_feature_X",
    "stage": "00_request"
  },
  "type": "layer",
  "payload": {
    "summary": "Task assignment to child layer",
    "objective": "What needs to be accomplished",
    "constraints": [],
    "context": {},
    "tasks": [],
    "artifacts": [],
    "deadline": "ISO timestamp (optional)",
    "notes": ""
  }
}
```

<!-- section_id: "2a39a89d-fb52-402f-bee8-b6f29633b368" -->
## Best Practices

1. **Clear Objectives** - State what success looks like
2. **Provide Context** - Include relevant background
3. **Set Constraints** - Define boundaries and limitations
4. **List Tasks** - Break down into actionable items
5. **Include References** - Point to relevant docs and examples
