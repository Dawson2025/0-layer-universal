---
resource_id: "3e620a21-b811-45eb-9893-3726ad5274d3"
resource_type: "readme_document"
resource_name: "README"
---
# Gemini CLI MCP Setup

<!-- section_id: "a8e2efa9-fe5f-4fcf-b050-392e768fb51c" -->
## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

<!-- section_id: "cf5c4487-9c17-443a-b2d0-e75576050640" -->
## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

<!-- section_id: "cf0f6925-85cd-4a9c-ac63-bdfe52f135af" -->
## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

<!-- section_id: "124fc7fc-63c5-47b1-a6c8-b501939ae6fd" -->
## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
