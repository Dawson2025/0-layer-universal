---
resource_id: "1a3c5269-b855-43f8-bd1b-7d5d0971f03d"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (cursor_agent on wsl)

<!-- section_id: "ab2c9127-7c2b-402c-97d6-91d099d351e2" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "3c970018-50c3-4db8-a0fa-be226285dd47" -->
## Quick Start

<!-- section_id: "73032930-2577-41c6-91ca-07ed8540a983" -->
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

<!-- section_id: "6b21a62c-07cf-43c4-8836-e5d19dceca83" -->
## Notes

<!-- section_id: "b8dbb7f3-8405-4cb4-97ff-92a3d5bcff51" -->
### Concurrent browser (optional)
Use OS+tool-specific Playwright configs so Cursor Agent can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_11_mcp_servers_and_tools_setup/0.06_automation/scripts

# Create the WSL + Cursor config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools cursor

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.config/mcp/playwright.wsl_cursor.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-cursor`

<!-- section_id: "1462ad97-2b3b-4144-b980-9da3d36fc533" -->
## Issues and Fixes

- **Browser crashes on WSLg**: See `general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md`
