---
resource_id: "81269c33-ebbc-4d18-9645-29cdcc0e11a6"
resource_type: "document"
resource_name: "custom_layer_stage_loading"
---
# Custom Layer-Stage Context Loading

**Purpose**: Document how our layer-stage system extends Claude Code's official context loading with custom conventions, navigation, and triggers.

**Relationship to Official**: See [Official Claude Code Loading](./official_claude_code_loading.md) for what Claude Code auto-loads. This document shows what we've built on top.

---

<!-- section_id: "bb6ac9ef-7c8d-4979-995e-215a4a16d9cb" -->
## Extension Strategy

Our system extends Claude Code through **two mechanisms**:

1. **Instructions in CLAUDE.md files** - Tell the agent to read additional files (index.jsonld, SKILL.md, etc.)
2. **Directory conventions** - Use naming patterns that encode meaning (layer_N, stage_NN, sub_layer_N_NN)

We do NOT currently use:
- SessionStart hooks (could automate context loading)
- .claude/rules/ directory (could put universal rules there)
- @import system (could chain CLAUDE.md files)

**Future Enhancement Opportunity**: We could use Claude Code's official hooks and @import system to make context loading more automatic.

---

<!-- section_id: "505349d9-7277-4300-863f-985b2641fef3" -->
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

<!-- section_id: "bdc0da29-6f9d-47bf-9abe-fad6abeec9bf" -->
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

<!-- section_id: "11b4598c-76c5-462a-9808-8226a2c78e77" -->
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

<!-- section_id: "7c7969d6-e503-4c65-a9c1-78f0d98e3538" -->
## Our Custom File Types

| File Type | Purpose | How Loaded | Location Pattern |
|-----------|---------|------------|------------------|
| `index.jsonld` | Navigation, conventions, triggers | CLAUDE.md instructs agent | Every entity directory |
| `SKILL.md` | Detailed procedures | trigger: in index.jsonld | `.claude/skills/*/SKILL.md` |
| `schema.jsonld` | Type definitions, validation | SKILL.md references | `.claude/schema/*.jsonld` |
| `sub_layer_*/` | Rules, knowledge, principles | CLAUDE.md references | `layer_N/layer_N_03_sub_layers/` |
| `status.json` | Current state | CLAUDE.md instructs | Any directory with state |
| `AGENTS.md` | Delegation rules | CLAUDE.md references | Deprecated, use .claude/ |
| `0AGNOSTIC.md` | Tool-agnostic instructions | Synced to CLAUDE.md | Same dir as CLAUDE.md |

<!-- section_id: "d7777ac9-90cf-4323-858e-c2991d5cbb37" -->
### Detailed File Descriptions

#### index.jsonld

JSON-LD file providing structured navigation and metadata for an entity:

```json
{
  "@context": { "@vocab": "https://layer-stage.dev/schema#" },
  "@type": "Feature",
  "name": "Context Framework",
  "nav:parent": { "@id": "../" },
  "nav:children": [{ "@id": "layer_1_subx2_feature_context_system/" }],
  "conventions": {
    "childNaming": "layer_{parentLayer+1}_sub_feature_{kebab-case-name}"
  },
  "trigger:onEntityCreation": ".claude/skills/entity-creation/SKILL.md"
}
```

**Key Properties**:
- `@type` - Entity type (Project, Feature, SubFeature, Stage, etc.)
- `nav:*` - Navigation links (parent, children, siblings)
- `conventions.*` - Naming and structure rules
- `trigger:*` - Actions to take on events

#### SKILL.md

Markdown file with detailed procedures for specific tasks:

```markdown
---
name: Entity Creation
description: Create new entities following conventions
tokenCost: ~500
---

# Entity Creation Skill

## When to Use
- Creating new features, sub-features, components

## Procedure
1. Read parent's index.jsonld
2. Get conventions.childNaming pattern
3. Create directory with correct name
...
```

**YAML Frontmatter**: Loaded at session start (lightweight)
**Full Content**: Loaded on-demand when skill invoked

#### schema.jsonld

JSON-LD schema defining types, patterns, and validation:

```json
{
  "@context": { "@vocab": "https://layer-stage.dev/schema#" },
  "entityTypes": {
    "SubFeature": {
      "pattern": "layer_{N}_sub_feature_{name}",
      "requiredFiles": ["CLAUDE.md", "index.jsonld"]
    }
  }
}
```

---

<!-- section_id: "84c6bc4e-f538-4f5e-84e6-c007a14a5d29" -->
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

<!-- section_id: "09fc9f7a-4357-455d-abeb-22fcbd6ea723" -->
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

<!-- section_id: "809381e9-efee-4b79-bc95-57eb7bf3878f" -->
## Potential Improvements Using Official Features

Claude Code provides several features we could leverage to improve our context loading:

<!-- section_id: "95485e6d-5cfc-439d-b6a4-129d451dbad9" -->
### 1. SessionStart Hooks

**Current**: Agent reads rules manually when instructed
**Improvement**: Use SessionStart hook to automatically load context

