---
resource_id: "435b2963-8b82-462a-9bf7-036bda7d0735"
resource_type: "readme_document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "0f1aa8b5-85c7-43b2-99f4-83fdbbbfd14d" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "fca15a05-95db-4f37-8259-75d8f73eea0c" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "d74220a8-115a-433f-91e9-d4276e623a6e" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
