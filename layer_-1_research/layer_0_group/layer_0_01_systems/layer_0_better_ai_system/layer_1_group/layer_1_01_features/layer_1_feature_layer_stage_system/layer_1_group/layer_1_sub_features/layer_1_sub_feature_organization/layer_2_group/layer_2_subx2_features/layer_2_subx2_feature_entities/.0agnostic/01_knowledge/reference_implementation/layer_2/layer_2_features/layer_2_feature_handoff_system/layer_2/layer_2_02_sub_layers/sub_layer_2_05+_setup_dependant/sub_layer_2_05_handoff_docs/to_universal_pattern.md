---
resource_id: "cd9f6945-b07b-49cd-b0d0-08e9f0ae5832"
resource_type: "knowledge"
resource_name: "to_universal_pattern"
---
# To Universal Pattern

<!-- section_id: "ef351c07-5fbc-4766-b72f-75a5ef903451" -->
## Overview
Pattern for handing off from a specific layer to a universal (parent) layer.

<!-- section_id: "5a9d524e-0429-48de-95fb-d6763fe030d3" -->
## When to Use
- Reporting completion status up the hierarchy
- Escalating issues that require higher-level decisions
- Providing aggregated results from child operations
- Requesting guidance or clarification

<!-- section_id: "cf75f3f3-09b4-4c01-b336-c6225665c054" -->
## Pattern Structure

<!-- section_id: "221d5b1c-8b5d-4af1-9351-0760d5e26a33" -->
### Direction
`layer_N` -> `layer_N-1` (more universal)

<!-- section_id: "6245bf83-7d49-4edd-80c8-6b75b76d614d" -->
### Location
`layer_N_01_manager_handoff_documents/layer_N_00_to_universal/`

<!-- section_id: "2ca5d93b-19e7-4163-80f1-864f91b4eb96" -->
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

<!-- section_id: "d2fa081e-c2d1-42d6-863b-15e68788fa92" -->
## Best Practices

1. **Be Concise** - Parent layers need summaries, not details
2. **Include Status** - Always report current status
3. **Highlight Blockers** - Escalate issues early
4. **Reference Artifacts** - Point to detailed docs if needed
