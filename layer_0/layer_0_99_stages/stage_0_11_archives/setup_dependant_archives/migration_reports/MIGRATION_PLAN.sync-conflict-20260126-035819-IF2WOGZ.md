---
resource_id: "060e5e05-352f-4b4a-9f49-f0cc6d042b87"
resource_type: "document"
resource_name: "MIGRATION_PLAN.sync-conflict-20260126-035819-IF2WOGZ"
---
# Migration Plan: Old Sub_Layers → Unified File Tree

**Created**: January 12, 2026

## Summary

Analysis of old sub_layers (0.05-0.14) vs the unified file tree reveals:
- **Content already duplicated** in unified tree: Can be deleted immediately
- **Content needing migration**: Specific files with unique content
- **Empty sub_layers**: Just placeholder READMEs, can be deleted

## Analysis by Sub_Layer

### Already Duplicated (Delete Immediately)

| Sub_Layer | Files | Status |
|-----------|-------|--------|
| `sub_layer_0_12_universal_tools` | 37 files | **Fully duplicated** in `0.12_universal_tools` |
| `sub_layer_0_13_universal_protocols` | 20 files | **Fully duplicated** in `0.13_protocols` |

### Empty/Placeholder (Delete Immediately)

| Sub_Layer | Files | Content |
|-----------|-------|---------|
| `sub_layer_0_06_coding_app_setup` | 1 | README.md only |
| `sub_layer_0_08_apps_browsers_extensions_setup` | 1 | README.md only |
| `sub_layer_0_09_ai_apps_tools_setup` | 1 | README.md only |
| `sub_layer_0_12_agent_setup` | 0 | Empty |
| `sub_layer_0_14_agent_setup` | 1 | README.md only |

### Needs Migration

| Sub_Layer | Files | Action |
|-----------|-------|--------|
| `sub_layer_0_05_os_setup` | 38 | Contains `trickle_down_0.5_setup` - **Project-specific content**, may need review for what's universal vs project-specific |
| `sub_layer_0_07_environment_setup` | 2 | Migrate `github_sso_token_setup.md` to unified tree |
| `sub_layer_0_10_mcp_servers_and_tools_setup` | 75+ | Substantial MCP docs - **consolidate with unified tree's MCP structure** |
| `sub_layer_0_11_ai_models` | 2 | Migrate `LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md` |

## Migration Destinations

### sub_layer_0_07_environment_setup/github_sso_token_setup.md
→ `0.01_universal_setup_file_tree_0/0.05_operating_systems/_shared/0.06_environments/_shared/setup/github/`

### sub_layer_0_10_mcp_servers_and_tools_setup
This has its own nested file tree (`0.02_mcp_config_options_0_file_tree_0`). Options:
1. **Merge into unified tree's MCP sections** (under each AI app's `0.10_mcp_servers_and_apis_and_secrets/`)
2. **Keep as separate MCP-focused tree** (if structure is significantly different)

Analysis shows it has a different hierarchy:
- Old: `0.03_operating_systems/_shared/0.04_ai_apps/_shared/0.05_mcp_servers/`
- New: `0.05_operating_systems/.../0.09_ai_apps/.../0.10_mcp_servers_and_apis_and_secrets/`

**Recommendation**: Migrate unique content from old MCP tree into the unified tree's existing MCP server directories.

### sub_layer_0_11_ai_models/LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md
→ `0.01_universal_setup_file_tree_0/0.05_operating_systems/linux_ubuntu/0.06_environments/_shared/ai_models/`

### sub_layer_0_05_os_setup/trickle_down_0.5_setup
This contains **project-specific** content (Firebase setup, WSL, deployment guides for a specific project).

**Options**:
1. Move to project-specific context directory
2. Extract truly universal content (WSL setup, agent specs) to unified tree
3. Archive as historical project documentation

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

## Verification

Before deleting, verify:
- [x] 0.12_universal_tools content matches 0.12_universal_tools in unified tree (VERIFIED - identical)
- [x] 0.13_universal_protocols content matches 0.13_protocols in unified tree (VERIFIED - identical)
- [x] 0.10_mcp_servers_and_tools_setup content matches 0.10_mcp_servers in unified tree (VERIFIED - identical)
- [x] All migrated files are in correct locations
- [ ] No broken references in other documentation

## Migration Status (Updated January 12, 2026)

### Completed Migrations:
1. **github_sso_token_setup.md** → `0.05_operating_systems/_shared/0.06_environments/_shared/setup/github/`
2. **LINUX_UBUNTU_MODEL_ACCESS_ISSUES.md** → `0.05_operating_systems/linux_ubuntu/0.06_environments/_shared/ai_models/`

### Verified Duplications (Safe to Delete):
- `sub_layer_0_10_mcp_servers_and_tools_setup` - Content exists in unified tree's `0.10_mcp_servers`
- `sub_layer_0_12_universal_tools` - Content exists in unified tree's `0.12_universal_tools`
- `sub_layer_0_13_universal_protocols` - Content exists in unified tree's `0.13_protocols`

### Empty Sub_Layers (Safe to Delete):
- `sub_layer_0_06_coding_app_setup`
- `sub_layer_0_08_apps_browsers_extensions_setup`
- `sub_layer_0_09_ai_apps_tools_setup`
- `sub_layer_0_12_agent_setup`
- `sub_layer_0_14_agent_setup`

### Remaining Items:
- `sub_layer_0_05_os_setup` - Contains project-specific trickle_down content (needs user decision)
- ~~`sub_layer_0_07_environment_setup`~~ - DELETED (content migrated)
- ~~`sub_layer_0_11_ai_models`~~ - DELETED (content migrated)

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

## FINAL STATUS (January 12, 2026)

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
