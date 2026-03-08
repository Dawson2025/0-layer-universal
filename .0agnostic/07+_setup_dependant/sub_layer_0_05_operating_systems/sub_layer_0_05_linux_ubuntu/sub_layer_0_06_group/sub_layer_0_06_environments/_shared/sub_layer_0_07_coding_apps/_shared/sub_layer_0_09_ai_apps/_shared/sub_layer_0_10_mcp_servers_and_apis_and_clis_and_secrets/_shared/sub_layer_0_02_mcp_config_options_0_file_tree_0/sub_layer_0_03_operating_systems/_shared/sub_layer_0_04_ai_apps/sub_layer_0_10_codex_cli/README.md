---
resource_id: "86c47180-fafd-4271-9d18-2452d13e15d5"
resource_type: "readme_document"
resource_name: "README"
---
# Codex CLI MCP Setup

<!-- section_id: "344e6933-e7c3-4340-ae6c-ea76b7608b03" -->
## Config location
- `~/.codex/config.toml` (`[mcp_servers.*]` blocks)

<!-- section_id: "ce2c058d-7312-4920-8304-6625696bb709" -->
## Automation (recommended)
- Sync/generate: `../../../../../../0.06_automation/scripts/codex_mcp_sync.py`
- Documentation: `../../../../../../0.01_core-system/CODEX_CLI_MCP_SETUP.md`

<!-- section_id: "9b17eb53-c964-4d14-bc40-a346af6a0432" -->
## WSLg headed browser notes (Playwright)
- On WSLg, headed Chromium may crash unless Playwright is launched with Wayland/Ozone args.
- The Codex sync script writes a Playwright MCP config file (e.g. `~/.codex/playwright.<env>.json`) and points Playwright MCP to it via `--config`.

<!-- section_id: "cc7109cf-b57c-42bf-a911-4cbecc8d7be8" -->
## Disable/re-enable servers
- Use `codex_mcp_sync.py --disable <servers...>`; disabled servers are saved in `~/.codex/environments/<env>.disabled.toml` and can be re-enabled by re-running without disabling them.
