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

## 1. Overview

The AI Manager Hierarchy System defines:
- Tool-agnostic source (the universal truth)
- Tool-specific implementations (CLAUDE.md, .cursorrules, etc.)
- Nested specificity (os → environment → coding_app → ai_app)

---

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

## 3. Agnostic Source

The agnostic source is the **tool-independent** source of truth.

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

## 4. Tool-Specific Implementations

Each AI tool has its own configuration file(s) at the entity root.

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

### 4.3 OpenAI Codex

```
entity_root/
└── AGENTS.md                         # Codex agents configuration
```

### 4.4 Gemini CLI

```
entity_root/
└── GEMINI.md                         # Gemini configuration
```

---

## 5. Nested Specificity Structure

The `specific/` folder allows for nested, increasingly specific configurations.

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

### 5.2 Levels Explained

| Level | Folder | Options | Purpose |
|-------|--------|---------|---------|
| 1 | `os/` | wsl, linux_ubuntu, macos, windows | OS-specific configurations |
| 2 | `environment/` | local, cloud/{aws,gcp,azure} | Environment-specific |
| 3 | `coding_app/` | cursor_ide, vscode, jetbrains, rstudio, terminal | IDE-specific |
| 4 | `ai_app/` | claude_code_cli, codex_cli, gemini_cli, cursor_agent | AI tool-specific |

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

## 6. Inheritance Model

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

## 7. Tool Configuration Templates

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

## 8. Implementation at Each Entity

Every entity must have:

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
