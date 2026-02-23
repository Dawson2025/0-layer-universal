# Context Propagation Design

How work products consolidate within stages and propagate across the layer-stage hierarchy.

**Companion**: `AI_CONTEXT_FLOW_ARCHITECTURE.md` covers **top-down context loading** (how agents receive context). This document covers **bottom-up context propagation** (how work products consolidate and flow upward).

---

## The Universal Pattern

Every level in the hierarchy follows the same consolidation funnel:

```
Many detailed files  →  Consolidation reports  →  Structured system  →  Summary report  →  Entry point
     (inputs)            (overview + refs)         (.0agnostic/)        (stage/layer rpt)   (0AGNOSTIC.md)
```

- **Stages**: inputs are work product files in `outputs/`
- **Entities**: inputs are stage reports + child layer reports, consolidated via overview reports

The pattern is recursive. A stage report becomes input to its entity. An entity's layer report becomes input to its parent. All the way to the root.

The theme is **progressive detail reduction**: each tier summarizes, organizes, references, and consolidates the tier above it. The final result — `0AGNOSTIC.md` — is the single entry point that ties everything together for any AI agent arriving at that level.

---

## Diagram 1: Stage-Internal Consolidation Funnel

How content within a single stage reduces from many detailed files down to a single consolidated entry point.

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
│   └── 06_context_avenue_web/  Agent access paths (AALang,        │
│                               skills, hooks, etc.)               │
│                                                                  │
│          │                                                       │
│          ▼  extracted into <30-line summary for the hierarchy    │
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
│   │ STATIC (always loaded):                    CONSOL- │         │
│   │   Identity, Key Behaviors, Methodology,    IDATED  │         │
│   │   Inputs/Outputs, Triggers, AALang,                │         │
│   │   Current Status (substantive summary —            │         │
│   │     the most distilled view of where               │         │
│   │     this stage stands)                             │         │
│   │                                                    │         │
│   │ DYNAMIC (loaded on-demand):                        │         │
│   │   Current State Detail, Key Outputs table,         │         │
│   │   Key Findings, Open Items, Handoff,               │         │
│   │   Navigation (pointers into .0agnostic/)           │         │
│   └────────────────────────────────────────────────────┘         │
│          │                                                       │
│          └──▶  agnostic-sync.sh  ──▶  CLAUDE.md, AGENTS.md,     │
│                                       GEMINI.md, OPENAI.md,     │
│                                       .cursorrules,             │
│                                       copilot-instructions.md   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### What each tier does

