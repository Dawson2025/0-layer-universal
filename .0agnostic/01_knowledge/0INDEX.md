---
resource_id: "604353dc-9ac9-4fbe-b62b-0e1f16375798"
resource_type: "index
knowledge"
resource_name: "0INDEX"
---
# AI System Knowledge Base

<!-- section_id: "551721d4-7b1e-4873-982a-80a88dba5446" -->
## Purpose

This knowledge base documents how the AI system and layer-stage framework works. AI agents should load relevant sections on-demand when they need to understand, create, or maintain system components.

<!-- section_id: "7a76b868-564e-471f-bf13-89cbad007776" -->
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

<!-- section_id: "cd8eb3cd-6f3d-48d9-b982-c559fdbc0370" -->
## Quick Start for AI Agents

<!-- section_id: "f2a3814e-b27a-4b9d-8a04-7a9e92d1c65f" -->
### New to this system?
1. Read `layer_stage_system/OVERVIEW.md` first
2. Then `entity_lifecycle/ENTITY_TYPES.md`
3. Then `context_loading/HOW_CONTEXT_WORKS.md`

<!-- section_id: "9ff45486-bfde-4bdc-8658-63b7153b7759" -->
### Need to create something?
1. Read `entity_lifecycle/INSTANTIATION_GUIDE.md`
2. Check `naming_conventions/` for correct names
3. Follow templates in `.0agnostic/templates/`

<!-- section_id: "d0676594-3c5a-4f50-b799-691fa3f16a64" -->
### Need to find something?
1. Read `navigation_patterns/TRAVERSAL_GUIDE.md`
2. Use 0INDEX.md files at each level
3. Check triggers in 0AGNOSTIC.md files

<!-- section_id: "aef4192a-532a-4adc-853c-ee058c6ab073" -->
### Need to update something?
1. Read `entity_lifecycle/MAINTENANCE_GUIDE.md`
2. Follow modification protocols in `sub_layer_0_02_rules/`

---

<!-- section_id: "f877ef46-51a5-4d02-963d-49f02f5c459b" -->
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
