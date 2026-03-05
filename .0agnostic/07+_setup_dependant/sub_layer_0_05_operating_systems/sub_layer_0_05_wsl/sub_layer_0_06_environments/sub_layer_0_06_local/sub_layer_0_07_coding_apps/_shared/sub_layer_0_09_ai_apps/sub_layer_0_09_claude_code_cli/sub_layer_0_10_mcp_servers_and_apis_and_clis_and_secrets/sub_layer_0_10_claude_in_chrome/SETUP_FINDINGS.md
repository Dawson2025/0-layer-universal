---
resource_id: "4d405957-887c-44ba-9bff-81bcfe98c3d3"
resource_type: "document"
resource_name: "SETUP_FINDINGS"
---
# Claude in Chrome Setup Findings for WSL

**Date:** 2025-12-30
**Environment:** WSL2 (Ubuntu 24.04) on Windows
**Claude Code Version:** 2.0.76

<!-- section_id: "6436c6c3-c76c-488f-8f43-7cf624655a6f" -->
## Critical Finding: WSL Not Supported

**Status:** ❌ **NOT SUPPORTED**

According to official Claude Code documentation, Claude in Chrome integration is **explicitly not supported on WSL**.

<!-- section_id: "35cd6487-cca3-469e-b7c2-45e3e8cc2818" -->
### Why It Doesn't Work

1. **Native Messaging API Limitation**: Claude in Chrome uses Chrome's Native Messaging API to communicate between the extension and Claude Code CLI
2. **WSL Incompatibility**: The native messaging host installation and functionality do not work when Claude Code runs in WSL, even if Chrome is installed on Windows
3. **Architecture Mismatch**: The extension expects to communicate with a native Windows process, not a WSL Linux process

<!-- section_id: "b90ca68b-978e-49b2-b6fc-24c9a72abba9" -->
### What We Tried

1. ✅ Installed Chrome in WSL using WSLg
2. ✅ Installed Claude extension from Chrome Web Store in WSL Chrome
3. ✅ Extension works for web-based Claude interactions
4. ❌ Extension does not expose WebSocket API on port 45454
5. ❌ `claude --chrome` hangs when trying to connect

<!-- section_id: "1596381b-1b50-4bf1-aa68-77803554b871" -->
### Port 45454 Clarification

Port 45454 is used for **OAuth authentication during Claude Code login**, NOT for Chrome extension WebSocket API. This was a red herring in our troubleshooting.

<!-- section_id: "ddfa186a-d365-41df-a35e-4b53311b1900" -->
## Recommended Alternatives for WSL

<!-- section_id: "3ac714d3-67e1-4945-b781-96633b592ac5" -->
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

<!-- section_id: "67fe3459-43c5-49ec-b622-e2743f62054f" -->
### Option 2: Chrome DevTools MCP

Configure Chrome on Windows with remote debugging enabled, then connect from WSL:

1. Launch Chrome on Windows with: `chrome.exe --remote-debugging-port=9222`
2. Configure MCP to connect to Windows host IP
3. Use Chrome DevTools Protocol for automation

**Note:** More complex setup, requires networking between WSL and Windows.

<!-- section_id: "55b844af-4a65-4b2d-8a0d-384e9015c47d" -->
### Option 3: Install Claude Code Natively on Windows

If you need Claude in Chrome features:
- Install Claude Code directly on Windows (not WSL)
- Use PowerShell or Command Prompt instead of WSL terminal
- Full Claude in Chrome integration will work

<!-- section_id: "4b609e34-e83e-4568-a1ac-7a2c07ce4804" -->
## Documentation References

- [Claude in Chrome Official Docs](https://code.claude.com/docs/en/chrome)
- [GitHub Issue #14367: Support Claude in Chrome for WSL](https://github.com/anthropics/claude-code/issues/14367)
- [GitHub Issue #14445: Native Host not supported on WSL2](https://github.com/anthropics/claude-code/issues/14445)

<!-- section_id: "c1623acf-e7d7-427d-9174-1b7f1e35a97e" -->
## Next Steps

1. ✅ Use Playwright MCP for browser automation in WSL
2. ⏳ Monitor GitHub issues for future WSL support
3. 💡 Consider dual setup: WSL for development, Windows Claude Code for Chrome integration if needed

<!-- section_id: "460bbf7e-eeb4-4919-88cf-23d799791d07" -->
## Lessons Learned

1. Always check official documentation for platform compatibility
2. WSL has limitations for native Windows integrations
3. MCP servers provide powerful alternatives to direct integrations
4. Port 45454 is for OAuth, not Chrome extension API
