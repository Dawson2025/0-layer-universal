# AI Context Flow Constraints - 2026-02-03

## Source

User requirements from session 2026-02-03.

---

## Constraints (MUST Follow)

### 1. Stage Completeness Rule

**Constraint**: ALL 11 stages MUST be created when an entity uses stages.

```
entity_99_stages/
├── stage_XX_01_request_gathering/outputs/   ← REQUIRED
├── stage_XX_02_research/outputs/            ← REQUIRED
├── stage_XX_03_instructions/outputs/        ← REQUIRED
├── stage_XX_04_planning/outputs/            ← REQUIRED
├── stage_XX_05_design/outputs/              ← REQUIRED
├── stage_XX_06_development/outputs/         ← REQUIRED
├── stage_XX_07_testing/outputs/             ← REQUIRED
├── stage_XX_08_criticism/outputs/           ← REQUIRED
├── stage_XX_09_fixing/outputs/              ← REQUIRED
├── stage_XX_10_current_product/outputs/     ← REQUIRED
└── stage_XX_11_archives/outputs/            ← REQUIRED
```

**Rationale**: Empty stages are valid. Missing stages cause inconsistency and agent confusion.

---

### 2. Propagation Chain Required

**Constraint**: All AI context changes MUST show a propagation chain diagram before implementation.

**Required elements**:
1. Knowledge layer (what file in sub_layer?)
2. Skills layer (which skills reference it?)
3. Tool files layer (what gets regenerated?)
4. Agent usage (how agents will use it)

**Rationale**: Ensures traceability, consistency, and prevents "amnesia" where agents don't know about changes.

---

### 3. Minimal CLAUDE.md

**Constraint**: CLAUDE.md (and equivalent tool files) MUST contain only:
- Identity
- Critical rules
- Triggers
- Pointers to tool folders (.claude/, skills/)

**NOT allowed in CLAUDE.md**:
- Detailed instructions (put in skills)
- Knowledge content (put in sub_layers)
- Duplicated information

**Rationale**: Single source of truth in knowledge docs, accessed via skills.

---

### 4. Skills Reference, Don't Duplicate

**Constraint**: Skills MUST reference knowledge docs, NOT duplicate content.

**Structure**:
```
skill-name/
├── SKILL.md           ← Instructions and protocol
└── references/        ← Pointers to knowledge (paths, not copies)
```

**Rationale**: One source of truth. Changes propagate automatically.

---

### 5. Document User Decisions

**Constraint**: User decisions and requirements MUST be documented in the appropriate research stages.

| Content Type | Stage |
|--------------|-------|
| Requirements | 01_request_gathering |
| Constraints/Rules | 03_instructions |
| Architecture/Design | 05_design |
| Alternatives | 08_criticism |

**Rationale**: Creates audit trail, enables future agents to understand "why".

---

---

### 6. Tree of Needs Required

**Constraint**: Every `stage_XX_01_request_gathering/outputs/` MUST contain a `requests/tree_of_needs/` folder.

**Structure**:
```
outputs/requests/tree_of_needs/
├── README.md                     ← Overview and quick reference
├── TREE_TO_FEATURES_MAPPING.md   ← How needs map to features
├── _meta/                        ← Versioning, changelog, sessions
│   └── sessions/                 ← Session documents
└── 00_root_need/                 ← Hierarchical folder structure
    ├── 01_branch/
    │   ├── need_01_xxx/
    │   └── need_02_yyy/
    └── 02_branch/
        └── ...
```

**Rationale**: Creates clear hierarchy of requirements, helps future agents understand motivations.

---

### 7. Tree of Needs Informs Further Layering

**Constraint**: The tree of needs hierarchy MUST inform how child entities are organized in further layers.

**Mapping (Relative to Current Position)**:
| Tree Level | Relative Depth | At Project (L1) | At Feature (L2) |
|------------|----------------|-----------------|-----------------|
| Root need | Current (+0) | Project itself | Feature itself |
| Branch | Child (+1) | Features | Components |
| Need | Grandchild (+2) | Components | Sub-components |
| Sub-need | Great-grandchild (+3) | Sub-components | Modules |

**Example at Layer 1 (Project)**:
```
Tree: 00_root/01_branch/need_01_xxx
Maps to: project/layer_2_features/layer_2_feature_branch/layer_3_components/layer_3_component_xxx
```

**Example at Layer 2 (Feature)**:
```
Tree: 00_root/01_branch/need_01_xxx
Maps to: feature/layer_3_components/layer_3_component_branch/layer_4_subcomponents/layer_4_subcomponent_xxx
```

**Rationale**: Ensures child entities are organized by purpose, traceable to requirements, and consistently structured regardless of where you are in the hierarchy.

---

## Enforcement

These constraints are documented in:
- `layer_0/.../STAGES_EXPLAINED.md` - Stage Completeness Rule
- `layer_0/.../AI_CONTEXT_FLOW_ARCHITECTURE.md` - Propagation Chain, Skills Architecture
- `0AGNOSTIC.md` - Critical rules at root level
