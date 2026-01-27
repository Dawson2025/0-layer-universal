# layer_0_99_stages

## Role

**Stages Manager** - Manages universal workflow stages (templates for all projects).

## Responsibilities

- Create/remove/reorder universal stages
- Delegate tasks to appropriate stage
- Aggregate results from stages
- Handle escalations from stages
- Maintain stage registry

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from layer_0
2. Check `hand_off_documents/incoming/from_below/` for results/escalations from stages
3. Process pending work or delegate to appropriate stage

## Children (Universal Stages)

| Number | Name | Purpose |
|--------|------|---------|
| 00 | stage_registry | Stage definitions and metadata (data only) |
| 01 | request_gathering | Collect and clarify requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints and guidelines |
| 04 | planning | Break into subtasks |
| 05 | design | Architecture decisions |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review and critique |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical versions |

## Navigation

- **Parent**: `../` (layer_0)
- **Registry**: `layer_0_00_stage_registry/`

## Scope

These are **universal stage templates**. Project-specific stages inherit from these.
