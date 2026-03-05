---
resource_id: "8664bf46-095a-4dfd-942d-d40c5901db5d"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
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
