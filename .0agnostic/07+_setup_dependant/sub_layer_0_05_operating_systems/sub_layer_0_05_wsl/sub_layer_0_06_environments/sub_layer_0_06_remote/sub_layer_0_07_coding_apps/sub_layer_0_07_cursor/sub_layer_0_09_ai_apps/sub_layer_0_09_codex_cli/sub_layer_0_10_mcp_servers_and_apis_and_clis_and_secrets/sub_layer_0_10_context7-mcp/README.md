---
resource_id: "fc46bcd3-dd8d-40df-b99f-2f951beb56ed"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "b0dd1fb2-d3a7-4e3d-83da-dc03cab96749" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "d080a7a1-1f67-45ad-aeb8-a2167a267fdb" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "bd078444-d4d5-4c05-9073-5e0105a58ea6" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
