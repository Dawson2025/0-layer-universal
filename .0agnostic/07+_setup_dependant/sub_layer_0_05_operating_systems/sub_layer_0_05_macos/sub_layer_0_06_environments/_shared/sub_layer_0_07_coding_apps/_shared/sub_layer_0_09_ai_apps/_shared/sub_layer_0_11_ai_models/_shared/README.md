---
resource_id: "9cacfb9a-0cb7-4546-b5fe-37ec98aa9022"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "bca4759f-45f6-4b4b-a184-54933978791f" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "e8230128-2ff5-4b52-8c8f-db5216376a94" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "bcb51960-e1e7-4871-977c-01b1fe925b5d" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "faf60268-0199-4e12-9f64-67853a21639d" -->
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

<!-- section_id: "7e90a378-5705-4edb-96fa-9c8b1fde124c" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
