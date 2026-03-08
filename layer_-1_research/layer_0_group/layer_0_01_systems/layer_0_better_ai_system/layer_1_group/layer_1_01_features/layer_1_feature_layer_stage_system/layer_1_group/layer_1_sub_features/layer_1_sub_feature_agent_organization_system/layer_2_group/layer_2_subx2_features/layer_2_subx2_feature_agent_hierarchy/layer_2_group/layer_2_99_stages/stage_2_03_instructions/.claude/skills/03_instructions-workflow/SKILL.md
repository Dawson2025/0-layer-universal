---
resource_id: "f06b0403-ae54-4409-8d4b-e8a81727d46f"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 03_instructions-workflow
description: Workflow skill for Document setup and usage instructions. Activated when working on 03_instructions tasks.
version: 1.0.0
---

# 03_instructions Workflow Skill

<!-- section_id: "0df9a3c9-9ea7-4208-a777-545da3484972" -->
## When to Use
- When entering the 03_instructions stage
- When performing 03_instructions activities
- When completing 03_instructions deliverables

<!-- section_id: "526b3836-96f2-428d-bf36-7d61e37cb506" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 03_instructions activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "108b9ee6-7f52-4e91-820a-d3a54b8d07d8" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "3fa309ae-07bf-4597-9824-5e86c8553861" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
