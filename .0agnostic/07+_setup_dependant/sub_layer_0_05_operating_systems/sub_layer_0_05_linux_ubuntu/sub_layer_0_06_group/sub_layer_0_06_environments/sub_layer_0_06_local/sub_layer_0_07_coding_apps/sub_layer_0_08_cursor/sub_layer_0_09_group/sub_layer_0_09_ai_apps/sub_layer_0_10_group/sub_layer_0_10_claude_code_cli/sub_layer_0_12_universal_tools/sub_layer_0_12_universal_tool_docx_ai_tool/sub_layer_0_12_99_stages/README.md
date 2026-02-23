# sub_layer_0_12_99_stages (Tool Development)

## Purpose

Manages the development lifecycle for the DOCX AI tool through 12 stages.

## Current Development Stage

See `status.json` for the active stage.

## Stage Structure

All tool development progresses through 12 stages:

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
| `10_current_product` | Active tool |
| `11_archives` | Historical versions |

## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to other stages

## Navigation

See `CLAUDE.md` for stage manager info and `status.json` for current stage.
