---
resource_id: "c1bacc23-0300-4b62-b049-c3d638bb02fe"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup

<!-- section_id: "db441d41-09f0-4d93-89ca-301c4c8fa631" -->
## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

<!-- section_id: "772e05f9-97b6-45ba-b3c6-9ab966880b0f" -->
## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

<!-- section_id: "c2a0524c-47e9-4e2c-95c6-a626b35838e0" -->
## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

<!-- section_id: "67bd8d27-b139-4015-98fb-7912195fc851" -->
## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
