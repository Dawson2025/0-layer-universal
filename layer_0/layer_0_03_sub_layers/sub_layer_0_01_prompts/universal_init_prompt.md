# Universal Session Initialization

**Purpose:** Entry point for ALL AI assistant sessions. Directs you to the right documentation.

---

## Quick Start

### 0. Sync First
```bash
git pull && git status
```

### 1. Read Essential Docs

| Priority | Document | Path |
|----------|----------|------|
| 1 | Master Index | `0_context/MASTER_DOCUMENTATION_INDEX.md` |
| 2 | System Overview | `0_context/SYSTEM_OVERVIEW.md` |
| 3 | Framework Guide | `0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` |

### 2. Find Project Init Prompt
```bash
# List project init prompts
ls -d ../**/project_init_prompt.md 2>/dev/null
```

---

## Directory Structure

```
0_layer_universal/0_context/
├── MASTER_DOCUMENTATION_INDEX.md    # Start here
├── SYSTEM_OVERVIEW.md
├── layer_1/layer_1_features/layer_1_feature_layer_stage_system/         # System management & planning
│   └── stages/
│       └── stage_0.08_current_product/
│           ├── changes/             # Change protocols
│           └── setup/               # Entity creation guides
├── layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/      # Templates & framework docs
└── layer_0/
    ├── 0.02_sub_layers/
    │   ├── sub_layer_0_01_basic_prompts_throughout/  ← You are here
    │   ├── sub_layer_0_02_software_engineering_knowledge_system/
    │   ├── sub_layer_0.03_universal_principles/
    │   ├── sub_layer_0.04_universal_rules/
    │   └── sub_layer_0.05-0.014_setup_dependant_sub_layers/
    │       └── 0.01_universal_setup_file_tree_0/    # OS, AI apps, MCP, tools, protocols
    └── 0.99_stages/                 # Universal layer stages (N.00-N.09)
```

---

## Quick Reference Paths

### Universal Rules & Protocols
```
sub_layer_0.04_universal_rules/0_instruction_docs/
├── UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md
├── cursor_terminal_issues.md
├── ai_agent_documentation_rule.md
└── git_commit_rule.md
```

### Setup & Configuration (Unified Tree)
```
sub_layer_0.05-0.014_setup_dependant_sub_layers/0.01_universal_setup_file_tree_0/
└── 0.05_operating_systems/
    ├── _shared/          # Universal (all OSes)
    ├── linux_ubuntu/
    ├── macos/
    ├── windows/
    └── wsl/
        └── 0.06_environments/
            └── 0.07_coding_apps/
                └── 0.09_ai_apps/
                    ├── 0.10_mcp_servers_and_apis_and_clis_and_secrets/
                    ├── 0.11_ai_models/
                    ├── 0.12_universal_tools/
                    ├── 0.13_protocols/
                    └── 0.14_agent_setup/
```

---

## Common Tasks Quick Lookup

