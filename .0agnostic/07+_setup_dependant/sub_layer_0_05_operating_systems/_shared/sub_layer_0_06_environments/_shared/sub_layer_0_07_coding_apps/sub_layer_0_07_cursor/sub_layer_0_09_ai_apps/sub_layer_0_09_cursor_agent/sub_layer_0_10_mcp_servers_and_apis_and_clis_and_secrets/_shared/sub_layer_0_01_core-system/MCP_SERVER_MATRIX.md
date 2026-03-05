---
resource_id: "1bf9f209-495e-4c81-afb2-26890bfd2a52"
resource_type: "document"
resource_name: "MCP_SERVER_MATRIX"
---
# MCP Server Matrix (with tool automation coverage)

Lists all MCP servers we have configs for, plus which AI tools/CLIs have automation or documented setup. Disabled servers remain listed for visibility.

See `BROWSER_MCP_ROUTING_TABLE.md` for recommendations on which browser server to use per CLI/OS/task.

<!-- section_id: "9b0f258c-f022-47a2-ae64-089b40939989" -->
## Legend
- ✅ Automated / documented working setup
- ⚠️ Manual setup documented but not automated
- ✖️ Not configured

<!-- section_id: "a68c26e9-d819-4dd4-9172-d0661a548c0b" -->
## Servers
| Server              | Status (Codex env: development) | Codex CLI (config.toml / codex_mcp_sync.py) | Gemini CLI (~/.gemini/settings.json) | Notes |
|---------------------|----------------------------------|--------------------------------------------|---------------------------------------|-------|
| playwright          | Enabled (headed)                 | ✅ (auto via sync script; headed)           | ✅ (settings.json pattern)            | Uses PLAYWRIGHT_BROWSERS_PATH, DISPLAY, HOME |
| web-search (Tavily) | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires TAVILY_API_KEY env |
| context7            | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires CONTEXT7_API_KEY/URL env |
| browser             | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (doc’d, manual add)                | Headed via DISPLAY/PLAYWRIGHT_BROWSERS_PATH |
| filesystem          | Disabled                         | ✅ (auto via sync script; currently disabled) | ✖️                                    | Generic fs server; enable as needed |
| chrome-devtools     | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (manual pattern)                  | Needs running Chrome with remote debugging |

<!-- section_id: "7541c818-c7fb-4610-b635-893991279031" -->
## How to switch/disable/enable (Codex)
- Use `codex_mcp_sync.py --env <env> [--disable <servers...>]`
  - Active snippet: `~/.codex/environments/<env>.toml`
  - Full snippet: `~/.codex/environments/<env>.full.toml`
  - Disabled snippet: `~/.codex/environments/<env>.disabled.toml`
  - Backup: `~/.codex/config.toml.bak`
- Restart Codex CLI after sync.

<!-- section_id: "a0767ac1-8342-411d-ad95-d6ec6c448995" -->
## Gemini reference
- Single canonical file: `~/.gemini/settings.json` with `mcpServers` entries (see core-system/README.md and GEMINI CLI sections).

<!-- section_id: "41811df5-b05d-455a-9f48-2edc3deaabb3" -->
## To add another tool
- Add its server block to the presets in `automation/scripts/codex_mcp_sync.py` (and, if desired, document Gemini settings.json pattern).
- Rerun the sync script to regenerate Codex config and snippets.
