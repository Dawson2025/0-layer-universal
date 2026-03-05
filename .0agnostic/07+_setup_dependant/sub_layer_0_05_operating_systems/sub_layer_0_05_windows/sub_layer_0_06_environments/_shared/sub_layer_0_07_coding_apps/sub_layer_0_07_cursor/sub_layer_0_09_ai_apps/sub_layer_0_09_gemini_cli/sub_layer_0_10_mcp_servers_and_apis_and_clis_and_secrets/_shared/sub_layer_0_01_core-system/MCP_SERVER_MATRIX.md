---
resource_id: "9f25134f-d44a-4551-8c91-a92f39361141"
resource_type: "document"
resource_name: "MCP_SERVER_MATRIX"
---
# MCP Server Matrix (with tool automation coverage)

Lists all MCP servers we have configs for, plus which AI tools/CLIs have automation or documented setup. Disabled servers remain listed for visibility.

See `BROWSER_MCP_ROUTING_TABLE.md` for recommendations on which browser server to use per CLI/OS/task.

<!-- section_id: "5dc77803-4375-4fcb-9a8c-71b2271aebb3" -->
## Legend
- ✅ Automated / documented working setup
- ⚠️ Manual setup documented but not automated
- ✖️ Not configured

<!-- section_id: "a4243e69-ba42-4f91-8dfe-7d6056f32c0e" -->
## Servers
| Server              | Status (Codex env: development) | Codex CLI (config.toml / codex_mcp_sync.py) | Gemini CLI (~/.gemini/settings.json) | Notes |
|---------------------|----------------------------------|--------------------------------------------|---------------------------------------|-------|
| playwright          | Enabled (headed)                 | ✅ (auto via sync script; headed)           | ✅ (settings.json pattern)            | Uses PLAYWRIGHT_BROWSERS_PATH, DISPLAY, HOME |
| web-search (Tavily) | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires TAVILY_API_KEY env |
| context7            | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires CONTEXT7_API_KEY/URL env |
| browser             | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (doc’d, manual add)                | Headed via DISPLAY/PLAYWRIGHT_BROWSERS_PATH |
| filesystem          | Disabled                         | ✅ (auto via sync script; currently disabled) | ✖️                                    | Generic fs server; enable as needed |
| chrome-devtools     | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (manual pattern)                  | Needs running Chrome with remote debugging |

<!-- section_id: "8c35bfab-d9b5-474a-94d6-922229407fdf" -->
## How to switch/disable/enable (Codex)
- Use `codex_mcp_sync.py --env <env> [--disable <servers...>]`
  - Active snippet: `~/.codex/environments/<env>.toml`
  - Full snippet: `~/.codex/environments/<env>.full.toml`
  - Disabled snippet: `~/.codex/environments/<env>.disabled.toml`
  - Backup: `~/.codex/config.toml.bak`
- Restart Codex CLI after sync.

<!-- section_id: "076cce0e-f247-4246-8820-0080f71fb6ac" -->
## Gemini reference
- Single canonical file: `~/.gemini/settings.json` with `mcpServers` entries (see core-system/README.md and GEMINI CLI sections).

<!-- section_id: "71d701eb-de27-419a-bf2e-9470fb9eb7b1" -->
## To add another tool
- Add its server block to the presets in `automation/scripts/codex_mcp_sync.py` (and, if desired, document Gemini settings.json pattern).
- Rerun the sync script to regenerate Codex config and snippets.
