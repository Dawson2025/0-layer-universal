---
resource_id: "d3d02935-4d14-4851-8efc-6347f1a4c03b"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

<!-- section_id: "bd0a1978-7521-4b74-9671-c61a4d8f73b7" -->
## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

<!-- section_id: "55357f4e-64c4-4177-8201-6308bcbf9e3c" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "ef3158e6-4e9f-414a-830b-34f4bba5b70a" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "e6676ed3-3fc3-47b8-a9b4-90be66e8e803" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
