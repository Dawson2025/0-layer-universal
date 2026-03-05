---
resource_id: "e2788326-68d5-4351-a861-705e99a4f04f"
resource_type: "knowledge"
resource_name: "to_specific_pattern"
---
# To Specific Pattern

<!-- section_id: "ad02db2a-75b5-42fa-8ac7-84d07c293627" -->
## Overview
Pattern for handing off from a universal (parent) layer to a specific (child) layer.

<!-- section_id: "a72270f3-d43d-4437-9117-7cf9461d9bcc" -->
## When to Use
- Delegating tasks to specialized child layers
- Providing instructions for implementation
- Passing context and requirements down
- Initiating new work streams

<!-- section_id: "e7de3724-ec86-43b4-b893-88399de78e8f" -->
## Pattern Structure

<!-- section_id: "0386256a-0bce-487a-b778-90e0d3888a3f" -->
### Direction
`layer_N` -> `layer_N+1` (more specific)

<!-- section_id: "c83c1cca-e4bd-4cfd-9082-9d1b4eae952e" -->
### Location
`layer_N_01_manager_handoff_documents/layer_N_01_to_specific/`

<!-- section_id: "53894c94-8e26-46be-8f39-4310207c5140" -->
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

<!-- section_id: "73c54864-9d82-41e0-8733-5d3ec892574d" -->
## Best Practices

1. **Clear Objectives** - State what success looks like
2. **Provide Context** - Include relevant background
3. **Set Constraints** - Define boundaries and limitations
4. **List Tasks** - Break down into actionable items
5. **Include References** - Point to relevant docs and examples
