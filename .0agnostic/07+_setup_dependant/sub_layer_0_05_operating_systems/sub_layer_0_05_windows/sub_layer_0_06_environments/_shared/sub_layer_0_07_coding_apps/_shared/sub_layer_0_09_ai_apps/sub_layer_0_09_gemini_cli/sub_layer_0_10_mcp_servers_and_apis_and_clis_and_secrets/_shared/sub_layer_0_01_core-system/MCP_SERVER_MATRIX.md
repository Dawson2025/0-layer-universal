---
resource_id: "0149b228-ed89-49a6-81e8-d0d6d4d6394f"
resource_type: "document"
resource_name: "MCP_SERVER_MATRIX"
---
# MCP Server Matrix (with tool automation coverage)

Lists all MCP servers we have configs for, plus which AI tools/CLIs have automation or documented setup. Disabled servers remain listed for visibility.

See `BROWSER_MCP_ROUTING_TABLE.md` for recommendations on which browser server to use per CLI/OS/task.

<!-- section_id: "70d8efda-85c3-44e2-afd5-a8f136a28596" -->
## Legend
- ✅ Automated / documented working setup
- ⚠️ Manual setup documented but not automated
- ✖️ Not configured

<!-- section_id: "044f2ca5-11a7-4253-8620-2519c071ff8e" -->
## Servers
| Server              | Status (Codex env: development) | Codex CLI (config.toml / codex_mcp_sync.py) | Gemini CLI (~/.gemini/settings.json) | Notes |
|---------------------|----------------------------------|--------------------------------------------|---------------------------------------|-------|
| playwright          | Enabled (headed)                 | ✅ (auto via sync script; headed)           | ✅ (settings.json pattern)            | Uses PLAYWRIGHT_BROWSERS_PATH, DISPLAY, HOME |
| web-search (Tavily) | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires TAVILY_API_KEY env |
| context7            | Enabled                          | ✅ (auto via sync script)                  | ⚠️ (doc’d, manual add)                | Requires CONTEXT7_API_KEY/URL env |
| browser             | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (doc’d, manual add)                | Headed via DISPLAY/PLAYWRIGHT_BROWSERS_PATH |
| filesystem          | Disabled                         | ✅ (auto via sync script; currently disabled) | ✖️                                    | Generic fs server; enable as needed |
| chrome-devtools     | Disabled                         | ✅ (auto via sync script; currently disabled) | ⚠️ (manual pattern)                  | Needs running Chrome with remote debugging |

<!-- section_id: "3ee8df74-2e5e-4270-8638-71324891a316" -->
## How to switch/disable/enable (Codex)
- Use `codex_mcp_sync.py --env <env> [--disable <servers...>]`
  - Active snippet: `~/.codex/environments/<env>.toml`
  - Full snippet: `~/.codex/environments/<env>.full.toml`
  - Disabled snippet: `~/.codex/environments/<env>.disabled.toml`
  - Backup: `~/.codex/config.toml.bak`
- Restart Codex CLI after sync.

<!-- section_id: "251649e6-71d8-45d9-8664-463822401baa" -->
## Gemini reference
- Single canonical file: `~/.gemini/settings.json` with `mcpServers` entries (see core-system/README.md and GEMINI CLI sections).

<!-- section_id: "c6df7561-4952-477c-89a7-c7e573a0b626" -->
## To add another tool
- Add its server block to the presets in `automation/scripts/codex_mcp_sync.py` (and, if desired, document Gemini settings.json pattern).
- Rerun the sync script to regenerate Codex config and snippets.
