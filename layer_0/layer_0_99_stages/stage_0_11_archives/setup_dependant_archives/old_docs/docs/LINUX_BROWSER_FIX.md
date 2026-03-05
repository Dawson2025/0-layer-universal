---
resource_id: "3f46c169-0803-45a0-b639-2cb9b8a424f6"
resource_type: "document"
resource_name: "LINUX_BROWSER_FIX"
---
# Linux/Ubuntu Browser Automation Fix

## Problem
Cursor's browser automation has known issues on Linux/Ubuntu, even when Chrome is installed and detected.

## Solution

### Step 1: Set Custom Executable Path
1. In Cursor IDE, go to **Settings** → **Tools & MCP** → **Browser Automation**
2. Click the **Connection Type** dropdown
3. Select **"Custom Executable Path"**
4. Enter the Chrome path: `/usr/bin/google-chrome`
5. Save/Apply the setting

### Step 2: Alternative - Use Playwright Chromium
If system Chrome doesn't work, try the Playwright Chromium:
- Path: `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

### Step 3: Restart Cursor
After changing the connection type, completely restart Cursor IDE.

## Known Linux Issues

Based on community reports:
- Chrome path detection can fail on Linux even when Chrome is installed
- Explicitly setting the executable path resolves the issue
- The "Default (Bundled Chrome)" option may not work properly on Linux

## Verification

After applying the fix, test with:
- Navigate to a website
- Take a screenshot
- The browser tools should work without the "Browser not installed" error

## References
- [Cursor Forum: Browser Automation Linux Install Path](https://forum.cursor.com/t/browser-automation-linux-install-path/140507)
- Linux users report needing to explicitly set Chrome paths

