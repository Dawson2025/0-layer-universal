---
resource_id: "06e8f0e5-61a3-4bdc-b985-8040edbc6e35"
resource_type: "readme_document"
resource_name: "README"
---
# Sub Layer 0.07: Coding App Setup

**Purpose**: IDE and editor setup, including Cursor IDE configuration.

<!-- section_id: "c5eb65af-497f-4548-9b54-f56edd2764e9" -->
## ⚠️ Cursor IDE Linux/Ubuntu MCP Issues

**CRITICAL**: Cursor IDE on Linux has specific MCP limitations. Read:

- **[Cursor IDE Linux MCP Issues](trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md)**: Cursor IDE-specific Linux limitations

**Key Issues**:
- Playwright MCP tools are NOT exposed to AI agents on Linux
- Browser path configuration required
- MCP configuration requires bash wrappers for NVM
- Use `mcp_browser_*` tools instead of `mcp_playwright_*` on Linux

<!-- section_id: "0161bf12-5945-4d64-9637-f3f4f55380e3" -->
## Related Documentation

- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **AI Apps Issues**: `../sub_layer_0_09_ai_apps_tools_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_AI_APPS_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "269cc488-84df-4e1e-93d3-3bc3d6ff0595" -->
## Notes
- Add slot-specific docs here over time.
- Keep mappings up to date if paths change.


---

<!-- section_id: "526cf62a-92e1-497c-aad4-2cb9a61db20e" -->
## Legacy Source

Source: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_08_apps_browsers_extensions_setup/README.md`

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "3d0d09b7-f8bd-4b5e-b8cc-78d50932b13b" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.
