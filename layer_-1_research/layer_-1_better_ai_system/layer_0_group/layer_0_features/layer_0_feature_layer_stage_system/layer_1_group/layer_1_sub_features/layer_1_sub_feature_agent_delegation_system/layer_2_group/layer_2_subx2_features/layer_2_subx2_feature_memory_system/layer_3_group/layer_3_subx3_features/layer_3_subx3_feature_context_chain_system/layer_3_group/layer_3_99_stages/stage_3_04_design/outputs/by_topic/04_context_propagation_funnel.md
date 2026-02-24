# Context Propagation Funnel (Bottom-Up)

**Date**: 2026-02-23
**Status**: Approved and implemented
**Scope**: How work products consolidate within stages and propagate upward across the layer-stage hierarchy

---

## Overview

The propagation chain architecture (doc 03) covers **top-down** flow: how context reaches agents. This document covers **bottom-up** flow: how work products consolidate and propagate upward through the hierarchy.

The core insight: **stages and entities follow the same consolidation pattern** — many inputs → consolidation overview → structured system → summary report → entry point.

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
- **What inherits across levels**: `05_hierarchy_inheritance_model.md`
- **Sync orchestrator**: `07_unified_sync_architecture.md`
- **Stage report format**: `../../.0agnostic/03_protocols/stage_report_protocol.md`
