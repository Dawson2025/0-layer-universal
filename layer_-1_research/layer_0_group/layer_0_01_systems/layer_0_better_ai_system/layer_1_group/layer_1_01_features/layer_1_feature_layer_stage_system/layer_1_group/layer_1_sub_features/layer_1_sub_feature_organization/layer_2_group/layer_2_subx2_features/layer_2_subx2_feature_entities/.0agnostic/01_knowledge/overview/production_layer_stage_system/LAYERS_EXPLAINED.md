---
resource_id: "53d4c941-456e-444d-ae8c-cd28d6d94b74"
resource_type: "knowledge"
resource_name: "LAYERS_EXPLAINED"
---
# Layers Explained — CANONICAL SOURCE POINTER

This file has been replaced with a pointer to the canonical source.

**[READ CANONICAL LAYERS_EXPLAINED.md](../../../../../../../../../../../../../../../.0agnostic/01_knowledge/layer_stage_system/LAYERS_EXPLAINED.md)**

---

All layer definitions, numbering, hierarchy rules, and naming conventions are maintained in a single location to prevent inconsistency.

This pointer file directs you to the current production definition.

<!-- section_id: "10094ccf-4a0b-4697-8aad-f1f3588033d8" -->
## What is a Layer?

A layer represents a **scope level** in the system hierarchy. Higher layers (lower numbers) are more universal; lower layers (higher numbers) are more specific.

<!-- section_id: "bfdf00dc-f237-4c53-ad73-1c3e6d4789b5" -->
## Layer Numbers

| Layer | Name | Scope | Example |
|-------|------|-------|---------|
| 0 | Universal | Everything | Rules that apply to all projects |
| 1 | Project | One project | A specific application |
| 2 | Feature | One feature | Login system within an app |
| 3 | Component | One component | Password validator |
| 4+ | Sub-component | Nested components | Specific validation rule |
| -1 | Research | Experimental | Research projects |

<!-- section_id: "2b689c2c-d46b-455d-ad31-81fbc656d420" -->
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

<!-- section_id: "7b4cb702-5cca-48b2-806b-be52c6e6b466" -->
## Special Layer: -1 (Research)

Research projects use negative layer numbers:
- **layer_-1**: Research project root
- Uses **layer_0** for features (not layer_2)
- Has "research-only" scope - doesn't implement in production

```
layer_-1_research/
└── layer_-1_better_ai_system/
    ├── layer_-1_group/        # Research internals
    └── layer_0_group/         # Research features (not layer_2!)
        └── layer_0_features/
```

<!-- section_id: "49b9e017-c47a-408b-95e5-30547695e712" -->
## Layer Structure

Every layer entity has the same basic structure:

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md              # Identity
├── 0INDEX.md                 # Contents
├── CLAUDE.md                 # Tool context
├── .0agnostic/               # AI config
├── layer_N_group/            # THIS layer's internal content
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_03_sub_layers/
│   └── layer_N_99_stages/
└── layer_N+1_group/          # CHILDREN (next layer down)
    └── layer_N+1_<type>s/
```

<!-- section_id: "089b0cb5-ab2d-4d11-a2ab-3d9666ec0b11" -->
## The Two Group Folders

<!-- section_id: "d9d4b877-2271-4c42-bc0a-2cf57236ee9a" -->
### `layer_N_group/` - Internal Content

Contains this entity's own stuff:
- **00_layer_registry**: Proposals, registrations
- **03_sub_layers**: Knowledge, rules, prompts, setup-dependent
- **99_stages**: Workflow stages (01-11)

<!-- section_id: "95cb386b-f81f-4acf-93c0-f78392f89ec2" -->
### `layer_N+1_group/` - Children

Contains the next layer down:
- **layer_N+1_features/**: For projects holding features
- **layer_N+1_components/**: For features holding components
- **layer_N+1_<type>s/**: Whatever the children are

<!-- section_id: "b90f8536-c691-4d67-832b-56827f7bdc27" -->
## Layer Inheritance Rules

<!-- section_id: "95cb69f7-3fc8-4ace-9e5a-870184a146e4" -->
### What Inherits

| Content | Inherits? | How |
|---------|-----------|-----|
| Rules | Yes | All ancestor rules apply |
| Knowledge | Reference | Load from parent on-demand |
| Principles | Yes | Ancestor principles guide decisions |
| Identity | No | Each entity has unique identity |
| Stages | No | Each entity has own workflow |

<!-- section_id: "416a0222-a7f6-4714-80fc-5aa92c6f0a49" -->
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

<!-- section_id: "cf879f69-6c7c-4f26-b4b4-a86f93633c73" -->
## When to Create a New Layer

<!-- section_id: "1eb49ab1-b2d8-402b-9c04-e4e500128e0b" -->
### Create layer_1 (Project) when:
- Starting a new application/system
- Work has distinct identity and lifecycle
- Will have its own features and components

<!-- section_id: "1a5789d5-4e84-454c-884b-492e69e17b8a" -->
### Create layer_2 (Feature) when:
- Adding distinct capability to a project
- Work could potentially be reused
- Has its own development cycle

<!-- section_id: "48c66f8f-a000-4b19-9c7a-c1c1d717fc4b" -->
### Create layer_3+ (Component) when:
- Feature has separable sub-parts
- Need further organization
- Component has distinct interface

<!-- section_id: "404ea986-bb98-4aa5-84d7-a35151122478" -->
### Create layer_-1 (Research) when:
- Exploring new ideas
- Work is experimental
- Not ready for production

<!-- section_id: "955aa2b3-34a4-40ba-b763-4e8c6e81a848" -->
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

---

*See STAGES_EXPLAINED.md for workflow stages*
*See SUB_LAYERS_EXPLAINED.md for content organization*
