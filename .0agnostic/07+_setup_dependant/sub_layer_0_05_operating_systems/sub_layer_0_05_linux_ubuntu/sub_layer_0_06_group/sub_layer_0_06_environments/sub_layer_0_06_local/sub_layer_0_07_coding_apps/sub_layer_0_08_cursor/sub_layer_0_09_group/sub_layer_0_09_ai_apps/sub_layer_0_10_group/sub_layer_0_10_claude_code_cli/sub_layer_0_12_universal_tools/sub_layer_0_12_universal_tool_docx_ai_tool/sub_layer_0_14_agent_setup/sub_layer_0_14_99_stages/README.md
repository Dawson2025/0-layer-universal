# sub_layer_0_14_99_stages (Agent Setup Development)

## Purpose

Manages the development lifecycle for AI agent setup and configuration through 12 stages.

## Current Development Stage

See `status.json` for the active stage.

## Stage Structure

All agent setup progresses through 12 stages:

| Stage | Purpose |
|-------|---------|
| `00_registry` | Registry and initialization |
| `01_request_gathering` | Clarify setup requirements |
| `02_research` | Explore and research |
| `03_instructions` | Define constraints |
| `04_design` | Architecture decisions |
| `05_planning` | Break into subtasks |
| `06_development` | Implementation |
| `07_testing` | Verification and testing |
| `08_criticism` | Review |
| `09_fixing` | Corrections |
| `10_current_product` | Active setup |
| `11_archives` | Historical setup versions |

## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to deployment

## Navigation

See `CLAUDE.md` for agent setup lifecycle manager info and `status.json` for current stage.
