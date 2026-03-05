---
resource_id: "d71e9999-022f-43d3-916c-c06d2667d9b5"
resource_type: "knowledge"
resource_name: "STAGE_06_DEVELOPMENT"
---
# Stage 06: Development — Universal Guide

<!-- section_id: "0cd17072-a14a-44e3-b4aa-5a014526d29a" -->
## Purpose

Build the artifacts specified in the implementation plan. This is the **build stage** — execute the plan, create the deliverables.

<!-- section_id: "9f023b4e-2901-4f5f-98e4-f23d8a568fb5" -->
## What This Stage IS

The development agent:
- Reads the implementation plan (from stage 05) and executes tasks in order
- Creates code, scripts, configuration files, directory structures, documentation
- Follows constraints from stage 03 and design from stage 04
- Produces working artifacts that can be validated in stage 07
- Maintains a development status document tracking what's done vs remaining

<!-- section_id: "24cb0149-c18c-40ed-8116-e3244af14dbf" -->
## What This Stage IS NOT

The development agent does NOT:
- **Gather requirements** — that's stage 01
- **Research alternatives** — that's stage 02
- **Make architecture decisions** — that's stage 04 (follow the design, don't redesign)
- **Break work into tasks** — that's stage 05 (follow the plan)
- **Validate correctness** — that's stage 07 (testing) — but basic smoke checks during development are fine
- **Critique quality** — that's stage 08 (criticism)

The agent **builds what was planned**, not **decides what to build**.

<!-- section_id: "b62abbda-23b1-4206-b340-e2ec61d1de70" -->
## Methodology

```
outputs/
├── by_topic/
│   ├── README.md                             <- Development index
│   ├── 01_development_runbook.md             <- Step-by-step execution guide
│   └── 02_development_status.md              <- Progress tracking
├── stage_report.md
└── [actual artifacts may live in the entity itself, not in outputs/]
```

<!-- section_id: "558a2bd8-9d40-4c95-ac4c-55d1ed77d66c" -->
### Development Tracking

The development status document tracks:
- **Completed tasks**: What's been built (with links to artifacts)
- **In-progress tasks**: What's currently being worked on
- **Remaining tasks**: What's left to build
- **Deviations**: Any changes from the plan (with rationale)
- **Blockers**: Issues preventing progress

<!-- section_id: "6068c77b-14f4-48de-a9bc-7bc03a9d819b" -->
### Artifact Locations

Development artifacts typically live in the **entity itself**, not in `outputs/`:
- `.0agnostic/` structure (knowledge, rules, protocols, skills)
- Scripts in `.0agnostic/06_hooks/scripts/`
- Entity-specific files in their canonical locations

The `outputs/` directory holds the **development documentation** (runbook, status), not the artifacts themselves.

<!-- section_id: "2e21edbd-5590-428e-9376-3d6cd68da236" -->
## Inputs

- **Stage 05 outputs** — implementation plan with ordered tasks
- **Stage 04 outputs** — design specs defining what to build
- **Stage 03 outputs** — constraints to follow during building
- **Parent entity .0agnostic/** — existing structure to build upon

<!-- section_id: "a34dc47f-a093-461f-a406-5d1a00f4f8e5" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Development runbook | `outputs/by_topic/01_development_runbook.md` | Step-by-step execution guide |
| Development status | `outputs/by_topic/02_development_status.md` | Progress tracker |
| Built artifacts | Entity itself (`.0agnostic/`, scripts, etc.) | Whatever the plan specifies |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

<!-- section_id: "375ece5c-7e4b-4ccd-a4ea-a32dffc050cc" -->
## Success Criteria

This stage is complete when:
1. All planned tasks are executed (or explicitly deferred with rationale)
2. Built artifacts match the design specifications
3. Constraints from stage 03 are respected
4. Development status document reflects final state
5. Artifacts are ready for stage 07 (testing) validation

<!-- section_id: "c7135014-349a-4853-bb58-bc449a4e23d5" -->
## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 07** (testing): list what to test and where artifacts live
3. If handing off to **stage 04** (design): note design issues discovered during implementation
4. If handing off to **stage 05** (planning): note tasks that need replanning

<!-- section_id: "35aa7304-6c35-4d72-9aa2-196d1b18d82c" -->
## Common Patterns

- **Runbook-driven**: Follow the runbook step by step — deviations should be documented
- **Incremental builds**: Build and verify incrementally, not all at once
- **Status tracking**: Update the status document as tasks complete
- **Minimal design changes**: If the design needs changing, flag it — don't silently redesign during development

<!-- section_id: "b4ba170c-6485-4bd5-9aab-0b1bffb9aaed" -->
## Anti-Patterns

- Building without reading the plan (stage 05) first
- Redesigning architecture during development without going back to stage 04
- Not tracking what was built vs what was planned (makes testing harder)
- Building artifacts that don't match the design specification
- Over-testing during development (save thorough testing for stage 07)
