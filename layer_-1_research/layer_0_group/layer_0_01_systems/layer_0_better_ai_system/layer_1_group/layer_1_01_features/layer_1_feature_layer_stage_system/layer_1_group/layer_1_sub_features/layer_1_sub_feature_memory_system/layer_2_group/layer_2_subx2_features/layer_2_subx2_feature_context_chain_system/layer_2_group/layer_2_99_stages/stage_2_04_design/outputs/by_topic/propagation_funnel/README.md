---
resource_id: "c0671b6e-717b-4ee3-8d4d-d2ba7034027e"
resource_type: "readme
output"
resource_name: "README"
---
# Propagation Funnel: Context Flow Architecture

**Date**: 2026-02-27
**Location**: `stage_2_04_design/outputs/by_topic/propagation_funnel/`
**Purpose**: Document the complete context propagation pathway from stage outputs through AI apps

---

<!-- section_id: "155aa049-c1be-4260-89cf-2b5dc6e95000" -->
## Overview

The **Propagation Funnel** is a hierarchical system that tracks how context flows through the entire system:

```
Stage Outputs (stage_2_04_design/outputs/)
         ↓
   [01_stage_outputs_to_stage_report]
         ↓
 Stage Reports (aggregated per stage)
         ↓
   [02_stage_reports_to_layer_reports]
         ↓
  Layer Reports (aggregated per layer)
         ↓
   [03_layer_reports_to_entity_reports]
         ↓
 Entity Reports (aggregated per entity)
         ↓
   [04_entity_context_to_ai_apps]
         ↓
  AI Apps (.claude/, .cursor/, .codex/, .gemini/, .github/)
         ↓
    User Interface & Skill Execution
```

Each level in the funnel represents a **transformation and aggregation** of context, ensuring information flows correctly from source to destination.

---

<!-- section_id: "2a352a41-5f46-411b-828b-f6322e8353d6" -->
## Four Propagation Levels

<!-- section_id: "f877f1ac-3949-4acc-9bcf-0742d36b1061" -->
### Level 01: Stage Outputs → Stage Reports
**Directory**: `01_stage_outputs_to_stage_report/`

**Purpose**: Collect all outputs from a stage and produce a comprehensive stage report

**Input**:
- Stage outputs (research, design, planning documents)
- Multiple files from `outputs/`, `by_purpose/`, etc.

**Processing**:
- Aggregate related documents
- Extract key findings and decisions
- Link to 0AGNOSTIC.md
- Identify what should port to AI apps

**Output**:
- `stage_report.md` — Comprehensive stage summary
- `0AGNOSTIC.md` — Stage context (if new stage created)
- AI app–specific contexts (CLAUDE.md, GEMINI.md, etc.)
- `.1merge_system/` — Merge rules for AI apps
- AI app directories (`.claude/`, `.cursor/`, `.codex/`, `.gemini/`, `.github/`)

**Subdirectories**:
- `01_outputs/` — Raw stage outputs
- `02_output_reports/` — Processed reports
- `03_0agnostic_system/` — Context definitions
- `1merge_system/` — Port mappings
- `.claude/`, `.codex/`, `.gemini/`, `.cursor/`, `.github/` — AI app–specific contexts

---

<!-- section_id: "2ff0934b-1370-479d-8617-1521925046de" -->
### Level 02: Stage Reports → Layer Reports
**Directory**: `02_stage_reports_to_layer_reports/`

**Purpose**: Aggregate stage reports into a unified layer report

**Input**:
- Multiple stage reports (stage_01, stage_02, ... stage_11)
- Each stage's 0AGNOSTIC.md, stage_report.md

**Processing**:
- Synthesize findings across all stages
- Identify cross-stage dependencies
- Link to layer's 0AGNOSTIC.md
- Map context to entities below

**Output**:
- `layer_report.md` — Comprehensive layer summary
- `0AGNOSTIC.md` — Layer context

**Subdirectories**:
- `01_stage_reports/` — Input from all stages
- `02_aggregated_layer_report/` — Processed report
- `03_0agnostic_system/` — Layer context

---

<!-- section_id: "9a0dca98-50db-408f-a190-1d6289685c56" -->
### Level 03: Layer Reports → Entity Reports
**Directory**: `03_layer_reports_to_entity_reports/`

**Purpose**: Translate layer context into entity-specific context

**Input**:
- Layer reports from parent layer
- Entity's own 0AGNOSTIC.md
- Inheritance rules from parent

**Processing**:
- Customize layer context for this entity
- Override with entity-specific rules
- Create entity-specific 0AGNOSTIC.md
- Prepare merge rules for AI apps

**Output**:
- Entity 0AGNOSTIC.md (source of truth)
- Entity-specific contexts
- Merge system rules

**Subdirectories**:
- `01_layer_reports/` — Input from parent layer
- `02_aggregated_entity_reports/` — Entity-specific reports
- `03_entity_0agnostic/` — Entity context system

---

