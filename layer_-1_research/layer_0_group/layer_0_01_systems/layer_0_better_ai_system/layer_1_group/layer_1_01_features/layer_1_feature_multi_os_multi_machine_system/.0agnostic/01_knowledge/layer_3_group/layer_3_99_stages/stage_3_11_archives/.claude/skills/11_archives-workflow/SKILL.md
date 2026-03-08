---
resource_id: "49408ef4-3378-46a2-8e63-53bfaf91061f"
resource_type: "skill_knowledge"
resource_name: "SKILL"
---
---
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

<!-- section_id: "d11e2438-bd34-4f6c-8d09-bb9d31d19788" -->
## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

<!-- section_id: "cdb162ca-ea60-4aaa-9635-3df3f29ec2fe" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "3830b471-7280-4711-8cf0-362a787c88f4" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "e98ce281-9689-4c46-9e56-1374e92d04c1" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
