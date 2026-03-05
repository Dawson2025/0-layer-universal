---
resource_id: "e80ffe6c-9903-4684-a91f-a59ee15aff28"
resource_type: "document"
resource_name: "MCP_SERVER_MATRIX"
---
# MCP Server Matrix (with tool automation coverage)

Lists all MCP servers we have configs for, plus which AI tools/CLIs have automation or documented setup. Disabled servers remain listed for visibility.

See `BROWSER_MCP_ROUTING_TABLE.md` for recommendations on which browser server to use per CLI/OS/task.

<!-- section_id: "e0a02565-a625-4d95-9ef2-6ae926686857" -->
## Legend
- ✅ Automated / documented working setup
- ⚠️ Manual setup documented but not automated
- ✖️ Not configured

<!-- section_id: "3d03cee9-53d9-4f10-9e0f-96f6d454b497" -->
## Servers
| Server              | Status (Codex env: development) | Codex CLI (config.toml / codex_mcp_sync.py) | Gemini CLI (~/.gemini/settings.json) | Notes |
|---------------------|----------------------------------|--------------------------------------------|---------------------------------------|-------|
| playwright          | Enabled (headed)                 | ✅ (auto via sync script; headed)           | ✅ (settings.json pattern)            | Uses PLAYWRIGHT_BROWSERS_PATH, DISPLAY, HOME |
| web-search (Tavily) | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires TAVILY_API_KEY env |
| context7            | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires CONTEXT7_API_KEY/URL env |
| browser             | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (doc’d, manual add)                | Headed via DISPLAY/PLAYWRIGHT_BROWSERS_PATH |
| filesystem          | Disabled                         | ✅ (auto via sync script; currently disabled) | ✖️                                    | Generic fs server; enable as needed |
| chrome-devtools     | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (manual pattern)                  | Needs running Chrome with remote debugging |

<!-- section_id: "d42345bd-bd23-410d-ad4a-f18818beb529" -->
## How to switch/disable/enable (Codex)
- Use `codex_mcp_sync.py --env <env> [--disable <servers...>]`
  - Active snippet: `~/.codex/environments/<env>.toml`
  - Full snippet: `~/.codex/environments/<env>.full.toml`
  - Disabled snippet: `~/.codex/environments/<env>.disabled.toml`
  - Backup: `~/.codex/config.toml.bak`
- Restart Codex CLI after sync.

<!-- section_id: "30b6ada4-0b55-42e7-909a-e544cd2151e5" -->
## Gemini reference
- Single canonical file: `~/.gemini/settings.json` with `mcpServers` entries (see core-system/README.md and GEMINI CLI sections).

<!-- section_id: "291d9915-ffdf-4be9-8aa1-2428f33b4ff4" -->
## To add another tool
- Add its server block to the presets in `automation/scripts/codex_mcp_sync.py` (and, if desired, document Gemini settings.json pattern).
- Rerun the sync script to regenerate Codex config and snippets.