<!-- section_id: "e8e539f6-cf74-419e-95d3-715cf7e5692e" -->
### Level 04: Entity Context → AI Apps
**Directory**: `04_entity_context_to_ai_apps/`

**Purpose**: Port entity context to each AI app's native configuration system

**Input**:
- Entity 0AGNOSTIC.md
- Entity .0agnostic/ directory
- .1merge/ merge rules

**Processing**:
- Run agnostic-sync.sh to generate CLAUDE.md, .cursorrules, etc. (Tier 0: synced)
- Apply .1merge Tier 1 (overrides) for app-specific boilerplate
- Apply .1merge Tier 2 (additions) for custom enhancements
- Merge and deploy to app-native locations

**Output**:
- `.claude/CLAUDE.md` — Claude Code context
- `.cursor/rules` — Cursor IDE context
- `.codex/CODEX.md` — OpenAI/Codex context
- `.gemini/GEMINI.md` — Google Gemini context
- `.github/copilot-instructions.md` — GitHub Copilot context
- All supporting skill files, rule files, knowledge files

**Subdirectories**:
- `01_entity_context/` — Input (0AGNOSTIC.md + .0agnostic/)
- `02_merge_system/` — .1merge rules (Tier 0+1+2)
- `03_ai_app_ports/` — Processed outputs for each app
- `.claude/`, `.codex/`, `.gemini/`, `.cursor/`, `.github/` — AI app–specific directories

---

<!-- section_id: "245233db-438f-4d87-b72b-7de9e6f80310" -->
## Data Structures

<!-- section_id: "81865087-2129-41b9-a088-5152b675bc33" -->
### Stage Report Format
```yaml
# stage_report.md

## Stage Definition
- Name, number, purpose
- Context requirements, inputs, outputs

## Key Deliverables
- List of 3-5 main artifacts produced

## Findings & Decisions
- What was learned
- Key architectural decisions made

## Connections
- Parent stage (what feeds into this)
- Child stages (what this feeds into)
- Cross-layer dependencies

## Propagation
- What should propagate to parent layer
- What should propagate to AI apps
- Override rules if any
```

<!-- section_id: "ebf25cb9-8804-4345-8715-225466799453" -->
### Layer Report Format
```yaml
# layer_report.md

## Layer Definition
- Name, scope, identity
- Parent and child layers

## Stage Synthesis
- How all 11 stages connect
- Key flows and dependencies
- Critical decisions per stage

## Entity Output
- What context should go to each child entity
- Customization rules
- Inheritance rules

## System Health
- Coverage metrics
- Consistency checks
- Missing pieces identified
```

<!-- section_id: "0dcb6ecf-2e36-4c8e-bd67-584eb5cb3665" -->
### Entity 0AGNOSTIC.md Structure
```yaml
# 0AGNOSTIC.md

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──
## Identity
## Key Behaviors
## Triggers

# ── Current Status ──
## Current Status

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──
## Current State Detail

# ── References ──
## Navigation
## Resources
## Success Criteria
## On Exit
```

---

<!-- section_id: "6d18df7f-9a49-4671-800d-502fdfecf886" -->
## Propagation Rules

<!-- section_id: "a1437107-6a1f-4bd1-8ee3-08549605eb62" -->
### Upward Propagation (Funnel Taper)
- Stage outputs → stage_report.md (summarize, synthesize)
- Stage reports → layer_report.md (aggregate, connect)
- Layer reports → entity reports (customize, inherit)
- Entity context → AI app ports (deploy, merge)

<!-- section_id: "ab1bed27-f5c2-4c10-abc9-776bfedf2ca8" -->
### Downward Propagation (Cascade)
- Layer rules cascade to child entities (all children inherit)
- Entity rules cascade to child features (all features inherit)
- Inherited rules can be overridden at any level (child can customize)

<!-- section_id: "29b62520-d7c4-4c97-8b49-e96166a9771b" -->
### Merge Precedence
When context from multiple sources:
- **Child rules** > **Parent rules** (more specific wins)
- **Tier 2 (additions)** > **Tier 1 (overrides)** > **Tier 0 (synced)** (later tiers override)
- **Entity-specific** > **Layer-inherited** > **Universal** (specificity hierarchy)

---

<!-- section_id: "2156ec70-0200-49ef-a257-520df2ad15c5" -->
## File Organization Pattern

Each level follows numbered subdirectories with specific purposes:

**Pattern**: `[NN_name]/[01_PURPOSE]/`

