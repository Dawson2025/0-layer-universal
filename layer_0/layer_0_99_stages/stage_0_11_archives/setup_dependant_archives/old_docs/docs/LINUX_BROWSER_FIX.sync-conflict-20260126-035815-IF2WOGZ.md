---
resource_id: "6fd53963-476c-4513-ba8f-bd1e5bd54fdf"
resource_type: "document"
resource_name: "LINUX_BROWSER_FIX.sync-conflict-20260126-035815-IF2WOGZ"
---
# Linux/Ubuntu Browser Automation Fix

<!-- section_id: "09eb28dd-8a2e-42f6-919d-6772d7c8a444" -->
## Problem
Cursor's browser automation has known issues on Linux/Ubuntu, even when Chrome is installed and detected.

<!-- section_id: "e091c8e1-a84f-4558-b236-c040ee634444" -->
## Solution

<!-- section_id: "a07a78e0-9661-425c-b0c2-7b3b6863ab9a" -->
### Step 1: Set Custom Executable Path
1. In Cursor IDE, go to **Settings** → **Tools & MCP** → **Browser Automation**
2. Click the **Connection Type** dropdown
3. Select **"Custom Executable Path"**
4. Enter the Chrome path: `/usr/bin/google-chrome`
5. Save/Apply the setting

<!-- section_id: "b16dbcef-5916-40dc-be38-00a3a28dfe94" -->
### Step 2: Alternative - Use Playwright Chromium
If system Chrome doesn't work, try the Playwright Chromium:
- Path: `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

<!-- section_id: "a1bffc5e-2a43-4f5c-83f1-b7f0028c3ca7" -->
### Step 3: Restart Cursor
After changing the connection type, completely restart Cursor IDE.

<!-- section_id: "a7a96994-0a22-451f-be07-603c76aa89b6" -->
## Known Linux Issues

Based on community reports:
- Chrome path detection can fail on Linux even when Chrome is installed
- Explicitly setting the executable path resolves the issue
- The "Default (Bundled Chrome)" option may not work properly on Linux

<!-- section_id: "476110e0-c876-4a94-965f-6d457c64b456" -->
## Verification

After applying the fix, test with:
- Navigate to a website
- Take a screenshot
- The browser tools should work without the "Browser not installed" error

<!-- section_id: "a2e93a74-3eae-43bb-84f9-a22a2f0f864e" -->
## References
- [Cursor Forum: Browser Automation Linux Install Path](https://forum.cursor.com/t/browser-automation-linux-install-path/140507)
- Linux users report needing to explicitly set Chrome paths

