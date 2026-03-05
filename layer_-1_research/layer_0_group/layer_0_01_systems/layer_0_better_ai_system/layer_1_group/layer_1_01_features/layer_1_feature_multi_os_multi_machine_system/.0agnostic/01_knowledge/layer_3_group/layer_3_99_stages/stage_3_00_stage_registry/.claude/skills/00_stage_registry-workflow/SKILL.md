---
resource_id: "4a72a175-d0f8-4207-b04b-43724c76e644"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

<!-- section_id: "5c1be7ec-fc88-4d14-b4b3-4ac6cb61d0e6" -->
## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

<!-- section_id: "dc771d4d-9760-4536-89dc-dc258a184aa1" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "6543a185-9ddc-46b9-8d8d-3325a45ae95b" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "bcc9c606-78c8-4d53-925b-fd1c446770e5" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
