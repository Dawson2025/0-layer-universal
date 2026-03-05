---
resource_id: "d459f827-34b1-44fe-b183-f2d6a662d6ca"
resource_type: "protocol"
resource_name: "universal_init_prompt"
---
# Universal Session Initialization

**Purpose:** Entry point for ALL AI assistant sessions. Directs you to the right documentation.

---

<!-- section_id: "51f77f4c-7f8b-4e76-9b98-fef881dc344e" -->
## Quick Start

<!-- section_id: "03c5144c-c9c9-41fe-b563-ce7318b44fed" -->
### 0. Sync First
```bash
git pull && git status
```

<!-- section_id: "76b5339c-6dbc-44ea-843b-72c3a24cc646" -->
### 1. Read Essential Docs

| Priority | Document | Path |
|----------|----------|------|
| 1 | This File | You're reading it |
| 2 | Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` |
| 3 | Project CLAUDE.md | Find via `find . -name "CLAUDE.md" -type f` |

<!-- section_id: "044ecf50-6c9e-49bf-a75e-9a30a32bef0d" -->
### 2. Find Project Init Prompt
```bash
# List project init prompts
find . -name "project_init_prompt.md" -type f 2>/dev/null
```

---

<!-- section_id: "da44b958-976e-43e2-90e2-8dffa3876a45" -->
## Directory Structure

```
0_layer_universal/
├── CLAUDE.md                           # Root AI context
├── layer_0/                            # Universal layer (applies to all)
│   ├── layer_0_00_layer_registry/      # Layer registry
│   ├── layer_0_01_ai_manager_system/   # AI agent management
│   │   ├── agnostic/                   # Tool-agnostic config
│   │   └── specific/                   # Tool-specific config
│   ├── layer_0_02_manager_handoff_documents/
│   ├── layer_0_04_sub_layers/          # Sub-layers (you are here)
│   │   ├── sub_layer_0_01_knowledge_system/
│   │   ├── sub_layer_0_02_rules/
│   │   ├── sub_layer_0_03_protocols/  # ← You are here
│   │   └── sub_layer_0_04+_setup_dependant/
│   └── layer_0_99_stages/              # Universal stages
├── layer_1/
│   └── layer_1_features/
│       └── layer_1_feature_layer_stage_system/  # Framework definition
└── layer_-1_research/                  # Research projects
    └── layer_-1_better_ai_system/      # AI system improvements
```

---

<!-- section_id: "23eb993a-e3c3-46c3-8b75-bcc8da1330bf" -->
## Quick Reference Paths

<!-- section_id: "e323b3d3-ccfa-4c05-87aa-c861524f0c6c" -->
### Universal Rules & Protocols
```
layer_0/layer_0_04_sub_layers/sub_layer_0_02_rules/
├── 0_instruction_docs/
│   ├── MASTER_TERMINAL_EXECUTION_REFERENCE.md
│   ├── git_commit_rule.md
│   └── subagent_usage_decision_matrix.md
├── CROSS_OS_COMPATIBILITY_RULES.md
└── LAYER_CONTEXT_HEADER_PROTOCOL.md
```

<!-- section_id: "d81f1b90-f3d4-46cb-92e9-28c02995e3af" -->
### Setup & Configuration
```
layer_0/layer_0_04_sub_layers/sub_layer_0_04+_setup_dependant/
└── sub_layer_0_04_operating_systems/
    ├── sub_layer_0_04_linux_ubuntu/
    ├── sub_layer_0_04_macos/
    ├── sub_layer_0_04_windows/
    └── sub_layer_0_04_wsl/
```

---

<!-- section_id: "c80e62e7-ffc7-4994-b3e1-557db8616675" -->
## Common Tasks Quick Lookup

| Task | Go To |
|------|-------|
| Git operations | `sub_layer_0_02_rules/0_instruction_docs/git_commit_rule.md` |
| Terminal protocol | `sub_layer_0_02_rules/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` |
| **Create new entity** | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_99_stages/stage_0_08_current_product/setup/instantiation_guide.md` |
| **Subagent decisions** | `sub_layer_0_02_rules/0_instruction_docs/subagent_usage_decision_matrix.md` |

---

<!-- section_id: "9f2c1889-2bf9-4d46-b877-8a6baf87000c" -->
## Layer System Summary

| Layer | Purpose | Location |
|-------|---------|----------|
| -1 | Research | `layer_-1_research/` - Experimental projects |
| 0 | Universal | `layer_0/` - Applies to all projects |
| 1+ | Projects/Features | `layer_1/layer_1_features/` - Project-specific |

