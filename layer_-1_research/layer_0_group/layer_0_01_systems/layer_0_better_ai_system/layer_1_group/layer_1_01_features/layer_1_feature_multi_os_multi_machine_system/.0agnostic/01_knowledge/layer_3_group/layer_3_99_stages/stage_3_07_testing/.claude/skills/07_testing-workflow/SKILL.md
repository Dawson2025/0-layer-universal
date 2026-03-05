---
resource_id: "01256d85-f2f8-4a74-a42c-9df024993962"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on 07_testing tasks.
version: 1.0.0
---

# 07_testing Workflow Skill

<!-- section_id: "c68183fc-d9cd-436d-8c33-6828052087cb" -->
## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

<!-- section_id: "258f915b-4512-4e2f-81ce-a270df2879af" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "8343db8f-20d1-4ecb-9446-e138d8965a6d" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "b1423282-9ff5-490b-8c8f-0cbb650ea80a" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
