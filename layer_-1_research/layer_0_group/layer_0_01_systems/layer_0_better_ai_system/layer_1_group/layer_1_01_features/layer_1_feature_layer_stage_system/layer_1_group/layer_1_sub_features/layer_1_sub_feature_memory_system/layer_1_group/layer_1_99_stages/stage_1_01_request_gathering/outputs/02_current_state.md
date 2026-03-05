---
resource_id: "d4f59f95-aaed-4fbd-a5d1-4f964bc37614"
resource_type: "output"
resource_name: "02_current_state"
---
# Current State: What Memory Mechanisms Exist Today

<!-- section_id: "6593b291-afde-4ed4-a60a-569910655de6" -->
## Overview

The layer-stage framework has five distinct memory mechanisms, each serving a different purpose but not coordinated into a unified system.

---

<!-- section_id: "91901947-328c-419e-a42e-f390aa7ea7e3" -->
## 1. CLAUDE.md Context Chain (Static Hierarchical Memory)

<!-- section_id: "6c1d4ed9-0847-4b1d-ab69-ab9c0be3e78a" -->
### What It Is
A chain of CLAUDE.md files from the user root down to the current working directory. Each file is auto-generated from its corresponding `0AGNOSTIC.md` source.

<!-- section_id: "59fdeaa6-734e-4841-ac62-e6831ebbfdca" -->
### How It Works
- **Loading**: Claude Code automatically reads all CLAUDE.md files in the ancestor path at session start
- **Hierarchy**: `~/.claude/CLAUDE.md` → `~/CLAUDE.md` → `~/dawson-workspace/CLAUDE.md` → `~/dawson-workspace/code/CLAUDE.md` → `~/dawson-workspace/code/0_layer_universal/CLAUDE.md` → deeper per layer/stage
- **Scope**: Each file defines identity, triggers, pointers, and contribution locations for its level

<!-- section_id: "9aa1f178-9bcd-4fcc-8810-89688f062692" -->
### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Static (always loaded) |
| **Form** | Token-level (Markdown text in context) |
| **Function** | Factual + Working (identity, rules, navigation) |
| **Persistence** | Permanent (git-tracked files) |
| **Cost** | Every line costs tokens on EVERY API call |
| **Tool-agnostic?** | Partially — `0AGNOSTIC.md` is source; CLAUDE.md is Claude-specific |

<!-- section_id: "9971042a-3e53-42dd-b68e-10c962f93992" -->
### Current Strengths
- Reliable hierarchical context loading
- Human-readable and editable
- Git-tracked version history
- Survives context compaction

<!-- section_id: "6d2e96d7-406d-43ff-ab9e-de05612ad616" -->
### Current Gaps
- No dynamic adaptation — loads everything regardless of relevance
- No way to load sibling/cousin entity context (only ancestors)
- Token cost scales with hierarchy depth
- Child CLAUDE.md files only load on-demand when entering directories

---

<!-- section_id: "153882fa-27a6-4875-8e7c-94c879564bc8" -->
## 2. Auto-Memory (`~/.claude/projects/*/memory/`)

<!-- section_id: "b983a0b3-7249-4503-9510-d8202666ab0c" -->
### What It Is
Claude Code's built-in persistent memory — Markdown files that persist across conversations.

<!-- section_id: "e93fd628-8dd7-4bdb-b3b1-1fffc08d9792" -->
### How It Works
- **MEMORY.md**: First 200 lines loaded into system prompt every session
- **Topic files**: Sit alongside MEMORY.md, loaded on-demand (not at startup)
- **Updates**: Claude records operational learnings; users can say "remember X"
- **Location**: `~/.claude/projects/<project-path-hash>/memory/`

<!-- section_id: "c9539b29-a083-477a-86aa-cc059ed0275c" -->
### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (persists across sessions) |
| **Form** | Token-level (Markdown) |
| **Function** | Experiential (learnings, gotchas, conventions) |
| **Persistence** | Permanent (local filesystem, NOT git-tracked) |
| **Scope** | Per-launch-directory ONLY |
| **Tool-agnostic?** | No — Claude Code specific |

<!-- section_id: "39bd8c11-edc4-4ead-9e52-45db761a2ecd" -->
### Current Strengths
- Automatic learning accumulation
- Loaded into every session without manual effort
- Topic files allow expansion

<!-- section_id: "69ab980e-65f2-4931-aa2f-f4b7f7a33971" -->
### Current Gaps
- **Flat, not hierarchical** — different cwd = completely different memory
- **Not shared** — per-machine, not synced, not in git
- **200-line limit** — MEMORY.md truncated after 200 lines in system prompt
- **No cross-project bridging** — learnings from one project don't transfer

---

<!-- section_id: "51f45d1e-a5ef-4dd3-bca0-94f5d9c7f988" -->
## 3. Episodic Memory Bridge (`.0agnostic/episodic_memory/`)

<!-- section_id: "53ce03db-3be1-4852-a013-abd332bc34d0" -->
### What It Is
A directory structure at each entity level for recording session histories and work-in-progress.

<!-- section_id: "f37d7fdc-f7d5-4359-acbb-1ab57eabac8b" -->
### How It Works
- **Session files**: Created after significant work with date, changes, decisions
- **index.md**: Aggregated session history for the entity
- **Divergence log**: Tracks when shared outputs are modified
- **Sync tool**: `tools/episodic-sync.sh` generates `memory/episodic.md` in auto-memory

