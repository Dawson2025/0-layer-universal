---
resource_id: "f72da99d-1e42-4cf8-9ecd-559e79f22455"
resource_type: "document"
resource_name: "to_universal_pattern"
---
# To Universal Pattern

<!-- section_id: "47af9592-e777-4ff7-9f94-663729ff680b" -->
## Overview
Pattern for handing off from a specific layer to a universal (parent) layer.

<!-- section_id: "c09af382-8d69-4f8e-b17e-3ab0ce754d5e" -->
## When to Use
- Reporting completion status up the hierarchy
- Escalating issues that require higher-level decisions
- Providing aggregated results from child operations
- Requesting guidance or clarification

<!-- section_id: "3f1fd8f8-7dc9-4e1e-b688-5329535759da" -->
## Pattern Structure

<!-- section_id: "c67d96db-d4bf-414c-ba69-0feda61b01a3" -->
### Direction
`layer_N` -> `layer_N-1` (more universal)

<!-- section_id: "ee2f25df-5ceb-454b-a1b7-08ef42526f47" -->
### Location
`layer_N_01_manager_handoff_documents/layer_N_00_to_universal/`

<!-- section_id: "c0ea1143-e8f4-4632-a089-3c1f87343762" -->
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

<!-- section_id: "fe231f5e-56aa-480c-978f-298223001d77" -->
## Best Practices

1. **Be Concise** - Parent layers need summaries, not details
2. **Include Status** - Always report current status
3. **Highlight Blockers** - Escalate issues early
4. **Reference Artifacts** - Point to detailed docs if needed
