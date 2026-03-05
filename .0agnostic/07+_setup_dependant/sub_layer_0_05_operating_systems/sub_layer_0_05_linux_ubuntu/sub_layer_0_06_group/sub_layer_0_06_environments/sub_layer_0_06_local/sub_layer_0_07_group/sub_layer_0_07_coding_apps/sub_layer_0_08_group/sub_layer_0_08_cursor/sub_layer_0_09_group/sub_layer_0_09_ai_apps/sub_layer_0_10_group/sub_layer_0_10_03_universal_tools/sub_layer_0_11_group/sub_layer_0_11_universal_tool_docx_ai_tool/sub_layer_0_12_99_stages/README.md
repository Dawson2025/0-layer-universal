---
resource_id: "5d834ebd-b895-41d3-bae1-89dcf989e534"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_12_99_stages (Tool Development)

<!-- section_id: "23a9de91-654d-4306-9e4d-25d6e95af2e9" -->
## Purpose

Manages the development lifecycle for the DOCX AI tool through 12 stages.

<!-- section_id: "ba6dea0e-b673-4aa0-86cd-6a1bf37956c9" -->
## Current Development Stage

See `status.json` for the active stage.

<!-- section_id: "319daf4e-0a4f-4e9b-968d-692c48232e84" -->
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

<!-- section_id: "55c0be50-fb2d-4b85-844e-944bf76b5736" -->
## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to other stages

<!-- section_id: "46cae5d1-24cb-493f-942c-836160d5890a" -->
## Navigation

See `CLAUDE.md` for stage manager info and `status.json` for current stage.
