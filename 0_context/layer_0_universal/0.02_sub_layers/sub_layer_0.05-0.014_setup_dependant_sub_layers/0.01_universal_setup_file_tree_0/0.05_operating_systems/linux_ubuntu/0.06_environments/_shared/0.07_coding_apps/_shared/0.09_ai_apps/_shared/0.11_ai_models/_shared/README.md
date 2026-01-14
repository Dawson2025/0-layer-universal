# sub_layer_0.11_ai_models

**Purpose**: Approved AI models and usage guidance.

## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

## Structure

```
sub_layer_0.11_ai_models/
└── (content to be added)
```

## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0.09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0.10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

## ⚠️ Linux/Ubuntu-Specific Model Access Issues

**CRITICAL**: AI model access to MCP tools is limited on Linux. Read:

- **[Linux/Ubuntu Model Access Issues](trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md)**: Model access limitations on Linux

**Key Issues**:
- Some MCP tools unavailable to models on Linux
- Tool naming conventions may differ
- Model fallback strategies need Linux-specific configuration
- Model instructions must account for Linux tool limitations

**Related Documentation**:
- **OS-Level Issues**: `../sub_layer_0.05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Cursor IDE Issues**: `../sub_layer_0.07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/CURSOR_IDE_LINUX_MCP_ISSUES.md`
- **MCP Setup**: `../sub_layer_0.10_mcp_servers_and_tools_setup/`

## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
