---
resource_id: "6e80c1c8-5ce2-4084-ae07-64a04116ff89"
resource_type: "output"
resource_name: "DD-03_stage_scaffolding_defaults"
---
# DD-03: Stage Scaffolding Defaults

**Date**: 2026-02-25
**Status**: accepted
**Addresses**: All branches — production template improvements

---

<!-- section_id: "5306e537-3e9a-4047-9ac0-e935c67ba1e1" -->
## Problem Statement

When a new entity is created with stages, the `outputs/` directory of each stage is empty. This means:

1. Stage agents start with no structure — they have to create output directories from scratch
2. There's no hint about what outputs are expected
3. The tree of needs pattern (stage 01) requires a specific directory structure that every entity needs
4. Design decisions (stage 04) need an `outputs/design_decisions/` directory
5. Without scaffolding, every entity reinvents its output structure

<!-- section_id: "a2729656-7184-4666-993e-670cdc72b1c3" -->
## Proposed Solution: Default Output Scaffolding per Stage

When a stage is instantiated (via entity creation), its `outputs/` directory should include **scaffolding** — empty directory structures and README files that hint at expected outputs.

<!-- section_id: "459664a3-e4af-403a-ae23-0dd182a87d2b" -->
### Scaffolding per Stage

| Stage | Default Scaffolding |
|-------|-------------------|
| 01_request_gathering | `outputs/requests/tree_of_needs/` with `_meta/` and root need placeholder |
| 02_research | `outputs/by_topic/` with `README.md` explaining topic-based organization |
| 03_instructions | `outputs/constraints/` and `outputs/rules/` |
| 04_design | `outputs/design_decisions/` with `README.md` template |
| 05_planning | `outputs/plans/` |
| 06_development | `outputs/artifacts/` |
| 07_testing | `outputs/test_results/` |
| 08_criticism | `outputs/reviews/` |
| 09_fixing | `outputs/fixes/` |
| 10_current_product | `outputs/deliverables/` |
| 11_archives | `outputs/archived/` |

<!-- section_id: "a6e54a53-112b-4a26-8672-c6ce75f81e02" -->
### Tree of Needs Scaffolding (Stage 01)

The most structured default. When stage 01 is created:

```
outputs/
  requests/
    tree_of_needs/
      _meta/
        VERSION.md       # "| 0.0.0 | [date] | Initial scaffolding |"
        DEPENDENCIES.md  # Empty template
        CHANGELOG.md     # Empty template
      README.md          # Instructions for creating the tree of needs
```

The `README.md` includes:
- How to structure root needs, branches, and leaf needs
- File naming conventions (REQ-01_name.md, US-01_name.md)
- Links to the tree of needs methodology from the stage guide

<!-- section_id: "76b4f502-8870-48ab-a828-294178fd261c" -->
### Design Decisions Scaffolding (Stage 04)

```
outputs/
  design_decisions/
    README.md            # Template for design decision records
```

The `README.md` includes:
- Design decision format (Problem Statement, Proposed Solution, Alternatives, Trade-offs)
- Naming convention (DD-01_name.md)
- Link to design stage guide

<!-- section_id: "3c35baa2-91e8-4b5f-bdbe-e6602d7e266b" -->
### Where This Lives

The scaffolding templates should be added to the **production entity creation** tools:

1. **`entity_structure.md`** — Add scaffolding specs to stage output definitions
2. **`/entity-creation` skill** — Generate scaffolding when creating stages
3. **`create-tree-of-needs.sh`** — Already creates tree of needs structure; extend to create the initial `_meta/` and `README.md`

<!-- section_id: "240623cc-0b6a-4510-8d45-f89f79318336" -->
### Production Change Required

Update these files in the production layer:
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` — Add output scaffolding specs
- `.claude/skills/entity-creation/SKILL.md` — Reference scaffolding in entity creation
- `.0agnostic/01_knowledge/layer_stage_system/stage_guides/` — Each stage guide should mention its default outputs

<!-- section_id: "008de409-6851-4b6d-a406-ff79d9e035e2" -->
## Alternatives Considered

<!-- section_id: "1cbfed34-bf9d-415f-9cd4-77a5678dd2d4" -->
### Alternative A: No Scaffolding
Leave outputs/ empty. Let each stage agent create structure as needed.
- **Rejected**: Inconsistent output structures across entities. Stage agents waste time reinventing structure.

<!-- section_id: "3d114352-97da-4de2-a103-6bde735ac1d0" -->
### Alternative B: Full Template Content
Pre-populate with template content (not just structure).
- **Rejected**: Too opinionated. Different entities have different needs. Scaffolding provides structure without content.

<!-- section_id: "0c4f6daf-8b2f-46ac-a4a0-0006cde72c9c" -->
### Alternative C: Scaffolding Script Only
Only provide a script to generate scaffolding on demand.
- **Rejected**: Should be automatic on entity creation. Script is fine as backup, but default creation should include scaffolding.

<!-- section_id: "f44613ff-ff6e-439f-bcc6-8c80ff153148" -->
## Trade-offs

| Trade-off | Accepted | Why |
|-----------|----------|-----|
| More files in fresh entities | Yes | Structure hints are more valuable than empty directories |
| Scaffolding may not fit all cases | Yes | README files explain conventions; agents can deviate if needed |
| Production template changes | Yes | Benefits all future entities — worth the one-time update |

<!-- section_id: "ca6568dc-e748-4a55-892c-8e4da2dc7c80" -->
## Design Constraints

- MUST NOT add content that assumes a specific domain
- MUST only scaffold directory structure and instructional READMEs
- MUST be compatible with the existing entity creation workflow
- SHOULD use .gitkeep for empty directories to ensure git tracks them

<!-- section_id: "4d1f282f-89ca-4cf3-a5e9-56dde8e53e62" -->
## Implementation Plan

1. Update `entity_structure.md` with output scaffolding specs per stage
2. Update entity-creation skill to generate scaffolding
3. Update stage guides to reference expected outputs
4. Add scaffolding templates to `.0agnostic/01_knowledge/layer_stage_system/resources/templates/`
