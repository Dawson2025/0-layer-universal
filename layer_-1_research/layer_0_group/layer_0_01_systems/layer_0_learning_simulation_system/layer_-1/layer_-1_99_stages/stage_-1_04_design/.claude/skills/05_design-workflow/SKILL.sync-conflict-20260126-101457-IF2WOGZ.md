---
resource_id: "a98280da-ed8c-48ed-a7fc-d383418370fc"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101457-IF2WOGZ"
name: 05_design-workflow
description: Workflow skill for Technical design and architecture. Activated when working on 05_design tasks.
version: 1.0.0
---

# 05_design Workflow Skill

<!-- section_id: "267c4768-8de2-4cad-bb11-04c40bfd72fe" -->
## When to Use
- When entering the 05_design stage
- When performing 05_design activities
- When completing 05_design deliverables

<!-- section_id: "9f92f31a-b0f6-400d-ab72-9e42f242886a" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 05_design activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "eadbc3fb-73cd-4589-858b-07d1cdf26421" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "ef171e4b-a6f1-49bb-a32a-0c848e129716" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
