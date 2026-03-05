---
resource_id: "9a5aa040-5f81-4567-bdf7-aabee5197dae"
resource_type: "document"
resource_name: "INSTRUCTIONS_AI_MANAGER_HIERARCHY_SYSTEM.sync-conflict-20260126-035815-IF2WOGZ"
---
# INSTRUCTIONS: AI Manager Hierarchy System

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define the agnostic/specific pattern for AI tool configurations

---

<!-- section_id: "679e92af-3f1f-4b13-8495-57a165996e93" -->
## 1. Overview

The AI Manager Hierarchy System defines:
- Tool-agnostic source (the universal truth)
- Tool-specific implementations (CLAUDE.md, .cursorrules, etc.)
- Nested specificity (os → environment → coding_app → ai_app)

---

<!-- section_id: "6957fb2e-905a-4f59-84c7-d4d57eecee1a" -->
## 2. Core Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AGNOSTIC SOURCE                                       │
│                                                                             │
│  layer_N_00_ai_manager_system/agnostic/                                     │
│  ├── init_prompt.md              # Universal source of truth                │
│  ├── context_gathering_rules.md  # How to gather context                    │
│  ├── handoff_schema.md           # Handoff format                           │
│  └── layer_navigation.md         # How to navigate layers                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ FEEDS INTO
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                     TOOL-SPECIFIC IMPLEMENTATIONS                            │
│                                                                             │
│  At Entity Root:                                                            │
│  ├── CLAUDE.md           # Claude Code                                      │
│  ├── .claude/            # Claude Code folder                               │
│  ├── .cursorrules        # Cursor IDE                                       │
│  ├── AGENTS.md           # OpenAI Codex                                     │
│  ├── GEMINI.md           # Gemini CLI                                       │
│  └── .mcp.json           # MCP servers                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ SPECIALIZED BY
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NESTED SPECIFICITY                                    │
│                                                                             │
│  layer_N_00_ai_manager_system/specific/                                     │
│  └── os/                         # Level 1: Operating System                │
│      └── environment/            # Level 2: Environment                     │
│          └── coding_app/         # Level 3: Coding Application              │
│              └── ai_app/         # Level 4: AI Application                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "9b5e7595-398a-4905-85b4-47886575b710" -->
## 3. Agnostic Source

The agnostic source is the **tool-independent** source of truth.

<!-- section_id: "8aace001-2fdf-4fff-998f-a74661cf1ad6" -->
### 3.1 Directory Structure

```
layer_N_00_ai_manager_system/
└── agnostic/
    ├── init_prompt.md                # Core init prompt
    ├── context_gathering_rules.md    # Context rules
    ├── handoff_schema.md             # Handoff format
    ├── layer_navigation.md           # Navigation rules
    └── conventions.md                # Entity conventions
```

<!-- section_id: "6643ea85-2837-477e-898f-36b696a8c8b4" -->
### 3.2 init_prompt.md Template

```markdown
# Layer N: [Entity Name]

## Inherited From
- Parent: `../../../layer_N-1_00_ai_manager_system/agnostic/init_prompt.md`

## Purpose
[What this entity does]

## Context Rules
- Vertical chain: Always gather ancestors and descendants
- Horizontal siblings: Only when task-relevant
- Task sources: user request, status.json, handoffs, todos

## Stage Status
- Current stage: [from status_N.json]
- In progress: [tasks]

## Conventions
- [Entity-specific conventions]

## Children
- `layer_N+1/layer_N+1_features/` - Features
- `layer_N+1/layer_N+1_components/` - Components

## Tools Available
- See CLAUDE.md for Claude Code specifics
- See .cursorrules for Cursor IDE specifics
```

---

<!-- section_id: "cee0925a-3e3c-4fec-ba4e-6f964af36361" -->
## 4. Tool-Specific Implementations

Each AI tool has its own configuration file(s) at the entity root.

<!-- section_id: "b35b3764-68b5-414e-bca4-f92a11a7709c" -->
### 4.1 Claude Code

```
entity_root/
├── CLAUDE.md                         # Context and rules
└── .claude/
    ├── settings.json                 # Settings
    ├── commands/                     # Slash commands
    │   └── command-name.md
    ├── agents/                       # Subagents
    │   └── agent-name.md
    └── skills/                       # Model-invoked skills
        └── skill-name/
            └── SKILL.md
```

**CLAUDE.md Template:**
```markdown
# [Entity Name]

## Overview
[Brief description, generated from agnostic/init_prompt.md]

## Commands Available
- `/command-name` - Description

## Agents Available
- `agent-name` - Description

## Skills Available
- `skill-name` - Description

## Context
[Inherited from parent CLAUDE.md + entity-specific]
```

<!-- section_id: "d14207ed-00f7-431d-859e-5bce96563f9a" -->
### 4.2 Cursor IDE

```
entity_root/
├── .cursorrules                      # Cursor rules
└── .cursor/                          # Cursor folder (if needed)
```

