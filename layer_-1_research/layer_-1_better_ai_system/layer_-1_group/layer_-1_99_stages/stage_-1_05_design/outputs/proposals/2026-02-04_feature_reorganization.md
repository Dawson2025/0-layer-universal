# Proposal: Feature Reorganization & Layer Structure

## Metadata

| Field | Value |
|-------|-------|
| **Proposal ID** | PROP-2026-02-04-REORG |
| **Status** | Draft |
| **Created** | 2026-02-04 |

---

## Problems Identified

### 1. Duplicate Infrastructure in layer_0_group

**Current layer_0_group:**
```
layer_0_group/
├── layer_0_00_layer_registry        ← WRONG: Duplicates layer_-1_group
├── layer_0_01_ai_manager_system     ← WRONG: Duplicates layer_-1_group
├── layer_0_02_manager_handoff_documents ← WRONG: Duplicates
├── layer_0_03_sub_layers            ← OK: Universal rules/knowledge
├── layer_0_99_stages                ← OK: Universal stage templates
└── layer_0_features/                ← OK: Features folder
```

**Fix**: Remove duplicates, add proper further-layering structure.

### 2. Flat Feature List is Cluttered

**Current 8 features (flat):**
```
layer_0_features/
├── layer_0_feature_ai_automation_system
├── layer_0_feature_ai_context_system
├── layer_0_feature_ai_documentation_system
├── layer_0_feature_ai_dynamic_memory_system
├── layer_0_feature_ai_manager_hierarchy_system
├── layer_0_feature_ai_rules_system
├── layer_0_feature_better_layer_stage_system
└── layer_0_feature_better_setup_system
```

**Problem**: 8 items at root is too many to scan quickly.

**Fix**: Group into higher-level feature categories based on tree of needs.

### 3. Where Does JSON-LD Navigation Fit?

**Options:**
- A. Sub-feature of `better_layer_stage_system` (structure focus)
- B. Sub-feature of `ai_context_system` (context delivery focus)
- C. New feature `ai_navigation_system`

**Recommendation**: Sub-feature of a new high-level **context_framework** feature.

---

## Proposed Structure

### layer_0_group (Cleaned Up)

**Principle**: layer_0_group is for **further layering** (features, components, subprojects) only.
Infrastructure (registry, managers, handoffs, sub_layers, stages) belongs in **layer_-1_group**.

**Each folder has its own registry inside it** (not separate registry folders).

```
layer_0_group/
├── layer_0_features/
│   ├── 0INDEX.md                    ← Features registry (inside features folder)
│   └── ...features...
├── layer_0_components/
│   └── 0INDEX.md                    ← Components registry (inside components folder)
└── layer_0_subprojects/
    └── 0INDEX.md                    ← Subprojects registry (inside subprojects folder)
```

**Removed (all belong in layer_-1_group):**
- `layer_0_00_layer_registry` → Use layer_-1_group's registry
- `layer_0_01_ai_manager_system` → Use layer_-1_group's manager
- `layer_0_02_manager_handoff_documents` → Use layer_-1_group's handoffs
- `layer_0_03_sub_layers` → Sub-layers are research infrastructure
- `layer_0_99_stages` → Stages are research infrastructure

### layer_0_features (Reorganized)

**Group features by tree of needs branches:**

```
layer_0_features/
├── 0INDEX.md                        ← Features registry
│
├── layer_0_feature_context_framework/      ← HIGH-LEVEL (06_context_flow + 01_capable)
│   ├── layer_1_subfeature_context_system/        ← Was: ai_context_system
│   ├── layer_1_subfeature_dynamic_memory/        ← Was: ai_dynamic_memory_system
│   └── layer_1_subfeature_navigation_system/     ← NEW: JSON-LD navigation
│
├── layer_0_feature_structure_framework/    ← HIGH-LEVEL (organization)
│   ├── layer_1_subfeature_layer_stage_system/    ← Was: better_layer_stage_system
│   └── layer_1_subfeature_setup_system/          ← Was: better_setup_system
│
├── layer_0_feature_governance_framework/   ← HIGH-LEVEL (03_trustworthy)
│   ├── layer_1_subfeature_rules_system/          ← Was: ai_rules_system
│   └── layer_1_subfeature_manager_hierarchy/     ← Was: ai_manager_hierarchy_system
│
└── layer_0_feature_tooling_framework/      ← HIGH-LEVEL (02_continuous + 04_observable)
    ├── layer_1_subfeature_automation_system/     ← Was: ai_automation_system
    └── layer_1_subfeature_documentation_system/  ← Was: ai_documentation_system
```

