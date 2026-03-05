---
resource_id: "767a00b3-5c83-432e-9cfe-1e9b967d767c"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035815-IF2WOGZ"
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on 09_fixing tasks.
version: 1.0.0
---

# 09_fixing Workflow Skill

<!-- section_id: "2ec21c32-6874-4643-aa2b-07210ca5ee3b" -->
## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

<!-- section_id: "0f752c01-5880-473e-acec-bd4e2880b0fe" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "21e08cba-63e9-4a03-afe6-2cfe18cccf00" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "541e8077-166b-4754-a0bb-7c8bd70cea56" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
