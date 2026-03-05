---
resource_id: "345d0c7d-010f-49b9-b0a8-dc1eca138ce4"
resource_type: "knowledge"
resource_name: "STAGE_05_PLANNING"
---
# Stage 05: Planning — Universal Guide

## Purpose

Break design specifications into ordered, actionable implementation tasks. This is the **task breakdown stage** — transform architecture into a step-by-step execution plan.

## What This Stage IS

The planning agent:
- Reads design specs (from stage 04) and breaks them into discrete tasks
- Orders tasks by dependencies (what must be done before what)
- Identifies an MVP or phased approach when the full scope is large
- Estimates scope and complexity per task (not time — avoid time estimates)
- Documents the implementation sequence clearly enough that stage 06 can execute

## What This Stage IS NOT

The planning agent does NOT:
- **Gather requirements** — that's stage 01
- **Research** — that's stage 02
- **Make architecture decisions** — that's stage 04 (planning works within the design)
- **Write code or build artifacts** — that's stage 06
- **Test anything** — that's stage 07

The agent creates **the execution roadmap**, not **the artifacts themselves**.

## Methodology

```
outputs/
├── by_topic/
│   ├── README.md                         <- Plan index
│   └── 01_implementation_plan.md         <- Primary plan with task breakdown
└── stage_report.md
```

### Implementation Plan Format

Each plan should contain:
- **Scope**: What this plan covers (links to design specs)
- **Approach**: MVP-first, phased, or full implementation
- **Task breakdown**: Numbered tasks with:
  - Task description (what to build/do)
  - Dependencies (what must be completed first)
  - Inputs (what files/specs to read)
  - Expected outputs (what gets created)
  - Complexity: Low / Medium / High
- **Phase structure** (if phased): Which tasks form each phase
- **Verification plan**: How to verify each phase works (feeds into stage 07)

## Inputs

- **Stage 04 outputs** — design specs to break into tasks
- **Stage 03 outputs** — constraints affecting task ordering
- **Stage 01 outputs** — requirements for priority ordering
- **Parent entity 0AGNOSTIC.md** — context for scope decisions

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Implementation plan(s) | `outputs/by_topic/` | Task breakdowns with ordering |
| Plan index | `outputs/by_topic/README.md` | Overview linking all plans |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All design components have corresponding implementation tasks
2. Task dependencies are clearly documented
3. MVP or first phase is identified (if applicable)
4. Tasks are specific enough for stage 06 to execute without ambiguity
5. Verification approach is outlined for each phase

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 06** (development): specify which tasks to start with and their inputs
3. If handing off to **stage 04** (design): note gaps where design needs more detail before tasks can be defined

## Common Patterns

- **MVP-first**: For large scopes, identify the minimum viable implementation first
- **Dependency chains**: Tasks form a DAG — identify the critical path
- **Phase gates**: Define what "done" looks like for each phase before moving to the next
- **Parallel work**: Identify tasks that can be done independently in parallel

## Anti-Patterns

- Creating tasks that are too vague ("implement the system")
- Over-planning with tasks that are too granular for the current stage
- Planning without reading design specs (stage 04)
- Including time estimates (focus on scope and ordering, not duration)
