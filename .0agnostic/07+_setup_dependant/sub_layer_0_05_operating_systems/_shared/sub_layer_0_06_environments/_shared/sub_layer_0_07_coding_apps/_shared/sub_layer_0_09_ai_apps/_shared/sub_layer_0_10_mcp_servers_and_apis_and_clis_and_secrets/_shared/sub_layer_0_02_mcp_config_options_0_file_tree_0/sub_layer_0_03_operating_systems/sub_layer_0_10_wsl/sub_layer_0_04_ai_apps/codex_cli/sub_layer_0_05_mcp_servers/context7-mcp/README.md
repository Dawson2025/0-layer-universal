---
resource_id: "b09ca2bb-70c8-40e2-acf3-63c294c532f4"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "d5346901-e9db-4c09-a4fe-4e5dcc465b80" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "a1ed7885-a5b5-473f-b390-6374a688be61" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "e77dc64b-fa55-4dfa-80d9-86523ece66f1" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
