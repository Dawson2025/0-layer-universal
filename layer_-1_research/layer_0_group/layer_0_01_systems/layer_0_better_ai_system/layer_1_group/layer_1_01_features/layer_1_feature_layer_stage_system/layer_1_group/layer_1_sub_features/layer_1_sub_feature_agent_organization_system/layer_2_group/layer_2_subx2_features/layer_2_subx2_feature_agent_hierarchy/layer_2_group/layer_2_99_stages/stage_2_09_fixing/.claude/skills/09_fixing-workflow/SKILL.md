---
resource_id: "1ff9c38b-6f9b-4c3e-9460-4d8346648456"
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

<!-- section_id: "82fab660-9fc4-4511-9af8-a6dcf8420d3d" -->
## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

<!-- section_id: "5b03c42a-a564-4708-bfda-722a60662f1b" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "193b73bd-d444-4da7-8f97-01dacdf051fd" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "9eafce87-0252-480d-a1b8-e8af8a73c6ad" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
