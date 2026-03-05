---
resource_id: "51daa2e5-35c1-4523-8580-efb00f5ca4a2"
resource_type: "document"
resource_name: "tool_boilerplate"
---
## Codex CLI Configuration

### Context Source
- Use `AGENTS.md` as the hot context source for this entity.
- Treat `0AGNOSTIC.md` as source-of-truth; never hand-edit generated context files.

### Codex Operational Rules
- For structural edits, read `.0agnostic/03_protocols/` first.
- For behavior constraints, read `.0agnostic/02_rules/static/` first, then dynamic rules.
- For deep domain detail, load only the needed file from `.0agnostic/01_knowledge/`.

### Session Continuity
- On resume, check `.0agnostic/04_episodic_memory/sessions/` and `changes/`.
- Keep edits scoped to the active entity unless explicitly asked to broaden scope.
