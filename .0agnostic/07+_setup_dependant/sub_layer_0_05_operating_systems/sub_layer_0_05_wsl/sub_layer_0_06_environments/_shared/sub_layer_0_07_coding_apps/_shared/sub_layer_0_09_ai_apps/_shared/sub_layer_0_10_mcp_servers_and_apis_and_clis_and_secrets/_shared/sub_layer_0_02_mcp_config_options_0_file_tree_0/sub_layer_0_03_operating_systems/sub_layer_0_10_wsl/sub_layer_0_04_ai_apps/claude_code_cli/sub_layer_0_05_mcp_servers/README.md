---
resource_id: "9bf4a4f9-7398-497c-af07-e41131ca2918"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers Configuration for Claude Code CLI in WSL

This directory contains configuration and documentation for MCP (Model Context Protocol) servers used with Claude Code CLI in WSL environment.

<!-- section_id: "846f99f2-b7df-4304-bc8b-2fe86b1ac56b" -->
## Directory Structure

```
0.05_mcp_servers/
├── README.md                          # This file  
├── claude_in_chrome/                  # Claude in Chrome investigation
│   ├── SETUP_FINDINGS.md             # NOT SUPPORTED in WSL
│   └── screenshots/                   # Investigation screenshots
├── playwright-mcp-test-results.md    # Playwright MCP test documentation
└── (other MCP servers to be added)
```

<!-- section_id: "b308ad51-ad30-4c94-adf3-f3335d617219" -->
## Quick Summary

| MCP Server | Status | Notes |
|-----------|--------|-------|
| **Playwright MCP** | ⚠️ Configured | Needs browser path fix |
| **Claude in Chrome** | ❌ Not Supported | WSL incompatible |

<!-- section_id: "ca28e5a7-7ee8-47d0-9db9-1e37b884b275" -->
## Key Findings

<!-- section_id: "1533adad-208a-4d64-8ea7-f61ae165d94b" -->
### ✅ Playwright MCP (Recommended for WSL)
- **Configuration:** Already set up in `/home/dawson/.claude.json`
- **Status:** Server starts and responds, but browser detection needs fixing
- **Solution:** Use `browser_install` tool from within Claude Code
- **Documentation:** See `playwright-mcp-test-results.md`

<!-- section_id: "e46d5071-7959-4792-92c4-f592b4e143fe" -->
### ❌ Claude in Chrome  
- **Status:** Explicitly NOT supported on WSL
- **Reason:** Uses Chrome Native Messaging API incompatible with WSL/Windows boundary
- **Alternative:** Use Playwright MCP instead
- **Documentation:** See `claude_in_chrome/SETUP_FINDINGS.md`

<!-- section_id: "5eeda53e-7e85-446c-b80a-5fe00f2c25c3" -->
## Quick Start

<!-- section_id: "c09638b0-97fa-42b7-97b4-49a126b639df" -->
### Using Playwright MCP

1. From Claude Code, run:
   ```
   Ask Claude to use the browser_install tool
   ```

2. Once installed, Playwright tools will work for:
   - Web navigation
   - Form filling
   - Screenshots
   - JavaScript execution
   - Full browser automation

<!-- section_id: "6fb25061-1967-4776-87e8-60f12df3aa89" -->
## Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright)
- [Claude Code Docs](https://code.claude.com/docs)

**Last Updated:** 2025-12-30
