---
resource_id: "45c2b8aa-4931-4a49-b16e-3cfdf708a029"
resource_type: "readme
knowledge"
resource_name: "README"
---
# 0_every_api_request

## Purpose

Rules in this folder apply to **EVERY API request** universally. These rules should be included (or summarized) in system prompts like CLAUDE.md files.

## Rules

| File | Purpose |
|------|---------|
| `AI_CONTEXT_MODIFICATION_PROTOCOL.md` | Show diagram, wait for approval before modifying AI context |
| `AI_CONTEXT_COMMIT_PUSH_RULE.md` | Git add/commit/push after approved AI context changes |
| `CONTEXT_TRAVERSAL_RULE.md` | Read CLAUDE.md files and gather context before starting work |

## Usage

These rules are summarized in:
- `/home/dawson/CLAUDE.md`
- `/home/dawson/.claude/CLAUDE.md`
- `0_layer_universal/CLAUDE.md`

The full rule documents here provide complete details when needed.

## Why "Every API Request"

These rules ensure:
1. **Context awareness** - AI understands where it's working
2. **Change safety** - No unauthorized modifications to AI context
3. **Audit trail** - Changes are committed and pushed
