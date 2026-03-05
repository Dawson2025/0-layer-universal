---
resource_id: "75abe846-4f77-4e64-88b9-a715ba7a7f42"
resource_type: "document"
resource_name: "LINUX_UBUNTU_MODEL_ACCESS_ISSUES"
---
# Linux/Ubuntu AI Model Access Issues

**Date**: 2025-12-02  
**Location**: Universal Layer → AI Models  
**Status**: Platform-specific limitations affecting model access via MCP

<!-- section_id: "8687eb8b-1633-4b35-9064-2fb413fba83f" -->
## Overview

This document outlines Linux/Ubuntu-specific issues that affect how AI models access MCP (Model Context Protocol) tools and capabilities. These issues impact model selection, tool availability, and agent configuration.

<!-- section_id: "3f77fc02-36e3-4ac7-b168-6a3726dc4df7" -->
## Model Access Issues on Linux

<!-- section_id: "384dff08-3f2a-44a3-93cc-605cd683571e" -->
### 1. MCP Tool Availability

**Problem**: Some MCP tools are not available to AI models on Linux, even when MCP servers are configured and running.

**Impact on Models**:
- Models cannot access Playwright MCP tools (22 tools unavailable)
- Limited browser automation capabilities
- Must use alternative tools (`mcp_browser_*` instead of `mcp_playwright_*`)

**Example**: 
- Model attempts to use `mcp_playwright_browser_navigate` → Tool not found
- Workaround: Use `mcp_browser_browser_navigate` instead

<!-- section_id: "4731f38b-93a5-4155-80a4-f1cd7ebf3bda" -->
### 2. Tool Naming Conventions

**Problem**: Tool naming may differ on Linux, causing model confusion.

**Impact**:
- Models may attempt to use tools with incorrect names
- Documentation examples may not work on Linux
- Requires Linux-specific tool name references

**Solution**: Always verify tool names available on Linux before instructing models.

<!-- section_id: "04bcf98f-67ef-4995-98c4-2569d3480e0c" -->
### 3. Model Fallback Strategy

**Problem**: Different models may have different capabilities for handling Linux-specific tool limitations.

**Impact**:
- Some models may not adapt well to unavailable tools
- Fallback models may need different tool configurations
- Model-specific instructions may need Linux variants

**Recommendation**: Configure model fallback chains that account for Linux tool limitations.

<!-- section_id: "4abc91a3-84f5-4542-89fe-4f0debfc2c51" -->
## Model Configuration Considerations

<!-- section_id: "6ebc6c50-e327-4005-be47-853136371391" -->
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

<!-- section_id: "1c492f1d-397a-4b6c-95ec-22a1edb49c96" -->
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

<!-- section_id: "bb952731-2e12-4dcc-afbf-7e2a274683f8" -->
## Available Tools for Models on Linux

<!-- section_id: "583b5ed8-b623-414c-9600-c0cc84fb161e" -->
### ✅ Available MCP Tools

- `mcp_browser_*` (21 tools) - Browser automation via Browser MCP
- `mcp_cursor-browser-extension_*` (18 tools) - Cursor browser extension (may have issues)
- Other non-browser MCP tools (documentation, search, filesystem, etc.)

<!-- section_id: "918167d5-ed02-4d01-b0a9-73762c879d20" -->
### ❌ Unavailable MCP Tools

- `mcp_playwright_*` (22 tools) - Server connects but tools not exposed on Linux

<!-- section_id: "9be31431-4653-49f6-b22e-f207cb86a355" -->
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

<!-- section_id: "9d55747b-7086-4dd5-a6e8-083d334678c5" -->
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

<!-- section_id: "391acd4b-4ebf-4b94-b613-e243d4054040" -->
## Testing Model Access

<!-- section_id: "f0a0fe43-3fce-4756-bb1c-c82c7ef843d6" -->
### Verify Tool Availability

```bash
# Check MCP server status
ps aux | grep -E "playwright|mcp" | grep -v grep

# Check Cursor MCP logs
find ~/.config/Cursor/logs -name "*mcp*" | head -5
```

<!-- section_id: "5897334f-5434-4005-9cec-53eb3ec923e5" -->
### Test Tool Access

In Cursor IDE:
1. Open Settings → Tools & MCP
2. Check "Model Context Protocol" section
3. Note which tools are listed
4. Test tool access in agent session

<!-- section_id: "ebd6ba86-d628-4f75-8667-b80cf1d3cf67" -->
## Related Documentation

- **OS-Level Issues**: `layer_0/0.02_sub_layers/sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `layer_0/0.02_sub_layers/sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/`
- **Universal Tools**: `layer_0/0.02_sub_layers/sub_layer_0_12_universal_tools/`

<!-- section_id: "3a2f6ee2-e574-40a0-bb6a-79060c1c85b9" -->
## References

- Model Context Protocol: https://modelcontextprotocol.io
- Cursor IDE Documentation: https://cursor.com/docs
- GitHub Issues: Platform-specific MCP tool exposure problems

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
