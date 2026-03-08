---
resource_id: "ecf52262-e722-42d9-8af0-bb4002f4d766"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "c379c8a4-7b6a-4992-9fe3-b8b4b7f39767" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "5cf6de79-2783-4abc-ba91-b43ecbe0c533" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "4c35f77f-e92b-4e06-8280-9d3ab508ac59" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
