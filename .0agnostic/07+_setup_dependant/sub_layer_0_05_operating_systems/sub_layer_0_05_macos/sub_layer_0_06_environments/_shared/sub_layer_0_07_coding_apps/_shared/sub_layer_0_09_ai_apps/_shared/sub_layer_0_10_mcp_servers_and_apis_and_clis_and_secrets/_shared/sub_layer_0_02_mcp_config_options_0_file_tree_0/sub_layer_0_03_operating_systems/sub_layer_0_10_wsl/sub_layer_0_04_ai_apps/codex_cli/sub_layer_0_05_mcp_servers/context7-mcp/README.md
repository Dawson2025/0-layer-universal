---
resource_id: "73e43724-2bd7-45f8-95f0-d1284def3f2e"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "f777b5ee-55e9-4c29-ace0-18b7b4a0a261" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "5f3d618d-497c-40b2-a583-64ca2ef9b38e" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "169de797-739d-4af8-a533-b4801a4edc4d" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
