---
resource_id: "d7e73f14-e183-4a46-815c-0f8bc51f08cc"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

<!-- section_id: "efb7eccf-7f9e-4c2e-9bfe-e13e4e2936ec" -->
## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

<!-- section_id: "34f42af9-c2d0-487d-8f19-4ffa6f4807f1" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "d47692a0-f9db-4d28-a39f-a6785c6be061" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "813f605f-94d2-4cda-ac85-d7cb53c1bc94" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
