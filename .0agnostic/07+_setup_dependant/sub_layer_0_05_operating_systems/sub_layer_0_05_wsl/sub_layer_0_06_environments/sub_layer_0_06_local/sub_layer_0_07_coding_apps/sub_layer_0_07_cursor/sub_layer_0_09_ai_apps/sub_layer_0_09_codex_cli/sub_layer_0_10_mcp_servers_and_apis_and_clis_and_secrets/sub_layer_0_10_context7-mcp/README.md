---
resource_id: "29192052-6ff9-4c80-a002-d8654210e8be"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "cd9d3037-76fc-45f1-a320-7f9ab9e0918a" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "f026b278-acab-4215-80ea-5808c4f2410d" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "628438a3-1b6f-42bf-aa54-49a7d1c5c375" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
