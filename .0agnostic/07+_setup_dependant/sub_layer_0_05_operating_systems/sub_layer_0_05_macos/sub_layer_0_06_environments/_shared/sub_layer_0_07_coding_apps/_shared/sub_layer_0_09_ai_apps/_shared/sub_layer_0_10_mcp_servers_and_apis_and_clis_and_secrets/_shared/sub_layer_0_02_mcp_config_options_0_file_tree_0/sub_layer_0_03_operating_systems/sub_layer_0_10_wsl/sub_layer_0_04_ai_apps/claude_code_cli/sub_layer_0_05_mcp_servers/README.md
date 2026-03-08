---
resource_id: "d80dbcc5-2e77-4fa9-b688-271674afb375"
resource_type: "readme_document"
resource_name: "README"
---
# MCP Servers Configuration for Claude Code CLI in WSL

This directory contains configuration and documentation for MCP (Model Context Protocol) servers used with Claude Code CLI in WSL environment.

<!-- section_id: "3f79e3e6-e426-41d0-aa47-a04a7e1b6b30" -->
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

<!-- section_id: "5d4cbd59-1bb9-417d-ae12-aadb4bcfeaf8" -->
## Quick Summary

| MCP Server | Status | Notes |
|-----------|--------|-------|
| **Playwright MCP** | ⚠️ Configured | Needs browser path fix |
| **Claude in Chrome** | ❌ Not Supported | WSL incompatible |

<!-- section_id: "10a39aa5-c73a-48bf-b33f-2f75e8895e9f" -->
## Key Findings

<!-- section_id: "f69bf460-0eb6-4300-af77-c250ff142a77" -->
### ✅ Playwright MCP (Recommended for WSL)
- **Configuration:** Already set up in `/home/dawson/.claude.json`
- **Status:** Server starts and responds, but browser detection needs fixing
- **Solution:** Use `browser_install` tool from within Claude Code
- **Documentation:** See `playwright-mcp-test-results.md`

<!-- section_id: "8fd5f2f1-2818-4ee0-8add-49b4b04a5249" -->
### ❌ Claude in Chrome  
- **Status:** Explicitly NOT supported on WSL
- **Reason:** Uses Chrome Native Messaging API incompatible with WSL/Windows boundary
- **Alternative:** Use Playwright MCP instead
- **Documentation:** See `claude_in_chrome/SETUP_FINDINGS.md`

<!-- section_id: "f8a6edb2-bde7-4274-a85f-789af79cafaf" -->
## Quick Start

<!-- section_id: "a5d69ca2-d294-4419-a0f9-1e4700895d07" -->
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

<!-- section_id: "7847a66e-e4e2-47c1-85cf-90fc02622699" -->
## Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright)
- [Claude Code Docs](https://code.claude.com/docs)

**Last Updated:** 2025-12-30
