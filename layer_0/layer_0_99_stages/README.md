# Staging System Quick Reference

**Purpose**: Quick reference for AI agents working with the staging system.

---

## Quick Reference for AI Agents

### Before Creating ANY File
1. Read `CROSS_OS_COMPATIBILITY_RULES.md` (in `../layer_0_02_sub_layers/sub_layer_0_04_rules/`)
2. **NEVER** use: `* ? < > : " | \ /` in filenames
3. Use lowercase with underscores: `my_file_name.md`

### When Working on Tasks
1. Check for `HANDOFF.md` in current stage
2. Read handoff first (short), then output files if needed
3. Update handoff when status changes

---

## Core Documents

| Document | Location | Purpose |
|----------|----------|---------|
| `STAGING_SYSTEM.md` | This folder | How to use stages and handoffs |
| `WORKFLOW.md` | `../layer_0_00_ai_manager_system/` | AI agent coordination system |
| `CROSS_OS_COMPATIBILITY_RULES.md` | `../layer_0_02_sub_layers/sub_layer_0_04_rules/` | File naming rules for Windows/Linux/macOS |
| `_templates/` | This folder | Templates for handoffs, requests, etc. |

---

## Staging System Overview

```
layer_0_99_stages/
├── stage_0_00_request_gathering/
│   ├── HANDOFF.md          ← Read first (short summary)
│   ├── _ai_manager/        ← AI instructions for this stage
│   │   └── INSTRUCTIONS.md
│   └── output/             ← Detailed artifacts
│
├── stage_0_01_instructions/
│   ├── HANDOFF.md
│   ├── _ai_manager/
│   └── output/
│
├── stage_0_02_planning/
│   ├── HANDOFF.md
│   ├── _ai_manager/
│   └── output/
│
├── stage_0_03_design/
├── stage_0_04_development/
├── stage_0_05_testing/
├── stage_0_06_criticism/
├── stage_0_07_fixing/
├── stage_0_08_current_product/
└── stage_0_09_archives/
```

### AI Agent Entry Protocol
1. Read `HANDOFF.md` (status summary)
2. Read `_ai_manager/INSTRUCTIONS.md` (what to do)
3. Read `output/` files only if details needed
4. Update HANDOFF.md before stopping

### Token-Efficient Workflow
1. Read `HANDOFF.md` (~500 tokens)
2. Only read `output/` files if details needed
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
3. Start with `stage_0_00_request_gathering/`
4. Create `HANDOFF.md` first, then `output/` details

---

## Current Active Tasks

Check `.../linux_ubuntu/setup/stages/` for:
- Linux login loop fix
- Termius cross-device SSH setup
- Full mesh SSH connectivity

Read the `HANDOFF.md` in `stage_0_03_execution/` for current status.
