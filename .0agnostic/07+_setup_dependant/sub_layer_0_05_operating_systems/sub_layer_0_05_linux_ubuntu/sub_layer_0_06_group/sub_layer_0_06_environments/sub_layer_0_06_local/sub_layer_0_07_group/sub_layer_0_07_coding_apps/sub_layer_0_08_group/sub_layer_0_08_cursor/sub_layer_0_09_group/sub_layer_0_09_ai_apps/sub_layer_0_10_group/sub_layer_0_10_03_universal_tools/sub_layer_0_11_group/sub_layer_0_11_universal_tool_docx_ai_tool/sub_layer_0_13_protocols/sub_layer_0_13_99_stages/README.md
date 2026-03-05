---
resource_id: "bb9fef5b-df4c-44b4-b6fe-61748140d48d"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_13_99_stages (Protocol Development)

<!-- section_id: "a7704424-1e8b-4489-9695-cd254b18a582" -->
## Purpose

Manages the development lifecycle for DOCX operation protocols through 12 stages.

<!-- section_id: "dd28d90e-c11e-4717-99b0-74aac4b87fe0" -->
## Current Development Stage

See `status.json` for the active stage.

<!-- section_id: "2773f266-6eba-42e2-8c75-136b6140a1fd" -->
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

<!-- section_id: "3fd9c067-6cae-43ae-8e9f-b4d5ba35b0d3" -->
## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to other systems

<!-- section_id: "5a6bd40a-a2ba-4bbf-81d3-001388a28625" -->
## Navigation

See `CLAUDE.md` for protocol lifecycle manager info and `status.json` for current stage.
