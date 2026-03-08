---
resource_id: "c20df2b3-5fda-4ce6-a718-cc0035b01f35"
resource_type: "readme_document"
resource_name: "README"
---
<!-- section_id: "f6090073-dcd0-4dc5-b29a-fe8abe47ecdf" -->
## Memory Handling – Workflows

This folder is for **concrete workflows** that apply the Memory Handling Protocol, such as:

- “Remember user preferences” workflows.
- “Update long-term rules/configs” workflows.
- “Sync memory across layers/projects” workflows.

Each workflow instance you create here can follow the standard pattern:

- `0.02_sub_layers/` – any internal helpers.
- `0.99_stages/` – request_gathering → instructions → planning → design → implementation → testing → criticism → fixing → archiving, each with `ai_agent_system/` and `hand_off_documents/`.


