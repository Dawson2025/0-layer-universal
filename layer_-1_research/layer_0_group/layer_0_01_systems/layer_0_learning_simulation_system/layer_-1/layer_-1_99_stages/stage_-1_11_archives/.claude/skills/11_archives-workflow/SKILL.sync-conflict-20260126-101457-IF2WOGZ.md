---
resource_id: "908cf4ca-51ec-4d80-82a0-18b7266749aa"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101457-IF2WOGZ"
name: 11_archives-workflow
description: Workflow skill for Historical versions and deprecated content. Activated when working on 11_archives tasks.
version: 1.0.0
---

# 11_archives Workflow Skill

<!-- section_id: "30e01172-1509-4627-817e-b9115e257069" -->
## When to Use
- When entering the 11_archives stage
- When performing 11_archives activities
- When completing 11_archives deliverables

<!-- section_id: "4e6afa4d-b51b-495a-8252-6c095f2007e7" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 11_archives activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "69c43b62-c740-4582-8fe0-f76cd79000d3" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "b621b53f-c500-40db-bc05-9fc5873c380a" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
