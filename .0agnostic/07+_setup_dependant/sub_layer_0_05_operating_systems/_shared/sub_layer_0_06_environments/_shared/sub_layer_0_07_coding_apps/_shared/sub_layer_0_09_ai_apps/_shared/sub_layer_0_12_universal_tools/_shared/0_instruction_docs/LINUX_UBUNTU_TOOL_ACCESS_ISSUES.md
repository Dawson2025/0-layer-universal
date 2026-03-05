---
resource_id: "691a85f2-6709-4bc9-84d3-61462df0eed6"
resource_type: "document"
resource_name: "LINUX_UBUNTU_TOOL_ACCESS_ISSUES"
---
# Linux/Ubuntu Universal Tools Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Universal Tools  
**Status**: Platform-specific limitations affecting universal tool access

<!-- section_id: "c309a5c0-0a1a-4059-9f4f-d69f116f9705" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect access to universal tools, particularly those that depend on MCP (Model Context Protocol) servers. These issues impact browser automation tools, development frameworks, and other cross-cutting utilities.

<!-- section_id: "a6b019d7-5c81-40da-8173-7a68323d7b82" -->
## Universal Tools Affected by Linux Issues

<!-- section_id: "429ebace-5c96-472a-aa24-dcf383c963e0" -->
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

<!-- section_id: "b5a8ccc6-9285-445c-b1ad-58d7256fb3b0" -->
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

<!-- section_id: "546fe1bb-8d77-4f1a-8750-1a3dede420b3" -->
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

<!-- section_id: "77d7fabd-6e25-4dd3-b8b2-0d6c7ddf48f3" -->
## Tool Access Patterns

<!-- section_id: "bb59fdf6-830b-44b9-ab51-946cec1d111a" -->
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

<!-- section_id: "c047f91d-a67e-42bf-af8e-a07fc07e6f61" -->
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

<!-- section_id: "a379933e-efef-4d10-a7ae-2cd0b8a27ed2" -->
### Pattern 3: Platform Detection

**Detect Platform and Use Appropriate Tools**:
```javascript
const platform = detect_platform();
const browserTool = platform === "linux" 
  ? "mcp_browser_browser_navigate"
  : "mcp_playwright_browser_navigate";
```

<!-- section_id: "5fd33663-f099-4709-82d4-272d7e1023c5" -->
## Universal Tools Documentation Updates

<!-- section_id: "2dd0a7f2-6d68-42d3-9136-91cdced7a7d8" -->
### Browser Automation Documentation

**Update Required Sections**:
- Tool name references (Playwright → Browser MCP for Linux)
- Example code snippets (Linux-specific versions)
- Troubleshooting guides (Linux-specific issues)
- Platform compatibility notes

<!-- section_id: "067f0384-aaf1-4ab7-8813-9fce08425826" -->
### Framework Documentation

**Update Required Sections**:
- Framework setup instructions (Linux-specific steps)
- Example workflows (Linux tool alternatives)
- Testing guides (Linux tool verification)
- Platform-specific configurations

<!-- section_id: "a28775bf-ef00-4a52-86f9-47a2bd66594d" -->
## Tool Configuration

<!-- section_id: "a2b2eed0-3edd-4363-8743-c66fad362729" -->
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

<!-- section_id: "9598b329-f730-4e81-a55d-c012c08534a7" -->
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

<!-- section_id: "dc88e7f2-eb4f-4fae-b1b7-4862ec298a84" -->
## Verification and Testing

<!-- section_id: "6042c0f9-942c-4c82-9a25-a79de2766175" -->
### Verify Tool Access

```bash
# Check which browser MCP tools are available
# In Cursor IDE: Settings → Tools & MCP → Model Context Protocol
# Look for tools prefixed with:
# - mcp_browser_* (should be available)
# - mcp_playwright_* (will NOT be available on Linux)
```

<!-- section_id: "78438075-ba64-4510-af24-c96ee1c78250" -->
### Test Tool Usage

1. **Test Browser Navigation**:
   - Try: `mcp_browser_browser_navigate({ url: "https://example.com" })`
   - Should work on Linux
   - Alternative: `mcp_cursor-browser-extension_browser_navigate()` (may have issues)

2. **Test Tool Availability**:
   - Check tool list in Cursor IDE
   - Verify expected tools are present
   - Note any missing tools

<!-- section_id: "3771ce65-38e6-4d75-83da-3b91c7851e03" -->
## Tool Migration Guide

<!-- section_id: "a4db66a0-37bd-4df3-9344-81e1ff40009c" -->
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

<!-- section_id: "7c633119-fb0e-412b-91c5-1151809a248c" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Browser Automation**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

<!-- section_id: "f27c54da-e95d-425b-92ec-b7a97373db58" -->
## References

- Browser Automation Tools: See browser-automation documentation
- MCP Tool Reference: See MCP setup documentation
- Platform Compatibility: Check tool-specific documentation

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
