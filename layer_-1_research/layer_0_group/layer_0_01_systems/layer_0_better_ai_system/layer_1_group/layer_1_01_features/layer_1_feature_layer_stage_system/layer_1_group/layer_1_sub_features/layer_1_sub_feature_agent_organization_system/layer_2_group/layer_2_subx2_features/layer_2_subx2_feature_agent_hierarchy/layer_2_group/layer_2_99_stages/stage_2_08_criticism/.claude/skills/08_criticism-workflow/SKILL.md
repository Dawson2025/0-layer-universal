---
resource_id: "69113340-57cf-43db-8aee-0e5ae9487168"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

<!-- section_id: "68388ab0-80e7-496d-98c5-92c09ed5c86b" -->
## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

<!-- section_id: "cfa8edc5-9a86-4b7d-9cd7-aa7fea82d64f" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "2d1f74eb-8fc9-4ec6-a28f-a594ec1f41c3" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "7cc5e691-7133-4c59-b55f-c52b25970554" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
