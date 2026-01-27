# layer_-1_99_stages

## Role

**Stages Manager** - Manages workflow stages for the better_ai_system research project.

## Responsibilities

- Create/remove/reorder stages
- Delegate tasks to appropriate stage
- Aggregate results from stages
- Handle escalations from stages
- Maintain stage registry

## On Session Start

1. Check `hand_off_documents/incoming/from_above/` for tasks from layer
2. Check `hand_off_documents/incoming/from_below/` for results/escalations from stages
3. Process pending work or delegate to appropriate stage

## Children (Stages)

| Number | Name | Purpose |
|--------|------|---------|
| 00 | registry | Stage definitions and metadata (data only) |
| 01 | request_gathering | Collect and clarify requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints and guidelines |
| 04 | design | Architecture decisions |
| 05 | planning | Break into subtasks |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review and critique |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical versions |

## Navigation

- **Parent**: `../../` (layer_-1 of better_ai_system)
- **Registry**: `stage_-1_00_registry/`

## Stage Operations

### Delegate to Stage
1. Write task to `stage_-1_XX_*/hand_off_documents/incoming/from_above/`
2. Stage reads and executes
3. Stage writes result to its `outgoing/to_above/`
4. This manager reads from `incoming/from_below/`

### Reorder Stages
1. Update stage definitions in registry
2. Rename stage directories to new numbers
3. Update all cross-references
4. Document changes

### Add New Stage
1. Determine position in sequence
2. Renumber subsequent stages if needed
3. Create stage directory with standard structure
4. Update registry