```json
// .claude/settings.json
{
  "hooks": {
    "SessionStart": [{
      "command": "cat layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/*.md"
    }]
  }
}
```

**Benefit**: Rules loaded automatically, no agent decision required

<!-- section_id: "a213ab94-1b8e-4b03-bd54-f9b8f1c10436" -->
### 2. .claude/rules/ Directory

**Current**: Rules in `sub_layer_0_04_rules/`, agent must navigate
**Improvement**: Symlink or copy critical rules to `.claude/rules/`

```
.claude/rules/
├── context_modification.md    → auto-loaded
├── commit_push_rule.md        → auto-loaded
└── file_path_linking.md       → auto-loaded
```

**Benefit**: Critical rules auto-loaded, always present

<!-- section_id: "03df5e1c-478a-4316-9940-35b74265f033" -->
### 3. @import System in CLAUDE.md

**Current**: CLAUDE.md files are independent, contain instructions to read others
**Improvement**: Use @import to chain files automatically

```markdown
# CLAUDE.md

@layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/critical_rules.md
@.claude/schema/layer-stage-schema.jsonld
```

**Benefit**: Context loaded when CLAUDE.md loads, no agent action needed

<!-- section_id: "7c71cf0b-3d4e-44a8-816f-02788b2827a1" -->
### 4. CLAUDE.local.md for Personal Preferences

**Current**: All context is shared via git
**Improvement**: Use CLAUDE.local.md for personal workflow preferences

```markdown
# CLAUDE.local.md (gitignored)

## My Preferences
- Always show full file paths
- Prefer verbose explanations
- Default to stage 06 (development)
```

**Benefit**: Personal customization without affecting shared config

---

<!-- section_id: "fb4e9886-8a9b-455f-8c17-426a5d5a18b7" -->
## Migration Path

If we decide to adopt official features:

| Current Approach | Official Feature | Migration Steps |
|-----------------|------------------|-----------------|
| Instructions in CLAUDE.md | SessionStart hooks | Create hook scripts, update settings.json |
| sub_layer_0_04_rules/ | .claude/rules/ | Symlink or move critical rules |
| "Read index.jsonld" instructions | @import | Convert to @import statements |
| Shared-only config | CLAUDE.local.md | Document personal override patterns |

**Risk**: Over-automation could make the system harder to understand and debug.

**Recommendation**: Start with .claude/rules/ for critical rules, evaluate hooks later.

---

<!-- section_id: "99d80989-b333-4f55-b328-eb9eabd89dcf" -->
## Directory Naming Conventions

Our system encodes meaning in directory names:

```
layer_{N}_{type}_{name}
  │     │    │       │
  │     │    │       └── Descriptive name (kebab-case or snake_case)
  │     │    └────────── Type: feature, sub_feature, component, stage, etc.
  │     └─────────────── Layer number: 0=universal, 1=project, -1=research
  └───────────────────── Literal "layer_"

stage_{NN}_{name}
  │     │     │
  │     │     └── Stage name
  │     └──────── Two-digit stage number (01-11)
  └────────────── Literal "stage_"

sub_layer_{L}_{NN}_{name}
  │          │   │     │
  │          │   │     └── Sub-layer name
  │          │   └──────── Two-digit sub-layer number
  │          └──────────── Parent layer number
  └─────────────────────── Literal "sub_layer_"
```

**Examples**:
- `layer_0_feature_context_framework` - Layer 0, Feature type, context-framework name
- `layer_1_subx2_feature_context_system` - Layer 1, SubFeature type
- `stage_06_development` - Stage 06 (development phase)
- `sub_layer_0_04_rules` - Sub-layer of layer 0, #04 (rules)

---

<!-- section_id: "abb99c11-0b54-40cd-afdb-9b13e3bd357d" -->
## AALang Context Agents (NEW - 2026-02-05)

Our system now includes **AALang context agents** that formalize the context loading process.