| Task | Go To |
|------|-------|
| MCP setup | `.../0.10_mcp_servers_and_apis_and_clis_and_secrets/` |
| Browser automation | `.../0.13_protocols/` |
| Git operations | `sub_layer_0.04_universal_rules/0_instruction_docs/git_commit_rule.md` |
| Terminal issues | `sub_layer_0.04_universal_rules/0_instruction_docs/cursor_terminal_issues.md` |
| Universal tools | `.../0.12_universal_tools/` |
| Documentation protocol | `.../0.13_protocols/file_documentation_and_organization/` |
| **Create new entity** | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/setup/instantiation_guide.md` |
| **Subagent decisions** | `sub_layer_0.04_universal_rules/0_instruction_docs/subagent_usage_decision_matrix.md` |

---

## Layer System Summary

| Layer | Purpose | Location |
|-------|---------|----------|
| 0 | Universal | `layer_0/` - Applies to all projects |
| 1+ | Project | `<N>_layer_<project>/layer_<N>/` - Project-specific |
| N+1 | Features/Components | `<project>/layer_<N+1>/` - Nested under project |

**Key principle:** Lower layers are prerequisites for higher layers.
**Naming:** Top-level projects use `<N>_layer_<name>/` format (e.g., `1_layer_school/`)

---

## Stage System Summary

Each layer has stages representing workflow phases:

| Stage | Name | Purpose |
|-------|------|---------|
| 00 | request_gathering | Clarify requirements |
| 01 | **research** | Explore problem space, gather info |
| 02 | instructions | Define constraints |
| 03 | planning | Break into subtasks |
| 04 | design | Architecture decisions |
| 05 | development | Implementation |
| 06 | testing | Verification |
| 07 | criticism | Review |
| 08 | fixing | Corrections |
| 09 | **current_product** | **The actual deliverable** |
| 10 | archives | Historical versions |

**Stage structure:**
```
stage_N_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes (reference outputs)
└── outputs/               # Stage artifacts
```

**Current stage tracked in:** `<layer>/layer_<N>_99_stages/status_<N>.json`

---

## Workflow (Abbreviated)

1. **Sync repos** - `git pull`
2. **Read master index** - Understand available docs
3. **Load project init** - If working on a project
4. **Identify layer/stage** - What level? What phase?
5. **Load relevant sub_layers** - Based on task type
6. **Execute work** - Follow stage guidelines
7. **Update status** - Mark progress

**Full workflow:** See `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md`

---

## Critical Rules

1. **Always sync first** - `git pull` before any work
2. **Read before writing** - Understand existing context
3. **Follow terminal protocol** - See `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
4. **Document changes** - Update relevant docs when making changes
5. **Commit & push at significant points** - See below

### Commit & Push Protocol

**Commit and push to remote at each significant milestone**, not just at the end of a session. This ensures:
- Work is preserved if session is interrupted
- Progress is trackable
- Changes can be reviewed incrementally

**When to commit & push:**
- After completing a logical unit of work (feature, fix, refactor)
- After updating documentation
- After making structural changes (renames, reorganization)
- Before starting a risky operation
- At natural breakpoints in multi-step tasks

**Commit message format:**
```
<type>: <short description>

<optional body explaining what/why>

Co-Authored-By: <AI model> <noreply@anthropic.com>
```

**Types:** `feat`, `fix`, `docs`, `refactor`, `chore`, `style`, `test`

See `git_commit_rule.md` for full guidelines.

---

## Reference Documents

For detailed information, see these documents:

| Topic | Document |
|-------|----------|
| System Management | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/README.md` |
| **Creating Entities** | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/setup/instantiation_guide.md` |
| Restructuring/Migration | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/changes/restructuring_migration_protocol.md` |
| **Traversal/Path Updates** | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/changes/traversal_update_protocol.md` |
| Layer/Stage Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` |
| Flexible Layering | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FLEXIBLE_LAYERING_SYSTEM.md` |
| Extending Framework | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/EXTENDING_THE_FRAMEWORK.md` |
| Feature Types | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/FEATURE_TYPE_DECISION_GUIDE.md` |
| Workflow Features | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/WORKFLOW_FEATURE_PATTERN.md` |
| Sub-layer Registry | `layer_0/0.02_sub_layers/0.00_sub_layer_registry/README.md` |

---

## Maintenance Note

> **When making structural changes to the framework** (renaming directories, adding new stages/layers, modifying the hierarchy):
>
> **Critical:**
> 1. **Content migration** - Migrate actual content, not just create empty structures
> 2. **Traversal updates** - Update ALL navigation docs so agents can find the new paths
>
> See:
> - `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/changes/restructuring_migration_protocol.md`
> - `layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0.08_current_product/changes/traversal_update_protocol.md`
>
> | Priority | File | What to Update |
> |----------|------|----------------|
> | 1 | **This file** (`universal_init_prompt.md`) | Directory paths & structure diagrams |
> | 2 | `MASTER_DOCUMENTATION_INDEX.md` | Document links |
> | 3 | `SYSTEM_OVERVIEW.md` | Architecture description |
> | 4 | `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/README.md` | Framework structure |
> | 5 | All `*.md` files with hardcoded paths | Use `grep` + `sed` for bulk updates |
>
> **Verify:** After changes, test navigation from this file to new locations.
>
> **Last updated:** 2026-01-25 (Added research stage (01), outputs folders, stage_registry system)

---

*This is a condensed navigation hub. For detailed explanations, refer to the documents listed above.*
