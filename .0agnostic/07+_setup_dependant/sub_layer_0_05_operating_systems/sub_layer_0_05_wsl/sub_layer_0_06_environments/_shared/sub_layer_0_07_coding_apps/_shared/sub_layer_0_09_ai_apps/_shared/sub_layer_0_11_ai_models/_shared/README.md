---
resource_id: "c965c1d2-0991-4f59-9706-4280896bd485"
resource_type: "readme_document"
resource_name: "README"
---
# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "0a6289ed-533c-4df3-9c21-5da835f2cc89" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "5c8bd6a9-f7de-4a80-8fb2-870ae1cdf09c" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "42285043-8a6d-4709-8913-c66251368fcd" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "c79be738-8612-467b-88d1-c76a58e62c97" -->
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

<!-- section_id: "dc1a24f3-51ec-4a1b-93ac-3f5f16914d0d" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
