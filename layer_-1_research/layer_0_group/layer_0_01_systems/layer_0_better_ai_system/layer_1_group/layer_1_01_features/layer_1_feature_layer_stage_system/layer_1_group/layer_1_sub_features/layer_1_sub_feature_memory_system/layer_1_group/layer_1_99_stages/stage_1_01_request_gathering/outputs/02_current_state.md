---
resource_id: "d4f59f95-aaed-4fbd-a5d1-4f964bc37614"
resource_type: "output"
resource_name: "02_current_state"
---
# Current State: What Memory Mechanisms Exist Today

## Overview

The layer-stage framework has five distinct memory mechanisms, each serving a different purpose but not coordinated into a unified system.

---

## 1. CLAUDE.md Context Chain (Static Hierarchical Memory)

### What It Is
A chain of CLAUDE.md files from the user root down to the current working directory. Each file is auto-generated from its corresponding `0AGNOSTIC.md` source.

### How It Works
- **Loading**: Claude Code automatically reads all CLAUDE.md files in the ancestor path at session start
- **Hierarchy**: `~/.claude/CLAUDE.md` → `~/CLAUDE.md` → `~/dawson-workspace/CLAUDE.md` → `~/dawson-workspace/code/CLAUDE.md` → `~/dawson-workspace/code/0_layer_universal/CLAUDE.md` → deeper per layer/stage
- **Scope**: Each file defines identity, triggers, pointers, and contribution locations for its level

### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Static (always loaded) |
| **Form** | Token-level (Markdown text in context) |
| **Function** | Factual + Working (identity, rules, navigation) |
| **Persistence** | Permanent (git-tracked files) |
| **Cost** | Every line costs tokens on EVERY API call |
| **Tool-agnostic?** | Partially — `0AGNOSTIC.md` is source; CLAUDE.md is Claude-specific |

### Current Strengths
- Reliable hierarchical context loading
- Human-readable and editable
- Git-tracked version history
- Survives context compaction

### Current Gaps
- No dynamic adaptation — loads everything regardless of relevance
- No way to load sibling/cousin entity context (only ancestors)
- Token cost scales with hierarchy depth
- Child CLAUDE.md files only load on-demand when entering directories

---

## 2. Auto-Memory (`~/.claude/projects/*/memory/`)

### What It Is
Claude Code's built-in persistent memory — Markdown files that persist across conversations.

### How It Works
- **MEMORY.md**: First 200 lines loaded into system prompt every session
- **Topic files**: Sit alongside MEMORY.md, loaded on-demand (not at startup)
- **Updates**: Claude records operational learnings; users can say "remember X"
- **Location**: `~/.claude/projects/<project-path-hash>/memory/`

### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (persists across sessions) |
| **Form** | Token-level (Markdown) |
| **Function** | Experiential (learnings, gotchas, conventions) |
| **Persistence** | Permanent (local filesystem, NOT git-tracked) |
| **Scope** | Per-launch-directory ONLY |
| **Tool-agnostic?** | No — Claude Code specific |

### Current Strengths
- Automatic learning accumulation
- Loaded into every session without manual effort
- Topic files allow expansion

### Current Gaps
- **Flat, not hierarchical** — different cwd = completely different memory
- **Not shared** — per-machine, not synced, not in git
- **200-line limit** — MEMORY.md truncated after 200 lines in system prompt
- **No cross-project bridging** — learnings from one project don't transfer

---

## 3. Episodic Memory Bridge (`.0agnostic/episodic_memory/`)

### What It Is
A directory structure at each entity level for recording session histories and work-in-progress.

### How It Works
- **Session files**: Created after significant work with date, changes, decisions
- **index.md**: Aggregated session history for the entity
- **Divergence log**: Tracks when shared outputs are modified
- **Sync tool**: `tools/episodic-sync.sh` generates `memory/episodic.md` in auto-memory

### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (git-tracked) |
| **Form** | Token-level (Markdown) |
| **Function** | Episodic (session records, what happened when) |
| **Persistence** | Permanent (git-tracked) |
| **Scope** | Per-entity (hierarchical) |
| **Tool-agnostic?** | Yes (plain Markdown, any tool can read) |

### Current Strengths
- Tool-agnostic design
- Hierarchical per-entity structure
- Git-tracked for version history
- Sync bridge to auto-memory

### Current Gaps
- **Mostly empty** — directories exist as `.gitkeep` stubs
- **Manual creation** — requires discipline to write session files
- **No automated extraction** — agent doesn't auto-record significant events
- **Sync tool rarely run** — `episodic-sync.sh` needs to be triggered manually
- **No retrieval mechanism** — reading episodic memory requires knowing which entity to look at

---

## 4. Status.json (Stage Tracking)

### What It Is
JSON files tracking which stage each entity is in, with progress and history.

### How It Works
- **Location**: `<entity>/layer_N_group/layer_N_99_stages/status_N.json`
- **Content**: Feature name, layer, current stage, stage history, progress percentage, last updated
- **Read**: At session start as part of context traversal rule

### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Long-term (git-tracked) |
| **Form** | Token-level (structured JSON) |
| **Function** | Working (project state tracking) |
| **Persistence** | Permanent |
| **Scope** | Per-entity |
| **Tool-agnostic?** | Yes (JSON readable by anything) |

### Current Strengths
- Clear stage tracking
- Machine-readable format
- Lightweight

### Current Gaps
- **Rarely updated** — often stale
- **No automation** — stage transitions are manual
- **Minimal metadata** — no record of WHY stage changed or what was accomplished

---

## 5. AALang / GAB Agent Definitions (`.gab.jsonld`)

### What It Is
Formal agent specifications that define modes, actors, personas, and constraints for AI behavior.

### How It Works
- **Format**: JSON-LD graph with GAB vocabulary
- **Integration summaries**: `.integration.md` files provide human-readable versions
- **Context loading**: Agent definitions describe WHAT SHOULD happen (design spec)
- **Runtime**: Claude reads these as natural language guidance, not executable code

### Characteristics
| Property | Value |
|----------|-------|
| **Duration** | Permanent (design specification) |
| **Form** | Token-level (JSON-LD + Markdown summaries) |
| **Function** | Procedural (how to behave in each mode) |
| **Persistence** | Permanent (git-tracked) |
| **Tool-agnostic?** | Yes (JSON-LD is universal) |

### Current Strengths
- Formal specification of ideal behavior
- Rich mode/constraint definitions
- Tool-agnostic format

### Current Gaps
- **Not runtime-executable** — guidance only, not enforced
- **Gap between spec and reality** — defines confidence thresholds, state persistence, etc. that don't actually run
- **Large context cost** — full .gab.jsonld files are verbose

---

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
