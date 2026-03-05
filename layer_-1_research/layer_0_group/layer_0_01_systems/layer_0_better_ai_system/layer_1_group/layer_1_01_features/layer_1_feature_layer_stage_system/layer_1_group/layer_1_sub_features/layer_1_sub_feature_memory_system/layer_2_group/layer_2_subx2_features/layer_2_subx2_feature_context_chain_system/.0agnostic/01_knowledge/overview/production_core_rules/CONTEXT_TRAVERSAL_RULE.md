---
resource_id: "95f421ad-092f-4eee-9083-45fb5ada2674"
resource_type: "knowledge"
resource_name: "CONTEXT_TRAVERSAL_RULE"
---
# Context Traversal Rule

<!-- section_id: "33e0fd78-5ef0-47fd-9ea2-97a8eaf6acd6" -->
## Status
**MANDATORY** - Applies to EVERY API request

<!-- section_id: "8bf27e74-5012-4bec-b6e1-2731228e0da0" -->
## Rule

Before starting any task, traverse the AI system to gather context:

1. **Read CLAUDE.md files** in the path from root to working directory
2. **Identify current layer and stage** (layer_0, layer_1, layer_-1)
3. **Check relevant sub_layers** for applicable rules, prompts, knowledge
4. **Read status.json** if exists to understand current state

<!-- section_id: "4100cabc-dd70-4e66-b2b9-a17ed38f762a" -->
## Why This Matters

The layer-stage system contains context that informs how work should be done:
- Layer determines scope (universal vs project-specific vs research)
- Stage determines workflow phase (research, development, testing, etc.)
- Sub_layers contain rules, prompts, and knowledge that may apply
- status.json tracks progress and dependencies

<!-- section_id: "45d5d9e9-a540-43be-9711-89dc36993200" -->
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

<!-- section_id: "602621df-f8b4-4658-93b2-5ca930bc7522" -->
## Integration

This rule works with:
- **AI_CONTEXT_MODIFICATION_PROTOCOL.md** - Know what you're modifying
- **AI_CONTEXT_COMMIT_PUSH_RULE.md** - Track changes properly
