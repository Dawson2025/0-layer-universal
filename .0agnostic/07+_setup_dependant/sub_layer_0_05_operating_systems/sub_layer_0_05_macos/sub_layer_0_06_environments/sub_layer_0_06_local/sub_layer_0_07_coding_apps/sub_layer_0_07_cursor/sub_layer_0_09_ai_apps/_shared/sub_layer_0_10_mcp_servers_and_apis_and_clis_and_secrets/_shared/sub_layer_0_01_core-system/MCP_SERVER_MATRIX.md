---
resource_id: "08b83e80-f33c-476a-b0a7-656ffd0217d2"
resource_type: "document"
resource_name: "MCP_SERVER_MATRIX"
---
# MCP Server Matrix (with tool automation coverage)

Lists all MCP servers we have configs for, plus which AI tools/CLIs have automation or documented setup. Disabled servers remain listed for visibility.

See `BROWSER_MCP_ROUTING_TABLE.md` for recommendations on which browser server to use per CLI/OS/task.

<!-- section_id: "b1606f01-f2f3-4108-a9eb-b62b8a13a889" -->
## Legend
- ✅ Automated / documented working setup
- ⚠️ Manual setup documented but not automated
- ✖️ Not configured

<!-- section_id: "32e2572a-453c-4251-a235-b7a9ece3012b" -->
## Servers
| Server              | Status (Codex env: development) | Codex CLI (config.toml / codex_mcp_sync.py) | Gemini CLI (~/.gemini/settings.json) | Notes |
|---------------------|----------------------------------|--------------------------------------------|---------------------------------------|-------|
| playwright          | Enabled (headed)                 | ✅ (auto via sync script; headed)           | ✅ (settings.json pattern)            | Uses PLAYWRIGHT_BROWSERS_PATH, DISPLAY, HOME |
| web-search (Tavily) | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires TAVILY_API_KEY env |
| context7            | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires CONTEXT7_API_KEY/URL env |
| browser             | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (doc’d, manual add)                | Headed via DISPLAY/PLAYWRIGHT_BROWSERS_PATH |
| filesystem          | Disabled                         | ✅ (auto via sync script; currently disabled) | ✖️                                    | Generic fs server; enable as needed |
| chrome-devtools     | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (manual pattern)                  | Needs running Chrome with remote debugging |

<!-- section_id: "a5d07624-7c0d-426e-ad15-8d7cd6243b2a" -->
## How to switch/disable/enable (Codex)
- Use `codex_mcp_sync.py --env <env> [--disable <servers...>]`
  - Active snippet: `~/.codex/environments/<env>.toml`
  - Full snippet: `~/.codex/environments/<env>.full.toml`
  - Disabled snippet: `~/.codex/environments/<env>.disabled.toml`
  - Backup: `~/.codex/config.toml.bak`
- Restart Codex CLI after sync.

<!-- section_id: "bd9088ef-5a21-4175-a89c-ce25fcc65989" -->
## Gemini reference
- Single canonical file: `~/.gemini/settings.json` with `mcpServers` entries (see core-system/README.md and GEMINI CLI sections).

<!-- section_id: "545b385f-58e3-4ed6-ae6b-04cc75bf53b4" -->
## To add another tool
- Add its server block to the presets in `automation/scripts/codex_mcp_sync.py` (and, if desired, document Gemini settings.json pattern).
- Rerun the sync script to regenerate Codex config and snippets.
