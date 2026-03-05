---
resource_id: "96eb1cf9-b6ee-483e-b1d3-fd6d9c23fdcd"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

<!-- section_id: "2011dbd9-3e3b-4212-adc7-310f40e98b07" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "9b57802d-c66b-4fca-bccb-2b940b32c15b" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "a5f102a1-0a9b-4d5b-8214-bf29ff7e5e4f" -->
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

<!-- section_id: "db241f56-bd50-4a56-b086-6be77ba2e4f3" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "43603835-db0e-47ad-91f2-68534243f969" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "a9634a0a-1a2d-4bf1-93c3-1e4672b072e8" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "000c3c90-0908-431c-b9af-3f7f489b2c65" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).

---

<!-- section_id: "dab316c3-8004-4304-b5be-db5e3005fc48" -->
## Legacy MCP Source

# Codex CLI MCP Setup (WSL)

<!-- section_id: "49d9d392-1ccd-4210-bea1-44acbb83df7a" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "93099ae4-9ba5-48f4-9b2b-652ac5d5ad20" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "a44ab901-f563-483e-af10-67cd1630e719" -->
### Quickstart (headed, visible browser)
```bash
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
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

<!-- section_id: "93dd5255-3c32-444f-b948-37113e930424" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "1dca96a0-8a03-45ec-af02-5939a081f256" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "8c1985e2-97bd-462c-b7dd-59a19d81f559" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "c324c575-8cc2-4a2f-b318-8e15a72b984d" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
