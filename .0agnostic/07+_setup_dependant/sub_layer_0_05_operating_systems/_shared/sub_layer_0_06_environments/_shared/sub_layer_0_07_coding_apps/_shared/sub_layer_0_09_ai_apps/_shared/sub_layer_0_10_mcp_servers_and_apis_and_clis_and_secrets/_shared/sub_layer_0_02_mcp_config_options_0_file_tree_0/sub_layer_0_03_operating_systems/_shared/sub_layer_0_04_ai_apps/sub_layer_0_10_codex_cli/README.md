---
resource_id: "0550713d-3827-4082-a965-027138c8e6e2"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup

<!-- section_id: "41cbe9bc-19e2-4f73-966d-aa26333e834c" -->
## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

<!-- section_id: "06f039e8-02bf-47ea-8b19-f026c2e474ab" -->
## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

<!-- section_id: "66481797-1033-4888-8a65-a6f9a9e031f8" -->
## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

<!-- section_id: "ce5b5b96-bc81-416b-a383-f48ab3b2b547" -->
## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
