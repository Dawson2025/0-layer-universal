---
resource_id: "177db1e3-f602-4fdb-852a-d3f70afd82ce"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035812-IF2WOGZ"
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

<!-- section_id: "79f18e15-aa8f-48d0-b89a-8a525362b8a2" -->
## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

<!-- section_id: "c0b4a9b6-7380-48e6-ad21-b9324110ec4d" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "01cc8db5-9d73-48e0-9906-e449ebfa0ac4" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "cd5166f1-b48b-4cf4-8818-7f2bdb0a024b" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
