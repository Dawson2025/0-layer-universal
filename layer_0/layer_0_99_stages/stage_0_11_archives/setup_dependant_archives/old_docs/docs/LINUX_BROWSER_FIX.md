---
resource_id: "3f46c169-0803-45a0-b639-2cb9b8a424f6"
resource_type: "document"
resource_name: "LINUX_BROWSER_FIX"
---
# Linux/Ubuntu Browser Automation Fix

<!-- section_id: "26a3c110-e8a9-42f5-9dc6-9ece48eadc6f" -->
## Problem
Cursor's browser automation has known issues on Linux/Ubuntu, even when Chrome is installed and detected.

<!-- section_id: "c9ed5554-248f-4d19-aea4-586d4716936d" -->
## Solution

<!-- section_id: "d86923eb-11fe-4645-b2da-fa4920448d21" -->
### Step 1: Set Custom Executable Path
1. In Cursor IDE, go to **Settings** → **Tools & MCP** → **Browser Automation**
2. Click the **Connection Type** dropdown
3. Select **"Custom Executable Path"**
4. Enter the Chrome path: `/usr/bin/google-chrome`
5. Save/Apply the setting

<!-- section_id: "fee323a3-8eb6-4af8-baa4-29f3e49f0c4d" -->
### Step 2: Alternative - Use Playwright Chromium
If system Chrome doesn't work, try the Playwright Chromium:
- Path: `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

<!-- section_id: "898a1f9b-11ea-4459-8b29-9e532aba9749" -->
### Step 3: Restart Cursor
After changing the connection type, completely restart Cursor IDE.

<!-- section_id: "987e910c-1db0-419c-a241-b7544a457c4e" -->
## Known Linux Issues

Based on community reports:
- Chrome path detection can fail on Linux even when Chrome is installed
- Explicitly setting the executable path resolves the issue
- The "Default (Bundled Chrome)" option may not work properly on Linux

<!-- section_id: "e50eeb39-c8bf-4bc8-b5bb-690fa0481a25" -->
## Verification

After applying the fix, test with:
- Navigate to a website
- Take a screenshot
- The browser tools should work without the "Browser not installed" error

<!-- section_id: "5e88616e-a9df-451a-b15a-01f40eb5902b" -->
## References
- [Cursor Forum: Browser Automation Linux Install Path](https://forum.cursor.com/t/browser-automation-linux-install-path/140507)
- Linux users report needing to explicitly set Chrome paths

