# Custom Layer-Stage Context Loading

**Purpose**: Document how our layer-stage system extends Claude Code's official context loading with custom conventions, navigation, and triggers.

---

## Architecture: Official + Custom

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│               HOW OUR SYSTEM EXTENDS CLAUDE CODE                                 │
└─────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  CLAUDE CODE (Official)                                                    ║
    ║  ════════════════════════                                                  ║
    ║                                                                            ║
    ║  Auto-loads:                                                               ║
    ║  • System prompt                                                           ║
    ║  • Tools + MCP servers                                                     ║
    ║  • ~/.claude/CLAUDE.md                                                     ║
    ║  • All CLAUDE.md files from ~ to working directory                         ║
    ║  • .claude/settings.json                                                   ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
                    │
                    │ Our CLAUDE.md files contain instructions that tell
                    │ agent to load additional context
                    │
                    ▼
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  OUR CUSTOM LAYER (via CLAUDE.md instructions)                             ║
    ║  ═════════════════════════════════════════════                             ║
    ║                                                                            ║
    ║  CLAUDE.md files instruct agent to read:                                   ║
    ║  • index.jsonld (navigation, conventions, triggers)                        ║
    ║  • .claude/skills/*/SKILL.md (procedures)                                  ║
    ║  • .claude/schema/*.jsonld (type definitions)                              ║
    ║  • sub_layer files (rules, knowledge, principles)                          ║
    ║  • status.json (current state)                                             ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## Custom Loading Sequence (Full)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│         CUSTOM LAYER-STAGE CONTEXT LOADING                                       │
│         (Working Directory: .../layer_0_group/)                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE A: CLAUDE CODE OFFICIAL (Auto-loaded)
    ════════════════════════════════════════════════════════════════════════════

    ORDER 1: System Prompt [OFFICIAL]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Anthropic's system prompt                                                │
    │  Contains: Git Safety Protocol, tool instructions, security rules         │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ORDER 2: Tools + MCP [OFFICIAL]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Built-in tools + MCP servers from ~/.claude/settings.json                │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ORDER 3: ~/.claude/CLAUDE.md [OFFICIAL + OUR CONTENT]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CUSTOM CONTENT:                                                │  │
    │  │                                                                     │  │
    │  │  [CRITICAL] 1. AI Context Modification Protocol                     │  │
    │  │  [CRITICAL] 2. AI Context Commit/Push Rule                          │  │
    │  │  [CRITICAL] 3. Context Traversal Rule ← KEY INSTRUCTION             │  │
    │  │  [CRITICAL] 4. AI Documentation Protocol                            │  │
    │  │  [CRITICAL] 5. Research and Sources Practice                        │  │
    │  │  [CRITICAL] 6. File Path Linking Rule                               │  │
    │  │                                                                     │  │
    │  │  Context Traversal Rule tells agent:                                │  │
    │  │  • "Read all CLAUDE.md files in path"                               │  │
    │  │  • "Identify current layer and stage"                               │  │
    │  │  • "Check relevant sub_layers"                                      │  │
    │  │  • "Read status.json if exists"                                     │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ORDER 4-N: Path CLAUDE.md Files [OFFICIAL + OUR CONTENT]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │                                                                           │
    │  ~/CLAUDE.md                                                              │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: User root, workspace pointers, same critical rules    │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                     │                                     │
    │                                     ▼                                     │
    │  ~/dawson-workspace/CLAUDE.md                                             │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: Sync awareness, code location                         │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                     │                                     │
    │                                     ▼                                     │
    │  .../code/CLAUDE.md                                                       │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: Code root, points to 0_layer_universal                │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                     │                                     │
    │                                     ▼                                     │
    │  .../0_layer_universal/CLAUDE.md                                          │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: Root Manager role                                     │  │
    │  │  • Layer-stage framework explanation                                │  │
    │  │  • Navigation guide (sub_layers, stages)                            │  │
    │  │  • "Read sub_layer_0_04_rules/ for universal rules"                 │  │
    │  │  • Session workflow instructions                                    │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                     │                                     │
    │                                     ▼                                     │
    │  .../layer_-1_research/CLAUDE.md                                          │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: Research layer context                                │  │
    │  │  • "Load rules from ../layer_0/"                                    │  │
    │  │  • Triggers for different situations                                │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                     │                                     │
    │                                     ▼                                     │
    │  .../layer_-1_better_ai_system/CLAUDE.md                                  │
    │  ┌─────────────────────────────────────────────────────────────────────┐  │
    │  │  OUR CONTENT: Project context                                       │  │
    │  │  • Layer -1, Project: better_ai_system                              │  │
    │  │  • Features location                                                │  │
    │  │  • Load triggers                                                    │  │
    │  └─────────────────────────────────────────────────────────────────────┘  │
    │                                                                           │
    └───────────────────────────────────────────────────────────────────────────┘

    ════════════════════════════════════════════════════════════════════════════
    PHASE B: OUR CUSTOM LAYER (Agent-Driven, Instructed by CLAUDE.md)
    ════════════════════════════════════════════════════════════════════════════

    Agent follows instructions from CLAUDE.md files to load additional context:

    ORDER N+1: index.jsonld [OUR CUSTOM FILE]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  CLAUDE.md says: "For navigation, read index.jsonld"                      │
    │                                                                           │
    │  Agent READs: .../layer_0_group/index.jsonld                              │
    │                                                                           │
    │  FINDS:                                                                   │
    │  • @type: "FeaturesGroup"                                                 │
    │  • nav:parent, nav:children (navigation graph)                            │
    │  • conventions.childNaming (naming rules)                                 │
    │  • trigger:onEntityCreation → skill path                                  │
    │  • rel:treeOfNeedsBranch (requirements link)                              │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    │ If agent is creating an entity, trigger fires
                    │
                    ▼
    ORDER N+2: SKILL.md [OUR CUSTOM FILE]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  trigger:onEntityCreation says: load ".claude/skills/entity-creation/"    │
    │                                                                           │
    │  Agent READs: .../layer_0_group/.claude/skills/entity-creation/SKILL.md   │
    │                                                                           │
    │  FINDS:                                                                   │
    │  • Naming pattern rules                                                   │
    │  • Layer hierarchy explanation                                            │
    │  • Checklist for entity creation                                          │
    │  • Common mistakes table                                                  │
    │  • "See schema for entityTypes"                                           │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    │ Skill references schema
                    │
                    ▼
    ORDER N+3: schema.jsonld [OUR CUSTOM FILE]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  SKILL.md says: "See schema for entityTypes"                              │
    │                                                                           │
    │  Agent READs: .../layer_0_group/.claude/schema/layer-stage-schema.jsonld  │
    │                                                                           │
    │  FINDS:                                                                   │
    │  • entityTypes definitions                                                │
    │  • SubFeature, Component, Subproject classes                              │
    │  • Naming patterns with examples                                          │
    │  • Validation rules                                                       │
    └───────────────────────────────────────────────────────────────────────────┘
                    │
                    ▼
    ORDER N+4+: Additional Context [OUR CUSTOM FILES]
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  Based on task, agent may also read:                                      │
    │                                                                           │
    │  • sub_layer_0_04_rules/*.md (universal rules)                            │
    │  • sub_layer_0_03_principles/*.md (guiding principles)                    │
    │  • sub_layer_0_02_knowledge_system/ (domain knowledge)                    │
    │  • status.json (current state)                                            │
    │  • stage_*/CLAUDE.md (stage-specific context)                             │
    │  • stage_*/.claude/skills/*/SKILL.md (stage workflows)                    │
    └───────────────────────────────────────────────────────────────────────────┘
```

---

## How We Hook Into Claude Code

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│               OUR EXTENSION POINTS                                               │
└─────────────────────────────────────────────────────────────────────────────────┘

    CLAUDE CODE OFFICIAL          OUR CUSTOM ADDITIONS
    ═══════════════════           ════════════════════

    ~/.claude/CLAUDE.md  ────────▶ Critical rules, context traversal instruction
         │
         │ (instructs agent)
         │
         ▼
    Path CLAUDE.md files ────────▶ Layer-stage framework, navigation guides
         │
         │ (instructs agent)
         │
         ▼
    Agent reads files    ────────▶ index.jsonld, SKILL.md, schema.jsonld
         │                         sub_layers, status.json
         │
         │ (chains continue)
         │
         ▼
    More files           ────────▶ rules, principles, knowledge, etc.
```

---

## Our Custom File Types

| File Type | Purpose | How Loaded |
|-----------|---------|------------|
| `index.jsonld` | Navigation, conventions, triggers | CLAUDE.md instructs agent to read |
| `SKILL.md` | Detailed procedures | trigger: in index.jsonld |
| `schema.jsonld` | Type definitions, validation | SKILL.md references |
| `sub_layer_*/` | Rules, knowledge, principles | CLAUDE.md references |
| `status.json` | Current state | CLAUDE.md instructs |
| `AGENTS.md` | Delegation rules | CLAUDE.md references |

---

## The Key Mechanism: CLAUDE.md Instructions

Our system works because CLAUDE.md files (which Claude Code auto-loads) contain instructions that tell the agent to read our custom files:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  EXAMPLE: How ~/.claude/CLAUDE.md Triggers Custom Loading                        │
└─────────────────────────────────────────────────────────────────────────────────┘

    ~/.claude/CLAUDE.md contains:

    ┌─────────────────────────────────────────────────────────────────────────┐
    │  ### [CRITICAL] 3. Context Traversal Rule                               │
    │                                                                         │
    │  **Before starting any task**, traverse the AI system to gather context:│
    │  1. **Read CLAUDE.md files** in the path from root to working directory │
    │  2. **Identify current layer and stage** (layer_0, layer_1, layer_-1)   │
    │  3. **Check relevant sub_layers** for applicable rules, prompts...      │
    │  4. **Read status.json** if exists to understand current state          │
    └─────────────────────────────────────────────────────────────────────────┘

    This instruction causes agent to:
    1. Already done by Claude Code (path CLAUDE.md)
    2. Parse layer/stage from directory names
    3. Read sub_layer files
    4. Read status.json

    ═══════════════════════════════════════════════════════════════════════════

    .../0_layer_universal/CLAUDE.md contains:

    ┌─────────────────────────────────────────────────────────────────────────┐
    │  ## Navigation: How to Find Things                                      │
    │                                                                         │
    │  ### Sub-Layers (layer_0/layer_0_03_sub_layers/)                        │
    │  | Sub-Layer | Purpose | When to Read |                                 │
    │  |-----------|---------|--------------|                                 │
    │  | sub_layer_0_04_rules/ | Universal rules | ALWAYS |                   │
    └─────────────────────────────────────────────────────────────────────────┘

    This instruction causes agent to read rules when needed.
```

---

## Summary: Official vs Custom

| Aspect | Claude Code Official | Our Custom Addition |
|--------|---------------------|---------------------|
| **Auto-loaded** | System prompt, tools, CLAUDE.md chain | None (all agent-driven) |
| **Extension point** | CLAUDE.md files | Instructions in CLAUDE.md |
| **File types** | CLAUDE.md, settings.json | index.jsonld, SKILL.md, schema.jsonld, sub_layers |
| **Navigation** | Path-based (~ to cwd) | Graph-based (nav:parent/children/siblings) |
| **Conventions** | None built-in | conventions.childNaming in index.jsonld |
| **Triggers** | None built-in | trigger:onEntityCreation, etc. |
| **Validation** | None built-in | schema.jsonld entityTypes |

---

*Last updated: 2026-02-05*
