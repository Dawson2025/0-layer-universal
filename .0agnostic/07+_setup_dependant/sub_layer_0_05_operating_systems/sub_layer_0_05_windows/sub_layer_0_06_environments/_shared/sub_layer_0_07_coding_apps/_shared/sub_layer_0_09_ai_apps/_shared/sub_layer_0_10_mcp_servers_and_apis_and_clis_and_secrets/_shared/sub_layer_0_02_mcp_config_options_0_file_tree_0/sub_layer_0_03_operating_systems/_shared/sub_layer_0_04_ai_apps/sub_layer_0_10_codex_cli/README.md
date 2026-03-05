---
resource_id: "1661c616-aee0-424a-9a69-1ec40b163449"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup

<!-- section_id: "d578a615-f64d-4528-a0c8-14ba5f01ccbc" -->
## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

<!-- section_id: "02c3c664-5005-434d-a0de-304a8ef9ac90" -->
## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

<!-- section_id: "60314892-cfb7-4a0d-97e1-197ae2ddb9a7" -->
## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

<!-- section_id: "a866a145-1f06-49d5-a283-77f2a38f43eb" -->
## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
