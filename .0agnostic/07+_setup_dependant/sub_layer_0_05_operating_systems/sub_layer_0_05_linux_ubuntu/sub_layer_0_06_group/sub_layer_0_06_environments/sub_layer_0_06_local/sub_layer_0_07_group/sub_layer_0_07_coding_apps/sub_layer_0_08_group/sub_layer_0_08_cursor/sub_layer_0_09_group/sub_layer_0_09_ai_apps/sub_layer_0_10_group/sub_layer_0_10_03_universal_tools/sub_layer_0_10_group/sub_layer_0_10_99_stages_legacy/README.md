---
resource_id: "b4a7670b-3b87-44fd-bcd9-fda6c9752591"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_12_universal_tools (Stages)

## Purpose

This directory manages the development lifecycle for universal tools that enhance AI agent capabilities across all projects and layers.

## Current Tools

Active tools in `stage_0_10_current_product/outputs/`:
(Currently empty - tools tracked in `_shared/` or specific project layers)

## Stage Structure

All tools progress through 12 stages:

| Stage | Purpose |
|-------|---------|
| `00_registry` | Registry and initialization |
| `01_request_gathering` | Clarify tool requirements |
| `02_research` | Research and exploration |
| `03_instructions` | Define constraints |
| `04_design` | Architecture decisions |
| `05_planning` | Break into subtasks |
| `06_development` | Implementation |
| `07_testing` | Verification |
| `08_criticism` | Review |
| `09_fixing` | Corrections |
| `10_current_product` | Active tools |
| `11_archives` | Historical tools |

## Shared Resources

Common resources available to all tools: `../_shared/`

## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages/layers
- `outgoing/` - Hand-offs to other stages/layers

## Navigation

See `CLAUDE.md` for stage manager info and `status.json` for current stage.