---

## Tree of Needs → Feature Mapping

| Tree Branch | Question | High-Level Feature | Sub-Features |
|-------------|----------|-------------------|--------------|
| 06_context_flow | Does context reach agents? | **context_framework** | context_system, dynamic_memory, navigation_system |
| 01_capable | Can AI do the work? | **context_framework** | (same - knowledge/context) |
| 02_continuous | Does work keep going? | **tooling_framework** | automation_system |
| 03_trustworthy | Can I trust AI? | **governance_framework** | rules_system, manager_hierarchy |
| 04_observable | Can I see what's happening? | **tooling_framework** | documentation_system |
| (structure) | Is it organized? | **structure_framework** | layer_stage_system, setup_system |

---

## JSON-LD Navigation Placement

**Recommendation**: `context_framework/layer_1_subfeature_navigation_system/`

**Why:**
- JSON-LD navigation is about **context delivery** (how context reaches agents)
- Maps to `06_context_flow/need_02_context_propagation_works`
- Works alongside context_system and dynamic_memory

**Structure:**
```
layer_0_feature_context_framework/
└── layer_1_subfeature_navigation_system/
    ├── index.jsonld              ← Self-describing!
    ├── CLAUDE.md
    ├── layer_1_group/
    │   └── layer_1_99_stages/
    └── layer_2_group/
        └── layer_2_components/
            ├── layer_2_component_jsonld_schema/
            ├── layer_2_component_link_validator/
            └── layer_2_component_graph_builder/
```

---

## Migration Plan

### Phase 1: Clean layer_0_group

1. Remove ALL infrastructure folders:
   - `layer_0_00_layer_registry/`
   - `layer_0_01_ai_manager_system/`
   - `layer_0_02_manager_handoff_documents/`
   - `layer_0_03_sub_layers/`
   - `layer_0_99_stages/`
2. Add proper further-layering folders (each with its own 0INDEX.md registry):
   - `layer_0_components/0INDEX.md`
   - `layer_0_subprojects/0INDEX.md`
3. Keep `layer_0_features/` and add `0INDEX.md` (will reorganize in Phase 2)

### Phase 2: Create High-Level Features

1. Create 4 high-level feature folders
2. Move existing features as sub-features
3. Update all CLAUDE.md and index files

### Phase 3: Add Navigation System

1. Move JSON-LD prototype to `context_framework/navigation_system/`
2. Create proper sub-feature structure
3. Update cross-references

---

## Before/After Comparison

### Before (8 items at root)
```
layer_0_features/
├── ai_automation_system
├── ai_context_system
├── ai_documentation_system
├── ai_dynamic_memory_system
├── ai_manager_hierarchy_system
├── ai_rules_system
├── better_layer_stage_system
└── better_setup_system
```

### After (4 items at root, 8 as sub-features)
```
layer_0_features/
├── 0INDEX.md
├── context_framework/      ← 3 sub-features
├── structure_framework/    ← 2 sub-features
├── governance_framework/   ← 2 sub-features
└── tooling_framework/      ← 2 sub-features
```

---

## Questions for User

1. **Naming**: `layer_0_feature_context_framework` or simpler `context_framework`?
2. **Sub-feature depth**: `layer_1_subfeature_*` or just `subfeature_*`?
3. **Empty folders**: Create `layer_0_components/` now even if empty?
4. **Migration**: Do full migration now or incrementally?

---

## Version

- **Proposal Version**: 1.0.0
- **Created**: 2026-02-04
