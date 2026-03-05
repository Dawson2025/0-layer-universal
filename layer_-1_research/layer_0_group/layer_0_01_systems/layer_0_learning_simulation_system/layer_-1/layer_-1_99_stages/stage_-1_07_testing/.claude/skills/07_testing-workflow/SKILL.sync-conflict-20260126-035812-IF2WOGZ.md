---
resource_id: "bf1afb6f-782e-46a9-8d58-e73684829948"
resource_type: "document"
resource_name: "SKILL.sync-conflict-20260126-035812-IF2WOGZ"
name: 07_testing-workflow
description: Workflow skill for Quality assurance and validation. Activated when working on 07_testing tasks.
version: 1.0.0
---

# 07_testing Workflow Skill

<!-- section_id: "cf4f4bbc-ab97-4c8b-a617-ecaf7bcd0067" -->
## When to Use
- When entering the 07_testing stage
- When performing 07_testing activities
- When completing 07_testing deliverables

<!-- section_id: "aa9373d7-a685-45a4-9b30-1ba0c0abf48e" -->
## Workflow Steps
1. **Initialize**: Check hand_off_documents/ for incoming context
2. **Execute**: Perform 07_testing activities
3. **Document**: Place outputs in outputs/
4. **Handoff**: Prepare context for next stage

<!-- section_id: "138a2113-b598-40ee-b7ed-5f013bbabdfe" -->
## Key Files
- `outputs/` - Stage deliverables
- `hand_off_documents/` - Incoming/outgoing context
- `ai_agent_system/` - Agent configurations

<!-- section_id: "d9ac8e9c-ebf9-4bd7-b42a-5278e18bfa5a" -->
## Best Practices
- Cite sources for all findings
- Compare at least 2-3 alternatives
- Note limitations of research
