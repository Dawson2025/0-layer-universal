# Stage 01: Stage Report Generation

## Purpose

**Stage Report** is the canonical handoff document that summarizes ALL outputs from a stage and prepares them for synthesis into the next level.

A stage report:
- **Aggregates** all stage outputs (scripts, findings, artifacts)
- **Synthesizes** findings into coherent narrative
- **Documents** decisions made, trade-offs, and open items
- **Provides** input to the next propagation level (synthesis into parent context)

## When to Create

Create a stage report **at the end of each stage** (stages 01-11 in the layer-stage system):

- Stage 01 (Request Gathering) → stage report documenting all needs collected
- Stage 02 (Research) → stage report documenting all findings
- Stage 04 (Design) → stage report documenting all architecture decisions
- ... and so on through Stage 11

## Location Convention

**At each level** (01-04 in propagation funnel):

```
{level}/04_stage_report/
├── stage_report.md (main document)
└── stage_report_examples.md (optional: patterns, templates)
```

**In the layer-stage system** (actual stage output):

```
stage_2_NN_name/
├── outputs/
│   └── stage_report.md (actual stage report file)
└── .0agnostic/05_handoff_documents/02_outgoing/01_to_above/
    └── stage_report.md (copy for handoff)
```

## Stage Report Structure

A canonical stage report contains:

### 1. Executive Summary (1-2 paragraphs)
- What this stage accomplished
- Key findings or decisions
- Status: Ready / Needs Rework / Blocked

### 2. Inputs (What came in)
- Requirements from previous stage
- Parent entity context
- Handoff documents from earlier stages

### 3. Outputs (What was delivered)
- List of all artifacts (files, decisions, findings)
- Where outputs are located
- Format: file path, line count, purpose

### 4. Key Findings / Decisions
- Top 3-5 most important findings
- Architecture decisions made (with trade-offs)
- Problems encountered and solutions

### 5. Open Items
- Unresolved questions
- Blocked work (and why)
- Items for next stage

### 6. Methodology
- How was this stage approached?
- Tools used
- Process followed (agile, waterfall, research, etc.)

### 7. Success Metrics
- How do we know this stage succeeded?
- Completion criteria
- Validation performed

### 8. Handoff Readiness
- ✅ All outputs documented
- ✅ Decisions recorded in 0AGNOSTIC.md / 0INDEX.md
- ✅ Artifacts committed to git
- ✅ No blocking issues for next stage
- Status: Ready / Almost Ready / Needs Work

### 9. References
- Links to key output files
- Parent/child stage reports
- Related documentation

## Example: CSE 300 Grade Strategy (Level 1)

**Stage**: Design the universal grade strategy system

**Executive Summary**:
Designed a cascading .0agnostic system at layer_2 that any class can inherit. Key innovation: trajectory stores (procedural memory) capture 5 step-by-step workflows. Triggers defined to determine when to load trajectories. Shared skills (canvas-fetch, grade-calculator) parameterized for reuse. Knowledge base created with grading model types, Canvas patterns, templates.

**Inputs**:
- User requirement: Build reusable grade dashboard for ANY class
- Research findings: Trajectory stores are procedural memory (from ProcMEM, AgentWorkforce, Trajectory Miner)
- Constraints: Must support specs-based (MATH 119) and percentage-based (CSE 300) grading

**Outputs**:
- 5 trajectory stores (canvas_grade_dashboard_trajectory.md, grading_model_analysis_trajectory.md, etc.) - 400 lines total
- Triggers/rules (grade_strategy_triggers.md) - 80 lines
- 2 shared skills (canvas-fetch, grade-calculator SKILL.md) - 120 lines
- Knowledge base (grading_model_types.md, canvas_tools_reference.md, templates) - 300 lines total

**Key Decisions**:
- Trajectory stores in `.0agnostic/03_protocols/` (procedural memory, not knowledge)
- Shared skills at layer_2, class-specific skills at layer_4 (DRY vs usability)
- Triggers cascade automatically (no duplication at each class)

**Handoff Readiness**: ✅ Ready
- All 5 trajectories created and documented
- Triggers defined and tested
- Shared skills created
- Validated on MATH 119 (specs-based)
- Ready for CSE 300 (percentage-based)

## File Format

**Markdown** — Keep stage reports in markdown for:
- Version control (git-friendly)
- Easy reading in terminal / GitHub
- Inclusion in documentation sites
- Linking to other documents

## Phase in Propagation Funnel

Stage reports are the **bridge** between:
- **Upstream**: Stage outputs (code, findings, decisions, artifacts)
- **Downstream**: Synthesis into parent context (layer reports, entity context, AI app prompts)

Without stage reports, outputs remain disconnected. Stage reports are the **glue** that makes hierarchical knowledge flow possible.

## See Also

- `.0agnostic/03_protocols/stage_report_protocol.md` — Complete protocol for creating stage reports
- Stage 07 (Testing) → tests stage reports for completeness
- Stage 08 (Criticism) → critiques stage reports for clarity and accuracy
- Level 02 (Layer Reports) → synthesizes all stage reports into unified layer summary
