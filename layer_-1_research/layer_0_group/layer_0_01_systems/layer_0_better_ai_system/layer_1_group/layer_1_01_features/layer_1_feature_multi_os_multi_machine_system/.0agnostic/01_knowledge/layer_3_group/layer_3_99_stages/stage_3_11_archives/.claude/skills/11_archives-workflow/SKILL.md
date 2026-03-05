---
resource_id: "49408ef4-3378-46a2-8e63-53bfaf91061f"
resource_type: "skill
knowledge"
resource_name: "SKILL"
---
---
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
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
