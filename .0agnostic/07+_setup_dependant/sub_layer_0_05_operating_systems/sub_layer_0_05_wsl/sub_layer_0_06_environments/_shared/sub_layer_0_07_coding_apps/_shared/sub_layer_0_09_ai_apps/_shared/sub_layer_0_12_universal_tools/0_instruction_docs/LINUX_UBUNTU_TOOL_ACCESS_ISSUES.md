---
resource_id: "5629938e-a6ef-4455-8e8f-62ac81dbe8ec"
resource_type: "document"
resource_name: "LINUX_UBUNTU_TOOL_ACCESS_ISSUES"
---
# Linux/Ubuntu Universal Tools Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Universal Tools  
**Status**: Platform-specific limitations affecting universal tool access

<!-- section_id: "8227d581-fdf3-4e8e-91f7-baa2bb0507ca" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect access to universal tools, particularly those that depend on MCP (Model Context Protocol) servers. These issues impact browser automation tools, development frameworks, and other cross-cutting utilities.

<!-- section_id: "c4304e4e-1070-40dd-901e-44c056bc21a7" -->
## Universal Tools Affected by Linux Issues

<!-- section_id: "210005e7-4930-4a73-b2c8-fcd4eafecce4" -->
### 1. Browser Automation Tools

**Problem**: Browser automation tools that depend on Playwright MCP are not available on Linux.

**Affected Tools**:
- Playwright-based browser automation scripts
- Tools expecting `mcp_playwright_*` tool access
- Documentation referencing Playwright MCP tools

**Impact**:
- Browser automation workflows must use alternative tools
- Scripts and frameworks need Linux-specific adaptations
- Documentation must be updated with Linux workarounds

**Solution**: 
- Use `mcp_browser_*` tools instead of `mcp_playwright_*`
- Update tool references in scripts and documentation
- Provide Linux-specific tool usage examples

<!-- section_id: "65a58cd7-0eb1-44ad-bfd8-4b3e32271cac" -->
### 2. Development Frameworks

**Problem**: AI development frameworks that assume Playwright MCP availability may not work on Linux.

**Affected Frameworks**:
- Frameworks with Playwright MCP dependencies
- Browser automation testing frameworks
- Tools expecting standard MCP tool naming

**Impact**:
- Framework examples may not work on Linux
- Testing workflows may need adaptation
- Framework documentation may need Linux-specific sections

**Solution**:
- Update frameworks to support alternative browser MCP tools
- Provide Linux-specific framework configurations
- Document Linux workarounds in framework guides

<!-- section_id: "0ed3cf0d-1d41-4cdf-874f-8506fdb80064" -->
### 3. Cross-Cutting Utilities

**Problem**: Universal utilities that depend on MCP tools may have Linux-specific limitations.

**Affected Utilities**:
- Browser automation utilities
- Testing scripts
- Development workflow tools

**Impact**:
- Utilities may fail with "Tool not found" errors
- Scripts may need Linux-specific tool name updates
- Workflows may require alternative tool paths

<!-- section_id: "0b313f7a-8a46-4448-b585-df46b0f45ac2" -->
## Tool Access Patterns

<!-- section_id: "fae86ba3-abc4-4390-bd40-f19ae48401dd" -->
### Pattern 1: Browser Automation

**Standard (Windows/macOS)**:
```javascript
// Use Playwright MCP tools
mcp_playwright_browser_navigate({ url: "https://example.com" })
mcp_playwright_browser_click({ element: "button" })
```

**Linux Workaround**:
```javascript
// Use Browser MCP tools instead
mcp_browser_browser_navigate({ url: "https://example.com" })
mcp_browser_browser_click({ element: "button" })
```

<!-- section_id: "1b8f5d03-0016-4295-8e2c-6627219e672b" -->
### Pattern 2: Tool Availability Check

**Before Using Tools**:
```javascript
// Check if Playwright tools are available
if (tool_available("mcp_playwright_browser_navigate")) {
  // Use Playwright
} else if (tool_available("mcp_browser_browser_navigate")) {
  // Use Browser MCP (Linux fallback)
} else {
  // Error: No browser automation available
}
```

