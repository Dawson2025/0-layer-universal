---
resource_id: "7be3ea0e-9397-4368-bc44-7c83cb47524a"
resource_type: "readme_document"
resource_name: "README"
---
# ⚠️ DEPRECATED - This Sublayer Has Been Consolidated

**Deprecation Date**: 2026-01-01
**Replaced By**: `sub_layer_0_05-0.014_setup`

This sublayer has been consolidated into the unified setup sublayer for better organization and discoverability.

<!-- section_id: "1a7cd14f-8d30-47d7-8c2d-a9dc3c7f79f3" -->
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

<!-- section_id: "25ad3d22-3734-4156-bd12-f3dabbc4698e" -->
## Why Consolidate?

- **Single entry point** for all setup docs
- **Better discoverability** through hierarchical file tree
- **Cross-cutting organization** with `_shared/` folders at every level
- **Easier maintenance** - one structure instead of 10

<!-- section_id: "6345949e-030d-4726-8e18-d452f2a6ddda" -->
## Legacy Content Below

The original content of this sublayer is preserved below for reference, but should not be updated. All new setup documentation should go into the consolidated sublayer.

---

# Sub Layer 0.08: Apps, Browsers, and Extensions Setup

**Purpose**: Setup for general apps (non-AI), browsers, and browser extensions used across projects.

<!-- section_id: "92074233-a59c-4aff-9441-dbbe2b0f8b06" -->
## Notes
- Keep OS-specific details in `sub_layer_0_05_os_setup/`.
- Keep AI app install/config in `sub_layer_0_09_ai_apps_tools_setup/`.
- Keep MCP-specific setup in `sub_layer_0_10_mcp_servers_and_tools_setup/`.

Add slot-specific docs here over time.
