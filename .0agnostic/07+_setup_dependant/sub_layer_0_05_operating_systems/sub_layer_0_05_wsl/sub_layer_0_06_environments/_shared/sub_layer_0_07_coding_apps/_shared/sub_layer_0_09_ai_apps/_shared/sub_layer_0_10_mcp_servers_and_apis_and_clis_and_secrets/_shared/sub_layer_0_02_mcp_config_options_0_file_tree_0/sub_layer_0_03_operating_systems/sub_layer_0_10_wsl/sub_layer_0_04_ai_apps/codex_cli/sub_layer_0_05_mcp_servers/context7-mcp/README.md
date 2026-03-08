---
resource_id: "8bcff153-a0ae-41db-b346-0915a188046d"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "c46c35dd-6b58-4918-8e29-467a66e87e4f" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "0800e53a-4a0e-4fdd-9d36-f6704c109dcb" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "ac8215f7-d004-46e1-87a6-bd628f0ad6dc" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
