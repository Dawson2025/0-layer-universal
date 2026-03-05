---
resource_id: "3f89eb85-4525-42d6-ac97-8abdc5dbc403"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

<!-- section_id: "676f3ff3-9614-4b1e-baec-3bce768d8cfc" -->
## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

<!-- section_id: "c5c40eba-9dee-418b-b52f-d6d5e16c2395" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "fd5b72e5-2773-4771-bf72-e58f872c5670" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "7efb635f-072b-41a4-8816-e712860c8a5d" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
