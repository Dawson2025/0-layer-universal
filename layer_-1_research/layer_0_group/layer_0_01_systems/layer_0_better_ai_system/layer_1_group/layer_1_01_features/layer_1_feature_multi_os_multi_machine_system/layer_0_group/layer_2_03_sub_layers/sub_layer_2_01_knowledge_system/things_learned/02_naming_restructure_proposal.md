---
resource_id: "23a87d1d-163d-41e0-ba30-e38722c653ec"
resource_type: "document"
resource_name: "02_naming_restructure_proposal"
---
# Setup Sub-Layer Naming & Restructure Proposal

**Date**: 2026-01-25
**Source**: User conversation + AI System Audit
**Severity**: CRITICAL
**Status**: COMPLETED on 2026-01-25

---

<!-- section_id: "d56548b2-2b7b-4acd-ae0d-85ccceb387d4" -->
## Problem Statement

Inside `sub_layer_0_05+_setup_dependant/`, child folders incorrectly use `layer_0_XX_` naming when they should use `sub_layer_0_XX_` naming.

**Rule**: When you're inside a `sub_layer`, children should also be `sub_layer` (not `layer`).

---

<!-- section_id: "657d593f-2543-4c28-824a-37af0ecd77c6" -->
## Current Structure (WRONG)

```
sub_layer_0_05+_setup_dependant/
├── layer_0_01_universal_setup_file_tree_0/     ❌ WRONG: uses "layer_"
│   └── layer_0_05_operating_systems/           ❌ WRONG: uses "layer_"
│       ├── linux_ubuntu/
│       │   └── layer_0_06_environments/        ❌ WRONG: uses "layer_"
│       │       ├── local/
│       │       │   └── layer_0_07_coding_apps/ ❌ WRONG: uses "layer_"
│       │       └── remote/
│       ├── macos/
│       ├── windows/
│       └── wsl/
├── legacy_sublayer_readmes/
├── docs/                                        # Loose docs
├── scripts/
├── *.md files (many migration/audit reports)   # Clutter
└── ui_controls/
```

**Issues**:
1. Uses `layer_0_XX` instead of `sub_layer_0_XX`
2. `layer_0_01_universal_setup_file_tree_0` wrapper is unnecessary
3. Lots of loose files and reports cluttering the structure
4. Numbering (0_05, 0_06, 0_07) doesn't follow consistent pattern

---

<!-- section_id: "888886a7-6766-4a81-9f20-9aa86d464ace" -->
## Proposed Structure (CORRECT)

Just like features use `layer_N_feature_name`, every folder at each level gets the `sub_layer_0_XX_` prefix.

```
sub_layer_0_05+_setup_dependant/
├── README.md
├── sub_layer_0_05_operating_systems/                    ✅ Category has prefix
│   ├── sub_layer_0_05__shared/                          ✅ Each OS has prefix (double underscore for readability)
│   ├── sub_layer_0_05_linux_ubuntu/                     ✅ Each OS has prefix
│   │   └── sub_layer_0_06_environments/                 ✅ Category has prefix
│   │       ├── sub_layer_0_06_local/                    ✅ Each environment has prefix
│   │       │   ├── sub_layer_0_07_desktop/
│   │       │   │   └── sub_layer_0_08_troubleshooting/
│   │       │   └── sub_layer_0_07_terminal/
│   │       └── sub_layer_0_06_remote/                   ✅ Each environment has prefix
│   ├── sub_layer_0_05_macos/
│   │   └── sub_layer_0_06_environments/
│   │       ├── sub_layer_0_06_local/
│   │       └── sub_layer_0_06_remote/
│   ├── sub_layer_0_05_windows/
│   │   └── sub_layer_0_06_environments/
│   └── sub_layer_0_05_wsl/
│       └── sub_layer_0_06_environments/
├── sub_layer_0_09_ai_apps/
│   ├── sub_layer_0_10_mcp_servers/
│   ├── sub_layer_0_11_ai_models/
│   └── sub_layer_0_12_agent_setup/
├── sub_layer_0_13_protocols/
└── sub_layer_0_14_archives/
```

<!-- section_id: "a7f49169-569b-4460-a772-0c97daf42ea5" -->
### Pattern Comparison

**Features pattern**:
```
layer_1_features/
├── layer_1_feature_multi_os_system/       # Each feature has layer_1_feature_ prefix
├── layer_1_feature_better_setup/
└── layer_1_feature_ai_context/
```

**Sub-layers pattern** (same logic):
```
sub_layer_0_05_operating_systems/
├── sub_layer_0_05_linux_ubuntu/           # Each OS has sub_layer_0_05_ prefix
├── sub_layer_0_05_macos/
├── sub_layer_0_05_windows/
└── sub_layer_0_05_wsl/
```

