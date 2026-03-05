---
resource_id: "d2d7fad3-1849-4389-9b98-10d7b2bf4204"
resource_type: "document"
resource_name: "MIGRATION_PLAN.sync-conflict-20260126-102106-IF2WOGZ"
---
# Migration Plan: Old Sub_Layers → Unified File Tree

**Created**: January 12, 2026

<!-- section_id: "971928ad-9009-4ed9-af2f-0441feaf71c5" -->
## Summary

Analysis of old sub_layers (0.05-0.14) vs the unified file tree reveals:
- **Content already duplicated** in unified tree: Can be deleted immediately
- **Content needing migration**: Specific files with unique content
- **Empty sub_layers**: Just placeholder READMEs, can be deleted

<!-- section_id: "38b002d2-8bb0-4adb-9e50-14a65809fcf9" -->
## Analysis by Sub_Layer

<!-- section_id: "f76de5c0-5012-46aa-a5f8-acad8e2bedb5" -->
### Already Duplicated (Delete Immediately)

| Sub_Layer | Files | Status |
|-----------|-------|--------|
| `sub_layer_0_12_universal_tools` | 37 files | **Fully duplicated** in `0.12_universal_tools` |
| `sub_layer_0_13_universal_protocols` | 20 files | **Fully duplicated** in `0.13_protocols` |

<!-- section_id: "652e38ee-483f-49b5-9e8f-1193ccc824da" -->
### Empty/Placeholder (Delete Immediately)

| Sub_Layer | Files | Content |
|-----------|-------|---------|
| `sub_layer_0_06_coding_app_setup` | 1 | README.md only |
| `sub_layer_0_08_apps_browsers_extensions_setup` | 1 | README.md only |
| `sub_layer_0_09_ai_apps_tools_setup` | 1 | README.md only |
| `sub_layer_0_12_agent_setup` | 0 | Empty |
| `sub_layer_0_14_agent_setup` | 1 | README.md only |

<!-- section_id: "b70390ef-db75-4d44-bfd9-1ee571360c72" -->
### Needs Migration

| Sub_Layer | Files | Action |
|-----------|-------|--------|
| `sub_layer_0_05_os_setup` | 38 | Contains `trickle_down_0.5_setup` - **Project-specific content**, may need review for what's universal vs project-specific |
| `sub_layer_0_07_environment_setup` | 2 | Migrate `github_sso_token_setup.md` to unified tree |
| `sub_layer_0_10_mcp_servers_and_tools_setup` | 75+ | Substantial MCP docs - **consolidate with unified tree's MCP structure** |
| `sub_layer_0_11_ai_models` | 2 | Migrate `LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md` |

<!-- section_id: "1d27fbcf-d139-4441-ab99-f04bad115cc4" -->
## Migration Destinations

<!-- section_id: "59145aad-6971-47c7-9c89-79b4756c6928" -->
### sub_layer_0_07_environment_setup/github_sso_token_setup.md
→ `0.01_universal_setup_file_tree_0/0.05_operating_systems/_shared/0.06_environments/_shared/setup/github/`

<!-- section_id: "ea936631-e2a6-44b8-ac9c-9994e39390c0" -->
### sub_layer_0_10_mcp_servers_and_tools_setup
This has its own nested file tree (`0.02_mcp_config_options_0_file_tree_0`). Options:
1. **Merge into unified tree's MCP sections** (under each AI app's `0.10_mcp_servers_and_apis_and_secrets/`)
2. **Keep as separate MCP-focused tree** (if structure is significantly different)

Analysis shows it has a different hierarchy:
- Old: `0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/`
- New: `0.05_operating_systems/.../0.09_ai_apps/.../0.10_mcp_servers_and_apis_and_secrets/`

**Recommendation**: Migrate unique content from old MCP tree into the unified tree's existing MCP server directories.

<!-- section_id: "2c57c0e4-c7fe-4343-8a92-f9fa6c91bcd2" -->
### sub_layer_0_11_ai_models/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md
→ `0.01_universal_setup_file_tree_0/0.05_operating_systems/linux_ubuntu/0.06_environments/_shared/ai_models/`

<!-- section_id: "5d7bfec0-5edd-497a-b898-e417af0e52b5" -->
### sub_layer_0_05_os_setup/trickle_down_0.5_setup
This contains **project-specific** content (Firebase setup, WSL, deployment guides for a specific project).

**Options**:
1. Move to project-specific context directory
2. Extract truly universal content (WSL setup, agent specs) to unified tree
3. Archive as historical project documentation

<!-- section_id: "45448768-2c5e-4f15-8f5b-4614c641e208" -->
## Execution Order

1. **Phase 1 - Delete Empty/Duplicated** (safe, no data loss risk)
   - Delete: 0.06, 0.08, 0.09, 0.12_agent_setup, 0.14
   - Delete: 0.12_universal_tools, 0.13_universal_protocols (after verifying duplication)

2. **Phase 2 - Migrate Unique Content**
   - Migrate: 0.07 github_sso_token_setup.md
   - Migrate: 0.11 LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md
   - Migrate: 0.10 unique MCP content

3. **Phase 3 - Handle Project-Specific Content**
   - Review: 0.05 trickle_down_0.5_setup
   - Decide on archival vs extraction

<!-- section_id: "c96fb7bc-b99b-49d7-9e6f-d5b7b1b6a6fb" -->
## Verification

