---
resource_id: "842a2fb4-24ec-42fc-8b80-9bbc1c696275"
resource_type: "readme
document"
resource_name: "README"
---
# Gemini CLI MCP Setup

<!-- section_id: "c9457206-2053-4e68-8064-e8e87212e523" -->
## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

<!-- section_id: "5dc87334-abff-418e-b356-de1626c326c7" -->
## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

<!-- section_id: "8afbf82d-0544-46de-a30d-77bc2b1e4765" -->
## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

<!-- section_id: "7b541376-679a-4389-afa3-8964b9a7de54" -->
## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
