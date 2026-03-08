---
resource_id: "b6bf4e45-9517-401a-a341-6ed9a7983046"
resource_type: "readme_document"
resource_name: "README"
---
# MCP Servers Configuration for Claude Code CLI in WSL

This directory contains configuration and documentation for MCP (Model Context Protocol) servers used with Claude Code CLI in WSL environment.

<!-- section_id: "625694a4-98c2-4363-a6c6-fbd357850d84" -->
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

<!-- section_id: "41eec61c-b954-4dcb-81fb-b84d2148b09b" -->
## Quick Summary

| MCP Server | Status | Notes |
|-----------|--------|-------|
| **Playwright MCP** | ⚠️ Configured | Needs browser path fix |
| **Claude in Chrome** | ❌ Not Supported | WSL incompatible |

<!-- section_id: "3b89aca7-7368-40ab-a503-2a652970d375" -->
## Key Findings

<!-- section_id: "4aed1bdc-3084-47b0-ab7a-3139a290e2fd" -->
### ✅ Playwright MCP (Recommended for WSL)
- **Configuration:** Already set up in `/home/dawson/.claude.json`
- **Status:** Server starts and responds, but browser detection needs fixing
- **Solution:** Use `browser_install` tool from within Claude Code
- **Documentation:** See `playwright-mcp-test-results.md`

<!-- section_id: "f9774edd-2e31-4c6b-84c8-ad19871fe6df" -->
### ❌ Claude in Chrome  
- **Status:** Explicitly NOT supported on WSL
- **Reason:** Uses Chrome Native Messaging API incompatible with WSL/Windows boundary
- **Alternative:** Use Playwright MCP instead
- **Documentation:** See `claude_in_chrome/SETUP_FINDINGS.md`

<!-- section_id: "d114ba7a-998b-4f7f-8513-227b3fe5ad03" -->
## Quick Start

<!-- section_id: "48ae64f7-d888-40b6-a08e-faa3bdfd7f67" -->
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

<!-- section_id: "5eec490a-26ae-452d-95c1-4b5d89c12283" -->
## Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright)
- [Claude Code Docs](https://code.claude.com/docs)

**Last Updated:** 2025-12-30
