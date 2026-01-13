# Layer & Stage System Management

This directory contains documentation and plans for **managing the layering and staging system itself** - the meta-level documentation about how to set up, maintain, and extend the framework.

## Contents

| File/Folder | Purpose |
|-------------|---------|
| `MCP_DOCUMENTATION_PLAN.md` | Plan for documenting MCP servers & APIs |
| `plans/` | Active planning documents |
| `setup/` | Setup guides for the system |
| `management/` | Ongoing management protocols |

## Distinction from `0.01_layer_stage_framework/`

| This folder (`0.00_`) | Framework folder (`0.01_`) |
|----------------------|---------------------------|
| **Meta**: How to manage the system | **Content**: Templates & guides for using the system |
| Plans, setup, maintenance | Layer templates, feature guides |
| System administration | System usage |

## Structural Change Checklist

When making structural changes to the framework (renaming directories, adding new stages/layers, modifying the hierarchy), **ALL** of the following MUST be updated:

| Priority | Location | File | What to Update |
|----------|----------|------|----------------|
| 1 | **Here** | `README.md` (this file) | Update change log below |
| 2 | Here | `MCP_DOCUMENTATION_PLAN.md` | Any active plans referencing changed paths |
| 3 | `layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/` | `universal_init_prompt.md` | Directory paths and structure diagrams |
| 4 | `layer_0_universal/0.02_sub_layers/0.00_sub_layer_registry/` | `sub_layer_registry.yaml` | Registry entries |
| 5 | `0.01_layer_stage_framework/` | All template READMEs | Directory structures in templates |
| 6 | All locations | `*.md`, `*.yaml`, `*.sh`, `*.txt`, `*.csv` files | Use `find` + `sed` for bulk path updates |

### Bulk Update Command

```bash
# Replace old_name with new_name across all documentation
find /path/to/0_ai_context -type f \( -name "*.md" -o -name "*.yaml" -o -name "*.sh" -o -name "*.txt" -o -name "*.csv" \) \
  -exec sed -i 's/old_name/new_name/g' {} \;
```

### Recent Structural Changes

| Date | Change |
|------|--------|
| 2026-01-13 | Renamed `0.06_mcp_servers` → `0.06_mcp_servers_and_apis_and_secrets` |

## Related

- `0.01_layer_stage_framework/` - Templates and guides for using the framework
- `layer_0_universal/` - Universal layer implementation
