---
resource_id: "81f72ac3-d849-4c04-8ad7-9cd214d1f001"
resource_type: "output"
resource_name: "layer_stage_instantiation_understanding"
---
# Layer-Stage Instantiation Understanding

**Date**: 2026-01-31
**Time**: 01:15 UTC (updated 2026-02-01)
**Topic**: How layers and stages are instantiated in the framework
**Sources**: SYSTEM_OVERVIEW.md, layer_registry.yaml, stage_registry.yaml, USAGE_GUIDE.md, entity-creation skill, FLEXIBLE_LAYERING_SYSTEM.md

---

<!-- section_id: "b2e22486-20d5-417f-94a3-8e7281a98fc6" -->
## Core Concept: Layers of Specificity

**The layer system is fundamentally about SPECIFICITY and ABSTRACTION.**

- **Lower layer numbers = more universal/abstract** (applies broadly)
- **Higher layer numbers = more specific** (applies narrowly)
- **Rules and context CASCADE from universal → specific**

| Layer | Name | Scope of Rules/Context |
|-------|------|------------------------|
| -1 | Research | Exploratory (outside main hierarchy) |
| 0 | Universal | **GLOBAL** - applies to ALL projects everywhere |
| 1 | Project | Applies to ONE specific project |
| 2 | Feature | Applies to ONE specific feature of that project |
| 3 | Component | Applies to ONE specific component of that feature |
| 4+ | Sub-* | Applies to increasingly specific nested entities |

**Key Principle**: Rules at Layer 0 apply EVERYWHERE. Rules at Layer 1 apply only to that project. Rules at Layer 2 apply only to that feature. And so on.

---

<!-- section_id: "f84f2805-cbbc-4baf-b689-366aaf482cb2" -->
## Cascading Context

When an agent works at any level:
1. It inherits ALL rules/context from Layer 0 (universal)
2. Plus rules/context from Layer 1 (if in a project)
3. Plus rules/context from Layer 2 (if in a feature)
4. Plus rules/context from Layer 3 (if in a component)
5. ...and so on down the hierarchy

**This is why lower layers are "prerequisites"** - you must understand universal rules before project rules, project rules before feature rules, etc.

---

<!-- section_id: "e1e59a24-ca2e-4396-913b-43ab93db8b4d" -->
## Nesting: Same-Type vs Different-Type

<!-- section_id: "0be3189e-a8e8-42db-a764-f139fed372fb" -->
### CRITICAL NAMING RULE

The **"sub" prefix ONLY applies when nesting the SAME type**:

| Nesting Pattern | Result | Why |
|-----------------|--------|-----|
| Project inside Project | **sub_project** | Same type → uses "sub" |
| Feature inside Feature | **sub_feature** | Same type → uses "sub" |
| Component inside Component | **sub_component** | Same type → uses "sub" |
| Feature inside Project | **feature** (NOT sub_feature) | Different type → no "sub" |
| Component inside Project | **component** (NOT sub_component) | Different type → no "sub" |
| Component inside Feature | **component** (NOT sub_component) | Different type → no "sub" |

<!-- section_id: "f9c7971e-5f11-4943-821e-cdec93b5cefa" -->
### Same-Type Nesting Depth Markers

When nesting the same type multiple levels deep:
- 1 level deep: `sub_project`, `sub_feature`, `sub_component`
- 2 levels deep: `subx2_project`, `subx2_feature`, `subx2_component`
- 3 levels deep: `subx3_project`, `subx3_feature`, `subx3_component`
- N levels deep: `subxN_*`

<!-- section_id: "ad1aff6b-d500-451b-9a68-cef8c6f8251c" -->
### What Each Entity Contains

| Entity Type | Contains (in layer_N+1/) |
|-------------|--------------------------|
| Project / Sub*_project | `sub*_projects/`, `features/`, `components/` |
| Feature | `sub_features/`, `components/` |
| Component | `sub_components/` |

**Key Rules**:
- **Projects** contain `features/` and `components/` (no sub prefix) plus `sub_projects/` for same-type nesting
- **Features** contain `sub_features/` (same-type) and `components/` (different type → no sub prefix)
- **Components** only contain `sub_components/` (same-type nesting)
- **Layer N+1 can have multiple types**: At any `layer_N+1/`, you may find `sub_projects/`, `features/`, AND `components/` as siblings

<!-- section_id: "60578c56-701c-41ee-8257-aa5f6322b690" -->
### Stages Within Sub-Layers

Stages can exist WITHIN sub-layers for specialized workflows. Example location:
```
layer_0_group/layer_0_03_sub_layers/sub_layer_0_05+_setup_dependant/
└── sub_layer_0_05_os/
    └── sub_layer_0_05_01_linux_ubuntu/
        └── layer_0_99_stages/    # Stages specific to Linux Ubuntu setup
```

This allows stage-based workflows (01-11) to be applied to specific setup contexts when needed.

---

<!-- section_id: "e6b0f8b0-2d82-4b8c-95b1-39c0846bce53" -->
## Layer Hierarchy (Detailed)

---

<!-- section_id: "281b7140-cba5-4916-bdf7-fdb044139326" -->
## The Two-Folder Structure (Layer Grouping)

Every entity has TWO sibling **GROUP folders** at its root:

```
layer_N_<type>_<name>/              # THE ENTITY
├── layer_N/                        # GROUP: This entity's INTERNALS
│   ├── layer_N_00_ai_manager_system/
│   ├── layer_N_01_manager_handoff_documents/
│   ├── layer_N_02_sub_layers/
│   └── layer_N_99_stages/
└── layer_N+1/                      # GROUP: NESTED CONTENT (children)
    ├── layer_N+1_sub*_projects/    # Sub-projects (if applicable)
    ├── layer_N+1_features/         # Features (or sub_features)
    └── layer_N+1_components/       # Components (or sub_components)
```

**Key Points**:
- `layer_N/` = **GROUP folder** containing the entity's own internals (manager, handoffs, stages)
- `layer_N+1/` = **GROUP folder** containing the entity's children (nested entities)
- These are SIBLINGS at the entity root, not nested within each other
- **IMPORTANT**: `layer_N/` and `layer_N+1/` are containers (groups), NOT entities themselves
- The actual ENTITY is the parent folder: `layer_N_<type>_<name>/`

---

<!-- section_id: "bb521ad5-3a77-4183-82d7-3b84a65dd6f3" -->
## Layer Internal Structure

Each layer has standard components at specific positions (from `layer_registry.yaml`):

| Position | Slug | Purpose | Folder Pattern |
|----------|------|---------|----------------|
| 00 | layer_registry | Metadata for this layer | `layer_N_00_layer_registry` |
| 01 | ai_manager_system | **How the AI system works** - agent hierarchy, delegation patterns, manager/worker relationships | `layer_N_01_ai_manager_system` |
| 02 | manager_handoff_documents | Session transition state, communication between layers | `layer_N_02_manager_handoff_documents` |
| 03 | sub_layers | Knowledge, prompts, principles, rules, setup | `layer_N_03_sub_layers` |
| 99 | stages | Workflow stages (01-11) | `layer_N_99_stages` |

**Position 99** keeps stages at the end for visibility/sorting.

---

<!-- section_id: "1f263591-dc5b-4316-83b1-0f055905a344" -->
## Sub-Layer Slots (within position 03)

Sub-layers organize different types of content:

| Slot | Content |
|------|---------|
| 00 | sub_layer_registry |
| 01 | prompts |
| 02 | knowledge_system |
| 03 | principles |
| 04 | rules |
| 05+ | setup_dependant (progressively specific) |

**Setup slots** (05+) go from general to specific:
- 05: OS setup
- 06: coding app setup
- 07: environment
- 08: AI apps/tools
- 09: MCP servers and tools
- 10: AI models
- 11: universal tools
- 12: agent setup

---

<!-- section_id: "8bc2b724-4e1d-4be5-91e9-652fe290bc66" -->
## Stage System

**CORRECTED ORDER** (design before planning):

| Position | Stage | Purpose |
|----------|-------|---------|
| 00 | stage_registry | Metadata only (not a workflow stage) |
| 01 | request_gathering | Gather requirements |
| 02 | research | Explore problem space |
| 03 | instructions | Define constraints |
| 04 | **design** | Architecture decisions |
| 05 | **planning** | Break into subtasks |
| 06 | development | Implementation |
| 07 | testing | Verification |
| 08 | criticism | Review |
| 09 | fixing | Corrections |
| 10 | current_product | Deliverable |
| 11 | archives | Historical records |

**Note**: Design (04) comes BEFORE planning (05). You design the solution first, then plan how to implement it.

<!-- section_id: "650842d4-5691-4e7c-afe3-390bf006ab72" -->
### Stage Internal Structure

Each stage contains:
```
stage_N_XX_name/
├── ai_agent_system/     # Stage-specific agent guidance
├── hand_off_documents/  # Incoming/outgoing handoffs
├── outputs/             # Stage artifacts
└── .claude/             # Claude-specific (commands, scripts, hooks, skills, agents)
```

---

<!-- section_id: "501c46af-88a7-46b7-80d8-06fd250eda87" -->
## Stage Output Organization Patterns

Each stage has specific output organization patterns suited to its purpose:

<!-- section_id: "e0db75a4-5254-42d7-9d20-ace7f73af9c1" -->
### Stage 01: Request Gathering

```
outputs/
├── overview/                    # High-level views
│   ├── consolidated_requirements.md
│   ├── dependencies.md
│   ├── system_vision.md
│   └── implementation_roadmap.md
├── requests/
│   ├── tree_of_needs/           # Hierarchical needs structure
│   │   ├── _meta/               # Metadata about the tree
│   │   └── 00_root_need/        # Root need with child branches
│   │       ├── 01_branch_need/
│   │       └── ...
│   └── README.md
└── STAGE_01_SUMMARY.md
```

**Key Pattern**: Tree of Needs - hierarchical breakdown of requirements

---

<!-- section_id: "a2dda373-d63c-4b7f-8fce-f1487051ac28" -->
### Stage 02: Research

```
outputs/
├── 01_understanding_in_progress/    # Work in progress
│   ├── by_need/                     # Organized by specific need from tree
│   ├── by_topic/                    # Organized by research topic
│   └── synthesis/                   # Combined insights
├── 02_finished_understanding/       # Completed research
│   ├── by_need/
│   ├── by_topic/
│   └── synthesis/
├── episodic/                        # Session tracking
│   ├── index.md
│   ├── sessions/
│   └── changes/
└── README.md
```

**Key Pattern**: In-progress vs Finished separation with by_need/by_topic/synthesis organization

---

<!-- section_id: "4313fd7c-e1c4-45db-b65d-e4e77d467e11" -->
### Stage 03: Instructions

```
outputs/
├── 01_instructions_in_progress/
│   ├── by_need/
│   ├── by_topic/
│   └── synthesis/
├── 02_finished_instructions/
│   ├── by_need/
│   ├── by_topic/
│   └── synthesis/
└── README.md
```

**Key Pattern**: Same as Research - mirrors the in-progress/finished + by_need/by_topic/synthesis pattern