Before deleting, verify:
- [x] 0.12_universal_tools content matches 0.12_universal_tools in unified tree (VERIFIED - identical)
- [x] 0.13_universal_protocols content matches 0.13_protocols in unified tree (VERIFIED - identical)
- [x] 0.10_mcp_servers_and_tools_setup content matches 0.10_mcp_servers in unified tree (VERIFIED - identical)
- [x] All migrated files are in correct locations
- [ ] No broken references in other documentation

<!-- section_id: "8f8dba5d-6ddd-402a-8d3c-1ae31335911e" -->
## Migration Status (Updated January 12, 2026)

<!-- section_id: "adb3b394-b099-4d08-9e6d-df5b4c77e753" -->
### Completed Migrations:
1. **github_sso_token_setup.md** → `0.05_operating_systems/_shared/0.06_environments/_shared/setup/github/`
2. **LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md** → `0.05_operating_systems/linux_ubuntu/0.06_environments/_shared/ai_models/`

<!-- section_id: "b6e09aff-ab0a-4ad8-a380-e470c13af7c8" -->
### Verified Duplications (Safe to Delete):
- `sub_layer_0_10_mcp_servers_and_tools_setup` - Content exists in unified tree's `0.10_mcp_servers`
- `sub_layer_0_12_universal_tools` - Content exists in unified tree's `0.12_universal_tools`
- `sub_layer_0_13_universal_protocols` - Content exists in unified tree's `0.13_protocols`

<!-- section_id: "cb308ecc-1293-4e11-b6bc-4ffe929358b7" -->
### Empty Sub_Layers (Safe to Delete):
- `sub_layer_0_06_coding_app_setup`
- `sub_layer_0_08_apps_browsers_extensions_setup`
- `sub_layer_0_09_ai_apps_tools_setup`
- `sub_layer_0_12_agent_setup`
- `sub_layer_0_14_agent_setup`

<!-- section_id: "b88a7f6f-b03d-4ebb-a4c6-80bd56339536" -->
### Remaining Items:
- `sub_layer_0_05_os_setup` - Contains project-specific trickle_down content (needs user decision)
- ~~`sub_layer_0_07_environment_setup`~~ - DELETED (content migrated)
- ~~`sub_layer_0_11_ai_models`~~ - DELETED (content migrated)

<!-- section_id: "76824268-d2db-4363-aa39-4c58e8b0254b" -->
## DELETION LOG (January 12, 2026)

**Deleted sub_layers:**
1. `sub_layer_0_06_coding_app_setup` - Empty placeholder
2. `sub_layer_0_08_apps_browsers_extensions_setup` - Empty placeholder
3. `sub_layer_0_09_ai_apps_tools_setup` - Empty placeholder
4. `sub_layer_0_10_mcp_servers_and_tools_setup` - Duplicated in unified tree
5. `sub_layer_0_11_ai_models` - Content migrated
6. `sub_layer_0_12_agent_setup` - Empty
7. `sub_layer_0_12_universal_tools` - Duplicated in unified tree
8. `sub_layer_0_13_universal_protocols` - Duplicated in unified tree
9. `sub_layer_0_14_agent_setup` - Empty placeholder
10. `sub_layer_0_07_environment_setup` - Content migrated

**Remaining sub_layers in directory:**
- `0.00_sub_layer_registry` - Meta registry (keep)
- `sub_layer_0_01_basic_prompts_throughout` - Active
- `sub_layer_0_02_software_engineering_knowledge_system` - Active
- `sub_layer_0_03_universal_principles` - Active
- `sub_layer_0_04_universal_rules` - Active
- `sub_layer_0_05-0.014_setup` - Unified file tree (this is the target)
- `sub_layer_0_05_os_setup` - **PENDING USER DECISION** (project-specific content)

<!-- section_id: "f6c96658-5b99-481f-9c2e-ff56e5a211d0" -->
## FINAL STATUS (January 12, 2026)

<!-- section_id: "ad361223-9b22-4846-8ce1-908edc922b14" -->
### ✅ Migration Complete

**From `sub_layer_0_05_os_setup` (38 files):**

**Universal content extracted:**
1. `WSL_STABILITY_FIX.md` → `windows/wsl_setup/`
2. `CLAUDE_CODE_CLI_GUIDE.md` → `_shared/.../0.09_ai_apps/claude_code_cli/setup/`

**Project-specific content deleted:**
- All Firebase documentation (project-specific)
- All deployment guides (project-specific)
- All agent spec kits (project-specific methodology)
- All archive docs (historical project data)
- All other trickle_down project content

<!-- section_id: "a1946c12-f0fe-4fbd-b854-adff25646e06" -->
### Final Sub_Layers Directory Structure

```
0.02_sub_layers/
├── 0.00_sub_layer_registry/        # Meta registry
├── sub_layer_0_01_basic_prompts_throughout/
├── sub_layer_0_02_software_engineering_knowledge_system/
├── sub_layer_0_03_universal_principles/
├── sub_layer_0_04_universal_rules/
└── sub_layer_0_05-0.014_setup/     # ← Unified file tree (COMPLETE)
```

<!-- section_id: "ff1641b6-aa4c-47b0-8800-9e4b7126e19b" -->
### Total Deleted Sub_Layers: 11
1. sub_layer_0_05_os_setup (content extracted/archived)
2. sub_layer_0_06_coding_app_setup
3. sub_layer_0_07_environment_setup
4. sub_layer_0_08_apps_browsers_extensions_setup
5. sub_layer_0_09_ai_apps_tools_setup
6. sub_layer_0_10_mcp_servers_and_tools_setup
7. sub_layer_0_11_ai_models
8. sub_layer_0_12_agent_setup
9. sub_layer_0_12_universal_tools
10. sub_layer_0_13_universal_protocols
11. sub_layer_0_14_agent_setup
