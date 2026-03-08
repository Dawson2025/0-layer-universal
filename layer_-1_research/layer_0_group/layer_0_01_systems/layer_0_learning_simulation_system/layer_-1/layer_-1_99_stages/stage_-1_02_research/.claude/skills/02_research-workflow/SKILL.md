---
resource_id: "dd567943-a87b-4e02-af73-ecb460f9dcc1"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

<!-- section_id: "50c8f1e2-13b9-4e1d-a1dd-a928803b97b0" -->
## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

<!-- section_id: "1b8e9300-8c04-4c8a-a800-3494de78f4cf" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "8ac89ed2-2c9e-4221-9e3f-23f85cfb75ff" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "9f7db4ad-4103-4f7d-acb4-673b302f6a46" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
