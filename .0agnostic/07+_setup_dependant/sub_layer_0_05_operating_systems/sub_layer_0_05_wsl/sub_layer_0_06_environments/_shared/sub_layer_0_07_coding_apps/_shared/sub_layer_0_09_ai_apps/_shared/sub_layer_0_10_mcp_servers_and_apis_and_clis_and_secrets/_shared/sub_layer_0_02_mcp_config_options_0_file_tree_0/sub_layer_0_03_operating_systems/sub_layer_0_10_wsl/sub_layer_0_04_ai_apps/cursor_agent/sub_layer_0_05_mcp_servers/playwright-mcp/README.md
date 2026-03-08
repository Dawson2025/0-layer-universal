---
resource_id: "3807f197-baab-4d1c-bd68-324dc44e244c"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (cursor_agent on wsl)

<!-- section_id: "8a6b1a69-75bf-42d3-afdd-e867bc3f87d5" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "52420db0-c30e-4102-9e54-fed157fcc5b7" -->
## Quick Start

<!-- section_id: "f79fecaf-5a4e-4fc1-b635-7e5551ee0c2c" -->
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

<!-- section_id: "114dfefd-1092-4d76-a1fd-4d4c0cf58988" -->
## Notes

<!-- section_id: "2f44d20b-1883-443e-9c8e-1928e4ab2a77" -->
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

<!-- section_id: "029ff8a8-4ece-468e-a6f7-e09296cdb96f" -->
## Issues and Fixes

- **Browser crashes on WSLg**: See `general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md`

---

<!-- section_id: "89548d47-c65f-4c47-add4-461a1a4d8d39" -->
## Legacy MCP Source

# playwright-mcp (cursor_agent on wsl)

<!-- section_id: "6a4d87cc-0b1b-4199-b06c-eeca18b30cfd" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "d6af58ce-a090-475f-9716-6397db113dd4" -->
## Quick Start

<!-- section_id: "a15ad826-b9b9-4a34-ae22-6fd99d8bc4a1" -->
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

<!-- section_id: "fcc1d965-431d-4fff-baa9-1f0e9ac45375" -->
## Notes

<!-- section_id: "551da83f-bc37-4440-bc82-650b172aa928" -->
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

<!-- section_id: "99d71f74-9a10-4676-be82-2e6162f2b2a4" -->
## Issues and Fixes

- **Browser crashes on WSLg**: See `general_issues_and_fixes/WSLG_BROWSER_CRASH_FIX.md`
