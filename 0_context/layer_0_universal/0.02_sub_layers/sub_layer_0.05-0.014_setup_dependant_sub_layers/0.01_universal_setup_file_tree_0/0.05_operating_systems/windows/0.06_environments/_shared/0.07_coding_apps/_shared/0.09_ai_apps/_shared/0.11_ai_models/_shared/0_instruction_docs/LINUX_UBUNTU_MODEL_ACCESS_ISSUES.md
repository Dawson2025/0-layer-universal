# Linux/Ubuntu AI Model Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Models  
**Status**: Platform-specific limitations affecting model access via MCP

## Overview

This document outlines Linux/Ubuntu-specific issues that affect how AI models access MCP (Model Context Protocol) tools and capabilities. These issues impact model selection, tool availability, and agent configuration.

## Model Access Issues on Linux

### 1. MCP Tool Availability

**Problem**: Some MCP tools are not available to AI models on Linux, even when MCP servers are configured and running.

**Impact on Models**:
- Models cannot access Playwright MCP tools (22 tools unavailable)
- Limited browser automation capabilities
- Must use alternative tools (`mcp_browser_*` instead of `mcp_playwright_*`)

**Example**: 
- Model attempts to use `mcp_playwright_browser_navigate` → Tool not found
- Workaround: Use `mcp_browser_browser_navigate` instead

### 2. Tool Naming Conventions

**Problem**: Tool naming may differ on Linux, causing model confusion.

**Impact**:
- Models may attempt to use tools with incorrect names
- Documentation examples may not work on Linux
- Requires Linux-specific tool name references

**Solution**: Always verify tool names available on Linux before instructing models.

### 3. Model Fallback Strategy

**Problem**: Different models may have different capabilities for handling Linux-specific tool limitations.

**Impact**:
- Some models may not adapt well to unavailable tools
- Fallback models may need different tool configurations
- Model-specific instructions may need Linux variants

**Recommendation**: Configure model fallback chains that account for Linux tool limitations.

## Model Configuration Considerations

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

## Available Tools for Models on Linux

### ✅ Available MCP Tools

- `mcp_browser_*` (21 tools) - Browser automation via Browser MCP
- `mcp_cursor-browser-extension_*` (18 tools) - Cursor browser extension (may have issues)
- Other non-browser MCP tools (documentation, search, filesystem, etc.)

### ❌ Unavailable MCP Tools

- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed on Linux

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

## Testing Model Access

### Verify Tool Availability

```bash
# Check MCP server status
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*mcp*" | head -5
```

### Test Tool Access

In Cursor IDE:
1. Open Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Note which tools are listed
4. Test tool access in agent session

## Related Documentation

- **OS-Level Issues**: `layer_0_universal/0.02_sub_layers/sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0_universal/0.02_sub_layers/sub_layer_0.07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0_universal/0.02_sub_layers/sub_layer_0.10_mcp_servers_and_tools_setup/`
- **Universal Tools**: `layer_0_universal/0.02_sub_layers/sub_layer_0.12_universal_tools/`

## References

- Model Context Protocol: https://modelcontextprotocol.io
- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: Platform-specific MCP tool exposure problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
