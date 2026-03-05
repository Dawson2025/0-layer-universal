---
resource_id: "b3d25708-391b-43f1-868f-1d5287c07eac"
resource_type: "knowledge"
resource_name: "SUB_LAYERS_AS_ENTRY_POINTS"
---
# Sub-Layers as Agent Entry Points

<!-- section_id: "bb399924-b6df-4032-8016-363c4b143265" -->
## Overview

Every sub-layer can serve as an **entry point** for AI agents. Just like layers (layer_0, layer_1, layer_2), sub-layers can have their own CLAUDE.md, 0AGNOSTIC.md, and context flow architecture.

---

<!-- section_id: "93f0b321-d2d4-4819-a14c-8342eafd7ae9" -->
## Why Sub-Layers Can Be Entry Points

Sub-layers represent **specialized domains** within a layer:
- `sub_layer_01_prompts/` - Prompt engineering domain
- `sub_layer_02_knowledge_system/` - Knowledge management domain
- `sub_layer_03_principles/` - Philosophy/principles domain
- `sub_layer_04_rules/` - Rules and protocols domain
- `sub_layer_05+_setup_dependant_hierarchy/` - Setup-specific configuration

Each domain may need its own:
- **Identity** - Who is the agent working here?
- **Rules** - What rules apply specifically here?
- **Knowledge** - What does an agent need to know?
- **Triggers** - When should this context activate?

---

<!-- section_id: "8aa44ad9-2c78-4572-ad65-b47807b53f6b" -->
## Sub-Layer Context Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SUB-LAYER AS ENTRY POINT                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER CASCADE (parent context)                                             │
│  ─────────────────────────────                                              │
│  layer_0/CLAUDE.md                                                          │
│       │                                                                     │
│       ▼                                                                     │
│  layer_1/project/CLAUDE.md                                                  │
│       │                                                                     │
│       ▼                                                                     │
│  layer_N_group/layer_N_03_sub_layers/CLAUDE.md     (sub_layers root)       │
│       │                                                                     │
│       ▼                                                                     │
│  sub_layer_N_XX_<domain>/CLAUDE.md                 (specific sub-layer)    │
│       │                                                                     │
│       │ points to                                                           │
│       ▼                                                                     │
│  sub_layer_N_XX_<domain>/.claude/                  (tool config)           │
│  sub_layer_N_XX_<domain>/.0agnostic/               (sync source)           │
│  sub_layer_N_XX_<domain>/0INDEX.md                 (contents)              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "160455b0-1273-4b3b-ad85-e60a5391d173" -->
## Sub-Layer Structure (When Used as Entry Point)

```
sub_layer_N_XX_<domain>/
├── 0AGNOSTIC.md              # Identity, triggers, pointers
├── 0INDEX.md                 # Contents and navigation
├── CLAUDE.md                 # Tool-specific context (generated)
├── .0agnostic/               # Sync source
│   ├── hooks/scripts/
│   ├── skills/
│   └── episodic/
├── .claude/                  # Tool config
│   └── settings.json
└── <domain_content>/         # Actual domain files
```

---

<!-- section_id: "d0dc902a-d003-4576-a115-6c0645dd6434" -->
## When to Make a Sub-Layer an Entry Point

<!-- section_id: "eaaf7dc9-7478-4f77-8680-e1bfe67114f9" -->
### Make It an Entry Point When:

1. **Specialized Agent Needed**
   - The domain requires specific expertise
   - Example: `sub_layer_04_rules/` needs a "Rules Specialist" agent

2. **Distinct Workflow**
   - Work in this domain follows different patterns
   - Example: `sub_layer_02_knowledge_system/` has research/documentation workflow

3. **Separate Critical Rules**
   - This domain has rules that don't apply elsewhere
   - Example: `sub_layer_05+_setup_dependant_hierarchy/` has OS-specific rules

4. **Frequent Direct Access**
   - Agents often enter directly into this sub-layer
   - Example: Direct questions about knowledge base

<!-- section_id: "e22a4040-b553-474c-b5b4-eb0b48c26340" -->
### Keep It Simple When:

1. **Content Only**
   - Just stores files, no special context needed
   - Parent layer context is sufficient

2. **Rarely Accessed Directly**
   - Only accessed through parent layer navigation
   - No need for independent identity

---

