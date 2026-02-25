# DD-03: Stage Scaffolding Defaults

**Date**: 2026-02-25
**Status**: accepted
**Addresses**: All branches — production template improvements

---

## Problem Statement

When a new entity is created with stages, the `outputs/` directory of each stage is empty. This means:

1. Stage agents start with no structure — they have to create output directories from scratch
2. There's no hint about what outputs are expected
3. The tree of needs pattern (stage 01) requires a specific directory structure that every entity needs
4. Design decisions (stage 04) need an `outputs/design_decisions/` directory
5. Without scaffolding, every entity reinvents its output structure

## Proposed Solution: Default Output Scaffolding per Stage

When a stage is instantiated (via entity creation), its `outputs/` directory should include **scaffolding** — empty directory structures and README files that hint at expected outputs.

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

### Where This Lives

The scaffolding templates should be added to the **production entity creation** tools:

1. **`entity_structure.md`** — Add scaffolding specs to stage output definitions
2. **`/entity-creation` skill** — Generate scaffolding when creating stages
3. **`create-tree-of-needs.sh`** — Already creates tree of needs structure; extend to create the initial `_meta/` and `README.md`

### Production Change Required

Update these files in the production layer:
- `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` — Add output scaffolding specs
- `.claude/skills/entity-creation/SKILL.md` — Reference scaffolding in entity creation
- `.0agnostic/01_knowledge/layer_stage_system/stage_guides/` — Each stage guide should mention its default outputs

## Alternatives Considered

### Alternative A: No Scaffolding
Leave outputs/ empty. Let each stage agent create structure as needed.
- **Rejected**: Inconsistent output structures across entities. Stage agents waste time reinventing structure.

### Alternative B: Full Template Content
Pre-populate with template content (not just structure).
- **Rejected**: Too opinionated. Different entities have different needs. Scaffolding provides structure without content.

### Alternative C: Scaffolding Script Only
Only provide a script to generate scaffolding on demand.
- **Rejected**: Should be automatic on entity creation. Script is fine as backup, but default creation should include scaffolding.

## Trade-offs

| Trade-off | Accepted | Why |
|-----------|----------|-----|
| More files in fresh entities | Yes | Structure hints are more valuable than empty directories |
| Scaffolding may not fit all cases | Yes | README files explain conventions; agents can deviate if needed |
| Production template changes | Yes | Benefits all future entities — worth the one-time update |

## Design Constraints

- MUST NOT add content that assumes a specific domain
- MUST only scaffold directory structure and instructional READMEs
- MUST be compatible with the existing entity creation workflow
- SHOULD use .gitkeep for empty directories to ensure git tracks them

## Implementation Plan

1. Update `entity_structure.md` with output scaffolding specs per stage
2. Update entity-creation skill to generate scaffolding
3. Update stage guides to reference expected outputs
4. Add scaffolding templates to `.0agnostic/01_knowledge/layer_stage_system/resources/templates/`
