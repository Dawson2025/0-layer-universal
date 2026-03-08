---
resource_id: "6a43fb56-30df-48a7-8235-96bace151a7d"
resource_type: "readme_document"
resource_name: "README"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

<!-- section_id: "fe5a8fc8-8a72-4a2b-a758-68427c98409d" -->
## Migration Path

All setup documentation is now located in:
```
sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/
```

Navigate the file tree by your configuration:
1. Choose your OS: `0.05_operating_systems/<os>/`
2. Choose your environment: `0.06_environments/<env>/`
3. Choose your coding app: `0.07_coding_apps/<app>/`
4. Continue through all levels to find your specific setup documentation

<!-- section_id: "5a01fe0d-2dce-4cc8-9c34-c300b75422c3" -->
## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

<!-- section_id: "0ce1a0d8-6474-4093-8515-9e8824e5ee6a" -->
## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# sub_layer_0_11_ai_models

**Purpose**: Approved AI models and usage guidance.

<!-- section_id: "a3563290-0331-4c6d-b5b1-9a8be313ddff" -->
## Overview

This sublayer contains documentation about approved AI models, their usage guidelines, and best practices for selecting and using models across different contexts.

<!-- section_id: "998a376b-a73a-43be-aa7f-f25323b6f35c" -->
## Structure

```
sub_layer_0_11_ai_models/
└── (content to be added)
```

<!-- section_id: "c618bafb-97eb-4a81-ab90-26d8b16ee70f" -->
## Relationship to Other Sublayers

- **Depends on**: 
  - `sub_layer_0_09_ai_apps_tools_setup` - Models are used through AI apps/tools
  - `sub_layer_0_10_mcp_servers_and_tools_setup` - Some models may be accessed via MCP
- **Provides to**: All layers that need model selection and usage guidance

<!-- section_id: "50cc1d5a-8b46-4f10-bcfe-20c7e92b7621" -->
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

<!-- section_id: "3dc1bafc-4b7d-4ecf-9c52-d7c66a715506" -->
## Notes

- Document approved models and usage guidance here
- Add slot-specific docs here over time
- Keep mappings up to date if paths change

---

**Last Updated**: 2025-12-02  
**Version**: 1.0
