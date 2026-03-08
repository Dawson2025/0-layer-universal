---
resource_id: "e54296cc-7b07-4743-8487-5a8d980a6909"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "970cd174-bc5a-4c36-8b8b-199085710796" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "a8365727-d283-456c-b7ee-8f96b77eff9e" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "3e522dbc-dc6b-49bc-be70-3e498533cafa" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
