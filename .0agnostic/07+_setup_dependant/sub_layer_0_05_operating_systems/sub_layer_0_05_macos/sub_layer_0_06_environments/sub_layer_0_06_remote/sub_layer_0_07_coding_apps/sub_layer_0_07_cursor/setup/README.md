---
resource_id: "07bc6b3d-b6db-47d8-8692-a637fa0eeef2"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "e7303624-1002-4ab5-b79a-fd9db8c2acbf" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "f5da2f6a-2e79-4a27-b180-dfc18b0d6b89" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "4eb7ab0d-3e0b-4ee1-a5e9-b77fe1d5cb9d" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.
