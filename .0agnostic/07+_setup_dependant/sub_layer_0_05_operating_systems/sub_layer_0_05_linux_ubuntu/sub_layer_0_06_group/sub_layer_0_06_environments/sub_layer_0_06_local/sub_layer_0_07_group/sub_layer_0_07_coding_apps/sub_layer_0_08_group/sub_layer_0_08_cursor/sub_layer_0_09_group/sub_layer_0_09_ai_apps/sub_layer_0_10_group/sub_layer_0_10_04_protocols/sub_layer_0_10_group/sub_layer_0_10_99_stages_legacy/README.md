---
resource_id: "c429600f-bfd5-410f-a622-b644c50612b8"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_13_protocols (Stages)

## Purpose

This directory manages the development lifecycle for universal protocols that AI agents use when performing operations across the system.

## Current Protocols

Active protocols in `stage_0_10_current_product/outputs/`:
- `docx_operations.md` - Protocol for AI agents working with .docx files
- `github_operations.md` - Protocol for AI agents working with GitHub

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

## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages/layers
- `outgoing/` - Hand-offs to other stages/layers

## Navigation

See `CLAUDE.md` for stage manager info and `status.json` for current stage.
