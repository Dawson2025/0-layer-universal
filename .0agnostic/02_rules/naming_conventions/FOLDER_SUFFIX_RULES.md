---
resource_id: "8caf5ad8-a7a4-4744-a460-dd53521dc562"
resource_type: "rule"
resource_name: "FOLDER_SUFFIX_RULES"
---
# Folder Suffix Rules

<!-- section_id: "ceefcd1a-3f99-4ed3-99ed-c060dff734b1" -->
## Mandatory Suffixes

These suffixes have specific meanings and MUST be used correctly:

<!-- section_id: "a394a220-8a89-4bd6-a267-31e4be99d858" -->
### `_group` - Child Content Container

**Use when**: A folder contains direct children (content, files, subfolders)

**Pattern**: `layer_N_group/`, `sub_layer_N_XX_group/`

**Example**:
```
layer_-1_group/           # Contains layer -1's internal content
sub_layer_0_05_group/     # Contains sub-layer 5's direct content
```

<!-- section_id: "af44b410-2499-450d-b784-5e59a486079e" -->
### `_hierarchy` - Branching Sub-Layer Tree

**Use when**: A folder contains nested sub-layers that branch based on choices

**Pattern**: `sub_layer_N_XX+_<name>_hierarchy/`

**Example**:
```
sub_layer_0_04+_setup_dependant/
└── sub_layer_0_05_operating_systems/
    ├── sub_layer_0_05_linux/     → leads to different sub_layer_06
    ├── sub_layer_0_05_macos/     → leads to different sub_layer_06
    └── sub_layer_0_05_windows/   → leads to different sub_layer_06
```

**Key indicator**: The `05+` means "sub-layer 5 and beyond" - the hierarchy contains multiple levels.

<!-- section_id: "2fe41e1b-42cf-4342-ae44-6343d21f2196" -->
## Rules for AI Agents

1. **When creating folders**: Choose the correct suffix based on contents
2. **When navigating `_hierarchy`**: Select only the relevant branch for current context
3. **When documenting**: Explain the branching factor if creating a hierarchy

<!-- section_id: "54d87b52-b0d9-419b-807d-180542d5711c" -->
## Full Documentation

- Detailed `_hierarchy` documentation: `sub_layer_0_01_knowledge_system/naming_conventions/HIERARCHY_NAMING_CONVENTION.md`

---

*Universal rules for folder naming suffixes*
