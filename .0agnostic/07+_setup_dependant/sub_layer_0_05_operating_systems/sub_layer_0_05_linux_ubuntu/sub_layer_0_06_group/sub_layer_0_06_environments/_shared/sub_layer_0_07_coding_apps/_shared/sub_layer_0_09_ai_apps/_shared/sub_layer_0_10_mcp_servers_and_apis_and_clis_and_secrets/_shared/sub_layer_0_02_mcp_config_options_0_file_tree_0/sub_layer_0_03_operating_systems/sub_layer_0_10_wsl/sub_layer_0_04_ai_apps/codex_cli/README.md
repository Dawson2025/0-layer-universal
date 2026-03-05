---
resource_id: "05c2ded3-a812-4b2f-bb41-96212076bf0d"
resource_type: "readme
document"
resource_name: "README"
---
# Codex CLI MCP Setup (WSL)

<!-- section_id: "b4fea747-80c1-4aff-992c-1cfd1ad8ef34" -->
## Config location
- `~/.codex/config.toml`

<!-- section_id: "25782a44-6285-4426-a4fe-b93b26563380" -->
## Recommended setup (WSLg headed Playwright)
Use the Codex sync automation:
- `automation/scripts/codex_mcp_sync.py`

<!-- section_id: "a12faca9-76d0-4a2c-9b16-40d9ebc1bfa8" -->
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

<!-- section_id: "36acedcb-4285-4a39-ac29-3bda285fdc17" -->
### If no WSLg (no visible Linux GUI browser)
If `/mnt/wslg/runtime-dir` does not exist, you will not get a visible headed browser from WSL.

Options:
- Use Playwright MCP headless:
  ```bash
  python3 codex_mcp_sync.py --env development --headless
  ```
- Use a Windows-visible browser:
  - Start Windows Chrome with remote debugging and use `chrome-devtools-mcp` from WSL.

<!-- section_id: "f7c9a62f-db64-4f99-8ec2-b7cefc29a237" -->
## Secrets
Put API keys in `~/.codex/mcp.env` and re-run the sync:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```

<!-- section_id: "745c0155-b899-44e2-90fb-e3ef77f781ff" -->
## Disable/enable servers
- Disable: `codex_mcp_sync.py --disable <servers...>`
- Re-enable: rerun without disabling (or restore from `~/.codex/environments/<env>.full.toml`)

<!-- section_id: "473f3cd9-3979-44d8-b032-93a45c48693f" -->
## Server notes
See `0.05_mcp_servers/` in this folder for Codex-on-WSL notes per server (mirrors the top-level server list).
