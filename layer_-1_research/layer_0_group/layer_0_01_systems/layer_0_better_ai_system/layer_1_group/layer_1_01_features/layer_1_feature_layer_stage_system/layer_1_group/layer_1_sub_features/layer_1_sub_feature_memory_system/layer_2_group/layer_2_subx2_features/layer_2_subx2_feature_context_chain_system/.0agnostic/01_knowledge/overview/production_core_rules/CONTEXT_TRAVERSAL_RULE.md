---
resource_id: "95f421ad-092f-4eee-9083-45fb5ada2674"
resource_type: "knowledge"
resource_name: "CONTEXT_TRAVERSAL_RULE"
---
# Context Traversal Rule

## Status
**MANDATORY** - Applies to EVERY API request

## Rule

Before starting any task, traverse the AI system to gather context:

1. **Read CLAUDE.md files** in the path from root to working directory
2. **Identify current layer and stage** (layer_0, layer_1, layer_-1)
3. **Check relevant sub_layers** for applicable rules, prompts, knowledge
4. **Read status.json** if exists to understand current state

## Why This Matters

The layer-stage system contains context that informs how work should be done:
- Layer determines scope (universal vs project-specific vs research)
- Stage determines workflow phase (research, development, testing, etc.)
- Sub_layers contain rules, prompts, and knowledge that may apply
- status.json tracks progress and dependencies

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

## Integration

This rule works with:
- **AI_CONTEXT_MODIFICATION_PROTOCOL.md** - Know what you're modifying
- **AI_CONTEXT_COMMIT_PUSH_RULE.md** - Track changes properly
