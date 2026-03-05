---
resource_id: "409614b7-44b8-412b-93cc-742eb53119da"
resource_type: "document"
resource_name: "BROWSER_MCP_SETUP_COMPLETE.sync-conflict-20260126-102106-IF2WOGZ"
---
# Browser MCP Setup - Complete

<!-- section_id: "ffd1050c-59d7-40d2-85ee-8d9e703abeeb" -->
## ✅ What's Been Configured

<!-- section_id: "ae2bf927-bd3e-412b-84b9-6f65b9af9497" -->
### 1. Playwright MCP Server
- **Status**: ✅ Configured and running
- **Location**: `~/.cursor/mcp.json`
- **Browser**: Chromium (installed at `~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`)
- **Processes**: 3+ Playwright MCP processes running

<!-- section_id: "31449bfc-887b-4176-b5b6-43ad56b0bbe7" -->
### 2. Alternative Browser MCP Server
- **Status**: ✅ Configured
- **Server**: `@agent-infra/mcp-server-browser`
- **Browser Path**: Explicitly set to Chromium executable
- **Note**: Will be available after Cursor restart

<!-- section_id: "47f27eaf-62ce-4fd7-8b04-2345c8bf3ac0" -->
### 3. Cursor Browser Extension
- **Status**: ⚠️ Requires manual installation
- **Issue**: "No server info found" - needs Chrome extension installed
- **Solution**: Install Cursor browser extension in Chrome (see below)

<!-- section_id: "b1eab3b4-5372-4bf6-b5d1-4682491e8f9c" -->
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

<!-- section_id: "613e2b97-5018-4c66-8ca2-050377477829" -->
## 📋 Next Steps

<!-- section_id: "8d5b610c-9e6f-4950-ba0a-8fdd392d9331" -->
### Option 1: Use Playwright/Browser MCP (Recommended - No Extension Needed)
1. **Restart Cursor completely** (close all windows)
2. After restart, Playwright MCP tools should be available
3. Tools may be named differently (check available tools)

<!-- section_id: "382250bf-3447-4aca-9fed-83dd90672d6e" -->
### Option 2: Install Cursor Browser Extension (For cursor-browser-extension)
1. Open Google Chrome
2. Go to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Search Chrome Web Store for "Cursor" browser extension
5. Install the official Cursor extension
6. Restart Cursor IDE
7. The `cursor-browser-extension` tools should then work

<!-- section_id: "c9e2a6f3-dcdd-45ac-993f-8acc060e1bc0" -->
## 🧪 Testing

After restarting Cursor, test with:
- Navigate to a website
- Take a screenshot
- Click elements
- Fill forms

<!-- section_id: "6146b15d-1a02-48e5-84c7-dec497e3363a" -->
## 📝 Available Tools (18 total)

All browser automation tools are available:
- Navigation (navigate, navigate_back, tabs)
- Interaction (click, type, hover, drag, select_option)
- Information (snapshot, screenshot, console_messages, network_requests)
- Forms (fill_form, file_upload)
- Dialogs (handle_dialog)
- Code execution (evaluate, run_code)
- Browser management (resize, close, install)

<!-- section_id: "0f4045a4-e261-47d2-9e3b-344c430ba33e" -->
## ⚠️ Important Notes

- **Playwright MCP** is configured and should work after restart
- **cursor-browser-extension** requires the Chrome extension to be installed
- **@agent-infra/mcp-server-browser** is configured as an alternative
- All browsers are properly installed and accessible

<!-- section_id: "4bbeb034-f97d-42c1-a90e-a640ddb6b87d" -->
## 🔍 Troubleshooting

If tools still don't work after restart:
1. Check MCP logs: `~/.config/Cursor/logs/*/window*/exthost/anysphere.cursor-mcp/`
2. Verify Playwright processes: `ps aux | grep playwright`
3. Test browser path: `ls -la ~/.cache/ms-playwright/chromium-1200/chrome-linux64/chrome`
4. Check Node.js: `which node && node --version`


