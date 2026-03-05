---
resource_id: "84529b6e-6389-429e-9d7a-cb1d5cc68023"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035813-IF2WOGZ"
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

<!-- section_id: "aa9a1946-5ef6-4424-9cbe-5bbd32b7f0ca" -->
## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

<!-- section_id: "0ab58b86-b627-4525-b5ef-7aef54b504f0" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "dad2b6f6-0102-4d88-8c86-d06054631c0b" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "6b84b7d0-a156-4b3e-9f93-d7bfeb07bc01" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
