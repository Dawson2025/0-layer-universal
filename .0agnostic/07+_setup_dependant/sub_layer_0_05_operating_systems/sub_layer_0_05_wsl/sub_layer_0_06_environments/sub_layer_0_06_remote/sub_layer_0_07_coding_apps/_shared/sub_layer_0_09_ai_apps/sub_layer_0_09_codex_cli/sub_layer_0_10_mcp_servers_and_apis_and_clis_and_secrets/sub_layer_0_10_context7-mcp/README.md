---
resource_id: "431b0eb0-4e9e-42d1-8d91-a79faa007957"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
