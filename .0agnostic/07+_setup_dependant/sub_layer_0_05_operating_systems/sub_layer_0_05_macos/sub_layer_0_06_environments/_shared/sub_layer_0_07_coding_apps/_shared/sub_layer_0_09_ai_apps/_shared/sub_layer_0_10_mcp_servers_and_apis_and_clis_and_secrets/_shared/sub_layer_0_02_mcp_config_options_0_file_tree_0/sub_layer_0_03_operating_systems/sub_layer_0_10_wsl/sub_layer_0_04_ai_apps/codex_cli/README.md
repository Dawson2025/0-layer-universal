---
resource_id: "7d421913-0024-4a28-9daa-577669744271"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

<!-- section_id: "8866d0f3-c85c-446f-bbab-3ee9ef2d7d2e" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "cf89c512-ecb2-4e16-976f-0b802d3331d0" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "aee527ec-4947-4dd6-a5d3-5aab8a44a384" -->
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

<!-- section_id: "55f2db1f-b499-47be-aa2a-c45d8e7684b6" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "2122d59e-c24f-468c-92f3-6576ba26b51a" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "d7bfcf1c-9e3a-40b4-9ee1-a4a01beb014a" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "e75fca53-7422-474c-900d-9894b409b6ba" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
