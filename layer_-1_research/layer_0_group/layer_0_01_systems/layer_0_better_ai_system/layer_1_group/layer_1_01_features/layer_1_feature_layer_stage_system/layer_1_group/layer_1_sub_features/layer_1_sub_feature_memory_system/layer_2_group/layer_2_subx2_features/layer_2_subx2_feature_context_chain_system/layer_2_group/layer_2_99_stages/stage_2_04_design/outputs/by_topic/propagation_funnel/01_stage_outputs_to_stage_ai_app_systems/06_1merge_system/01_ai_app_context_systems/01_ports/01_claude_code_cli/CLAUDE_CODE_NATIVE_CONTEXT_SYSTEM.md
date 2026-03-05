---
resource_id: "f8237040-5571-41e1-a777-bba06d954b8c"
resource_type: "output"
resource_name: "CLAUDE_CODE_NATIVE_CONTEXT_SYSTEM"
---
# Claude Code CLI — Native Context System Architecture

**Date Created**: 2026-02-27
**Research Source**: Claude Code documentation, layer-stage system research, CLAUDE.md specifications
**Status**: Production-Ready Context System

---

<!-- section_id: "31f55afe-0f0c-40f4-8e5a-8f1fa4a8abb0" -->
## Overview

Claude Code's native context system is **hierarchical and file-based**. Unlike Cursor IDE (which uses rule patterns) or Gemini (which uses explicit caching), Claude Code uses a multi-level **CLAUDE.md chain** that cascades context from the root workspace down through layers and stages.

The system is built on the **layer-stage architecture**: a recursive directory structure where each entity (layer, stage, feature) has its own `0AGNOSTIC.md` (source of truth) and auto-generated `CLAUDE.md` (for tools like Claude Code).

---

<!-- section_id: "e3d7097a-06ca-4a52-9793-a01b58f9ec72" -->
## Core Architecture

<!-- section_id: "928bb734-ec03-47b0-8801-35ed77354bdd" -->
### 1. The CLAUDE.md Hierarchy

**Purpose**: Provide tool-specific context that cascades down the directory tree.

**The Chain** (from root to working directory):

```
~/.claude/CLAUDE.md                    (User-level global rules)
  ↓
~/dawson-workspace/code/CLAUDE.md      (Workspace level)
  ↓
0_layer_universal/CLAUDE.md            (Layer 0: Universal)
  ↓
layer_1/layer_1_projects/[project]/CLAUDE.md  (Layer 1: Project)
  ↓
layer_-1_research/[feature]/CLAUDE.md  (Layer -1: Research)
  ↓
[entity]/.0agnostic/                   (On-demand resources)
```

**How Context Loads** (Claude Code startup):

```
1. Session begins in working directory
2. Claude Code scans parent directories for CLAUDE.md files
3. Loads all CLAUDE.md files up to root (or first non-git boundary)
4. Merges context hierarchically (child overrides parent)
5. Injects merged context into every API call
6. Also loads on-demand resources (.0agnostic/) when triggered
```

**Key Characteristic**: CLAUDE.md files are **auto-generated** from `0AGNOSTIC.md` via `agnostic-sync.sh`. Never edit CLAUDE.md directly — edit `0AGNOSTIC.md` instead.

<!-- section_id: "faa9ae8a-7a4d-4ce9-8ec7-48889c85232d" -->
### 2. Source of Truth: 0AGNOSTIC.md

**Location**: One per entity (layer, stage, project, feature)

**Purpose**: **Single source of truth** for entity context. All tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md) are generated from this file.

**Structure**:

```markdown
# [Entity Name]

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
- Role: [what this entity does]
- Scope: [what it's responsible for]
- Parent: [path to parent 0AGNOSTIC.md]
- Children: [list of child entities]

## Key Behaviors
[What this entity autonomously does]

## Triggers
[When to load context for this entity]

# ── Current Status ──

## Current Status
[Substantive summary of current state]

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail
[Expanded details, metrics, findings]

# ── References ──

## Navigation
[How to find related content]

## Resources Available
[Pointers to .0agnostic/ content]
```

