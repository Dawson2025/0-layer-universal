# AI System Knowledge Base

## Purpose

This knowledge base documents how the AI system and layer-stage framework works. AI agents should load relevant sections on-demand when they need to understand, create, or maintain system components.

## Knowledge Areas

| Area | Purpose | When to Load |
|------|---------|--------------|
| [Layer-Stage System](layer_stage_system/) | Core framework architecture | Understanding system structure |
| [Entity Lifecycle](entity_lifecycle/) | Create, maintain, update, archive | Creating or modifying entities |
| [Naming Conventions](naming_conventions/) | Suffixes, prefixes, patterns | Naming anything |
| [Navigation Patterns](navigation_patterns/) | How to traverse the system | Finding or loading content |
| [Context Loading](context_loading/) | CLAUDE.md, 0AGNOSTIC.md, triggers | Setting up agent context |
| [Agent Coordination](agent_coordination/) | Scope vs delegation, multi-agent patterns | Working across layers/stages |
| [AALang & GAB System](aalang_gab_system/) | Mode-Actor pattern, GAB compiler, agent patterns | Understanding or creating AALang agents |

---

## Quick Start for AI Agents

### New to this system?
1. Read `layer_stage_system/OVERVIEW.md` first
2. Then `entity_lifecycle/ENTITY_TYPES.md`
3. Then `context_loading/HOW_CONTEXT_WORKS.md`

### Need to create something?
1. Read `entity_lifecycle/INSTANTIATION_GUIDE.md`
2. Check `naming_conventions/` for correct names
3. Follow templates in `.0agnostic/templates/`

### Need to find something?
1. Read `navigation_patterns/TRAVERSAL_GUIDE.md`
2. Use 0INDEX.md files at each level
3. Check triggers in 0AGNOSTIC.md files

### Need to update something?
1. Read `entity_lifecycle/MAINTENANCE_GUIDE.md`
2. Follow modification protocols in `sub_layer_0_02_rules/`

---

## Knowledge Map

```
sub_layer_0_01_knowledge_system/
├── 0INDEX.md                          ← You are here
├── AI_CONTEXT_FLOW_ARCHITECTURE.md    ← Master architecture doc
├── layer_stage_system/                ← Core framework
│   ├── OVERVIEW.md                    ← Start here
│   ├── LAYERS_EXPLAINED.md
│   ├── STAGES_EXPLAINED.md
│   ├── SUB_LAYERS_EXPLAINED.md
│   ├── SUB_LAYERS_AS_ENTRY_POINTS.md  ← Sub-layers as agent entry points
│   ├── NESTED_DEPTH_NAMING.md         ← subxN naming conventions
│   ├── SUB_STAGES_EXPLAINED.md        ← Sub-stages and subxN_stages
│   └── GROUP_VS_HIERARCHY.md
├── entity_lifecycle/                  ← CRUD operations
│   ├── ENTITY_TYPES.md
│   ├── INSTANTIATION_GUIDE.md
│   ├── MAINTENANCE_GUIDE.md
│   └── ARCHIVAL_GUIDE.md
├── naming_conventions/                ← Naming rules
│   ├── FOLDER_SUFFIX_RULES.md
│   ├── HIERARCHY_NAMING_CONVENTION.md
│   └── NUMBERING_PATTERNS.md
├── navigation_patterns/               ← Finding things
│   ├── TRAVERSAL_GUIDE.md
│   ├── INDEX_SYSTEM.md
│   └── CONTEXT_CASCADE.md
├── context_loading/                   ← Agent setup
│   ├── HOW_CONTEXT_WORKS.md
│   ├── AGNOSTIC_SYSTEM.md
│   └── TRIGGER_PATTERNS.md
├── agent_coordination/                ← Multi-agent work
│   ├── SCOPE_VS_DELEGATION.md         ← When to expand vs delegate
│   ├── HANDOFF_PROTOCOLS.md           ← Agent-to-agent communication
│   └── MULTI_AGENT_PATTERNS.md        ← Coordination patterns
└── aalang_gab_system/                 ← AALang & GAB reference
    ├── README.md                      ← Overview & key concepts
    ├── mode_actor_pattern.md          ← Core execution pattern
    ├── gab_compiler.md                ← How GAB creates agents
    ├── runtime_and_formats.md         ← Runtime behaviors & output formats
    └── agent_patterns.md              ← 4-mode, 5-mode pattern reference
```

---

*Master index for AI system knowledge*
