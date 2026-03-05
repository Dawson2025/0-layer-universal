---
resource_id: "cd9f6945-b07b-49cd-b0d0-08e9f0ae5832"
resource_type: "knowledge"
resource_name: "to_universal_pattern"
---
# To Universal Pattern

## Overview
Pattern for handing off from a specific layer to a universal (parent) layer.

## When to Use
- Reporting completion status up the hierarchy
- Escalating issues that require higher-level decisions
- Providing aggregated results from child operations
- Requesting guidance or clarification

## Pattern Structure

### Direction
`layer_N` -> `layer_N-1` (more universal)

### Location
`layer_N_01_manager_handoff_documents/layer_N_00_to_universal/`

### Template
```json
{
  "handoff_id": "uuid",
  "created": "ISO timestamp",
  "from": {
    "entity": "layer_N_feature_X",
    "stage": "current_stage"
  },
  "to": {
    "entity": "layer_N-1_parent",
    "stage": "awaiting_child_report"
  },
  "type": "layer",
  "payload": {
    "summary": "Report/Request from child layer",
    "status": "completed|blocked|in_progress",
    "results": {},
    "issues": [],
    "artifacts": [],
    "notes": ""
  }
}
```

## Best Practices

1. **Be Concise** - Parent layers need summaries, not details
2. **Include Status** - Always report current status
3. **Highlight Blockers** - Escalate issues early
4. **Reference Artifacts** - Point to detailed docs if needed
