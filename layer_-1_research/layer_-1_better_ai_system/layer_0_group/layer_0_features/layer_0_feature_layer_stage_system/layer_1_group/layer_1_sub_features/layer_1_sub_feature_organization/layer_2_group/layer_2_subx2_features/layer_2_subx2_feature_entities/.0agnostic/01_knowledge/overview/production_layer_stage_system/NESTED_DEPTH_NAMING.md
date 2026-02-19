# Nested Depth Naming Convention (subxN)

## Overview

When sub-layers contain nested sub-layers, we use a **depth indicator** in the naming:
- `sub_layer_` = Depth 1 (direct child of layer)
- `subx2_layer_` = Depth 2 (sub-layer within a sub-layer)
- `subx3_layer_` = Depth 3 (sub-layer within subx2)
- `subxN_layer_` = Depth N (generalized pattern)

---

## Why Depth Naming Matters

### Problem Without Depth Indicators

```
sub_layer_0_05_operating_systems/
└── sub_layer_0_06_environments/        # Is this depth 1 or 2?
    └── sub_layer_0_07_coding_apps/     # Confusing!
```

### Solution With Depth Indicators

```
sub_layer_0_05_operating_systems/
└── subx2_layer_0_06_environments/      # Clearly depth 2
    └── subx3_layer_0_07_coding_apps/   # Clearly depth 3
```

---

## Naming Pattern

```
sub[x{depth}]_layer_{layer_number}_{sequence}_{name}/
```

| Component | Meaning | Example |
|-----------|---------|---------|
| `sub` | Sub-layer prefix | sub |
| `x{depth}` | Depth indicator (omit for depth 1) | x2, x3, x4 |
| `layer_` | Layer marker | layer_ |
| `{layer_number}` | Parent layer number | 0, 1, 2, -1 |
| `{sequence}` | Ordering number | 01, 02, 05+ |
| `{name}` | Descriptive name | prompts, knowledge_system |

---

## Depth Examples

### Depth 1: `sub_layer_`

Direct children of a layer's `layer_N_03_sub_layers/` folder.

```
layer_0/
└── layer_0_group/
    └── layer_0_03_sub_layers/
        ├── sub_layer_0_01_prompts/              # Depth 1
        ├── sub_layer_0_02_knowledge_system/     # Depth 1
        ├── sub_layer_0_03_principles/           # Depth 1
        ├── sub_layer_0_04_rules/                # Depth 1
        └── sub_layer_0_05+_setup_dependant_hierarchy/  # Depth 1
```

### Depth 2: `subx2_layer_`

Children nested within a depth-1 sub-layer.

```
sub_layer_0_05+_setup_dependant_hierarchy/
└── sub_layer_0_05_operating_systems/
    ├── subx2_layer_0_05_linux_ubuntu/          # Depth 2
    ├── subx2_layer_0_05_macos/                 # Depth 2
    └── subx2_layer_0_05_windows/               # Depth 2
```

### Depth 3: `subx3_layer_`

Children nested within a depth-2 sub-layer.

```
subx2_layer_0_05_linux_ubuntu/
└── subx2_layer_0_06_environments/
    ├── subx3_layer_0_06_local/                 # Depth 3
    ├── subx3_layer_0_06_cloud/                 # Depth 3
    └── subx3_layer_0_06_container/             # Depth 3
```

### Depth 4+: `subx4_layer_`, `subx5_layer_`, etc.

Continue the pattern as needed.

```
subx3_layer_0_06_local/
└── subx3_layer_0_07_coding_apps/
    ├── subx4_layer_0_07_cursor/                # Depth 4
    ├── subx4_layer_0_07_vscode/                # Depth 4
    └── subx4_layer_0_07_vim/                   # Depth 4
```

---

## Complete Hierarchy Example

```
layer_0/
└── layer_0_group/
    └── layer_0_03_sub_layers/
        └── sub_layer_0_05+_setup_dependant_hierarchy/       # Depth 1
            └── sub_layer_0_05_operating_systems/
                ├── subx2_layer_0_05_linux_ubuntu/           # Depth 2
                │   └── subx2_layer_0_06_environments/
                │       ├── subx3_layer_0_06_local/          # Depth 3
                │       │   └── subx3_layer_0_07_coding_apps/
                │       │       ├── subx4_layer_0_07_cursor/ # Depth 4
                │       │       ├── subx4_layer_0_07_vscode/
                │       │       └── subx4_layer_0_07_vim/
                │       ├── subx3_layer_0_06_cloud/
                │       └── subx3_layer_0_06_container/
                ├── subx2_layer_0_05_macos/
                └── subx2_layer_0_05_windows/
```

---

## Context Flow for Nested Sub-Layers

