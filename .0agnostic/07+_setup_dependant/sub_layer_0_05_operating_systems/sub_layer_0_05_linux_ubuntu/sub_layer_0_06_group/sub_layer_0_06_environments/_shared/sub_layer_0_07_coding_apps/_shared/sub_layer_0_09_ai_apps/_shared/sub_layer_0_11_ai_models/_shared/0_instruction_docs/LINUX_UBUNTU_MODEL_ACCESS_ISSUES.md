---
resource_id: "5bf78995-2c48-4fdd-b7d0-2e7a7bb06fda"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MODEL_ACCESS_ISSUES"
---
# Linux/Ubuntu AI Model Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Models  
**Status**: Platform-specific limitations affecting model access via MCP

<!-- section_id: "0db1fc0b-a8cd-4312-9dd3-fcd4c7fd78a5" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect how AI models access MCP (Model Context Protocol) tools and capabilities. These issues impact model selection, tool availability, and agent configuration.

<!-- section_id: "e40c6bd3-16e8-4c20-880c-98ddcdb58605" -->
## Model Access Issues on Linux

<!-- section_id: "019f6dd4-a3cd-4799-9dc0-70058afab5d3" -->
### 1. MCP Tool Availability

**Problem**: Some MCP tools are not available to AI models on Linux, even when MCP servers are configured and running.

**Impact on Models**:
- Models cannot access Playwright MCP tools (22 tools unavailable)
- Limited browser automation capabilities
- Must use alternative tools (`mcp_browser_*` instead of `mcp_playwright_*`)

**Example**: 
- Model attempts to use `mcp_playwright_browser_navigate` → Tool not found
- Workaround: Use `mcp_browser_browser_navigate` instead

<!-- section_id: "4601ec5e-2690-4440-b0c5-2f7d38629425" -->
### 2. Tool Naming Conventions

**Problem**: Tool naming may differ on Linux, causing model confusion.

**Impact**:
- Models may attempt to use tools with incorrect names
- Documentation examples may not work on Linux
- Requires Linux-specific tool name references

**Solution**: Always verify tool names available on Linux before instructing models.

<!-- section_id: "d3a7bc5f-b634-4690-ad71-ed53d28800e7" -->
### 3. Model Fallback Strategy

**Problem**: Different models may have different capabilities for handling Linux-specific tool limitations.

**Impact**:
- Some models may not adapt well to unavailable tools
- Fallback models may need different tool configurations
- Model-specific instructions may need Linux variants

**Recommendation**: Configure model fallback chains that account for Linux tool limitations.

<!-- section_id: "9f7bdc50-ca9d-425f-8e9b-01946ee24eb6" -->
## Model Configuration Considerations

<!-- section_id: "b2f1165b-65ff-47e2-b8c5-af84f79be9ad" -->
### Primary Model Setup

When configuring primary models on Linux:

1. **Verify Tool Availability**:
   - Check which MCP tools are actually accessible
   - Document available vs. unavailable tools
   - Update model instructions accordingly

2. **Tool-Specific Instructions**:
   - Provide Linux-specific tool names
   - Include workarounds for unavailable tools
   - Document alternative tools to use

3. **Error Handling**:
   - Instruct models on how to handle "Tool not found" errors
   - Provide fallback tool options
   - Document Linux-specific error patterns

<!-- section_id: "1867aa4e-aecc-447a-a974-4de99201bc35" -->
### Fallback Model Configuration

When setting up fallback models:

1. **Tool Compatibility**:
   - Ensure fallback models can use available Linux tools
   - Test tool access with each fallback model
   - Document any model-specific tool limitations

2. **Model-Specific Instructions**:
   - Adapt instructions for each model in the fallback chain
   - Account for different model capabilities
   - Provide Linux-specific guidance for each model

<!-- section_id: "ceaeb17c-187d-478f-a6d8-510ee9d1c58d" -->
## Available Tools for Models on Linux

<!-- section_id: "a2d683e4-1a4f-498d-898e-ec2d23794874" -->
### ✅ Available MCP Tools

- `mcp_browser_*` (21 tools) - Browser automation via Browser MCP
- `mcp_cursor-browser-extension_*` (18 tools) - Cursor browser extension (may have issues)
- Other non-browser MCP tools (documentation, search, filesystem, etc.)

<!-- section_id: "4de55385-bd13-4ca8-8b23-a73e0d6b2427" -->
### ❌ Unavailable MCP Tools

- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed on Linux

<!-- section_id: "4a96f4f9-c5b6-4de2-a41a-492c13aed011" -->
## Model Instructions Template

When creating model instructions for Linux:

```markdown
## Browser Automation on Linux

**Available Tools**:
- Use `mcp_browser_browser_navigate` (NOT `mcp_playwright_browser_navigate`)
- Use `mcp_browser_browser_click` (NOT `mcp_playwright_browser_click`)
- Use `mcp_browser_browser_snapshot` (NOT `mcp_playwright_browser_snapshot`)

**If Tool Not Found**:
1. Check if you're using the correct tool name for Linux
2. Try the `mcp_browser_*` variant instead of `mcp_playwright_*`
3. Verify MCP server is running: Check Cursor Settings → Tools & MCP
```

<!-- section_id: "0702e304-f855-4ddc-a002-58a01a645d98" -->
## Agent Configuration

When configuring agents for Linux:

1. **Tool Access Configuration**:
   - List only available Linux tools
   - Exclude unavailable tools from agent capabilities
   - Provide clear tool availability documentation

2. **Model-Specific Tool Instructions**:
   - Adapt instructions based on which model is active
   - Account for model-specific tool handling differences
   - Provide Linux-specific examples

3. **Error Recovery**:
   - Configure agents to handle Linux-specific tool errors
   - Provide fallback strategies
   - Document recovery procedures

<!-- section_id: "fdaa10ef-3029-451a-9a4a-ff21b5989373" -->
## Testing Model Access

<!-- section_id: "17091fd3-70fb-44ce-9b35-5d7793c689a4" -->
### Verify Tool Availability

```bash
# Check MCP server status
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*mcp*" | head -5
```

<!-- section_id: "87e4aceb-cbcc-4158-876d-009cf5331343" -->
### Test Tool Access

In Cursor IDE:
1. Open Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Note which tools are listed
4. Test tool access in agent session

<!-- section_id: "da20a26a-ba93-479b-b6d0-b2eb2ff15342" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Universal Tools**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/`

<!-- section_id: "a390aebc-a041-43b8-8340-870bcf93e40a" -->
## References

- Model Context Protocol: https://modelcontextprotocol.io
- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: Platform-specific MCP tool exposure problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
