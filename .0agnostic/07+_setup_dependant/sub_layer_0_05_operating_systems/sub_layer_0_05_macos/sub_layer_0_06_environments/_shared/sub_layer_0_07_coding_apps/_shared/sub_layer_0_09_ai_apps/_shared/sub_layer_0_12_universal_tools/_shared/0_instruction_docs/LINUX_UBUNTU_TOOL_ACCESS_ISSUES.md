---
resource_id: "e42b5285-9fd9-409b-a5a8-5a0ae95bdacf"
resource_type: "document"
resource_name: "LINUX_UBUNTU_TOOL_ACCESS_ISSUES"
---
# Linux/Ubuntu Universal Tools Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Universal Tools  
**Status**: Platform-specific limitations affecting universal tool access

<!-- section_id: "ee40f523-449b-4290-8af0-b5fe586e8205" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect access to universal tools, particularly those that depend on MCP (Model Context Protocol) servers. These issues impact browser automation tools, development frameworks, and other cross-cutting utilities.

<!-- section_id: "4c704b79-4d99-4f3c-8205-e531a4840d45" -->
## Universal Tools Affected by Linux Issues

<!-- section_id: "f01bf891-2979-433c-bf05-6889dc4dcd7b" -->
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

<!-- section_id: "62a0b146-e37f-4fc1-9e3d-f34ca8b2ad24" -->
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

<!-- section_id: "ae729911-ea74-4407-b069-a80469c6746a" -->
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

<!-- section_id: "9ba0d77c-c356-4aaf-a6cc-24cd57ea2415" -->
## Tool Access Patterns

<!-- section_id: "15df9f73-2bf6-45cc-ae11-5427eecc48b2" -->
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

<!-- section_id: "f8782a6d-90e0-4e45-8977-b9c15cac0d98" -->
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

<!-- section_id: "065fe6ae-c835-44a3-a30e-f5e18b99e0d5" -->
### Pattern 3: Platform Detection

**Detect Platform and Use Appropriate Tools**:
```javascript
const platform = detect_platform();
const browserTool = platform === "linux" 
  ? "mcp_browser_browser_navigate"
  : "mcp_playwright_browser_navigate";
```

<!-- section_id: "c1661734-58b1-432b-b672-119fbd147095" -->
## Universal Tools Documentation Updates

<!-- section_id: "788cae72-ebc1-4cfc-b10c-e71d7ddde63a" -->
### Browser Automation Documentation

**Update Required Sections**:
- Tool name references (Playwright → Browser MCP for Linux)
- Example code snippets (Linux-specific versions)
- Troubleshooting guides (Linux-specific issues)
- Platform compatibility notes

<!-- section_id: "063c2db0-068f-43b3-8fff-a726e378f5a5" -->
### Framework Documentation

**Update Required Sections**:
- Framework setup instructions (Linux-specific steps)
- Example workflows (Linux tool alternatives)
- Testing guides (Linux tool verification)
- Platform-specific configurations

<!-- section_id: "333139f3-2ddd-4746-a3ab-5412da18ac15" -->
## Tool Configuration

<!-- section_id: "c035ef82-8a65-4183-a217-09ac0951e0a3" -->
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

<!-- section_id: "77fcf7b0-4fb9-430b-9149-3d770ce64ee4" -->
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

<!-- section_id: "1d016525-efd1-4abe-9f51-fec10b2d40f7" -->
## Verification and Testing

<!-- section_id: "6e428415-bf66-4a3c-8eb0-0ec9c34c8d4c" -->
### Verify Tool Access

```bash
# Check which browser MCP tools are available
# In Cursor IDE: Settings → Tools & MCP → Model Context Protocol
# Look for tools prefixed with:
# - mcp_browser_* (should be available)
# - mcp_playwright_* (will NOT be available on Linux)
```

<!-- section_id: "3c66f843-8fd2-433e-b1a2-66d7bcf7e0a8" -->
### Test Tool Usage

1. **Test Browser Navigation**:
   - Try: `mcp_browser_browser_navigate({ url: "https://example.com" })`
   - Should work on Linux
   - Alternative: `mcp_cursor-browser-extension_browser_navigate()` (may have issues)

2. **Test Tool Availability**:
   - Check tool list in Cursor IDE
   - Verify expected tools are present
   - Note any missing tools

<!-- section_id: "56c2da6f-9f68-41d9-ab5a-1f286f742d5a" -->
## Tool Migration Guide

<!-- section_id: "e7101d75-d414-4414-ba5d-876b12416018" -->
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

<!-- section_id: "4f478a4b-6c97-4765-84ed-521be55c9153" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Browser Automation**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

<!-- section_id: "c7656188-78b4-419d-824e-8d4f8371691b" -->
## References

- Browser Automation Tools: See browser-automation documentation
- MCP Tool Reference: See MCP setup documentation
- Platform Compatibility: Check tool-specific documentation

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