<!-- section_id: "2d279744-bca4-493a-b6a5-23269c61f6e0" -->
### Pattern 3: Platform Detection

**Detect Platform and Use Appropriate Tools**:
```javascript
const platform = detect_platform();
const browserTool = platform === "linux" 
  ? "mcp_browser_browser_navigate"
  : "mcp_playwright_browser_navigate";
```

<!-- section_id: "332b4361-13c6-4019-afef-cc96720028a5" -->
## Universal Tools Documentation Updates

<!-- section_id: "c7d06d97-e6e5-4c56-beb6-78b22f6ea3bd" -->
### Browser Automation Documentation

**Update Required Sections**:
- Tool name references (Playwright → Browser MCP for Linux)
- Example code snippets (Linux-specific versions)
- Troubleshooting guides (Linux-specific issues)
- Platform compatibility notes

<!-- section_id: "8ed3c69c-a284-48d6-97c7-9ce920413767" -->
### Framework Documentation

**Update Required Sections**:
- Framework setup instructions (Linux-specific steps)
- Example workflows (Linux tool alternatives)
- Testing guides (Linux tool verification)
- Platform-specific configurations

<!-- section_id: "4a8ca398-dfa0-439e-87cf-b3f5b9a6516c" -->
## Tool Configuration

<!-- section_id: "e638e39a-6925-428c-a382-4d6608d13286" -->
### Browser Automation Tools

**Linux Configuration**:
```json
{
  "browserAutomation": {
    "platform": "linux",
    "toolPrefix": "mcp_browser_",
    "fallbackTools": ["mcp_cursor-browser-extension_"],
    "excludedTools": ["mcp_playwright_"]
  }
}
```

<!-- section_id: "3673b6d0-9c2c-4583-a378-5ff104cabc1d" -->
### Development Framework Configuration

**Linux-Specific Settings**:
```json
{
  "framework": {
    "platform": "linux",
    "browserTools": {
      "primary": "mcp_browser_",
      "fallback": "mcp_cursor-browser-extension_"
    },
    "skipPlaywright": true
  }
}
```

<!-- section_id: "46309a44-0ac0-4a83-ace2-fe17b56d938b" -->
## Verification and Testing

<!-- section_id: "11827014-d950-4ff9-8b4e-ebaec12f150f" -->
### Verify Tool Access

```bash
# Check which browser MCP tools are available
# In Cursor IDE: Settings → Tools & MCP → Model Context Protocol
# Look for tools prefixed with:
# - mcp_browser_* (should be available)
# - mcp_playwright_* (will NOT be available on Linux)
```

<!-- section_id: "2a9f19c1-a658-4ef9-98f1-6f47c24790f5" -->
### Test Tool Usage

1. **Test Browser Navigation**:
   - Try: `mcp_browser_browser_navigate({ url: "https://example.com" })`
   - Should work on Linux
   - Alternative: `mcp_cursor-browser-extension_browser_navigate()` (may have issues)

2. **Test Tool Availability**:
   - Check tool list in Cursor IDE
   - Verify expected tools are present
   - Note any missing tools

<!-- section_id: "95e22242-aa38-4821-a8ab-1d60a2d85458" -->
## Tool Migration Guide

<!-- section_id: "9a03cf92-bff3-42a7-8348-7b6b7a36caca" -->
### Migrating from Playwright to Browser MCP

**Step 1**: Identify Playwright tool usage
```javascript
// Find all mcp_playwright_* tool calls
grep -r "mcp_playwright_" .
```

**Step 2**: Replace with Browser MCP equivalents
```javascript
// Replace mcp_playwright_browser_navigate
// With mcp_browser_browser_navigate
```

**Step 3**: Update tool parameters
```javascript
// Some parameters may differ between tools
// Check tool documentation for differences
```

**Step 4**: Test on Linux
```bash
# Verify tools work on Linux
# Test all browser automation workflows
```

<!-- section_id: "793ec745-5286-4851-8e13-7cce939227c2" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Browser Automation**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

<!-- section_id: "fad1450d-8d26-454b-84f1-da77f44cdcba" -->
## References

- Browser Automation Tools: See browser-automation documentation
- MCP Tool Reference: See MCP setup documentation
- Platform Compatibility: Check tool-specific documentation

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
