---
resource_id: "018728a9-86f3-49d9-879a-f3593df372e5"
resource_type: "document"
resource_name: "universal_init_prompt"
---
# Universal Session Initialization

**Purpose:** Entry point for ALL AI assistant sessions. Directs you to the right documentation.

---

<!-- section_id: "a7449411-d14e-4e33-82ad-dca6c53a6888" -->
## Quick Start

<!-- section_id: "17bd4824-8346-4945-afde-3cf1867a233d" -->
### 0. Sync First
```bash
git pull && git status
```

<!-- section_id: "011001f5-908e-4219-a1f1-260e02d10fed" -->
### 1. Read Essential Docs

| Priority | Document | Path |
|----------|----------|------|
| 1 | This File | You're reading it |
| 2 | Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/` |
| 3 | Project CLAUDE.md | Find via `find . -name "CLAUDE.md" -type f` |

<!-- section_id: "279e8491-2d82-4313-ba27-6974a766d179" -->
### 2. Find Project Init Prompt
```bash
# List project init prompts
find . -name "project_init_prompt.md" -type f 2>/dev/null
```

---

<!-- section_id: "d3226162-2222-47fe-94ce-77b27b0ba005" -->
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
│   ├── layer_0_03_sub_layers/          # Sub-layers (you are here)
│   │   ├── sub_layer_0_01_prompts/     # ← You are here
│   │   ├── sub_layer_0_02_knowledge_system/
│   │   ├── sub_layer_0_03_principles/
│   │   ├── sub_layer_0_04_rules/
│   │   └── sub_layer_0_05+_setup_dependant/
│   └── layer_0_99_stages/              # Universal stages
├── layer_1/
│   └── layer_1_features/
│       └── layer_1_feature_layer_stage_system/  # Framework definition
└── layer_-1_research/                  # Research projects
    └── layer_-1_better_ai_system/      # AI system improvements
```

---

<!-- section_id: "56c2b0a3-51b8-4629-8203-fdeffad7becc" -->
## Quick Reference Paths

<!-- section_id: "b6631d6d-a658-4679-a94c-084767ee7afb" -->
### Universal Rules & Protocols
```
layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/
├── 0_instruction_docs/
│   ├── MASTER_TERMINAL_EXECUTION_REFERENCE.md
│   ├── git_commit_rule.md
│   └── subagent_usage_decision_matrix.md
├── CROSS_OS_COMPATIBILITY_RULES.md
└── LAYER_CONTEXT_HEADER_PROTOCOL.md
```

<!-- section_id: "0b221eed-5747-40f6-8192-43ae9e1ce919" -->
### Setup & Configuration
```
layer_0/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/
└── sub_layer_0_05_operating_systems/
    ├── sub_layer_0_05_linux_ubuntu/
    ├── sub_layer_0_05_macos/
    ├── sub_layer_0_05_windows/
    └── sub_layer_0_05_wsl/
```

---

<!-- section_id: "2e035d91-eb95-448c-800a-f33830924e5a" -->
## Common Tasks Quick Lookup

| Task | Go To |
|------|-------|
| Git operations | `sub_layer_0_04_rules/0_instruction_docs/git_commit_rule.md` |
| Terminal protocol | `sub_layer_0_04_rules/0_instruction_docs/MASTER_TERMINAL_EXECUTION_REFERENCE.md` |
| **Create new entity** | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_99_stages/stage_0_08_current_product/setup/instantiation_guide.md` |
| **Subagent decisions** | `sub_layer_0_04_rules/0_instruction_docs/subagent_usage_decision_matrix.md` |

---

<!-- section_id: "a9eb9330-46ea-4bfe-9c6f-ec40a9caca94" -->
## Layer System Summary

| Layer | Purpose | Location |
|-------|---------|----------|
| -1 | Research | `layer_-1_research/` - Experimental projects |
| 0 | Universal | `layer_0/` - Applies to all projects |
| 1+ | Projects/Features | `layer_1/layer_1_features/` - Project-specific |

**Key principle:** Lower layers are prerequisites for higher layers.

**Naming Convention:** Use underscores, not dots: `layer_0_01_name`, `stage_0_02_name`

---

<!-- section_id: "a28d7410-821e-4f5e-8547-a8c30b431e09" -->
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

<!-- section_id: "8d07fdad-36c7-49d2-992b-3b331e5aac67" -->
## Workflow (Abbreviated)

1. **Sync repos** - `git pull`
2. **Read CLAUDE.md** - Start from root or project CLAUDE.md
3. **Identify layer/stage** - What level? What phase?
4. **Load relevant sub_layers** - Based on task type
5. **Execute work** - Follow stage guidelines
6. **Update status** - Mark progress in status.json

**Full workflow:** See `layer_1/layer_1_features/layer_1_feature_layer_stage_system/`

---

<!-- section_id: "08e4cbee-c579-4fdf-9ba1-326a530ffcba" -->
## Critical Rules

1. **Always sync first** - `git pull` before any work
2. **Read before writing** - Understand existing context
3. **Follow terminal protocol** - See `MASTER_TERMINAL_EXECUTION_REFERENCE.md`
4. **Document changes** - Update relevant docs when making changes
5. **Commit & push at significant points** - See below

<!-- section_id: "284b5523-18ec-4689-b0d5-bf7d0239cec2" -->
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

<!-- section_id: "2cc5c8e5-bec7-4b52-b9a1-3f3dcdf161b8" -->
## Reference Documents

| Topic | Document |
|-------|----------|
| Layer-Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/CLAUDE.md` |
| **Creating Entities** | `.../layer_1_99_stages/stage_0_08_current_product/setup/instantiation_guide.md` |
| Framework Docs | `.../layer_1_02_sub_layers/sub_layer_1_05+_setup_dependant/sub_layer_1_05_framework_docs/` |
| Context Gathering | `layer_0/layer_0_01_ai_manager_system/agnostic/context_gathering_rules.md` |
| Sub-layer Registry | `layer_0/layer_0_03_sub_layers/layer_0_00_sub_layer_registry/README.md` |

---

<!-- section_id: "f13c6eaa-ed19-47c2-9b47-b2e97a51bad5" -->
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

<!-- section_id: "5adb477d-9933-4d50-aea0-009ff1ef54f8" -->
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
