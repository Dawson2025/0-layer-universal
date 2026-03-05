---
resource_id: "cc2e3f1a-14cf-4c15-9aa1-691f3b3e2dc5"
resource_type: "readme
document"
resource_name: "README"
---
# Gemini CLI MCP Setup

<!-- section_id: "aac669ad-c12b-4671-bc6f-e533c62cca41" -->
## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

<!-- section_id: "1065144d-d735-4e0b-abd9-99045605fce7" -->
## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

<!-- section_id: "db9962d3-e77c-4c52-934d-acda1a651298" -->
## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

<!-- section_id: "3c67cfba-08e3-47c5-bbb4-f3f31e79ca68" -->
## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
