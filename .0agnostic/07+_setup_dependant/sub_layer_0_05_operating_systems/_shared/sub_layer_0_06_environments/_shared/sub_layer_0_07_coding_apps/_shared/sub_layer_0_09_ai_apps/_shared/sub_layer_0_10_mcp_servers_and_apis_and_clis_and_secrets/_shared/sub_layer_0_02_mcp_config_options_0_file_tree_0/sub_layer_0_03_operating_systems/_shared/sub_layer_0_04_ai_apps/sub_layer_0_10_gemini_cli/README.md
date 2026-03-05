---
resource_id: "9e05300e-308e-4fd8-bc32-42060ada0e05"
resource_type: "readme
document"
resource_name: "README"
---
# Gemini CLI MCP Setup

## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
