---
resource_id: "7bea9972-6a66-4d33-924e-00bc69de21ea"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

<!-- section_id: "ba682732-17d8-496f-88b5-cfc5eeedc81c" -->
## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

<!-- section_id: "5808895e-a97e-4527-853c-ca05ed907cda" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "c7681458-b9f0-4136-bb2b-b72cb8309872" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "250f0d7f-0626-4b50-b77c-3bed377e5ca8" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
