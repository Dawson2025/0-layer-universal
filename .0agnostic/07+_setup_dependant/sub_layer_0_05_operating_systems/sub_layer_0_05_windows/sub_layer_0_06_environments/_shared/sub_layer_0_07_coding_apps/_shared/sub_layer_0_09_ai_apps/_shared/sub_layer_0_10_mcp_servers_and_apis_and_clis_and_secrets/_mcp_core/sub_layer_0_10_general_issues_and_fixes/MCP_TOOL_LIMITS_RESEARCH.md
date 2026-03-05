---
resource_id: "5f2a3c2f-4b3e-4a83-85d9-430289ad68f7"
resource_type: "document"
resource_name: "MCP_TOOL_LIMITS_RESEARCH"
---
# MCP Tool Limits Research

**Date**: 2025-12-05  
**Location**: Universal Layer → MCP Servers and Tools Setup  
**Status**: Comprehensive research findings

<!-- section_id: "d8036a2b-a200-4d2e-9b03-0362efcf167e" -->
## Executive Summary

Cursor IDE has **hard limits on MCP tools** that can affect tool availability. Understanding these limits is critical for managing MCP server configurations.

<!-- section_id: "9038ad19-5093-4fc6-8466-d062950c9ea5" -->
## Key Findings

<!-- section_id: "4317ec22-67c4-468e-bb9a-098c2521231d" -->
### 1. 40-Tool Hard Limit ✅ **CONFIRMED**

**Finding**: Cursor currently has a **hard limit of 40 tools total** across all enabled MCP servers.

