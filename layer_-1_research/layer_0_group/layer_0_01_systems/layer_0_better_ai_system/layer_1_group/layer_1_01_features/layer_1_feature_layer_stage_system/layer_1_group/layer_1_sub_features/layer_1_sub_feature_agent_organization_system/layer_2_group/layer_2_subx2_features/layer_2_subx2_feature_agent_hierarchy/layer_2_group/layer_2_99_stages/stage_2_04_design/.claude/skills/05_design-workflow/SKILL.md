---
resource_id: "1e36270c-0d3b-4c4d-b2ae-c485161b34de"
resource_type: "skill
document"
resource_name: "SKILL"
---
---
name: 05_design-workflow
description: Workflow skill for Technical design and architecture. Activated when working on 05_design tasks.
version: 1.0.0
---

# 05_design Workflow Skill

<!-- section_id: "7f579498-b3d9-4eee-a797-c72de6fc2219" -->
## When to Use
- When entering the 05_design stage
- When performing 05_design activities
- When completing 05_design deliverables

<!-- section_id: "ad0d057f-7c2b-48e1-baa1-40d88789e8aa" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 05_design activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "8b2df8db-0cac-48bc-8e76-f620a4ea6abc" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "11ecc2f0-4c1b-4265-a017-5aa37131274a" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
