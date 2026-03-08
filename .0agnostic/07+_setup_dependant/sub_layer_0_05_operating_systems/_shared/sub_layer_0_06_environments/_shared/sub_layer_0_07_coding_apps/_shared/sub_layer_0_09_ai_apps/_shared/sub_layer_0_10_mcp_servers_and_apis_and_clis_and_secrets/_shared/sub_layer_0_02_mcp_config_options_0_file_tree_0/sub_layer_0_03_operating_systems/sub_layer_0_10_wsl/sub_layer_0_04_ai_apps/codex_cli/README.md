---
resource_id: "3627de7e-f656-46ac-9b77-54dd897d106d"
resource_type: "readme_document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

<!-- section_id: "07d410e6-11c6-4e3a-b5af-0a9d8cfef0fe" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "ebe56413-4124-4a41-bbe2-84e7380e4e2f" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "c891b608-a3e4-4c31-9ec0-1f359b46d2a8" -->
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

<!-- section_id: "1cbd840a-c45b-45dd-a790-229cb49779ec" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "66146f07-13ba-4f0c-a77e-bb19e9b6d421" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "1581f2d8-3330-46fb-b4b0-4c98f078c924" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "89972fa0-4323-4d16-a3cd-71b96cb1e802" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
