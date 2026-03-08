---
resource_id: "0c4794c5-5b85-4627-a970-e63a24bdb0f0"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: 04_planning-workflow
description: Workflow skill for Create implementation plan. Activated when working on 04_planning tasks.
version: 1.0.0
---

# 04_planning Workflow Skill

<!-- section_id: "a598a736-9430-4adc-a878-e7c9b635552f" -->
## When to Use
- When entering the 04_planning stage
- When performing 04_planning activities
- When completing 04_planning deliverables

<!-- section_id: "dc022d70-1fae-43ec-8f92-8de1dbb3499a" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 04_planning activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "75875354-c4c6-4862-99ad-22b4e290834e" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "a65d8b0a-0a7d-4194-b992-4fee31f0f863" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