**.cursorrules Template:**
```
# [Entity Name] - Cursor Rules

## Context
[Generated from agnostic/init_prompt.md]

## Rules
- [Rule 1]
- [Rule 2]

## Conventions
- [Convention 1]
- [Convention 2]
```

<!-- section_id: "e30b7aec-a34b-4e28-9e2f-916b4511d263" -->
### 4.3 OpenAI Codex

```
entity_root/
└── AGENTS.md                         # Codex agents configuration
```

<!-- section_id: "a24ff8a7-32eb-402f-8bf7-9ebd8ac2a0a8" -->
### 4.4 Gemini CLI

```
entity_root/
└── GEMINI.md                         # Gemini configuration
```

---

<!-- section_id: "48ec1dee-f753-4957-be9d-7852671ed5ab" -->
## 5. Nested Specificity Structure

The `specific/` folder allows for nested, increasingly specific configurations.

<!-- section_id: "1e22091c-0f05-4ec6-81ce-877852d820ef" -->
### 5.1 Full Structure

```
specific/
└── os/                                           # LEVEL 1: Operating System
    ├── wsl/
    │   └── environment/                          # LEVEL 2: Environment
    │       ├── local/
    │       │   └── coding_app/                   # LEVEL 3: Coding Application
    │       │       ├── cursor_ide/
    │       │       │   └── ai_app/               # LEVEL 4: AI Application
    │       │       │       ├── claude_code_cli/
    │       │       │       │   └── config.md
    │       │       │       ├── codex_cli/
    │       │       │       │   └── config.md
    │       │       │       ├── gemini_cli/
    │       │       │       │   └── config.md
    │       │       │       └── cursor_agent/
    │       │       │           └── config.md
    │       │       ├── vscode/
    │       │       │   └── ai_app/
    │       │       │       └── ...
    │       │       ├── jetbrains/
    │       │       │   └── ai_app/
    │       │       │       └── ...
    │       │       ├── rstudio/
    │       │       │   └── ai_app/
    │       │       │       └── ...
    │       │       └── terminal/
    │       │           └── ai_app/
    │       │               ├── claude_code_cli/
    │       │               ├── codex_cli/
    │       │               └── gemini_cli/
    │       └── cloud/
    │           ├── aws/
    │           │   └── coding_app/
    │           │       └── ...
    │           ├── gcp/
    │           │   └── coding_app/
    │           │       └── ...
    │           └── azure/
    │               └── coding_app/
    │                   └── ...
    ├── linux_ubuntu/
    │   └── environment/
    │       └── ...
    ├── macos/
    │   └── environment/
    │       └── ...
    └── windows/
        └── environment/
            └── ...
```

<!-- section_id: "93a76a3d-6dee-4fa8-897d-841a2a8bf88c" -->
### 5.2 Levels Explained

| Level | Folder | Options | Purpose |
|-------|--------|---------|---------|
| 1 | `os/` | wsl, linux_ubuntu, macos, windows | OS-specific configurations |
| 2 | `environment/` | local, cloud/{aws,gcp,azure} | Environment-specific |
| 3 | `coding_app/` | cursor_ide, vscode, jetbrains, rstudio, terminal | IDE-specific |
| 4 | `ai_app/` | claude_code_cli, codex_cli, gemini_cli, cursor_agent | AI tool-specific |

<!-- section_id: "ee665f74-57fd-421f-8174-7e31c50a0695" -->
### 5.3 Configuration Resolution

Navigate down through the levels to find the most specific configuration:

```
Example: WSL + Local + Terminal + Claude Code CLI

Path: specific/os/wsl/environment/local/coding_app/terminal/ai_app/claude_code_cli/

Configuration is built by:
1. Start with agnostic/init_prompt.md (base)
2. Apply os/wsl/ overrides
3. Apply environment/local/ overrides
4. Apply coding_app/terminal/ overrides
5. Apply ai_app/claude_code_cli/ overrides
```

---

<!-- section_id: "709934a6-fc42-4446-8d8a-56d065c984ab" -->
## 6. Inheritance Model

<!-- section_id: "8bb828ef-e9c0-479c-9788-e8d9f64b49db" -->
### 6.1 Agnostic → Tool-Specific

```
agnostic/init_prompt.md
        │
        ├──────────────────┬──────────────────┬──────────────────┐
        ▼                  ▼                  ▼                  ▼
   CLAUDE.md         .cursorrules        AGENTS.md         GEMINI.md
```

**Generation options:**
- **Manual sync**: Update tool files when agnostic changes
- **@import references**: Tool files reference agnostic source
- **Build script**: Generate tool files from agnostic source

<!-- section_id: "efcf9519-40ad-42c6-bde4-f1ca0604044e" -->
### 6.2 Entity Inheritance

