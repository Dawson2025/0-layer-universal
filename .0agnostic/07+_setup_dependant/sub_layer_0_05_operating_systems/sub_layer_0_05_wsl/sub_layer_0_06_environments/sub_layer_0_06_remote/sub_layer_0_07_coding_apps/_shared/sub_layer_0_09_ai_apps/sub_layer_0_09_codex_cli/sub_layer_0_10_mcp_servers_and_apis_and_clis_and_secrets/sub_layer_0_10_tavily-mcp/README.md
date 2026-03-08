---
resource_id: "a99edacf-03fd-4071-b0cb-4ad45e7c6de6"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "99c2e421-7f33-436f-978b-2127d7652dec" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "41b7cbe5-aa83-4ef3-84e6-c5486cbba579" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "ede2f64d-2341-4a41-a494-a87ed0e9d31c" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