---

<!-- section_id: "4fb9f627-bd3c-475e-8e5a-ec6a75b7afe9" -->
## Naming Rules

<!-- section_id: "9f43bcee-d2fa-40ae-b4c9-704b1f5d117f" -->
### Rule 1: Every folder at a sub_layer level gets the prefix
Just like features: `layer_1_feature_X`, `layer_1_feature_Y`, etc.
Sub-layers: `sub_layer_0_05_linux`, `sub_layer_0_05_macos`, etc.

<!-- section_id: "a3c01ee5-59f5-4bc3-876e-8d2c8ffb0d87" -->
### Rule 2: The number indicates the depth/specificity level
- `sub_layer_0_05_*` = Operating system level
- `sub_layer_0_06_*` = Environment level (inside an OS)
- `sub_layer_0_07_*` = Application level (inside an environment)
- etc.

<!-- section_id: "a1704743-a284-4598-9ed0-3ce0add55555" -->
### Rule 3: Category folders and item folders both get prefixes
```
sub_layer_0_05_operating_systems/           # Category
├── sub_layer_0_05_linux_ubuntu/            # Item (same number as category)
├── sub_layer_0_05_macos/                   # Item
└── sub_layer_0_05_windows/                 # Item
```

<!-- section_id: "515e3b5b-e8bb-4750-8ba1-a333d2eaabd3" -->
### Rule 4: When nesting gets deep (subx2)
If you're multiple sub_layer levels deep and need to create new organizational units:
```
sub_layer_0_06_local/
└── setup/
    └── subx2_layer_0_01_troubleshooting/   # subx2_ indicates 2+ levels deep
```

<!-- section_id: "d395a388-2a87-47de-93e9-62288ab23f5e" -->
### Full Pattern Example:
```
layer_0_03_sub_layers/
└── sub_layer_0_05+_setup_dependant/
    └── sub_layer_0_05_operating_systems/
        └── sub_layer_0_05_linux_ubuntu/         # OS item (0_05)
            └── sub_layer_0_06_environments/     # Environment category (0_06)
                └── sub_layer_0_06_local/        # Environment item (0_06)
                    └── sub_layer_0_07_desktop/  # App category (0_07)
                        └── subx2_layer_0_01_gnome_fixes/  # Deep nesting (subx2)
```

---

<!-- section_id: "96fe27a1-4199-47e1-ad9e-1d588df85ef5" -->
## Migration Log

The migration was completed on 2026-01-25. The following actions were taken:

<!-- section_id: "5f2f5544-726c-4875-88e7-c94db193229b" -->
### Phase 1: Archive Clutter
- All loose `*.md` reports were moved to `sub_layer_0_14_archives/migration_reports/`
- `legacy_sublayer_readmes/` was moved to `sub_layer_0_14_archives/legacy/`
- `docs/` content was moved to `sub_layer_0_14_archives/old_docs/`

<!-- section_id: "1cf53621-c24c-4274-b959-b3afe0e18ce1" -->
### Phase 2: Flatten Structure
- The `layer_0_01_universal_setup_file_tree_0/` wrapper was removed.
- `layer_0_05_operating_systems/` was moved up to the root of `sub_layer_0_05+_setup_dependant/`.

<!-- section_id: "cdb59843-40a7-430c-a382-28b45c3025d5" -->
### Phase 3: Rename Folders
- All `layer_0_XX_*` directories were renamed to `sub_layer_0_XX_*`.
- All directories inside `sub_layer_0_05_operating_systems` and `sub_layer_0_06_environments` were prefixed with the appropriate `sub_layer_` number.

<!-- section_id: "c0583bb7-f0dc-41bb-8107-06fa6ad4880d" -->
### Phase 4: Validate
- `universal_init_prompt.md` was updated with the new paths.
- Other documentation files (`ai_system_problems_audit.md`, `01_setup_problems.md`, and this file) were updated to reflect the completion of the refactoring.

---

<!-- section_id: "d0fa4052-1895-49ff-a8a0-34c0e5b699d9" -->
## Files to Update After Migration

1. `universal_init_prompt.md` - Directory structure diagram
2. `layer_0_01_ai_manager_system/specific/` - References to setup paths
3. Any CLAUDE.md files referencing setup locations
4. Registry files (when created)

---

<!-- section_id: "b9ee068c-bb8b-4c9c-b978-5f655959de7c" -->
## Related

- `better_layer_stage_system` - Naming convention standards
- `ai_documentation_system` - Path reference updates
- `ai_automation_system` - Migration scripts
