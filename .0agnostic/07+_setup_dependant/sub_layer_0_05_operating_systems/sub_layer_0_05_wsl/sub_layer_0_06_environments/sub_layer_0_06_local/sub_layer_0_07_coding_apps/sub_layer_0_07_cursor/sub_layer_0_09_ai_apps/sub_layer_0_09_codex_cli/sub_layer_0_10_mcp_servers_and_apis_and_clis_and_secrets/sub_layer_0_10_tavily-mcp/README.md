---
resource_id: "06447b97-3dc8-480e-91bd-2c7b1217ce10"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "1a075589-b93f-4a6b-8a6d-dfbc65de3ad3" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "08013e53-d943-47bc-ac33-392b50e2bb67" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "f08dca20-b16e-4742-b7b1-906cf894bca1" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
