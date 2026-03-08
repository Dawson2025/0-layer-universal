---
resource_id: "ff18f19e-ea46-4e48-9b84-5d74ab2ef5ca"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 10_current_product-workflow
description: Workflow skill for Production-ready artifacts. Activated when working on 10_current_product tasks.
version: 1.0.0
---

# 10_current_product Workflow Skill

<!-- section_id: "8038cb87-aced-4de0-a839-78655d3fe174" -->
## When to Use
- When entering the 10_current_product stage
- When performing 10_current_product activities
- When completing 10_current_product deliverables

<!-- section_id: "9f361145-3915-4733-9ab3-b316ce91b79e" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 10_current_product activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "56d45c5c-bd63-4a32-ba0e-0b595be57897" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "671a75d4-4070-4ff5-89a3-955feb6d1e22" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
