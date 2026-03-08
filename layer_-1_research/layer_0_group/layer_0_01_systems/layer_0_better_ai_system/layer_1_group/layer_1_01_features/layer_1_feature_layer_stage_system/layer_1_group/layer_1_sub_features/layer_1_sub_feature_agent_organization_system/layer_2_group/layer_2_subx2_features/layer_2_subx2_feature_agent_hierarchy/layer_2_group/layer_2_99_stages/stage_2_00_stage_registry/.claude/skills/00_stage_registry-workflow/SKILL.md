---
resource_id: "7b9324fe-5b4f-4d80-874d-60f68476e425"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

<!-- section_id: "c189103f-589f-46cf-b36b-ac9e84e75863" -->
## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

<!-- section_id: "58cb73e9-ed02-4cf5-9c9d-cb1448b2f92d" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "9a025eb9-c66a-4cbd-ab01-1d60527a7fca" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "9560eeb2-71db-4e50-905c-eb28c3e6344c" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
