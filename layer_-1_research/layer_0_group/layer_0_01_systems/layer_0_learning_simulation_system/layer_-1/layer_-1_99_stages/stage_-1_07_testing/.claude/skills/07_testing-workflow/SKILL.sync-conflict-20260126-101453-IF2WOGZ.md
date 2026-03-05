---
resource_id: "220b1209-e1b0-431a-a7b9-319245656c05"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101453-IF2WOGZ"
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on 07_testing tasks.
version: 1.0.0
---

# 07_testing Workflow Skill

## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
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
