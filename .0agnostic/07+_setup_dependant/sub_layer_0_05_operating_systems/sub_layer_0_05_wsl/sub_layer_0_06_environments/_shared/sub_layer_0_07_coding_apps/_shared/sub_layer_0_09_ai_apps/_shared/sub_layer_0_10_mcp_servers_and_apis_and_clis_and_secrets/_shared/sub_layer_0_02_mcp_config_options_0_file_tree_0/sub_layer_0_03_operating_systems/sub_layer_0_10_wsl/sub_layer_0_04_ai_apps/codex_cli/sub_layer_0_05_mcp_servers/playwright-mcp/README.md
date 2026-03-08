---
resource_id: "955b55ff-5e22-4956-9676-2ffeb9ee99b2"
resource_type: "readme_document"
resource_name: "README"
---
# Playwright MCP (Codex CLI on WSL/WSLg)

<!-- section_id: "c7b74eed-4175-4b1b-9f59-af8aac261663" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "d6aec01b-7dbe-4c0d-91f4-81b9d72cfade" -->
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

<!-- section_id: "25a7a866-029e-4389-a1ca-e60a93fbbea9" -->
## Open a visible browser (WSL Codex CLI)

1. Ensure WSLg exists:
   ```bash
   test -d /mnt/wslg/runtime-dir && echo "WSLg OK"
   ```
2. Apply the Codex MCP sync (headed/default):
   ```bash
   cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts
   python3 codex_mcp_sync.py --env development
   ```
3. Restart Codex CLI, then use Playwright MCP tools; Chromium should open visibly.

If the server fails to start, check for:
- `--headless=false` anywhere in your config (remove it; headed is default).
- Missing WSLg (`/mnt/wslg/runtime-dir`), in which case use `--headless` or a Windows-visible browser fallback.

<!-- section_id: "5b7d27b9-8fc6-4116-815d-fa8d91a8f9ee" -->
## Codex integration
- Use `0.06_automation/scripts/codex_mcp_sync.py` to generate `~/.codex/config.toml` and the Playwright config file under `~/.codex/`.

<!-- section_id: "344c7cd6-57c6-4a20-b2b0-d1d9d3d4d53a" -->
## Concurrent Browser Setup (NEW)

To enable **simultaneous** Playwright MCP browser use in both Codex CLI and other AI tools (Claude Code, Gemini):

```bash
# Navigate to automation scripts
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

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

---

<!-- section_id: "f38c5678-9465-4802-a665-e71f0caccd2b" -->
## Legacy MCP Source

# Playwright MCP (Codex CLI on WSL/WSLg)

<!-- section_id: "5f328e33-6cb7-4483-8c24-f78265c510ec" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "41524303-814f-4cc2-b30f-bf0e5bca6ff9" -->
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

<!-- section_id: "ae3e4788-fbe1-4f57-bc16-bd8ecb11df68" -->
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

<!-- section_id: "0091fa61-56ca-4b7c-9809-dfd3442218da" -->
## Codex integration
- Use `0.06_automation/scripts/codex_mcp_sync.py` to generate `~/.codex/config.toml` and the Playwright config file under `~/.codex/`.

<!-- section_id: "1a584ce8-1caa-4e3c-acd2-db4957370f49" -->
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
