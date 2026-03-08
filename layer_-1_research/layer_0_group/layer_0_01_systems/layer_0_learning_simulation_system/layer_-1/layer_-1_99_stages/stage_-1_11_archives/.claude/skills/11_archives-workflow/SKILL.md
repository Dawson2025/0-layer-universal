---
resource_id: "1281da58-a198-4305-8218-e7a72aed803c"
resource_type: "skill_document"
resource_name: "SKILL"
---
---
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

<!-- section_id: "35c372fe-3631-4daa-acf5-3dee4faf3b7f" -->
## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

<!-- section_id: "9906a3ec-36b5-4797-8e46-90ea233ceb4a" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "1ee9dedd-0028-4e46-b2f9-2931aeb5c3e7" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "4e260151-1740-40b6-9cf5-6d4344cde3ad" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
