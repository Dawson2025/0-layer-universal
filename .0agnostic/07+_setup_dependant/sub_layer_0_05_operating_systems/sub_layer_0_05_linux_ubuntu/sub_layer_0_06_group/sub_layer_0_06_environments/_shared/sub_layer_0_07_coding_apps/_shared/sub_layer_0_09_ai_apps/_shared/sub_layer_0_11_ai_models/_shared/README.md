---
resource_id: "f7c40ee8-ebbb-4604-930a-898bcefa34da"
resource_type: "readme_document"
resource_name: "README"
---
# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "dcceabe3-2185-4ec6-bbbe-4838f53f6b52" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "c2c13fb5-dc96-4f7c-a9db-42d6bb30fae3" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "f50f27bf-a62c-4ab3-aefa-25b823d3c073" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "2a629016-36c3-4663-a1f2-c74dfe114c10" -->
## ⚠️ Linux/Ubuntu-Specific Model Access Issues

**CRITICAL**: AI model access to MCP tools is limited on Linux. Read:

- **[Linux/Ubuntu Model Access Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md)**: Model access limitations on Linux

**Key Issues**:
- Some MCP tools unavailable to models on Linux
- Tool naming conventions may differ
- Model fallback strategies need Linux-specific configuration
- Model instructions must account for Linux tool limitations

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0_10_mcp_servers_and_tools_setup/`

<!-- section_id: "cb222a6d-7566-4ed9-b3d2-cf4091b73a35" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
