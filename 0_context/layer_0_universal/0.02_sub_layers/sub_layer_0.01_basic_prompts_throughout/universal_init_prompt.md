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
| 3 | Framework Guide | `0_context/0.00_layer_stage_framework/README.md` |

### 2. Find Project Init Prompt
```bash
# List project init prompts
ls -d ../**/project_init_prompt.md 2>/dev/null
```

---

## Directory Structure

```
0_ai_context/0_context/
├── MASTER_DOCUMENTATION_INDEX.md    # Start here
├── SYSTEM_OVERVIEW.md
├── 0.00_layer_stage_framework/      # Templates & framework docs
└── layer_0_universal/
    └── 0.02_sub_layers/
        ├── sub_layer_0.01_basic_prompts_throughout/  ← You are here
        ├── sub_layer_0.02_software_engineering_knowledge_system/
        ├── sub_layer_0.03_universal_principles/
        ├── sub_layer_0.04_universal_rules/
        └── sub_layer_0.05-0.014_setup_dependant_sub_layers/
            └── 0.01_universal_setup_file_tree_0/    # OS, AI apps, MCP, tools, protocols
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
└── 0.02_operating_systems/
    ├── _shared/          # Universal (all OSes)
    ├── linux_ubuntu/
    ├── macos/
    ├── windows/
    └── wsl/
        └── 0.03_environments/
            └── 0.04_coding_apps/
                └── 0.05_ai_apps/
                    ├── 0.06_mcp_servers/
                    ├── 0.06_ai_models/
                    ├── 0.07_universal_tools/
                    ├── 0.08_protocols/
                    └── 0.09_agent_setup/
```

---

## Common Tasks Quick Lookup

| Task | Go To |
|------|-------|
| MCP setup | `.../0.06_mcp_servers/_mcp_core/` |
| Browser automation | `.../0.08_protocols/` |
| Git operations | `sub_layer_0.04_universal_rules/.../git_commit_rule.md` |
| Terminal issues | `sub_layer_0.04_universal_rules/.../cursor_terminal_issues.md` |
| Universal tools | `.../0.07_universal_tools/` |
| Documentation protocol | `.../0.08_protocols/file_documentation_and_organization/` |

---

## Layer System Summary

| Layer | Purpose | Location |
|-------|---------|----------|
| 0 | Universal | `layer_0_universal/` - Applies to all projects |
| 1 | Project | `<project>/0_context/` - Project-specific |
| 2+ | Features/Components | Nested under project |

**Key principle:** Lower layers are prerequisites for higher layers.

---

## Stage System Summary

Each layer has stages representing workflow phases:

| Stage | Purpose |
|-------|---------|
| 01 | Instructions |
| 02 | Planning |
| 03 | Design |
| 04 | Development |
| 05 | Testing |
| 06 | Criticism |
| 07 | Fixing |
| 08 | Archives |

**Current stage tracked in:** `<layer>/.99_stages/status_<N>.json`

---

## Workflow (Abbreviated)

1. **Sync repos** - `git pull`
2. **Read master index** - Understand available docs
3. **Load project init** - If working on a project
4. **Identify layer/stage** - What level? What phase?
5. **Load relevant sub_layers** - Based on task type
6. **Execute work** - Follow stage guidelines
7. **Update status** - Mark progress

**Full workflow:** See `0.00_layer_stage_framework/README.md`

---

## Critical Rules

1. **Always sync first** - `git pull` before any work
2. **Read before writing** - Understand existing context
3. **Follow terminal protocol** - See `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
4. **Document changes** - Update relevant docs when making changes
5. **Commit appropriately** - Follow `git_commit_rule.md`

---

## Reference Documents

For detailed information, see these documents:

| Topic | Document |
|-------|----------|
| Layer/Stage System | `0.00_layer_stage_framework/README.md` |
| Flexible Layering | `0.00_layer_stage_framework/FLEXIBLE_LAYERING_SYSTEM.md` |
| Extending Framework | `0.00_layer_stage_framework/EXTENDING_THE_FRAMEWORK.md` |
| Feature Types | `0.00_layer_stage_framework/FEATURE_TYPE_DECISION_GUIDE.md` |
| Workflow Features | `0.00_layer_stage_framework/WORKFLOW_FEATURE_PATTERN.md` |
| Sub-layer Registry | `0.02_sub_layers/0.00_sub_layer_registry/README.md` |

---

*This is a condensed navigation hub. For detailed explanations, refer to the documents listed above.*
