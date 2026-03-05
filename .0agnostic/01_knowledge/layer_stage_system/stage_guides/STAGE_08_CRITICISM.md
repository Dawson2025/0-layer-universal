---
resource_id: "4ab47aca-7134-44e4-89d5-621f3853f2a3"
resource_type: "knowledge"
resource_name: "STAGE_08_CRITICISM"
---
# Stage 08: Criticism — Universal Guide

## Purpose

Review the work product with a critical eye — identify quality issues, gaps, alternatives, and improvements. This is the **quality review stage** — challenge what was built.

## What This Stage IS

The criticism agent:
- Reviews artifacts from stages 04-07 for quality, completeness, and correctness
- Identifies gaps between requirements (stage 01) and what was delivered
- Suggests improvements and alternative approaches
- Evaluates whether the design decisions (stage 04) were sound given results
- Produces a critique document with categorized findings

## What This Stage IS NOT

The criticism agent does NOT:
- **Gather new requirements** — that's stage 01 (but may recommend requirement revisions)
- **Research new approaches** — that's stage 02 (but may suggest areas for further research)
- **Fix issues** — that's stage 09 (criticism identifies, fixing resolves)
- **Build alternatives** — that's stage 06 (criticism evaluates, not implements)

The agent asks **"is this good enough?"** and **"what's wrong?"**, not **"how do I fix it?"**.

## Methodology

```
outputs/
├── critique.md                <- Primary critique document
├── gaps.md                    <- Requirements gap analysis
├── alternatives.md            <- Alternative approaches worth considering
└── stage_report.md
```

### Critique Document Format

The critique should cover:
- **Quality assessment**: Overall quality rating and justification
- **Strengths**: What works well (acknowledge good work)
- **Issues**: Problems found, categorized by severity:
  - **Critical**: Must fix before release (blocks progress)
  - **Major**: Should fix — significant quality concern
  - **Minor**: Nice to fix — small improvements
  - **Suggestion**: Optional enhancement ideas
- **Gaps**: Requirements not fully met
- **Risks**: Potential problems not yet realized

### Gap Analysis

Compare stage 01 requirements against delivered artifacts:
- Which requirements are fully met?
- Which are partially met?
- Which are unaddressed?
- Are there over-deliveries (built more than required)?

## Inputs

- **Stage 01 outputs** — requirements to verify coverage
- **Stage 04 outputs** — design specs to evaluate decisions
- **Stage 06 outputs** — built artifacts to review
- **Stage 07 outputs** — test results to assess quality
- **Parent entity .0agnostic/** — entity context

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Critique | `outputs/critique.md` | Categorized findings (critical/major/minor/suggestion) |
| Gap analysis | `outputs/gaps.md` | Requirements coverage matrix |
| Alternatives | `outputs/alternatives.md` | Alternative approaches worth considering |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All delivered artifacts have been reviewed
2. Issues are categorized by severity
3. Gap analysis against requirements is complete
4. Critique is actionable (issues can be addressed by stage 09)
5. Overall quality assessment is documented

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 09** (fixing): prioritize issues by severity
3. If handing off to **stage 01** (request_gathering): note requirement revisions needed
4. If handing off to **stage 02** (research): note areas needing further investigation

## Common Patterns

- **Loop: 07 → 08 → 09 → 07**: The most common loop — test, critique, fix, re-test
- **Fresh perspective**: Ideally, the criticism agent is NOT the same agent that built the artifact
- **Constructive critique**: Identify strengths alongside weaknesses
- **Severity-driven prioritization**: Critical issues block progress; suggestions are optional

## Anti-Patterns

- Criticizing without reading test results (stage 07) — don't re-discover known issues
- Suggesting fixes instead of just identifying problems (that's stage 09's job)
- Being only negative — acknowledge what works well
- Reviewing without referencing requirements — critique must be grounded
