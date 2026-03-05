---
resource_id: "aafe9cb7-50da-4fde-93db-08bb67ee420b"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035811-IF2WOGZ"
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
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
