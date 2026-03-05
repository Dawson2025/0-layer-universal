---
resource_id: "680e4295-3b60-4c68-be96-a9f44216b43a"
resource_type: "readme
document"
resource_name: "README"
---
# Staging System Quick Reference

**Purpose**: Quick reference for AI agents working with the staging system.

---

<!-- section_id: "5567ada3-a5d8-4ab9-a0aa-d1dada1dabef" -->
## Quick Reference for AI Agents

<!-- section_id: "b82e78cb-5cf8-4edd-acb9-19693fb5a76b" -->
### Before Creating ANY File
1. Read `CROSS_OS_COMPATIBILITY_RULES.md` (in `../layer_0_04_sub_layers/sub_layer_0_02_rules/`)
2. **NEVER** use: `* ? < > : " | \ /` in filenames
3. Use lowercase with underscores: `my_file_name.md`

<!-- section_id: "980c658e-4fce-46e6-b01b-159a6da2a326" -->
### When Working on Tasks
1. Check `hand_off_documents/incoming.json` in the current stage
2. Read handoff first (short), then `outputs/` files if needed
3. Update `hand_off_documents/outgoing.json` when status changes

---

<!-- section_id: "07b8bbb3-091a-4d4e-b09c-89b52518c478" -->
## Core Documents

| Document | Location | Purpose |
|----------|----------|---------|
| `STAGING_SYSTEM.md` | This folder | How to use stages and handoffs |
| `WORKFLOW.md` | `../layer_0_01_ai_manager_system/` | AI agent coordination system |
| `CROSS_OS_COMPATIBILITY_RULES.md` | `../layer_0_04_sub_layers/sub_layer_0_02_rules/` | File naming rules for Windows/Linux/macOS |
| `_templates/` | This folder | Templates for handoffs, requests, etc. |

---

<!-- section_id: "53ed2ec4-ef4d-469e-b1c1-1850e3daee8b" -->
## Staging System Overview

```
layer_0_99_stages/
├── stage_0_01_request_gathering/
│   ├── ai_agent_system/     ← Stage-specific agent guidance
│   ├── hand_off_documents/  ← Incoming/outgoing handoffs
│   └── outputs/             ← Detailed artifacts
│
├── stage_0_02_research/
│   ├── ai_agent_system/
│   ├── hand_off_documents/
│   └── outputs/
│
├── stage_0_03_instructions/
├── stage_0_04_planning/
├── stage_0_05_design/
├── stage_0_06_development/
├── stage_0_07_testing/
├── stage_0_08_criticism/
├── stage_0_09_fixing/
├── stage_0_10_current_product/
└── stage_0_11_archives/
```

<!-- section_id: "5ea24816-a836-4e76-bb25-a06a536b8540" -->
### AI Agent Entry Protocol
1. Read `hand_off_documents/incoming.json` (status summary)
2. Read `ai_agent_system/` (what to do)
3. Read `outputs/` files only if details needed
4. Update `hand_off_documents/outgoing.json` before stopping

<!-- section_id: "69df0187-aeeb-4720-b2ac-2e57ffcdbd7c" -->
### Token-Efficient Workflow
1. Read `hand_off_documents/incoming.json` (~500 tokens)
2. Only read `outputs/` files if details needed
3. Reference files instead of repeating content

---

<!-- section_id: "3779de6e-491a-44e3-aa28-b37903c66895" -->
## Cross-OS Rules Summary

| Rule | Reason |
|------|--------|
| No `*` in filenames | Windows forbidden |
| No spaces | Causes script issues |
| Lowercase only | Case sensitivity differs |
| Paths < 200 chars | Windows limit |
| Use `/` in configs | Works on all OS |

---

<!-- section_id: "0aa0cabe-6bca-4e98-bcb0-bb58c23779b8" -->
## For New Projects

1. Create `stages/` folder structure
2. Copy templates from `_templates/`
3. Start with `stage_0_01_request_gathering/`
4. Create `hand_off_documents/` first, then `outputs/` details

---

<!-- section_id: "57ece0bc-0aff-4b4e-88bc-7748871d0936" -->
## Current Active Tasks

Check `status.json` for the current stage and active tasks.
