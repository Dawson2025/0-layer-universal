---
resource_id: "03d66dcd-c4db-4d48-b86f-4640ed688e15"
resource_type: "document"
resource_name: "SETUP_FINDINGS"
---
# Claude in Chrome Setup Findings for WSL

**Date:** 2025-12-30
**Environment:** WSL2 (Ubuntu 24.04) on Windows
**Claude Code Version:** 2.0.76

<!-- section_id: "277fbe76-fae6-4ecc-b290-19e47b7c4490" -->
## Critical Finding: WSL Not Supported

**Status:** ❌ **NOT SUPPORTED**

According to official Claude Code documentation, Claude in Chrome integration is **explicitly not supported on WSL**.

<!-- section_id: "5698e9e4-9625-40ca-a118-c647dcb43e64" -->
### Why It Doesn't Work

1. **Native Messaging API Limitation**: Claude in Chrome uses Chrome's Native Messaging API to communicate between the extension and Claude Code CLI
2. **WSL Incompatibility**: The native messaging host installation and functionality do not work when Claude Code runs in WSL, even if Chrome is installed on Windows
3. **Architecture Mismatch**: The extension expects to communicate with a native Windows process, not a WSL Linux process

<!-- section_id: "10643db4-db1e-454b-aa25-1766a3445e23" -->
### What We Tried

1. ✅ Installed Chrome in WSL using WSLg
2. ✅ Installed Claude extension from Chrome Web Store in WSL Chrome
3. ✅ Extension works for web-based Claude interactions
4. ❌ Extension does not expose WebSocket API on port 45454
5. ❌ `claude --chrome` hangs when trying to connect

<!-- section_id: "7010a733-1ff1-47a4-ac26-5769af19c087" -->
### Port 45454 Clarification

Port 45454 is used for **OAuth authentication during Claude Code login**, NOT for Chrome extension WebSocket API. This was a red herring in our troubleshooting.

<!-- section_id: "37e3eadb-4678-4654-b8ce-1c19bcd82678" -->
## Recommended Alternatives for WSL

<!-- section_id: "779cadbb-6331-4396-8a46-6224c9f37d53" -->
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

<!-- section_id: "572eda3b-d9de-45fd-8cef-b55d5fe4c745" -->
### Option 2: Chrome DevTools MCP

Configure Chrome on Windows with remote debugging enabled, then connect from WSL:

1. Launch Chrome on Windows with: `chrome.exe --remote-debugging-port=9222`
2. Configure MCP to connect to Windows host IP
3. Use Chrome DevTools Protocol for automation

**Note:** More complex setup, requires networking between WSL and Windows.

<!-- section_id: "bb937be6-48df-4f34-a8f7-7674c298d44a" -->
### Option 3: Install Claude Code Natively on Windows

If you need Claude in Chrome features:
- Install Claude Code directly on Windows (not WSL)
- Use PowerShell or Command Prompt instead of WSL terminal
- Full Claude in Chrome integration will work

<!-- section_id: "8840837d-b903-4e9a-8ed2-f1e2108fafda" -->
## Documentation References

- [Claude in Chrome Official Docs](https://code.claude.com/docs/en/chrome)
- [GitHub Issue #14367: Support Claude in Chrome for WSL](https://github.com/anthropics/claude-code/issues/14367)
- [GitHub Issue #14445: Native Host not supported on WSL2](https://github.com/anthropics/claude-code/issues/14445)

<!-- section_id: "bea22f20-c5b8-41b4-ad92-0bbf569744e3" -->
## Next Steps

1. ✅ Use Playwright MCP for browser automation in WSL
2. ⏳ Monitor GitHub issues for future WSL support
3. 💡 Consider dual setup: WSL for development, Windows Claude Code for Chrome integration if needed

<!-- section_id: "11c03c40-5346-40bc-a1a6-7b51243d38f5" -->
## Lessons Learned

1. Always check official documentation for platform compatibility
2. WSL has limitations for native Windows integrations
3. MCP servers provide powerful alternatives to direct integrations
4. Port 45454 is for OAuth, not Chrome extension API
