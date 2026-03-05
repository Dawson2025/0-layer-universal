---
resource_id: "de28acac-3c74-4859-a1b2-e66c61c22fa5"
resource_type: "knowledge"
resource_name: "HOW_CONTEXT_WORKS"
---
# How Context Loading Works

<!-- section_id: "eb68f92a-6a67-4491-86ef-0f32174e11c9" -->
## Overview

AI agents need context to understand their role, scope, and available resources. This document explains how context is loaded and managed.

<!-- section_id: "b5ad4e3f-f506-4d52-b6cc-3fa76ba7d07e" -->
## Context Loading Mechanism

<!-- section_id: "e248c1b4-b6d0-4776-b65a-005eb4c5329e" -->
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

<!-- section_id: "7e335f47-f6b6-42f5-a29b-79cfbfe68782" -->
### 2. Context Sources

| Source | Loaded | Purpose |
|--------|--------|---------|
| CLAUDE.md | Always (cascade) | Primary context |
| 0AGNOSTIC.md | On-demand | Source of truth |
| .0agnostic/ | On-demand | Detailed resources |
| sub_layer_*/ | On-demand | Rules, knowledge, prompts |

<!-- section_id: "ce2ec3a2-f42d-4b46-bd97-6a7586417f3b" -->
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

<!-- section_id: "fd2c7c0a-4055-4046-b0c2-61f059a8fbac" -->
## The Agnostic System

<!-- section_id: "cb4e1a2e-912f-42ed-a2e3-a97f805f5947" -->
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

<!-- section_id: "3fadfb96-7e78-4f18-923f-46f136172b78" -->
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

<!-- section_id: "5594d97a-75f9-4113-9696-090752fad319" -->
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

<!-- section_id: "59066eb6-bc74-466b-82fa-fc8fab260463" -->
## Trigger-Based Loading

<!-- section_id: "aa6033db-6285-4bfe-84c4-2409be00c9c9" -->
### What Are Triggers?

Triggers tell AI agents when to load specific context:

```markdown
## Triggers

Load this context when:
- User mentions: "auth system", "login", "authentication"
- Working on: security features, user management
- Entering: `/layer_1_project_app/layer_2_features/layer_2_feature_auth/`
```

<!-- section_id: "b69b9951-5434-4dd8-a21d-86dd8bb8d2dc" -->
### Trigger Types

| Type | Example | When Activated |
|------|---------|----------------|
| Keyword | "auth system" | User says these words |
| Activity | "security features" | Working on this type of task |
| Path | `/path/to/entity/` | Entering this directory |

<!-- section_id: "432dd1ed-d5db-4046-b2de-44bbf44f7886" -->
### Trigger Hierarchy

More specific triggers override general ones:
```
layer_0 triggers (general)
  → layer_1 triggers (project-specific)
    → layer_2 triggers (feature-specific)  ← Most specific wins
```

---

<!-- section_id: "7b88aad0-0e5e-45b1-99e9-28a40607a036" -->
## Context Inheritance

<!-- section_id: "daaf2103-a6d7-472b-a17f-d9cb429d9b33" -->
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

<!-- section_id: "ac78660e-6516-4545-be29-2584bd32d9c0" -->
### What Inherits

| Content Type | Inherits? | Notes |
|--------------|-----------|-------|
| Rules | Yes | All rules cascade down |
| Knowledge | Reference | Load on-demand from parent |
| Prompts | No | Entity-specific |
| Identity | No | Each entity has own identity |

---

<!-- section_id: "52620dda-deea-47ea-a7b9-77fc3c549c1d" -->
## Best Practices

<!-- section_id: "3876c645-34db-4bc3-8b84-561e63f93ca2" -->
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

<!-- section_id: "b035533b-cd24-47dd-9a9d-f3a910af2dde" -->
### Use Pointers

```markdown
## Pointers

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Full rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge base | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge/` |
```

<!-- section_id: "eabe6c38-f53f-44f3-a119-5c20e3ab216e" -->
### Layer Your Context

```
Always loaded:     Identity, critical rules, triggers
Sometimes loaded:  Project rules, feature config
Rarely loaded:     Detailed knowledge, archived docs
```

---

<!-- section_id: "b224e819-c5a4-47bb-8ba5-e301847b1cd4" -->
## Debugging Context Issues

<!-- section_id: "52a0fd96-a70d-4748-b5ca-87a793bbc3b2" -->
### Context Not Loading?

1. Check CLAUDE.md exists and has correct path
2. Verify file is valid markdown
3. Check for syntax errors
4. Verify parent CLAUDE.md files exist

<!-- section_id: "14fbcdcb-88b9-4487-94f0-f2828a96c471" -->
### Wrong Context Loading?

1. Check triggers in 0AGNOSTIC.md
2. Verify you're in the right directory
3. Check for conflicting triggers in parents

<!-- section_id: "6f4236bb-a801-406e-848d-348f3940c11c" -->
### Context Too Large?

1. Move details to .0agnostic/ or sub_layers
2. Use pointers instead of inline content
3. Split into multiple documents

---

*See AGNOSTIC_SYSTEM.md for detailed agnostic architecture*
