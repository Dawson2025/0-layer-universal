---
resource_id: "9ab46661-f3e2-4d4e-8d69-96b8d4ab41c3"
resource_type: "knowledge"
resource_name: "HIERARCHY_NAMING_CONVENTION"
---
# Hierarchy Naming Convention (`_hierarchy` suffix)

<!-- section_id: "bd0b7c2d-e136-472b-8b0a-ab3a012655d6" -->
## Purpose

The `_hierarchy` suffix indicates that a folder contains **nested sub-layers that branch based on choices made at higher levels**. This is different from `_group` which simply contains child content.

<!-- section_id: "3eb3b50e-f685-471b-840e-147c1de02e11" -->
## Quick Reference

| Suffix | Meaning | Contains |
|--------|---------|----------|
| `_group` | Child content container | Direct children (files, folders) |
| `_hierarchy` | Branching sub-layer tree | Nested sub-layers that vary by parent choice |

<!-- section_id: "868d130c-9271-4787-9a86-3fea7253aa23" -->
## When to Use `_hierarchy`

Use `_hierarchy` when:
1. A sub-layer contains **multiple sub-layer children**
2. Those children **branch differently based on a choice/selection**
3. The structure forms a **tree where paths diverge**

<!-- section_id: "162e6a6a-48b7-49fe-aa54-18d0efcbbb19" -->
## Canonical Example: Setup-Dependent Hierarchy

```
sub_layer_0_05+_setup_dependant_hierarchy/
├── sub_layer_0_05_operating_systems/
│   ├── sub_layer_0_05_linux_ubuntu/
│   │   ├── sub_layer_0_06_environments/        ← Different for Linux
│   │   │   ├── sub_layer_0_06_local/
│   │   │   └── sub_layer_0_06_remote/
│   │   └── sub_layer_0_05_group/               ← Linux-specific content
│   ├── sub_layer_0_05_macos/
│   │   ├── sub_layer_0_06_environments/        ← Different for macOS
│   │   │   ├── sub_layer_0_06_local/
│   │   │   └── sub_layer_0_06_remote/
│   │   └── sub_layer_0_05_group/               ← macOS-specific content
│   └── sub_layer_0_05_windows/
│       ├── sub_layer_0_06_environments/        ← Different for Windows
│       │   ├── sub_layer_0_06_local/
│       │   └── sub_layer_0_06_wsl/             ← Windows-specific!
│       └── sub_layer_0_05_group/               ← Windows-specific content
```

<!-- section_id: "ea1db4ca-3f22-4770-a8e4-3a41a5e1f088" -->
### Why This is a Hierarchy

1. **Choice at Level 05**: Which operating system? (Linux, macOS, Windows)
2. **Different Level 06 for each**: Each OS has different environments
3. **Further branching**: Each environment has different apps, tools, configs

The sub_layer_06 content **depends on** which sub_layer_05 you chose. This branching structure is what makes it a hierarchy.

<!-- section_id: "fa3e0e2e-cab3-495f-a30c-77fb0ed3fc6d" -->
## Visual: Hierarchy vs Group

```
_group (flat children):              _hierarchy (branching tree):

folder_group/                        folder_hierarchy/
├── file1.md                         ├── choice_A/
├── file2.md                         │   ├── sub_layer_A1/
└── subfolder/                       │   └── sub_layer_A2/
                                     └── choice_B/
                                         ├── sub_layer_B1/  ← Different!
                                         └── sub_layer_B2/
```

<!-- section_id: "8f5d61ac-d375-4291-a6f8-79b35655c5b8" -->
## AI Agent Guidance

<!-- section_id: "257ee293-70eb-4519-aa4c-20843be7f244" -->
### When Navigating a `_hierarchy` Folder

1. **Identify the branching factor** - What choice determines the path?
2. **Select the relevant branch** - Based on current context (OS, environment, tool)
3. **Descend only the relevant path** - Don't load all branches

<!-- section_id: "077ebcee-4ad6-4319-a75c-509b2f22bd2b" -->
### Example Navigation

```
Context: Running on Linux Ubuntu, local environment, using Cursor

Path through hierarchy:
sub_layer_0_05+_setup_dependant_hierarchy/
  → sub_layer_0_05_operating_systems/
    → sub_layer_0_05_linux_ubuntu/        ← Selected by OS
      → sub_layer_0_06_environments/
        → sub_layer_0_06_local/           ← Selected by environment
          → sub_layer_0_07_coding_apps/
            → sub_layer_0_07_cursor/      ← Selected by tool
```

<!-- section_id: "fa83c631-7d1c-4c71-8780-ab05e3b29f59" -->
### When Creating a `_hierarchy` Folder

Ask yourself:
1. Will this folder contain sub-layers?
2. Do those sub-layers branch based on a selection/choice?
3. Will different choices lead to different nested content?

If yes to all → use `_hierarchy` suffix.

<!-- section_id: "248545ab-b951-448e-8da6-d0be630b3253" -->
## Common Hierarchy Patterns

| Hierarchy Root | Branching Factor | Example Branches |
|----------------|------------------|------------------|
| `setup_dependant_hierarchy` | Operating System | linux, macos, windows |
| `environments_hierarchy` | Deployment Target | local, staging, production |
| `tools_hierarchy` | Tool/App Choice | cursor, vscode, vim |
| `models_hierarchy` | AI Model | claude-4, gpt-4, gemini |

<!-- section_id: "997d0cf6-2300-4f3c-810c-acd252b4c30b" -->
## Relationship to Layer-Stage System

Hierarchies exist **within** sub-layers, not as a replacement:

```
layer_0/
├── layer_0_03_sub_layers/           ← Standard sub-layer container
│   ├── sub_layer_0_01_prompts/      ← Regular sub-layer
│   ├── sub_layer_0_02_knowledge/    ← Regular sub-layer
│   ├── sub_layer_0_03_principles/   ← Regular sub-layer
│   ├── sub_layer_0_04_rules/        ← Regular sub-layer
│   └── sub_layer_0_05+_setup_dependant_hierarchy/  ← HIERARCHY
│       └── (branching tree inside)
```

The `05+` indicates "sub-layer 5 and beyond" - the hierarchy contains sub-layers 05, 06, 07, etc. nested by choice.

---

*Documentation for AI agents on hierarchy naming convention*
