---
resource_id: "8a7d4f85-aaea-48d5-8a0c-d23a1cc5971a"
resource_type: "output"
resource_name: "04_context_propagation_funnel"
---
# Context Propagation Funnel (Bottom-Up)

**Date**: 2026-02-23
**Status**: Approved and implemented
**Scope**: How work products consolidate within stages, propagate upward across the layer-stage hierarchy, and fan out to AI app-specific configuration systems

---

## Overview

The propagation chain architecture (doc 03) covers **top-down** flow: how context reaches agents. This document covers **bottom-up** flow: how work products consolidate and propagate upward through the hierarchy, and the **last mile fan-out**: how the consolidated agnostic content propagates into each AI app's native configuration system.

The core insight: **stages and entities follow the same consolidation pattern** — many inputs → consolidation overview → structured system → summary report → entry point. Then 0AGNOSTIC.md fans out through `.1merge` into every AI app's specific config system.

---

## The Universal Consolidation Pattern

```
Many detailed files  →  Consolidation reports  →  Structured system  →  Summary report  →  Entry point
     (inputs)            (overview + refs)         (.0agnostic/)        (stage/layer rpt)   (0AGNOSTIC.md)
```

This pattern is **recursive**. A stage report becomes input to its entity. An entity's layer report becomes input to its parent. All the way to the root.

The theme is **progressive detail reduction**: each tier summarizes, organizes, references, and consolidates the tier above it.

---

## Diagram 1: Stage-Internal Consolidation Funnel

How content within a single stage reduces from many files to a single consolidated entry point.

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   MOST DETAIL                                                    │
│   ════════════                                                   │
│                                                                  │
│   outputs/                                                       │
│   ├── research_notes.md                                          │
│   ├── analysis_v1.md          Many files, full detail.           │
│   ├── data/raw_results.csv    The actual work products of        │
│   ├── drafts/proposal_v3.md   the stage — everything the         │
│   └── ...                     agent produced.                    │
│                                                                  │
│          │                                                       │
│          ▼  organized, summarized, referenced                    │
│                                                                  │
│   outputs/reports/                                               │
│   └── output_report.md        References all outputs.            │
│                               Summarizes key findings.           │
│                               Organizes results into             │
│                               a navigable overview.              │
│                                                                  │
│          │                                                       │
│          ▼  insights structured into navigable system            │
│                                                                  │
│   .0agnostic/                                                    │
│   ├── 01_knowledge/           Structured insights from work      │
│   ├── 02_rules/               Constraints discovered             │
│   ├── 03_protocols/           Processes defined                  │
│   ├── 04_episodic_memory/     Session history                    │
│   ├── 05_handoff_documents/   Incoming context + outgoing        │
│   │   ├── 01_incoming/        reports and summaries              │
│   │   │   ├── 01_from_above/  (manager instructions, layer rpt) │
│   │   │   └── 02_from_sides/  (sibling stage reports)           │
│   │   └── 02_outgoing/                                          │
│   │       └── 01_to_above/    stage_report.md                   │
│   └── 06_context_avenue_web/  Agent access paths                 │
│                                                                  │
│          │                                                       │
│          ▼  extracted into <30-line summary                      │
│                                                                  │
│   .0agnostic/05_handoff_documents/02_outgoing/01_to_above/       │
│   └── stage_report.md                                            │
│   ┌────────────────────────────────────────────────────┐         │
│   │ Status, Summary, Key Outputs, Findings,            │         │
│   │ Open Items, Handoff readiness                      │         │
│   │ (<30 lines — manager-readable at a glance)         │         │
│   │                                                    │         │
│   │ Draws from: output_report.md + .0agnostic/         │         │
│   │ Covers the WHOLE stage, not just outputs            │         │
│   └────────────────────────────────────────────────────┘         │
│          │                                                       │
│          │  sync-handoffs.sh distributes to:                     │
│          │  ┌──────────┐ ┌──────────┐ ┌──────────────┐          │
│          ├─▶│ Siblings  │ │ Siblings │ │ Entity Mgr   │          │
│          │  │ (left)    │ │ (right)  │ │ from_below/  │          │
│          │  └──────────┘ └──────────┘ └──────────────┘          │
│          │                                                       │
│          ▼  consolidated into single entry point                 │
│                                                                  │
│   0AGNOSTIC.md                                       MOST        │
│   ┌────────────────────────────────────────────────────┐         │
│   │ STATIC: Identity, Key Behaviors, Methodology,      │ CONSOL- │
│   │   Inputs/Outputs, Triggers, Current Status          │ IDATED  │
│   │                                                    │         │
│   │ DYNAMIC: State Detail, Key Outputs table,          │         │
│   │   Key Findings, Open Items, Handoff, Navigation    │         │
│   └────────────────────────────────────────────────────┘         │
│          │                                                       │
│          └──▶  agnostic-sync.sh  ──▶  CLAUDE.md, AGENTS.md,     │
│                                       GEMINI.md, OPENAI.md      │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### What each tier does

