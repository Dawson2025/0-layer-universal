---
resource_id: "d29e5189-a1ab-4f52-a9f1-75f6523887eb"
resource_type: "rule"
resource_name: "CONTEXT_TRAVERSAL_RULE"
---
# Context Traversal Rule

<!-- section_id: "f2f96b9d-b64f-4abd-a291-7401e619bf61" -->
## Status
**MANDATORY** - Applies to EVERY API request

<!-- section_id: "2add72bf-2dc0-40c4-992a-f88ae6f3aa49" -->
## Rule

Before starting any task, traverse the AI system to gather context:

1. **Read CLAUDE.md files** in the path from root to working directory
2. **Identify current layer and stage** (layer_0, layer_1, layer_-1)
3. **Check relevant sub_layers** for applicable rules, prompts, knowledge
4. **Read status.json** if exists to understand current state

<!-- section_id: "aa2fd2e1-9c20-4d9a-bbde-eb9abef0f2fa" -->
## Why This Matters

The layer-stage system contains context that informs how work should be done:
- Layer determines scope (universal vs project-specific vs research)
- Stage determines workflow phase (research, development, testing, etc.)
- Sub_layers contain rules, prompts, and knowledge that may apply
- status.json tracks progress and dependencies

<!-- section_id: "ca56bd2e-b324-4792-9048-657ab9f79d29" -->
## Example Traversal

Working in: `layer_1/layer_1_projects/project_foo/`

Read in order:
1. `/home/dawson/CLAUDE.md` (user root)
2. `dawson-workspace/CLAUDE.md` (workspace)
3. `code/CLAUDE.md` (code root)
4. `0_layer_universal/CLAUDE.md` (system root)
5. `layer_1/CLAUDE.md` (layer)
6. `layer_1_projects/CLAUDE.md` (projects container)
7. `project_foo/CLAUDE.md` (specific project)

<!-- section_id: "61565543-54dc-46af-9b1e-eb4b35c32635" -->
## Integration

This rule works with:
- **AI_CONTEXT_MODIFICATION_PROTOCOL.md** - Know what you're modifying
- **AI_CONTEXT_COMMIT_PUSH_RULE.md** - Track changes properly
