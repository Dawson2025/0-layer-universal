---
resource_id: "8664bf46-095a-4dfd-942d-d40c5901db5d"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

<!-- section_id: "7f965a6a-cada-4832-97e0-f2e4a1a17f70" -->
## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

<!-- section_id: "6f152962-a4f1-4285-9a85-a7afc779e90d" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "84742790-9adf-4dfd-87c0-27b2a03cdf27" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "7fa288e2-c3d8-4d0e-8c10-50057b6b12c8" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
