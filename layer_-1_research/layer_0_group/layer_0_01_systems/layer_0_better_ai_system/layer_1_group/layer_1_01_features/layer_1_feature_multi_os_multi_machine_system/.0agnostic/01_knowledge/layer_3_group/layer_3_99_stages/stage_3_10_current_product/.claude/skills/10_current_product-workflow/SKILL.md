---
resource_id: "a5eb457f-f150-4a7e-af7e-50ae2aa332a0"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 10_current_product-workflow
description: Workflow skill for Production-ready artifacts. Activated when working on 10_current_product tasks.
version: 1.0.0
---

# 10_current_product Workflow Skill

<!-- section_id: "4ec4befe-d4f8-4df0-a041-6da6ee89f864" -->
## When to Use
- When entering the 10_current_product stage
- When performing 10_current_product activities
- When completing 10_current_product deliverables

<!-- section_id: "69e41b1c-3b79-42f1-9574-8bacfb90865c" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 10_current_product activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "42f825f4-7088-4fc9-9088-cec7d399b7e1" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "db841139-21d0-474e-9f6c-d1728556c3da" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
