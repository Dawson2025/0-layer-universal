# Layers Explained

## What is a Layer?

A layer represents a **scope level** in the system hierarchy. Higher layers (lower numbers) are more universal; lower layers (higher numbers) are more specific.

## Layer Numbers

| Layer | Name | Scope | Example |
|-------|------|-------|---------|
| 0 | Universal | Everything | Rules that apply to all projects |
| 1 | Project | One project | A specific application |
| 2 | Feature | One feature | Login system within an app |
| 3 | Component | One component | Password validator |
| 4+ | Sub-component | Nested components | Specific validation rule |
| -1 | Research | Experimental | Research projects |

## Layer Relationships

```
layer_0 (Universal)
│
├── Applies to: EVERYTHING
├── Contains: Rules, knowledge, principles that govern all work
│
└─── layer_1 (Projects)
     │
     ├── Inherits from: layer_0
     ├── Contains: Project-specific configuration
     │
     └─── layer_2 (Features)
          │
          ├── Inherits from: layer_0 + layer_1
          ├── Contains: Feature-specific work
          │
          └─── layer_3+ (Components)
               │
               └── Nested as needed
```

## Special Layer: -1 (Research)

Research projects use negative layer numbers:
- **layer_-1**: Research project root
- Uses **layer_0** for features (not layer_2)
- Has "research-only" scope - doesn't implement in production

```
layer_-1_research/
└── layer_-1_better_ai_system/     # Research entity
    ├── layer_-1_group/         # Entity's internal (stages for research)
    │   └── layer_-1_99_stages/
    └── layer_0_group/          # Further layering container (for layer_0 child entities)
        ├── layer_0_00_layer_registry/
        ├── layer_0_01_features/    # Grouping container for layer_0 feature research
        │   └── layer_0_feature_one/
```

## Layer Structure

Every layer entity has the same basic structure:

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md              # Identity
├── 0INDEX.md                 # Contents
├── CLAUDE.md                 # Tool context
├── .0agnostic/               # AI config (01_knowledge, 02_rules, 03_protocols, etc.)
├── layer_N_group/            # THIS layer's internal structure (MINIMAL)
│   ├── layer_N_00_layer_registry/     # Registry only
│   └── layer_N_99_stages/             # Workflow stages only
└── layer_N+1_group/          # Further layering (CHILDREN container)
    ├── layer_N+1_00_layer_registry/
    ├── layer_N+1_01_features/         # Grouping container for features
    ├── layer_N+1_02_projects/         # (optional)
    └── layer_N+1_03_components/       # (optional)
```

## The Two Group Folders

### `layer_N_group/` - Entity's Internal Structure (MINIMAL)

Contains ONLY this entity's own workflow:
- **layer_N_00_layer_registry/**: Proposals, registrations (metadata only)
- **layer_N_99_stages/**: Workflow stages (01-11)

**⚠️ CRITICAL**: Does NOT contain features, projects, or child-organizing containers. Those go in layer_N+1_group.

**Why minimal?** Entity-scoped AI resources (knowledge, rules, protocols) go in `.0agnostic/`, not in layer_N_group. This keeps layer_N_group focused and prevents confusion about where child entities belong.

### `layer_N+1_group/` - Further Layering (CHILDREN CONTAINER)

Contains the next layer down and organizing containers for them:
- **layer_N+1_00_layer_registry/**: Registry of layer_N+1 organization
- **layer_N+1_01_features/**: Grouping container for feature entities
- **layer_N+1_02_projects/**: (optional) Grouping container for project entities
- **layer_N+1_03_components/**: (optional) Grouping container for component entities

**Key distinction**: `layer_N+1_group/` is not a layer itself — it's a container for organizing child layer entities. Child entities inside these containers are actual layers with their own `layer_N+1_group/` and stages.

## Layer Inheritance Rules

### What Inherits

| Content | Inherits? | How |
|---------|-----------|-----|
| Rules | Yes | All ancestor rules apply |
| Knowledge | Reference | Load from parent on-demand |
| Principles | Yes | Ancestor principles guide decisions |
| Identity | No | Each entity has unique identity |
| Stages | No | Each entity has own workflow |

### Inheritance Example

```
layer_0 rules:
  - "Always cite sources"
  - "Use markdown formatting"

layer_1 (project) inherits:
  - "Always cite sources" ← From layer_0
  - "Use markdown formatting" ← From layer_0
  - "Follow REST conventions" ← Added by project

layer_2 (feature) inherits:
  - "Always cite sources" ← From layer_0
  - "Use markdown formatting" ← From layer_0
  - "Follow REST conventions" ← From layer_1
  - "Validate all inputs" ← Added by feature
```

## When to Create a New Layer

### Create layer_1 (Project) when:
- Starting a new application/system
- Work has distinct identity and lifecycle
- Will have its own features and components

### Create layer_2 (Feature) when:
- Adding distinct capability to a project
- Work could potentially be reused
- Has its own development cycle

### Create layer_3+ (Component) when:
- Feature has separable sub-parts
- Need further organization
- Component has distinct interface

### Create layer_-1 (Research) when:
- Exploring new ideas
- Work is experimental
- Not ready for production

## Layer Naming Convention

```
layer_N_<type>_<name>/
```

| Part | Meaning | Example |
|------|---------|---------|
| layer_N | Layer number | layer_1, layer_2, layer_-1 |
| <type> | Entity type | project, feature, component |
| <name> | Entity name | my_app, auth_system |

**Examples**:
- `layer_1_project_website/`
- `layer_2_feature_user_auth/`
- `layer_3_component_password_validator/`
- `layer_-1_research_new_framework/`

## Renumbering

When entities move to a different depth in the hierarchy, their layer numbers must be updated. Common triggers: re-parenting entities, promoting features to projects, or merging entity trees.

Use the renumbering tool to shift layer numbers across directories, filenames, and file contents in a single pass:

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --shift 1 --dry-run
```

**Full guide**: `.0agnostic/01_knowledge/layer_stage_system/docs/RENUMBERING_GUIDE.md`

**Note**: `subxN_` prefixes track nesting depth, not layer number -- they are intentionally preserved during renumbering. See `NESTED_DEPTH_NAMING.md`.

## Research vs Production (Context Chain Modes)

Any system can have two parallel versions of its context chain:

| Version | Purpose | Location Pattern |
|---------|---------|-----------------|
| **Research** | Experimental — for trying new patterns, features, designs | `layer_-1_research/layer_-1_better_<system>/` |
| **Production (Default)** | Tried-and-true — stable, validated, what agents use by default | `layer_0/` + `.0agnostic/` (for AI system), or `layer_1_project_<system>/` (for specific systems) |

### How It Works

1. **Research version**: Lives in `layer_-1_research/`. Features are developed through stages (01-11). Each feature has its own layers and stages for research, design, development, testing.
2. **Production version**: Lives in the production tree. Contains only proven, validated patterns.
3. **Promotion**: When research features pass testing, they're promoted to production via the research promotion protocol.
4. **Mode switching**: Agents default to production context. Users can say "use research context chain" to additionally load research knowledge. See `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/`.

### Current Example: AI System

- **Research**: `layer_-1_research/layer_-1_better_ai_system/` (agent delegation, memory, context chains)
- **Production**: `layer_0/` + `.0agnostic/` (entity structure, tools, protocols, rules)
- **Promotion protocol**: `.0agnostic/03_protocols/research_promotion_protocol.md`
- **Knowledge index**: `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`

---

*See STAGES_EXPLAINED.md for workflow stages*
*See SUB_LAYERS_EXPLAINED.md for content organization*
