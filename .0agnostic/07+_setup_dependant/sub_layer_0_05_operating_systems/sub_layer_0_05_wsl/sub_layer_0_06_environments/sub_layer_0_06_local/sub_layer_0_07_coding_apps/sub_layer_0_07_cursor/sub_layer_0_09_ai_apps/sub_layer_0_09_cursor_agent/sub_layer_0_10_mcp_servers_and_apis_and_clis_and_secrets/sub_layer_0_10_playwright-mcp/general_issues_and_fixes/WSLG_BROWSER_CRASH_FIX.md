---
resource_id: "30ff641a-1de9-4dfd-a24b-a82d0f2bd637"
resource_type: "document"
resource_name: "WSLG_BROWSER_CRASH_FIX"
---
# WSLg Browser Crash Fix - Playwright MCP on Cursor IDE

**Date**: 2025-01-26  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Cursor IDE  
**Status**: ✅ Fixed and Verified

<!-- section_id: "3273e2fb-d4d2-4cbb-871a-ce0f04f31c72" -->
## Problem

Playwright MCP browser was crashing on WSLg when attempting to:
- Take screenshots (`page.screenshot: Target crashed`)
- Navigate to pages (`page.goto: Page crashed`)
- Interact with pages (`page._snapshotForAI: Target crashed`)

**Symptoms**:
- Browser would launch successfully
- Navigation would work initially
- Browser would crash when attempting screenshots or certain operations
- Error messages: "Target crashed" in Playwright operations

<!-- section_id: "c43fe189-8d75-492c-a2d1-01e9c6067242" -->
## Root Cause

Headed Chromium on WSLg requires specific Wayland/Ozone platform flags to function properly. Without these flags, the browser process crashes due to display system incompatibilities.

**Key Issue**: WSLg uses Wayland for display, and Chromium needs explicit configuration to use the Wayland platform instead of defaulting to X11.

<!-- section_id: "daf2bbb1-32db-4918-aef0-7b6fb967b21e" -->
## Solution

Create a Playwright configuration file with Wayland/Ozone flags and reference it in the MCP server configuration.

<!-- section_id: "6abda2b0-7574-4490-a31a-7686a2a0b183" -->
### Step 1: Create Playwright Config File

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

**Critical Flags**:
- `--ozone-platform=wayland` - Forces Chromium to use Wayland (required for WSLg)
- `--enable-features=UseOzonePlatform` - Enables Ozone platform features
- `--disable-dev-shm-usage` - Prevents shared memory issues in WSL
- `--no-sandbox` - Helps with WSL permissions (use with caution)

**Note**: Update `executablePath` to match your actual Chromium version:
```bash
ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
```

<!-- section_id: "d2a935e1-da26-4ff9-8b96-b35e55b91362" -->
### Step 2: Update MCP Configuration

Update `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json` which symlinks to it):

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

**Key Changes**:
- Added `--config` flag pointing to the config file
- Ensures NVM is loaded via bash wrapper
- Sets WSLg environment variables

<!-- section_id: "370e53bc-1273-4ff7-8ca8-ee4400949b48" -->
### Step 3: Restart Cursor IDE

1. **Completely close Cursor IDE** (ensure all processes are terminated)
2. **Restart Cursor IDE**
3. **Verify in Settings**: Cursor Settings → Tools & MCP → Installed MCP Servers
   - Playwright should show as "connected" (green circle)
   - Should list 22 tools available

<!-- section_id: "0d49de8e-7d09-4151-a2b3-724d73a890a4" -->
## Verification

After applying the fix, test the browser:

```bash
# Test navigation
# Use Playwright MCP tools to navigate to a page

# Test screenshot
# Use browser_take_screenshot tool - should work without crashing

# Test multiple operations
# Navigate, take screenshots, interact with pages - all should work
```

**Expected Results**:
- ✅ Browser launches successfully
- ✅ Navigation works without crashes
- ✅ Screenshots work without crashes
- ✅ Page interactions work without crashes
- ✅ Browser remains stable during extended use

<!-- section_id: "c0bb4e09-9189-427c-8a9e-36541afcfa1f" -->
## Configuration Details

<!-- section_id: "5932297f-b246-4cf5-8975-9adadea70872" -->
### Environment Variables

The MCP configuration includes these WSLg-specific environment variables:

- `DISPLAY=:0` - X11 display (WSLg provides this)
- `WAYLAND_DISPLAY=wayland-0` - Wayland display (WSLg provides this)
- `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir` - Runtime directory for Wayland

<!-- section_id: "270a782c-7808-4591-90c3-15e0b3ed9eb0" -->
### Why These Flags Work

1. **`--ozone-platform=wayland`**: 
   - Forces Chromium to use Wayland instead of X11
   - Required for WSLg which uses Wayland for display

2. **`--enable-features=UseOzonePlatform`**:
   - Enables Ozone platform abstraction layer
   - Required for Wayland support in Chromium

3. **`--disable-dev-shm-usage`**:
   - Prevents shared memory issues in WSL
   - WSL has limited `/dev/shm` space

4. **`--no-sandbox`**:
   - Disables Chromium sandbox (helps with WSL permissions)
   - **Security Note**: Only use in trusted environments

<!-- section_id: "cd56e552-f743-4a24-b9c3-4d369d29cf9f" -->
## Related Documentation

- **WSL MCP Notes**: `../../README.md` (WSL general documentation)
- **Playwright MCP Cursor Setup**: `../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/PLAYWRIGHT_MCP_CURSOR_SETUP.md`
- **Browser MCP Routing Table**: `../../../../../../0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md`
- **MCP Configuration Guide**: `../../../../../../0.01_core-system/MCP_CONFIGURATION_GUIDE.md`

<!-- section_id: "5587fe0b-01ed-4e96-b9a3-8711f18e13a2" -->
## Testing Performed

**Date**: 2025-01-26  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Cursor IDE

**Test Results**:
- ✅ Navigation to `https://byuidatascience.github.io/pac20026_fall2025/` - Success
- ✅ Screenshot capture (full page) - Success (no crash)
- ✅ Navigation to Canvas course - Success
- ✅ Multiple tab operations - Success
- ✅ Extended browser session - Stable

**Before Fix**:
- ❌ Screenshots caused "Target crashed" errors
- ❌ Page navigation after initial load caused crashes
- ❌ Browser was unstable

**After Fix**:
- ✅ All operations work without crashes
- ✅ Browser remains stable
- ✅ Ready for production use

<!-- section_id: "64088a89-a559-401a-acbf-ba6b1fcfdcb3" -->
## Troubleshooting

<!-- section_id: "0e7ae4f9-80d4-408c-9af4-15bf449194c8" -->
### Browser Still Crashes

1. **Verify config file exists**:
   ```bash
   cat ~/.config/mcp/configs/playwright.json
   ```

2. **Check Chromium path**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome
   ```
   Update `executablePath` in config if version differs

3. **Verify WSLg is working**:
   ```bash
   test -d /mnt/wslg && echo "WSLg OK" || echo "WSLg missing"
   echo "DISPLAY: $DISPLAY"
   echo "WAYLAND_DISPLAY: $WAYLAND_DISPLAY"
   ```

4. **Check MCP server is using config**:
   - Verify `--config` flag is in MCP server args
   - Check Cursor Settings → Tools & MCP → Playwright command

<!-- section_id: "4ec4ec51-4399-46ab-ab58-4b7d513213a9" -->
### Browser Won't Launch

1. **Check Node.js/NVM**:
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   npx -y @playwright/mcp@latest --help
   ```

2. **Verify browser installation**:
   ```bash
   ls -la ~/.cache/ms-playwright/chromium-*/
   ```

3. **Check MCP server logs** in Cursor Settings

<!-- section_id: "9cdad640-6f78-41db-95b0-f0a35edcdbce" -->
## Alternative Solutions

If Wayland flags don't work:

1. **Use Headless Mode**:
   - Set `"headless": true` in config
   - Browser runs without display (screenshots still work)

2. **Use Windows Chrome via DevTools MCP**:
   - Configure Chrome DevTools MCP
   - Use Windows Chrome path: `C:\Program Files\Google\Chrome\Application\chrome.exe`

3. **Use Hosted Browser MCP**:
   - Browserbase or similar hosted browser service
   - Avoids local display issues entirely

---

**Last Updated**: 2025-01-26  
**Verified By**: Browser automation testing on WSL2 + Cursor IDE  
**Status**: ✅ Production Ready