**Key principle:** Lower layers are prerequisites for higher layers.

**Naming Convention:** Use underscores, not dots: `layer_0_01_name`, `stage_0_02_name`

---

<!-- section_id: "6b35ddaf-4170-45e7-9ccf-5c9baddcf88a" -->
## Stage System Summary

Each layer has stages representing workflow phases:

| Stage | Name | Purpose |
|-------|------|---------|
| 01 | request_gathering | Clarify requirements |
| 02 | research | Explore problem space, gather info |
| 03 | instructions | Define constraints |
| 04 | planning | Break into subtasks |
| 05 | design | Architecture decisions |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | The actual deliverable |
| 11 | archives | Historical versions |

**Stage structure:**
```
stage_0_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes (reference outputs)
└── outputs/               # Stage artifacts
```

**Current stage tracked in:** `<layer>/layer_N_99_stages/status.json`

---

<!-- section_id: "59c97d06-c573-463a-8fb3-a0de98ba5593" -->
## Workflow (Abbreviated)

1. **Sync repos** - `git pull`
2. **Read CLAUDE.md** - Start from root or project CLAUDE.md
3. **Identify layer/stage** - What level? What phase?
4. **Load relevant sub_layers** - Based on task type
5. **Execute work** - Follow stage guidelines
6. **Update status** - Mark progress in status.json

**Full workflow:** See `layer_1/layer_1_features/layer_1_feature_layer_stage_system/`

---

<!-- section_id: "dd7a52b2-66f7-48b0-aff4-d66a3f78f69e" -->
## Critical Rules

1. **Always sync first** - `git pull` before any work
2. **Read before writing** - Understand existing context
3. **Follow terminal protocol** - See `MASTER_TERMINAL_EXECUTION_REFERENCE.md`
4. **Document changes** - Update relevant docs when making changes
5. **Commit & push at significant points** - See below

<!-- section_id: "af6bfb1c-1329-4139-bb6c-94d590332810" -->
### Commit & Push Protocol

**Commit and push to remote at each significant milestone**, not just at the end of a session.

**When to commit & push:**
- After completing a logical unit of work (feature, fix, refactor)
- After updating documentation
- After making structural changes (renames, reorganization)
- Before starting a risky operation

**Commit message format:**
```
<type>: <short description>

<optional body explaining what/why>

Co-Authored-By: <AI model> <noreply@anthropic.com>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `style`, `test`

---

<!-- section_id: "f880c57a-79e0-423a-a1ed-a71cf71f830f" -->
## Reference Documents

| Topic | Document |
|-------|----------|
| Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/CLAUDE.md` |
| **Creating Entities** | `.../layer_1_99_stages/stage_0_08_current_product/setup/instantiation_guide.md` |
| Framework Docs | `.../layer_1_02_sub_layers/sub_layer_1_05+_setup_dependant/sub_layer_1_05_framework_docs/` |
| Context Gathering | `layer_0/layer_0_01_ai_manager_system/agnostic/context_gathering_rules.md` |
| Sub-layer Registry | `layer_0/layer_0_04_sub_layers/layer_0_00_sub_layer_registry/README.md` |

---

<!-- section_id: "d4f4924f-1efb-4387-9bd6-18d33d459d6d" -->
## Known Issues & Research

> **Active Research:** The AI system has known inconsistencies being addressed in:
> `layer_-1_research/layer_-1_better_ai_system/`
>
> **Key Issues:**
> - Naming conventions (standardizing to underscores)
> - Stage numbering (11 stages: 00-10)
> - Documentation drift from implementation
>
> See: `layer_-1_research/layer_-1_better_ai_system/layer_0/layer_0_99_stages/stage_0_02_research/outputs/ai_system_problems_audit.md`

---

<!-- section_id: "108b8327-8002-4025-b8cc-158394adcfc4" -->
## Maintenance Note

> **When making structural changes to the framework:**
>
> 1. **Content migration** - Migrate actual content, not just create empty structures
> 2. **Traversal updates** - Update ALL navigation docs so agents can find the new paths
>
> **Priority files to update:**
> 1. **This file** (`universal_init_prompt.md`)
> 2. Root `CLAUDE.md`
> 3. Framework docs in `layer_1_feature_layer_stage_system`
>
> **Last updated:** 2026-01-25 (Fixed naming to use underscores, updated paths to match actual structure)

---

*This is a condensed navigation hub. For detailed explanations, refer to the documents listed above.*
