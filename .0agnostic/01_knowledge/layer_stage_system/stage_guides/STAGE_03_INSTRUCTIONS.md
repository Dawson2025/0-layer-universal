---
resource_id: "0a1d3fa8-a96b-4fbf-b5fa-2b441f9ea549"
resource_type: "knowledge"
resource_name: "STAGE_03_INSTRUCTIONS"
---
# Stage 03: Instructions — Universal Guide

<!-- section_id: "7bc55118-d41b-4aec-b39b-2d13c0237d63" -->
## Purpose

Define constraints, guidelines, and non-negotiable rules that govern all subsequent stages. This is the **guardrails stage** — it sets boundaries that design, development, and testing must respect.

<!-- section_id: "970d363c-7602-49a3-bb40-d5aa81879891" -->
## What This Stage IS

The instructions agent:
- Documents constraints that cannot be violated (technical, organizational, legal, architectural)
- Defines guidelines that should be followed unless there's a justified reason not to
- Codifies conventions and standards for the entity's work
- Captures non-functional requirements (performance, security, compatibility)
- Records decisions that constrain future work ("we MUST use X", "we MUST NOT do Y")

<!-- section_id: "9f439cb2-11bc-45a3-a1d4-4a22e497cd3e" -->
## What This Stage IS NOT

The instructions agent does NOT:
- **Gather requirements** — that's stage 01 (request_gathering)
- **Research the problem space** — that's stage 02 (research)
- **Make architecture decisions** — that's stage 04 (design) — instructions set constraints, design works within them
- **Create implementation plans** — that's stage 05 (planning)
- **Build anything** — that's stage 06 (development)

The agent defines **what must be true**, not **how to make it true**.

<!-- section_id: "b528d1ec-5aab-4ff3-b887-29a02b6ba584" -->
## Methodology

Instructions are organized by type:

```
outputs/
├── constraints.md          <- Non-negotiable rules (MUST/MUST NOT)
├── guidelines.md           <- Recommended practices (SHOULD/SHOULD NOT)
├── conventions.md          <- Standards and naming conventions
├── non_functional.md       <- Performance, security, compatibility requirements
└── stage_report.md
```

<!-- section_id: "6730b77f-5202-4a19-9dfd-73aa0c3b9663" -->
### Constraint Format

Each constraint should specify:
- **Rule**: Clear statement of what must/must not be done
- **Rationale**: Why this constraint exists
- **Scope**: What stages/artifacts this applies to
- **Enforcement**: How to verify compliance (feeds into stage 07 testing)

<!-- section_id: "0af5cca6-ff7b-470d-a908-8e3253c953b1" -->
## Inputs

- **Stage 01 outputs** — requirements that imply constraints
- **Stage 02 outputs** — research findings that reveal technical constraints
- **Parent entity .0agnostic/02_rules/** — inherited rules from parent hierarchy
- **Organizational standards** — from layer_0 universal rules

<!-- section_id: "d36ff83a-a43a-44dc-a237-bba0e01d90d7" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Constraints | `outputs/constraints.md` | MUST/MUST NOT rules with rationale |
| Guidelines | `outputs/guidelines.md` | SHOULD/SHOULD NOT recommendations |
| Conventions | `outputs/conventions.md` | Naming, formatting, structural standards |
| Non-functional reqs | `outputs/non_functional.md` | Performance, security, compatibility |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

<!-- section_id: "0915c486-d6e2-4c98-b7c3-e9499c4d465c" -->
## Success Criteria

This stage is complete when:
1. All known constraints are documented with rationale
2. Guidelines are clearly separated from hard constraints
3. Constraints are enforceable (can be checked in stage 07)
4. No contradictions between constraints
5. Parent hierarchy rules are referenced (not duplicated)

<!-- section_id: "cc0f77c4-da72-4c8b-90ac-625250e014db" -->
## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 04** (design): highlight constraints that most affect architecture decisions
3. If handing off to **stage 06** (development): highlight coding standards and conventions

<!-- section_id: "e1be1532-f385-4886-8560-4a3ba4c51d7b" -->
## Common Patterns

- **Often lightweight**: Many entities inherit most constraints from parent hierarchy — only entity-specific constraints need documenting
- **Can be skipped initially**: If constraints are obvious or inherited, this stage may stay scaffolded until specific constraints emerge
- **Feeds testing**: Every constraint should have a corresponding test in stage 07
- **Living document**: Constraints may be added as work progresses and new boundaries are discovered

<!-- section_id: "29c24b86-abe8-41b5-ad48-8e31db5c25aa" -->
## Anti-Patterns

- Duplicating parent rules (reference them instead)
- Making constraints so strict they prevent good design
- Confusing constraints with design decisions (constraints set boundaries, design fills them)
- Leaving constraints unenforceable (if you can't test it, reconsider it)
