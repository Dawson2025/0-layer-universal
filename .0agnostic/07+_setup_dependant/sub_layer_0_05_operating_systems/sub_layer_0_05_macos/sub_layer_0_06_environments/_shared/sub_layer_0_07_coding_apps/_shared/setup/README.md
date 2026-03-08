---
resource_id: "07e5e0b6-0f1e-4011-843d-7b9d3f914dae"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "991667dd-f16b-4526-abc0-46c26496874b" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "79b24035-02fd-4e07-9116-0e1f175cc608" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "ec750bbf-2c16-45c2-927e-d46959a597a4" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.
