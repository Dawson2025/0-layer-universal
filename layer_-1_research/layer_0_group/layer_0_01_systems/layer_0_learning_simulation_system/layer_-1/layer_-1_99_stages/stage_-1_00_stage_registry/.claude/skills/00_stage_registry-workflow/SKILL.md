---
resource_id: "ba31081e-3bf7-4ba4-923a-7000dadddea9"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

<!-- section_id: "0da62cc6-376e-43df-9108-fb9aeb86a990" -->
## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

<!-- section_id: "a450484d-864a-4cab-ab94-ee4afe2ba516" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "f8153d3e-4ee5-471b-a0dd-3425a8793b1f" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "a15f6a7e-16bf-49aa-b08d-226b11dc19fd" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