<!-- section_id: "9e3d30b8-76f3-4e3d-b463-590a28f91775" -->
## Sub-Layer CLAUDE.md Template

```markdown
# sub_layer_N_XX_<domain> - CLAUDE.md

## Identity

**Role**: [Domain specialist role]
**Scope**: [What this sub-layer contains]
**Parent**: [Parent layer path]

## [CRITICAL] Rules - EVERY API Call

⚠️ These rules MUST be followed on EVERY output in this sub-layer:

### Inherited from layer_0 (Universal)
- [ ] Always cite sources when doing research
- [ ] Show diagram before modifying AI context files
- [ ] Commit AI context changes with `[AI Context]` prefix

### Inherited from layer_N (Parent Layer)
- [ ] [Parent layer rules...]

### This Sub-Layer
- [ ] [Sub-layer specific rule 1]
- [ ] [Sub-layer specific rule 2]

## Triggers

Load this context when:
- Working with: [domain-specific topics]
- User mentions: "[relevant keywords]"
- Entering: `<path to this sub-layer>`

## Pointers

| Resource | Location |
|----------|----------|
| Tool config | `.claude/` |
| Sync source | `.0agnostic/` |
| Contents | `0INDEX.md` |
| Parent context | `../CLAUDE.md` |
```

---

<!-- section_id: "6acb3bb6-a502-44cd-bf5e-90d1f18f121d" -->
## Sub-Layer Critical Rules Cascade

```
layer_0/CLAUDE.md
├── CRITICAL RULES (universal)
│
└── layer_1/project/CLAUDE.md
    ├── INHERITS: layer_0 rules
    ├── ADDS: project rules
    │
    └── layer_1_group/layer_1_03_sub_layers/CLAUDE.md
        ├── INHERITS: layer_0 + layer_1 rules
        ├── ADDS: sub_layers root rules (if any)
        │
        └── sub_layer_1_04_rules/CLAUDE.md
            ├── INHERITS: layer_0 + layer_1 + sub_layers root rules
            └── ADDS: Rules domain specific rules
                - "All rules must have unique identifiers"
                - "Rules must specify enforcement level"
```

---

<!-- section_id: "99bc8d28-c045-4a36-a57f-51d1174853cb" -->
## Example: Knowledge System as Entry Point

```
sub_layer_0_01_knowledge_system/
├── 0AGNOSTIC.md
│   └── Identity: Knowledge System Manager
│   └── Triggers: "knowledge", "documentation", "how does X work"
│
├── CLAUDE.md
│   └── [CRITICAL] Rules:
│       - Inherited from layer_0
│       - "All knowledge must be indexed in 0INDEX.md"
│       - "Cross-reference related knowledge areas"
│
├── .claude/
│   └── settings.json
│
├── .0agnostic/
│   ├── skills/
│   │   └── knowledge_indexing.md
│   └── episodic/
│       └── sessions/
│
├── 0INDEX.md
│   └── [Master index of all knowledge areas]
│
├── layer_stage_system/
├── entity_lifecycle/
├── naming_conventions/
├── navigation_patterns/
└── context_loading/
```

---

<!-- section_id: "879161e7-b50a-46da-9d58-3aec0a3636b9" -->
## Navigation: Parent to Sub-Layer

```
Agent enters: /layer_0/

1. Loads: layer_0/CLAUDE.md (automatic)
2. Sees pointer: "Knowledge in layer_0_04_sub_layers/sub_layer_0_01_knowledge_system/"
3. Navigates to: sub_layer_0_01_knowledge_system/
4. Loads: sub_layer_0_01_knowledge_system/CLAUDE.md
5. Now has: Parent context + sub-layer specialized context
```

---

<!-- section_id: "e126e165-79d1-40fc-96e5-5f0b6783120a" -->
## Self-Check for Sub-Layer Entry Points

Before working in a sub-layer entry point:

- [ ] Did I load parent layer CLAUDE.md files?
- [ ] Did I load this sub-layer's CLAUDE.md?
- [ ] Am I following ALL inherited critical rules?
- [ ] Am I following this sub-layer's specific rules?
- [ ] Did I check 0INDEX.md for available resources?

---

*See NESTED_DEPTH_NAMING.md for subx2_, subx3_, subxN_ conventions*
*See SUB_STAGES_EXPLAINED.md for sub_stages within stages*
