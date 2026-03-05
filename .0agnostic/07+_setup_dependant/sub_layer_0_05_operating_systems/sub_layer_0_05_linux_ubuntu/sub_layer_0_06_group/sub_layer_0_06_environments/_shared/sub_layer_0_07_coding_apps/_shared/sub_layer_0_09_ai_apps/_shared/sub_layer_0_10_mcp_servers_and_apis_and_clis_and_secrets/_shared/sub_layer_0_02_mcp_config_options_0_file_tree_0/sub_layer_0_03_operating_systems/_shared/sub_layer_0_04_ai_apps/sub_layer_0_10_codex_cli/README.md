---
resource_id: "86c47180-fafd-4271-9d18-2452d13e15d5"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup

## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