```
propagation_funnel/
├── 01_stage_outputs_to_stage_report/
│   ├── 01_outputs/           ← Raw stage outputs
│   ├── 02_output_reports/    ← Processed reports
│   ├── 03_0agnostic_system/  ← Context definitions
│   ├── 1merge_system/        ← Merge rules
│   ├── .claude/              ← Claude Code config
│   ├── .cursor/              ← Cursor IDE config
│   ├── .codex/               ← OpenAI config
│   ├── .gemini/              ← Gemini config
│   ├── .github/              ← GitHub config
│   ├── stage_report.md       ← Output
│   ├── 0AGNOSTIC.md          ← Output
│   ├── CLAUDE.md             ← Output
│   ├── AGENTS.md             ← Output
│   └── ... (other AI app files)
│
├── 02_stage_reports_to_layer_reports/
│   ├── 01_stage_reports/
│   ├── 02_aggregated_layer_report/
│   ├── 03_0agnostic_system/
│   ├── layer_report.md       ← Output
│   └── 0AGNOSTIC.md          ← Output
│
├── 03_layer_reports_to_entity_reports/
│   ├── 01_layer_reports/
│   ├── 02_aggregated_entity_reports/
│   ├── 03_entity_0agnostic/
│   └── 0AGNOSTIC.md          ← Output (entity version)
│
└── 04_entity_context_to_ai_apps/
    ├── 01_entity_context/
    ├── 02_merge_system/
    ├── 03_ai_app_ports/
    ├── .claude/
    ├── .cursor/
    ├── .codex/
    ├── .gemini/
    ├── .github/
    └── (all AI app context files)
```

---

<!-- section_id: "d850ffa2-bfd2-478c-860e-623ebca6095d" -->
## Integration with Existing Systems

<!-- section_id: "cb7db694-a67e-4a8d-9fcf-0afa5b52b765" -->
### Connection to Stage Outputs
- Stage 04 (Design) produces outputs → collected in `01_outputs/`
- Stage 05 (Planning) produces outputs → collected in `01_outputs/`
- Each stage's outputs aggregated → `02_output_reports/stage_NNN_report.md`

<!-- section_id: "93b064c7-9ed3-41d7-a349-2e428b19d906" -->
### Connection to 0AGNOSTIC.md
- `0AGNOSTIC.md` is source of truth at each level
- Propagation funnel processes `0AGNOSTIC.md`
- agnostic-sync.sh generates tool-specific files from `0AGNOSTIC.md`

<!-- section_id: "5d88e75f-3567-4786-8cc1-9f8d800b6362" -->
### Connection to .1merge
- .1merge system rules live in `02_merge_system/`
- Tier 0 (synced): Generated by agnostic-sync.sh
- Tier 1 (overrides): App-specific boilerplate in .1merge/
- Tier 2 (additions): Custom content in .1merge/

<!-- section_id: "f0b13661-056f-4e17-8542-f4b5f3af3b89" -->
### Connection to AI Apps
- Final outputs port to `.claude/`, `.cursor/`, etc.
- Each app loads from its native location
- All apps receive same underlying content, different formatting

---

<!-- section_id: "fac54385-aaae-4616-aa34-9f038da0786f" -->
## Execution Workflow

**Step 1: Collect Stage Outputs**
- Copy all stage outputs to `01_outputs/`
- Examples: research docs, design specs, planning roadmaps

**Step 2: Generate Stage Report**
- Analyze `01_outputs/`
- Create `stage_report.md` summarizing findings
- Create `0AGNOSTIC.md` defining stage identity
- Place in `02_output_reports/`

**Step 3: Aggregate with Other Stages**
- Collect all stage reports (stage_01 through stage_11)
- Synthesize into `layer_report.md`
- Place in `02_stage_reports_to_layer_reports/`

**Step 4: Customize for Entities**
- Take layer_report.md
- Customize for each child entity
- Create entity 0AGNOSTIC.md
- Place in `03_layer_reports_to_entity_reports/`

**Step 5: Port to AI Apps**
- Take entity context
- Run agnostic-sync.sh (generates Tier 0)
- Apply .1merge rules (Tier 1+2)
- Deploy to `.claude/`, `.cursor/`, etc.
- Place outputs in `04_entity_context_to_ai_apps/`

**Step 6: Verify Propagation**
- Check that all AI apps received context
- Verify triggers parse correctly
- Test skill invocations
- Confirm knowledge and rules accessible

---

<!-- section_id: "ccfd781f-fc45-4b11-ae5d-07e57c606e0d" -->
## Benefits of Propagation Funnel

1. **Transparency** — Clear path showing how context flows through system
2. **Traceability** — Easy to find where decisions came from
3. **Consistency** — Funnel ensures all entities follow same flow
4. **Flexibility** — Override rules at any level
5. **Scalability** — Add new entities without redesigning flow
6. **Auditability** — Every transformation documented
7. **Maintenance** — Changes propagate correctly when system followed

---

<!-- section_id: "e58e2cbe-24d3-4f02-9392-9aac2e1a2f2c" -->
## Status

**Implemented**: Directory structure created (01-04)
**Pending**: Documentation for each level (files to create)
**Next**: Create level-specific documentation and populate with actual content

**References**:
- Context Chain Architecture: `../../../stage_2_04_design/outputs/02_context_chain_architecture.md`
- Implementation Roadmap Phase 5: `../../../stage_2_05_planning/outputs/01_implementation_roadmap.md`
- agnostic-sync.sh: `0_layer_universal/.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh`
- .1merge System: `.0agnostic/03_protocols/.1merge_port_system_protocol.md` (to be created)
