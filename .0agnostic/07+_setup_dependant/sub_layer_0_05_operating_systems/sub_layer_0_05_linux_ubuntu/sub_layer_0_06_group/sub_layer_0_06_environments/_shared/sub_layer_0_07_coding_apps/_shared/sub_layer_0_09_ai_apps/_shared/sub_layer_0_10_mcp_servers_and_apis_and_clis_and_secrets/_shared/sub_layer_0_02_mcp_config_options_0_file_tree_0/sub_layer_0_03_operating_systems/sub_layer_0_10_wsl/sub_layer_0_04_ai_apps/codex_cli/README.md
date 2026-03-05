---
resource_id: "05c2ded3-a812-4b2f-bb41-96212076bf0d"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

## Config location
- `~/.codex/config.toml`

## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

### Quickstart (headed, visible browser)
```bash
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
python3 codex_mcp_sync.py --env development
```
Restart Codex CLI after running the sync.

Key requirements for headed browser on WSLg:
- Inject WSLg env vars into the MCP server process:
  - `DISPLAY=:0`
  - `WAYLAND_DISPLAY=wayland-0`
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
- Use Playwright MCP `--config` JSON to set:
  - `launchOptions.headless=false`
  - `launchOptions.args=["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]`
  - `isolated=true` to avoid profile lock
  - `executablePath` pointing at `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
