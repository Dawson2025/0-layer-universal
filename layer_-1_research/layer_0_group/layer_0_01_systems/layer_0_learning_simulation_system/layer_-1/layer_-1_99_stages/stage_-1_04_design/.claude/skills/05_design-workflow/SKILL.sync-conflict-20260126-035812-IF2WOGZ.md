---
resource_id: "b9c73763-705c-4d70-ba7c-ebc257429066"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035812-IF2WOGZ"
name: 05_design-workflow
description: Workflow skill for Technical design and architecture. Activated when working on 05_design tasks.
version: 1.0.0
---

# 05_design Workflow Skill

<!-- section_id: "05cbc4f4-fc69-4786-ad46-fc5308d8a9de" -->
## When to Use
- When entering the 05_design stage
- When performing 05_design activities
- When completing 05_design deliverables

<!-- section_id: "f6b87ae6-c58c-4e06-97b4-a4cb13ba9eb1" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 05_design activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "e5536877-6c49-4de1-b2b4-8c3d649443b6" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "3bc77730-c75a-49d9-b48e-3cdb9cd4e5f9" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