**Key Distinction**:
- **0AGNOSTIC.md**: Master source (hand-edited, version-controlled)
- **CLAUDE.md**: Generated output (auto-generated, don't edit)

<!-- section_id: "b72540de-16ae-4d13-9990-6e06baa7bb8f" -->
### 3. The .0agnostic/ Directory (On-Demand Resources)

**Location**: Every entity has `.0agnostic/` with numbered subdirectories

**Structure** (unified convention):

```
.0agnostic/
├── 01_knowledge/              # Domain knowledge (per-topic)
│   ├── principles/            # Core principles
│   ├── docs/                  # Reference documentation
│   └── resources/templates/   # Reusable templates
│
├── 02_rules/                  # Behavioral rules
│   ├── static/                # Always-apply rules
│   └── dynamic/               # Scenario-triggered rules
│
├── 03_protocols/              # Step-by-step procedures
│
├── 04_episodic_memory/        # Session history and learnings
│   ├── sessions/              # Session records
│   └── changes/               # What was modified
│
├── 05_handoff_documents/      # Async handoff communication
│   ├── 01_incoming/           # From parent/siblings/children
│   └── 02_outgoing/           # To parent/siblings/children
│
├── 06_context_avenue_web/     # Multiple delivery avenues
│   ├── 01_file_based/         # File-based (AALang, skills, agents)
│   └── 02_data_based/         # Data-based (KG, embeddings, etc.)
│
└── 07+_setup_dependant/       # Machine/OS-specific context
```

**Key Files**:

| Location | Purpose | When Loaded |
|----------|---------|------------|
| `02_rules/static/` | Rules always applied | Session startup |
| `02_rules/dynamic/` | Context-triggered rules | When condition met |
| `01_knowledge/` | Domain reference | On-demand when needed |
| `03_protocols/` | Step-by-step procedures | Skill invocation |
| `04_episodic_memory/` | Session history | Resumption |

<!-- section_id: "da88a1a6-38b8-4ae4-a8dc-9abef240a6bf" -->
### 4. The Layer-Stage Hierarchy

**Purpose**: Organize all work into **11 stages** (request, research, design, planning, development, testing, criticism, fixing, current product, archives).

**Structure**:

```
layer_N_group/
├── layer_N_00_layer_registry/
├── layer_N_01_ai_manager_system/        (deprecated, moved to 0AGNOSTIC)
└── layer_N_99_stages/
    ├── stage_N_01_request_gathering/
    ├── stage_N_02_research/
    ├── stage_N_03_instructions/
    ├── stage_N_04_design/
    ├── stage_N_05_planning/
    ├── stage_N_06_development/
    ├── stage_N_07_testing/
    ├── stage_N_08_criticism/
    ├── stage_N_09_fixing/
    ├── stage_N_10_current_product/
    └── stage_N_11_archives/

layer_N+1_group/                         (child entities)
└── layer_N+1_sub_features/
    ├── layer_N+1_sub_feature_[name]/
    ├── [nested .0agnostic/]
    └── [nested stages]
```

**Key Characteristic**: Each stage has its own `.0agnostic/` directory with stage-specific knowledge, rules, and protocols. Each stage agent (manager for that stage) reads the stage's `0AGNOSTIC.md` to understand its methodology and output format.

<!-- section_id: "9530c62f-5fac-469b-9bdd-48f4ef0b06c3" -->
### 5. Skills System

**Location**: `.claude/skills/[skill-name]/SKILL.md`

**Purpose**: Specialized, reusable workflows for complex tasks.

**Anatomy**:

```markdown
---
name: [skill-name]
description: "[What this skill does]"
---

# [Skill Title]

## WHEN to Use
[Situations where this skill applies]

## WHEN NOT to Use
[Situations to avoid]

## Prerequisites
[What must be true before using]

## Protocol
[Step-by-step workflow]

## References
[Links to related 0AGNOSTIC.md / skills / knowledge]
```

**Key Skills**:

| Skill | Purpose |
|-------|---------|
| `/context-gathering` | Identify layer/stage, load context chain |
| `/entity-creation` | Create new layer/stage with full structure |
| `/stage-workflow` | Transition between stages (01→02→04→05→06→07) |
| `/handoff-creation` | Create handoff documents (async communication) |

**How Skills Load**: When invoked (e.g., `/context-gathering`), Claude Code loads the skill's SKILL.md and executes the described workflow.

<!-- section_id: "819e7ef2-4420-425e-bf9f-605f6aa74f6f" -->
### 6. Rules System

**Two Types**:

#### Static Rules (`.0agnostic/02_rules/static/`)
**Always applied**, no conditions.

```markdown
# Rule: File Change Reporting

Every turn with filesystem modifications:
1. Describe changes INLINE with absolute paths
2. Provide end-of-turn summary (Added/Updated/Moved/Removed)
```

#### Dynamic Rules (`.0agnostic/02_rules/dynamic/`)
**Scenario-triggered**, applied when conditions match.

```markdown
# Rule: Source of Truth Protocol

**Triggered when**: User says "use research context chain"

When triggered:
1. Load all episodic memory
2. Read canonical sources
3. Trace propagation paths
4. Validate consistency
```

<!-- section_id: "0455371f-383a-48ee-8ded-3a2bd7f8111a" -->
### 7. Skills-Based Context Injection

**How Skills Work**:

```
User: "/context-gathering"
  ↓
Claude Code reads: .claude/skills/context-gathering/SKILL.md
  ↓
Skill describes workflow:
  1. Read CLAUDE.md chain
  2. Identify layer and stage
  3. Load relevant rules
  4. Load 0AGNOSTIC.md for current entity
  ↓
Claude Code executes each step
  ↓
Skill outputs context loaded and ready
```

<!-- section_id: "b41d2cbe-d469-4c01-8327-303631bd3744" -->
### 8. Context Chain Propagation

**Principle**: Context **cascades down** (parent → child) but child can **override** parent.

**Example Chain**:

```
root CLAUDE.md (universal rules)
  ├─ Triggers: [Always load these]
  └─ Resources: [Root-level knowledge]
    ↓
layer_0/CLAUDE.md (universal features)
  ├─ Inherits: root rules
  ├─ Adds: layer_0-specific rules
  └─ Can override: root rules for layer_0
    ↓
layer_1/[project]/CLAUDE.md (specific project)
  ├─ Inherits: layer_0 + root
  ├─ Adds: project-specific context
  └─ Overrides: as needed for this project
    ↓
stage_2_04_design/CLAUDE.md (specific stage)
  ├─ Inherits: project + layer_0 + root
  ├─ Adds: design-stage methodology
  └─ Overrides: for design work only
```

<!-- section_id: "2e7a885a-f31f-4b5b-8331-62f3b33fd833" -->
### 9. Episodic Memory (Session Continuity)

**Location**: `.0agnostic/04_episodic_memory/`

**Purpose**: Record session history for resumption in future sessions.

**Structure**:

```
.0agnostic/04_episodic_memory/
├── sessions/
│   ├── 2026-02-26-session-01.md    (what was done)
│   ├── 2026-02-26-session-02.md
│   └── index.md                     (session index/summary)
│
└── changes/
    └── divergence.log               (track modifications to outputs)
```

**How It Works**:

```
Session 1: Work on stage 02 research
  ├─ Create findings
  ├─ Record session notes in .0agnostic/04_episodic_memory/sessions/
  └─ Update divergence.log

Session 2: Resume work
  ├─ Read .0agnostic/04_episodic_memory/index.md
  ├─ Understand: "research was at 40% complete, blockers were X and Y"
  ├─ Continue from known state
  └─ Update new session notes
```

<!-- section_id: "dfa5589c-9c9f-4534-ae6b-8e05e6172205" -->
### 10. Handoff Documents (Async Communication)

**Location**: `.0agnostic/05_handoff_documents/`

**Purpose**: Asynchronous communication between agents across stage/layer boundaries.

**Structure**:

```
.0agnostic/05_handoff_documents/
├── 01_incoming/                     (what we receive)
│   ├── 01_from_above/              (parent/manager instructions)
│   ├── 02_from_sides/              (sibling communications)
│   │   ├── 01_from_left/
│   │   └── 02_from_right/
│   └── 03_from_below/              (child reports)
│
└── 02_outgoing/                     (what we send)
    ├── 01_to_above/                (reports to parent/manager)
    ├── 02_to_sides/                (coordinate with siblings)
    │   ├── 01_to_left/
    │   └── 02_to_right/
    └── 03_to_below/                (instructions to children)
```

**Example Handoff**:

```
stage_2_02_research sends to stage_2_04_design:
  File: .0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md
  Content:
    - Research findings (3 topics completed)
    - Blockers (2 remaining unknowns)
    - Recommendations for design
    - Artifacts location (stage outputs)

stage_2_04_design reads:
  File: .0agnostic/05_handoff_documents/01_incoming/03_from_below/stage_report.md
  (synced from research's outgoing by sync-handoffs.sh)
```

<!-- section_id: "79451b4b-52f6-4c5f-89f7-1ca3208a6f90" -->
### 11. MCP Integration (Tool Expansion)

**Purpose**: Extend Claude Code with external tools and services.

**Configuration**: `.claude/mcp.json`

```json
{
  "mcpServers": {
    "canvas": {
      "command": "python",
      "args": ["/path/to/canvas-mcp-server.py"]
    },
    "github": {
      "command": "node",
      "args": ["/path/to/github-mcp-server.js"]
    }
  }
}
```

**How MCP Works**:

```
User: "Fetch the latest Canvas assignments for CSE 300"
  ↓
Claude Code sees: MCP server "canvas" available
  ↓
Claude Code calls: canvas.fetch_assignments(course_id=406222)
  ↓
MCP server executes (has access to Canvas API)
  ↓
Result returned to Claude Code context
  ↓
Claude Code continues with result (e.g., processes data, generates dashboard)
```

**Common MCP Servers**:
- Canvas LMS (assignments, grades, submissions)
- GitHub (repositories, issues, PRs)
- Databases (SQL query execution)
- Slack (messaging, file operations)

---

<!-- section_id: "2c277e11-9554-4c10-9e09-04560ce3d44f" -->
## How Context Flows in Claude Code

<!-- section_id: "58cea2c3-36f2-4d42-9e00-9cfdc9f41f89" -->
### Session Startup

```
1. User opens Claude Code in a directory
2. Scan parent directories for CLAUDE.md files (up to git root)
3. Load all found CLAUDE.md files
4. Merge hierarchically (child > parent)
5. Inject merged context into Claude Code internal state
6. On first API message: prepend merged context to user message
```

<!-- section_id: "84841bde-748b-4c94-ac7c-0885723ea06d" -->
### User Issues Command

```
1. User types message
2. Claude Code checks: does message start with "/"?
   a. If yes: look up skill in .claude/skills/
   b. If no: proceed normally
3. If skill found: load SKILL.md and execute described workflow
4. Include in context: active rules (static + triggered dynamic)
5. Include on-demand: any .0agnostic/ resources mentioned in active rules
```

<!-- section_id: "68c3ffbf-c9ea-4a6b-a4d2-1cd44bd8cb1d" -->
### API Call

```
User message
  ↓ (Claude Code prepares)
Merged CLAUDE.md context
  ↓
Active rules context
  ↓
Skill protocol (if applicable)
  ↓
MCP tool descriptions (if available)
  ↓ (sent as system prompt + message)
Claude API call
  ↓
Response processed
```

---

<!-- section_id: "7d52ced8-5877-4e9b-a6b6-f03371a5a062" -->
## Cascade vs. Inheritance

**Key Principle**: Context **cascades** (flows down), not inherits (stays same).

```
Root defines: "Always use absolute paths"
Layer 1 adds: "For this project, use relative paths instead"
  ↓
Result: Layer 1 overrides root, uses relative paths
         But if Layer 1 didn't mention it, root rule applies

Stage 04 Design adds: "Documentation format is markdown"
Layer 0 adds: "Documentation format is HTML"
  ↓
Result: Stage 04 overrides Layer 0 (child > parent)
```

---

<!-- section_id: "b8b5148d-a8d2-4149-a6f1-c533473481bf" -->
## Token Budget Management

**Context Window**: 200K tokens (Claude Code + any pro upgrades)

**Budget Distribution**:

```
CLAUDE.md chain:           5-10K tokens   (all CLAUDE.md files combined)
Active rules:              2-5K tokens    (static + triggered dynamic)
User message:              1-2K tokens
Skill protocol:            1-3K tokens    (if skill invoked)
Available for response:     180K+ tokens
```

**Optimization Strategies**:
1. Keep CLAUDE.md lean (pointers only, not full content)
2. Load .0agnostic/ resources on-demand (not all at startup)
3. Use episodic memory to compress session history
4. Create handoff documents to pass context between sessions

---

<!-- section_id: "81b943d2-fcef-47b7-b1b8-0876faf47026" -->
## Comparison with Other Native Systems

| Aspect | Claude Code | Cursor IDE | Gemini | Codex |
|--------|-----------|-----------|--------|-------|
| **Context Model** | Hierarchical chain | Rule-based | Cache-based | Config-based |
| **File Structure** | CLAUDE.md + .0agnostic | .cursor/rules | N/A | config.toml |
| **Persistence** | Episodic memory | Memory Bank | Session-based | Database |
| **Skill System** | Yes (.claude/skills) | No (hooks) | No | No |
| **Async Communication** | Handoff documents | Messages | No | No |
| **Stage System** | Yes (11 stages) | No | No | No |
| **Token Efficiency** | Lean (cascade + pointers) | Flat (all rules) | Efficient (caching) | Dense (full config) |

---

<!-- section_id: "6d83b2fe-86be-45d2-9b1d-ba1db33f4f53" -->
## Key Insights for Porting to Claude Code

1. **Hierarchical Design**: Everything cascade from root down. Child overrides parent for flexibility.

2. **Single Source of Truth**: 0AGNOSTIC.md is master; CLAUDE.md is generated. Never edit generated files.

3. **On-Demand Loading**: Don't load everything. Use triggers and pointers to load contextual resources only when needed.

4. **Skill-Based Workflows**: Complex workflows are packaged as skills, not embedded in rules. Skills are reusable.

5. **Handoff Documents**: Stage-to-stage and layer-to-layer communication happens via async handoff docs, not real-time messages.

6. **Episode Memory for Continuity**: Each session records what it did. Next session reads history and continues.

7. **MCP for External Tools**: Extend Claude Code's capabilities by connecting MCP servers (Canvas, GitHub, databases, etc.).

---

<!-- section_id: "1a907eea-d1cf-4b01-b98c-0a38a5466345" -->
## Porting Checklist

- [ ] Create root-level 0AGNOSTIC.md with Identity, Key Behaviors, Triggers
- [ ] Generate CLAUDE.md via agnostic-sync.sh
- [ ] Create `.0agnostic/02_rules/{static,dynamic}/` for rules
- [ ] Populate `.0agnostic/01_knowledge/` with reference docs
- [ ] Create `.0agnostic/03_protocols/` for workflows
- [ ] Set up `.0agnostic/04_episodic_memory/` for session history
- [ ] Design `.0agnostic/05_handoff_documents/` structure for communication
- [ ] Create skills in `.claude/skills/` for complex tasks
- [ ] Configure MCP servers in `.claude/mcp.json` if needed
- [ ] Test CLAUDE.md chain loading in multiple directories

---

<!-- section_id: "ab2b0992-cec6-48c8-9dce-7f5c7ed5f3cf" -->
## References

- **Layer-Stage System**: `layer_0/.../layer_stage_system/`
- **0AGNOSTIC.md Template**: `layer_0/.../entity_lifecycle/INSTANTIATION_GUIDE.md`
- **CLAUDE.md Generation**: `agnostic-sync.sh` in root `.0agnostic/`
- **Episodic Memory**: `.0agnostic/04_episodic_memory/`
- **Skills System**: `.claude/skills/*/SKILL.md`
