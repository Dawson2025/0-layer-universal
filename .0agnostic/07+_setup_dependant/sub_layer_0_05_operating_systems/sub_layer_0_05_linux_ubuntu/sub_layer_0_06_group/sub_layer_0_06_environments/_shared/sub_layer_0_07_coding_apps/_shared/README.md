---
resource_id: "85e02b27-6cf3-4f4f-9d89-8d939ac389f4"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "8a0c8668-daf5-437e-8f27-08a4d06414d0" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "cb2151c2-95db-4b0f-b06c-28013c8e7f5c" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "538ca24a-b576-449d-ba84-bb6c54645a65" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.


---

<!-- section_id: "c2d5086d-888c-43d0-b15a-22c24310f390" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_08_apps_browsers_extensions_setup/README.md`

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "bee32406-9b31-4b68-b365-2a5b5d595ac4" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.
