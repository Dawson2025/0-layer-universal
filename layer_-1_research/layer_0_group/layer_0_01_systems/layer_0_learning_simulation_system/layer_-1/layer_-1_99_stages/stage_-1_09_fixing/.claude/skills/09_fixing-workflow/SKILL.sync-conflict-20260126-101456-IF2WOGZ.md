---
resource_id: "831d14aa-0880-4b22-856a-da1d2ac2fdac"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-101456-IF2WOGZ"
name: 09_fixing-workflow
description: Workflow skill for Address issues from criticism. Activated when working on 09_fixing tasks.
version: 1.0.0
---

# 09_fixing Workflow Skill

<!-- section_id: "14b16a7a-b1d0-4712-829e-b0ecb1c0180b" -->
## When to Use
- When entering the 09_fixing stage
- When performing 09_fixing activities
- When completing 09_fixing deliverables

<!-- section_id: "d038bdac-46a9-46e9-8668-3d34d0df69e8" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 09_fixing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "ed2bb08f-614a-4712-93ba-7392f893f551" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "89a0dad9-0fd8-4b70-a05b-6d961d84c033" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
