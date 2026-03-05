---
resource_id: "bf15b58e-73b4-47ac-8cc4-dfe4db00b7cf"
resource_type: "document"
resource_name: "LINUX_UBUNTU_TOOL_ACCESS_ISSUES"
---
# Linux/Ubuntu Universal Tools Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Universal Tools  
**Status**: Platform-specific limitations affecting universal tool access

<!-- section_id: "d50d2f7c-1828-4a85-9d42-ef317c1aabea" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect access to universal tools, particularly those that depend on MCP (Model Context Protocol) servers. These issues impact browser automation tools, development frameworks, and other cross-cutting utilities.

<!-- section_id: "fd10a375-ebe8-4b9b-aa89-a757b82d3916" -->
## Universal Tools Affected by Linux Issues

<!-- section_id: "97cbf7e0-d022-489b-ba64-a5f83428731b" -->
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

<!-- section_id: "35204f75-6472-43d4-8dbf-5a9bcaf19c2e" -->
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

<!-- section_id: "2b4a5b89-996b-402d-9807-68ac10e09ee4" -->
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

<!-- section_id: "d35ecf04-953b-4af3-aa2f-f8a6c6c38aa7" -->
## Tool Access Patterns

<!-- section_id: "3eef1ffd-3945-4831-8710-47dbfd5fa34a" -->
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

<!-- section_id: "18053ef2-fd10-4e32-96f6-775ea108abc6" -->
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

<!-- section_id: "f0acc1c3-fb2b-4a04-b3b4-5f591c5eb361" -->
### Pattern 3: Platform Detection

**Detect Platform and Use Appropriate Tools**:
```javascript
const platform = detect_platform();
const browserTool = platform === "linux" 
  ? "mcp_browser_browser_navigate"
  : "mcp_playwright_browser_navigate";
```

<!-- section_id: "19b67588-23f0-4406-872d-3d0c3d034b32" -->
## Universal Tools Documentation Updates

<!-- section_id: "0f91e556-f164-4ce1-aca8-c68ef45cea78" -->
### Browser Automation Documentation

**Update Required Sections**:
- Tool name references (Playwright → Browser MCP for Linux)
- Example code snippets (Linux-specific versions)
- Troubleshooting guides (Linux-specific issues)
- Platform compatibility notes

<!-- section_id: "5c57afc4-d436-4d3c-9cf4-edd823977e9f" -->
### Framework Documentation

**Update Required Sections**:
- Framework setup instructions (Linux-specific steps)
- Example workflows (Linux tool alternatives)
- Testing guides (Linux tool verification)
- Platform-specific configurations

<!-- section_id: "58d8af05-b9cd-4442-813f-e28b96ad4564" -->
## Tool Configuration

<!-- section_id: "a1bebd0e-4bc6-4eee-a616-7350dbe389a7" -->
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

<!-- section_id: "8d4c25e1-db45-4373-b2d4-b70578c84614" -->
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

<!-- section_id: "746a9854-e391-4b6e-a1b8-c1fbab8ca5d2" -->
## Verification and Testing

<!-- section_id: "44566112-7810-4d39-a3c3-e412abe9adcc" -->
### Verify Tool Access

```bash
# Check which browser MCP tools are available
# In Cursor IDE: Settings → Tools & MCP → Model Context Protocol
# Look for tools prefixed with:
# - mcp_browser_* (should be available)
# - mcp_playwright_* (will NOT be available on Linux)
```

<!-- section_id: "d8ebd47e-7dd3-472d-9ef1-df2a4c0d960d" -->
### Test Tool Usage

1. **Test Browser Navigation**:
   - Try: `mcp_browser_browser_navigate({ url: "https://example.com" })`
   - Should work on Linux
   - Alternative: `mcp_cursor-browser-extension_browser_navigate()` (may have issues)

2. **Test Tool Availability**:
   - Check tool list in Cursor IDE
   - Verify expected tools are present
   - Note any missing tools

<!-- section_id: "7bdefb85-16ee-4f47-8acf-bb616a2f80d9" -->
## Tool Migration Guide

<!-- section_id: "64ed7f14-98bd-4178-b090-926848fa1e5e" -->
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

<!-- section_id: "3699b470-3d38-4998-a7c9-c1d4249b8390" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Browser Automation**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

<!-- section_id: "f7c379a2-5a1d-4dfd-8b98-2b244fd4e788" -->
## References

- Browser Automation Tools: See browser-automation documentation
- MCP Tool Reference: See MCP setup documentation
- Platform Compatibility: Check tool-specific documentation

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
