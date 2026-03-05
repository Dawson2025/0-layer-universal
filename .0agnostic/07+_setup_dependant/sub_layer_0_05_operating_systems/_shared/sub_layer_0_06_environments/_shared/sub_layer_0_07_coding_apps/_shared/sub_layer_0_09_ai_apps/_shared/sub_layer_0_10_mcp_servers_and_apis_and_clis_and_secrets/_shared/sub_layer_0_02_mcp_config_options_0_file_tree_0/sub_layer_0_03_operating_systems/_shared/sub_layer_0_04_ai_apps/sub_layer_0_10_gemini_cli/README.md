---
resource_id: "9e05300e-308e-4fd8-bc32-42060ada0e05"
resource_type: "readme
document"
resource_name: "README"
---
# Gemini CLI MCP Setup

<!-- section_id: "4b84204d-cfd2-45ce-9987-9dd8aaac7eb9" -->
## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

<!-- section_id: "827033f6-ae22-40a2-ba76-93c05d5e339c" -->
## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

<!-- section_id: "02af4cc6-956e-4bcc-8177-bd5bf7509792" -->
## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

<!-- section_id: "eb01c5f7-27de-499f-bc84-e96550f8724a" -->
## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
