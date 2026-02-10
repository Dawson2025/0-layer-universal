# Staging System Quick Reference

**Purpose**: Quick reference for AI agents working with the staging system.

---

## Quick Reference for AI Agents

### Before Creating ANY File
1. Read `CROSS_OS_COMPATIBILITY_RULES.md` (in `../layer_0_04_sub_layers/sub_layer_0_02_rules/`)
2. **NEVER** use: `* ? < > : " | \ /` in filenames
3. Use lowercase with underscores: `my_file_name.md`

### When Working on Tasks
1. Check `hand_off_documents/incoming.json` in the current stage
2. Read handoff first (short), then `outputs/` files if needed
3. Update `hand_off_documents/outgoing.json` when status changes

---

## Core Documents

| Document | Location | Purpose |
|----------|----------|---------|
| `STAGING_SYSTEM.md` | This folder | How to use stages and handoffs |
| `WORKFLOW.md` | `../layer_0_01_ai_manager_system/` | AI agent coordination system |
| `CROSS_OS_COMPATIBILITY_RULES.md` | `../layer_0_04_sub_layers/sub_layer_0_02_rules/` | File naming rules for Windows/Linux/macOS |
| `_templates/` | This folder | Templates for handoffs, requests, etc. |

---

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

### AI Agent Entry Protocol
1. Read `hand_off_documents/incoming.json` (status summary)
2. Read `ai_agent_system/` (what to do)
3. Read `outputs/` files only if details needed
4. Update `hand_off_documents/outgoing.json` before stopping

### Token-Efficient Workflow
1. Read `hand_off_documents/incoming.json` (~500 tokens)
2. Only read `outputs/` files if details needed
3. Reference files instead of repeating content

---

## Cross-OS Rules Summary

| Rule | Reason |
|------|--------|
| No `*` in filenames | Windows forbidden |
| No spaces | Causes script issues |
| Lowercase only | Case sensitivity differs |
| Paths < 200 chars | Windows limit |
| Use `/` in configs | Works on all OS |

---

## For New Projects

1. Create `stages/` folder structure
2. Copy templates from `_templates/`
3. Start with `stage_0_01_request_gathering/`
4. Create `hand_off_documents/` first, then `outputs/` details

---

## Current Active Tasks

Check `status.json` for the current stage and active tasks.
