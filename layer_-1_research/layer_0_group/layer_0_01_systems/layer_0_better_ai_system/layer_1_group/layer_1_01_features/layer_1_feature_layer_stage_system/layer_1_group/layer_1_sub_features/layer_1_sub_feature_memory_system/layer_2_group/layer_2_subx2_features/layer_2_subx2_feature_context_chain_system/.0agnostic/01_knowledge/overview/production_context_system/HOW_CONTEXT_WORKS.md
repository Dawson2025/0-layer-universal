---
resource_id: "69936231-d9dd-4bc8-9dbc-af3ddc773cf1"
resource_type: "knowledge"
resource_name: "HOW_CONTEXT_WORKS"
---
# How Context Loading Works

## Overview

AI agents need context to understand their role, scope, and available resources. This document explains how context is loaded and managed.

## Context Loading Mechanism

### 1. CLAUDE.md Cascade

When Claude Code starts in a directory, it walks **upward** to find CLAUDE.md files:

```
Starting in: /project/layer_2_group/layer_2_features/feature_a/

Loads (in order):
1. ~/.claude/CLAUDE.md           (global user config)
2. ~/CLAUDE.md                   (user home)
3. ~/workspace/CLAUDE.md         (workspace)
4. ~/workspace/code/CLAUDE.md    (code root)
5. .../layer_0/CLAUDE.md         (universal)
6. .../project/CLAUDE.md         (project)
7. .../feature_a/CLAUDE.md       (feature) ← Current location
```

**Each file adds context**, with more specific files having priority for conflicts.

### 2. Context Sources

| Source | Loaded | Purpose |
|--------|--------|---------|
| CLAUDE.md | Always (cascade) | Primary context |
| 0AGNOSTIC.md | On-demand | Source of truth |
| .0agnostic/ | On-demand | Detailed resources |
| sub_layer_*/ | On-demand | Rules, knowledge, prompts |

### 3. Always-Loaded vs On-Demand

**Always-Loaded** (keep small!):
- CLAUDE.md - Main context file
- Identity, role, scope
- Key triggers
- Critical rules

**On-Demand** (load when needed):
- Detailed rules from sub_layer_04_rules/
- Knowledge from sub_layer_02_knowledge_system/
- Prompts from sub_layer_01_prompts/
- Setup-specific content from sub_layer_05+/

---

## The Agnostic System

### Three-Tier Architecture

```
┌─────────────────────────────────────────┐
│          0AGNOSTIC.md                   │  Source of truth
│    (tool-agnostic identity)             │  Edit this one
└─────────────────┬───────────────────────┘
                  │
                  ▼ agnostic-sync.sh
┌─────────────────────────────────────────┐
│         .0agnostic/                     │  Detailed config
│    (on-demand resources)                │  Skills, hooks, agents
└─────────────────┬───────────────────────┘
                  │
                  ▼ generates
┌─────────────────────────────────────────┐
│   CLAUDE.md  .cursorrules  GEMINI.md    │  Tool-specific
│   AGENTS.md  copilot-instructions.md    │  Auto-generated
└─────────────────────────────────────────┘
```

### 0AGNOSTIC.md Structure

```markdown
# 0AGNOSTIC.md - <entity_name>

## Identity
- Role, scope, parent, children

## Triggers
- When to load this context

## Pointers
- Where to find detailed resources
```

### .0agnostic/ Structure

```
.0agnostic/
├── hooks/scripts/       # Automation scripts
├── skills/              # Loadable skills
├── agents/              # Agent definitions
└── episodic/            # Session memory
    ├── sessions/        # Session logs
    └── changes/         # Change logs
```

---

## Trigger-Based Loading

### What Are Triggers?

Triggers tell AI agents when to load specific context:

```markdown
## Triggers

Load this context when:
- User mentions: "auth system", "login", "authentication"
- Working on: security features, user management
- Entering: `/layer_1_project_app/layer_2_features/layer_2_feature_auth/`
```

### Trigger Types

| Type | Example | When Activated |
|------|---------|----------------|
| Keyword | "auth system" | User says these words |
| Activity | "security features" | Working on this type of task |
| Path | `/path/to/entity/` | Entering this directory |

### Trigger Hierarchy

More specific triggers override general ones:
```
layer_0 triggers (general)
  → layer_1 triggers (project-specific)
    → layer_2 triggers (feature-specific)  ← Most specific wins
```

---

## Context Inheritance

### How Inheritance Works

Child entities inherit from parents:

```
layer_0 (universal)
├── Rules: All rules apply everywhere
├── Knowledge: Available to all
└── Principles: Guide all decisions

  └── layer_1 (project)
      ├── Inherits: All of layer_0
      ├── Adds: Project-specific rules
      └── Overrides: None (additive)

        └── layer_2 (feature)
            ├── Inherits: layer_0 + layer_1
            ├── Adds: Feature-specific config
            └── Can reference: Parent knowledge
```

### What Inherits

| Content Type | Inherits? | Notes |
|--------------|-----------|-------|
| Rules | Yes | All rules cascade down |
| Knowledge | Reference | Load on-demand from parent |
| Prompts | No | Entity-specific |
| Identity | No | Each entity has own identity |

---

## Best Practices

### Keep CLAUDE.md Small

```markdown
# Good: ~100-300 lines
- Identity (who am I)
- Key triggers (when to activate)
- Critical rules (must-follow)
- Pointers (where to find more)

# Bad: 1000+ lines
- Full documentation
- All rules inline
- Detailed examples
- Historical information
```

### Use Pointers

```markdown
## Pointers

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Full rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge base | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge/` |
```

### Layer Your Context

```
Always loaded:     Identity, critical rules, triggers
Sometimes loaded:  Project rules, feature config
Rarely loaded:     Detailed knowledge, archived docs
```

---

## Debugging Context Issues

### Context Not Loading?

1. Check CLAUDE.md exists and has correct path
2. Verify file is valid markdown
3. Check for syntax errors
4. Verify parent CLAUDE.md files exist

### Wrong Context Loading?

1. Check triggers in 0AGNOSTIC.md
2. Verify you're in the right directory
3. Check for conflicting triggers in parents

### Context Too Large?

1. Move details to .0agnostic/ or sub_layers
2. Use pointers instead of inline content
3. Split into multiple documents

---

*See AGNOSTIC_SYSTEM.md for detailed agnostic architecture*
