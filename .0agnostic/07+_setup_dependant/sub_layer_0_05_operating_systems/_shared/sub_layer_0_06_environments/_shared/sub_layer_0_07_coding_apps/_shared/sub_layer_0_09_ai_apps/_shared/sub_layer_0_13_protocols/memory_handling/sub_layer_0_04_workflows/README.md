---
resource_id: "a9fbfb7b-5efa-4f4d-9007-e9fc8f94e715"
resource_type: "readme
document"
resource_name: "README"
---
<!-- section_id: "81f322fa-101d-4c8b-8dec-f75f1df09edc" -->
## Memory Handling – Workflows

This folder is for **concrete workflows** that apply the Memory Handling Protocol, such as:

- “Remember user preferences” workflows.
- “Update long-term rules/configs” workflows.
- “Sync memory across layers/projects” workflows.

Each workflow instance you create here can follow the standard pattern:

- `0.02_sub_layers/` – any internal helpers.
- `0.99_stages/` – request_gathering → instructions → planning → design → implementation → testing → criticism → fixing → archiving, each with `ai_agent_system/` and `hand_off_documents/`.


