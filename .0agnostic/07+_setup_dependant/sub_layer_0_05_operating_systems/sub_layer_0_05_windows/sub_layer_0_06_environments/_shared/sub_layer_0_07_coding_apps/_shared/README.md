---
resource_id: "1800d015-6c52-4f5a-9820-1bcd02d84779"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "398dc149-de42-4726-bc14-f6a9135f22eb" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "b84b4b12-5094-4ad3-a5a8-3e6c6f6786e9" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "aed60bb6-e71a-4e56-8e05-8f13c3bf6007" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.


---

<!-- section_id: "c8adfa40-630f-4b96-9f24-bfd17482f49c" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_08_apps_browsers_extensions_setup/README.md`

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "3a839939-8726-4865-b7db-2eea3cae59f2" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.
