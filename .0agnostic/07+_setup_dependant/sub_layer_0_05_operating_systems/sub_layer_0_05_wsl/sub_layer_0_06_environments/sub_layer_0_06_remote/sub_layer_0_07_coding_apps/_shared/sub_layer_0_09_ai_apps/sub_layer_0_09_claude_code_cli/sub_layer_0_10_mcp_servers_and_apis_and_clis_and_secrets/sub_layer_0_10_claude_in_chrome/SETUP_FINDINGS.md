---
resource_id: "d84567ad-7440-48a3-b786-bcfdffe1b730"
resource_type: "document"
resource_name: "SETUP_FINDINGS"
---
# Claude in Chrome Setup Findings for WSL

**Date:** 2025-12-30
**Environment:** WSL2 (Ubuntu 24.04) on Windows
**Claude Code Version:** 2.0.76

<!-- section_id: "3f1a4cc5-7d3a-4657-ab82-0b5a2ee28402" -->
## Critical Finding: WSL Not Supported

**Status:** ❌ **NOT SUPPORTED**

According to official Claude Code documentation, Claude in Chrome integration is **explicitly not supported on WSL**.

<!-- section_id: "c6015753-cf80-448b-a365-f08f66012b14" -->
### Why It Doesn't Work

1. **Native Messaging API Limitation**: Claude in Chrome uses Chrome's Native Messaging API to communicate between the extension and Claude Code CLI
2. **WSL Incompatibility**: The native messaging host installation and functionality do not work when Claude Code runs in WSL, even if Chrome is installed on Windows
3. **Architecture Mismatch**: The extension expects to communicate with a native Windows process, not a WSL Linux process

<!-- section_id: "aae293f8-1b43-49c6-bed0-39bf134d8650" -->
### What We Tried

1. ✅ Installed Chrome in WSL using WSLg
2. ✅ Installed Claude extension from Chrome Web Store in WSL Chrome
3. ✅ Extension works for web-based Claude interactions
4. ❌ Extension does not expose WebSocket API on port 45454
5. ❌ `claude --chrome` hangs when trying to connect

<!-- section_id: "fd7d7ccd-a81b-48d4-a2a7-2a37d53db902" -->
### Port 45454 Clarification

Port 45454 is used for **OAuth authentication during Claude Code login**, NOT for Chrome extension WebSocket API. This was a red herring in our troubleshooting.

<!-- section_id: "69461caf-36e2-421f-9aa0-378760391cb8" -->
## Recommended Alternatives for WSL

<!-- section_id: "747c74cf-f4e9-4111-9236-c3ca998f3924" -->
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

<!-- section_id: "68f4d6f6-8c91-443b-8a8d-8ec2b2e0abee" -->
### Option 2: Chrome DevTools MCP

Configure Chrome on Windows with remote debugging enabled, then connect from WSL:

1. Launch Chrome on Windows with: `chrome.exe --remote-debugging-port=9222`
2. Configure MCP to connect to Windows host IP
3. Use Chrome DevTools Protocol for automation

**Note:** More complex setup, requires networking between WSL and Windows.

<!-- section_id: "95050f2b-8269-48d0-a086-9b98f66c1357" -->
### Option 3: Install Claude Code Natively on Windows

If you need Claude in Chrome features:
- Install Claude Code directly on Windows (not WSL)
- Use PowerShell or Command Prompt instead of WSL terminal
- Full Claude in Chrome integration will work

<!-- section_id: "603de996-257d-4a3a-a809-a0626085d92b" -->
## Documentation References

- [Claude in Chrome Official Docs](https://code.claude.com/docs/en/chrome)
- [GitHub Issue #14367: Support Claude in Chrome for WSL](https://github.com/anthropics/claude-code/issues/14367)
- [GitHub Issue #14445: Native Host not supported on WSL2](https://github.com/anthropics/claude-code/issues/14445)

<!-- section_id: "87007f72-4c52-4b99-9eb6-eb37d218d4c0" -->
## Next Steps

1. ✅ Use Playwright MCP for browser automation in WSL
2. ⏳ Monitor GitHub issues for future WSL support
3. 💡 Consider dual setup: WSL for development, Windows Claude Code for Chrome integration if needed

<!-- section_id: "44965413-5aa3-4ee8-b95d-e7317725c447" -->
## Lessons Learned

1. Always check official documentation for platform compatibility
2. WSL has limitations for native Windows integrations
3. MCP servers provide powerful alternatives to direct integrations
4. Port 45454 is for OAuth, not Chrome extension API
