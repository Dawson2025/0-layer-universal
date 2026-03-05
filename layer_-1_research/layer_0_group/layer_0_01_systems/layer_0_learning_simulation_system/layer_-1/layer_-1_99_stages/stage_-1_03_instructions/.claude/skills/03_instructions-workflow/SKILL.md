---
resource_id: "d3d98a0f-9ae5-480c-aeb8-a5100bc06ef8"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 03_instructions-workflow
description: Workflow skill for Document setup and usage instructions. Activated when working on 03_instructions tasks.
version: 1.0.0
---

# 03_instructions Workflow Skill

<!-- section_id: "8e3865a8-3d06-4d8b-99de-658ba43ebfd3" -->
## When to Use
- When entering the 03_instructions stage
- When performing 03_instructions activities
- When completing 03_instructions deliverables

<!-- section_id: "6a2ae9ba-8f71-4b62-a6c7-db4557bfe054" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 03_instructions activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "e00535a5-cb05-438c-bb20-048d977a01ae" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "51178eb4-7253-4d8f-94b9-3a146ab62547" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
