# To Specific Pattern

## Overview
Pattern for handing off from a universal (parent) layer to a specific (child) layer.

## When to Use
- Delegating tasks to specialized child layers
- Providing instructions for implementation
- Passing context and requirements down
- Initiating new work streams

## Pattern Structure

### Direction
`layer_N` -> `layer_N+1` (more specific)

### Location
`layer_N_01_manager_handoff_documents/layer_N_01_to_specific/`

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

## Best Practices

1. **Clear Objectives** - State what success looks like
2. **Provide Context** - Include relevant background
3. **Set Constraints** - Define boundaries and limitations
4. **List Tasks** - Break down into actionable items
5. **Include References** - Point to relevant docs and examples
