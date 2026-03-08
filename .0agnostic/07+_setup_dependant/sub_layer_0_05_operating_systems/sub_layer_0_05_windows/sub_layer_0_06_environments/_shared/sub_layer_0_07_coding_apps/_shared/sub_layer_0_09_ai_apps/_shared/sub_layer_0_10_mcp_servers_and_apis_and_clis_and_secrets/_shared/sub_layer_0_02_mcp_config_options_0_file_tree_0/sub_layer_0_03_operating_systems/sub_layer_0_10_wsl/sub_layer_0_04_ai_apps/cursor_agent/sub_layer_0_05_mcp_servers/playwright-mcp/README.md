---
resource_id: "06dcefc5-be20-4bb2-9fb3-a670e9d95be1"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (cursor_agent on wsl)

<!-- section_id: "84e168e3-e20c-44fd-b67a-a629d3f63218" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "a08d7e92-7507-424e-be68-1368a97e7767" -->
## Quick Start

<!-- section_id: "16822672-14af-43d1-9965-a570dbbb80fe" -->
### Basic Setup (Recommended)

1. **Create Playwright config with WSLg fixes**:
   ```bash
   mkdir -p ~/.config/mcp/configs
   ```
   
   Create `~/.config/mcp/configs/playwright.json`:
   ```json
   {
     "browser": "chromium",
     "launchOptions": {
       "executablePath": "/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome",
       "args": [
         "--ozone-platform=wayland",
         "--enable-features=UseOzonePlatform",
         "--disable-dev-shm-usage",
         "--no-sandbox"
       ],
       "headless": false
     }
   }
   ```

2. **Update MCP config** (`~/.config/mcp/mcp.json`):
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "bash",
         "args": [
           "-c",
           "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\" && npx -y @playwright/mcp@latest --browser chromium --config /home/dawson/.config/mcp/configs/playwright.json"
         ],
         "env": {
           "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
           "HOME": "/home/dawson",
           "DISPLAY": ":0",
           "WAYLAND_DISPLAY": "wayland-0",
           "XDG_RUNTIME_DIR": "/mnt/wslg/runtime-dir"
         }
       }
     }
   }
   ```

3. **Restart Cursor IDE** completely

**⚠️ Critical**: The Wayland/Ozone flags are required to prevent browser crashes on WSLg. See `general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md` for details.

<!-- section_id: "b6631a79-684d-433c-a6a5-feebfb394086" -->
## Notes

<!-- section_id: "f0118af5-3bc0-4c2c-868d-ab6d848d7cd9" -->
### Concurrent browser (optional)
Use OS+tool-specific Playwright configs so Cursor Agent can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_11_mcp_servers_and_tools_setup/0.06_automation/scripts

# Create the WSL + Cursor config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools cursor

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.config/mcp/playwright.wsl_cursor.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-cursor`

<!-- section_id: "24eb8486-fb2f-4aa2-94cb-23772aeadbd1" -->
## Issues and Fixes

- **Browser crashes on WSLg**: See `general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md`