<!-- section_id: "efd3e49e-e1b6-46c2-a309-61199064c3cf" -->
### Agent-Based Context Loading

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│         AALANG CONTEXT LOADING AGENT                                             │
│         (ctx:ContextLoadingAgent)                                                │
└─────────────────────────────────────────────────────────────────────────────────┘

    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  PHASE 1: CONTEXT LOADING MODE                                             ║
    ║  ═══════════════════════════════                                           ║
    ║                                                                            ║
    ║  • Load ~/.claude/CLAUDE.md chain                                          ║
    ║  • Track each file in ContextLoadingStateActor                             ║
    ║  • Calculate initial confidence                                            ║
    ║                                                                            ║
    ║  EXIT: overallConfidence >= 0.6                                            ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
                    │
                    ▼
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  PHASE 2: CONTEXT VALIDATION MODE                                          ║
    ║  ═══════════════════════════════                                           ║
    ║                                                                            ║
    ║  • Identify current layer (-1, 0, 1, 2, ...)                               ║
    ║  • Identify current stage (01-11, if applicable)                           ║
    ║  • Check required context loaded (rules, protocols)                        ║
    ║  • Update NavigationStateActor                                             ║
    ║                                                                            ║
    ║  EXIT: overallConfidence >= 0.8                                            ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
                    │
                    ▼
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  PHASE 3: CONTEXT PROPAGATION MODE                                         ║
    ║  ═══════════════════════════════                                           ║
    ║                                                                            ║
    ║  • Build inheritance chain (layer_0 → layer_1 → layer_2 → ...)             ║
    ║  • Detect @override markers                                                ║
    ║  • Resolve priority conflicts                                              ║
    ║  • Higher layer CAN override lower layer                                   ║
    ║                                                                            ║
    ║  EXIT: All conflicts resolved                                              ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
                    │
                    ▼
    ╔═══════════════════════════════════════════════════════════════════════════╗
    ║  PHASE 4: CONTEXT DELIVERY MODE                                            ║
    ║  ═══════════════════════════════                                           ║
    ║                                                                            ║
    ║  • If debugMode: show summary                                              ║
    ║  • Confirm ready for work                                                  ║
    ║  • Update context_state.json for cross-session persistence                 ║
    ║                                                                            ║
    ║  EXIT: User provides task                                                  ║
    ╚═══════════════════════════════════════════════════════════════════════════╝
```

<!-- section_id: "59678903-22f4-4a55-b05d-dba00da963d9" -->
### State Actors

| Actor | Purpose | Persisted |
|-------|---------|-----------|
| `ContextLoadingStateActor` | Track loaded files, chain position | Yes |
| `ContextConfidenceStateActor` | Track confidence scores (0.0-1.0) | Yes |
| `NavigationStateActor` | Track layer/stage/sub_layer position | Yes |
| `DebugContextStateActor` | Control debug output | Yes |

<!-- section_id: "9f6edf2d-b85a-4131-be10-a92952d41837" -->
### Layer Inheritance Model

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│         LAYER INHERITANCE (Higher can override lower)                            │
└─────────────────────────────────────────────────────────────────────────────────┘

    layer_0 (universal base)
        │
        ├── Provides default rules, protocols, knowledge
        │
        ▼
    layer_1 (project)
        │
        ├── INHERITS all of layer_0
        ├── CAN OVERRIDE layer_0 with @override marker
        │
        ▼
    layer_2+ (sub-projects)
        │
        ├── INHERITS all of layer_0 + layer_1
        └── CAN OVERRIDE any inherited context

    PRECEDENCE:
    1. Higher layer number wins (layer_1 > layer_0)
    2. Later in chain wins (within same layer)
    3. CLAUDE.local.md wins (personal overrides)
    4. Explicit @override wins over implicit
```

<!-- section_id: "e577986b-6568-4d4e-a130-e6578a900f7c" -->
### Cross-Session Persistence

State is persisted to: `.claude/context_state.json`

```json
{
  "contextLoadingState": { "loadedFiles": [...], "overrides": [...] },
  "contextConfidenceState": { "overallConfidence": 0.85 },
  "navigationState": { "currentLayer": 1, "currentStage": "06" },
  "debugContextState": { "debugMode": false }
}
```

<!-- section_id: "500c2925-8c42-4bec-a272-3c26c99d0469" -->
### AALang Agent Files

Location: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_context_agents/`

| File | Purpose |
|------|---------|
| `context_loading_agent.jsonld` | Main agent with 4-phase workflow |
| `context_state_actors.jsonld` | State actor definitions |
| `context_modes.jsonld` | Mode definitions |
| `README.md` | Documentation |

<!-- section_id: "6f3a83d4-a025-472c-8caa-736cd6ab1b71" -->
### CLAUDE.md Integration

Each CLAUDE.md in the chain includes:

```markdown
## AALang Integration

@agent ctx:ContextLoadingAgent

### Context Chain Position
- **Position**: N of M
- **Parent**: path/to/parent/CLAUDE.md
- **Children**: [child paths]
- **Inherits**: layer_0
- **Can Override**: layer_0

### On Load
- ctx:ContextLoadingStateActor.loadedFiles += this file
- ctx:NavigationStateActor.currentLayer = N
```

<!-- section_id: "e74750db-8ae4-4e33-996e-e03e6fffa494" -->
### Related Documentation

| Document | Location |
|----------|----------|
| Context Loading Protocol | `sub_layer_0_05_protocols/context_loading_protocol.md` |
| Priority Rules | `sub_layer_0_04_rules/context_priority_rules.md` |
| Scope Boundaries | `sub_layer_0_04_rules/context_scope_boundaries.md` |
| Quality Checklist | `sub_layer_0_05_protocols/context_quality_checklist.md` |

---

*Last updated: 2026-02-05*

**Related Documentation**:
- [Official Claude Code Loading](./official_claude_code_loading.md) - What Claude Code auto-loads
- [Context Architecture](./context_architecture.md) - What context exists
- [Agent Instantiation Chain](./agent_instantiation_chain.md) - How agents get context
