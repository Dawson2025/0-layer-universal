---
resource_id: "839dac09-dab6-45ff-b32e-1a723781338a"
resource_type: "document"
resource_name: "README.sync-conflict-20260101-084512-IF2WOGZ"
---
# sub_layer_0_05-0.014_setup - Universal Setup Sublayer

**Sublayer Range**: 0.05 through 0.14
**Purpose**: Consolidated setup documentation covering all setup dimensions

---

<!-- section_id: "11d5aafa-9df3-4406-8df1-491ff682a322" -->
## Overview

This sublayer consolidates all setup documentation that was previously scattered across sublayers 0.05 through 0.14:

- **0.05** - Operating System Setup
- **0.06** - Environment Setup
- **0.07** - Coding App Setup
- **0.08** - Apps/Browsers/Extensions Setup
- **0.09** - AI Apps/Tools Setup
- **0.10** - MCP Servers and Tools Setup
- **0.11** - AI Models
- **0.12** - Universal Tools
- **0.13** - Universal Protocols
- **0.14** - Agent Setup

Instead of maintaining 10 separate sublayers, all setup documentation is now organized in a single **hierarchical file tree structure**.

---

<!-- section_id: "8a351b36-3cad-42f1-a2cb-c74c7c77a306" -->
## Primary Navigation: Universal Setup File Tree

**Main entry point**: `0.01_universal_setup_file_tree_0/`

This file tree provides hierarchical navigation across all 10 setup dimensions:

```
OS → Environment → Coding App → AI App → MCP Server → AI Model → Universal Tools → Protocols → Agent Setup
```

<!-- section_id: "63728b80-a2c7-489e-acbd-cdb75ffff75d" -->
### Quick Start

```bash
# Navigate to the file tree
cd 0.01_universal_setup_file_tree_0/

# Read the quick start guide
cat QUICK_START.md

# Navigate to your specific setup
cd 0.05_operating_systems/<your_os>/
# Continue navigating down...
```

<!-- section_id: "3c7f78e2-975b-40d1-abc1-300b14e7283d" -->
### Key Files in File Tree

- **README.md** - Complete navigation guide
- **QUICK_START.md** - How to use the file tree
- **STRUCTURE_VISUALIZATION.md** - Visual hierarchy
- **DESIGN_DOCUMENTATION.md** - Design decisions and technical details
- **IMPLEMENTATION_SUMMARY.md** - What was delivered

---

<!-- section_id: "4e85ec48-09b0-40dd-92dd-995057915c40" -->
## Organization Structure

<!-- section_id: "8a268759-16c6-4704-b72a-f70bc5179bc8" -->
### Primary Organization: File Tree

The file tree at `0.01_universal_setup_file_tree_0/` is the **primary organizational structure** for this sublayer. It provides:

1. **Hierarchical navigation** - Drill down from general to specific
2. **Cross-cutting organization** - `_shared/` folders at every level
3. **Combination-specific docs** - Setup for specific OS + IDE + MCP combinations
4. **Discoverability** - Browse to find relevant documentation

<!-- section_id: "8f68a8d9-1c1b-4050-b6da-61d730d0a81d" -->
### Content Organization

All content from the old sublayers (0.05-0.14) has been integrated into the file tree at appropriate levels:

- **Level 1 (_shared)**: OS and environment setup docs
- **Level 5 (_shared/0.10_mcp_servers_and_apis_and_secrets/_shared/)**: MCP core documentation and configuration guides
- **Level 7 (_shared/.../0.08_universal_tools/)**: Universal tools documentation
- **Level 8 (_shared/.../0.09_protocols/)**: Protocol specifications and standards
- **Level 9**: Agent setup documentation

Each level's `_shared/` directory contains documentation that applies across all options at that level.

---

<!-- section_id: "2182c684-075c-4337-ba62-1ca5526b8fbe" -->
## How to Use This Sublayer

<!-- section_id: "6695c7d6-d911-44f3-8df9-188300bdb269" -->
### For Users: Finding Setup Documentation

