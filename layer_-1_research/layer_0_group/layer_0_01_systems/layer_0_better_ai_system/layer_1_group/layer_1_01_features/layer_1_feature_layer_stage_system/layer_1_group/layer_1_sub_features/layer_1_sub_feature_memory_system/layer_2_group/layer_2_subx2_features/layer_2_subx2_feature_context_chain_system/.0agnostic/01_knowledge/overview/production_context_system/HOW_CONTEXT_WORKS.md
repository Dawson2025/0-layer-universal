---
resource_id: "69936231-d9dd-4bc8-9dbc-af3ddc773cf1"
resource_type: "knowledge"
resource_name: "HOW_CONTEXT_WORKS"
---
# How Context Loading Works

<!-- section_id: "9f844342-9ca3-4bd6-ad71-1e3be51d82c6" -->
## Overview

AI agents need context to understand their role, scope, and available resources. This document explains how context is loaded and managed.

<!-- section_id: "715d2bb9-755d-4eff-8d36-da0af8f3f4ef" -->
## Context Loading Mechanism

<!-- section_id: "11d4f1ec-0c14-4b18-a133-c94d4e1cc843" -->
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

<!-- section_id: "d4d74cd4-056d-40ef-8254-58b2b0c9f109" -->
### 2. Context Sources

| Source | Loaded | Purpose |
|--------|--------|---------|
| CLAUDE.md | Always (cascade) | Primary context |
| 0AGNOSTIC.md | On-demand | Source of truth |
| .0agnostic/ | On-demand | Detailed resources |
| sub_layer_*/ | On-demand | Rules, knowledge, prompts |

<!-- section_id: "0074a54c-22e2-4ef4-a64f-d5f4343f6ab1" -->
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

<!-- section_id: "cecce893-cfc8-41d7-90e3-b5448ef7842f" -->
## The Agnostic System

<!-- section_id: "ae4e95e9-b92e-4ee4-8c2d-7db1267bf871" -->
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

<!-- section_id: "b2bd7e34-e8df-4703-927e-2d9afc9d4995" -->
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

<!-- section_id: "656c9d96-72c2-473b-b268-27eb4822ecdb" -->
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

<!-- section_id: "82a71b43-6973-4128-834c-753f63b501f9" -->
## Trigger-Based Loading

<!-- section_id: "9e860258-b6ca-4005-8da1-54aa5515f5a2" -->
### What Are Triggers?

Triggers tell AI agents when to load specific context:

```markdown
## Triggers

Load this context when:
- User mentions: "auth system", "login", "authentication"
- Working on: security features, user management
- Entering: `/layer_1_project_app/layer_2_features/layer_2_feature_auth/`
```

<!-- section_id: "9968bd96-799e-4074-8abb-c4cc12f76f82" -->
### Trigger Types

| Type | Example | When Activated |
|------|---------|----------------|
| Keyword | "auth system" | User says these words |
| Activity | "security features" | Working on this type of task |
| Path | `/path/to/entity/` | Entering this directory |

<!-- section_id: "a9185a6a-a812-4fd7-8c3f-d1f93adbb33d" -->
### Trigger Hierarchy

More specific triggers override general ones:
```
layer_0 triggers (general)
  → layer_1 triggers (project-specific)
    → layer_2 triggers (feature-specific)  ← Most specific wins
```

---

<!-- section_id: "9bbcf5af-55ec-4c98-a831-6ac12e846ea9" -->
## Context Inheritance

<!-- section_id: "14dfc975-a0b8-4e55-95e8-e4d604ab8abc" -->
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

<!-- section_id: "a3bbeb1f-5ec9-4557-b676-89e50c19c09b" -->
### What Inherits

| Content Type | Inherits? | Notes |
|--------------|-----------|-------|
| Rules | Yes | All rules cascade down |
| Knowledge | Reference | Load on-demand from parent |
| Prompts | No | Entity-specific |
| Identity | No | Each entity has own identity |

---

<!-- section_id: "fc333870-1601-457a-845b-4e283ab0612a" -->
## Best Practices

<!-- section_id: "30bad8aa-795a-48ee-b39d-0c99b7cface8" -->
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

<!-- section_id: "a94b89d6-79d0-4262-a576-feea0a24fde5" -->
### Use Pointers

```markdown
## Pointers

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Full rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge base | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge/` |
```

<!-- section_id: "3e38357e-7936-4b8b-97f6-bed0fea59bd7" -->
### Layer Your Context

```
Always loaded:     Identity, critical rules, triggers
Sometimes loaded:  Project rules, feature config
Rarely loaded:     Detailed knowledge, archived docs
```

---

<!-- section_id: "617eb0f0-19dd-4396-a53d-64c725f1512c" -->
## Debugging Context Issues

<!-- section_id: "c498b910-627d-4c19-8c3a-d4f0cbdff3d4" -->
### Context Not Loading?

1. Check CLAUDE.md exists and has correct path
2. Verify file is valid markdown
3. Check for syntax errors
4. Verify parent CLAUDE.md files exist

<!-- section_id: "90a42d07-38a2-4c4c-a3b5-aba4f7853000" -->
### Wrong Context Loading?

1. Check triggers in 0AGNOSTIC.md
2. Verify you're in the right directory
3. Check for conflicting triggers in parents

<!-- section_id: "8e3536a1-71b3-4302-b77a-f3c5c145115d" -->
### Context Too Large?

1. Move details to .0agnostic/ or sub_layers
2. Use pointers instead of inline content
3. Split into multiple documents

---

*See AGNOSTIC_SYSTEM.md for detailed agnostic architecture*
