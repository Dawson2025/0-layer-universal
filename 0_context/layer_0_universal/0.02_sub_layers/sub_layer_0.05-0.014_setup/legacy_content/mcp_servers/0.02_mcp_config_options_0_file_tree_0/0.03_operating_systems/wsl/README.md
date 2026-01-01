# WSL (Windows Subsystem for Linux) MCP Notes

## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

## Key prerequisites
- **WSLg enabled** for headed browser visibility (required if you want a visible Chromium window from WSL):
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Do **not** use `--headless=false` (newer `@playwright/mcp` versions reject it).
- **CRITICAL**: Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- **See**: `0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

## Quickstart: visible browser from WSL (Codex CLI)

1. Confirm WSLg is present:
   ```bash
   test -d /mnt/wslg/runtime-dir && echo "WSLg OK" || echo "WSLg missing (use headless or Windows Chrome fallback)"
   ```
2. Configure Codex CLI MCP (headed):
   ```bash
   cd /home/dawson/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.10_mcp_servers_and_tools_setup/0.06_automation/scripts
   python3 codex_mcp_sync.py --env development
   ```
3. Restart Codex CLI.
4. Use the Playwright MCP tools from Codex; the browser should open visibly (WSLg window).

If you do not have WSLg, you cannot open a visible Linux GUI browser from WSL. Use:
- Playwright MCP **headless** (`codex_mcp_sync.py --headless`) and rely on screenshots/logs, or
- A **Windows-visible** browser via DevTools (see `chrome-devtools-mcp` in the Codex WSL runbook).

## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.
