---
resource_id: "2373ac3b-e498-4cbb-a6e5-c6887564d30b"
resource_type: "rule"
resource_name: "context_scope_boundaries"
---
# Context Scope Boundaries

**Purpose**: Define what context applies where and how scope is determined.

---

<!-- section_id: "a3cb3826-1ac2-4568-8bde-6c1327081b33" -->
## Core Concept: Scope

Context has **scope** - it applies to certain locations and not others.

```
layer_0 context → applies to EVERYTHING (universal)
layer_1 context → applies to that project only
layer_2 context → applies to that feature only
```

---

<!-- section_id: "8b2b4bf4-4532-4541-9a22-38b338c6bf7f" -->
## Scope Inheritance

<!-- section_id: "19c0321c-eaf1-43d2-9f9b-d99019dfc93b" -->
### Downward Inheritance

Context flows DOWN the hierarchy:

```
layer_0 (applies to all)
    │
    ├─── layer_1/project_a/ (inherits layer_0)
    │         │
    │         └─── feature_x/ (inherits layer_0 + project_a)
    │
    └─── layer_1/project_b/ (inherits layer_0, NOT project_a)
```

<!-- section_id: "66370eb2-9d9c-46eb-bfb6-042a2b0ff050" -->
### No Sibling Inheritance

Context does NOT flow between siblings:

```
layer_1/project_a/     layer_1/project_b/
        │                      │
        │    (NO sharing)      │
        ├──────────────────────┤
        ▼                      ▼
(has its own context)   (has its own context)
```

project_a's context does NOT apply to project_b.

---

<!-- section_id: "5814410f-da31-4d88-b72c-903a872225b1" -->
## Scope by Layer

<!-- section_id: "6a26b6da-0297-4b44-8cbe-c9bd666e3917" -->
### layer_0 (Universal Scope)

- **Applies to**: Everything in the system
- **Readable by**: All layers, all stages, all sub_layers
- **Examples**: Universal rules, shared protocols, common knowledge

```
layer_0/
├── sub_layer_0_02_rules/       ← Applies everywhere
├── sub_layer_0_05_protocols/   ← Applies everywhere
└── sub_layer_0_02_knowledge/   ← Available everywhere
```

<!-- section_id: "b8d43423-42a3-4828-a5c3-145ec8b380fa" -->
### layer_1 (Project Scope)

- **Applies to**: That project and its children
- **Readable by**: That project's descendants only
- **NOT readable by**: Other layer_1 projects, layer_0

```
layer_1/
├── project_a/                  ← Scope: project_a only
│   ├── feature_x/              ← Can read project_a context
│   └── feature_y/              ← Can read project_a context
│
└── project_b/                  ← Scope: project_b only (separate)
    └── feature_z/              ← Can read project_b context, NOT project_a
```

<!-- section_id: "c8613fdf-5d84-4a95-9ded-99bc04726568" -->
### layer_-1 (Research Scope)

- **Applies to**: Research projects only
- **Inherits from**: layer_0
- **Experimental**: May test ideas before they go to layer_0

```
layer_-1_research/
├── research_project_1/         ← Experimental scope
└── research_project_2/         ← Separate experimental scope
```

---

<!-- section_id: "25eda1d1-dbbb-4017-b2ab-5e0bc40ff458" -->
## Scope Rules

<!-- section_id: "9b28dc6b-ea4b-474d-853e-da952e33ac6a" -->
### Rule 1: Parent Context Applies to Children

If you're in `layer_1/project_a/feature_x/`, these contexts apply:

1. layer_0 context (universal)
2. layer_1/project_a context (project)
3. layer_1/project_a/feature_x context (feature)

<!-- section_id: "b1d365d7-3815-4951-a1af-229e9284ffa2" -->
### Rule 2: Sibling Context is Invisible

If you're in `layer_1/project_a/`, you CANNOT see:

- layer_1/project_b/ context
- layer_1/project_c/ context
- Any other sibling's context

