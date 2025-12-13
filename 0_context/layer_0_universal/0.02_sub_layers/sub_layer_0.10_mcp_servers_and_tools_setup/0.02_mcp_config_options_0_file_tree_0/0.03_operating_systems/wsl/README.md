# WSL (Windows Subsystem for Linux) MCP Notes

## Scope
Use this when running AI CLIs inside WSL (Ubuntu) and using MCP servers (especially Playwright/browser automation).

## Key prerequisites
- WSLg enabled for headed browser visibility:
  - `/mnt/wslg` exists
  - `WAYLAND_DISPLAY` set (often `wayland-0`)
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
  - `DISPLAY` typically `:0`
- For Playwright MCP, ensure:
  - `PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright`
  - Node/NPM available (often via NVM)

## Critical browser automation findings (WSLg)
- Playwright MCP is headed by default; use `--headless` to force headless.
- Headed Chromium can crash on WSLg unless launched with Wayland/Ozone flags:
  - `--ozone-platform=wayland`
  - `--enable-features=UseOzonePlatform`
- Avoid browser profile lock issues by using Playwright MCP `isolated` mode.

## Runbooks
See `0.04_ai_apps/` for per-app MCP setup instructions on WSL.
