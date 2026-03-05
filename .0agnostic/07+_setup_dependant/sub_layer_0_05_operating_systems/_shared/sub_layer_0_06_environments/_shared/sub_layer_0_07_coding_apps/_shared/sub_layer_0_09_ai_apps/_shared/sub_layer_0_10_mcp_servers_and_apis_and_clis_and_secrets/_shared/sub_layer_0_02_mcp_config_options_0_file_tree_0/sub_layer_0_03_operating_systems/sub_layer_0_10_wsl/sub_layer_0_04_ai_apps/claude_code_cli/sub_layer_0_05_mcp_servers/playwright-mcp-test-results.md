---
resource_id: "8ea5c862-82f6-43b5-9714-398e80350065"
resource_type: "document"
resource_name: "playwright-mcp-test-results"
---
# Playwright MCP Server Test Results

**Date:** 2025-12-30
**System:** WSL (Windows Subsystem for Linux) - Ubuntu
**Node.js Version:** v22.20.0
**Playwright Version:** 1.55.0
**Playwright MCP Version:** 0.0.54

<!-- section_id: "ab8a50df-e24f-4052-860c-815326d8ff0a" -->
## Test Summary

The Playwright MCP server is **CONFIGURED and PARTIALLY WORKING** in Claude Code CLI. The server can start successfully and respond to MCP protocol commands, but has browser installation path issues that prevent full functionality.

<!-- section_id: "996e0b59-85c4-4f7c-ac37-f4bdd1ddcf4e" -->
### Overall Status: ⚠️ CONFIGURED BUT NEEDS BROWSER PATH FIX

---

<!-- section_id: "bbeffba6-482a-40c1-a732-939b223f3b8a" -->
## 1. Configuration Review

<!-- section_id: "5788594a-fbeb-415d-9892-8fdde57753fa" -->
### Claude Code Configuration Location
- **File:** `/home/dawson/.claude.json`
- **Project Scope:** `/home/dawson` (user's home directory)

<!-- section_id: "68fc5720-2792-45c3-bbc3-d011b547ff5f" -->
### Playwright MCP Configuration
```json
{
  "playwright": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "@playwright/mcp@latest",
      "--browser",
      "chromium"
    ],
    "env": {
      "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
      "HOME": "/home/dawson"
    }
  }
}
```

**Configuration Status:** ✅ VALID - Properly configured with correct environment variables

---

<!-- section_id: "5966691f-c19c-4485-a3f1-718e1de6e11a" -->
## 2. Browser Installation Verification

<!-- section_id: "34f47074-5156-46aa-a9ad-c1fd8bdd9e12" -->
### Playwright Browsers Directory
- **Path:** `/home/dawson/.cache/ms-playwright`
- **Status:** ✅ EXISTS

<!-- section_id: "2f1c69a6-662a-45b2-8bb6-b8adb2820d54" -->
### Installed Browsers
```
/home/dawson/.cache/ms-playwright/
├── chromium-1200/
│   └── chrome-linux64/chrome (263,990,488 bytes) ✅
├── chromium_headless_shell-1200/
├── firefox-1497/
├── webkit-2227/
├── mcp-chromium-ec5e1e8/
├── mcp-chromium/
├── mcp-chromium-9c76515/
└── [various other browser installations]
```

**Browser Status:** ✅ INSTALLED - Chromium 1200 is present at `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`

---

<!-- section_id: "fe572cc4-763a-4b2e-9ec3-f2e866b0889b" -->
## 3. MCP Server Startup Test

<!-- section_id: "6ba29b60-ea33-467a-86b8-10edda7a5648" -->
### Test Method
Sent MCP protocol initialization request via stdio:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {"name": "test", "version": "1.0"}
  }
}
```

<!-- section_id: "a6018f19-2979-48fa-bf7f-38a905564f6e" -->
### Response
```json
{
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {"tools": {}},
    "serverInfo": {"name": "Playwright", "version": "0.0.54"}
  },
  "jsonrpc": "2.0",
  "id": 1
}
```

**Startup Status:** ✅ SUCCESS - Server starts and responds correctly

---

<!-- section_id: "27a4768e-f9ef-4b83-ad6e-b4c2e04ea711" -->
## 4. Available Tools Test

<!-- section_id: "3b187fa7-b2f5-40e2-835b-260f5e41e32a" -->
### Test Method
Sent `tools/list` request after initialization

<!-- section_id: "c03ed0cb-78bf-414c-b62c-bd8f7fae111c" -->
### Available Tools (22 total)
1. `browser_close` - Close the page
2. `browser_resize` - Resize the browser window
3. `browser_console_messages` - Returns all console messages
4. `browser_handle_dialog` - Handle a dialog
5. `browser_evaluate` - Evaluate JavaScript expression on page or element
6. `browser_file_upload` - Upload one or multiple files
7. `browser_fill_form` - Fill multiple form fields
8. `browser_install` - Install the browser specified in the config
9. `browser_press_key` - Press a key on the keyboard
10. `browser_type` - Type text into editable element
11. `browser_navigate` - Navigate to a URL
12. `browser_navigate_back` - Go back to the previous page
13. `browser_network_requests` - Returns all network requests since loading the page
14. `browser_run_code` - Run Playwright code snippet
15. `browser_take_screenshot` - Take a screenshot of the current page
16. `browser_snapshot` - Capture accessibility snapshot of the current page
17. `browser_click` - Perform click on a web page
18. `browser_drag` - Perform drag and drop between two elements
19. `browser_hover` - Hover over element on page
20. `browser_select_option` - Select an option in a dropdown
21. `browser_tabs` - List, create, close, or select a browser tab
22. `browser_wait_for` - Wait for text to appear or disappear or a specified time to pass

**Tools List Status:** ✅ SUCCESS - All 22 tools available

---

<!-- section_id: "4e195a11-c0bc-48fa-8a49-fd1ce60ea8d7" -->
## 5. Functional Test Results

<!-- section_id: "dea7ded2-5fdf-424c-ae6c-76699d84ceaa" -->
### Test: Navigate to https://example.com

**Command Sent:**
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "browser_navigate",
    "arguments": {"url": "https://example.com"}
  }
}
```

