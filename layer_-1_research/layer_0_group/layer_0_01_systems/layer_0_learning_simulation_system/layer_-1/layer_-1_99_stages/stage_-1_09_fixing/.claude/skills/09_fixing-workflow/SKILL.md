---
resource_id: "ce902ca2-b78e-47dc-953b-8b67c9cad3ef"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on 09_fixing tasks.
version: 1.0.0
---

# 09_fixing Workflow Skill

<!-- section_id: "696a0ed1-b0d1-44e2-9c5d-b8a1f0bfc433" -->
## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

<!-- section_id: "e1f86ec7-57c3-4174-837e-fcf967979e84" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "3301f302-0132-44b1-9611-9a1590437f04" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "f16916e9-0009-442c-aee3-1c0b820dc430" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
