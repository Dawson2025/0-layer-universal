---
resource_id: "71e35587-71b9-4cc6-b158-c1fa78c51c37"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 05_design-workflow
description: Workflow skill for Technical design and architecture. Activated when working on 05_design tasks.
version: 1.0.0
---

# 05_design Workflow Skill

## When to Use
- When entering the 05_design stage
- When performing 05_design activities
- When completing 05_design deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 05_design activities
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
