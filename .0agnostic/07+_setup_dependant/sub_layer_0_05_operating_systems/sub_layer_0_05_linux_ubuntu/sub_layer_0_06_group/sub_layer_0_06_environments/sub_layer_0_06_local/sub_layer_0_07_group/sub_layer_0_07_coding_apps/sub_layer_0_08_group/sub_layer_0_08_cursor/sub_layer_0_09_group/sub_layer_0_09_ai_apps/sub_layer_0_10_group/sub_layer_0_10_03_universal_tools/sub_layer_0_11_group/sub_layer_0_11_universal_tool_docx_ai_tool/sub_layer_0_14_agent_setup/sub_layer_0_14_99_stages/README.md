---
resource_id: "d8400bbd-ad5e-4a19-8d69-747eb39d3fc0"
resource_type: "readme
document"
resource_name: "README"
---
# sub_layer_0_14_99_stages (Agent Setup Development)

<!-- section_id: "001c0f87-3c86-4169-bcce-0aea88bd2774" -->
## Purpose

Manages the development lifecycle for AI agent setup and configuration through 12 stages.

<!-- section_id: "6250cf6d-c473-4034-8bb0-0b9b722dfd7b" -->
## Current Development Stage

See `status.json` for the active stage.

<!-- section_id: "26b1529f-b847-4ab3-94e1-18a0741400a6" -->
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

<!-- section_id: "c7b1dee1-0826-4276-8aad-838469cec6e1" -->
## Hand-offs

Cross-stage communication: `hand_off_documents/`
- `incoming/` - Hand-offs from other stages
- `outgoing/` - Hand-offs to deployment

<!-- section_id: "42387349-d60a-4acc-9d49-088ffb4e0203" -->
## Navigation

See `CLAUDE.md` for agent setup lifecycle manager info and `status.json` for current stage.
