---
resource_id: "aafe9cb7-50da-4fde-93db-08bb67ee420b"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035811-IF2WOGZ"
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

<!-- section_id: "7c5bac9c-682f-4eb6-b8cd-69dad37e8b00" -->
## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

<!-- section_id: "f5d9dd06-c547-4d83-a503-44686bc7244b" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "2137bf48-477e-49f6-8ca5-6618ae4c1055" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "8e147241-abee-4585-9b6b-3d0927d0e779" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