1. **Start at the file tree**: `cd 0.01_universal_setup_file_tree_0/`
2. **Navigate by your configuration**:
   - Choose your OS: `cd 0.05_operating_systems/<os>/`
   - Choose your environment: `cd 0.06_environments/<env>/`
   - Choose your coding app: `cd 0.07_coding_apps/<app>/`
   - Continue through all levels to your specific combination
3. **Read setup docs**: `cat general_setup_and_config/README.md`

<!-- section_id: "ed90f10c-6981-4e92-941e-83b9fa644a30" -->
### For Maintainers: Adding Setup Documentation

1. **Determine the appropriate path** in the file tree
2. **Use `_shared/` folders** for cross-cutting setup (applies to all options)
3. **Create specific paths** for OS/app/tool-specific setup
4. **Add setup docs** in `general_setup_and_config/README.md`
5. **Link to detailed docs** in other sublayers if needed

---

<!-- section_id: "e89488a9-0a0b-43ee-b96a-3e32b54a0a14" -->
## Relationship to Other Sublayers

<!-- section_id: "a55b3524-4bdd-4dc7-8768-1110d47feb2d" -->
### Previously Separate Sublayers (Now Consolidated)

This sublayer consolidates what were previously 10 separate sublayers:

| Old Sublayer | Now Located In |
|-------------|----------------|
| sub_layer_0_05_os_setup | File tree: `0.05_operating_systems/` |
| sub_layer_0_06_environment_setup | File tree: `0.06_environments/` |
| sub_layer_0_07_coding_app_setup | File tree: `0.07_coding_apps/` |
| sub_layer_0_08_apps_browsers_extensions_setup | File tree: (browsers under coding apps) |
| sub_layer_0_09_ai_apps_tools_setup | File tree: `0.09_ai_apps/` |
| sub_layer_0_10_mcp_servers_and_tools_setup | File tree: `0.10_mcp_servers_and_apis_and_secrets/` |
| sub_layer_0_11_ai_models | File tree: `0.07_ai_models/` |
| sub_layer_0_12_universal_tools | File tree: `0.08_universal_tools/` |
| sub_layer_0_13_universal_protocols | File tree: `0.09_protocols/` |
| sub_layer_0_14_agent_setup | File tree: `0.10_agent_setup/` |

<!-- section_id: "d5131b80-f20a-4d25-b721-3ba752d3c9f6" -->
### Integration with Non-Setup Sublayers

This sublayer works alongside other universal sublayers:

- **sub_layer_0_01_basic_prompts_throughout** - Init prompts
- **sub_layer_0_02_software_engineering_knowledge_system** - SE knowledge
- **sub_layer_0_03_universal_principles** - Universal principles
- **sub_layer_0_04_universal_rules** - Universal rules

---

<!-- section_id: "e0d10e16-1552-4338-8535-a1ca6f3b7306" -->
## Why Consolidate?

<!-- section_id: "64fb196d-ce78-430a-83b0-764c91a30cfb" -->
### Problems with 10 Separate Sublayers

1. **Scattered documentation** - Hard to find setup for specific combinations
2. **No unified navigation** - Each sublayer had its own organization
3. **Duplication** - Similar setup docs repeated across sublayers
4. **Maintenance burden** - 10 separate structures to maintain
5. **Unclear relationships** - How does OS setup relate to AI app setup?

<!-- section_id: "07a40f61-d8d2-45b5-9860-8e105f8513bd" -->
### Benefits of Consolidated Sublayer

1. **Single entry point** - One place to find all setup docs
2. **Hierarchical organization** - Clear relationships between setup dimensions
3. **Cross-cutting concerns** - `_shared/` folders prevent duplication
4. **Easier maintenance** - One structure instead of 10
5. **Better discoverability** - Browse the tree to see what's available

---

<!-- section_id: "45e38893-783c-4ec6-9ee5-c3a2c285a0e2" -->
## Structure Statistics

