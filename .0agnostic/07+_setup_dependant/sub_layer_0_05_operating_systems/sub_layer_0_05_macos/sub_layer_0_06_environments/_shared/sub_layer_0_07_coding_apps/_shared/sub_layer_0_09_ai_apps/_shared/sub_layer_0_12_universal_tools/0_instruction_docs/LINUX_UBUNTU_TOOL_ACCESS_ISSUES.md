---
resource_id: "0a9a85ab-c51f-48ed-977e-862c88915b30"
resource_type: "document"
resource_name: "LINUX_UBUNTU_TOOL_ACCESS_ISSUES"
---
# Linux/Ubuntu Universal Tools Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → Universal Tools  
**Status**: Platform-specific limitations affecting universal tool access

<!-- section_id: "c9ee3bfa-9d0d-4b75-a4d8-5bffd2a6c502" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect access to universal tools, particularly those that depend on MCP (Model Context Protocol) servers. These issues impact browser automation tools, development frameworks, and other cross-cutting utilities.

<!-- section_id: "79bfc328-9fba-48cb-b3c2-d566ee01af85" -->
## Universal Tools Affected by Linux Issues

<!-- section_id: "17179cc7-b2ac-4e21-b3d4-4f4ce91e30a6" -->
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

<!-- section_id: "b5857ca8-4f76-4c69-8597-df9b0ce0ea22" -->
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

<!-- section_id: "d444224c-e691-49e6-8132-140b28aa42e1" -->
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

<!-- section_id: "81120f30-5741-442c-a1d9-ba61dfdb7515" -->
## Tool Access Patterns

<!-- section_id: "d83290fd-fa84-4497-a236-c1d57a867211" -->
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

<!-- section_id: "9567b823-0ba2-4e53-a0e9-65dc1c401f02" -->
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

<!-- section_id: "0185761e-631a-4e9f-88f4-ad112038f455" -->
### Pattern 3: Platform Detection

**Detect Platform and Use Appropriate Tools**:
```javascript
const platform = detect_platform();
const browserTool = platform === "linux" 
  ? "mcp_browser_browser_navigate"
  : "mcp_playwright_browser_navigate";
```

<!-- section_id: "273587eb-e749-40f3-a971-a81028d8a908" -->
## Universal Tools Documentation Updates

<!-- section_id: "fa40af41-27f8-47ca-a4cd-016792a4c001" -->
### Browser Automation Documentation

**Update Required Sections**:
- Tool name references (Playwright → Browser MCP for Linux)
- Example code snippets (Linux-specific versions)
- Troubleshooting guides (Linux-specific issues)
- Platform compatibility notes

<!-- section_id: "d1872c76-c0ed-4a4c-ba14-7fc6ee9c611f" -->
### Framework Documentation

**Update Required Sections**:
- Framework setup instructions (Linux-specific steps)
- Example workflows (Linux tool alternatives)
- Testing guides (Linux tool verification)
- Platform-specific configurations

<!-- section_id: "1c5e663a-bd12-46fb-b263-33cdbc345470" -->
## Tool Configuration

<!-- section_id: "f850d38a-80a9-4c0e-9411-caa875256d3e" -->
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

<!-- section_id: "58edf06f-4083-4215-9912-8c7ad288782b" -->
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

<!-- section_id: "97198ae7-16da-448a-b4bc-db4d39580f7b" -->
## Verification and Testing

<!-- section_id: "479478e6-3d59-4939-9e5f-047dbf9a2ad7" -->
### Verify Tool Access

```bash
# Check which browser MCP tools are available
# In Cursor IDE: Settings → Tools & MCP → Model Context Protocol
# Look for tools prefixed with:
# - mcp_browser_* (should be available)
# - mcp_playwright_* (will NOT be available on Linux)
```

<!-- section_id: "b65f7eae-ca0e-4949-a60c-538fb5418485" -->
### Test Tool Usage

1. **Test Browser Navigation**:
   - Try: `mcp_browser_browser_navigate({ url: "https://example.com" })`
   - Should work on Linux
   - Alternative: `mcp_cursor-browser-extension_browser_navigate()` (may have issues)

2. **Test Tool Availability**:
   - Check tool list in Cursor IDE
   - Verify expected tools are present
   - Note any missing tools

<!-- section_id: "0252a1ed-45bb-4486-af1e-fef3daf137b2" -->
## Tool Migration Guide

<!-- section_id: "a17d5aa2-5f6e-4d60-bb72-873b27ca436d" -->
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

<!-- section_id: "140de8bf-a0fb-4701-89f2-30e76fb686e6" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Browser Automation**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/browser-automation/`

<!-- section_id: "604f50be-6a3c-4dd3-adf4-bee4fc2dee1e" -->
## References

- Browser Automation Tools: See browser-automation documentation
- MCP Tool Reference: See MCP setup documentation
- Platform Compatibility: Check tool-specific documentation

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
