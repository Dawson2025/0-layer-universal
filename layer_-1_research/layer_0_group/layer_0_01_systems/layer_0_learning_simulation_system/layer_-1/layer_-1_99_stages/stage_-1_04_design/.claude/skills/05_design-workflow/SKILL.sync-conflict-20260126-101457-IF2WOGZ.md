---
resource_id: "a98280da-ed8c-48ed-a7fc-d383418370fc"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101457-IF2WOGZ"
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
