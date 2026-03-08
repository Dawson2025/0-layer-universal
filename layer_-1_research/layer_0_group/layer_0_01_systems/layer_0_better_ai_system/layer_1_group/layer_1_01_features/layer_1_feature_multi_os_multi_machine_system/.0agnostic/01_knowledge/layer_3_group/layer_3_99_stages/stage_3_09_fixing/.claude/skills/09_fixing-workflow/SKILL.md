---
resource_id: "6d838af5-f91d-402b-bb39-59b19e41bec9"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on 09_fixing tasks.
version: 1.0.0
---

# 09_fixing Workflow Skill

<!-- section_id: "e7c511f9-9959-42c5-8573-39e0f98d9122" -->
## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

<!-- section_id: "76745482-bcbc-4ad4-a495-a1fdf007bd61" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "aba689d4-7be1-4495-b934-612df750a0fe" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "652a2af1-a7e9-4019-83ad-f3851269590e" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
