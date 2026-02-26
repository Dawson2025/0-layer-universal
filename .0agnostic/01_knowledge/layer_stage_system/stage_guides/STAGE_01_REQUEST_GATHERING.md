# Stage 01: Request Gathering — Universal Guide

## Purpose

Transform vague user needs into structured, testable requirements. This is the **intake stage** — everything starts here.

## What This Stage IS

The request gathering agent:
- Asks questions to clarify what the user actually needs
- Decomposes large needs into smaller, specific, testable needs
- Writes requirements in a standard format (requirements/ and user_stories/ subdirectories per need)
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
├── _meta/                            <- Versioning, changelog, dependencies
│   ├── VERSION.md
│   ├── CHANGELOG.md
│   └── DEPENDENCIES.md
└── 00_root_need/                     <- The fundamental goal
    ├── README.md                     <- Branch index with overview
    ├── 01_branch/                    <- A major aspect of the goal
    │   ├── README.md                 <- Branch overview with needs index
    │   ├── need_01/                  <- A specific, testable need
    │   │   ├── README.md             <- Need overview: definition, why, acceptance criteria, references
    │   │   ├── requirements/         <- Individual requirement files
    │   │   │   ├── README.md         <- Index table of all requirements
    │   │   │   ├── REQ-01_name.md    <- One file per requirement group (MUST/SHOULD statements)
    │   │   │   └── REQ-02_name.md
    │   │   └── user_stories/         <- Individual user story files
    │   │       ├── README.md         <- Index table + actors section
    │   │       ├── US-01_name.md     <- One file per user story
    │   │       └── US-02_name.md
    │   └── need_02/
    └── 02_branch/
```

### Need README.md Format

Each need's `README.md` contains the overview:
- **Definition**: What this need is about
- **Why This Matters**: Impact and motivation
- **Acceptance Criteria**: How to verify the need is met
- **Research References**: Links to related research
- Links to `requirements/` and `user_stories/` subdirectories

### Requirements Format

Each `requirements/REQ-NN_name.md` contains:
- **Functional requirements**: MUST/SHOULD/MUST NOT statements for one requirement group
- **Back-reference**: Link to the parent need README.md

The `requirements/README.md` provides an index table of all requirements in the need.

### User Stories Format

Each `user_stories/US-NN_name.md` contains one story in standard format:
```
As a [agent/manager/user/system], I need [specific capability] so that [benefit/outcome].
```
Plus an acceptance line and back-reference to the need README.md.

The `user_stories/README.md` provides an index table and the actors section.

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
| Tree of needs | `outputs/requests/tree_of_needs/` | Directory tree with requirements/ + user_stories/ subdirs per leaf need |
| Root need | `outputs/requests/tree_of_needs/00_{root_name}/` | README.md with branch overview |
| Meta | `outputs/requests/tree_of_needs/_meta/` | VERSION.md, CHANGELOG.md, DEPENDENCIES.md |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All identified needs have `requirements/` and `user_stories/` subdirectories with individual files
2. Requirements are testable (can be validated in stage 07)
3. User has validated the tree of needs (explicit sign-off)
4. Priority ordering exists across needs
5. No unresolved ambiguities in requirements
6. Dependencies between needs are documented

## Exit Protocol

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
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
