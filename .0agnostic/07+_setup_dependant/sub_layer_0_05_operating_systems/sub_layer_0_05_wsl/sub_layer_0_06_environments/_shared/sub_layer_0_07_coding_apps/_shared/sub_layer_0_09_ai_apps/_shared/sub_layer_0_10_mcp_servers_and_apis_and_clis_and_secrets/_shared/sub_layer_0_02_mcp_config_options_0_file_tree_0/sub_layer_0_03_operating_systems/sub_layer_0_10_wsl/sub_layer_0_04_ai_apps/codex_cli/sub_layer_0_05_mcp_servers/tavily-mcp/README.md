---
resource_id: "c39a8f35-e544-4eb9-8cd0-ba5ff87a751f"
resource_type: "readme_document"
resource_name: "README"
---
# Tavily MCP (web-search) (Codex CLI on WSL)

<!-- section_id: "0430a15c-9b1b-48f6-abdf-7bcb42baa52d" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/tavily-mcp/`

<!-- section_id: "a25b8bc0-336f-4847-aa53-9bbcb3c428f9" -->
## Key requirement
- `TAVILY_API_KEY` must be present or the server will exit immediately (MCP handshake fails).

<!-- section_id: "5ceb4aba-2ace-4bb5-8dcc-fa08ee9a486b" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py` to inject them into `~/.codex/config.toml`.
