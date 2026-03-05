---
resource_id: "089d1063-dd05-48eb-bf95-2f0da5d4d334"
resource_type: "readme
document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
