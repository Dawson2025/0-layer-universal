---
resource_id: "b1b090c5-f6ad-431b-9cfc-70fa3633a358"
resource_type: "document"
resource_name: "BROWSER_MCP_SETUP_COMPLETE.sync-conflict-20260126-035820-IF2WOGZ"
---
# Browser MCP Setup - Complete

<!-- section_id: "878aa509-0237-4e14-8763-044c8eb27667" -->
## ✅ What's Been Configured

<!-- section_id: "c8ffed52-4f0e-43f1-959e-6775cd270f06" -->
### 1. Playwright MCP Server
- **Status**: ✅ Configured and running
- **Location**: `~/.cursor/mcp.json`
- **Browser**: Chromium (installed at `~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`)
- **Processes**: 3+ Playwright MCP processes running

<!-- section_id: "ef2adfd2-f229-44fe-9fbb-a8109329cb32" -->
### 2. Alternative Browser MCP Server
- **Status**: ✅ Configured
- **Server**: `@agent-infra/mcp-server-browser`
- **Browser Path**: Explicitly set to Chromium executable
- **Note**: Will be available after Cursor restart

<!-- section_id: "245ca067-e131-4efb-a314-a4d9b3ca097c" -->
### 3. Cursor Browser Extension
- **Status**: ⚠️ Requires manual installation
- **Issue**: "No server info found" - needs Chrome extension installed
- **Solution**: Install Cursor browser extension in Chrome (see below)

<!-- section_id: "306a6930-10ed-4138-863b-bd21ef7bfde0" -->
## 🔧 Current Configuration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium"
      ]
    },
    "browser": {
      "command": "npx",
      "args": [
        "-y",
        "@agent-infra/mcp-server-browser",
        "--executable-path",
        "/home/dawson/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome"
      ]
    }
  }
}
```

<!-- section_id: "90bce978-bf68-4d63-a1b4-6a4e0ae281f1" -->
## 📋 Next Steps

<!-- section_id: "bd945ec0-f46d-4f65-9d72-6c34ca4e11fb" -->
### Option 1: Use Playwright/Browser MCP (Recommended - No Extension Needed)
1. **Restart Cursor completely** (close all windows)
2. After restart, Playwright MCP tools should be available
3. Tools may be named differently (check available tools)

<!-- section_id: "21a35a17-fb2b-44f9-beb4-66a51510abae" -->
### Option 2: Install Cursor Browser Extension (For cursor-browser-extension)
1. Open Google Chrome
2. Go to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Search Chrome Web Store for "Cursor" browser extension
5. Install the official Cursor extension
6. Restart Cursor IDE
7. The `cursor-browser-extension` tools should then work

<!-- section_id: "b135c77f-5fa2-4d36-afbd-246d247f83cc" -->
## 🧪 Testing

After restarting Cursor, test with:
- Navigate to a website
- Take a screenshot
- Click elements
- Fill forms

<!-- section_id: "1584cb88-d7db-4a62-b766-3bc04451a659" -->
## 📝 Available Tools (18 total)

All browser automation tools are available:
- Navigation (navigate, navigate_back, tabs)
- Interaction (click, type, hover, drag, select_option)
- Information (snapshot, screenshot, console_messages, network_requests)
- Forms (fill_form, file_upload)
- Dialogs (handle_dialog)
- Code execution (evaluate, run_code)
- Browser management (resize, close, install)

<!-- section_id: "7a3e09a3-c641-4521-bc34-5690baddb8a7" -->
## ⚠️ Important Notes

- **Playwright MCP** is configured and should work after restart
- **cursor-browser-extension** requires the Chrome extension to be installed
- **@agent-infra/mcp-server-browser** is configured as an alternative
- All browsers are properly installed and accessible

<!-- section_id: "cd392542-5a57-4c14-a959-58534e55a673" -->
## 🔍 Troubleshooting

If tools still don't work after restart:
1. Check MCP logs: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
2. Verify Playwright processes: `ps aux | grep playwright`
3. Test browser path: `ls -la ~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
4. Check Node.js: `which node && node --version`


