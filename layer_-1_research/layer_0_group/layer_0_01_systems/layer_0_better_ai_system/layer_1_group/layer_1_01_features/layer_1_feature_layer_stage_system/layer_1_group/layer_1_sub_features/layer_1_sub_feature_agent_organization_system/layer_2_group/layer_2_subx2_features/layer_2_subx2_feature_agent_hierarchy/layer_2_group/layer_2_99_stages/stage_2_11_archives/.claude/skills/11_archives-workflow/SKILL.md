---
resource_id: "cdc9d3dd-88ee-4512-8aaa-ac0b93e77194"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

<!-- section_id: "1ed72eb2-968d-4e58-999e-df5cee4006c7" -->
## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

<!-- section_id: "cc3b4943-42b4-484e-858b-9efd81832502" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "7d0b4da5-a3fe-4cfa-b9fa-093fd98424ee" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "603c006c-f732-4b29-bad8-b0e4ba2be6c4" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