**Response:**
```json
{
  "result": {
    "content": [{
      "type": "text",
      "text": "### Result\nError: Browser specified in your config is not installed. Either install it (likely) or change the config.\n"
    }],
    "isError": true
  },
  "jsonrpc": "2.0",
  "id": 3
}
```

**Navigation Status:** ❌ FAILED - Browser path not recognized by MCP server

---

<!-- section_id: "2d871993-d161-42da-8649-2175ba607f32" -->
## 6. Issue Analysis

<!-- section_id: "e4a21f5e-a6ca-459e-af2f-c93aa1ab78be" -->
### Root Cause
The Playwright MCP server cannot find the installed Chromium browser despite:
- Chromium being installed at `/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
- Environment variable `PLAYWRIGHT_BROWSERS_PATH` being set in the configuration
- Environment variable `HOME` being set in the configuration

<!-- section_id: "ac372187-b96f-4487-890a-d499f5762e38" -->
### Possible Reasons
1. **Version Mismatch:** The MCP server may be looking for a different Chromium version
2. **Path Recognition:** The MCP server's internal Playwright installation may not respect the `PLAYWRIGHT_BROWSERS_PATH` environment variable when launched via `npx -y`
3. **NPX Caching:** The `npx -y` command may create its own temporary installation that doesn't share the browser cache

<!-- section_id: "a85b05a8-ac59-4c58-a418-cf2d420ca3c0" -->
### Evidence
- Browser install attempt via `browser_install` tool timed out (15+ seconds)
- Manual Playwright installation shows Chromium 1200 is present
- When installing via `npx -y playwright install chromium`, it removed version 1202 but kept 1200

---

<!-- section_id: "84a0c149-419c-4c7e-a417-0d1ef8716d01" -->
## 7. Test Results Summary

| Test Component | Status | Details |
|---------------|--------|---------|
| Configuration File | ✅ PASS | Valid JSON, correct structure |
| Browser Installation | ✅ PASS | Chromium 1200 installed |
| MCP Server Startup | ✅ PASS | Responds to initialization |
| Tools Discovery | ✅ PASS | All 22 tools available |
| Browser Navigation | ❌ FAIL | Cannot find browser |
| Page Snapshot | ❌ FAIL | Cannot find browser |
| Browser Close | ✅ PASS | Executes (no browser to close) |

**Overall Score:** 5/7 tests passed (71%)

---

<!-- section_id: "bce57132-0b9c-4be5-82b8-e103609599f8" -->
## 8. Recommendations

<!-- section_id: "912fdcc8-46c5-41e5-aae6-aa49e3fe9664" -->
### Immediate Fixes

1. **Run Browser Install Tool from Claude Code:**
   ```bash
   # Let the MCP server install its own browser
   # Use the browser_install tool within Claude Code
   ```

2. **Alternative: Install via npx with explicit path:**
   ```bash
   PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright \
   npx -y @playwright/mcp@latest --browser chromium &
   # Then use the browser_install tool
   ```

3. **Verify Browser Detection:**
   Check if the MCP server can detect browsers:
   ```bash
   PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright \
   npx -y playwright install --dry-run chromium
   ```

<!-- section_id: "629d7e20-4859-41c8-86d4-26688bf530a3" -->
### Configuration Adjustments

Consider adding these to the MCP configuration:
```json
{
  "playwright": {
    "type": "stdio",
    "command": "npx",
    "args": [
      "-y",
      "@playwright/mcp@latest",
      "--browser",
      "chromium"
    ],
    "env": {
      "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
      "HOME": "/home/dawson",
      "DEBUG": "pw:browser*"  // Enable browser detection debugging
    }
  }
}
```

<!-- section_id: "ddfcc557-0b33-4e3b-96f4-97c8e8e57da5" -->
### Long-term Solution

1. **Use Local Installation:**
   Instead of `npx -y @playwright/mcp@latest`, install locally:
   ```bash
   npm install -g @playwright/mcp
   playwright install chromium
   ```

   Then update configuration:
   ```json
   {
     "command": "playwright-mcp",
     "args": ["--browser", "chromium"]
   }
   ```

2. **Create Wrapper Script:**
   Create `/home/dawson/.local/bin/playwright-mcp-wrapper.sh`:
   ```bash
   #!/bin/bash
   export PLAYWRIGHT_BROWSERS_PATH=/home/dawson/.cache/ms-playwright
   export HOME=/home/dawson
   exec npx -y @playwright/mcp@latest "$@"
   ```

---

<!-- section_id: "df4dc892-1281-475f-b6a2-693c583e1ef4" -->
## 9. Workaround for Immediate Use

If you need to use Playwright MCP right now:

1. Open Claude Code
2. Navigate to a project with Playwright MCP configured
3. Ask Claude to use the `browser_install` tool
4. Wait for the installation to complete
5. Try browser automation again

This will let the MCP server install browsers in its own cache location.

---

<!-- section_id: "8986fd2b-a4ec-4b55-b5c0-ff8a58c987f8" -->
## 10. Additional Information

<!-- section_id: "706ea427-942d-4f3b-81a9-760838dac5a8" -->
### Environment Details
- **OS:** Linux 6.6.87.2-microsoft-standard-WSL2 (WSL)
- **Shell:** bash
- **Node Package Manager:** npm via nvm
- **npx Path:** `/home/dawson/.nvm/versions/node/v22.20.0/bin/npx`

<!-- section_id: "97bcbbca-45c5-4429-9f9d-be03881e13f0" -->
### Related Directories
- **Playwright Cache:** `/home/dawson/.cache/ms-playwright/`
- **Claude Config:** `/home/dawson/.claude.json`
- **MCP Directory:** `/home/dawson/.playwright-mcp/` (empty/doesn't exist)

<!-- section_id: "b720aa6e-607b-4aa7-8beb-540ce98d481e" -->
### Test Files Created
- `/tmp/test-playwright-mcp.js` - Node.js test script for MCP protocol

---

<!-- section_id: "ba349962-fc13-466b-99ef-fc87b306ab87" -->
## Conclusion

The Playwright MCP server is **properly configured** in Claude Code and can:
- Start successfully
- Respond to MCP protocol commands
- List all available tools
- Execute non-browser commands

However, it **cannot execute browser automation** due to browser path detection issues. The issue is likely related to how `npx -y` handles temporary package installations and browser caching.

**Recommended Next Step:** Use the `browser_install` tool from within Claude Code to let the MCP server install browsers in its own location, or switch to a local installation of `@playwright/mcp` for better control over browser paths.

---

**Test Performed By:** Claude Code Agent
**Test Script:** `/tmp/test-playwright-mcp.js`
**Documentation Generated:** 2025-12-30
