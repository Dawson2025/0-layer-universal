---
resource_id: "51daa2e5-35c1-4523-8580-efb00f5ca4a2"
resource_type: "document"
resource_name: "tool_boilerplate"
---
<!-- section_id: "bb4f6af3-2cad-4738-ae8e-240747f8b521" -->
## Codex CLI Configuration

<!-- section_id: "3da3b550-81a8-4792-86c4-c401bb5535e8" -->
### Context Source
- Use `AGENTS.md` as the hot context source for this entity.
- Treat `0AGNOSTIC.md` as source-of-truth; never hand-edit generated context files.

<!-- section_id: "5ab6159e-e0fd-4edd-8f0a-9c345b7d5840" -->
### Codex Operational Rules
- For structural edits, read `.0agnostic/03_protocols/` first.
- For behavior constraints, read `.0agnostic/02_rules/static/` first, then dynamic rules.
- For deep domain detail, load only the needed file from `.0agnostic/01_knowledge/`.

<!-- section_id: "c7f623ec-deed-4dcb-9a4f-46179302a15a" -->
### Session Continuity
- On resume, check `.0agnostic/04_episodic_memory/sessions/` and `changes/`.
- Keep edits scoped to the active entity unless explicitly asked to broaden scope.
