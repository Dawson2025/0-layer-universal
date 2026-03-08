---
resource_id: "b8456c77-53a2-41bf-a4c1-af600832283d"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "cf8bbb23-e198-4a53-9f13-e5689e35aea9" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "e33bec3f-b366-40a2-be9c-fa0c16abaa95" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "bc0d0e8e-ac4a-4c96-a9f8-c68a5d0d3a26" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
