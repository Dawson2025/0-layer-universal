---
resource_id: "e534336f-85d8-49df-9847-2e1d2d0aa201"
resource_type: "readme
document"
resource_name: "README"
---
## Memory Handling – Workflows

This folder is for **concrete workflows** that apply the Memory Handling Protocol, such as:

- “Remember user preferences” workflows.
- “Update long-term rules/configs” workflows.
- “Sync memory across layers/projects” workflows.

Each workflow instance you create here can follow the standard pattern:

- `0.02_sub_layers/` – any internal helpers.
- `0.99_stages/` – request_gathering → instructions → planning → design → implementation → testing → criticism → fixing → archiving, each with `ai_agent_system/` and `hand_off_documents/`.


