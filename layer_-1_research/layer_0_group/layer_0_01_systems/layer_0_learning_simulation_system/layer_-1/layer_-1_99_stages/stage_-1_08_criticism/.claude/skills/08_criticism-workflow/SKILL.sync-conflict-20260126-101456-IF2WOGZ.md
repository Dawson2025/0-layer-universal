---
resource_id: "43b6e9dc-5d14-43c4-846a-d3599a0219e8"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
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
