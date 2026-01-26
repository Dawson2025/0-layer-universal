# System Prompt Architecture Research

**Status**: Draft - NOT ready for implementation
**Date**: 2026-01-26
**Related Needs**: rule_compliant, persistent_knowledge, discoverable
**Next Stage**: When approved, move to `stage_-1_03_instructions/outputs/`

---

## Core Principle

**System Prompt Files (CLAUDE.md, AGNOSTIC.md)** = Content that goes into EVERY API call at that scope

**Referenced Files** = Content that AI reads via tool calls when needed (NOT in every API call)

---

## What Goes INTO System Prompt Files

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         IN SYSTEM PROMPT                                │
│                    (Every API call at this scope)                       │
├─────────────────────────────────────────────────────────────────────────┤
│ • Rules that MUST be followed for every request                         │
│ • Constraints that always apply                                         │
│ • Identity/role of the agent at this level                              │
│ • Navigation instructions (how to find other things)                    │
│ • Brief context (what is this layer/stage/feature)                      │
└─────────────────────────────────────────────────────────────────────────┘
```

## What Gets REFERENCED (Not in System Prompt)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         REFERENCED FILES                                │
│                 (AI reads when situation arises)                        │
├─────────────────────────────────────────────────────────────────────────┤
│ • Detailed documentation                                                │
│ • Knowledge that's needed sometimes, not always                         │
│ • Historical context / archives                                         │
│ • Detailed explanations of rules (canonical source)                     │
│ • Setup instructions (only needed during setup)                         │
│ • Research outputs (consulted when relevant)                            │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## The Hierarchy: What Goes Where

```
0_layer_universal/CLAUDE.md
│
│  IN THIS FILE (every API call everywhere):
│  ├── Universal rules (modification protocol, commit/push, safety)
│  ├── Navigation to sub-layers and stages
│  └── Core conventions (naming, structure)
│
│  REFERENCED (not every call):
│  └── layer_0/layer_0_03_sub_layers/
│      ├── sub_layer_0_01_prompts/      → Detailed init prompts
│      ├── sub_layer_0_02_knowledge/    → Domain knowledge
│      ├── sub_layer_0_03_principles/   → Guiding principles
│      ├── sub_layer_0_04_rules/        → Canonical rule docs, detailed rules
│      └── sub_layer_0_05+_setup/       → OS/tool configuration
│
└── layer_1/layer_1_projects/layer_1_project_X/CLAUDE.md
    │
    │  IN THIS FILE (every API call in this project):
    │  ├── Project-specific rules
    │  ├── Project identity/purpose
    │  └── Navigation within project
    │
    │  REFERENCED:
    │  └── Project knowledge, docs, etc.
    │
    └── layer_2/layer_2_features/layer_2_feature_Y/CLAUDE.md
        │
        │  IN THIS FILE (every API call in this feature):
        │  ├── Feature-specific rules
        │  ├── Feature identity/purpose
        │  └── Navigation within feature
        │
        └── layer_2_99_stages/stage_02_research/CLAUDE.md
            │
            │  IN THIS FILE (every API call in this stage):
            │  ├── Stage-specific rules
            │  ├── Stage purpose and constraints
            │  └── What outputs go where
            │
            │  REFERENCED:
            │  └── outputs/, hand_off_documents/, etc.
```

---

## How Claude Code Builds the API Call

```
User is working in: stage_02_research/

Claude Code walks UP the tree, collecting CLAUDE.md files:

API Request System Prompt =
┌─────────────────────────────────────────┐
│ 0_layer_universal/CLAUDE.md             │  ← Universal rules
├─────────────────────────────────────────┤
│ layer_1_project_X/CLAUDE.md             │  ← + Project rules
├─────────────────────────────────────────┤
│ layer_2_feature_Y/CLAUDE.md             │  ← + Feature rules
├─────────────────────────────────────────┤
│ stage_02_research/CLAUDE.md             │  ← + Stage rules
└─────────────────────────────────────────┘

All of this goes into EVERY API call when working in that stage.
```

---

## Sub-Layers vs Stages vs Layers

| Concept | Purpose | Has CLAUDE.md? |
|---------|---------|----------------|
| **Sub-layers** | Content TYPES (prompts, knowledge, rules, principles, setup) | No - referenced content |
| **Stages** | Workflow PHASES (research, design, development, etc.) | Yes - stage-specific rules |
| **Layers** | Scope LEVELS (universal → project → feature → component) | Yes - scope-specific rules |

---

## The Sub-Layer Pattern

```
layer_0/layer_0_03_sub_layers/
├── sub_layer_0_01_prompts/        → Referenced for detailed prompts
├── sub_layer_0_02_knowledge/      → Referenced for domain knowledge
├── sub_layer_0_03_principles/     → Referenced for guiding principles
├── sub_layer_0_04_rules/          → CANONICAL source of rules
│   │                                 (detailed docs live here)
│   │
│   │   BUT: Universal rules get COPIED INTO root CLAUDE.md
│   │        so they're in every API call
│   │
└── sub_layer_0_05+_setup/         → Referenced for setup tasks
```

**Key insight:** `sub_layer_0_04_rules/` is the AUTHORITATIVE source, but the rules that must apply everywhere get EMBEDDED into CLAUDE.md files at the appropriate scope.

---

## Current Problem

**Current State:**
- Root CLAUDE.md says "go read rules from sub_layer_0_04_rules/"
- Rules are NOT in the system prompt
- AI must choose to read them (and might not)
- Rules not enforced if session starts outside tree

**Desired State:**
- Root CLAUDE.md CONTAINS the universal rules directly
- sub_layer_0_04_rules/ remains the canonical/detailed source
- Universal rules are in EVERY API call
- Scope-specific rules in scope-specific CLAUDE.md files

---

## Proposed Implementation (Draft)

### Root CLAUDE.md Should Contain:

1. **Universal Rules (embedded)**
   - AI Context Modification Protocol (show diagram, wait for approval)
   - AI Context Commit/Push Rule (commit and push after approved changes)
   - Core safety constraints

2. **Navigation (how to find things)**
   - Sub-layer locations
   - Stage structure
   - Quick lookup table

3. **Conventions**
   - Naming patterns
   - Structure overview

### Each Layer/Stage CLAUDE.md Should Contain:

1. **Scope-specific rules** that apply to every request at that scope
2. **Brief purpose/identity** of this layer/stage
3. **Navigation** within this scope

---

## Open Questions

1. **What specific rules should be IN the root CLAUDE.md?**
   - AI Context Modification Protocol? (full or summary?)
   - AI Context Commit/Push Rule? (full or summary?)
   - Safety governance? (which parts?)
   - Others?

2. **How to handle duplication between CLAUDE.md and sub_layer_0_04_rules/?**
   - Accept duplication, keep both in sync?
   - CLAUDE.md has summary, sub_layer has full detail?
   - Single source of truth approach?

3. **Should .claude/settings.json be involved?**
   - Currently only has permissions
   - Could it reference rules?
   - Would require Claude Code support

4. **What about sessions starting outside the tree?**
   - Still a problem even with embedded rules
   - Alias approach? Global settings?

---

## Related Research

- `rule_propagation_problem.md` - Documents the original issue
- `memory_systems.md` - CLAUDE.md as navigation guide discussion
- `existing_solutions.md` - Clawdbot's SKILL.md pattern

---

## Next Steps

1. User to clarify/correct understanding
2. User to specify which rules to embed
3. User to approve approach
4. Move to `stage_-1_03_instructions/` when ready
5. Create detailed implementation instructions
6. Execute changes following modification protocol
