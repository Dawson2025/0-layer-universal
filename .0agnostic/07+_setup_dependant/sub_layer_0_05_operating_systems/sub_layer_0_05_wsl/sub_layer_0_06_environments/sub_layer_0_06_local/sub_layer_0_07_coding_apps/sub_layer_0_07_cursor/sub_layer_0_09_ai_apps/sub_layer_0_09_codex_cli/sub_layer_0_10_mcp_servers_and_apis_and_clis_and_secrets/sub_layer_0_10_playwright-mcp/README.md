---
resource_id: "90c77700-8d2d-4f74-9d48-0fc68515a792"
resource_type: "readme_document"
resource_name: "README"
---
# Playwright MCP (Codex CLI on WSL/WSLg)

<!-- section_id: "9ddfa22a-5c45-4553-9d5e-5cb625f2762f" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "d0cf832e-8e8c-43b1-982d-8ba0408610cb" -->
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

<!-- section_id: "2c05af4b-f1de-40f2-9a37-e1eefeca4a73" -->
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

<!-- section_id: "9c7c413c-5081-4a8a-84bb-c6af41275f5f" -->
## Codex integration
- Use `0.06_automation/scripts/codex_mcp_sync.py` to generate `~/.codex/config.toml` and the Playwright config file under `~/.codex/`.

<!-- section_id: "e841825b-7a20-45df-81b9-e299f0f4e2c0" -->
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
