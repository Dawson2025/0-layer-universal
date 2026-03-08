---
resource_id: "2579ad15-52f5-4bb6-af10-55a7ad333692"
resource_type: "readme_output"
resource_name: "README"
---
# Design Decisions Overview — Organization Sub-Feature

**Entity**: Organization (layer_1_sub_feature_organization)
**Stage**: 04 Design
**Last Updated**: 2026-02-25

---

<!-- section_id: "c2fb37d3-974d-46f2-ac75-bf6a1e66fdd5" -->
## Summary

The organization sub-feature addresses a fundamental question: **how should any system be structurally organized to support experimentation, stability, and personalization?**

Three design decisions answer this question from different angles:

| Decision | Focus | Core Answer |
|----------|-------|-------------|
| [DD-01](#dd-01) | Architecture pattern | Every system has three versions: Research, Production, Instantiation |
| [DD-02](#dd-02) | Concrete example | The school system proves the pattern works for education |
| [DD-03](#dd-03) | Production tooling | Stage creation should auto-scaffold default output structures |

---

<!-- section_id: "705e2c4d-601d-49b3-a426-92535fa849a4" -->
## DD-01: Research/Production/Instantiation Pattern {#dd-01}

**File**: `../DD-01_research_production_instantiation_pattern.md`

The core architectural decision. Every system maintains three concurrent versions:

```
RESEARCH (layer_-1)          PRODUCTION (standard entity)         INSTANCES (children)
├── Experimental             ├── Stable, validated                ├── Per-user/per-context
├── Isolated from prod       ├── Serves as template               ├── Inherit via context chain
├── Multiple experiments     ├── Updated via promotion only        ├── Own stage lifecycle
└── Stage lifecycle (01-11)  └── Source of truth                   └── Instance-specific data
```

**Lifecycle flow**: Research → [promotion protocol] → Production → [instantiation] → Instances → [feedback loop]

**Key principle**: Separation by directory structure (not branches, not config flags). Research in `layer_-1_research/`, production in `layer_0/`/`layer_1/`, instances as child entities.

**Alternatives rejected**: Single-version (no experimentation), branch-based (git overhead), config-based (runtime complexity).

---

<!-- section_id: "7d90b384-6370-44da-ac55-9b07ffc4b533" -->
## DD-02: School System Architecture {#dd-02}

**File**: `../DD-02_school_system_architecture.md`

Concrete proof that DD-01's pattern applies to a real domain. The school system maps to R/P/I as:

| R/P/I Layer | School System Equivalent |
|-------------|-------------------------|
| **Research** | Experimental teaching approaches (knowledge graph awareness, adaptive learning, student modeling) |
| **Production** | Validated pedagogy, course structures, knowledge graphs, assessment templates |
| **Instances** | Per-student entities with individual knowledge state, goals, progress, career alignment |

**Research features identified**: knowledge_graph_awareness, student_modeling, adaptive_learning, prerequisite_tracking, career_alignment

**Instance context includes**: Student identity, enrolled courses, knowledge state per topic (mastered/in-progress/not-started), career goals, learning preferences

**Key insight**: The school system is a sub-system nested within the broader AI system — it has its own R/P/I cycle, independent of the parent. This demonstrates the recursive nature of the pattern.

---

<!-- section_id: "f2bed3a7-4dab-441b-a276-e5505d5cbaee" -->
## DD-03: Stage Scaffolding Defaults {#dd-03}

**File**: `../DD-03_stage_scaffolding_defaults.md`

Production-side tooling improvement. When new entities are created and their stages instantiated, the `outputs/` directory should include default scaffolding appropriate to each stage:

| Stage | Default Scaffolding |
|-------|-------------------|
| 01 Request Gathering | `outputs/requests/tree_of_needs/` with README template, `_meta/VERSION.md` |
| 02 Research | `outputs/reports/`, `outputs/by_topic/` |
| 04 Design | `outputs/design_decisions/` with README template, `overview/` |
| 06 Development | `outputs/artifacts/` |
| 07 Testing | `outputs/test_results/` |
| 10 Current Product | `outputs/deliverables/` |

**Changes required in production**: Update `entity_structure.md`, the `/entity-creation` skill, and stage guide templates.

**Key principle**: Convention over configuration — developers shouldn't need to invent output structures each time.

---

<!-- section_id: "7add8d55-fc48-4cc6-bc3a-dffa80d1ce7c" -->
## How These Decisions Relate

```
DD-01 (R/P/I Pattern)
  │
  ├── Applied to → DD-02 (School System)
  │                  └── Validates that R/P/I works for concrete domains
  │
  └── Tooling for → DD-03 (Stage Scaffolding)
                       └── Makes R/P/I easier to instantiate consistently
```

DD-01 defines the "what" (the pattern). DD-02 proves "it works" (the example). DD-03 addresses "make it easy" (the tooling).

---

<!-- section_id: "6495e6a6-83db-4b3d-9062-fb612242149d" -->
## Requirements Traceability

These design decisions address requirements from Stage 01's tree of needs:

| Design Decision | Addresses Branch | Addresses Needs |
|----------------|-----------------|-----------------|
| DD-01 | 01_research_production_lifecycle | need_01 (research version), need_02 (production version), need_03 (promotion workflow), need_04 (version coexistence) |
| DD-02 | 02_instantiation_pattern, 03_universal_pattern | need_01 (system features), need_02 (system instantiations), need_03 (instance context), need_02 (school system example) |
| DD-03 | 03_universal_pattern | need_01 (general pattern), need_03 (nested systems) |

---

<!-- section_id: "ffac5917-01e1-4691-9e73-a750bf8dc9b8" -->
## Next Steps

1. **Stage 02 (Research)**: Investigate how other systems implement similar patterns (academic research, industry case studies)
2. **Stage 05 (Planning)**: Break DD-01 implementation into concrete tasks
3. **Stage 06 (Development)**: Update production tooling per DD-03
4. **Promotion**: When validated, promote the R/P/I pattern documentation to production knowledge
