---
resource_id: "6c6f95b4-2b17-4480-8074-a13a4da869c2"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

<!-- section_id: "7d46f2c6-abf2-4d3d-b8fe-ac690a7703a0" -->
## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

<!-- section_id: "b86e77ed-11ac-4b17-9988-33d0edb91a6e" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "81884acc-1b20-4d67-aaf8-ce67c70ec5ec" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "f9ec8108-15f7-48cf-b1a0-3ec254260c32" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