```
Parent Entity
└── layer_N_00_ai_manager_system/
    └── agnostic/init_prompt.md
                │
                │ INHERITED BY
                ▼
Child Entity
└── layer_N+1_00_ai_manager_system/
    └── agnostic/init_prompt.md
        │
        │  References parent:
        │  "Inherited From: ../parent/init_prompt.md"
        │
        │  Adds child-specific context
        │
        ▼
    Child's own rules + Parent's rules
```

---

<!-- section_id: "f5419cfb-fb24-4e67-b45d-ec17737452ac" -->
## 7. Tool Configuration Templates

<!-- section_id: "5200304a-db6f-4c0c-adb9-204e9bd80caa" -->
### 7.1 Claude Code Settings Template

`.claude/settings.json`:
```json
{
  "permissions": {
    "allowedTools": ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
  },
  "context": {
    "includeParent": true,
    "includeChildren": false
  }
}
```

<!-- section_id: "f803b0f6-210f-4111-ac3a-e9a15aa55f95" -->
### 7.2 Claude Code Command Template

`.claude/commands/command-name.md`:
```markdown
---
name: command-name
description: What this command does
---

# Command: command-name

## Instructions
[What Claude should do when this command is invoked]

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

<!-- section_id: "5563bab0-eafd-4916-83d2-823df56abbb4" -->
### 7.3 Claude Code Agent Template

`.claude/agents/agent-name.md`:
```markdown
---
name: agent-name
description: What this agent specializes in
tools: Read, Grep, Glob
model: sonnet
---

# Agent: agent-name

## Role
[What this agent does]

## Capabilities
- [Capability 1]
- [Capability 2]

## Instructions
[How this agent should behave]
```

<!-- section_id: "0a26c4c0-6f87-485c-817c-dc21d9dc2c79" -->
### 7.4 Claude Code Skill Template

`.claude/skills/skill-name/SKILL.md`:
```markdown
---
name: skill-name
description: When to use this skill (Claude uses this to decide)
---

# Skill: skill-name

## Purpose
[What this skill helps with]

## When to Use
- [Trigger condition 1]
- [Trigger condition 2]

## Instructions
[Step-by-step instructions for Claude]

## Examples
[Example usage]
```

---

<!-- section_id: "cb712670-9983-4e34-b527-2de312bfb652" -->
## 8. Implementation at Each Entity

Every entity must have:

<!-- section_id: "26944515-15b5-4745-82c1-56a126d176ac" -->
### 8.1 At Entity Root
```
entity_root/
├── CLAUDE.md              # Required
├── .claude/               # Required
│   ├── settings.json
│   ├── commands/
│   ├── agents/
│   └── skills/
├── .cursorrules           # Required
├── AGENTS.md              # Required
├── GEMINI.md              # Required
└── .mcp.json              # Optional
```

<!-- section_id: "a478f3ba-b2b2-499a-9d37-47a8acf92653" -->
### 8.2 In layer_N/layer_N_00_ai_manager_system/
```
layer_N_00_ai_manager_system/
├── agnostic/              # Required
│   ├── init_prompt.md     # Required
│   └── ...
└── specific/              # Required (can be minimal)
    └── os/
        └── ...
```

---

<!-- section_id: "0b9abc57-4b96-4fb1-a980-71adc869058a" -->
## 9. Feature: layer_2_feature_ai_manager_hierarchy

This feature (within the layer-stage system) **defines** all of the above patterns.

```
layer_2_feature_ai_manager_hierarchy/
├── CLAUDE.md
├── layer_2/
│   └── layer_2_02_sub_layers/
│       └── sub_layer_2_05+_setup_dependant/
│           ├── sub_layer_2_05_pattern_docs/
│           │   ├── agnostic_source_pattern.md
│           │   ├── specific_nesting_pattern.md
│           │   └── tool_config_patterns.md
│           └── sub_layer_2_06_templates/
│               ├── agnostic_template/
│               └── specific_template/
└── layer_3/
    └── layer_3_components/
        ├── layer_3_component_claude_code_config/
        ├── layer_3_component_cursor_config/
        ├── layer_3_component_codex_config/
        └── layer_3_component_gemini_config/
```

---

<!-- section_id: "f3840c21-61ec-44c7-971f-905cd9d38586" -->
## 10. Success Criteria

- [ ] Every entity has `layer_N_00_ai_manager_system/`
- [ ] Every ai_manager_system has `agnostic/` and `specific/`
- [ ] Every entity has tool-specific files at root (CLAUDE.md, etc.)
- [ ] Agnostic init_prompt.md exists at every level
- [ ] Specific nesting follows os→environment→coding_app→ai_app
- [ ] Tool files are generated from/reference agnostic source
- [ ] layer_2_feature_ai_manager_hierarchy defines all patterns

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_03_instructions/hand_off_documents/INSTRUCTIONS_AI_MANAGER_HIERARCHY_SYSTEM.md`

**Last Updated:** 2026-01-15

**Related Documents:**
- `INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`
- `INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE.md`
- `INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM.md`
