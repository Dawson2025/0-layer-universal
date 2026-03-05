---
resource_id: "10218691-0df8-42ea-a057-51ad0141cfe3"
resource_type: "readme
document"
resource_name: "README"
---
# WSL (Windows Subsystem for Linux) MCP Notes

<!-- section_id: "ffb1cd36-28f2-4332-81eb-45e8e2b5f34e" -->
## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

<!-- section_id: "b880ee6b-2201-41a5-9462-fe73f177eecb" -->
## Key prerequisites
- **WSLg enabled** for headed browser visibility (required if you want a visible Chromium window from WSL):
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

<!-- section_id: "f8fa435e-00e7-4f09-91c7-68d6a89e1127" -->
## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Do **not** use `--headless=false` (newer `@playwright/mcp` versions reject it).
- **CRITICAL**: Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- **See**: `0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

<!-- section_id: "e8eaad1c-cd71-4717-8e6b-9553783c3397" -->
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

<!-- section_id: "e8a82c3c-5666-475e-b7d4-66ba22351a91" -->
## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.

---

<!-- section_id: "e89128a3-1ab0-452f-82d3-2610d268d2aa" -->
## Legacy MCP Source

# WSL (Windows Subsystem for Linux) MCP Notes

<!-- section_id: "97732921-9a1e-4ed0-b2a4-cdff105b9eb8" -->
## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

<!-- section_id: "bde290f0-4cb5-48ac-ada1-dac2220144b9" -->
## Key prerequisites
- **WSLg enabled** for headed browser visibility (required if you want a visible Chromium window from WSL):
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

<!-- section_id: "9ab98d06-6149-40ff-8511-60db6f9a8019" -->
## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Do **not** use `--headless=false` (newer `@playwright/mcp` versions reject it).
- **CRITICAL**: Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- **See**: `0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for complete setup instructions
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

<!-- section_id: "58f2fe0d-6104-4961-83a9-9ea40da62e64" -->
## Quickstart: visible browser from WSL (Codex CLI)

1. Confirm WSLg is present:
   ```bash
   test -d /mnt/wslg/runtime-dir && echo "WSLg OK" || echo "WSLg missing (use headless or Windows Chrome fallback)"
   ```
2. Configure Codex CLI MCP (headed):
   ```bash
   cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
   python3 codex_mcp_sync.py --env development
   ```
3. Restart Codex CLI.
4. Use the Playwright MCP tools from Codex; the browser should open visibly (WSLg window).

If you do not have WSLg, you cannot open a visible Linux GUI browser from WSL. Use:
- Playwright MCP **headless** (`codex_mcp_sync.py --headless`) and rely on screenshots/logs, or
- A **Windows-visible** browser via DevTools (see `chrome-devtools-mcp` in the Codex WSL runbook).

<!-- section_id: "2d12b46a-202a-4165-9860-e1e2b131cd47" -->
## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.