<!-- section_id: "e309209a-1e91-4461-b8dc-14d8ab90cd42" -->
### Rule 3: Child Context is Invisible to Parent

If you're in `layer_1/project_a/`, you cannot see:

- layer_1/project_a/feature_x/ context
- layer_1/project_a/feature_y/ context

(Parent doesn't know about child's specific context)

<!-- section_id: "9f4d3f30-01bf-4eb5-a04d-cbcf050285d5" -->
### Rule 4: Deeper Nesting = More Specific Scope

```
layer_0                          ← Broadest scope (everything)
layer_1/project                  ← Narrower (one project)
layer_1/project/feature          ← Narrower still (one feature)
layer_1/project/feature/sub      ← Most specific (one sub-feature)
```

---

<!-- section_id: "aaf14514-dc60-4386-a095-54f969c554c3" -->
## Context Visibility Matrix

| If you're in... | You can see context from... |
|-----------------|----------------------------|
| layer_0 | layer_0 only |
| layer_1/project_a | layer_0, layer_1/project_a |
| layer_1/project_a/feature_x | layer_0, layer_1/project_a, feature_x |
| layer_1/project_b | layer_0, layer_1/project_b (NOT project_a) |
| layer_-1_research/proj | layer_0, layer_-1_research/proj |

---

<!-- section_id: "8abe1020-97e2-4183-9fac-bc5d1b311c42" -->
## Scope Boundaries and Stages

Stages (01-11) are workflow phases, not scope boundaries.

All stages within a layer have the same scope:

```
layer_1/project_a/
├── stage_01_request_gathering/     ← Same scope as project_a
├── stage_02_research/              ← Same scope as project_a
├── stage_06_development/           ← Same scope as project_a
└── ...
```

---

<!-- section_id: "eddc85f9-963b-42a5-9a72-3ea744ca035d" -->
## Sub_layer Scope

Sub_layers are content types, and their scope matches their parent:

```
layer_0/sub_layer_0_02_rules/       ← Universal scope (from layer_0)
layer_1/project_a/sub_layer_1_02_knowledge/  ← Project scope (from layer_1/project_a)
```

---

<!-- section_id: "b9cf1f20-fd2d-4ec5-9187-ca179f812e1c" -->
## Determining Current Scope

To determine what context applies:

1. **Find current location** in filesystem
2. **Trace path back** to 0_layer_universal
3. **Collect CLAUDE.md files** along the path
4. **Each file's context applies** (in order, later overrides earlier)

Example:
```
/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/project_a/feature_x/

Scope includes:
1. 0_layer_universal/CLAUDE.md (layer_0)
2. 0_layer_universal/layer_0/**  (layer_0 content)
3. 0_layer_universal/layer_1/CLAUDE.md (if exists)
4. 0_layer_universal/layer_1/project_a/CLAUDE.md
5. 0_layer_universal/layer_1/project_a/feature_x/CLAUDE.md
```

---

<!-- section_id: "d9dcafe4-531c-4a7b-88de-d381e2be6439" -->
## Crossing Scope Boundaries

<!-- section_id: "0f443f8d-fcd1-4abd-8bd5-02ffd5b933c3" -->
### When Moving Between Projects

If you switch from `project_a` to `project_b`:

1. Unload project_a specific context
2. Keep layer_0 context (still applies)
3. Load project_b specific context

<!-- section_id: "70331570-fbdd-4b1c-8bbc-c4b2f81a414d" -->
### When Moving Up Layers

If you move from `layer_1/project_a` to `layer_0`:

1. Unload project_a specific context
2. Keep layer_0 context
3. Now in universal scope only

---

<!-- section_id: "f9d760dc-1a5d-4143-ab15-c9c247053365" -->
## Related Documentation

- `context_priority_rules.md` - How overrides work
- `context_loading_protocol.md` - How context is loaded
- `context_agents/` - Agent implementations
