---
resource_id: "e804b027-5bcc-4263-9ec3-0ca16c829c44"
resource_type: "readme
document"
resource_name: "README"
---
# Context7 MCP (Codex CLI on WSL)

<!-- section_id: "688c55d0-d50c-4606-b0f4-3d4c4e6f56c6" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/context7-mcp/`

<!-- section_id: "8c9d35e3-2a2a-4b69-b7f8-07cd6068fc70" -->
## Key requirements
- Provide `CONTEXT7_API_KEY`
- Optionally provide `CONTEXT7_API_URL` (commonly `https://context7.com/api/v1`)

<!-- section_id: "4a2d31b9-eb02-4ff8-96c7-56b9abe18912" -->
## Codex integration
- Prefer `~/.codex/mcp.env` for secrets, then run `0.06_automation/scripts/codex_mcp_sync.py`.
