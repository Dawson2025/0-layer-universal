---
resource_id: "63337039-4845-4ccf-b667-a5bdc489df33"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# context_chain_system — Layer 2 Group

<!-- section_id: "edba2bcf-7fc3-4cac-ab41-13f5aa682d05" -->
## Identity

entity_id: "d6d87ebc-58a1-4379-bd39-f756aec62aa3"

Internal structure container for the context_chain_system entity.
- **Parent**: `../0AGNOSTIC.md`

<!-- section_id: "d14e192f-7e40-4c67-ae87-c3d84dca6f4f" -->
## Contents
- `layer_2_00_layer_registry/` — Registry and proposals
- `layer_2_99_stages/` — Stage workflow (00-11)

<!-- section_id: "e904d7e2-8ea9-407b-bcef-f0c3e6866bee" -->
## Migration Note

`layer_2_01_ai_manager_system/` and `layer_2_02_manager_handoff_documents/` are legacy compatibility paths.

Canonical manager identity and handoff flow now live under:
- Entity root `0AGNOSTIC.md`
- Entity `.0agnostic/05_handoff_documents/`
- Stage `.0agnostic/05_handoff_documents/`