<!-- section_id: "76250900-61de-49b6-b724-a660a6e96dd0" -->
### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (git-tracked) |
| **Form** | Token-level (Markdown) |
| **Function** | Episodic (session records, what happened when) |
| **Persistence** | Permanent (git-tracked) |
| **Scope** | Per-entity (hierarchical) |
| **Tool-agnostic?** | Yes (plain Markdown, any tool can read) |

<!-- section_id: "d0636865-e407-4cc4-8cdc-54076d9e8be9" -->
### Current Strengths
- Tool-agnostic design
- Hierarchical per-entity structure
- Git-tracked for version history
- Sync bridge to auto-memory

<!-- section_id: "a6724448-8a0d-422c-8079-55fa684b936a" -->
### Current Gaps
- **Mostly empty** — directories exist as `.gitkeep` stubs
- **Manual creation** — requires discipline to write session files
- **No automated extraction** — agent doesn't auto-record significant events
- **Sync tool rarely run** — `episodic-sync.sh` needs to be triggered manually
- **No retrieval mechanism** — reading episodic memory requires knowing which entity to look at

---

<!-- section_id: "150f5910-e7c6-4c93-b55f-1cbc4a240815" -->
## 4. Status.json (Stage Tracking)

<!-- section_id: "4948019c-ebed-41ae-9a6b-1ec58fa9537e" -->
### What It Is
JSON files tracking which stage each entity is in, with progress and history.

<!-- section_id: "2f3781c5-e05b-4fff-b2f2-9d507472d291" -->
### How It Works
- **Location**: `<entity>/layer_N_group/layer_N_99_stages/status_N.json`
- **Content**: Feature name, layer, current stage, stage history, progress percentage, last updated
- **Read**: At session start as part of context traversal rule

<!-- section_id: "313ca0c3-2439-4db3-9819-51859ed9ee1a" -->
### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (git-tracked) |
| **Form** | Token-level (structured JSON) |
| **Function** | Working (project state tracking) |
| **Persistence** | Permanent |
| **Scope** | Per-entity |
| **Tool-agnostic?** | Yes (JSON readable by anything) |

<!-- section_id: "5650b2b6-b61b-4f14-a13e-b0897d9b86ee" -->
### Current Strengths
- Clear stage tracking
- Machine-readable format
- Lightweight

<!-- section_id: "1321650f-f64d-48fc-91b9-4b3ef1ddb836" -->
### Current Gaps
- **Rarely updated** — often stale
- **No automation** — stage transitions are manual
- **Minimal metadata** — no record of WHY stage changed or what was accomplished

---

<!-- section_id: "33d8509a-66fc-487f-9fbf-f84e1519e175" -->
## 5. AALang / GAB Agent Definitions (`.gab.jsonld`)

<!-- section_id: "5c5fcad8-fd97-423f-9c74-dba9ef388169" -->
### What It Is
Formal agent specifications that define modes, actors, personas, and constraints for AI behavior.

<!-- section_id: "c9cf38d9-46e5-4a3e-ad7d-2b5efa9c4c6a" -->
### How It Works
- **Format**: JSON-LD graph with GAB vocabulary
- **Integration summaries**: `.integration.md` files provide human-readable versions
- **Context loading**: Agent definitions describe WHAT SHOULD happen (design spec)
- **Runtime**: Claude reads these as natural language guidance, not executable code

<!-- section_id: "11db1f6f-923a-4883-8d71-75e116748feb" -->
### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Permanent (design specification) |
| **Form** | Token-level (JSON-LD + Markdown summaries) |
| **Function** | Procedural (how to behave in each mode) |
| **Persistence** | Permanent (git-tracked) |
| **Tool-agnostic?** | Yes (JSON-LD is universal) |

<!-- section_id: "6e925548-82b7-46c5-85f6-ec8c2a3f81a8" -->
### Current Strengths
- Formal specification of ideal behavior
- Rich mode/constraint definitions
- Tool-agnostic format

<!-- section_id: "22fc28da-093f-4210-9569-65cffacdf425" -->
### Current Gaps
- **Not runtime-executable** — guidance only, not enforced
- **Gap between spec and reality** — defines confidence thresholds, state persistence, etc. that don't actually run
- **Large context cost** — full .gab.jsonld files are verbose

---

<!-- section_id: "b449d6d4-12a3-4529-926f-48d9baacef56" -->
## Summary: What We Have vs. What We Need

| Capability | Have | Need |
|------------|------|------|
| Static hierarchical context | CLAUDE.md chain | Smarter loading (relevance-based) |
| Cross-session learning | Auto-memory (limited) | Unified, cross-project, tool-agnostic |
| Session history | Episodic stubs (empty) | Automated episodic recording |
| Stage tracking | status.json (stale) | Automated state transitions |
| Behavioral specification | AALang GAB agents | Runtime enforcement or transpilation |
| Dynamic context loading | Manual (Read tool) | Intelligent on-demand retrieval |
| Multi-agent sharing | Nothing | Shared memory protocol |
| Temporal reasoning | Nothing | "What were we doing last week?" |
| Forgetting/consolidation | Nothing | Decay, summarization, archival |
| Cross-tool memory | 0AGNOSTIC.md (partial) | Full tool-agnostic memory layer |
