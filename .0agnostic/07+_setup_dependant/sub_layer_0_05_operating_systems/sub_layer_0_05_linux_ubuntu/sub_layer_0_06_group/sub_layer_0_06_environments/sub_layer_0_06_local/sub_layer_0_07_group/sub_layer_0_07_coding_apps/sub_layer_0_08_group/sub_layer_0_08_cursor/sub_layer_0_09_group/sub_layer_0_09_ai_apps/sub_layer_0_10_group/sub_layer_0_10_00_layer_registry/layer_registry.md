---
resource_id: "460ecd5a-16bb-4539-9660-143b3dbd8d83"
resource_type: "document"
resource_name: "layer_registry"
---
# Level 10 Layer Registry — AI Apps Children

<!-- section_id: "199ac054-dcad-4a35-82c3-da7172eea80a" -->
## Entity Types at Level 10

<!-- section_id: "065ff2f2-b85c-4d5d-ab64-f02742ae4f82" -->
### Feature (numbered, shared)

**Naming**: `sub_layer_0_10_NN_name/` (with sequence number)
**Purpose**: Shared infrastructure and knowledge available to ALL AI app entities
**Sequence**: Features are numbered because they have dependency order — know your tools before configuring your agent

| # | Entity | Scope |
|---|--------|-------|
| 01 | tools_and_services | MCP servers, APIs, CLIs, secrets, budget tracking |
| 02 | ai_models | AI model definitions, capabilities, pricing |
| 03 | universal_tools | Shared dev tools (docx_ai_tool, etc.) |
| 04 | protocols | Shared operational protocols |
| 05 | agent_setup | Agent configuration and customization patterns |

<!-- section_id: "3b519a85-83db-4069-95fb-f07ca4ac3d8d" -->
### Further Specificity (unnumbered, app-specific)

**Naming**: `sub_layer_0_10_name/` (no sequence number)
**Purpose**: Configuration specific to a single AI app choice
**Relationship to features**: Each app inherits from and can override shared features

| Entity | Scope |
|--------|-------|
| claude_code_cli | Claude Code CLI setup, config, app-specific children (Claude in Chrome) |
| codex_cli | OpenAI Codex CLI setup and config |
| cursor_agent | Cursor Agent/Composer setup and config |
| gemini_cli | Google Gemini CLI setup and config |

<!-- section_id: "d6cd6707-cbe6-4921-8863-ad788a36099f" -->
## Notes

- Feature entities contain knowledge and tools shared across all AI apps
- Further specificity entities contain app-specific overrides and children
- Feature sequence: tools (01) → models (02) → dev tools (03) → protocols (04) → agent setup (05)