**Sources**:
- [Cursor Forum: About limitation of the number of MCP tools](https://forum.cursor.com/t/about-limitation-of-the-number-of-mcp-tools/107844)
- [Cursor Forum: Tools limited to 40 total](https://forum.cursor.com/t/tools-limited-to-40-total/67976)
- [Medium: Cursor's 40-Tool Barrier](https://medium.com/@sakshiaroraresearch/cursors-40-tool-tango-navigating-mcp-limits-213a111dc218)

**Evidence**:
- "Cursor currently has a hard limit of 40 tools total. I use 2 MCP servers that expose 41 tools in total. Cursor cannot see the 41st tool."
- "Currently, Cursor will only send the first 40 tools"
- "The limit is 40 tools – some tools may not be available to the agent"

<!-- section_id: "8a6b45cd-1b81-4734-8e4a-eebaf952c448" -->
### 2. Warning Threshold vs. Actual Limit

**Finding**: There may be a distinction between warning threshold and actual hard limit.

**Sources**:
- [Cursor Forum: MCP - 40 Tools way to less](https://forum.cursor.com/t/mcp-40-tools-way-to-less/79686)

**Evidence**:
- "The actual limit right now is 80, and the next build makes it clearer that 40 is just a limit to warn you that you might be degrading performance."

**Implication**: 
- 40 tools = Warning threshold (performance degradation)
- 80 tools = Actual hard limit (tools beyond this won't be available)

<!-- section_id: "5930a058-3759-4e46-8f11-0abdd1307f5f" -->
### 3. Performance Degradation Warning

**Finding**: Cursor displays warnings when tool count exceeds recommended limits.

**Sources**:
- [GitHub Issue: Granular Control Over MCP Server Tools](https://github.com/cursor/cursor/issues/3280)
- [Reddit: MCP Server 40-Tool Limit](https://www.reddit.com/r/cursor/comments/1k3pob9/mcp_server_40tool_limit_in_cursor_is_this/)

**Warning Message**:
- "You have 50 tools from enabled servers. The limit is 40 tools – some tools may not be available to the agent."

**Why the Limit Exists**:
- **Context window management**: The limit exists to manage the context window
- **AI tool selection**: Too many tools make it harder for AI to effectively choose the right tool
- **Performance**: Exceeding 40 tools can degrade performance

<!-- section_id: "5f3b4ffd-1ed2-4066-bac1-466efabe9a4b" -->
### 4. Tool Selection and Management

**Finding**: Individual tools can be enabled/disabled in MCP settings.

**Sources**:
- [Cursor Forum: Increase MCP Tools Limit](https://forum.cursor.com/t/request-increase-mcp-tools-limit-for-enhanced-development-workflow/108637)

**Evidence**:
- "They can be enabled and disabled by clicking on each tool name in the MCP settings."

**Implication**: You can selectively enable/disable specific tools from MCP servers to stay under the limit.

<!-- section_id: "c7340f8f-afd4-4fda-8943-b33fd13eb8ea" -->
### 5. Workarounds and Solutions

#### Solution 1: Disable Unused MCP Servers ✅ **RECOMMENDED**

**Action**: Disable entire MCP servers you're not actively using.

**Why This Works**:
- Reduces total tool count across all servers
- Frees up capacity for needed tools
- Simplifies tool management

**Evidence from Our Testing**:
- User reported Cursor warning about "too many MCP servers and too many tools"
- After disabling unused servers, Playwright tools became available
- This aligns with the 40-tool limit constraint

#### Solution 2: Disable Individual Tools

**Action**: Enable/disable specific tools within MCP servers.

**How**:
1. Go to Cursor Settings → Tools & MCP
2. Click on an MCP server
3. Enable/disable individual tools

**Limitation**: Not all MCP servers support granular tool control.

#### Solution 3: Use MCP Hub Server

**Finding**: Community-developed workaround exists.

**Sources**:
- [Cursor Forum: Unlimited MCP Tools: Break the 40 tools limit!](https://forum.cursor.com/t/unlimited-mcp-tools-break-the-40-tools-limit/78040)

**Solution**: `mcp-hub-mcp` server that connects to all servers in mcp.json and may help work around the limit.

**Note**: This is a community workaround, not an official solution.

<!-- section_id: "921d475e-559a-484b-8e46-b14d10998749" -->
## Impact on Our Solution

<!-- section_id: "02ff25a0-da6e-48df-a0b8-333cec7dcab5" -->
### Why Disabling Unused Servers Helped

**Our Experience**:
1. User had multiple MCP servers enabled
2. Cursor warned about "too many MCP servers and too many tools"
3. After disabling unused servers, Playwright tools became available
4. This freed up capacity within the 40-tool limit

**Conclusion**: Disabling unused MCP servers was likely a critical factor in getting Playwright tools to work, as it freed up slots within the 40-tool limit.

<!-- section_id: "f5d27061-f15f-4dad-8517-3168c77b1205" -->
## Recommendations

<!-- section_id: "e2648820-fe16-4049-804a-01f6e6e7ae13" -->
### For Users with Many MCP Servers

1. **Audit Your MCP Servers**:
   - List all enabled MCP servers
   - Count total tools across all servers
   - Identify which servers you actively use

2. **Disable Unused Servers**:
   - Disable servers you're not actively using
   - Keep only essential servers enabled
   - Monitor tool count to stay under 40

3. **Prioritize Essential Tools**:
   - Enable only the MCP servers you need for current work
   - Disable servers when not in use
   - Re-enable as needed

4. **Monitor Warnings**:
   - Pay attention to Cursor's warnings about tool limits
   - If you see "too many tools" warnings, disable unused servers
   - Check tool count in Cursor Settings → Tools & MCP

<!-- section_id: "bae72d96-aa6b-4867-8b2a-2b572dc39a2e" -->
### Best Practices

1. **Start Minimal**: Only enable MCP servers you're actively using
2. **Enable On-Demand**: Enable servers when needed, disable when done
3. **Monitor Count**: Keep total tool count under 40 for optimal performance
4. **Use Granular Control**: If available, disable individual tools within servers

<!-- section_id: "e7400571-7c00-450f-ab63-cc6c6e46a47f" -->
## Related Limits

<!-- section_id: "fadf0cde-315b-471f-84de-9c78a69d767a" -->
### Tool Call Limits (Separate from Tool Count)

**Finding**: Cursor also has tool call limits per interaction.

**Sources**:
- [Apidog: How to Continue When Cursor's 25 Tool Call Limit is Reached](https://apidog.com/blog/cursor-tool-call-limit/)

**Details**:
- Standard mode: 25 tool calls per interaction
- MAX mode: Different limits and cost structure
- "Continue" mechanism: Allows continuation after limit

**Note**: This is different from the 40-tool limit (which is about how many tools are available, not how many times they can be called).

<!-- section_id: "e792dd5e-7385-4e81-aaaa-75e863aa6b2b" -->
## Community Requests

<!-- section_id: "d3bca304-f938-4d3d-bd70-43d79ebd8be5" -->
### Feature Requests for Increased Limits

**Sources**:
- [Cursor Forum: Increase the MCP tool](https://forum.cursor.com/t/increase-the-mcp-tool/69194)
- [Cursor Forum: Exceeding total tools limit](https://forum.cursor.com/t/exceeding-total-tools-limit/134396)
- [Cursor Forum: Request: Increase MCP Tools Limit](https://forum.cursor.com/t/request-increase-mcp-tools-limit-for-enhanced-development-workflow/108637)

**Status**: Multiple feature requests exist, but limit remains at 40 tools (with 80 as hard cap).

**Cursor Team Response**:
- "Hey, we might increase the current limit soon or add the option to disable individual MCP tools."
- "The 40 tool limit is actually there for a good reason - if we increased it, the AI would struggle to effectively choose"

<!-- section_id: "4de3aa98-c5ee-430b-a381-c785769a0f10" -->
## Summary Table

| Limit Type | Value | Purpose | Source |
|------------|-------|---------|--------|
| **Warning Threshold** | 40 tools | Performance degradation warning | Multiple forum posts |
| **Hard Limit** | 80 tools | Maximum tools that can be available | Forum post (may have changed) |
| **Current Hard Limit** | 40 tools | Tools beyond this not available | Multiple confirmed sources |
| **Tool Call Limit** | 25 calls | Per interaction limit (separate) | Apidog article |

<!-- section_id: "76ee4c27-519f-4527-91a8-ff05c92a933e" -->
## References

<!-- section_id: "9fdcdf7b-7ecd-412e-82ff-fedaf6dd5a4c" -->
### Official/Forum Sources
- [About limitation of the number of MCP tools](https://forum.cursor.com/t/about-limitation-of-the-number-of-mcp-tools/107844)
- [Tools limited to 40 total](https://forum.cursor.com/t/tools-limited-to-40-total/67976)
- [MCP - 40 Tools way to less](https://forum.cursor.com/t/mcp-40-tools-way-to-less/79686)
- [Request: Increase MCP Tools Limit](https://forum.cursor.com/t/request-increase-mcp-tools-limit-for-enhanced-development-workflow/108637)
- [Exceeding total tools limit](https://forum.cursor.com/t/exceeding-total-tools-limit/134396)
- [Unlimited MCP Tools: Break the 40 tools limit!](https://forum.cursor.com/t/unlimited-mcp-tools-break-the-40-tools-limit/78040)

<!-- section_id: "95ea8f66-26f2-4e68-a634-c44d58a0fd33" -->
### GitHub Issues
- [Feature Request: Granular Control Over MCP Server Tools](https://github.com/cursor/cursor/issues/3280)

<!-- section_id: "a3cfc402-9f6b-4b3a-94d8-38abc878fbc0" -->
### Articles
- [Cursor's 40-Tool Barrier: Navigating MCP Limits](https://medium.com/@sakshiaroraresearch/cursors-40-tool-tango-navigating-mcp-limits-213a111dc218)
- [How to Continue When Cursor's 25 Tool Call Limit is Reached](https://apidog.com/blog/cursor-tool-call-limit/)

<!-- section_id: "37e41f77-732d-4816-adc5-96b65aca8e51" -->
### Reddit
- [MCP Server 40-Tool Limit in Cursor](https://www.reddit.com/r/cursor/comments/1k3pob9/mcp_server_40tool_limit_in_cursor_is_this/)

<!-- section_id: "d1fe797a-afcb-45d2-968f-6bb7f96ce983" -->
## Changelog

<!-- section_id: "85c34291-9afa-4eae-93ca-d4a1dee1d25c" -->
### 2025-12-05
- Comprehensive research on MCP tool limits
- Confirmed 40-tool hard limit
- Documented warning threshold vs. actual limit
- Explained why disabling unused servers helped
- Added recommendations and best practices
- Documented community workarounds
- Added references to all sources

---

**Key Takeaway**: Cursor has a **40-tool hard limit**. Disabling unused MCP servers is essential to stay under this limit and ensure needed tools are available.

