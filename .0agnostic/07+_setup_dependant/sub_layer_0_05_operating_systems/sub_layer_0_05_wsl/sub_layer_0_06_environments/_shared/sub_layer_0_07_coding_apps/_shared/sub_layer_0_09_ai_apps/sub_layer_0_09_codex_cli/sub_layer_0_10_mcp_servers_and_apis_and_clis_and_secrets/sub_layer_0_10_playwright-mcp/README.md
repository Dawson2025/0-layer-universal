---
resource_id: "be3a52da-f916-44d6-8678-67d034fc1ddd"
resource_type: "readme
document"
resource_name: "README"
---
# Playwright MCP (Codex CLI on WSL/WSLg)

<!-- section_id: "70c394ba-3983-4303-9460-408c57e38c08" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "617bf040-e77e-4d35-9c14-35ec5710f83a" -->
## WSL/WSLg requirements (headed)
- Ensure WSLg runtime env is present in the MCP server process:
  - `DISPLAY=:0`
  - `WAYLAND_DISPLAY=wayland-0`
  - `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`
- Prefer Playwright MCP `--config` JSON with:
  - `isolated: true` (avoids “browser already in use” profile locks)
  - `launchOptions.headless: false`
  - `launchOptions.args`: `["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]`
  - `launchOptions.executablePath`: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

<!-- section_id: "9074ba51-265a-4bf9-a2e2-30390604cf25" -->
## Open a visible browser (WSL Codex CLI)

1. Ensure WSLg exists:
   ```bash
   test -d /mnt/wslg/runtime-dir && echo "WSLg OK"
   ```
2. Apply the Codex MCP sync (headed/default):
   ```bash
   cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
   python3 codex_mcp_sync.py --env development
   ```
3. Restart Codex CLI, then use Playwright MCP tools; Chromium should open visibly.

If the server fails to start, check for:
- `--headless=false` anywhere in your config (remove it; headed is default).
- Missing WSLg (`/mnt/wslg/runtime-dir`), in which case use `--headless` or a Windows-visible browser fallback.

<!-- section_id: "cacc1af3-e353-4d1e-a841-2d903bb6df1d" -->
## Codex integration
- Use `0.06_automation/scripts/codex_mcp_sync.py` to generate `~/.codex/config.toml` and the Playwright config file under `~/.codex/`.

<!-- section_id: "2cef4b74-ab34-4b27-b567-ba0a9efaf48f" -->
## Concurrent Browser Setup (NEW)

To enable **simultaneous** Playwright MCP browser use in both Codex CLI and other AI tools (Claude Code, Gemini):

```bash
# Navigate to automation scripts
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

# Set up OS+tool-specific concurrent browser configs (auto-detects OS)
python3 mcp_concurrent_browser.py setup --tools codex claude

# Update Codex CLI config to use the OS+tool-specific Playwright config
python3 mcp_concurrent_browser.py apply-codex

# Verify setup (WSL)
python3 mcp_concurrent_browser.py status --os wsl
```

**What this does:**
- Creates `~/.codex/playwright.wsl_codex.json` (WSL + Codex config)
- Assigns unique browser profile directory: `~/.cache/ms-playwright/mcp-chromium-wsl-codex`
- Updates `~/.codex/config.toml` to reference the OS+tool config
- Enables concurrent browser use across AI tools

**Documentation:** See [CONCURRENT_BROWSER_SETUP.md](../../../../../../0.06_automation/CONCURRENT_BROWSER_SETUP.md)
