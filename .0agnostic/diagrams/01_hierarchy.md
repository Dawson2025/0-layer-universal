---
resource_id: "7d64fe6a-602c-4962-91a4-42afe632229a"
resource_type: "document"
resource_name: "01_hierarchy"
---
# System Architecture - Hierarchy Visualization

<!-- section_id: "1b7a6b61-700f-4720-8e52-0f07bdd0aa0a" -->
## Layer Hierarchy (Layer 0 → Layer 4)

```mermaid
graph TD
    L0["🔷 Layer 0: Universal<br/>0_layer_universal<br/>(Coordinates all layers)"]
    L1["🟦 Layer 1: Projects<br/>layer_1_project_school<br/>(School project)"]
    L2["🟩 Layer 2: Sub-Projects<br/>layer_2_sub_project_classes<br/>(Classes + Grade Strategy)"]
    L3["🟨 Layer 3: Sub²-Projects<br/>layer_3_subx2_project_computer_science<br/>(CS curriculum)"]
    L4["🟪 Layer 4: Courses<br/>layer_4_subx3_project_machine_learning<br/>(ML algorithms)"]
    L5A["🟥 Layer 5a: Assignments<br/>layer_5_feature_assignments"]
    L5B["🟧 Layer 5b: Modules<br/>layer_5_feature_module_content"]

    L0 -->|parent| L1
    L1 -->|parent| L2
    L2 -->|parent| L3
    L3 -->|parent| L4
    L4 -->|contains| L5A
    L4 -->|contains| L5B

    style L0 fill:#e1f5ff
    style L1 fill:#e8f5e9
    style L2 fill:#fffde7
    style L3 fill:#e0f2f1
    style L4 fill:#f3e5f5
    style L5A fill:#ffebee
    style L5B fill:#ffe0b2
```

<!-- section_id: "a2bcabeb-8b1b-4191-b32a-1e227c9387d7" -->
## Resource Inheritance

```mermaid
graph LR
    UNI["Universal<br/>(layer_0)"]
    RULES["Rules & Protocols<br/>(.0agnostic/)"]
    GRADE["Grade Strategy<br/>(5 trajectories)"]
    MODULE["Module Content<br/>(4 trajectories)"]
    SKILLS["Shared Skills<br/>(canvas-fetch,<br/>grade-calculator,<br/>layer-populator)"]

    UNI -->|provides| RULES
    RULES -->|enables| GRADE
    RULES -->|enables| MODULE
    GRADE -->|uses| SKILLS
    MODULE -->|uses| SKILLS

    style UNI fill:#e1f5ff
    style RULES fill:#f0f4c3
    style GRADE fill:#fff9c4
    style MODULE fill:#fff59d
    style SKILLS fill:#f3e5f5
```

<!-- section_id: "6e006914-8305-426c-83ab-7619eb36f069" -->
## Trigger System Architecture

```mermaid
graph TD
    T1["👤 User Event:<br/>Grade Status?"]
    T2["👤 User Event:<br/>Canvas Modules?"]
    T3["🔄 API Event:<br/>Requires Browser"]

    T1 -->|trigger| R1["Load Grade<br/>Strategy Trajectory"]
    T2 -->|trigger| R2["Load Module<br/>Fetching Trajectory"]
    T3 -->|trigger| R3["Load Browser<br/>Content Extraction"]

    R1 -->|invoke| S1["canvas-fetch<br/>Skill"]
    R2 -->|invoke| S2["canvas-module-fetch<br/>Skill"]
    R3 -->|invoke| S3["browser-canvas-reader<br/>Skill"]

    S1 -->|output| D1["Grade Dashboard"]
    S2 -->|output| D2["Module Structure"]
    S3 -->|output| D3["Extracted Content"]

    style T1 fill:#e3f2fd
    style T2 fill:#e3f2fd
    style T3 fill:#ffebee
    style R1 fill:#f1f8e9
    style R2 fill:#f1f8e9
    style R3 fill:#f1f8e9
    style S1 fill:#fce4ec
    style S2 fill:#fce4ec
    style S3 fill:#fce4ec
```

<!-- section_id: "cdd33dda-9352-4c63-a55b-303c21e51841" -->
## Path Organization (Current vs. Ideal)

<!-- section_id: "bb6a2ace-a637-4949-baa6-19a9133ef50b" -->
### Current Structure
**Problem**: Deep nesting creates long paths (155+ characters)

```
layer_0_universal/
└── layer_1/layer_1_projects/layer_1_project_school/
    └── layer_2/layer_2_sub_projects/layer_2_sub_project_classes/
        └── layer_3/layer_3_subx2_projects/layer_3_subx2_project_computer_science/
            └── layer_4_group/layer_4_subx3_projects/layer_4_subx3_project_machine_learning/
```

<!-- section_id: "05dd9465-9e50-443e-b10b-84f0fa5343c9" -->
### Ideal Structure (Flattened + Metadata-Based)
**Solution**: Flat filesystem + metadata layer defines relationships

```
school/
├── 0AGNOSTIC.md (defines: "parent: universal, children: classes")
├── .0agnostic/01_knowledge/
├── .0agnostic/02_rules/
└── .0agnostic/03_protocols/

classes/
├── 0AGNOSTIC.md (defines: "parent: school, triggers: grade-strategy")
└── .0agnostic/

computer_science/
├── 0AGNOSTIC.md
└── .0agnostic/

machine_learning/
├── 0AGNOSTIC.md (defines: "parent: cs, inherits: grade-strategy from classes")
└── .0agnostic/
```

**Key insight**: Relationships live in metadata, not filesystem depth.

```

