---
resource_id: "ffe28ca7-28a1-4d5c-850d-55bc3e5fff43"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

<!-- section_id: "bb8672fd-3826-478a-8090-00f78f1941fe" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "596936dc-21bd-4909-ae70-6cc0ea04c6c8" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "7d8ef00e-1efd-4ad0-ae03-5f3d5826bd25" -->
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

<!-- section_id: "c9fb1e31-b77a-40ef-8e55-39c8ac708a1a" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "85b3c556-beaa-4f1f-a980-9b43d15dd1c5" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "908bb851-7e8c-479f-b124-75dc012d4532" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "2b0f59b8-4998-4538-ac4d-2b7897eca2ce" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
