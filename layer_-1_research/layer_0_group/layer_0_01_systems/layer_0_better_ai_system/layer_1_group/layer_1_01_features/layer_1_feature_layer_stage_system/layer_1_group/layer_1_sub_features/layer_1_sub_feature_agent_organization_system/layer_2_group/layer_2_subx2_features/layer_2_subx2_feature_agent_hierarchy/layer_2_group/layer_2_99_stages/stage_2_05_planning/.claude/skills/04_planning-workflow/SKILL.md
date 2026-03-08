---
resource_id: "8b8253fb-67cb-4c1a-9798-74fa46c54332"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

<!-- section_id: "a55b3ad8-a089-499a-bcc9-6802abb19700" -->
## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

<!-- section_id: "c8e4cc75-9ff0-431b-9731-f6bcdb4c7430" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "ca98a79a-0388-4fbe-9c4e-030d63f72b8c" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "d04aa344-9599-4586-bbe9-f4281f54176c" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
