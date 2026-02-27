# Research Index: Layer Consolidation, Context Chain & Grade Strategy

**Session**: 2026-02-27
**Research Layer**: `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_tool_and_app_agnostic/layer_1_group/layer_1_99_stages/`

---

## Stage 04: Design Documents

Located in: `stage_1_04_design/outputs/`

### 1. Layer Consolidation Design
**File**: `01_layer_consolidation_design.md`
**Purpose**: Documents the pattern, pitfalls, and solutions for consolidating fragmented directory structures

**Key Sections**:
- Problem pattern (duplicate directories, old architecture remnants)
- Root cause (historical migration wasn't completed uniformly)
- 6-step consolidation workflow (verify → copy → rename → flatten → verify → cleanup)
- Common pitfalls and prevention (mv behavior, deleting before copying, not updating .gitmodules)
- Validation checklist (8 items to verify after consolidation)
- Session notes from layer_3 and layer_4 consolidations
- Key learnings about naming conventions and git submodule tracking

**Applicable To**: Any layer consolidation, future entity standardization, git submodule maintenance

---

### 2. Context Chain Architecture
**File**: `02_context_chain_architecture.md`
**Purpose**: Clarifies the distinction between AI Apps (context recipients) and MCP Server Tools (function responders)

**Key Sections**:
- Terminology clarification (AI Apps: Claude Code, Cursor, Copilot, Gemini, Codex vs MCP Tools: Canvas, Perplexity, etc.)
- Three-layer context delivery model
  - Layer 0: 0AGNOSTIC.md (source of truth)
  - Layer 1: agnostic-sync.sh output (CLAUDE.md, .cursorrules, GEMINI.md, etc.)
  - Layer 2: .1merge port system (deploys to .claude/, .cursor/, .codex/, .gemini/, .github/)
- .1merge Three-tier merge strategy (Tier 0: synced, Tier 1: overrides, Tier 2: additions)
- Context avenue web (13 avenues: 8 file-based + 5 data-based)
- Current implementation status (Layer 0&1 done, Layer 2 designed but not built)
- Data flow diagram (request → context load → trigger evaluation → skill execution → MCP call → response)

**Critical Distinction**: AI Apps RECEIVE context (CLAUDE.md, .cursorrules, etc.); MCP Tools DO NOT receive context, they respond to function calls

**Applicable To**: Context design, AI app integration, understanding how agents load context, designing .1merge port system

---

### 3. Trajectory Stores & Grade Strategy
**File**: `03_trajectory_stores_and_grade_strategy.md`
**Purpose**: Documents trajectory store concept (procedural memory) and its application to grade strategy system

**Key Sections**:
- Trajectory store definition (procedural memory capturing steps, successes, failures, preconditions, metrics, reasoning)
- Difference from SOPs/runbooks (focuses on reasoning, not just procedures)
- Research validation (ProcMEM, AgentWorkforce, Trajectory Miner academic papers)
- Cascading grade strategy system architecture (layer_2 universal → layer_3/4 classes inherit)
- Five trajectory stores implemented:
  1. canvas_grade_dashboard_trajectory.md (7-step workflow)
  2. grading_model_analysis_trajectory.md (detect specs/percentage/weighted/hybrid)
  3. assignment_classification_trajectory.md (name patterns, Canvas types)
  4. deadline_tracking_trajectory.md (urgency flags, lock dates)
  5. strategy_generation_trajectory.md (priority formulas)
- Integration with class-specific skills (/calc-dashboard, /cse300-dashboard)
- Trigger conditions (when to load which trajectories)
- Validated implementations:
  - MATH 119 (specs-based, 30-pt rubric, 83 assignments) ✅
  - CSE 300 (percentage-based, 1,082 pts, 30 assignments) ✅

**Applicable To**: Procedural knowledge capture, grade strategy for new classes, understanding trajectory-based skill design

---

## Stage 05: Planning Documents

Located in: `stage_1_05_planning/outputs/`

### 1. Implementation Roadmap
**File**: `01_implementation_roadmap.md`
**Purpose**: End-to-end roadmap from research findings through production promotion

**Key Sections**:
- Phase 1: Layer Consolidation (COMPLETED)
  - Objectives, scope (13 entities), deliverables, timeline, validation results, learnings

- Phase 2: Context Chain Architecture (COMPLETED design, Layer 2 implementation pending)
  - Objectives, scope (5 AI apps + MCP tools), key distinctions
  - Current status: Layer 0&1 implemented, Layer 2 (.1merge) designed but not built
  - Roadmap for .1merge implementation (Phases 2A-2E)

- Phase 3: Grade Strategy System (COMPLETED)
  - Trajectory stores (5 documents), implementations (MATH 119 + CSE 300)
  - All 6 course projects standardized
  - Validation results

- Phase 4: Documentation (CURRENT)
  - Design documents being written (this index included)

- Phase 5: Promotion to Production (PLANNED)
  - Archive to layer_0, create canonical protocols, establish best practices
  - Estimated 13 hours of work, break into 2-3 sessions
  - Success criteria, rollback procedures, risk mitigation

**Applicable To**: Project planning, understanding overall system status, identifying next work priorities, onboarding new contributors

---

## How These Documents Integrate

```
Design Phase (04)
├── Layer Consolidation Design ─── How to fix fragmented structures
├── Context Chain Architecture ─── How context flows to AI apps
└── Trajectory Stores & Grade Strategy ─── How to capture procedural knowledge

Planning Phase (05)
└── Implementation Roadmap ─── End-to-end execution (Phases 1-5)
    ├── Phase 1: Layer Consolidation (DONE) ──→ Use consolidation design
    ├── Phase 2: Context Chain (In Progress) ──→ Use context chain architecture
    ├── Phase 3: Grade Strategy (DONE) ──→ Use trajectory stores documentation
    ├── Phase 4: Documentation (NOW) ──→ These 4 research documents
    └── Phase 5: Promotion (PLANNED) ──→ Archive to layer_0 + implement .1merge
```

---

## Key Findings Summary

### 1. Naming Convention Matters
Inconsistent `layer_N/` vs `layer_N_group/` created confusion about canonical location. Consolidated to unified `layer_N_group/` naming across all 13 entities.

### 2. AI Apps ≠ MCP Server Tools
Critical terminology: AI Apps (Claude Code, Cursor, etc.) RECEIVE context; MCP Server Tools (Canvas, Perplexity, etc.) DON'T receive context, they respond to calls. These are fundamentally different roles.

### 3. Three-Layer Context Delivery
Source of truth (0AGNOSTIC.md) → Universal files (CLAUDE.md, .cursorrules) → AI app native directories (.claude/, .cursor/). The .1merge port system (Tier 0+1+2 merge) bridges Layer 1 → Layer 2.

### 4. Trajectory Stores Enable Reuse
By capturing procedural knowledge once at layer_2, all layer_3/4 classes can inherit without duplication. Grade strategy: write once (7-step workflow), use everywhere (MATH 119 + CSE 300 + future classes).

### 5. Two Grading Models Require Different Formulas
- **Specs-based** (MATH 119): Threshold crossing matters — completing 1 more item can jump multiple point tiers
- **Percentage-based** (CSE 300): Linear accumulation — each point earned is 1/1082 of grade
- Both models validated, both formulas work, system is generic enough to support more models

---

## What This Enables

**For Users**:
- Grade dashboards that automatically compute current percentage, letter grade, and recommended next actions
- Automatic urgency flagging for approaching deadlines
- Priority scoring based on grading model type and threshold crossing potential
- Consistent experience across all classes

**For Developers**:
- Reusable trajectory stores for building similar systems
- Clear terminology (AI Apps vs MCP Tools) for designing integrations
- Context chain pattern (Layer 0→1→2) for deploying universal context to any AI app
- Consolidation protocol for fixing directory structure issues

**For Future Sessions**:
- Layer_0 promotion creates canonical patterns for all future work
- .1merge implementation enables context deployment to all 5 AI apps simultaneously
- New class dashboard setup: 3 files (grading_model, categories, schedule) + 1 skill (inherit from template)
- Documentation ensures knowledge survives across multiple sessions and contributors

---

## Status of Each Phase

| Phase | Task | Status | Evidence |
|-------|------|--------|----------|
| 1 | Layer Consolidation | ✅ DONE | All 13 entities have layer_N_group naming, 0AGNOSTIC.md, .0agnostic/ |
| 2 | Context Chain Design | ✅ DONE | Architecture document complete, Layer 2 system designed |
| 2 | Context Chain Layer 0&1 | ✅ DONE | 0AGNOSTIC.md in all entities, agnostic-sync.sh generating CLAUDE.md etc. |
| 2 | Context Chain Layer 2 | 🔄 DESIGNED | .1merge three-tier merge designed, not yet built |
| 3 | Trajectory Stores | ✅ DONE | 5 trajectories implemented in layer_2 .0agnostic/03_protocols/ |
| 3 | Grade Strategy Systems | ✅ DONE | MATH 119 + CSE 300 working, all 6 projects using same pattern |
| 4 | Design Documentation | ✅ DONE | 3 comprehensive design docs + 1 roadmap in research layer |
| 5 | Promotion to Production | ⏳ PLANNED | Scheduled after Phase 4 research complete |

---

## Reading Guide

**For Understanding Context Chain**:
1. Start: `02_context_chain_architecture.md` (terminology + three-layer model)
2. Reference: Diagram in section "Context Chain Data Flow"
3. Next Steps: Phase 2C-2E in roadmap for .1merge implementation

**For Implementing Grade Dashboards for New Classes**:
1. Start: `03_trajectory_stores_and_grade_strategy.md` (workflow overview)
2. Reference: Templates in layer_2 `.0agnostic/01_knowledge/canvas_integration/resources/templates/`
3. Example: CSE 300 project structure for pattern
4. Reference: `.0agnostic/02_rules/dynamic/grade_strategy_triggers/` for when to invoke

**For Fixing Directory Structure Issues**:
1. Start: `01_layer_consolidation_design.md` (problem pattern + 6-step workflow)
2. Use: Validation checklist to ensure consolidation worked
3. Reference: Layer consolidation protocol in `.0agnostic/03_protocols/` (production version)

**For Understanding Overall Status**:
1. Start: `01_implementation_roadmap.md` (Phases 1-5 overview)
2. Check: "Status of Each Phase" table in this index
3. Identify: Pending work in Phase 5 (promotion to production)

---

## References to Production Implementations

These research findings are already partially implemented in production:

- ✅ **Layer Consolidation Protocol**: `.0agnostic/03_protocols/layer_consolidation_and_naming_protocol.md`
- ✅ **Trajectory Stores**: `.0agnostic/03_protocols/grade_strategy_system/` (5 trajectories)
- ✅ **Grade Strategy Triggers**: `.0agnostic/02_rules/dynamic/grade_strategy_triggers/`
- ✅ **Grade Dashboards**: MATH 119 `/calc-dashboard` skill + CSE 300 `/cse300-dashboard` skill
- ✅ **Class Grading Models**: Each class has `.0agnostic/01_knowledge/course_info/grading_model.md`
- 🔄 **Context Chain Architecture**: Documented in this research, Layer 0&1 implemented, Layer 2 (.1merge) pending
- 🔄 **.1merge Port System**: Designed but not yet implemented (Phase 2C in roadmap)

---

## Next Steps (From Roadmap Phase 5)

1. **Archive research docs to layer_0** — Move validated approaches to canonical location
2. **Create trajectory store template** — Pattern for future procedural memory captures
3. **Implement .1merge port system** — Deploy universal context to all 5 AI apps
4. **Create validation rules** — Prevent regression (missing 0AGNOSTIC.md, etc.)
5. **Update layer_0 CLAUDE.md** — Reference new protocols and patterns
6. **Test all systems end-to-end** — Verify complete context chain works

**Estimated Effort**: 13 hours | **Recommended**: Break into 2-3 sessions

---

**Last Updated**: 2026-02-27
**Session**: Grade Strategy System + Layer Consolidation + Context Chain Architecture Research
**Contributors**: Claude Code AI (session-based)