- **Sublayer range**: 0.05-0.014 (consolidates 10 sublayers)
- **File tree directories**: 99+
- **Documentation files**: 14+ README files
- **Setup dimensions**: 10 levels of hierarchy
- **Total documentation**: 2,400+ lines

---

<!-- section_id: "ee2cfda4-2f65-4043-8b92-86d28f0110f3" -->
## Migration Status

<!-- section_id: "0fabb7b1-d92f-4a67-8626-01741d79bea8" -->
### Completed ✅

✅ File tree structure created (`0.01_universal_setup_file_tree_0/`)
✅ Sublayer renamed to `sub_layer_0_05-0.014_setup`
✅ Documentation created (README, QUICK_START, DESIGN_DOCUMENTATION, etc.)
✅ Content from old sublayers (0.06-0.14) migrated into file tree at appropriate levels
✅ Sublayer registry updated to reflect consolidation
✅ References in universal_init_prompt.md updated
✅ Old sublayer directories removed

<!-- section_id: "389cd55b-af42-48fb-998d-58c0ecccda21" -->
### Content Integration Mapping

All content has been integrated into the file tree hierarchy:

- **sub_layer_0_05 → Level 1**: OS-specific setup in `0.05_operating_systems/`
- **sub_layer_0_07 → Level 2**: Environment setup in `0.06_environments/`
- **sub_layer_0_06 → Level 3**: Coding app setup in `0.07_coding_apps/`
- **sub_layer_0_09 → Level 4**: AI apps setup in `0.09_ai_apps/`
- **sub_layer_0_10 → Level 5**: MCP servers in `0.10_mcp_servers_and_apis_and_secrets/_shared/`
- **sub_layer_0_11 → Level 6**: AI models in `0.07_ai_models/`
- **sub_layer_0_12 → Level 7**: Universal tools in `0.08_universal_tools/`
- **sub_layer_0_13 → Level 8**: Protocols in `0.09_protocols/`
- **sub_layer_0_14 → Level 9**: Agent setup in `0.10_agent_setup/`

<!-- section_id: "3fba9a19-2f67-4357-9813-9c48cc160bbb" -->
### Future Enhancements

🔮 Continue organizing content within the hierarchy
🔮 Add more terminal node documentation at specific paths
🔮 Create cross-references between related documentation

---

<!-- section_id: "ae1b8795-f323-4b52-be1f-6978082f1385" -->
## Quick Reference

<!-- section_id: "b289cc15-f6a8-4f5a-9c06-92ad178d7507" -->
### Finding Setup Documentation

**Universal Git setup** (all platforms):
```
0.01_universal_setup_file_tree_0/
→ 0.05_operating_systems/_shared/
→ 0.06_environments/_shared/
→ 0.07_coding_apps/_shared/
→ 0.09_ai_apps/_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_shared/
→ 0.07_ai_models/_shared/
→ 0.08_universal_tools/git/
→ general_setup_and_config/
```

**Linux + Cursor + Playwright MCP**:
```
0.01_universal_setup_file_tree_0/
→ 0.05_operating_systems/linux_ubuntu/
→ 0.06_environments/development/
→ 0.07_coding_apps/cursor/
→ 0.09_ai_apps/cursor_agent/
→ 0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/
→ general_setup_and_config/
```

**MCP core issues** (any setup):
```
0.01_universal_setup_file_tree_0/
→ 0.05_operating_systems/_shared/
→ .../_shared/
→ 0.10_mcp_servers_and_apis_and_secrets/_mcp_core/
→ general_setup_and_config/
```

---

<!-- section_id: "b96f218e-6f65-479e-af5f-496cccb4ccd1" -->
## Contact & Support

For issues or questions about this sublayer:
- Read the file tree documentation: `0.01_universal_setup_file_tree_0/README.md`
- Check design documentation: `0.01_universal_setup_file_tree_0/DESIGN_DOCUMENTATION.md`
- Review implementation summary: `0.01_universal_setup_file_tree_0/IMPLEMENTATION_SUMMARY.md`

---

**Last Updated**: 2026-01-01
**Version**: 2.0 (Fully Integrated Hierarchical Setup)