---

<!-- section_id: "049d0bf3-4e45-437c-8195-70a06a46c95d" -->
### Stage 04: Design

```
outputs/
├── 03_design_decisions/
│   └── by_topic/
│       ├── 01_component_design.md
│       ├── 02_architecture_design.md
│       └── ...
├── episodic/
└── system_prompt_architecture_design.md
```

**Key Pattern**: Numbered design decisions organized by topic

---

<!-- section_id: "e5b5af07-a65c-4a6d-a415-b5588362fdc5" -->
### Stage 05: Planning

```
outputs/
├── IMPLEMENTATION_PLAN.md
├── system_prompt_architecture_plan.md
└── ...
```

**Key Pattern**: Implementation plans and roadmaps

---

<!-- section_id: "48971375-3574-49aa-be0f-20a724583e78" -->
### Stage 06: Development

```
outputs/
├── change_log.md
└── [implementation artifacts]
```

**Key Pattern**: Change tracking and implementation outputs

---

<!-- section_id: "a640913b-0c3b-4e06-a986-d95ecaa01745" -->
### Stage 07: Testing

```
outputs/
├── TEST_REPORT.md
├── test_plan.md
├── testing_results.md
└── findings.md
```

**Key Pattern**: Test plans, execution results, findings

---

<!-- section_id: "51945cf5-c24c-4858-9f6f-f510f6cee058" -->
### Stage 08: Criticism

```
outputs/
├── CRITICISM_REPORT.md
├── criticism_findings.md
├── feasibility_review.md
└── improvement_recommendations.md
```

**Key Pattern**: Critical analysis, reviews, recommendations

---

<!-- section_id: "2d96e709-0bcc-4596-b0fc-052b6ac2338f" -->
### Stage 09: Fixing

```
outputs/
└── FIXING_REPORT.md
```

**Key Pattern**: Fix tracking and resolution reports

---

<!-- section_id: "08ffda9a-3483-400f-a9c6-e53013616fbf" -->
### Stage 10: Current Product

```
outputs/
├── PRODUCT_RELEASE.md
├── [final deliverables]
└── setup_checklist.md
```

**Key Pattern**: Production-ready outputs and release documentation

---

<!-- section_id: "d392a425-f286-4ac7-ac0a-ec854fadb101" -->
### Stage 11: Archives

```
outputs/
└── [archived versions]
```

**Key Pattern**: Historical versions for reference

---

<!-- section_id: "4ee8a49f-9459-4eba-b43f-e5272e138f68" -->
### Universal Output Patterns

**Organization by Need vs Topic**:
- `by_need/` - Maps to tree_of_needs from Stage 01
- `by_topic/` - Cross-cutting topics that span multiple needs
- `synthesis/` - Combined insights from both

**Progress Tracking**:
- `01_*_in_progress/` - Active work
- `02_finished_*/` - Completed work (numbered to sort after in-progress)

---

<!-- section_id: "27bb3901-fca3-4381-b52c-8d2dcc000bb1" -->
### AI System Infrastructure (NOT in outputs/)

**Episodic Memory** - belongs in `.0agnostic/`, NOT `outputs/`:
```
.0agnostic/
└── episodic/
    ├── index.md           # Overview of sessions
    ├── sessions/          # Session-specific records
    └── changes/           # Change tracking
```

**Why?** Episodic memory is AI infrastructure for session continuity across tools, not a stage product.

**Proposed: Unified AI System Structure**

`.0agnostic/` mirrors tool-specific folder structure, but **content** (knowledge, prompts, rules, principles) lives in **sub-layers**:

```
.0agnostic/                    # SOURCE OF TRUTH (tool-agnostic CONFIG)
├── agents/                    # Agent configurations
├── episodic/                  # Session memory
│   ├── index.md
│   ├── sessions/
│   └── changes/
├── hooks/                     # Event hooks
│   └── scripts/
└── skills/                    # Skill definitions
                               # NOTE: NO knowledge/, prompts/, rules/
                               # Those live in sub-layers!

.claude/                       # GENERATED from .0agnostic (Claude-specific)
├── agents/
├── episodic/
├── hooks/
│   └── scripts/
├── rules/                     # Can reference sub_layer_N_04_rules/
└── skills/

.cursor/                       # GENERATED (Cursor-specific)
├── rules/                     # .mdc format, built from sub_layer rules
└── ...

.gemini/                       # GENERATED (Gemini-specific)
└── ...
```

**Content lives in sub-layers** (layer-stage system):
```
layer_N/layer_N_03_sub_layers/
├── sub_layer_N_01_prompts/           ← Prompts
├── sub_layer_N_02_knowledge_system/  ← Knowledge
├── sub_layer_N_03_principles/        ← Principles
└── sub_layer_N_04_rules/             ← Rules
```

**Benefits of This Split**:
1. **No duplication**: Content in one place (sub-layers), config in another (dot-folders)
2. **Layer cascade**: Content inherits naturally through layer hierarchy
3. **Tool flexibility**: Dot-folders reference sub-layers, transform as needed per tool
4. **Single source of truth**: Sub-layers for content, `.0agnostic/` for AI config

---

<!-- section_id: "c5ff0315-8b70-4784-ae51-e1a0b7646124" -->
### Tool-Specific Overrides, Additions, and Exclusions

