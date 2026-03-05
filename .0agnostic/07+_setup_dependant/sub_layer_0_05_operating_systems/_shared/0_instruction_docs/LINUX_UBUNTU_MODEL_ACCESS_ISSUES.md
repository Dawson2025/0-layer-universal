---
resource_id: "a4608e3f-c7cc-4601-84ff-2f9fa890bfca"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MODEL_ACCESS_ISSUES"
---
# Linux/Ubuntu AI Model Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Models  
**Status**: Platform-specific limitations affecting model access via MCP

<!-- section_id: "b7ded873-5c88-4117-8d90-be846419218a" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect how AI models access MCP (Model Context Protocol) tools and capabilities. These issues impact model selection, tool availability, and agent configuration.

<!-- section_id: "a1ae41df-ce0c-48f1-9d23-4249dc25bc69" -->
## Model Access Issues on Linux

<!-- section_id: "40716929-2081-4872-9bea-0f57e52c73fc" -->
### 1. MCP Tool Availability

**Problem**: Some MCP tools are not available to AI models on Linux, even when MCP servers are configured and running.

**Impact on Models**:
- Models cannot access Playwright MCP tools (22 tools unavailable)
- Limited browser automation capabilities
- Must use alternative tools (`mcp_browser_*` instead of `mcp_playwright_*`)

**Example**: 
- Model attempts to use `mcp_playwright_browser_navigate` → Tool not found
- Workaround: Use `mcp_browser_browser_navigate` instead

<!-- section_id: "532ad4db-19fa-4b02-878a-c67a47f41520" -->
### 2. Tool Naming Conventions

**Problem**: Tool naming may differ on Linux, causing model confusion.

**Impact**:
- Models may attempt to use tools with incorrect names
- Documentation examples may not work on Linux
- Requires Linux-specific tool name references

**Solution**: Always verify tool names available on Linux before instructing models.

<!-- section_id: "8897bc49-0895-4d9b-9a68-bb86fa27d61f" -->
### 3. Model Fallback Strategy

**Problem**: Different models may have different capabilities for handling Linux-specific tool limitations.

**Impact**:
- Some models may not adapt well to unavailable tools
- Fallback models may need different tool configurations
- Model-specific instructions may need Linux variants

**Recommendation**: Configure model fallback chains that account for Linux tool limitations.

<!-- section_id: "8d18d058-8324-444b-8e43-07303a1db524" -->
## Model Configuration Considerations

<!-- section_id: "dcb4bbbe-3b06-4f35-8a54-c2329296b677" -->
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

<!-- section_id: "2819312c-cb6f-464b-b5a5-db4fee50e6c3" -->
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

<!-- section_id: "ed85e8f5-3333-4905-b79b-0d3068c172c5" -->
## Available Tools for Models on Linux

<!-- section_id: "88a29094-47e9-4af2-9be7-733e7b478562" -->
### ✅ Available MCP Tools

- `mcp_browser_*` (21 tools) - Browser automation via Browser MCP
- `mcp_cursor-browser-extension_*` (18 tools) - Cursor browser extension (may have issues)
- Other non-browser MCP tools (documentation, search, filesystem, etc.)

<!-- section_id: "6d35d315-196a-44d4-aaee-ff11d0f18692" -->
### ❌ Unavailable MCP Tools

- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed on Linux

<!-- section_id: "bd53f92f-9830-4eaa-9f1e-105025eb36fd" -->
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

<!-- section_id: "d6c6a9e2-874a-429e-bd72-ccc552e76f57" -->
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

<!-- section_id: "b0cc4074-0908-414f-8133-0ae1670d6611" -->
## Testing Model Access

<!-- section_id: "6d0e69cf-0bbf-459c-9c27-9601ed728aff" -->
### Verify Tool Availability

```bash
# Check MCP server status
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*mcp*" | head -5
```

<!-- section_id: "7bb6eb6e-039b-4e32-ba62-5b5bacb5eaa9" -->
### Test Tool Access

In Cursor IDE:
1. Open Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Note which tools are listed
4. Test tool access in agent session

<!-- section_id: "f31ba5bc-a1b8-4f5e-bc7d-bcb92ad6e368" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Universal Tools**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/`

<!-- section_id: "8064e5fa-469d-4714-b96e-f0e9235e756a" -->
## References

- Model Context Protocol: https://modelcontextprotocol.io
- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: Platform-specific MCP tool exposure problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
