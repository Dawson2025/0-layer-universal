---
resource_id: "97156db8-e9a4-4ed1-ac37-9c037c8906b4"
resource_type: "knowledge"
resource_name: "LAYERS_EXPLAINED"
---
# Layers Explained

<!-- section_id: "f8f9a8af-9d42-40c0-87c3-b516c220f8db" -->
## What is a Layer?

A layer represents a **scope level** in the system hierarchy. Higher layers (lower numbers) are more universal; lower layers (higher numbers) are more specific.

<!-- section_id: "afe6c60e-032e-4243-8fee-612b59f4b9fb" -->
## Layer Numbers

| Layer | Name | Scope | Example |
|-------|------|-------|---------|
| 0 | Universal | Everything | Rules that apply to all projects |
| 1 | Project | One project | A specific application |
| 2 | Feature | One feature | Login system within an app |
| 3 | Component | One component | Password validator |
| 4+ | Sub-component | Nested components | Specific validation rule |
| -1 | Research | Experimental | Research projects |

<!-- section_id: "cc19a376-66ed-4a8f-a47b-27b85ec8a521" -->
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

<!-- section_id: "88f3d303-02be-43ef-a559-a9465615c658" -->
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

<!-- section_id: "37857ee3-6e18-41dd-b890-70eb9f903347" -->
## Layer Structure

**For the complete canonical entity structure**, see:
`.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`

That document is the **single source of truth** and includes full directory trees, mkdir templates, and complete file examples. This section provides the conceptual framework; the canonical reference provides the implementation details.

<!-- section_id: "8b925236-2c09-43c2-b55e-e30b0acd723a" -->
## The Two Group Folders

<!-- section_id: "18399dc2-ffd0-4351-b960-893980526958" -->
### `layer_N_group/` - Entity's Internal Structure (MINIMAL)

Contains ONLY this entity's own workflow:
- **layer_N_00_layer_registry/**: Proposals, registrations (metadata only)
- **layer_N_99_stages/**: Workflow stages (01-11)

**⚠️ CRITICAL**: Does NOT contain features, projects, or child-organizing containers. Those go in layer_N+1_group.

**Why minimal?** Entity-scoped AI resources (knowledge, rules, protocols) go in `.0agnostic/`, not in layer_N_group. This keeps layer_N_group focused and prevents confusion about where child entities belong.

<!-- section_id: "d132bc47-a29b-4722-836c-380076911e6d" -->
### `layer_N+1_group/` - Further Layering (CHILDREN CONTAINER)

Contains the next layer down and organizing containers for them:
- **layer_N+1_00_layer_registry/**: Registry of layer_N+1 organization
- **layer_N+1_01_features/**: Grouping container for feature entities
- **layer_N+1_02_projects/**: (optional) Grouping container for project entities
- **layer_N+1_03_components/**: (optional) Grouping container for component entities

**Key distinction**: `layer_N+1_group/` is not a layer itself — it's a container for organizing child layer entities. Child entities inside these containers are actual layers with their own `layer_N+1_group/` and stages.

<!-- section_id: "7c90ac07-7b56-48d5-b50a-227c78eb1248" -->
## Layer Inheritance Rules

<!-- section_id: "e64a572d-1428-4e8d-b56c-5fe70ebf7eaf" -->
### What Inherits

| Content | Inherits? | How |
|---------|-----------|-----|
| Rules | Yes | All ancestor rules apply |
| Knowledge | Reference | Load from parent on-demand |
| Principles | Yes | Ancestor principles guide decisions |
| Identity | No | Each entity has unique identity |
| Stages | No | Each entity has own workflow |

<!-- section_id: "8536e4f5-a0a8-4b60-abd2-d33ed5437d0c" -->
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

<!-- section_id: "b297212b-2180-47e9-a739-c757e16f7100" -->
## When to Create a New Layer

<!-- section_id: "a35add57-a2ec-48ec-961f-a391dab89226" -->
### Create layer_1 (Project) when:
- Starting a new application/system
- Work has distinct identity and lifecycle
- Will have its own features and components

<!-- section_id: "54d3a954-e708-4f49-9ecf-c71c710e2355" -->
### Create layer_2 (Feature) when:
- Adding distinct capability to a project
- Work could potentially be reused
- Has its own development cycle

<!-- section_id: "93b270be-c1be-491a-87d1-24854cb1509d" -->
### Create layer_3+ (Component) when:
- Feature has separable sub-parts
- Need further organization
- Component has distinct interface

<!-- section_id: "06c4d3c4-15ff-4d72-a9df-f3fa33fa6ee8" -->
### Create layer_-1 (Research) when:
- Exploring new ideas
- Work is experimental
- Not ready for production

<!-- section_id: "40e43954-d1e1-4ab1-853d-ffea98c08750" -->
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

<!-- section_id: "d7b32046-2538-4e27-b4f4-7d7574a1881a" -->
## Renumbering

When entities move to a different depth in the hierarchy, their layer numbers must be updated. Common triggers: re-parenting entities, promoting features to projects, or merging entity trees.

Use the renumbering tool to shift layer numbers across directories, filenames, and file contents in a single pass:

```bash
bash .0agnostic/01_knowledge/layer_stage_system/resources/tools/renumber-layers.sh \
  ./path/to/entity --shift 1 --dry-run
```

**Full guide**: `.0agnostic/01_knowledge/layer_stage_system/docs/RENUMBERING_GUIDE.md`

**Note**: `subxN_` prefixes track nesting depth, not layer number -- they are intentionally preserved during renumbering. See `NESTED_DEPTH_NAMING.md`.

<!-- section_id: "defe9a0c-17e9-46cb-a7e7-e6e6cbead905" -->
## Research vs Production (Context Chain Modes)

Any system can have two parallel versions of its context chain:

| Version | Purpose | Location Pattern |
|---------|---------|-----------------|
| **Research** | Experimental — for trying new patterns, features, designs | `layer_-1_research/layer_-1_better_<system>/` |
| **Production (Default)** | Tried-and-true — stable, validated, what agents use by default | `layer_0/` + `.0agnostic/` (for AI system), or `layer_1_project_<system>/` (for specific systems) |

<!-- section_id: "f3905b6b-4342-4681-8dd0-a9fd8c732e15" -->
### How It Works

1. **Research version**: Lives in `layer_-1_research/`. Features are developed through stages (01-11). Each feature has its own layers and stages for research, design, development, testing.
2. **Production version**: Lives in the production tree. Contains only proven, validated patterns.
3. **Promotion**: When research features pass testing, they're promoted to production via the research promotion protocol.
4. **Mode switching**: Agents default to production context. Users can say "use research context chain" to additionally load research knowledge. See `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/`.

<!-- section_id: "bafc119a-1d8d-4bf4-ae2b-9261c238ebc6" -->
### Current Example: AI System

- **Research**: `layer_-1_research/layer_-1_better_ai_system/` (agent delegation, memory, context chains)
- **Production**: `layer_0/` + `.0agnostic/` (entity structure, tools, protocols, rules)
- **Promotion protocol**: `.0agnostic/03_protocols/research_promotion_protocol.md`
- **Knowledge index**: `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`

---

*See STAGES_EXPLAINED.md for workflow stages*
*See SUB_LAYERS_EXPLAINED.md for content organization*
