# Stage 01: Request Gathering — Universal Guide

## Purpose

Transform vague user needs into structured, testable requirements. This is the **intake stage** — everything starts here.

## What This Stage IS

The request gathering agent:
- Asks questions to clarify what the user actually needs
- Decomposes large needs into smaller, specific, testable needs
- Writes requirements in a standard format (requirements.md + user_stories.md)
- Organizes requirements as a **tree of needs** (hierarchical decomposition)
- Validates requirements with the user before handing off

## What This Stage IS NOT

The request gathering agent does NOT:
- **Research solutions** — that's stage 02 (research)
- **Define constraints or guidelines** — that's stage 03 (instructions)
- **Design architectures** — that's stage 04 (design) / stage 05 (planning)
- **Write code or build artifacts** — that's stage 06 (development)
- **Judge feasibility** — that's stage 08 (criticism)
- **Make implementation decisions** — those emerge from design, not requirements

The agent captures **what** is needed, not **how** to achieve it.

## Methodology: Tree of Needs

Requirements are organized as a hierarchical tree:

```
outputs/requests/tree_of_needs/
├── _meta/                        <- Versioning, changelog, dependencies
│   ├── VERSION.md
│   ├── CHANGELOG.md
│   └── DEPENDENCIES.md
└── 00_root_need/                 <- The fundamental goal
    ├── README.md                 <- Branch index with overview
    ├── 01_branch/                <- A major aspect of the goal
    │   ├── need_01/              <- A specific, testable need
    │   │   ├── requirements.md   <- Functional requirements + success criteria
    │   │   └── user_stories.md   <- "As a [role], I need [X] so that [Y]"
    │   └── need_02/
    └── 02_branch/
```

### Requirements.md Format

Each `requirements.md` contains:
- **Functional requirements**: What the system must do (numbered, testable)
- **Success criteria**: How to verify the requirement is met
- **Constraints**: Boundaries or limitations
- **Priority**: High / Medium / Low
- **Dependencies**: Other needs this depends on

### User Stories Format

Each `user_stories.md` contains stories in standard format:
```
As a [agent/manager/user/system], I need [specific capability] so that [benefit/outcome].
```

## Inputs

What the request gathering agent reads:
- **Parent entity 0AGNOSTIC.md** — to understand what this entity IS and its domain
- **Parent entity .0agnostic/01_knowledge/** — for domain understanding (read selectively, not all at once)
- **User conversations** — primary source of requirements
- **Existing tree of needs** (if resuming) — `outputs/requests/tree_of_needs/`
- **Prior stage reports** — none (this is the first stage), but may re-enter after stage 08 (criticism) loops back

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Tree of needs | `outputs/requests/tree_of_needs/` | Directory tree with requirements.md + user_stories.md per leaf need |
| Root need | `outputs/requests/tree_of_needs/00_{root_name}/` | README.md with branch overview |
| Meta | `outputs/requests/tree_of_needs/_meta/` | VERSION.md, CHANGELOG.md, DEPENDENCIES.md |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All identified needs have `requirements.md` and `user_stories.md`
2. Requirements are testable (can be validated in stage 07)
3. User has validated the tree of needs (explicit sign-off)
4. Priority ordering exists across needs
5. No unresolved ambiguities in requirements
6. Dependencies between needs are documented

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 02** (research): note which needs require investigation of the problem space
3. If handing off to **stage 04** (design): note which needs are well-understood and ready for architecture decisions
4. If returning from **stage 08** (criticism): note which requirements need revision based on critique feedback

## Common Patterns

- **Parallel with stage 02**: Requirements gathering and research often run in parallel — research reveals new needs, requirements clarify research scope
- **Loop from stage 08**: After criticism, new or revised requirements may be needed — the agent re-enters to update the tree
- **Incremental growth**: The tree of needs grows over time — don't try to capture everything in one pass
- **User validation is mandatory**: Never hand off to later stages without user confirmation that requirements are correct

## Anti-Patterns

- Designing solutions while gathering requirements (scope creep into stage 04/05)
- Writing overly detailed requirements that constrain implementation unnecessarily
- Skipping user validation — requirements must be confirmed
- Loading all parent knowledge at once instead of reading selectively
- Treating requirements as final — they evolve as understanding deepens