| Tier | Contains | Produced by | Consumed by |
|------|----------|-------------|-------------|
| `outputs/` | Raw work products — files, data, drafts | Stage agent during work | The agent itself; next-stage agents |
| `outputs/reports/output_report.md` | Organized overview referencing all outputs | Stage agent on completion | Stage agent (to write report + update .0agnostic) |
| `.0agnostic/` | Structured system — knowledge, rules, protocols, avenues | Stage agent; sync scripts | Any agent entering this stage |
| `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | <30-line summary covering the whole stage | Stage agent before exiting | Entity manager; sibling stages (via sync) |
| `0AGNOSTIC.md` | Consolidated entry point — identity + status + references | Stage agent (updated each session) | Any AI agent delegated to this stage |

### How each tier references the one above

- **`output_report.md`** references files in `outputs/` by relative path — organizes and summarizes them
- **`.0agnostic/`** structures insights FROM outputs and the output report into knowledge, rules, protocols
- **`stage_report.md`** draws from the output report + .0agnostic content to summarize the whole stage (not just outputs — also findings, constraints, handoff readiness)
- **`0AGNOSTIC.md`** integrates everything: references INTO `.0agnostic/` for detail, includes Current Status as the most distilled pointer to where things stand

---

## Diagram 2: Cross-Level Connection Map

How stages feed entities, child entities feed parent entities, and how entities consolidate all inputs.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   ROOT ENTITY (e.g., 0_layer_universal)                                │
│                                                                         │
│   Receives layer_reports from child entities (layer_0, layer_1, etc.)  │
│   Consolidates into own .0agnostic/ → 0AGNOSTIC.md → CLAUDE.md        │
│                                                                         │
│          ▲ layer_report                                                 │
│          │                                                              │
│  ┌───────┴──────────────────────────────────────────────────────────┐   │
│  │                                                                   │   │
│  │   ENTITY (e.g., layer_0_feature_X)                               │   │
│  │                                                                   │   │
│  │   RAW INPUTS ─────────────────────────────────────────────────   │   │
│  │                                                                   │   │
│  │   From ABOVE (parent):                                           │   │
│  │   └─ 01_incoming/01_from_above/                                  │   │
│  │      ├── layer_report.md          (parent's layer report)        │   │
│  │      └── manager_instructions.md  (parent's directives)         │   │
│  │                                                                   │   │
│  │   From BELOW (own stages):                                       │   │
│  │   └─ 01_incoming/03_from_below/stage_reports/                    │   │
│  │      ├── layer_N.stage_01_request_gathering.stage_report.md     │   │
│  │      ├── layer_N.stage_02_research.stage_report.md              │   │
│  │      ├── layer_N.stage_04_design.stage_report.md                │   │
│  │      └── ...one per active stage                                │   │
│  │                                                                   │   │
│  │   From BELOW (child entities):                                   │   │
│  │   └─ 01_incoming/03_from_below/layer_reports/                    │   │
│  │      ├── layer_N+1.child_entity_A.layer_report.md               │   │
│  │      └── layer_N+1.child_entity_B.layer_report.md               │   │
│  │                                                                   │   │
│  │   CONSOLIDATION REPORTS ──────────────────────────────────────   │   │
│  │                                                                   │   │
│  │   The entity manager creates consolidation documents             │   │
│  │   that overview, summarize, and reference all incoming reports:  │   │
│  │                                                                   │   │
│  │   02_outgoing/01_to_above/                                       │   │
│  │   ├── stages_report.md          CONSOLIDATES all stage reports: │   │
│  │   │                              - Summarizes each stage's       │   │
│  │   │                                status, findings, blockers    │   │
│  │   │                              - References each stage_report  │   │
│  │   │                                by path for drill-down        │   │
│  │   │                              - Cross-stage patterns +        │   │
│  │   │                                readiness overview            │   │
│  │   │                                                              │   │
│  │   └── child_layers_report.md    CONSOLIDATES all child layer    │   │
│  │                                  reports:                        │   │
│  │                                  - Summarizes each child's       │   │
│  │                                    status and key findings       │   │
│  │                                  - References each layer_report  │   │
│  │                                    by path for drill-down        │   │
│  │                                  - Cross-entity patterns +       │   │
│  │                                    dependencies                  │   │
│  │                                                                   │   │
│  │          │                                                        │   │
│  │          ▼  structured into navigable system                     │   │
│  │                                                                   │   │
│  │   .0agnostic/                                                    │   │
│  │   ├── 01_knowledge/      (entity-level insights)                 │   │
│  │   ├── 02_rules/          (entity-level constraints)              │   │
│  │   ├── 03_protocols/      (entity-level processes)                │   │
│  │   ├── 05_handoff_docs/   (incoming + outgoing + consolidation)  │   │
│  │   └── 06_avenue_web/     (agent access: AALang, skills, etc.)   │   │
│  │                                                                   │   │
│  │          │                                                        │   │
│  │          ▼  extracted summary                                    │   │
│  │                                                                   │   │
│  │   layer_report.md                                                │   │
│  │   ┌──────────────────────────────────────────────────────┐       │   │
│  │   │ Summarizes entity status across all stages + child   │       │   │
│  │   │ entities. Key findings, open items, readiness.       │       │   │
│  │   │ Draws from: stages_report + child_layers_report      │       │   │
│  │   │ + .0agnostic/ content                                │       │   │
│  │   └──────────────────────────────────────────────────────┘       │   │
│  │          │                                                        │   │
│  │          │  → sync-handoffs.sh distributes UP to parent          │   │
│  │          │  → sync-handoffs.sh distributes DOWN to own stages    │   │
│  │          │                                                        │   │
│  │          ▼  consolidated entry point                             │   │
│  │                                                                   │   │
│  │   0AGNOSTIC.md                                                   │   │
│  │   ┌──────────────────────────────────────────────────────┐       │   │
│  │   │ STATIC: Entity identity, Current Status summarizing  │       │   │
│  │   │   all stages + child entities, Key Behaviors         │       │   │
│  │   │ DYNAMIC: Stage-by-stage state, child entity state,   │       │   │
│  │   │   navigation into .0agnostic/                        │       │   │
│  │   │                                                      │       │   │
│  │   │ THE entry point for any AI agent at this level       │       │   │
│  │   └──────────────────────────────────────────────────────┘       │   │
│  │          │                                                        │   │
│  │          └──▶  agnostic-sync.sh  ──▶  CLAUDE.md (agent entry)   │   │
│  │                                                                   │   │
│  │   STAGES ─────────────────────────────────────────────────────   │   │
│  │                                                                   │   │
│  │   Each stage follows the SAME funnel internally (Diagram 1):    │   │
│  │                                                                   │   │
│  │   ┌─────────┐ ┌─────────┐ ┌─────────┐       ┌─────────┐       │   │
│  │   │stage_01 │ │stage_02 │ │stage_04 │  ...  │stage_11 │       │   │
│  │   │         │ │         │ │         │       │         │       │   │
│  │   │outputs/ │ │outputs/ │ │outputs/ │       │outputs/ │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │out_rpt  │ │out_rpt  │ │out_rpt  │       │out_rpt  │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │.0agnstc│ │.0agnstc│ │.0agnstc│       │.0agnstc│       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │stg_rpt │ │stg_rpt │ │stg_rpt │       │stg_rpt │       │   │
│  │   │  ↓      │ │  ↓      │ │  ↓      │       │  ↓      │       │   │
│  │   │0AGNOSTC│ │0AGNOSTC│ │0AGNOSTC│       │0AGNOSTC│       │   │
│  │   └────┬────┘ └────┬────┘ └────┬────┘       └────┬────┘       │   │
│  │        │            │           │                  │            │   │
│  │        │     ◄──────┼───────►   │   (lateral:     │            │   │
│  │        │     sibling reports    │    from_sides)   │            │   │
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
| Stage ↔ Stage (lateral) | `stage_report.md` | `sync-handoffs.sh` → sibling `from_sides/` (left or right) |
| All stage reports → Consolidation | `stages_report.md` | Entity manager writes overview of all stages |
| All child layer reports → Consolidation | `child_layers_report.md` | Entity manager writes overview of all children |
| Consolidation → .0agnostic → layer_report | `.0agnostic/`, `layer_report.md` | Entity manager structures + extracts |
| Child Entity → Parent Entity (up) | `layer_report.md` | `sync-handoffs.sh` → parent `from_below/layer_reports/` |
| Entity → Stages (down) | `layer_report.md`, `manager_instructions.md` | `sync-handoffs.sh` → stage `from_above/` |
| 0AGNOSTIC.md → Tool files (lateral) | STATIC context section | `agnostic-sync.sh` → CLAUDE.md, AGENTS.md, etc. |

### How 0AGNOSTIC.md acts as the entry point

When an AI agent is delegated to any level (stage or entity):

1. **First read**: `0AGNOSTIC.md` — STATIC section is always loaded, gives identity + current status
2. **On-demand**: DYNAMIC section references into `.0agnostic/` for detail — agent reads only what's needed
3. **Tool-specific**: `agnostic-sync.sh` has already generated CLAUDE.md (etc.) from STATIC, so tool-native context is pre-built
4. **Full detail**: Agent can traverse to `outputs/` (stages) or `from_below/` (entities) for raw inputs

0AGNOSTIC.md is the **most consolidated document** at any level. It integrates identity, methodology, and current status into a single file that gives any agent enough context to work — with pointers to progressively more detail when needed.

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
- **Consolidation increases** — each level distills its inputs through consolidation reports into a .0agnostic system, then a summary report, then an entry point
- **The same pattern**: many inputs → consolidation overview → structured system → summary report → entry point (0AGNOSTIC.md)

---

## Automation Tools

| Tool | Direction | What it moves | When to run |
|------|-----------|---------------|-------------|
| `agnostic-sync.sh` | Lateral | 0AGNOSTIC.md STATIC → CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md | After editing any 0AGNOSTIC.md |
| `sync-handoffs.sh` | Vertical + Horizontal | Stage reports → entity + siblings; layer reports → stages + parent entity; manager instructions → stages | After updating any stage or layer report |
| `episodic-sync.sh` | Lateral | Episodic memory indexes → auto-memory topic file | After session work |

**Script locations**: `.0agnostic/01_knowledge/layer_stage_system/resources/tools/`

### Propagation triggers

| Event | What propagates | Script |
|-------|----------------|--------|
| Stage agent completes work | stage_report.md written | Manual (agent writes on exit) |
| Any report updated | Reports distributed to hierarchy | `sync-handoffs.sh` |
| Entity manager reviews stages | stages_report.md + child_layers_report.md written | Manual (manager consolidates) |
| 0AGNOSTIC.md edited | Tool files regenerated | `agnostic-sync.sh` |
| Session ends | Episodic memory captured | `episodic-sync.sh` |

---

## See Also

- **Top-down context loading**: `AI_CONTEXT_FLOW_ARCHITECTURE.md` — how agents RECEIVE context (CLAUDE.md chain, avenue web, layer cascade)
- **Stage report format**: `../03_protocols/stage_report_protocol.md` — exact format + sync-handoffs.sh usage
- **0AGNOSTIC.md template**: `layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` — canonical stage entry point structure
- **Entity structure**: `../06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` — full directory tree
