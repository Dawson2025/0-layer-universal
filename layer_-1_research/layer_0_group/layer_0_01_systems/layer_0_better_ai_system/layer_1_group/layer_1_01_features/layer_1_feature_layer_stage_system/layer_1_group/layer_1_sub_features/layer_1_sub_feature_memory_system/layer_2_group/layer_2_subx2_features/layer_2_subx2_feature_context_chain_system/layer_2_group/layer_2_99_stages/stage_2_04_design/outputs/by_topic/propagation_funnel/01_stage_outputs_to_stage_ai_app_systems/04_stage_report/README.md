---
resource_id: "e7527309-fbba-47da-b6ad-69ee0841383a"
resource_type: "readme_output"
resource_name: "README"
---
# Stage 01: Stage Report Generation

<!-- section_id: "f0e32069-aa22-4d47-b051-139918fbbf30" -->
## Purpose

**Stage Report** is the canonical handoff document that summarizes ALL outputs from a stage and prepares them for synthesis into the next level.

A stage report:
- **Aggregates** all stage outputs (scripts, findings, artifacts)
- **Synthesizes** findings into coherent narrative
- **Documents** decisions made, trade-offs, and open items
- **Provides** input to the next propagation level (synthesis into parent context)

<!-- section_id: "26e37fd1-68e1-440a-86c5-0c946fb93cee" -->
## When to Create

Create a stage report **at the end of each stage** (stages 01-11 in the layer-stage system):

- Stage 01 (Request Gathering) → stage report documenting all needs collected
- Stage 02 (Research) → stage report documenting all findings
- Stage 04 (Design) → stage report documenting all architecture decisions
- ... and so on through Stage 11

<!-- section_id: "020620e8-9b4d-4e87-8762-ada8fba7ee92" -->
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

<!-- section_id: "4d4096d6-3a03-4c1d-933d-69ee7333b008" -->
## Stage Report Structure

A canonical stage report contains:

<!-- section_id: "5e9fbeee-83c9-4fd0-8f32-d08579343d15" -->
### 1. Executive Summary (1-2 paragraphs)
- What this stage accomplished
- Key findings or decisions
- Status: Ready / Needs Rework / Blocked

<!-- section_id: "2c3e1b82-1dc0-4ae1-9078-b284b179e0ba" -->
### 2. Inputs (What came in)
- Requirements from previous stage
- Parent entity context
- Handoff documents from earlier stages

<!-- section_id: "6b1f8d76-4eae-47c1-95e2-e40a0e186e70" -->
### 3. Outputs (What was delivered)
- List of all artifacts (files, decisions, findings)
- Where outputs are located
- Format: file path, line count, purpose

<!-- section_id: "5b8bda21-e77f-4cc5-bec6-6c10113d2384" -->
### 4. Key Findings / Decisions
- Top 3-5 most important findings
- Architecture decisions made (with trade-offs)
- Problems encountered and solutions

<!-- section_id: "8bc82249-1a41-4338-8cbf-1776e499e937" -->
### 5. Open Items
- Unresolved questions
- Blocked work (and why)
- Items for next stage

<!-- section_id: "afa1d239-1236-4ee2-be93-bb547850c15e" -->
### 6. Methodology
- How was this stage approached?
- Tools used
- Process followed (agile, waterfall, research, etc.)

<!-- section_id: "55c74008-fcac-4c4a-89a0-8aa0839e8972" -->
### 7. Success Metrics
- How do we know this stage succeeded?
- Completion criteria
- Validation performed

<!-- section_id: "eaf79593-72a7-4aa7-8197-c624e19fbe00" -->
### 8. Handoff Readiness
- ✅ All outputs documented
- ✅ Decisions recorded in 0AGNOSTIC.md / 0INDEX.md
- ✅ Artifacts committed to git
- ✅ No blocking issues for next stage
- Status: Ready / Almost Ready / Needs Work

<!-- section_id: "6fe58a22-c158-4ae5-88ee-e5ae25b31329" -->
### 9. References
- Links to key output files
- Parent/child stage reports
- Related documentation

<!-- section_id: "2cbebc98-c216-4f3d-ac5e-b72268a94431" -->
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

<!-- section_id: "6df7213d-db92-4226-ae24-003792acc131" -->
## File Format

**Markdown** — Keep stage reports in markdown for:
- Version control (git-friendly)
- Easy reading in terminal / GitHub
- Inclusion in documentation sites
- Linking to other documents

<!-- section_id: "43b1f1db-5285-4f13-b060-48dfbb771b0e" -->
## Phase in Propagation Funnel

Stage reports are the **bridge** between:
- **Upstream**: Stage outputs (code, findings, decisions, artifacts)
- **Downstream**: Synthesis into parent context (layer reports, entity context, AI app prompts)

Without stage reports, outputs remain disconnected. Stage reports are the **glue** that makes hierarchical knowledge flow possible.

<!-- section_id: "e747c48e-0440-4334-b95f-005e290b2c65" -->
## See Also

- `.0agnostic/03_protocols/stage_report_protocol.md` — Complete protocol for creating stage reports
- Stage 07 (Testing) → tests stage reports for completeness
- Stage 08 (Criticism) → critiques stage reports for clarity and accuracy
- Level 02 (Layer Reports) → synthesizes all stage reports into unified layer summary
