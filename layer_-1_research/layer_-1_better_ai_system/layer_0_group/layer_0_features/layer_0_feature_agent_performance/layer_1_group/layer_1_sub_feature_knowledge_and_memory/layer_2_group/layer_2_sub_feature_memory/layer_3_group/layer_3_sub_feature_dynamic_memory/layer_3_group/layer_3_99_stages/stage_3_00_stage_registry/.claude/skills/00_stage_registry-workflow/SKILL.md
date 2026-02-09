---
name: 00_stage_registry-workflow
description: Workflow skill for Stage metadata and registration. Activated when working on 00_stage_registry tasks.
version: 1.0.0
---

# 00_stage_registry Workflow Skill

## When to Use
- When entering the 00_stage_registry stage
- When performing 00_stage_registry activities
- When completing 00_stage_registry deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 00_stage_registry activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
