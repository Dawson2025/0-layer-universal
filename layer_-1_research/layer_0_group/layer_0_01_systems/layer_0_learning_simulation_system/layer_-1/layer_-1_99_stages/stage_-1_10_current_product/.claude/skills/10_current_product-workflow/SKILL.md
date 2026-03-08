---
resource_id: "6d9fcda7-b205-4cc0-91ef-cade879937e1"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 10_current_product-workflow
description: Workflow skill for Production-ready artifacts. Activated when working on 10_current_product tasks.
version: 1.0.0
---

# 10_current_product Workflow Skill

<!-- section_id: "c09a0cee-6ea5-47f9-9ead-e8d757e7ff17" -->
## When to Use
- When entering the 10_current_product stage
- When performing 10_current_product activities
- When completing 10_current_product deliverables

<!-- section_id: "bcda73fe-8680-41ab-ac66-ba4ebb892e34" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 10_current_product activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "a14014d6-46f7-48ff-a9c2-e1df98cc75d7" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "59734803-88d1-48e4-85c1-51534079cf69" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
