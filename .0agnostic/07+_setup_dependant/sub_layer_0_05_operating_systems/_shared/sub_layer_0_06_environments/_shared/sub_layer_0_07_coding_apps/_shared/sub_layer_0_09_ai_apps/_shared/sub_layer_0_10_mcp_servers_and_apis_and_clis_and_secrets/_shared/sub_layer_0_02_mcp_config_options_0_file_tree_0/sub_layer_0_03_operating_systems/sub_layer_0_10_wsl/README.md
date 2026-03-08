---
resource_id: "e241bc52-eee6-4b82-9e58-7150e2b9374b"
resource_type: "readme_document"
resource_name: "README"
---
# WSL (Windows Subsystem for Linux) MCP Notes

<!-- section_id: "eb627e8c-79c2-4069-bf3d-989ef14474b1" -->
## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

<!-- section_id: "4f3c90a7-b687-4117-a853-d56a1f553a2b" -->
## Key prerequisites
- **WSLg enabled** for headed browser visibility (required if you want a visible Chromium window from WSL):
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

<!-- section_id: "6c1138f7-ddf3-4276-8d9a-3c29f43b1c91" -->
## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Do **not** use `--headless=false` (newer `@playwright/mcp` versions reject it).
- **CRITICAL**: Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- **See**: `0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

<!-- section_id: "9c403269-c767-432d-8e4a-3de11f87210c" -->
## Quickstart: visible browser from WSL (Codex CLI)

1. Confirm WSLg is present:
   ```bash
   test -d /mnt/wslg/runtime-dir && echo "WSLg OK" || echo "WSLg missing (use headless or Windows Chrome fallback)"
   ```
2. Configure Codex CLI MCP (headed):
   ```bash
   cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
   python3 codex_mcp_sync.py --env development
   ```
3. Restart Codex CLI.
4. Use the Playwright MCP tools from Codex; the browser should open visibly (WSLg window).

If you do not have WSLg, you cannot open a visible Linux GUI browser from WSL. Use:
- Playwright MCP **headless** (`codex_mcp_sync.py --headless`) and rely on screenshots/logs, or
- A **Windows-visible** browser via DevTools (see `chrome-devtools-mcp` in the Codex WSL runbook).

<!-- section_id: "b7d501b1-97d3-4b11-9847-5f34dde5814f" -->
## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.
