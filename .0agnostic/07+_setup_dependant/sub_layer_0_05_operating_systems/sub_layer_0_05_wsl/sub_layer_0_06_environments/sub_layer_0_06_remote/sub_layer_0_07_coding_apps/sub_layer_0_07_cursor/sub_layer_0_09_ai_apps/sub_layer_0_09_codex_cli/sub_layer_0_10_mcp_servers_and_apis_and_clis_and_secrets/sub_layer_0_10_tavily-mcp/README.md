---
resource_id: "94df2cf5-6c71-4f43-9b76-d6f4eb37662a"
resource_type: "readme
document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "3f4f1e4f-3c02-4abd-83f1-a01ed171093b" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "1ac77365-2a13-4f88-baa9-9ec9fc6ccf52" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "7350c6c1-c04b-4d47-bbb2-0f1dbfb10dec" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
