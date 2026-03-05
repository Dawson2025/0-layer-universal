---
resource_id: "a74d24a5-760c-4d5d-8ef9-d9edda2f42d3"
resource_type: "knowledge"
resource_name: "ENTITY_TYPES"
---
# Entity Types

<!-- section_id: "d335d711-dac8-4f36-af62-9beaa2dfca28" -->
## What is an Entity?

An entity is any managed unit in the layer-stage system: projects, features, components, stages, sub-layers, etc.

<!-- section_id: "68ca19c6-e500-4b27-b419-fcf1dd65ed7c" -->
## Entity Types

<!-- section_id: "e3dbe976-a569-4bff-b6b0-9168585f96c6" -->
### 1. Projects (layer_1)

**Purpose**: A complete application, system, or body of work

**Structure**:
```
layer_1_project_<name>/
├── 0AGNOSTIC.md              # Identity
├── 0INDEX.md                 # Contents index
├── CLAUDE.md                 # Generated tool file
├── .0agnostic/               # AI config
├── layer_1_group/            # Internals
│   ├── layer_1_00_layer_registry/
│   ├── layer_1_03_sub_layers/
│   └── layer_1_99_stages/
└── layer_2_group/            # Children (features)
    ├── layer_2_00_layer_registry/
    └── layer_2_features/
```

<!-- section_id: "b3ead950-e5c0-4f07-a060-4dca76ed9c83" -->
### 2. Features (layer_2+)

**Purpose**: A distinct capability within a project

**Structure**:
```
layer_2_feature_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── CLAUDE.md
├── .0agnostic/
├── layer_2_group/            # Feature internals
│   ├── layer_2_03_sub_layers/
│   └── layer_2_99_stages/
└── layer_3_group/            # Children (components)
    └── layer_3_components/
```

<!-- section_id: "d9428bab-dd96-43d4-ae08-0fb00a500ee5" -->
### 3. Research Projects (layer_-1)

**Purpose**: Experimental, exploratory work

**Structure**:
```
layer_-1_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── CLAUDE.md
├── .0agnostic/
├── layer_-1_group/           # Research internals
│   ├── layer_-1_00_layer_registry/
│   │   └── proposals/        # Research proposals
│   ├── layer_-1_03_sub_layers/
│   └── layer_-1_99_stages/
└── layer_0_group/            # Research features
    └── layer_0_features/
```

<!-- section_id: "37d561bc-6fac-49b3-8224-bbbfebc8c593" -->
### 4. Stages

**Purpose**: Workflow phase container

**Structure**:
```
stage_N_XX_<name>/
├── 0AGNOSTIC.md              # Optional
├── CLAUDE.md                 # Optional
├── outputs/                  # Work products
│   ├── by_topic/
│   ├── by_need/
│   └── episodic/
└── hand_off_documents/       # Communication
    ├── incoming/
    └── outgoing/
```

<!-- section_id: "8a607e0a-c90a-45f0-93fd-f652fbab6a58" -->
### 5. Sub-Layers

**Purpose**: Content type container

**Structure**:
```
sub_layer_N_XX_<name>/
├── 0INDEX.md                 # Contents index
└── <content>/                # Type-specific content
```

<!-- section_id: "17a3a2a4-e1fa-4ef7-9f5c-440934a0a7e1" -->
### 6. Proposals

**Purpose**: Formal change proposals with staging

**Structure**:
```
proposals/
├── 0INDEX.md
├── active/                   # Production proposals
├── staging/                  # Under testing
│   ├── stage_experimental/   # Each has 01-11 stages
│   ├── stage_testing/
│   └── stage_rollout/
└── archived/                 # Historical
```

<!-- section_id: "5f3f54d6-59c6-4ea2-979a-540eb351aaa2" -->
## Entity File Requirements

<!-- section_id: "f1f5025d-8c50-48ac-a881-ee59a5ecb935" -->
### Required Files

| File | Purpose | Required For |
|------|---------|--------------|
| `0AGNOSTIC.md` | Identity, triggers, pointers | All entities |
| `0INDEX.md` | Contents listing | Containers |
| `CLAUDE.md` | Claude Code context | Projects, features |

<!-- section_id: "9799efab-5719-48e3-8ec1-c321f57a61ba" -->
### Optional Files

| File | Purpose | When to Include |
|------|---------|-----------------|
| `.cursorrules` | Cursor context | When using Cursor |
| `GEMINI.md` | Gemini context | When using Gemini |
| `AGENTS.md` | Codex/agents context | When using Codex |

<!-- section_id: "122358ac-1ba1-48fc-9e10-bc0909ecf948" -->
## Entity Nesting Rules

1. **Projects contain features**: `layer_1` → `layer_2`
2. **Features contain components**: `layer_2` → `layer_3`
3. **Research uses layer_0 for features**: `layer_-1` → `layer_0`
4. **Sub-layers don't nest** (except `_hierarchy`)
5. **Stages don't nest**

---

*See INSTANTIATION_GUIDE.md for how to create entities*
