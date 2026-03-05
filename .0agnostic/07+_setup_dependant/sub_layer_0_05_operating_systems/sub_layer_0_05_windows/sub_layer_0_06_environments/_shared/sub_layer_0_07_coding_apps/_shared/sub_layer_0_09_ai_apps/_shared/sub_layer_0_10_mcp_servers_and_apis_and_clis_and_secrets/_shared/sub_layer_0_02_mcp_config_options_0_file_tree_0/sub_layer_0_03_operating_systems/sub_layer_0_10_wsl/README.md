---
resource_id: "ecc56972-4362-4b61-a429-3bd6c8e267a5"
resource_type: "readme
document"
resource_name: "README"
---
# WSL (Windows Subsystem for Linux) MCP Notes

<!-- section_id: "5ce22609-6351-4082-a239-1cf4623c2a93" -->
## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

<!-- section_id: "0856d3b3-3385-4693-a2fa-3b8188d823a0" -->
## Key prerequisites
- **WSLg enabled** for headed browser visibility (required if you want a visible Chromium window from WSL):
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

<!-- section_id: "1ab71f68-1b84-4509-a07f-920915c94ff0" -->
## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Do **not** use `--headless=false` (newer `@playwright/mcp` versions reject it).
- **CRITICAL**: Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- **See**: `0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

<!-- section_id: "333b02c4-228b-49f4-987c-7f40aaa91906" -->
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

<!-- section_id: "8ea7f7f5-4ad6-46a7-9d25-90f6db235940" -->
## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.
