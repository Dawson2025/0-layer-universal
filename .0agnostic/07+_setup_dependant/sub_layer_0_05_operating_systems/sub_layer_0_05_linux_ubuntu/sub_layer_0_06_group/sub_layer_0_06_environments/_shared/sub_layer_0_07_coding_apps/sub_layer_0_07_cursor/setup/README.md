---
resource_id: "32532573-5596-4317-8ed3-000c3fa46070"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "7a57d0a7-3e3d-4254-a024-f8a92486f232" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "86e1513c-7cbe-4fd8-9c0c-7e49d91e9b4d" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "85b9bb94-659f-4bbe-972b-58f1c6d49877" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.
