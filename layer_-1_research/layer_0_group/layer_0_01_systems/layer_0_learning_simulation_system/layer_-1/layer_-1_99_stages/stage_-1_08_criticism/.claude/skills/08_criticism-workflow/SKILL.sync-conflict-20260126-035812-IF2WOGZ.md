---
resource_id: "a474fdc5-9908-488b-a6b0-9582f8c48510"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035812-IF2WOGZ"
name: 08_criticism-workflow
description: Workflow skill for Review and identify improvements. Activated when working on 08_criticism tasks.
version: 1.0.0
---

# 08_criticism Workflow Skill

<!-- section_id: "a8f38755-78c8-4b8c-9d2b-60ab754d0262" -->
## When to Use
- When entering the 08_criticism stage
- When performing 08_criticism activities
- When completing 08_criticism deliverables

<!-- section_id: "91176e1b-15be-4e60-959c-61e6eee65b34" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 08_criticism activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "9e9a8a22-4498-49c7-873d-ccce2e9aa1be" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "e828c417-e84f-4620-8e97-b3957a1ba635" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