Each tool-specific folder (`.claude/`, `.cursor/`, `.gemini/`) needs:
1. **Synced section** - 1:1 from `.0agnostic/` (auto-generated, don't edit)
2. **Overrides** - Tool-specific modifications to agnostic items
3. **Additions** - Tool-only items (not in `.0agnostic/`)
4. **Exclusions** - Items from `.0agnostic/` to NOT include for this tool

**Proposed Structure Option A: Separate Folders**
```
.claude/
├── 0_synced/                 # AUTO-GENERATED from .0agnostic/ (don't edit!)
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   └── skills/
├── 1_overrides/              # Claude-specific OVERRIDES (edit here)
│   ├── agents/               # Override specific agents
│   │   └── researcher.md     # Overrides .0agnostic/agents/researcher.md
│   └── skills/
├── 2_additions/              # Claude-ONLY items (not in .0agnostic)
│   ├── agents/
│   │   └── claude_specific_agent.md
│   └── skills/
│       └── claude_only_skill/
└── sync-config.yaml          # Defines exclusions and sync rules
```

**Proposed Structure Option B: Merged with Markers**
```
.claude/
├── agents/
│   ├── researcher.md         # [SYNCED] from .0agnostic
│   ├── researcher.override.md  # [OVERRIDE] Claude-specific tweaks
│   └── claude_only.md        # [ADDITION] Claude-only agent
├── skills/
├── sync-config.yaml
└── _excluded.yaml            # List of .0agnostic items to skip
```

**sync-config.yaml Example**:
```yaml
# .claude/sync-config.yaml
sync:
  from: ../.0agnostic
  mode: selective  # or "full"

include:
  - agents/
  - skills/
  - episodic/
  - hooks/

exclude:
  - agents/gemini_specific.md    # Don't sync this
  - skills/cursor_only/          # Skip entire folder

overrides:
  - agents/researcher.md         # Has local override
  - skills/coding/               # Has local tweaks
```

**Tool-Specific MD Files**:
```
entity/
├── 0AGNOSTIC.md              # SOURCE OF TRUTH
├── CLAUDE.md                 # Generated from 0AGNOSTIC.md + Claude overrides
├── AGENTS.md                 # Generated from 0AGNOSTIC.md + Cursor/Agents overrides
├── GEMINI.md                 # Generated from 0AGNOSTIC.md + Gemini overrides
├── .0agnostic/
├── .claude/
│   └── CLAUDE.override.md    # Claude-specific additions to CLAUDE.md
├── .cursor/
│   └── AGENTS.override.md    # Cursor-specific additions
└── .gemini/
    └── GEMINI.override.md    # Gemini-specific additions
```

**Generation Flow**:
```
0AGNOSTIC.md + .1claude_merge/CLAUDE.override.md → CLAUDE.md
0AGNOSTIC.md + .1cursor_merge/AGENTS.override.md → AGENTS.md
0AGNOSTIC.md + .1gemini_merge/GEMINI.override.md → GEMINI.md
```

**Benefits**:
1. **Single source**: Edit `.0agnostic/` for shared behavior
2. **Tool flexibility**: Each tool can override, add, or exclude
3. **Clear separation**: Know what's synced vs custom
4. **Auditable**: `sync-config.yaml` documents all customizations

---

<!-- section_id: "233dfe73-1ae5-4ec2-8eab-6f5460158d05" -->
### Final Architecture: Source → Merge → Output

**Three-tier folder system with numbered sorting**:

```
entity/
├── .0agnostic/                 # 0 - SOURCE OF TRUTH (tool-agnostic)
│   ├── agents/
│   ├── episodic/
│   ├── hooks/
│   └── skills/
│
│ ## TERMINAL/CLI TOOLS
│
├── .1claude_merge/             # 1 - MERGE WORKSPACE (Claude Code CLI)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   ├── CLAUDE.override.md
│   └── sync-config.yaml
│
├── .1codex_merge/              # 1 - MERGE WORKSPACE (OpenAI Codex CLI)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml        # Note: Codex uses ~/.codex/config.toml (global)
│
├── .1aider_merge/              # 1 - MERGE WORKSPACE (Aider)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
├── .1opencode_merge/           # 1 - MERGE WORKSPACE (OpenCode CLI)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
│ ## IDE EXTENSIONS
│
├── .1copilot_merge/            # 1 - MERGE WORKSPACE (GitHub Copilot)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
├── .1cursor_merge/             # 1 - MERGE WORKSPACE (Cursor)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
├── .1continue_merge/           # 1 - MERGE WORKSPACE (Continue)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
├── .1gemini_merge/             # 1 - MERGE WORKSPACE (Gemini Code Assist)
│   ├── 0_synced/
│   ├── 1_overrides/
│   ├── 2_additions/
│   └── sync-config.yaml
│
│ ## FINAL OUTPUTS (Native tool locations)
│
├── .claude/                    # Claude Code reads this (folder)
│   ├── agents/
│   ├── rules/
│   ├── skills/
│   ├── episodic/
│   └── settings.json
├── CLAUDE.md                   # Claude Code reads this (file)
│
├── .aider.conf.yml             # Aider reads this (file, not folder)
│
├── .github/                    # GitHub Copilot reads from here
│   ├── copilot-instructions.md
│   └── instructions/           # Scoped instruction files
│       └── *.instructions.md
│
├── .cursor/                    # Cursor reads this
│   └── rules/
│       └── *.mdc
│
├── .continuerc.json            # Continue reads this (file, not folder)
│
├── .opencode/                  # OpenCode reads this
│   ├── config.yaml
│   └── agent/
│       └── default.md
│
├── GEMINI.md                   # Reference only (Gemini uses IDE settings)
│
└── 0AGNOSTIC.md                # Source MD for all tools
```

**Sorting order in directory listing**:
```
.0agnostic/          # 0 - Source
.1aider_merge/       # 1 - Build workspaces (alphabetical)
.1claude_merge/
.1codex_merge/
.1continue_merge/
.1copilot_merge/
.1cursor_merge/
.1gemini_merge/
.aider.conf.yml      # Final outputs (native locations)
.claude/
.continuerc.json
.cursor/
.github/
```

**Build process (outputs to NATIVE tool locations)**:
```
                    ┌──→ .1claude_merge/   ──→ .claude/ + CLAUDE.md
                    ├──→ .1codex_merge/    ──→ (global ~/.codex/config.toml)
                    ├──→ .1aider_merge/    ──→ .aider.conf.yml
                    ├──→ .1opencode_merge/ ──→ .opencode/ + agent/default.md
.0agnostic/ ────────┼──→ .1copilot_merge/  ──→ .github/copilot-instructions.md
                    ├──→ .1cursor_merge/   ──→ .cursor/rules/*.mdc
                    ├──→ .1continue_merge/ ──→ .continuerc.json
                    └──→ .1gemini_merge/   ──→ GEMINI.md (IDE settings manual)
```

**What tools read (native, researched)**:
| Tool | Reads From | Notes |
|------|------------|-------|
| Claude Code | `.claude/` + `CLAUDE.md` | Folder + file |
| OpenAI Codex CLI | `~/.codex/config.toml` | Global only (no project config) |
| Aider | `.aider.conf.yml` | File at repo root |
| OpenCode | `.opencode/config.yaml` + `.opencode/agent/` | Folder + agent prompts |
| GitHub Copilot | `.github/copilot-instructions.md` | + `.github/instructions/*.instructions.md` |
| Cursor | `.cursor/rules/*.mdc` | MDC format with YAML frontmatter |
| Continue | `.continuerc.json` | Workspace partial config |
| Gemini Code Assist | IDE settings | No project file (manual) |

**What you edit**:
- Shared: `.0agnostic/`
- Tool-specific: `.1<tool>_merge/1_overrides/` and `.1<tool>_merge/2_additions/`

**What scripts generate**:
- `.1<tool>_merge/0_synced/` (copied from `.0agnostic/`)
- `.<tool>/` (merged final output)
- `<TOOL>.md` (from `0AGNOSTIC.md` + overrides)

**SessionStart hook** (auto-merge on session start):
```json
// .claude/settings.json
{
  "hooks": {
    "SessionStart": [{
      "type": "command",
      "command": "./scripts/agnostic-merge.sh claude"
    }]
  }
}
```

---

<!-- section_id: "99657e4c-5d51-453e-a808-ab7a0d130485" -->
### Supported Tools Reference (Researched)

**IMPORTANT**: Each tool has different native conventions. Our merge system outputs to their ACTUAL locations.

| Tool | Merge Folder | Native Output Location | MD File |
|------|--------------|------------------------|---------|
| **Claude Code** | `.1claude_merge/` | `.claude/` (folder) | `CLAUDE.md` |
| **GitHub Copilot** | `.1copilot_merge/` | `.github/copilot-instructions.md` + `.github/instructions/*.instructions.md` | (embedded in instructions file) |
| **Cursor** | `.1cursor_merge/` | `.cursor/rules/*.mdc` | `CURSORRULES.md` (legacy: `.cursorrules`) |
| **Aider** | `.1aider_merge/` | `.aider.conf.yml` (file, not folder) | (embedded in conf) |
| **Continue** | `.1continue_merge/` | `.continuerc.json` (workspace) | (embedded in config) |
| **Gemini Code Assist** | `.1gemini_merge/` | IDE settings (no project file) | `GEMINI.md` (reference only) |

**Native Tool Conventions (Researched 2025-2026)**:

<!-- section_id: "8daa6b7c-eee4-4cbb-a52c-49ddb1a8f66a" -->
### Terminal/CLI Tools

| Tool | Official Location | Format | Notes |
|------|-------------------|--------|-------|
| **Claude Code** | `.claude/` + `CLAUDE.md` | Folder + MD | Hierarchy: `~/.claude/` → project `.claude/` |
| **OpenAI Codex CLI** | `~/.codex/config.toml` | TOML | Global only, no project folder |
| **Aider** | `.aider.conf.yml` | YAML | Searches: home → repo root → cwd |

<!-- section_id: "005b457f-abed-4a92-9564-fa637a39def5" -->
### IDE Extensions

| Tool | Official Location | Format | Notes |
|------|-------------------|--------|-------|
| **GitHub Copilot** | `.github/copilot-instructions.md` | MD file | Also `.github/instructions/*.instructions.md` |
| **Cursor** | `.cursor/rules/*.mdc` | MDC (YAML frontmatter) | Legacy `.cursorrules` deprecated |
| **Continue** | `.continuerc.json` (workspace) | JSON | Global: `~/.continue/config.yaml` |
| **Gemini Code Assist** | IDE settings | JSON in IDE | No project-level file yet |

**Merge script outputs to ACTUAL tool locations**:
```bash
# Terminal/CLI tools
./scripts/agnostic-merge.sh claude    # → .claude/ + CLAUDE.md
./scripts/agnostic-merge.sh codex     # → ~/.codex/config.toml (global)
./scripts/agnostic-merge.sh aider     # → .aider.conf.yml

# IDE extensions
./scripts/agnostic-merge.sh copilot   # → .github/copilot-instructions.md
./scripts/agnostic-merge.sh cursor    # → .cursor/rules/*.mdc
./scripts/agnostic-merge.sh continue  # → .continuerc.json
./scripts/agnostic-merge.sh gemini    # → GEMINI.md (IDE settings manual)

# All at once
./scripts/agnostic-merge.sh all       # Build all tools
```

**Sources**:
- [Claude Code Settings](https://code.claude.com/docs/en/settings)
- [OpenAI Codex CLI Config](https://developers.openai.com/codex/config-basic/)
- [Aider Config Docs](https://aider.chat/docs/config/aider_conf.html)
- [GitHub Copilot Instructions](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [Cursor Rules Docs](https://docs.cursor.com/context/rules)
- [Continue Config Reference](https://docs.continue.dev/reference)
- [Gemini Code Assist Overview](https://developers.google.com/gemini-code-assist/docs/overview)

---

<!-- section_id: "1554167b-8183-4998-a9bf-dc47c5102fba" -->
## Tool Context Systems (Researched 2025-2026)

This section documents how each AI coding tool handles system prompts, static context, and dynamic context.

---

<!-- section_id: "3288d994-8998-487e-8643-fa8b8dd43ede" -->
### Claude Code CLI

**Main Instruction File**: `CLAUDE.md` (project root) + `~/.claude/CLAUDE.md` (global)

**Context Hierarchy** (in priority order):
1. `~/.claude/CLAUDE.md` - Global (applies to all projects)
2. `<project>/.claude/CLAUDE.md` - Project-level
3. Files in `.claude/` folder hierarchy

**Folder Structure** (`.claude/`):
| Folder | Purpose | Loading |
|--------|---------|---------|
| `rules/` | Modular rules with YAML frontmatter | Recursive discovery of all `.md` files |
| `skills/` | Reusable prompts/procedures | Recursive (monorepo support) |
| `agents/` | Subagent configurations | Flat (no subdirectory traversal) |
| `hooks/` | Event hooks (SessionStart, etc.) | Scripts directory |
| `settings.json` | Tool configuration | Direct load |

**Static Context** (always loaded):
- `CLAUDE.md` files in hierarchy (global → project)
- Rules with `alwaysApply: true` in frontmatter
- Settings from `settings.json`

**Dynamic Context** (conditionally loaded):
- Rules with globs that match current file
- Skills invoked by user or agent
- Subagents spawned for specific tasks

**Rule Format** (`.md` with YAML frontmatter):
```markdown
---
description: Description for rule discovery
globs: "src/**/*.ts"      # Auto-attach when matching files open
alwaysApply: false        # true = always include
---
# Rule content here
```

**Skills System**:
- Skills stored in `~/.config/claude/skills/`, `.claude/skills/`, or plugin-provided
- Invoked via `/skill-name` or automatically by Claude
- Skills inject instructions into conversation context
- Can bundle scripts to extend functionality

**Hooks** (SessionStart example):
```json
{
  "hooks": {
    "SessionStart": [{
      "type": "command",
      "command": "./scripts/setup.sh"
    }]
  }
}
```

**Sources**:
- [Claude Code Docs - Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Claude Agent Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
- [Piebald-AI System Prompts](https://github.com/Piebald-AI/claude-code-system-prompts)
- [Writing a Good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

---

<!-- section_id: "988eaa23-da3a-4fa7-8eef-1a3311e3fd18" -->
### OpenAI Codex CLI

**Main Instruction File**: `AGENTS.md` (project root) - created via `/init` command

**Config Location**: `~/.codex/config.toml` (global only, no project folder)

**Context System**:
| Type | Source | Notes |
|------|--------|-------|
| System instructions | Built-in + `experimental_instructions_file` | Can override built-in via `--config` |
| Developer instructions | `developer_instructions` config | Additional injection |
| Project context | `AGENTS.md` | Auto-read from project root |
| Skills | `~/.codex/skills/` | Reusable instruction bundles |

**Static Context** (always loaded):
- Built-in system prompt (~50 instructions)
- Global config from `~/.codex/config.toml`
- `AGENTS.md` file in project root

**Dynamic Context** (conditionally loaded):
- Skills (metadata only loaded at startup, body on-demand)
- File context based on conversation
- Resumed session transcripts

**Configuration Options**:
```toml
# ~/.codex/config.toml
model = "gpt-5.1-codex-max"
approval_mode = "suggest"
sandbox = true
```

**Skills System**:
- Stored in `~/.codex/skills/` directory
- Each skill has: name, description, detailed instructions
- Only metadata injected into context (saves tokens)
- Full body loaded when skill is invoked

**Override Built-in Instructions**:
```bash
codex --config experimental_instructions_file=/path/to/override.md
codex --config developer_instructions="Additional context..."
```

**Session Resume**:
- Transcripts stored locally
- Use `codex resume` to continue previous session
- Preserves repository state and instructions

**Sources**:
- [Codex CLI Features](https://developers.openai.com/codex/cli/features/)
- [Codex Basic Configuration](https://developers.openai.com/codex/config-basic/)
- [Codex Advanced Configuration](https://developers.openai.com/codex/config-advanced/)
- [Codex Custom System Prompt Discussion](https://github.com/openai/codex/discussions/7296)

---

<!-- section_id: "380e739a-8cf7-4fbd-9b87-9ff04fa95973" -->
### Google Gemini CLI

**Main Instruction File**: `GEMINI.md` (hierarchical - global, ancestor, sub-directory)

**Config Location**: `~/.gemini/settings.json` (global) + project `settings.json`

**Context Hierarchy** (concatenated with path separators):
1. `~/.gemini/GEMINI.md` - Global instructions
2. Ancestor `GEMINI.md` files - From current dir up to project root
3. Sub-directory `GEMINI.md` files - Component-specific instructions

**Context File Discovery**:
- CLI searches UP from current directory for `GEMINI.md` files
- Also scans DOWN into subdirectories
- All found files concatenated into system prompt
- Footer displays count of loaded context files

**Static Context** (always loaded):
- All `GEMINI.md` files in hierarchy
- Settings from `settings.json`
- MCP server tool definitions

**Dynamic Context** (conditionally loaded):
- Imported files via `@path/to/file.md` syntax
- Tool results from MCP servers

**Modular Context (Imports)**:
```markdown
# GEMINI.md
## Base Instructions
...

@./shared/coding-standards.md
@./shared/api-guidelines.md
```

**Settings File** (`settings.json`):
```json
{
  "theme": "dark",
  "defaultModel": "gemini-pro",
  "mcpServers": [...]
}
```

**System Prompt Override**:
- Use `GEMINI_SYSTEM_MD` environment variable
- Replaces built-in system instructions

**Memory Commands**:
| Command | Purpose |
|---------|---------|
| `/memory refresh` | Force re-scan all context files |
| `/memory show` | Display combined context |

**Sources**:
- [Gemini CLI Configuration](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/configuration.md)
- [Gemini CLI Tutorial](https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718)
- [Gemini CLI Cheatsheet](https://www.philschmid.de/gemini-cli-cheatsheet)

---

<!-- section_id: "2d57553f-9c78-4475-a0be-537662c7815c" -->
### OpenCode CLI

**Main Instruction File**: Custom `prompt` config pointing to markdown file

**Config Location**: `~/.opencode/config.yaml` (global) + `.opencode/config.yaml` (project)

**Agent System**:
| Built-in Agent | Purpose | Access |
|----------------|---------|--------|
| `build` | Full access development | Default |
| `plan` | Read-only analysis | Tab to switch |

**Custom Agents**:
- Define in `~/.config/opencode/agent/` or `.opencode/agent/`
- Each agent = markdown file with system prompt
- Configure via `opencode agent create`

**Static Context** (always loaded):
- Built-in agent system prompt
- Global config settings
- Model configuration

**Dynamic Context** (conditionally loaded):
- Custom agent prompts when switched
- Turn-limit summarization prompt
- Custom command prompts

**Configuration**:
```yaml
# ~/.opencode/config.yaml or .opencode/config.yaml
model: claude-3-5-sonnet
agent:
  name: custom-agent
  prompt: ./prompts/custom.md
  tools:
    - read
    - write
    - bash
```

**Custom Commands**:
- Predefined prompts stored as markdown files
- Quick-send to AI assistant
- Stored in `~/.config/opencode/commands/` or `.opencode/commands/`

**Turn Limit Behavior**:
- When limit reached, special summarization prompt injected
- Agent summarizes work and recommends remaining tasks

**Sources**:
- [OpenCode CLI Docs](https://opencode.ai/docs/cli/)
- [OpenCode Agents](https://opencode.ai/docs/agents/)
- [OpenCode Config](https://opencode.ai/docs/config/)
- [OpenCode Commands](https://opencode.ai/docs/commands/)

---

<!-- section_id: "fb8f01db-1598-48c1-a1ba-4240e8b28705" -->
### Aider

**Main Instruction Files**: `.aider.conf.yml` + `.aider.model.settings.yml`

**Config Search Order**: Home directory → Git repo root → Current directory

**Configuration Files**:
| File | Purpose | Format |
|------|---------|--------|
| `.aider.conf.yml` | Main config (model, behavior) | YAML |
| `.aider.model.settings.yml` | Model-specific settings | YAML |
| `.env` | API keys for all providers | ENV |

**Static Context** (always loaded):
- System prompt based on model
- Configuration from `.aider.conf.yml`
- Model settings from `.aider.model.settings.yml`

**Dynamic Context** (conditionally loaded):
- Repository map (when `use_repo_map: true`)
- File contents added to chat
- Git diff context

**Main Config** (`.aider.conf.yml`):
```yaml
# .aider.conf.yml
model: claude-3-5-sonnet
edit-format: diff
auto-commits: true
weak-model: gpt-4o-mini
```

**Model Settings** (`.aider.model.settings.yml`):
```yaml
# .aider.model.settings.yml
- name: claude-3-5-sonnet
  edit_format: diff
  use_repo_map: true
  cache_control: true
  extra_params:
    max_tokens: 8192
- name: o1-preview
  edit_format: whole
  use_repo_map: false
  accepts_settings:
    - reasoning_effort
```

**Environment Variables**:
- All options can be set via `AIDER_xxx` env vars
- Keys stored in `.env` file
- Example: `AIDER_MODEL=claude-3-5-sonnet`

**Key Model Settings**:
| Setting | Purpose |
|---------|---------|
| `edit_format` | How edits are presented (diff, whole, etc.) |
| `use_repo_map` | Include repository structure |
| `weak_model_name` | Model for simple tasks |
| `reasoning_effort` | For reasoning models |
| `thinking_tokens` | Budget for Anthropic reasoning |

**Sources**:
- [Aider YAML Config](https://aider.chat/docs/config/aider_conf.html)
- [Aider Configuration Overview](https://aider.chat/docs/config.html)
- [Aider Model Settings](https://aider.chat/docs/config/adv-model-settings.html)

---

<!-- section_id: "3bc3c68d-15fb-4239-beb4-53d0ad2d548f" -->
### Cursor (IDE + CLI)

**Main Instruction File**: `.cursor/rules/*.mdc` (MDC format with YAML frontmatter)

**Legacy**: `.cursorrules` (deprecated, still functional)

**Rule Format** (`.mdc` with YAML frontmatter):
```markdown
---
description: "Short description for rule discovery"
globs: "src/**/*.ts"
alwaysApply: false
---
# Rule Title

Rule content with instructions...
```

**Frontmatter Fields**:
| Field | Type | Purpose |
|-------|------|---------|
| `description` | string | Shown in UI, used for filtering |
| `globs` | string | Comma-separated file patterns |
| `alwaysApply` | boolean | If true, always included |

**Rule Types** (inferred from frontmatter):
| Type | Configuration | Behavior |
|------|---------------|----------|
| **Always** | `alwaysApply: true` | Always attached |
| **Auto-Attach** | globs defined, `alwaysApply: false` | Attached when file matches |
| **Agent** | description present, no globs/always | Used when AI queries rules |
| **Manual** | No description/globs/always | Must be manually referenced |

**Static Context** (always loaded):
- Rules with `alwaysApply: true`
- Settings from Cursor preferences
- MCP server definitions

**Dynamic Context** (conditionally loaded):
- Rules with matching globs
- Agent-type rules (queried by AI)
- Manual rules (user-referenced)

**Settings Location**:
- UI: Settings > Features > Chat & Composer > Rules for AI
- Can set coding styles, naming conventions, architecture preferences

**CLI/Terminal Usage**:
- Agent mode from CLI with MCP support
- Rule integration works in terminal
- Command approval and sandboxing available

**YOLO Mode**:
- Executes commands without confirmation
- Enable: Settings > Features > Chat & Composer > Enable YOLO mode
- Use with caution

**Version 2.2+ Changes**:
- New rules created as folders: `.cursor/rules/my-rule/RULE.md`
- Old `.mdc` files still functional
- Folders improve maintainability

**Sources**:
- [Cursor Rules Docs](https://cursor.com/docs/agent/overview)
- [Cursor Agent Modes](https://cursor.com/docs/agent/modes)
- [Cursor CLI Usage](https://cursor.com/docs/cli/using)
- [MDC Best Practices Forum](https://forum.cursor.com/t/my-best-practices-for-mdc-rules-and-troubleshooting/50526)

---

<!-- section_id: "0bd9eaa1-ac94-45e2-9482-6d31759acfa8" -->
### GitHub Copilot

**Main Instruction File**: `.github/copilot-instructions.md`

**Additional Instructions**: `.github/instructions/*.instructions.md` (scoped)

**Hierarchy** (priority order):
1. Personal instructions (highest)
2. Repository instructions (`.github/copilot-instructions.md`)
3. Organization instructions (lowest)

**Static Context** (always loaded):
- `.github/copilot-instructions.md` - Repository-wide
- Personal instructions from settings

**Dynamic Context** (conditionally loaded):
- Path-specific `*.instructions.md` files with `applyTo` field

**Repository Instructions** (`.github/copilot-instructions.md`):
```markdown
# Project Guidelines

- Use TypeScript for all new code
- Follow ESLint configuration
- Write tests for all new features
```

**Scoped Instructions** (`.github/instructions/*.instructions.md`):
```markdown
---
applyTo: "docs/**/*.md"
---
# Documentation Guidelines

- Use clear, concise language
- Include code examples
- Keep sections short
```

**File Locations**:
| Type | Location |
|------|----------|
| Repository-wide | `.github/copilot-instructions.md` |
| Scoped | `.github/instructions/*.instructions.md` |
| Personal | IDE settings / `global-copilot-instructions.md` |

**Format**:
- Natural language in Markdown
- Whitespace between instructions ignored
- Can be single paragraph or bullet points
- Scoped files use `applyTo` YAML frontmatter

**Best Practices**:
- Keep instructions short and self-contained
- Clear, specific instructions work better
- Very long files may result in overlooked instructions

**Sources**:
- [VS Code Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [GitHub Copilot Instructions Docs](https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- [Copilot Best Practices](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)

---

<!-- section_id: "2616640b-bbcf-4df0-ae61-2b27c16446c6" -->
### Continue

**Main Config Files**: `config.yaml` or `config.json` (project) + `~/.continue/config.yaml` (global)

**Workspace Override**: `.continuerc.json` (partial config)

**Configuration Defines**:
| Setting | Purpose |
|---------|---------|
| `models` | Chat, edit, apply, embed, rerank model roles |
| `contextProviders` | Available context sources |
| `rules` | System message/rules for LLM |
| `slashCommands` | Custom slash commands |

**Static Context** (always loaded):
- Models configuration
- Rules/system message
- Global settings

**Dynamic Context** (conditionally loaded):
- Context providers (problems, tree, url, search, folder, codebase, web, open, docs, terminal)
- MCP server tools

**Config Format** (`config.yaml`):
```yaml
models:
  - name: claude-3-5-sonnet
    provider: anthropic
    contextLength: 200000
    maxTokens: 8192

contextProviders:
  - name: codebase
    onlyMyCode: true
  - name: docs
  - name: web

rules:
  - "Always use TypeScript"
  - "Follow project conventions"
```

**Workspace Override** (`.continuerc.json`):
```json
{
  "models": [...],
  "rules": ["Project-specific rules"]
}
```

**Context Providers**:
| Provider | Purpose |
|----------|---------|
| `problems` | IDE diagnostics |
| `tree` | File tree structure |
| `codebase` | Repository code |
| `docs` | Documentation |
| `web` | Web search |
| `terminal` | Terminal output |

**MCP Support**:
- Model Context Protocol for custom tools
- Configure MCP servers in config
- Tools discovered automatically

**Sources**:
- [Continue config.yaml Reference](https://docs.continue.dev/reference)
- [Continue Complete Guide](https://www.booststash.com/continue-dev-the-ai-coder-that-actually-works-in-2025/)

---

<!-- section_id: "de5a2f95-e297-40a8-afc8-59df51ddde03" -->
## Agnostic to Tool-Specific Mapping

<!-- section_id: "bbf39091-551f-426c-a2da-9277639e6361" -->
### Concept Matrix

| Agnostic Concept | Claude Code | Codex CLI | Gemini CLI | OpenCode | Aider | Cursor | Copilot | Continue |
|------------------|-------------|-----------|------------|----------|-------|--------|---------|----------|
| **Main MD file** | `CLAUDE.md` | `AGENTS.md` | `GEMINI.md` | Config prompt | N/A | `.cursorrules` | `copilot-instructions.md` | N/A |
| **Config folder** | `.claude/` | `~/.codex/` | `~/.gemini/` | `.opencode/` | N/A | `.cursor/` | `.github/` | `.continue/` |
| **Config format** | JSON + MD | TOML | JSON | YAML | YAML | MDC | MD | YAML/JSON |
| **Rules/Instructions** | `.claude/rules/` | `AGENTS.md` | `GEMINI.md` hierarchy | Agent prompts | Config | `.cursor/rules/` | `.github/instructions/` | `rules:` in config |
| **Skills/Commands** | `.claude/skills/` | Skills folder | N/A | Commands | N/A | N/A | N/A | `slashCommands:` |
| **Agents** | `.claude/agents/` | N/A | N/A | Agent configs | N/A | N/A | N/A | N/A |
| **Hooks/Events** | `hooks/` in settings | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **Context hierarchy** | Global → Project | Global + Project MD | Global → Ancestor → Sub-dir | Global + Project | Home → Repo → CWD | Settings + Rules | Personal → Repo → Org | Global + Workspace |
| **Dynamic rules** | Globs in frontmatter | N/A | `@import` | N/A | N/A | Globs in frontmatter | `applyTo` frontmatter | Context providers |

---

<!-- section_id: "4ef3dc45-c9d7-4b7e-921c-76ac9afafc8c" -->
### Mapping from .0agnostic/ to Tool Outputs

**Source Structure** (`.0agnostic/`):
```
.0agnostic/
├── instructions/           # → Tool-specific MD files
│   ├── base.md             # Core instructions
│   ├── coding-standards.md # Coding rules
│   └── project-specific.md # Project context
├── rules/                  # → Tool rule systems
│   ├── always/             # Always-apply rules
│   │   └── security.md
│   └── conditional/        # Glob-based rules
│       ├── typescript.md
│       └── python.md
├── agents/                 # → Claude agents, OpenCode agents
├── skills/                 # → Claude skills, Codex skills
├── hooks/                  # → Claude hooks (others N/A)
└── context-providers/      # → Continue context providers
```

**Generation Mappings**:

| Source | Claude Code | Cursor | Copilot | Gemini | Continue |
|--------|-------------|--------|---------|--------|----------|
| `instructions/base.md` | `CLAUDE.md` | `.cursorrules` | `copilot-instructions.md` | `GEMINI.md` | `rules:` |
| `rules/always/` | `.claude/rules/` (alwaysApply: true) | `.cursor/rules/` (alwaysApply: true) | Main instructions | Main `GEMINI.md` | `rules:` |
| `rules/conditional/` | `.claude/rules/` (with globs) | `.cursor/rules/` (with globs) | `.github/instructions/` (with applyTo) | Imported files | N/A |
| `agents/` | `.claude/agents/` | N/A | N/A | N/A | N/A |
| `skills/` | `.claude/skills/` | N/A | N/A | N/A | `slashCommands:` |
| `hooks/` | `.claude/settings.json` hooks | N/A | N/A | N/A | N/A |

---

<!-- section_id: "99cae584-4ea9-47ed-947c-05f14677e36e" -->
### Build Script Requirements

The `agnostic-merge.sh` script must handle these transformations:

**1. Claude Code** (most complete support):
```bash
# Instructions → CLAUDE.md
cat .0agnostic/instructions/*.md > CLAUDE.md

# Rules → .claude/rules/ with frontmatter
for rule in .0agnostic/rules/always/*.md; do
  add_frontmatter "alwaysApply: true" "$rule" ".claude/rules/"
done
for rule in .0agnostic/rules/conditional/*.md; do
  # Parse glob from filename or metadata
  add_frontmatter "globs: $glob" "$rule" ".claude/rules/"
done

# Copy agents, skills, hooks directly
cp -r .0agnostic/agents/ .claude/agents/
cp -r .0agnostic/skills/ .claude/skills/
```

**2. Cursor** (rules with MDC format):
```bash
# Instructions → .cursorrules or .cursor/rules/base.mdc
cat .0agnostic/instructions/*.md > .cursor/rules/base.mdc

# Rules → .cursor/rules/*.mdc with MDC frontmatter
for rule in .0agnostic/rules/**/*.md; do
  convert_to_mdc "$rule" ".cursor/rules/"
done
```

**3. GitHub Copilot** (single file + scoped):
```bash
# Instructions → .github/copilot-instructions.md
cat .0agnostic/instructions/*.md > .github/copilot-instructions.md

# Conditional rules → .github/instructions/*.instructions.md
for rule in .0agnostic/rules/conditional/*.md; do
  add_applyto_frontmatter "$rule" ".github/instructions/"
done
```

**4. Gemini CLI** (hierarchical GEMINI.md + imports):
```bash
# Instructions → GEMINI.md with @imports
echo "# Project Instructions" > GEMINI.md
for file in .0agnostic/instructions/*.md; do
  echo "@.0agnostic/instructions/$(basename $file)" >> GEMINI.md
done
```

**5. Continue** (config.yaml rules section):
```bash
# Instructions + Rules → rules: in config.yaml
yq '.rules = []' -i .continuerc.json
for rule in .0agnostic/instructions/*.md .0agnostic/rules/always/*.md; do
  content=$(cat "$rule")
  yq ".rules += [\"$content\"]" -i .continuerc.json
done
```

**6. Aider** (no instructions file - config only):
```bash
# Aider doesn't have instruction files
# Just copy config if present
cp .0agnostic/aider-config.yml .aider.conf.yml 2>/dev/null || true
```

**7. OpenCode** (agent prompt files):
```bash
# Instructions → .opencode/agent/default.md
cat .0agnostic/instructions/*.md > .opencode/agent/default.md
```

---

<!-- section_id: "a2757e8a-8670-446f-9d28-5d221940c707" -->
## AI Coding Tool Rankings & Prioritization (2025-2026)

<!-- section_id: "7b076635-51b9-42ab-8431-903c9a0e451c" -->
### Quick Reference: When to Use Which Tool

| Task Type | Best Tool | Runner-up | Why |
|-----------|-----------|-----------|-----|
| **Large codebase refactoring** | Claude Code | Cursor | 200k context window, agentic multi-file ops |
| **Real-time code completion** | Cursor / Copilot | Continue | IDE-integrated, instant suggestions |
| **Terminal-first workflows** | Claude Code | Aider | Native terminal, no GUI needed |
| **Model flexibility (BYOK)** | Aider | OpenCode | Supports all LLMs including local |
| **Git-integrated workflows** | Aider | Claude Code | Auto-commits, history preservation |
| **Complex debugging** | Claude Code | Cursor | Step-by-step reasoning |
| **Legacy code understanding** | Claude Code | Aider | Excellent documentation generation |
| **Quick prototyping** | Cursor | Copilot | Fast iteration, visual feedback |
| **Autonomous task completion** | Codex CLI | Claude Code | Runs in isolated environment, end-to-end |
| **Team/Enterprise use** | Copilot | Cursor | Seat-based pricing, admin controls |
| **Free high-volume usage** | Gemini CLI | Aider (local) | Free tier generous |
| **Learning/education** | Claude Code | Cursor | Explanatory output, reasoning visible |

---

<!-- section_id: "ab02276a-55bb-4ed2-a785-363a217c3c7a" -->
### Tool Tier Rankings

#### Tier 1: Primary Recommendations

| Tool | Rating | Best For | Limitations |
|------|--------|----------|-------------|
| **Claude Code** | ⭐⭐⭐⭐⭐ | Large codebases, refactoring, complex reasoning, terminal workflows | Not open source, context loss in very long sessions |
| **Cursor** | ⭐⭐⭐⭐⭐ | IDE experience, real-time completion, visual workflows | Subscription cost, VS Code fork only |

#### Tier 2: Strong Alternatives

| Tool | Rating | Best For | Limitations |
|------|--------|----------|-------------|
| **Aider** | ⭐⭐⭐⭐ | Git integration, model flexibility, BYOK cost control | Resource hungry, not agentic, no MCP |
| **GitHub Copilot** | ⭐⭐⭐⭐ | Teams, GitHub integration, inline suggestions | Less autonomous than CLI tools |
| **Codex CLI** | ⭐⭐⭐⭐ | Autonomous tasks, isolated execution, complex algorithms | Global config only, no project customization |

#### Tier 3: Specialized Use Cases

| Tool | Rating | Best For | Limitations |
|------|--------|----------|-------------|
| **Gemini CLI** | ⭐⭐⭐½ | Free usage, Google ecosystem, hierarchical context | IDE settings manual, newer tool |
| **OpenCode** | ⭐⭐⭐½ | Open source, custom agents, terminal TUI | Smaller community, less mature |
| **Continue** | ⭐⭐⭐ | IDE integration, open source, context providers | Configuration complexity |

---

<!-- section_id: "287e2ef6-55fd-479a-ba6b-7c92f9f47899" -->
### Detailed Tool Profiles

#### Claude Code CLI
**Category**: Terminal-first agentic coding

**Strengths**:
- 200k token context window (largest available)
- Excellent for 50k+ LOC codebases
- Superior reasoning and explanation
- Best legacy code understanding
- MCP integration for extensibility
- Skills, agents, hooks ecosystem

**Weaknesses**:
- Not open source
- Context management in very long sessions
- Terminal-only (no IDE integration)
- Cost can add up for heavy usage

**Best Use Cases**:
1. Multi-file refactoring across large codebases
2. Complex debugging requiring step-by-step reasoning
3. Documentation generation and legacy code analysis
4. Automated testing and project setup
5. System-wide automation tasks

**Cost Model**: Pay-per-token (Claude API) or Claude Max subscription

---

#### Cursor
**Category**: AI-augmented IDE

**Strengths**:
- Real-time code completion in editor
- Visual checkpoint system for complex work
- Watch AI's thought process
- Fast iteration cycles
- Familiar VS Code interface
- Highest user ratings (~4.9/5)

**Weaknesses**:
- Subscription-based pricing
- VS Code ecosystem only
- Less autonomous than CLI tools
- Smaller context than Claude Code

**Best Use Cases**:
1. Day-to-day coding with inline assistance
2. Rapid prototyping and iteration
3. Learning from AI suggestions
4. Visual code review and editing
5. Teams familiar with VS Code

**Cost Model**: Pro subscription ($20/month) or Business

---

#### Aider
**Category**: Git-native terminal AI

**Strengths**:
- Model agnostic (Claude, GPT, Gemini, local models)
- BYOK - no subscription, control your costs
- Native Git integration with auto-commits
- Intelligent codebase mapping
- Open source and customizable

**Weaknesses**:
- Not agentic (no autonomous task completion)
- No MCP support
- Resource intensive on weaker machines
- Higher per-command cost (~$0.70 avg)

**Best Use Cases**:
1. Git-centric workflows requiring commit history
2. Teams wanting model flexibility
3. Cost-conscious developers (BYOK)
4. Projects requiring local/private models
5. Open source contributors

**Cost Model**: BYOK (API costs only)

---

#### GitHub Copilot
**Category**: IDE code completion

**Strengths**:
- Deep GitHub integration
- Multiple model support (GPT-4, Claude, Gemini)
- Team/enterprise management
- Works in multiple IDEs
- Strong inline suggestions

**Weaknesses**:
- Less autonomous than CLI tools
- Context limited compared to Claude Code
- Subscription required

**Best Use Cases**:
1. Teams using GitHub for version control
2. Inline code completion during active coding
3. Enterprise environments needing admin controls
4. Cross-IDE consistency (VS Code, JetBrains, etc.)
5. Collaborative projects

**Cost Model**: Individual ($10/month), Business ($19/user/month), Enterprise

---

#### OpenAI Codex CLI
**Category**: Autonomous task completion

**Strengths**:
- Runs in isolated cloud environment
- End-to-end feature implementation
- Executes code, runs tests, iterates
- Strong algorithm generation
- Multi-language support

**Weaknesses**:
- Global config only (no project customization)
- Works asynchronously (not real-time)
- Less mature ecosystem than Claude Code

**Best Use Cases**:
1. Complete feature implementation ("implement auth system")
2. Complex multi-file projects
3. Automated code testing and iteration
4. Tasks that can run in background
5. Advanced algorithm development

**Cost Model**: API usage-based

---

#### Gemini CLI
**Category**: Google-ecosystem terminal AI

**Strengths**:
- Generous free tier
- Hierarchical context system
- @import for modular configs
- Google Cloud integration
- Active development

**Weaknesses**:
- IDE settings require manual config
- Newer tool, less battle-tested
- Context system still maturing

**Best Use Cases**:
1. High-volume usage on budget
2. Google Cloud projects
3. Hierarchical project documentation
4. Teams already in Google ecosystem

**Cost Model**: Free tier + API pricing

---

#### OpenCode CLI
**Category**: Open source terminal AI

**Strengths**:
- Fully open source
- Custom agent definitions
- Go-based (fast, portable)
- TUI interface option
- Custom commands

**Weaknesses**:
- Smaller community
- Less mature than established tools
- Limited ecosystem

**Best Use Cases**:
1. Open source purists
2. Custom agent development
3. Teams needing full control
4. Lightweight terminal workflows

**Cost Model**: BYOK (API costs only)

---

<!-- section_id: "74e3818e-7e00-4024-a899-eb8c219f743d" -->
### Recommended Tool Combinations

#### For Solo Developers
```
Primary: Claude Code (complex work) + Cursor (daily coding)
Secondary: Aider (when needing different models)
```

#### For Small Teams
```
Primary: Cursor (shared rules) + GitHub Copilot (team management)
Secondary: Claude Code (large refactors)
```

#### For Enterprise
```
Primary: GitHub Copilot Enterprise (admin, compliance)
Secondary: Cursor Business (power users)
Claude Code (senior devs doing architecture)
```

#### For Budget-Conscious
```
Primary: Aider with local models or DeepSeek
Secondary: Gemini CLI (free tier)
```

#### For Open Source Projects
```
Primary: Aider (model flexibility, Git native)
Secondary: OpenCode (fully open source)
```

---

<!-- section_id: "93951e71-cac7-4af2-8fb2-c204105b6e09" -->
### Migration Paths

**From Copilot to Claude Code**:
- Move `.github/copilot-instructions.md` → `CLAUDE.md`
- Convert scoped instructions to `.claude/rules/` with frontmatter

**From Cursor to Claude Code**:
- Move `.cursor/rules/*.mdc` → `.claude/rules/` (similar frontmatter)
- Adapt to terminal workflow

**From Claude Code to Multi-Tool**:
- Use `.0agnostic/` as source of truth
- Generate tool-specific configs via merge script

---

<!-- section_id: "f784536d-21e3-4393-8f9a-77ee70363f6a" -->
### Sources for Rankings
- [Render AI Coding Agents Benchmark](https://render.com/blog/ai-coding-agents-benchmark)
- [Claude Code vs Cursor Comparison](https://www.qodo.ai/blog/claude-code-vs-cursor/)
- [Artificial Analysis Coding Agents Comparison](https://artificialanalysis.ai/insights/coding-agents-comparison)
- [Agentic CLI Tools Compared](https://research.aimultiple.com/agentic-cli/)
- [OpenAI Codex vs Aider vs Claude Code](https://rumjahn.com/openai-codex-vs-aider-vs-claude-code-which-terminal-ai-coding-editor-is-best-in-2025/)
- [2025's Best AI Coding Tools Comparison](https://dev.to/stevengonsalvez/2025s-best-ai-coding-tools-real-cost-geeky-value-honest-comparison-4d63)

---

<!-- section_id: "400be2e1-6bdc-497c-9c6c-d88ecdb4fa73" -->
### Official vs Custom Folders

**Claude Code Official** (`.claude/`):
| Folder | Status | Purpose |
|--------|--------|---------|
| `skills/` | ✅ Official | Custom instructions (replaces commands) |
| `agents/` | ✅ Official | Subagent configurations |
| `rules/` | ✅ Official | Modular rules with YAML frontmatter |
| `hooks/` | ✅ Official | Event hooks |
| `hooks/scripts/` | ✅ Official | Hook scripts |
| `commands/` | ⚠️ Deprecated | Use skills instead |
| `settings.json` | ✅ Official | Tool configuration |

**Cursor Official** (`.cursor/`):
| Folder | Status | Purpose |
|--------|--------|---------|
| `rules/` | ✅ Official | Rules (`.mdc` files) |
| `mcp/` | ✅ Official | MCP server configs |

**Architecture Decision: Sub-Layers vs Dot-Folders**

**Sub-Layers** = Content storage (part of layer-stage system):
```
layer_N/layer_N_03_sub_layers/
├── sub_layer_N_01_prompts/           ← Prompts live HERE
├── sub_layer_N_02_knowledge_system/  ← Knowledge lives HERE
├── sub_layer_N_03_principles/        ← Principles live HERE
├── sub_layer_N_04_rules/             ← Rules live HERE
└── sub_layer_N_05+_setup_dependant/
```

**Dot-Folders** = Tool configuration (references sub-layers):
```
.0agnostic/                    # Tool-agnostic config
├── agents/
├── episodic/                  # Session memory (AI infra)
├── hooks/
├── skills/
└── [NO knowledge/, prompts/]  # These are in sub-layers!

.claude/                       # Claude-specific (generated)
├── agents/
├── episodic/
├── hooks/
├── rules/                     # Can reference sub_layer_N_04_rules/
└── skills/
```

**Key Principle**:
- **Sub-layers** = WHERE content lives (prompts, knowledge, rules, principles)
- **Dot-folders** = HOW tools access/configure (skills, agents, hooks, episodic)
- Dot-folders can **reference** or **build from** sub-layers, not duplicate them

**Benefits**:
1. No duplication between sub-layers and dot-folders
2. Layer-stage system remains the organizational backbone
3. Dot-folders stay lean (config only, not content)
4. Content inherits layer cascade naturally

---

<!-- section_id: "3293db2a-70fa-4019-b643-62609e789a6e" -->
## Entity Instantiation Patterns

<!-- section_id: "9fb77cef-3525-4f15-b64b-1b2afb953d2b" -->
### Research Project (Layer -1)

```
layer_-1_research/
└── layer_-1_<project_name>/
    ├── CLAUDE.md
    ├── layer_-1_group/
    │   ├── layer_-1_02_manager_handoff_documents/
    │   └── layer_-1_99_stages/
    │       ├── stage_-1_00_stage_registry/
    │       ├── stage_-1_01_request_gathering/
    │       ├── stage_-1_02_research/
    │       │   └── outputs/01_understanding_in_progress/by_topic/
    │       ├── stage_-1_03_instructions/
    │       ├── stage_-1_04_design/
    │       ├── stage_-1_05_planning/
    │       ├── stage_-1_06_development/
    │       ├── stage_-1_07_testing/
    │       ├── stage_-1_08_criticism/
    │       ├── stage_-1_09_fixing/
    │       ├── stage_-1_10_current_product/
    │       └── stage_-1_11_archives/
    └── layer_0_group/
        └── layer_0_features/   # Features within the research project
```

<!-- section_id: "284bb17a-358c-4c99-b30b-49dc1ecd24f5" -->
### Project (Layer 1)

```
layer_1/layer_1_projects/
└── layer_1_project_<name>/
    ├── CLAUDE.md
    ├── layer_1_00_layer_registry/
    ├── layer_1_01_ai_manager_system/
    ├── layer_1_02_manager_handoff_documents/
    │   ├── layer_1_00_to_universal/
    │   └── layer_1_01_to_specific/
    ├── layer_1_03_sub_layers/
    │   ├── sub_layer_1_01_prompts/
    │   ├── sub_layer_1_02_knowledge_system/
    │   └── ...
    └── layer_1_99_stages/
        ├── stage_1_01_request_gathering/
        ├── stage_1_02_research/
        └── ...
```

<!-- section_id: "b2ae03b6-2d8e-489b-adab-bdb86385de6f" -->
### Feature (Layer 2, nested under project)

```
layer_1_project_<name>/
└── layer_2/
    └── layer_2_features/
        └── layer_2_feature_<name>/
            ├── CLAUDE.md
            ├── layer_1/   # Feature's internal workings
            └── layer_2/   # Child features/components
```

<!-- section_id: "464c7848-fd1e-4bd2-b33e-ef347316bcad" -->
### Component (Layer 3)

```
layer_2_feature_<name>/
└── layer_3/
    └── layer_3_components/
        └── layer_3_component_<name>/
```

---

<!-- section_id: "f94656f2-a2fc-4274-b93a-727b5e248695" -->
## Entity Creation Process

From the `entity-creation` skill:

1. **Determine entity type and parent** (project/feature/component)
2. **Calculate next available number** (XX)
3. **Create directory structure**
4. **Initialize CLAUDE.md** with context
5. **Create initial status file** (status_N.json)
6. **Update parent's children list**

<!-- section_id: "6402fc1b-ae1e-4ecd-9b08-e19e30decc98" -->
### Required Structure for New Entity

Every new entity MUST have the two-folder structure with ALL possible child types:

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md              # Tool-agnostic foundational context (source of truth)
├── CLAUDE.md                 # Generated from 0AGNOSTIC.md (Claude-specific)
├── .0agnostic/               # Resources for agnostic system
│   ├── rules/
│   ├── prompts/
│   ├── knowledge/
│   └── scripts/
├── .claude/                  # Claude-specific settings
├── status_N.json             # Current state tracking
├── layer_N/                  # Entity's OWN internals
│   ├── layer_N_00_layer_registry/
│   ├── layer_N_01_ai_manager_system/
│   ├── layer_N_02_manager_handoff_documents/
│   ├── layer_N_03_sub_layers/
│   │   ├── sub_layer_N_01_prompts/
│   │   ├── sub_layer_N_02_knowledge_system/
│   │   ├── sub_layer_N_03_principles/
│   │   └── sub_layer_N_04_rules/
│   └── layer_N_99_stages/
│       ├── stage_N_00_stage_registry/
│       ├── stage_N_01_request_gathering/
│       └── ... (all 11 stages)
└── layer_N+1/                # Entity's CHILDREN (ALL types, even if empty)
    ├── layer_N+1_sub*_<types>/   # Same-type nesting
    ├── layer_N+1_features/       # Features
    └── layer_N+1_components/     # Components
```

**Key Points**:
- Always include `0AGNOSTIC.md` as the source of truth
- Tool-specific files (`CLAUDE.md`, `AGENTS.md`, etc.) are generated from `0AGNOSTIC.md`
- Include `.0agnostic/` and `.claude/` folders for tool support
- Always create ALL child type folders in `layer_N+1/` even if empty

---

<!-- section_id: "cf426e7f-d08e-41e2-81ac-c37b8ecd8e84" -->
## Handoff System

Entities communicate via handoff documents in **four directions**:

<!-- section_id: "abf026c7-b3c0-4b79-ae69-523f4e7026b8" -->
### Handoff Directions

| Direction | Purpose | Folder |
|-----------|---------|--------|
| **UP** | Escalate to parent, return results | `hand_off_documents/outgoing/to_above/` |
| **DOWN** | Delegate to children | `hand_off_documents/outgoing/to_below/` |
| **SIDEWAYS** | Coordinate with siblings | `hand_off_documents/outgoing/to_siblings/` |
| **INCOMING** | Receive from any direction | `hand_off_documents/incoming/from_above/`, `from_below/`, `from_siblings/` |

<!-- section_id: "85f2641f-fabb-4cf6-9933-43ff698c2bf4" -->
### Handoff Document Structure

```json
{
  "schemaVersion": "1.0.0",
  "id": "handoff-l2-auth-impl",
  "layer": 2,
  "stage": "development",
  "from": "layer_2/auth/design",
  "to": "layer_2/auth/development",
  "direction": "sideways",
  "task": "Implement login component",
  "constraints": ["TypeScript", "React"],
  "artifacts": {"files": ["src/components/LoginForm.tsx"]},
  "status": "pending"
}
```

<!-- section_id: "15111d9c-4f7e-4116-a0eb-cd7dc98f42aa" -->
### Handoff Workflow
1. **Read incoming** from `hand_off_documents/incoming/`
2. **Process** the task
3. **Write outgoing** to appropriate direction folder
4. **Track status** in status.json

---

<!-- section_id: "b76c77e5-6dff-4ba3-99d5-f06f22c2bd30" -->
## AGNOSTIC System (Subcomponent of Layer-Stage)

The AGNOSTIC system is a **subcomponent** of the layer-stage system, providing tool portability and session management at each layer:

<!-- section_id: "8617ed8c-e0ec-4be7-90cb-3ef47da3e836" -->
### Structure at Each Entity

```
layer_N_<type>_<name>/
├── 0AGNOSTIC.md          # SOURCE OF TRUTH - Tool-agnostic context
├── CLAUDE.md             # Generated from 0AGNOSTIC.md (Claude Code)
├── AGENTS.md             # Generated from 0AGNOSTIC.md (Cursor Agents)
├── GEMINI.md             # Generated from 0AGNOSTIC.md (Gemini)
├── OPENAI.md             # Generated from 0AGNOSTIC.md (OpenAI)
├── .0agnostic/           # Shared resources for all tools
│   ├── rules/
│   ├── prompts/
│   ├── knowledge/
│   ├── scripts/
│   └── skills/
├── .claude/              # Claude-specific settings
├── outputs/episodic/     # Session memory (episodic memory system)
│   ├── index.md
│   ├── sessions/
│   ├── changes/
│   └── divergence.log
└── .locks/               # Multi-agent file locking
```

<!-- section_id: "fa018271-009c-406d-80db-be88fa7b61aa" -->
### Key Functions

| Function | Component | Purpose |
|----------|-----------|---------|
| Tool Portability | `0AGNOSTIC.md` → tool-specific files | Same context works across Claude, Cursor, Gemini, etc. |
| Episodic Memory | `outputs/episodic/` | Solves agent amnesia across sessions |
| Multi-Agent Sync | `.locks/` | Prevents conflicts when multiple agents work in parallel |
| Session Continuity | `divergence.log` | Tracks changes made during sessions |

<!-- section_id: "9d131df6-4256-4c43-bbc7-6170c4156d95" -->
### Integration with Layer-Stage

- **0AGNOSTIC.md** defines Identity, Navigation, Behaviors for each entity
- Generated files (CLAUDE.md, etc.) inherit the layer-stage context automatically
- Episodic memory folders exist at each layer level
- The agnostic-sync.sh script regenerates tool-specific files from 0AGNOSTIC.md

---

<!-- section_id: "8705f513-276e-4338-b5d0-a51c02749e65" -->
## Key Observations

<!-- section_id: "684c60a5-4d3d-436f-890e-26d2ff43667b" -->
### Inconsistencies in Existing Structure

1. **Stage numbering varies**: Some older projects use stages 00-09, newer ones use 01-11
2. **Component positions vary**: Some use 01/02, others use 00/01/02/03/99
3. **Design/Planning order**: Stage registry says planning=04, design=05, but the decision is design=04, planning=05

<!-- section_id: "5dfe1bc8-924c-42cf-a137-fe72170ea363" -->
### System Integration

The AGNOSTIC system is a **subcomponent** of the layer-stage system:
- Layer-stage provides the organizational hierarchy and workflow structure
- AGNOSTIC provides tool portability and session continuity within that structure
- Both work together - entities have layer-stage structure AND agnostic files

<!-- section_id: "f1892bb2-7421-43d6-9395-a293e857c0f3" -->
### Nesting Capability

Features can contain their own layer structure:
- `layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_*/` shows features with internal layers

---

<!-- section_id: "81cc8517-378a-4bb1-9b9c-94625a4c8d18" -->
## Status Tracking

Each layer tracks status in `layer_N_99_stages/status.json`:

```json
{
  "current_stage": "development",
  "stages": {
    "request_gathering": "done",
    "research": "done",
    "instructions": "done",
    "design": "done",
    "planning": "done",
    "development": "in_progress",
    "testing": "not_started"
  }
}
```

---

<!-- section_id: "2f34e9a4-35aa-4623-8a76-5d184abf34c7" -->
## Summary

**Layer instantiation**:
1. Create directory with pattern `layer_N_entity_name/`
2. Add components at positions 00, 01, 02, 03, 99
3. Initialize CLAUDE.md and status.json
4. Create sub-layers as needed in position 03
5. Create stages in position 99

**Stage instantiation**:
1. Create directories 01-11 in `layer_N_99_stages/`
2. Each stage gets: ai_agent_system/, hand_off_documents/, outputs/
3. Position 00 reserved for stage_registry (metadata only)
4. **Design (04) before Planning (05)**

**Workflow**:
- Enter via handoff documents
- Work within current stage
- Output to outputs/ and outgoing handoff
- Track status in status.json

---

<!-- section_id: "fbf7cf65-cb69-4cca-8edd-5bd63e062460" -->
## Proposed Improvements (In Progress)

<!-- section_id: "9d12767b-596a-4065-b99c-ad695fe1b732" -->
### Problem 1: Container vs Item Ambiguity

**Current Issue**: Folders like `sub_layer_0_05_content` are ambiguous - is it an item at position 05, or a container grouping items?

**Proposed Solution**: Use `group` suffix (just "group", no additional descriptor):

| Current | Proposed | Purpose |
|---------|----------|---------|
| `sub_layer_0_05_content` | `sub_layer_0_05_group` | Contains multiple items at this level |
| `sub_layer_0_06_environments` | `sub_layer_0_06_group` | Groups items at this level |

**Pattern**:
- `layer_N_XX_name` = An actual item/entity at position XX
- `layer_N_XX_group` = A container for items at level N (just "group", no suffix)

---

<!-- section_id: "d664099d-770c-4b8b-9e8b-7c7aa2f50184" -->
### Clarification: Setup-Dependent Hierarchy vs SubxN Nesting

**Two DIFFERENT concepts - don't confuse them:**

#### 1. Setup-Dependent Hierarchy (Progressive Specificity)

The setup hierarchy is a **cascade of choices** where each position represents a DIFFERENT type of specificity. This is NOT subxN nesting:

```
sub_layer_0_05_operating_systems/         ← Position 05: OS type
└── sub_layer_0_05_linux_ubuntu/          ← Specific OS choice
    └── sub_layer_0_06_environments/      ← Position 06: Environment type (NOT subx2!)
        └── sub_layer_0_06_local/         ← Specific environment choice
            └── sub_layer_0_07_coding_apps/   ← Position 07: App type (NOT subx3!)
                └── sub_layer_0_07_cursor/
                    └── sub_layer_0_09_ai_apps/   ← Position 09: AI app type
```

**Why NOT subxN?** Because each level is a DIFFERENT sub-layer type (OS → Environment → App → AI App). The position numbers (05, 06, 07, 09...) already indicate the specificity level.

#### 2. SubxN Nesting (Same-Type Within a Node)

SubxN applies when you create **sub-layers WITHIN a specific node's setup** - meaning sub-layers nested inside sub-layers of the same entity:

```
sub_layer_0_06_local/
└── setup/
    ├── sub_layer_0_06_00_layer_registry/
    ├── sub_layer_0_06_01_ai_manager_system/
    ├── sub_layer_0_06_02_manager_handoff_documents/
    ├── sub_layer_0_06_03_subx2_layers/     ← SubxN HERE - sub-layers within local's own setup
    └── sub_layer_0_06_99_stages/
```

**When to use subxN**:
- Sub-layers WITHIN a node's `setup/` folder = subx2
- Sub-layers within those = subx3
- etc.

**When NOT to use subxN**:
- Moving through the setup-dependent hierarchy (05 → 06 → 07 → etc.)
- These are different sub-layer TYPES, not nested same-type

---

<!-- section_id: "7c232ba4-b4b3-4114-bb1e-0c8c46776259" -->
### Problem 2: Episodic Memory Location

**Current Issue**: Episodic memory (`outputs/episodic/`) is in the wrong place. It's AI system infrastructure, not stage output.

**Current (Wrong)**:
```
entity/
├── .0agnostic/
├── .claude/
└── outputs/
    └── episodic/        ← AI infrastructure mixed with outputs!
```

**Proposed (Correct)**:
```
entity/
├── .0agnostic/
│   ├── episodic/        ← Move here - tool-agnostic AI system
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── knowledge/
│   ├── prompts/
│   ├── rules/
│   ├── scripts/
│   └── skills/
├── .claude/
└── outputs/             ← Only actual stage products
```

**Why `.0agnostic/`?**
- Episodic memory is used by ANY AI tool (Claude, Cursor, Gemini, etc.)
- It's AI system infrastructure for session continuity
- It's NOT a product output of stage work
- Keeping it tool-agnostic allows session continuity across tools

**Affected Locations**:
- Entity root: `entity/outputs/episodic/` → `entity/.0agnostic/episodic/`
- Stage outputs: `stage_XX/outputs/episodic/` → `stage_XX/.0agnostic/episodic/`
- Feature outputs: `feature/outputs/episodic/` → `feature/.0agnostic/episodic/`

---

<!-- section_id: "48c0bf40-e0d5-4379-9e4e-3fbf8629e912" -->
### Problem 3: Content/Group Folder Naming

**Current Issue**: Folders like `sub_layer_0_06_content` are confusing - they act as containers but look like items.

---

<!-- section_id: "954cd1a9-0ae8-4f10-8a55-78f5d5964900" -->
### Problem 3: Setup Folder Ordering

**Current Issue**: Setup folders don't sort first in directory listings.

**Proposed Solution**: Use position `00` or `0` prefix for setup:
```
sub_layer_0_06_local/
├── 0_setup/                          ← Sorts FIRST
│   └── sub_layer_0_06_99_stages/
├── sub_layer_0_07_coding_apps/
└── sub_layer_0_08_other/
```

**Alternative**: Use `00_` prefix:
```
sub_layer_0_06_local/
├── 00_setup/                         ← Sorts FIRST
└── sub_layer_0_07_coding_apps/
```

---

<!-- section_id: "5d304801-23d1-4d0f-a1d4-253f7c2c45a3" -->
### Pattern: Stages Within Sub-Layers

**Observed Working Pattern**: Stages CAN exist within deep sub-layers for specialized workflows:

```
sub_layer_0_13_protocols/
└── sub_layer_0_13_99_stages/         ← Position 99 for stages
    ├── stage_0_01_request_gathering/
    ├── stage_0_03_instructions/
    └── stage_0_10_current_product/
```

**Structure**: Each stage within sub-layer follows standard stage structure:
- `hand_off_documents/` (incoming/outgoing)
- `ai_agent_system/`
- `outputs/`
- `.claude/` (commands, scripts, hooks, skills, agents)

**Use Case**: When a specific setup context (e.g., Linux + Local + Cursor + Claude Code + Protocols) needs its own workflow stages.

---

<!-- section_id: "304cb859-acbe-4e56-9fb2-e1fc38694d4e" -->
### Summary of Proposed Naming Conventions

| Concept | Naming Pattern | Example |
|---------|---------------|---------|
| Entity | `layer_N_<type>_<name>/` | `layer_1_project_myapp/` |
| Entity internals group | `layer_N/` (at entity root) | `layer_1/` |
| Entity children group | `layer_N+1/` (at entity root) | `layer_2/` |
| Item at position XX | `layer_N_XX_name` | `sub_layer_0_05_linux` |
| Container/group at position XX | `layer_N_XX_group` | `sub_layer_0_05_group` |
| Nested sub-layer (2 deep) | `subx2_layer_N_XX_name` | `subx2_layer_0_06_settings` |
| Nested sub-layer (3 deep) | `subx3_layer_N_XX_name` | `subx3_layer_0_07_advanced` |
| Setup (sorts first) | `00_setup/` or `0_setup/` | `00_setup/` |
| Stages within sub-layer | `..._99_stages/stage_N_XX_name` | `sub_layer_0_13_99_stages/` |

**Key distinction**:
- **Entity** = The actual thing (project, feature, component, sub-layer item)
- **Group** = A container holding multiple entities or internals

---

<!-- section_id: "18b06245-f365-4eae-a9b1-3cdc0baa2d4e" -->
## Key Source Documents

| Document | Location | What It Explains |
|----------|----------|------------------|
| **FLEXIBLE_LAYERING_SYSTEM.md** | `layer_1/.../sub_layer_1_05_framework_docs/` | Authoritative guide on nesting, naming, specificity |
| **SYSTEM_OVERVIEW.md** | `0_layer_universal/` | Big picture of layer + stage system |
| **layer_registry.yaml** | `layer_0_group/layer_0_00_layer_registry/` | Layer internal structure definition |
| **stage_registry.yaml** | `layer_0_group/layer_0_99_stages/layer_0_00_stage_registry/` | Stage workflow definition |

---

<!-- section_id: "dd69a1d7-c837-4e26-a918-5deeab392ac9" -->
## Summary

<!-- section_id: "ecf0206b-9b90-4af7-949c-d9f0810a6701" -->
### Core Concepts (Established)
1. **Layers = Specificity**: Universal (0) → Project (1) → Feature (2) → Component (3) → deeper
2. **Rules CASCADE**: Lower layer rules apply to all higher layers
3. **Same-type nesting uses "sub"**: project→sub_project, feature→sub_feature, component→sub_component
4. **Different-type nesting does NOT use "sub"**: project→feature, project→component, feature→component (no sub prefix)
5. **Two-folder structure**: `layer_N/` (internals) + `layer_N+1/` (children with ALL types even if empty)
6. **Design before Planning**: Stage 04 = design, Stage 05 = planning
7. **AGNOSTIC is a subcomponent**: Tool portability + episodic memory integrated into layer-stage structure
8. **Handoffs go 4 directions**: UP (to parent), DOWN (to children), SIDEWAYS (to siblings), INCOMING (receive)
9. **Stages can exist in sub-layers**: For specialized workflows like OS-specific setup
10. **Entity structure requires**: 0AGNOSTIC.md (source), tool-specific files, .0agnostic/, .claude/, layer_N/, layer_N+1/

<!-- section_id: "824e8444-6886-4542-8dc0-6fe3800601c8" -->
### Proposed Improvements (New)
11. **Entity vs Group distinction**:
    - **Entity** = actual item (project, feature, component, specific sub-layer)
    - **Group** = container folder, named with just `group` suffix: `layer_N_XX_group`
12. **Entity root groups**: `layer_N/` and `layer_N+1/` at entity root are GROUP folders (containers), not entities
13. **SubxN depth markers**: Nested sub-layers WITHIN a node's setup use `subx2_layer`, `subx3_layer` (NOT for setup hierarchy progression)
14. **Setup ordering**: Use `00_setup/` or `0_setup/` to ensure setup sorts first in directories
15. **Stages in deep sub-layers**: Pattern confirmed - position 99 for stages even within deep sub-layer nesting

<!-- section_id: "a5bbac8d-7b6a-405b-82d4-84af782aec56" -->
### Stage Output Patterns (Documented)
16. **Tree of Needs**: Stage 01 uses hierarchical `tree_of_needs/` structure for requirements
17. **In-progress/Finished**: Stages 02-03 use `01_*_in_progress/` and `02_finished_*/` separation
18. **By-need/By-topic/Synthesis**: Research-like stages organize by need, topic, and synthesis
19. **Numbered design decisions**: Stage 04 uses numbered `01_*, 02_*` files in `by_topic/`

<!-- section_id: "c4d0a4ff-d01b-4a6c-9ca6-8a8cd761c99b" -->
### AI System Infrastructure (Proposed Changes)
20. **Episodic memory location**: Move from `outputs/episodic/` to `.0agnostic/episodic/` (AI infra, not output)
21. **Content in sub-layers**: `knowledge/`, `prompts/`, `rules/`, `principles/` live in sub-layers, NOT dot-folders
22. **Dot-folders for tool config only**: agents, skills, hooks, episodic (references sub-layers)

<!-- section_id: "4e76e4d1-c292-4693-908e-d3700307668f" -->
### Three-Tier Folder Architecture
23. **Source**: `.0agnostic/` - tool-agnostic source of truth
24. **Merge workspaces**: `.1claude_merge/`, `.1cursor_merge/`, `.1gemini_merge/` - build folders with overrides/additions
25. **Final output**: `.claude/`, `.cursor/`, `.gemini/` - what tools actually read (generated)
26. **Numbered sorting**: `.0*` (source) → `.1*_merge` (build) → `.*` (output)
27. **Override structure**: `0_synced/` + `1_overrides/` + `2_additions/` in each merge folder
28. **MD generation**: `CLAUDE.md` = `0AGNOSTIC.md` + `.1claude_merge/CLAUDE.override.md`
29. **SessionStart hook**: Auto-runs merge script on session start

<!-- section_id: "4b010622-d33f-4924-96be-61df85382334" -->
### Tool Context Systems (Researched)
30. **Claude Code**: `CLAUDE.md` hierarchy + `.claude/rules/` (frontmatter: description, globs, alwaysApply) + skills + agents + hooks
31. **Codex CLI**: `AGENTS.md` + `~/.codex/config.toml` + skills folder + experimental_instructions_file override
32. **Gemini CLI**: `GEMINI.md` hierarchy (global → ancestor → sub-dir) + `@import` syntax + `/memory` commands
33. **OpenCode CLI**: `.opencode/config.yaml` + agent markdown files + custom commands
34. **Aider**: `.aider.conf.yml` + `.aider.model.settings.yml` + env vars (no instruction file)
35. **Cursor**: `.cursor/rules/*.mdc` (MDC frontmatter: description, globs, alwaysApply) + Settings UI + YOLO mode
36. **GitHub Copilot**: `.github/copilot-instructions.md` + `.github/instructions/*.instructions.md` (applyTo frontmatter)
37. **Continue**: `config.yaml` with models, rules, contextProviders, slashCommands + `.continuerc.json` workspace override

<!-- section_id: "7a8957e7-c262-490a-b478-e7e17b60ee85" -->
### Agnostic Mapping Patterns
38. **Instructions** → Main MD file (CLAUDE.md, AGENTS.md, GEMINI.md, copilot-instructions.md)
39. **Always rules** → Tool rules with `alwaysApply: true` or embedded in main file
40. **Conditional rules** → Tool rules with `globs:` (Claude/Cursor) or `applyTo:` (Copilot) frontmatter
41. **Agents** → Claude `.claude/agents/`, OpenCode `.opencode/agent/`
42. **Skills** → Claude `.claude/skills/`, Codex skills folder
43. **Hooks** → Claude `settings.json` hooks only (others don't support)

<!-- section_id: "c64d3bdd-9c05-4555-98a0-3c8cd56e1177" -->
### Tool Rankings (2025-2026)
44. **Tier 1**: Claude Code (⭐⭐⭐⭐⭐ - large codebases, refactoring, reasoning) + Cursor (⭐⭐⭐⭐⭐ - IDE, real-time)
45. **Tier 2**: Aider (⭐⭐⭐⭐ - Git native, BYOK) + Copilot (⭐⭐⭐⭐ - teams) + Codex CLI (⭐⭐⭐⭐ - autonomous)
46. **Tier 3**: Gemini CLI (⭐⭐⭐½ - free tier) + OpenCode (⭐⭐⭐½ - open source) + Continue (⭐⭐⭐ - IDE OSS)
47. **Best combo**: Claude Code (complex work) + Cursor (daily coding) + Aider (model flexibility)