Each depth level can be an entry point with its own context:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     NESTED SUB-LAYER CONTEXT CASCADE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  layer_0/CLAUDE.md                     (Universal)                          │
│       │                                                                     │
│       ▼                                                                     │
│  sub_layer_0_05+_setup_dependant_hierarchy/CLAUDE.md    (Depth 1)          │
│       │                                                                     │
│       ▼                                                                     │
│  subx2_layer_0_05_linux_ubuntu/CLAUDE.md               (Depth 2)           │
│       │                                                                     │
│       ▼                                                                     │
│  subx3_layer_0_06_local/CLAUDE.md                      (Depth 3)           │
│       │                                                                     │
│       ▼                                                                     │
│  subx4_layer_0_07_cursor/CLAUDE.md                     (Depth 4)           │
│       │                                                                     │
│       │ points to                                                           │
│       ▼                                                                     │
│  subx4_layer_0_07_cursor/.claude/       (tool config)                      │
│  subx4_layer_0_07_cursor/.0agnostic/    (sync source)                      │
│                                                                             │
│  CRITICAL RULES INHERITED:                                                  │
│  - All layer_0 rules                                                        │
│  - All sub_layer_0_05+ rules (setup hierarchy rules)                       │
│  - All subx2_layer_0_05_linux rules (Linux-specific)                       │
│  - All subx3_layer_0_06_local rules (local environment)                    │
│  - subx4_layer_0_07_cursor rules (Cursor-specific)                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## When to Use Depth Naming

### Use subxN_ When:

1. **Inside a `_hierarchy` folder**
   - Hierarchies branch into multiple paths
   - Depth indicates how far down the branch

2. **Clear parent-child relationship**
   - Child depends on parent's context
   - Child inherits parent's rules

3. **More than one level of nesting**
   - Single nesting can use regular `sub_layer_`
   - Multiple nesting needs depth indicators

### Don't Use subxN_ When:

1. **Flat structure**
   - All sub-layers at same level
   - No nesting relationship

2. **Independent sub-layers**
   - Sub-layers don't contain other sub-layers
   - Each stands alone

---

## Critical Rules at Each Depth

Each depth level can add its own critical rules:

```
layer_0/CLAUDE.md
├── CRITICAL: "Always cite sources"
│
└── sub_layer_0_05+_setup_dependant_hierarchy/CLAUDE.md
    ├── INHERITS: layer_0 rules
    ├── ADDS: "Navigate only your relevant branch"
    │
    └── subx2_layer_0_05_linux_ubuntu/CLAUDE.md
        ├── INHERITS: layer_0 + depth-1 rules
        ├── ADDS: "Use Linux commands only"
        │
        └── subx3_layer_0_06_local/CLAUDE.md
            ├── INHERITS: layer_0 + depth-1 + depth-2 rules
            ├── ADDS: "Check local paths exist"
            │
            └── subx4_layer_0_07_cursor/CLAUDE.md
                ├── INHERITS: ALL parent rules
                └── ADDS: "Use Cursor-specific keybindings"
```

---

## Generalized Pattern: subxN_

For any depth N:

```
subx{N}_layer_{layer_num}_{seq}_{name}/
```

| Depth | Prefix | Example |
|-------|--------|---------|
| 1 | `sub_layer_` | `sub_layer_0_05_os/` |
| 2 | `subx2_layer_` | `subx2_layer_0_05_linux/` |
| 3 | `subx3_layer_` | `subx3_layer_0_06_local/` |
| 4 | `subx4_layer_` | `subx4_layer_0_07_cursor/` |
| 5 | `subx5_layer_` | `subx5_layer_0_08_plugins/` |
| N | `subx{N}_layer_` | `subx{N}_layer_0_XX_name/` |

---

## AI Agent Navigation

When an agent encounters nested sub-layers:

```
1. Identify current depth from prefix
2. Load context cascade from layer_0 down to current depth
3. Follow ONLY the relevant branch (don't load all siblings)
4. Accumulate critical rules from each level
5. Apply most specific rules from current depth
```

### Example Navigation

```
Agent is in: subx4_layer_0_07_cursor/

Context loaded:
1. layer_0/CLAUDE.md                              ← Universal
2. sub_layer_0_05+_setup_dependant_hierarchy/CLAUDE.md  ← Depth 1
3. subx2_layer_0_05_linux_ubuntu/CLAUDE.md        ← Depth 2
4. subx3_layer_0_06_local/CLAUDE.md               ← Depth 3
5. subx4_layer_0_07_cursor/CLAUDE.md              ← Depth 4 (current)

NOT loaded:
- subx2_layer_0_05_macos/ (different branch)
- subx3_layer_0_06_cloud/ (different branch)
- subx4_layer_0_07_vscode/ (sibling, not current)
```

---

## Self-Check for Nested Navigation

- [ ] Did I identify the depth from the prefix?
- [ ] Did I load context from all parent depths?
- [ ] Am I only in ONE branch (not loading siblings)?
- [ ] Did I accumulate critical rules from each level?
- [ ] Am I applying the most specific rules?

---

*See SUB_LAYERS_AS_ENTRY_POINTS.md for sub-layer context architecture*
*See SUB_STAGES_EXPLAINED.md for sub_stages within stages*
