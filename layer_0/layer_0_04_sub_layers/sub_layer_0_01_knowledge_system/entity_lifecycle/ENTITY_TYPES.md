# Entity Types

## What is an Entity?

An entity is any managed unit in the layer-stage system: projects, features, components, stages, sub-layers, etc. All entities follow the canonical structure defined in `@imports/entity_structure.md`.

## Entity Types

### 1. Projects (layer_1)

**Purpose**: A complete application, system, or body of work

**Structure** (see `@imports/entity_structure.md` for full canonical tree):
```
layer_1_project_<name>/
├── 0AGNOSTIC.md              # Identity
├── 0INDEX.md                 # Contents index
├── CLAUDE.md                 # Generated tool file
├── .0agnostic/               # AI config (agents, episodic, hooks, knowledge, rules, skills)
├── .1merge/                  # Tool overrides (6 tools x 3 tiers)
├── .claude/rules/            # Claude Code config
├── .cursor/rules/            # Cursor config
├── .github/instructions/     # GitHub config
├── layer_1_group/            # Internals
│   ├── layer_1_00_layer_registry/proposals/
│   ├── layer_1_01_ai_manager_system/
│   ├── layer_1_02_manager_handoff_documents/
│   │   ├── incoming/{from_above,from_below}
│   │   └── outgoing/{to_above,to_below}
│   ├── layer_1_03_sub_layers/
│   │   ├── sub_layer_1_02_knowledge_system/{overview,things_learned}
│   │   └── ... (prompts, principles, rules, setup)
│   └── layer_1_99_stages/
├── layer_2_group/            # Children (features)
│   ├── layer_2_00_layer_registry/proposals/
│   └── layer_2_features/
└── synthesis/
```

### 2. Features (layer_2+)

**Purpose**: A distinct capability within a project

**Structure**:
```
layer_2_feature_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── CLAUDE.md
├── .0agnostic/               # Full structure
├── .1merge/                  # 6 tools x 3 tiers
├── .claude/, .cursor/, .github/
├── layer_2_group/            # Feature internals
│   ├── layer_2_00_layer_registry/proposals/
│   ├── layer_2_01_ai_manager_system/
│   ├── layer_2_02_manager_handoff_documents/
│   ├── layer_2_03_sub_layers/ (with knowledge_system/{overview,things_learned})
│   └── layer_2_99_stages/
├── layer_3_group/            # Children (components)
│   └── layer_3_components/
└── synthesis/
```

### 3. Research Projects (layer_-1)

**Purpose**: Experimental, exploratory work

**Structure**:
```
layer_-1_<name>/
├── 0AGNOSTIC.md
├── 0INDEX.md
├── CLAUDE.md
├── .0agnostic/               # Full structure
├── .1merge/                  # 6 tools x 3 tiers
├── .claude/, .cursor/, .github/
├── layer_-1_group/           # Research internals
│   ├── layer_-1_00_layer_registry/proposals/
│   ├── layer_-1_01_ai_manager_system/
│   ├── layer_-1_02_manager_handoff_documents/
│   ├── layer_-1_03_sub_layers/
│   └── layer_-1_99_stages/
├── layer_0_group/            # Research features
│   └── layer_0_features/
└── synthesis/
```

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
│       ├── sessions/
│       └── changes/
└── hand_off_documents/       # Communication
    ├── incoming/{from_above,from_below}
    └── outgoing/{to_above,to_below}
```

### 5. Sub-Layers

**Purpose**: Content type container

**Structure**:
```
sub_layer_N_XX_<name>/
├── 0INDEX.md                 # Contents index
└── <content>/                # Type-specific content
```

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

## Entity File Requirements

### Required Files

| File | Purpose | Required For |
|------|---------|--------------|
| `0AGNOSTIC.md` | Identity, triggers, pointers | All entities |
| `0INDEX.md` | Contents listing | Containers |
| `CLAUDE.md` | Claude Code context (auto-generated) | Projects, features |

### Optional Files

| File | Purpose | When to Include |
|------|---------|-----------------|
| `.cursorrules` | Cursor context (auto-generated) | When using Cursor |
| `GEMINI.md` | Gemini context (auto-generated) | When using Gemini |
| `AGENTS.md` | Codex/agents context (auto-generated) | When using Codex |

## Entity Nesting Rules

1. **Projects contain features**: `layer_1` → `layer_2`
2. **Features contain components**: `layer_2` → `layer_3`
3. **Research uses layer_0 for features**: `layer_-1` → `layer_0`
4. **Sub-layers don't nest** (except `_hierarchy`)
5. **Stages don't nest**

---

*See `@imports/entity_structure.md` for the canonical directory structure.*
*See INSTANTIATION_GUIDE.md for how to create entities.*
