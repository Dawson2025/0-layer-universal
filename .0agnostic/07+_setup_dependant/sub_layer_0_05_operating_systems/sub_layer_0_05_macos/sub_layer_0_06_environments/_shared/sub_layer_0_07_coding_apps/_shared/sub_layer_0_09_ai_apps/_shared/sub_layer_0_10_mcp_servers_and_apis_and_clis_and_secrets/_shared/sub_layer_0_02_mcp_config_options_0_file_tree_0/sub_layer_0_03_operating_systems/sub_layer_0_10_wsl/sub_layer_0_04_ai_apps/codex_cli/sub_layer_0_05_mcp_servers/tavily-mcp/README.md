---
resource_id: "7df97a5b-1a3d-470c-bab4-868204bbf9e5"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "49c772d0-0479-4e45-9f2b-0743768e5da8" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "88ba2889-72dd-4d4c-9336-e2741fabf70c" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "8ec64a2f-ac5d-4f47-9cdb-f6aebd4333f2" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
