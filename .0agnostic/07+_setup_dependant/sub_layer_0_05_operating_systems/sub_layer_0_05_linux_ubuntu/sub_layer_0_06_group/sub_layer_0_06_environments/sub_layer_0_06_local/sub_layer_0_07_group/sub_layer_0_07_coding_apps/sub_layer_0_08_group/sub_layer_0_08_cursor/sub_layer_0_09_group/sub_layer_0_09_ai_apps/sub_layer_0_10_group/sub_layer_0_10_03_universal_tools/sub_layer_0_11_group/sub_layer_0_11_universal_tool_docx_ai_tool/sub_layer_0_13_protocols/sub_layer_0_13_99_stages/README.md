---
resource_id: "bb9fef5b-df4c-44b4-b6fe-61748140d48d"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_13_99_stages (Protocol Development)

## Purpose

Manages the development lifecycle for DOCX operation protocols through 12 stages.

## Current Development Stage

See `status.json` for the active stage.

## Stage Structure

All protocols progress through 12 stages:

| Stage | Purpose |
|-------|---------|
| `00_registry` | Registry and initialization |
| `01_request_gathering` | Clarify requirements |
| `02_research` | Explore and research |
| `03_instructions` | Define constraints |
| `04_design` | Architecture decisions |
| `05_planning` | Break into subtasks |
| `06_development` | Implementation |
| `07_testing` | Verification |
| `08_criticism` | Review |
| `09_fixing` | Corrections |
| `10_current_product` | Active protocols |
| `11_archives` | Historical protocols |

## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to other systems

## Navigation

See `CLAUDE.md` for protocol lifecycle manager info and `status.json` for current stage.