| Tier | Contains | Produced by | Consumed by |
|------|----------|-------------|-------------|
| `outputs/` | Raw work products | Stage agent during work | The agent itself; next-stage agents |
| `outputs/reports/output_report.md` | Organized overview referencing all outputs | Stage agent on completion | Stage agent (to write report + update .0agnostic) |
| `.0agnostic/` | Structured system — knowledge, rules, protocols, avenues | Stage agent; sync scripts | Any agent entering this stage |
| `stage_report.md` | <30-line summary of the whole stage | Stage agent before exiting | Entity manager; sibling stages (via sync) |
| `0AGNOSTIC.md` | Consolidated entry point — identity + status + references | Stage agent (updated each session) | Any AI agent delegated to this stage |

### How each tier references the one above

- **`output_report.md`** references files in `outputs/` by relative path
- **`.0agnostic/`** structures insights FROM outputs into knowledge, rules, protocols
- **`stage_report.md`** draws from output report + .0agnostic content to summarize the whole stage
- **`0AGNOSTIC.md`** integrates everything: references INTO `.0agnostic/`, includes Current Status as the most distilled view

---

## Diagram 2: Cross-Level Connection Map

How stages feed entities, and child entities feed parent entities.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   ROOT ENTITY (e.g., 0_layer_universal)                                │
│                                                                         │
│   Receives layer_reports from child entities                           │
│   Consolidates into own .0agnostic/ → 0AGNOSTIC.md → CLAUDE.md        │
│                                                                         │
│          ▲ layer_report                                                 │
│          │                                                              │
│  ┌───────┴──────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │   ENTITY (e.g., layer_0_feature_X)                               │   │
│  │                                                                   │   │
│  │   RAW INPUTS:                                                    │   │
│  │                                                                   │   │
│  │   From ABOVE (parent):                                           │   │
│  │   └─ 01_incoming/01_from_above/                                  │   │
│  │      ├── layer_report.md          (parent's layer report)        │   │
│  │      └── manager_instructions.md  (parent's directives)         │   │
│  │                                                                   │   │
│  │   From BELOW (own stages):                                       │   │
│  │   └─ 01_incoming/03_from_below/stage_reports/                    │   │
│  │      ├── layer_N.stage_01.stage_report.md                       │   │
│  │      ├── layer_N.stage_02.stage_report.md                       │   │
│  │      └── ...one per active stage                                │   │
│  │                                                                   │   │
│  │   From BELOW (child entities):                                   │   │
│  │   └─ 01_incoming/03_from_below/layer_reports/                    │   │
│  │      ├── layer_N+1.child_A.layer_report.md                      │   │
│  │      └── layer_N+1.child_B.layer_report.md                      │   │
│  │                                                                   │   │
│  │   CONSOLIDATION REPORTS:                                         │   │
│  │                                                                   │   │
│  │   02_outgoing/01_to_above/                                       │   │
│  │   ├── stages_report.md          Summarizes all stage reports     │   │
│  │   └── child_layers_report.md    Summarizes all child reports     │   │
│  │                                                                   │   │
│  │          │                                                        │   │
│  │          ▼  structured → .0agnostic/ → layer_report → 0AGNOSTIC  │   │
│  │                                                                   │   │
│  │   STAGES (each follows the same funnel internally):              │   │
│  │                                                                   │   │
│  │   ┌─────────┐ ┌─────────┐ ┌─────────┐       ┌─────────┐       │   │
│  │   │stage_01 │ │stage_02 │ │stage_04 │  ...  │stage_11 │       │   │
│  │   │outputs/ │ │outputs/ │ │outputs/ │       │outputs/ │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │out_rpt  │ │out_rpt  │ │out_rpt  │       │out_rpt  │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │.0agnstc │ │.0agnstc │ │.0agnstc │       │.0agnstc │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │stg_rpt  │ │stg_rpt  │ │stg_rpt  │       │stg_rpt  │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │0AGNOSTC │ │0AGNOSTC │ │0AGNOSTC │       │0AGNOSTC │       │   │
│  │   └────┬────┘ └────┬────┘ └────┬────┘       └────┬────┘       │   │
│  │        │            │           │                  │            │   │
│  │        └────────────┴───────────┴──────────────────┘            │   │
│  │                     │                                            │   │
│  │                     ▼ all stage reports                          │   │
│  │              entity from_below/stage_reports/                    │   │
│  │                     ▼                                            │   │
│  │              stages_report.md (consolidation)                   │   │
│  │                                                                   │   │
│  └───────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Information flow summary

| Direction | What flows | Mechanism |
|-----------|-----------|-----------|
| Stage → Entity (up) | `stage_report.md` | `sync-handoffs.sh` → entity `from_below/stage_reports/` |
| Stage ↔ Stage (lateral) | `stage_report.md` | `sync-handoffs.sh` → sibling `from_sides/` |
| All stage reports → Consolidation | `stages_report.md` | Entity manager writes overview |
| All child reports → Consolidation | `child_layers_report.md` | Entity manager writes overview |
| Child Entity → Parent Entity (up) | `layer_report.md` | `sync-handoffs.sh` → parent `from_below/layer_reports/` |
| Entity → Stages (down) | `layer_report.md`, `manager_instructions.md` | `sync-handoffs.sh` → stage `from_above/` |
| 0AGNOSTIC.md → Tool files (lateral) | STATIC content | `agnostic-sync.sh` |

---

## The Recursive Nature

The consolidation funnel repeats at every level:

```
STAGE LEVEL                    ENTITY LEVEL                  ROOT LEVEL
─────────────                  ────────────                  ──────────

outputs/ (many)                stage_reports/ (several)      layer_reports/ (few)
      ↓                        + child layer_reports/              ↓
output_report.md                     ↓                             ↓
      ↓                        stages_report.md              consolidation reports
.0agnostic/ (structured)       + child_layers_report.md            ↓
      ↓                              ↓                       .0agnostic/ (structured)
stage_report.md (summary)     .0agnostic/ (structured)            ↓
      ↓                              ↓                       0AGNOSTIC.md (entry point)
0AGNOSTIC.md (entry point)    layer_report.md (summary)
      ↓                              ↓
  feeds entity                 0AGNOSTIC.md (entry point)
                                     ↓
                                feeds parent
```

At each level:
- **Input count decreases** — stages have many output files; entities have ~11 stage reports + child layer reports; root has a handful of layer reports
- **Consolidation increases** — each level distills through consolidation reports → structured system → summary report → entry point
- **Same pattern**: many inputs → overview → system → summary → entry point (0AGNOSTIC.md)

---

## Diagram 3: App-Specific Propagation (The Last Mile)

The funnel consolidates upward to 0AGNOSTIC.md. But 0AGNOSTIC.md is tool-agnostic — no AI app reads it directly. The **last mile** is where agnostic content fans out into each AI app's native configuration system through `agnostic-sync.sh` and the `.1merge` projection layer.

```
                    0AGNOSTIC.md
                    (tool-agnostic source of truth)
                         │
         ┌───────────────┼───────────────────────────┐
         │               │                            │
         ▼               ▼                            ▼
   agnostic-sync.sh    .1merge/                  .0agnostic/
   (generates tool     (per-tool projections)    (on-demand resources:
    files from STATIC)  ┌──────────────┐          skills, rules,
         │              │ 0_synced     │          knowledge, protocols,
         │              │ 1_overrides  │          episodic memory)
         │              │ 2_additions  │               │
         │              └──────┬───────┘               │
         │                     │                       │
         ▼─────────────────────▼───────────────────────▼
         │
         │  GENERATED TOOL FILES (consumed by AI apps)
         │  ═══════════════════════════════════════════
         │
         ├──▶ CLAUDE.md ─────────────────────┐
         │    (full STATIC content)           │
         │                                    ▼
         │                              ┌───────────────────────────────┐
         │                              │  .claude/ (Claude Code)       │
         │                              │  ├── CLAUDE.md (auto-loaded)  │
         │                              │  ├── rules/     (warm ctx)    │
         │                              │  ├── skills/    (cold ctx)    │
         │                              │  ├── agents/    (agent defs)  │
         │                              │  ├── settings.json (hooks)    │
         │                              │  └── commands/  (custom cmds) │
         │                              └───────────────────────────────┘
         │
         ├──▶ AGENTS.md / OPENAI.md ─────────┐
         │    (full STATIC content)            │
         │                                     ▼
         │                              ┌───────────────────────────────┐
         │                              │  .codex/ (Codex CLI)          │
         │                              │  ├── AGENTS.md (auto-loaded)  │
         │                              │  ├── AGENTS.override.md (opt) │
         │                              │  ├── config.toml (settings)   │
         │                              │  └── Agent Skills             │
         │                              │                               │
         │                              │  + Cursor CLI also reads      │
         │                              │    AGENTS.md as rules ──────┐ │
         │                              └─────────────────────────────┼─┘
         │                                                            │
         │
         ├──▶ GEMINI.md ─────────────────────┐
         │    (full STATIC content)           │
         │                                    ▼
         │                              ┌───────────────────────────────┐
         │                              │  ~/.gemini/ + .gemini/        │
         │                              │  ├── GEMINI.md (hierarchical) │
         │                              │  ├── settings.json (config)   │
         │                              │  ├── .geminiignore (filter)   │
         │                              │  └── /memory add (persistent) │
         │                              └───────────────────────────────┘
         │
         ├──▶ .cursorrules ──────────────────┐
         │    (lean: Identity + Navigation)   │
         │                                    ▼
         │                              ┌───────────────────────────────┐
         │                              │  .cursor/ (Cursor IDE + Agent │
         │                              │           CLI, headless/CI)   │
         │                              │  ├── .cursorrules (auto-load) │
         │                              │  ├── rules/     (warm ctx)    │
         │                              │  ├── mcp.json   (MCP config)  │
         │                              │  ├── cli.json   (CLI perms)   │
         │                              │  └── CLI also reads:          │
         │                              │      CLAUDE.md ◄──────────┐   │
         │                              │      AGENTS.md ◄──────────┘   │
         │                              │      (applied as rules)       │
         │                              └───────────────────────────────┘
         │
         └──▶ .github/copilot-instructions.md ─┐
              (medium: Identity + Triggers)      │
                                                 ▼
                                          ┌───────────────────────────────┐
                                          │  .github/ (GitHub Copilot)    │
                                          │  ├── copilot-instructions.md  │
                                          │  └── (workflows, actions)     │
                                          └───────────────────────────────┘
```

### How each app consumes context

Each AI app has its own **context loading mechanism** with a cascade/walk model, a config directory, and native context surfaces. The agnostic system adapts to each through `.1merge` projections and `agnostic-sync.sh` generation profiles.

#### Claude Code (`.claude/`)

| Aspect | Detail |
|--------|--------|
| **Generated file** | CLAUDE.md (Full STATIC profile) |
| **Auto-load** | Walks ALL CLAUDE.md files from filesystem root to cwd, concatenating them |
| **Config dir** | `.claude/` |
| **Global config** | `~/.claude/CLAUDE.md` (global instructions), `~/.claude/settings.json` |
| **Context surfaces** | `rules/` (warm — path-scoped), `skills/` (cold — on-demand invocation), `agents/` (agent definitions), `commands/` (custom slash commands), `settings.json` (hooks, MCP servers, permissions) |
| **MCP config** | `.claude/settings.json` mcpServers key |
| **Unique features** | PostToolUse hooks, auto-memory (`~/.claude/projects/.../memory/`), skill WHEN/WHEN NOT gating |

#### Codex CLI (`.codex/`)

| Aspect | Detail |
|--------|--------|
| **Generated file** | AGENTS.md (Full STATIC profile) |
| **Auto-load** | Walks AGENTS.md (or AGENTS.override.md) from `~/.codex/` → project root → cwd, concatenating in order |
| **Config dir** | `.codex/` |
| **Global config** | `~/.codex/config.toml`, `~/.codex/AGENTS.md` |
| **Project config** | `.codex/config.toml` (project-level overrides) |
| **Context surfaces** | AGENTS.md cascade, skills (Agent Skills system), config.toml for model/permission settings |
| **Unique features** | AGENTS.override.md (temporary global override without deleting base), project_doc_max_bytes limit (32 KiB default), project_doc_fallback_filenames for alternative doc names |

#### Gemini CLI (`~/.gemini/`)

| Aspect | Detail |
|--------|--------|
| **Generated file** | GEMINI.md (Full STATIC profile) |
| **Auto-load** | Hierarchical: `~/.gemini/GEMINI.md` (global) → parent dirs up to git root → cwd → subdirectories below cwd |
| **Config dir** | `~/.gemini/` (user-level), `.gemini/` (project-level) |
| **Global config** | `~/.gemini/GEMINI.md`, `~/.gemini/settings.json` |
| **Context surfaces** | GEMINI.md cascade (deepest is most specific), `.geminiignore` for filtering, settings.json `context.fileName` for custom filenames |
| **Unique features** | Bidirectional cascade (loads parent dirs AND subdirs), `/memory add` command for persistent global memory, `/memory refresh` to re-scan, configurable context filename |

#### Cursor IDE + Agent CLI (`.cursor/`)

| Aspect | Detail |
|--------|--------|
| **Generated file** | .cursorrules (Lean profile: Identity + Navigation) |
| **Auto-load** | Reads `.cursorrules` at project root + `.cursor/rules/` directory. **CLI also reads AGENTS.md and CLAUDE.md at project root** and applies them as rules |
| **Config dir** | `.cursor/` |
| **Global config** | `~/.cursor/cli-config.json` (CLI global settings) |
| **Project config** | `.cursor/cli.json` (CLI permissions), `.cursor/mcp.json` (MCP servers) |
| **Context surfaces** | `rules/` (warm — same system as IDE), MCP servers, agent configs |
| **MCP config** | `.cursor/mcp.json` (project) and `~/.cursor/mcp.json` (global) |
| **Unique features** | CLI reads CLAUDE.md + AGENTS.md as bonus rules (cross-tool consumption), same rules system as IDE editor, headless/CI operation, parallel agent instances |

#### GitHub Copilot (`.github/`)

| Aspect | Detail |
|--------|--------|
| **Generated file** | .github/copilot-instructions.md (Medium profile: Identity + Triggers + Navigation) |
| **Auto-load** | Reads `.github/copilot-instructions.md` at repo root |
| **Config dir** | `.github/` |
| **Context surfaces** | copilot-instructions.md only — limited dynamic runtime |
| **Unique features** | Minimal config surface — bias toward strong static propagation |

### Three content profiles

`agnostic-sync.sh` generates files at three detail levels, matched to each app's context budget and native capabilities:

| Profile | What's included | Used by | Rationale |
|---------|----------------|---------|-----------|
| **Full** | All STATIC sections from 0AGNOSTIC.md + .1merge additions + promoted rules | Claude Code, Codex, Gemini | These apps have large context windows and cascade mechanisms that walk the full hierarchy |
| **Medium** | Identity, Triggers, Navigation, Key Behaviors | GitHub Copilot | Moderate context budget, needs enough pointers to be useful but can't handle full detail |
| **Lean** | Identity, Navigation only | Cursor | Cursor has built-in indexing, its own rules/ system, AND reads CLAUDE.md/AGENTS.md as supplementary rules — .cursorrules just needs to orient the agent |

**Important**: Cursor CLI's cross-consumption of CLAUDE.md and AGENTS.md means our Full-profile generated files serve double duty — they're native to their primary app AND consumed as supplementary context by Cursor.

### The .1merge projection layer

`.1merge` is the bridge between tool-agnostic source and app-specific configuration. Each AI app gets its own merge directory:

```
.1merge/
├── .1claude_merge/           ◄── Claude Code adaptations
│   ├── 0_synced/             (from 0AGNOSTIC canonical content)
│   ├── 1_overrides/          (Claude-specific behavior changes)
│   └── 2_additions/          (Claude-only content: tool usage, session continuity)
│
├── .1agents_merge/           ◄── Codex / OpenAI adaptations (future)
│   ├── 0_synced/
│   ├── 1_overrides/
│   └── 2_additions/
│
├── .1cursor_merge/           ◄── Cursor / Cursor Agent adaptations (future)
│   ├── 0_synced/
│   ├── 1_overrides/
│   └── 2_additions/
│
├── .1gemini_merge/           ◄── Gemini CLI adaptations (future)
│   ├── 0_synced/
│   ├── 1_overrides/
│   └── 2_additions/
│
└── .1copilot_merge/          ◄── GitHub Copilot adaptations (future)
    ├── 0_synced/
    ├── 1_overrides/
    └── 2_additions/
```

**Merge precedence**: `2_additions` > `1_overrides` > `0_synced`. Higher tiers win when there's a conflict.

**Scoping rule**: Content in `.1claude_merge/2_additions/` appears ONLY in CLAUDE.md. It never leaks into AGENTS.md or GEMINI.md. Each app's additions are isolated to that app's generated file.

### App-specific context surfaces beyond generated files

The generated tool file is just the **entry point**. Each AI app has additional context surfaces that the agnostic system populates:

| Surface | Claude Code | Cursor / Agent | Codex CLI | Copilot | Gemini CLI |
|---------|------------|----------------|-----------|---------|------------|
| Auto-loaded context | CLAUDE.md cascade | .cursorrules + CLAUDE.md + AGENTS.md | AGENTS.md cascade | copilot-instructions.md | GEMINI.md hierarchy |
| Path-scoped rules | `.claude/rules/*.md` | `.cursor/rules/*.md` | N/A | N/A | N/A |
| Skills / Commands | `.claude/skills/` | N/A | Agent Skills | N/A | N/A |
| Agent definitions | `.claude/agents/` | (future) | N/A | N/A | N/A |
| Hooks | `settings.json` hooks | N/A | N/A | N/A | N/A |
| MCP config | `settings.json` | `.cursor/mcp.json` | N/A | N/A | N/A |
| Override mechanism | N/A | N/A | AGENTS.override.md | N/A | `.geminiignore` |
| Global config | `~/.claude/CLAUDE.md` | `~/.cursor/cli-config.json` | `~/.codex/config.toml` | N/A | `~/.gemini/settings.json` |
| Memory / Persistence | auto-memory dir | N/A | N/A | N/A | `/memory add` commands |

These additional surfaces are populated from `.0agnostic/` content through the avenue web. Some are generated by sync scripts, while others are manually maintained with content deriving from the agnostic source of truth.

**Cross-tool consumption note**: Cursor CLI's reading of CLAUDE.md and AGENTS.md means our generated files serve multiple apps simultaneously. This is a feature, not a bug — the agnostic system's Full-profile files contain universal context that any app can benefit from.

### Complete propagation pipeline

```
.0agnostic/ (01-05: source content)
      │
      ▼
0AGNOSTIC.md (consolidated entry point)
      │
      ├──▶ agnostic-sync.sh ──▶ Generated tool files (CLAUDE.md, AGENTS.md, etc.)
      │                              │
      │                              ├──▶ .claude/  (Claude Code reads CLAUDE.md + rules/ + skills/)
      │                              ├──▶ .codex/   (Codex CLI reads AGENTS.md)
      │                              ├──▶ .cursor/  (Cursor reads .cursorrules + rules/)
      │                              ├──▶ .gemini/  (Gemini CLI reads GEMINI.md)
      │                              └──▶ .github/  (Copilot reads copilot-instructions.md)
      │
      └──▶ .0agnostic/06_context_avenue_web/ ──▶ Avenue web runtime loading
                (skills, rules, JSON-LD, integration.md, episodic memory)
                     │
                     └──▶ Each app accesses on-demand through its native mechanism
                          (Claude: skills/rules, Cursor: rules/, etc.)
```

---

## Automation Tools

| Tool | Direction | What it moves | When to run |
|------|-----------|---------------|-------------|
| `agnostic-sync.sh` | Lateral | 0AGNOSTIC.md STATIC → tool files | After editing any 0AGNOSTIC.md |
| `sync-handoffs.sh` | Vertical + Horizontal | Reports → entity + siblings + parent | After updating any stage or layer report |
| `episodic-sync.sh` | Lateral | Episodic memory → auto-memory | After session work |

### Propagation triggers

| Event | What propagates | Script |
|-------|----------------|--------|
| Stage agent completes work | stage_report.md written | Manual (agent writes on exit) |
| Any report updated | Reports distributed to hierarchy | `sync-handoffs.sh` |
| Entity manager reviews stages | stages_report.md + child_layers_report.md | Manual (manager consolidates) |
| 0AGNOSTIC.md edited | Tool files regenerated | `agnostic-sync.sh` |
| Session ends | Episodic memory captured | `episodic-sync.sh` |

---

## Related Documents

- **Top-down propagation**: `03_propagation_chain_architecture.md`
- **0AGNOSTIC + .1merge integration**: `02_0agnostic_1merge_avenue_web_integration_design.md` — detailed merge tier semantics and cross-tool application model
- **What inherits across levels**: `05_hierarchy_inheritance_model.md`
- **Source-to-avenue flow**: `06_source_of_truth_to_avenue_flow.md` — .0agnostic/ numbering and authority direction
- **Sync orchestrator**: `07_unified_sync_architecture.md`
- **Discovery temperatures**: `08_discovery_temperature_model.md` — hot/warm/cold maps to content profiles
- **Stage report format**: `../../.0agnostic/03_protocols/stage_report_protocol.md`
- **Stages manager pattern**: `...agent_delegation_system/.../stage_1_04_design/outputs/design_decisions/stages_manager_pattern.md` — proposed coordinator for stage orchestration

---

## Sources

App-specific configuration research informing Diagram 3:

- [Cursor CLI Configuration](https://cursor.com/docs/cli/reference/configuration) — `~/.cursor/cli-config.json`, `.cursor/cli.json` (permissions)
- [Using Cursor Agent CLI](https://cursor.com/docs/cli/using) — `.cursor/rules/` system, reads CLAUDE.md + AGENTS.md as rules, headless/CI operation
- [Cursor CLI MCP](https://cursor.com/docs/cli/mcp) — MCP server integration via `.cursor/mcp.json`
- [Codex CLI AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) — AGENTS.md cascade walk, AGENTS.override.md, `~/.codex/AGENTS.md` global, 32 KiB project_doc_max_bytes
- [Codex CLI Config Basics](https://developers.openai.com/codex/config-basic/) — `.codex/config.toml`, `~/.codex/config.toml`, trust settings
- [Codex CLI Agent Skills](https://developers.openai.com/codex/skills/) — Agent Skills system
- [Gemini CLI Configuration](https://google-gemini.github.io/gemini-cli/docs/get-started/configuration.html) — `~/.gemini/` directory, settings.json, .geminiignore
- [Gemini CLI GEMINI.md](https://google-gemini.github.io/gemini-cli/docs/cli/gemini-md.html) — Hierarchical loading (global → parent dirs → cwd → subdirs), `/memory` commands, configurable context filename
