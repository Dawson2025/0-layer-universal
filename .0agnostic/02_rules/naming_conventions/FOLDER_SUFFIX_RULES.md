---
resource_id: "8caf5ad8-a7a4-4744-a460-dd53521dc562"
resource_type: "rule"
resource_name: "FOLDER_SUFFIX_RULES"
---
# Folder Suffix Rules

## Mandatory Suffixes

These suffixes have specific meanings and MUST be used correctly:

### `_group` - Child Content Container

**Use when**: A folder contains direct children (content, files, subfolders)

**Pattern**: `layer_N_group/`, `sub_layer_N_XX_group/`

**Example**:
```
layer_-1_group/           # Contains layer -1's internal content
sub_layer_0_05_group/     # Contains sub-layer 5's direct content
```

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

## Rules for AI Agents

1. **When creating folders**: Choose the correct suffix based on contents
2. **When navigating `_hierarchy`**: Select only the relevant branch for current context
3. **When documenting**: Explain the branching factor if creating a hierarchy

## Full Documentation

- Detailed `_hierarchy` documentation: `sub_layer_0_01_knowledge_system/naming_conventions/HIERARCHY_NAMING_CONVENTION.md`

---

*Universal rules for folder naming suffixes*
