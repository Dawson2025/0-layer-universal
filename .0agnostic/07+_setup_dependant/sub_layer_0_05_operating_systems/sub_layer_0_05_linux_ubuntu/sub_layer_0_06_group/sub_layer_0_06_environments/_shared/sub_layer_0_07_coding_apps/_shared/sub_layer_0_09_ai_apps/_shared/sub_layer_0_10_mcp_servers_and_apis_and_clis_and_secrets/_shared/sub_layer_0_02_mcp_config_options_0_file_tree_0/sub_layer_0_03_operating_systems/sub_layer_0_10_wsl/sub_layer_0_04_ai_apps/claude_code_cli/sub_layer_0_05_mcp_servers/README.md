---
resource_id: "1c13c9cb-30d1-4d62-bc2a-a48b0ef7d61b"
resource_type: "readme
document"
resource_name: "README"
---
# MCP Servers Configuration for Claude Code CLI in WSL

This directory contains configuration and documentation for MCP (Model Context Protocol) servers used with Claude Code CLI in WSL environment.

<!-- section_id: "4e382231-549e-48b8-b35c-be0df7aea5f9" -->
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

<!-- section_id: "28631efb-dbf8-4df5-9f5b-2850159a0b29" -->
## Quick Summary

| MCP Server | Status | Notes |
|-----------|--------|-------|
| **Playwright MCP** | ⚠️ Configured | Needs browser path fix |
| **Claude in Chrome** | ❌ Not Supported | WSL incompatible |

<!-- section_id: "e7a04def-f64e-4eab-be4f-2f63a9cc1d48" -->
## Key Findings

<!-- section_id: "7e57de63-3845-4d87-a70c-4c6d041707c5" -->
### ✅ Playwright MCP (Recommended for WSL)
- **Configuration:** Already set up in `/home/dawson/.claude.json`
- **Status:** Server starts and responds, but browser detection needs fixing
- **Solution:** Use `browser_install` tool from within Claude Code
- **Documentation:** See `playwright-mcp-test-results.md`

<!-- section_id: "a4750c47-dc76-4703-8979-9aa11c8da55d" -->
### ❌ Claude in Chrome  
- **Status:** Explicitly NOT supported on WSL
- **Reason:** Uses Chrome Native Messaging API incompatible with WSL/Windows boundary
- **Alternative:** Use Playwright MCP instead
- **Documentation:** See `claude_in_chrome/SETUP_FINDINGS.md`

<!-- section_id: "5f396919-bbfa-43d6-b325-593ed5506c54" -->
## Quick Start

<!-- section_id: "ce0b9c5d-755c-42ed-bc96-0f6555bcbd53" -->
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

<!-- section_id: "32b9d392-ee09-440e-b881-808f197bb66a" -->
## Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Playwright MCP GitHub](https://github.com/microsoft/playwright)
- [Claude Code Docs](https://code.claude.com/docs)

**Last Updated:** 2025-12-30
