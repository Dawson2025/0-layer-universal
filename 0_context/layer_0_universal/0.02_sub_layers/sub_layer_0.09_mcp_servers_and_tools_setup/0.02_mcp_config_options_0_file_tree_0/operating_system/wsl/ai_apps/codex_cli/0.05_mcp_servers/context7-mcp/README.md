# Context7 MCP (Codex CLI on WSL)

## Canonical docs
- `../../../../../../0.05_mcp_servers/context7-mcp/`

## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.03_automation/scripts/codex_mcp_sync.py`.
