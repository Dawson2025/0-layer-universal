---
resource_id: "43b6e9dc-5d14-43c4-846a-d3599a0219e8"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

<!-- section_id: "e7ba2161-9b8a-4d05-a6fd-5f2ea2dfa284" -->
## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

<!-- section_id: "ecf1e975-15ee-4a2b-8ccc-80da93ea66e1" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "b2c767e1-9a26-4c09-9a53-4ac068ec89ca" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "6f7d5f84-683e-4ea7-8dd4-50a739964cb6" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
