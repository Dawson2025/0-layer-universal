---
resource_id: "a716a470-607c-49eb-8712-64b156880bd3"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup

<!-- section_id: "58425ed2-8f3b-4f58-b2d9-6a16cfdb7bbe" -->
## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

<!-- section_id: "dca76e37-a7ea-4aa3-b88c-9e941505db36" -->
## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

<!-- section_id: "da3ae4ec-7a1d-4b07-a6cc-71a65fc06852" -->
## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

<!-- section_id: "ada70b89-6ce5-49ab-9410-6e9c90ada949" -->
## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
