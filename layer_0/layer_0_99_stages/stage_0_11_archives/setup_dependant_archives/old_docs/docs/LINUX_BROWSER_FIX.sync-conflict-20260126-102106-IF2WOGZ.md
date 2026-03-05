---
resource_id: "5cc4333f-74b8-4c3b-9b8b-13feffdf64bd"
resource_type: "document"
resource_name: "LINUX_BROWSER_FIX.sync-conflict-20260126-102106-IF2WOGZ"
---
# Linux/Ubuntu Browser Automation Fix

<!-- section_id: "1d53706e-2a62-46b4-9fbc-bdc7b2a6c73f" -->
## Problem
Cursor's browser automation has known issues on Linux/Ubuntu, even when Chrome is installed and detected.

<!-- section_id: "7fa6fcee-0c14-4788-9a5e-8ff2e65d1a78" -->
## Solution

<!-- section_id: "c21b6142-a7c7-4fe0-b726-a494cb2923c9" -->
### Step 1: Set Custom Executable Path
1. In Cursor IDE, go to **Settings** → **Tools & MCP** → **Browser Automation**
2. Click the **Connection Type** dropdown
3. Select **"Custom Executable Path"**
4. Enter the Chrome path: `/usr/bin/google-chrome`
5. Save/Apply the setting

<!-- section_id: "b8ec9c20-a3fe-4d95-86ef-4f6c634def54" -->
### Step 2: Alternative - Use Playwright Chromium
If system Chrome doesn't work, try the Playwright Chromium:
- Path: `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

<!-- section_id: "e48924dd-fc98-4561-af00-c96ed416d961" -->
### Step 3: Restart Cursor
After changing the connection type, completely restart Cursor IDE.

<!-- section_id: "9fbd202f-94af-4bee-8f89-e2a4a1f1a6df" -->
## Known Linux Issues

Based on community reports:
- Chrome path detection can fail on Linux even when Chrome is installed
- Explicitly setting the executable path resolves the issue
- The "Default (Bundled Chrome)" option may not work properly on Linux

<!-- section_id: "6295109e-c733-4bd4-a539-7bce9ca84c13" -->
## Verification

After applying the fix, test with:
- Navigate to a website
- Take a screenshot
- The browser tools should work without the "Browser not installed" error

<!-- section_id: "0962f4a9-7d13-41cb-b4c4-3caeb58e3e43" -->
## References
- [Cursor Forum: Browser Automation Linux Install Path](https://forum.cursor.com/t/browser-automation-linux-install-path/140507)
- Linux users report needing to explicitly set Chrome paths

