---
resource_id: "3fcc4aab-21be-447d-b347-352dbea79eed"
resource_type: "readme
document"
resource_name: "README"
---
# Gemini CLI MCP Setup

<!-- section_id: "a167b2c1-55d5-4fc1-b9fc-a88ec726643f" -->
## Config location
- `~/.gemini/settings.json` (single canonical file; contains `mcpServers`)

<!-- section_id: "55a48ec5-5d6d-4c58-a9e9-be275f0f75f3" -->
## Recommended pattern (universal MCP wrappers)
- Generate wrapper scripts with: `../../../../../../0.06_automation/scripts/mcp_manager.py --scope user`
- Gemini typically points to the generated wrappers under `~/.config/mcp/servers/` (e.g., `mcp-playwright-generic.sh`).

<!-- section_id: "4ed86d43-8361-4518-9416-4c04763d8b4a" -->
## WSL/WSLg notes (Playwright)
- Playwright MCP is headed by default; use `--headless` for headless.
- On WSLg, headed Chromium may require Wayland/Ozone flags; prefer `--config` JSON with `launchOptions.args` set accordingly.

<!-- section_id: "f6426e99-e1c6-472e-9f01-3a9cff5c71cc" -->
## References
- `../../../../../../0.06_automation/README.md`
- `0.05_mcp_servers/playwright-mcp/INSTALL.md`
- `../../../../../../0.01_core-system/README.md`
