---
resource_id: "e956f37d-5928-41d2-a403-9e4653c38a02"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 02_research-workflow
description: Workflow skill for Explore problem space, gather information. Activated when working on 02_research tasks.
version: 1.0.0
---

# 02_research Workflow Skill

<!-- section_id: "8d2d5009-267f-4e73-93df-dea77f75d616" -->
## When to Use
- When entering the 02_research stage
- When performing 02_research activities
- When completing 02_research deliverables

<!-- section_id: "be7eb2c4-b04e-4342-9d35-29a60b9b54bd" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 02_research activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "9eeb9a10-e1d7-4035-99aa-0f0006d9f3c8" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "3ff05f80-8ff2-45b9-8012-33053d0bd877" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
