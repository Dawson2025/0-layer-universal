---
resource_id: "72083449-6509-4292-b8b2-b24fcd498b38"
resource_type: "knowledge"
resource_name: "INSTRUCTIONS_AI_MANAGER_HIERARCHY_SYSTEM"
---
# INSTRUCTIONS: AI Manager Hierarchy System

**Created:** 2026-01-15
**Status:** Instructions Complete
**Purpose:** Define the agnostic/specific pattern for AI tool configurations

---

<!-- section_id: "f51829b0-8410-4066-8d86-ff4250ecd3bc" -->
## 1. Overview

The AI Manager Hierarchy System defines:
- Tool-agnostic source (the universal truth)
- Tool-specific implementations (CLAUDE.md, .cursorrules, etc.)
- Nested specificity (os → environment → coding_app → ai_app)

---

<!-- section_id: "d0853b45-5d5d-4dea-9f52-09aea0847823" -->
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

<!-- section_id: "16183540-2077-417a-9992-5b9c638105a8" -->
## 3. Agnostic Source

The agnostic source is the **tool-independent** source of truth.

<!-- section_id: "8b990a99-aedb-4186-b598-d082be931472" -->
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

<!-- section_id: "f0ea6985-9e19-49d8-b229-87af47af3d8f" -->
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

<!-- section_id: "fc8571f9-0957-4865-89bb-0d4c69f8bd42" -->
## 4. Tool-Specific Implementations

Each AI tool has its own configuration file(s) at the entity root.

<!-- section_id: "4c61026b-9c4a-4ad7-ac9b-de58458f16e8" -->
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

<!-- section_id: "62b5a5cf-5ef6-45fe-bf14-f0f2872c7183" -->
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

<!-- section_id: "52dfde0d-ac76-4833-9d98-c6933b2a5d23" -->
### 4.3 OpenAI Codex

```
entity_root/
└── AGENTS.md                         # Codex agents configuration
```

<!-- section_id: "c4ceeb30-2305-4ce9-95f8-ee53abbb320e" -->
### 4.4 Gemini CLI

```
entity_root/
└── GEMINI.md                         # Gemini configuration
```

---

<!-- section_id: "356afcb6-1db5-484b-96be-f7ba05401fa8" -->
## 5. Nested Specificity Structure

The `specific/` folder allows for nested, increasingly specific configurations.

<!-- section_id: "7ef6c5ba-1f53-48a8-8e30-1566a6b32f7c" -->
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

<!-- section_id: "a9d22bd1-dbd0-478b-b6e4-ef3c1aec3164" -->
### 5.2 Levels Explained

| Level | Folder | Options | Purpose |
|-------|--------|---------|---------|
| 1 | `os/` | wsl, linux_ubuntu, macos, windows | OS-specific configurations |
| 2 | `environment/` | local, cloud/{aws,gcp,azure} | Environment-specific |
| 3 | `coding_app/` | cursor_ide, vscode, jetbrains, rstudio, terminal | IDE-specific |
| 4 | `ai_app/` | claude_code_cli, codex_cli, gemini_cli, cursor_agent | AI tool-specific |

<!-- section_id: "64bf97d1-d567-4173-bf5e-f2f2e0436633" -->
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

<!-- section_id: "3f6a08c1-c6af-463c-904e-1d19770bd87a" -->
## 6. Inheritance Model

<!-- section_id: "85f7d3e8-f0e9-4783-936c-89aacbe11e69" -->
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

<!-- section_id: "37bc2c27-1faf-43bf-81cc-1b4699fbea23" -->
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

<!-- section_id: "132be7ce-cfeb-4bc8-acc8-77cc84b8d04e" -->
## 7. Tool Configuration Templates

<!-- section_id: "1a6fe7f3-aa19-4553-8020-4c8934054feb" -->
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

<!-- section_id: "a9b5deb5-b44d-44ac-81b2-91b46ad92646" -->
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

<!-- section_id: "21dcacba-2652-457f-8d0a-ad88cd204977" -->
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

<!-- section_id: "53d45ff9-2635-460a-a117-dd448cc854d3" -->
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

<!-- section_id: "19119291-a0ce-489d-8be6-3ac41ac375a0" -->
## 8. Implementation at Each Entity

Every entity must have:

<!-- section_id: "55db3521-38d7-4ff6-9121-a86b247a52bb" -->
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

<!-- section_id: "6f6d9b90-2a16-41b4-a044-1d3e6fdd0866" -->
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

<!-- section_id: "531607f6-ae54-49a8-a82f-7353d78bd700" -->
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

<!-- section_id: "07aedbb6-c8ce-4fd6-9bfd-95068f0a0b58" -->
## 10. Success Criteria

- [ ] Every entity has `layer_N_00_ai_manager_system/`
- [ ] Every ai_manager_system has `agnostic/` and `specific/`
- [ ] Every entity has tool-specific files at root (CLAUDE.md, etc.)
- [ ] Agnostic init_prompt.md exists at every level
- [ ] Specific nesting follows os→environment→coding_app→ai_app
- [ ] Tool files are generated from/reference agnostic source
- [ ] layer_2_feature_ai_manager_hierarchy defines all patterns

---

**Document Location:** `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_1/layer_1_features/layer_1_feature_layer_stage_system/stages/stage_0_01_instructions/hand_off_documents/INSTRUCTIONS_AI_MANAGER_HIERARCHY_SYSTEM.md`

**Last Updated:** 2026-01-15

**Related Documents:**
- `INSTRUCTIONS_LAYER_STAGE_RESTRUCTURE.md`
- `INSTRUCTIONS_LAYER_STAGE_SYSTEM_INTERNAL_STRUCTURE.md`
- `INSTRUCTIONS_CONTEXT_GATHERING_SYSTEM.md`
