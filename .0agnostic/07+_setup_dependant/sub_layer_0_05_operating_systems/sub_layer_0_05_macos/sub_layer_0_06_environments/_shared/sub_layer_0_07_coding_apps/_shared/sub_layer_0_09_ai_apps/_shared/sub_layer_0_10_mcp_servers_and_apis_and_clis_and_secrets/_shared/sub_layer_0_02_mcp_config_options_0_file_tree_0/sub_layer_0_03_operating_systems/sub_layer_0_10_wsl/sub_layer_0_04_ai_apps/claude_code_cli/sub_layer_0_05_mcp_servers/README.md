---
resource_id: "d80dbcc5-2e77-4fa9-b688-271674afb375"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers Configuration for Claude Code CLI in WSL

This directory contains configuration and documentation for MCP (Model Context Protocol) servers used with Claude Code CLI in WSL environment.

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

## Quick Summary

| MCP Server | Status | Notes |
|-----------|--------|-------|
| **Playwright MCP** | ⚠️ Configured | Needs browser path fix |
| **Claude in Chrome** | ❌ Not Supported | WSL incompatible |

## Key Findings

### ✅ Playwright MCP (Recommended for WSL)
- **Configuration:** Already set up in `/home/dawson/.claude.json`
- **Status:** Server starts and responds, but browser detection needs fixing
- **Solution:** Use `browser_install` tool from within Claude Code
- **Documentation:** See `playwright-mcp-test-results.md`

### ❌ Claude in Chrome  
- **Status:** Explicitly NOT supported on WSL
- **Reason:** Uses Chrome Native Messaging API incompatible with WSL/Windows boundary
- **Alternative:** Use Playwright MCP instead
- **Documentation:** See `claude_in_chrome/SETUP_FINDINGS.md`

## Quick Start

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

## Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright)
- [Claude Code Docs](https://code.claude.com/docs)

**Last Updated:** 2025-12-30
