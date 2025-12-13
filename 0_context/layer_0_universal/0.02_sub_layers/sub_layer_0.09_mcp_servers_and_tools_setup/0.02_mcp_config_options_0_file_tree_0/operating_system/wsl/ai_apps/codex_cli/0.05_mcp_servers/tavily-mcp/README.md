# Tavily MCP (web-search) (Codex CLI on WSL)

## Canonical docs
- `../../../../../../0.05_mcp_servers/tavily-mcp/`

## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.03_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
