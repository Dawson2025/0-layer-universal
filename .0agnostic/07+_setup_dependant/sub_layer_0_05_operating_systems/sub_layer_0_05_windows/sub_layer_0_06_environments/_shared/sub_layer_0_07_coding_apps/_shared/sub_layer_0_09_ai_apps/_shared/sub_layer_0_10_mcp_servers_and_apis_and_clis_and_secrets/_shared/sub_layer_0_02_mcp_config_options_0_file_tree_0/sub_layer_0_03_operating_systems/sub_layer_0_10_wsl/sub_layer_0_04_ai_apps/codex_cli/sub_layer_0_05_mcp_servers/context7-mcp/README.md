---
resource_id: "16524df7-4c0c-42f6-a500-1e45a1f79e01"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "7cc695a2-e1d7-47f1-aff8-4eb8b8d4811e" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "7c60e448-f272-494d-83ae-e77a0eb067ed" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "e8ea992b-4c53-4388-afc2-90c4ed9c8766" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
