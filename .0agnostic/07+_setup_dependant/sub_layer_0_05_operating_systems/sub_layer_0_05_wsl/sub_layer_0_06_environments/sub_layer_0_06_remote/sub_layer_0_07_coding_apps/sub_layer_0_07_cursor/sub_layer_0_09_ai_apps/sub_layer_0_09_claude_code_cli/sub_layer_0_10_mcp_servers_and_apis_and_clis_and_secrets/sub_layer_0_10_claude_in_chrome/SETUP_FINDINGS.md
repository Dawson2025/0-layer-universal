---
resource_id: "4b652eb5-f717-477f-b624-fe72a8ec7765"
resource_type: "document"
resource_name: "SETUP_FINDINGS"
---
# Claude in Chrome Setup Findings for WSL

**Date:** 2025-12-30
**Environment:** WSL2 (Ubuntu 24.04) on Windows
**Claude Code Version:** 2.0.76

<!-- section_id: "bd75daa4-d853-439d-9ddb-e13e2da9fc1d" -->
## Critical Finding: WSL Not Supported

**Status:** ❌ **NOT SUPPORTED**

According to official Claude Code documentation, Claude in Chrome integration is **explicitly not supported on WSL**.

<!-- section_id: "992c7463-884b-45d6-b0ff-3004f8ddedd4" -->
### Why It Doesn't Work

1. **Native Messaging API Limitation**: Claude in Chrome uses Chrome's Native Messaging API to communicate between the extension and Claude Code CLI
2. **WSL Incompatibility**: The native messaging host installation and functionality do not work when Claude Code runs in WSL, even if Chrome is installed on Windows
3. **Architecture Mismatch**: The extension expects to communicate with a native Windows process, not a WSL Linux process

<!-- section_id: "2edd2369-fe3d-4876-b3f4-2af273db40c0" -->
### What We Tried

1. ✅ Installed Chrome in WSL using WSLg
2. ✅ Installed Claude extension from Chrome Web Store in WSL Chrome
3. ✅ Extension works for web-based Claude interactions
4. ❌ Extension does not expose WebSocket API on port 45454
5. ❌ `claude --chrome` hangs when trying to connect

<!-- section_id: "1aa045ae-2202-4f93-8480-49ce0bc7767a" -->
### Port 45454 Clarification

Port 45454 is used for **OAuth authentication during Claude Code login**, NOT for Chrome extension WebSocket API. This was a red herring in our troubleshooting.

<!-- section_id: "90ad5270-6e48-4c88-b10b-2aae0c3b024a" -->
## Recommended Alternatives for WSL

<!-- section_id: "27cbc39f-59b0-417c-9e65-9972d11e0d76" -->
### Option 1: Playwright MCP (RECOMMENDED)

**Status:** ✅ Already configured in your `.claude.json`

```json
"playwright": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/home/dawson/.cache/ms-playwright",
    "HOME": "/home/dawson"
  }
}
```

**Advantages:**
- Works perfectly in WSL
- Provides full browser automation capabilities
- Supports headless and headful modes
- Can interact with web pages, fill forms, take screenshots
- More programmatic and reliable than manual browser control

**Current Testing:** Agent in progress...

<!-- section_id: "f5833475-b051-4376-96a9-ecef82feb9a7" -->
### Option 2: Chrome DevTools MCP

Configure Chrome on Windows with remote debugging enabled, then connect from WSL:

1. Launch Chrome on Windows with: `chrome.exe --remote-debugging-port=9222`
2. Configure MCP to connect to Windows host IP
3. Use Chrome DevTools Protocol for automation

**Note:** More complex setup, requires networking between WSL and Windows.

<!-- section_id: "acdb322e-807b-4c0f-a30c-a730fd554004" -->
### Option 3: Install Claude Code Natively on Windows

If you need Claude in Chrome features:
- Install Claude Code directly on Windows (not WSL)
- Use PowerShell or Command Prompt instead of WSL terminal
- Full Claude in Chrome integration will work

<!-- section_id: "75395d4d-0824-4a8d-bf65-5b5d739fc108" -->
## Documentation References

- [Claude in Chrome Official Docs](https://code.claude.com/docs/en/chrome)
- [GitHub Issue #14367: Support Claude in Chrome for WSL](https://github.com/anthropics/claude-code/issues/14367)
- [GitHub Issue #14445: Native Host not supported on WSL2](https://github.com/anthropics/claude-code/issues/14445)

<!-- section_id: "2bfef018-83f7-4acb-8723-4b9799eb328a" -->
## Next Steps

1. ✅ Use Playwright MCP for browser automation in WSL
2. ⏳ Monitor GitHub issues for future WSL support
3. 💡 Consider dual setup: WSL for development, Windows Claude Code for Chrome integration if needed

<!-- section_id: "33925d4b-684f-48ae-899b-2fb278bee9f9" -->
## Lessons Learned

1. Always check official documentation for platform compatibility
2. WSL has limitations for native Windows integrations
3. MCP servers provide powerful alternatives to direct integrations
4. Port 45454 is for OAuth, not Chrome extension API
