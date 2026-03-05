---
resource_id: "1ff9c38b-6f9b-4c3e-9460-4d8346648456"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on 09_fixing tasks.
version: 1.0.0
---

# 09_fixing Workflow Skill

## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
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
