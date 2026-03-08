---
resource_id: "645b47bd-326e-4be6-8dd0-b512a950eccd"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

<!-- section_id: "e16ca99f-13dd-41ba-a1d0-af84a60406a1" -->
## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

<!-- section_id: "0091b7ce-fc8e-4eeb-b84b-1856a5213ba4" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "ece20b7f-129b-49bc-83d8-503e512355f1" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "39fc453b-3ddd-4eaa-b129-7a2fc28c3bb2" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
