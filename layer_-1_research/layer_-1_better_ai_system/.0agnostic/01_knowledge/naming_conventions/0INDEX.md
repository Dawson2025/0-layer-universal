# Naming Conventions Knowledge

## Inherited from Universal Layer

These naming conventions are defined in the universal layer_0 and apply here:

| Convention | Documentation |
|------------|---------------|
| `_group` suffix | `layer_0/sub_layer_0_02_knowledge_system/naming_conventions/` |
| `_hierarchy` suffix | [HIERARCHY_NAMING_CONVENTION.md](../../../../../layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge_system/naming_conventions/HIERARCHY_NAMING_CONVENTION.md) |

## Quick Reference

| Suffix | Meaning | Example |
|--------|---------|---------|
| `_group` | Contains child content | `layer_-1_group/` |
| `_hierarchy` | Contains branching sub-layers | `sub_layer_-1_05+_setup_dependant_hierarchy/` |

## Research-Specific Notes

In this research project (`better_ai_system`), the hierarchy convention is used in:

```
layer_-1_group/layer_-1_03_sub_layers/sub_layer_-1_05+_setup_dependant_hierarchy/
└── sub_layer_-1_05_operating_systems/
    ├── sub_layer_-1_05_linux_ubuntu/    → has its own sub_layer_-1_06_*
    ├── sub_layer_-1_05_macos/           → has its own sub_layer_-1_06_*
    └── sub_layer_-1_05_windows/         → has its own sub_layer_-1_06_*
```

Each OS choice leads to different downstream sub-layers.

---

*See universal documentation for full details*
