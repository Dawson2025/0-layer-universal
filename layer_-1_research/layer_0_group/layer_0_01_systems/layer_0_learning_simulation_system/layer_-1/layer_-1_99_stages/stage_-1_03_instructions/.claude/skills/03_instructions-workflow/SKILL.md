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

## When to Use
- When entering the 03_instructions stage
- When performing 03_instructions activities
- When completing 03_instructions deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 03_instructions activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
