# Gemini CLI MCP Setup

## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

## References
- `automation/README.md`
- `mcp_servers/playwright-mcp/INSTALL.md`
- `core-system/README.md` (Gemini `settings.json` section)
