---
resource_id: "c617bd1c-374a-499c-9163-7a0bedddd412"
resource_type: "knowledge"
resource_name: "HOW_CONTEXT_WORKS"
---
# How Context Loading Works

<!-- section_id: "2f2821ee-1fd0-4cd6-b5d3-a0e3b9449d0e" -->
## Overview

AI agents need context to understand their role, scope, and available resources. This document explains how context is loaded and managed.

<!-- section_id: "29ad51e0-40f9-4f24-97bb-1e75f3a117f9" -->
## Context Loading Mechanism

<!-- section_id: "61a311e7-537f-4e35-98f8-b35711725189" -->
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

<!-- section_id: "078d488d-51f6-4ed3-ade7-c7bafff5c9a3" -->
### 2. Context Sources

| Source | Loaded | Purpose |
|--------|--------|---------|
| CLAUDE.md | Always (cascade) | Primary context |
| 0AGNOSTIC.md | On-demand | Source of truth |
| .0agnostic/ | On-demand | Detailed resources |
| sub_layer_*/ | On-demand | Rules, knowledge, prompts |

<!-- section_id: "a2f65176-c46b-4bd8-ad88-53a67ae9e0e3" -->
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

<!-- section_id: "ae9816b3-ae29-4995-bdd1-568a1b5e5b3b" -->
## The Agnostic System

<!-- section_id: "c7c64549-9b35-424a-b0cb-80b0ac3aaf44" -->
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

<!-- section_id: "0e693c55-0928-48bc-bb84-e7402211f266" -->
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

<!-- section_id: "c1162504-fc24-41a7-b21f-149bd1d9f173" -->
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

<!-- section_id: "b2ce4b89-579e-474b-a9c9-63ae947a53c5" -->
## Trigger-Based Loading

<!-- section_id: "ed20132e-3532-4ce4-b83f-c65e49b491c3" -->
### What Are Triggers?

Triggers tell AI agents when to load specific context:

```markdown
## Triggers

Load this context when:
- User mentions: "auth system", "login", "authentication"
- Working on: security features, user management
- Entering: `/layer_1_project_app/layer_2_features/layer_2_feature_auth/`
```

<!-- section_id: "27f35de0-3a76-424c-a287-ec2fe86d35c8" -->
### Trigger Types

| Type | Example | When Activated |
|------|---------|----------------|
| Keyword | "auth system" | User says these words |
| Activity | "security features" | Working on this type of task |
| Path | `/path/to/entity/` | Entering this directory |

<!-- section_id: "e8559ccc-4632-4ba6-aaff-c58de9067754" -->
### Trigger Hierarchy

More specific triggers override general ones:
```
layer_0 triggers (general)
  → layer_1 triggers (project-specific)
    → layer_2 triggers (feature-specific)  ← Most specific wins
```

---

<!-- section_id: "060cc9f1-f126-4fab-89ce-960ecc1a08c2" -->
## Context Inheritance

<!-- section_id: "6a268f37-014c-4beb-9532-4f124a8a972a" -->
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

<!-- section_id: "7e90109b-5ff8-4e58-8a57-27472f3220c8" -->
### What Inherits

| Content Type | Inherits? | Notes |
|--------------|-----------|-------|
| Rules | Yes | All rules cascade down |
| Knowledge | Reference | Load on-demand from parent |
| Prompts | No | Entity-specific |
| Identity | No | Each entity has own identity |

---

<!-- section_id: "33392bce-16a4-4b10-81c6-726a39c4cf36" -->
## Best Practices

<!-- section_id: "0a98e475-678a-4690-b612-3020dd32f05e" -->
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

<!-- section_id: "2f849772-5dd7-4ef8-b83f-25ce487d28ae" -->
### Use Pointers

```markdown
## Pointers

### Resources (load on-demand)
| Resource | Location |
|----------|----------|
| Full rules | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_04_rules/` |
| Knowledge base | `layer_N_group/layer_N_03_sub_layers/sub_layer_N_02_knowledge/` |
```

<!-- section_id: "88503155-538f-4e55-9ed1-edaae5eeafef" -->
### Layer Your Context

```
Always loaded:     Identity, critical rules, triggers
Sometimes loaded:  Project rules, feature config
Rarely loaded:     Detailed knowledge, archived docs
```

---

<!-- section_id: "0832fd33-9cb4-4963-9d9b-d5f08f74b8ca" -->
## Debugging Context Issues

<!-- section_id: "ce60c71d-9cd0-4fb3-a770-c621b5ab3067" -->
### Context Not Loading?

1. Check CLAUDE.md exists and has correct path
2. Verify file is valid markdown
3. Check for syntax errors
4. Verify parent CLAUDE.md files exist

<!-- section_id: "d4f50319-0006-40e9-8a5e-df317c7af314" -->
### Wrong Context Loading?

1. Check triggers in 0AGNOSTIC.md
2. Verify you're in the right directory
3. Check for conflicting triggers in parents

<!-- section_id: "e31399d7-e686-4e28-93bd-471550de586f" -->
### Context Too Large?

1. Move details to .0agnostic/ or sub_layers
2. Use pointers instead of inline content
3. Split into multiple documents

---

*See AGNOSTIC_SYSTEM.md for detailed agnostic architecture*
