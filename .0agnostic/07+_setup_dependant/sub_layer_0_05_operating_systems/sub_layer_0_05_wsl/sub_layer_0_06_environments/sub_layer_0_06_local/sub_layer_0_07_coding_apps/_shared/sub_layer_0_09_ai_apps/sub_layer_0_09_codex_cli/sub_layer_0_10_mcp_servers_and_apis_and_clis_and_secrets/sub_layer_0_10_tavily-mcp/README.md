---
resource_id: "1e1472ae-ec54-4631-bc31-aa57e986ac70"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "b5489981-15bd-49eb-b5f0-474d434654e4" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "63f2e0b7-2f61-44e2-a8da-efb0f1245b07" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "72322b9c-bada-4e1d-a643-85e5676a369b" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
