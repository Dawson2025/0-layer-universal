---
resource_id: "c429600f-bfd5-410f-a622-b644c50612b8"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_13_protocols (Stages)

<!-- section_id: "0d0ed91d-9ffb-40af-b1c3-7b839d954717" -->
## Purpose

This directory manages the development lifecycle for universal protocols that AI agents use when performing operations across the system.

<!-- section_id: "2c228fc4-99d0-4bc7-a4d0-732b494a5a98" -->
## Current Protocols

Active protocols in `stage_0_10_current_product/outputs/`:
- `docx_operations.md` - Protocol for AI agents working with .docx files
- `github_operations.md` - Protocol for AI agents working with GitHub

<!-- section_id: "621ebd4f-1de0-4cc8-8f74-4791ee21f687" -->
## Stage Structure

All protocols progress through 12 stages:

| Stage | Purpose |
|-------|---------|
| `00_registry` | Registry and initialization |
| `01_request_gathering` | Clarify protocol requirements |
| `02_research` | Research and exploration |
| `03_instructions` | Define constraints |
| `04_design` | Architecture decisions |
| `05_planning` | Break into subtasks |
| `06_development` | Implementation |
| `07_testing` | Verification |
| `08_criticism` | Review |
| `09_fixing` | Corrections |
| `10_current_product` | Active protocols |
| `11_archives` | Historical protocols |

<!-- section_id: "95dfb488-6ef1-401a-939b-eabb601fa468" -->
## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages/layers
- `outgoing/` - Hand-offs to other stages/layers

<!-- section_id: "ba89c262-b6d8-439b-84ce-629c4e38faf2" -->
## Navigation

See `CLAUDE.md` for stage manager info and `status.json` for current stage.
