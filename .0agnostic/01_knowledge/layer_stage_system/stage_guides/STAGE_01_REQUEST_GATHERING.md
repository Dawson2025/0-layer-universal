---
resource_id: "b69f7bc8-0a51-4b6a-86c9-281d01c14374"
resource_type: "knowledge"
resource_name: "STAGE_01_REQUEST_GATHERING"
---
# Stage 01: Request Gathering — Universal Guide

<!-- section_id: "7a7f9893-10aa-475a-ab68-a65bf36671f8" -->
## Purpose

Transform vague user needs into structured, testable requirements. This is the **intake stage** — everything starts here.

<!-- section_id: "3fd4e354-3135-411c-8e2f-d6ab823eac2d" -->
## What This Stage IS

The request gathering agent:
- Asks questions to clarify what the user actually needs
- Decomposes large needs into smaller, specific, testable needs
- Writes requirements in a standard format (requirements/ and user_stories/ subdirectories per need)
- Organizes requirements as a **tree of needs** (hierarchical decomposition)
- Validates requirements with the user before handing off

<!-- section_id: "8c7f1291-bce5-4d2c-b919-6aa17c3ea97c" -->
## What This Stage IS NOT

The request gathering agent does NOT:
- **Research solutions** — that's stage 02 (research)
- **Define constraints or guidelines** — that's stage 03 (instructions)
- **Design architectures** — that's stage 04 (design) / stage 05 (planning)
- **Write code or build artifacts** — that's stage 06 (development)
- **Judge feasibility** — that's stage 08 (criticism)
- **Make implementation decisions** — those emerge from design, not requirements

The agent captures **what** is needed, not **how** to achieve it.

<!-- section_id: "5ee5747c-73c6-4a21-94f4-a1ece7a33440" -->
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

<!-- section_id: "c2bef048-eb6e-4d83-b6d7-89a469b7179c" -->
### Need README.md Format

Each need's `README.md` contains the overview:
- **Definition**: What this need is about
- **Why This Matters**: Impact and motivation
- **Acceptance Criteria**: How to verify the need is met
- **Research References**: Links to related research
- Links to `requirements/` and `user_stories/` subdirectories

<!-- section_id: "0749b0ad-3464-4800-adbc-448f2e4ca5ee" -->
### Requirements Format

Each `requirements/REQ-NN_name.md` contains:
- **Functional requirements**: MUST/SHOULD/MUST NOT statements for one requirement group
- **Back-reference**: Link to the parent need README.md

The `requirements/README.md` provides an index table of all requirements in the need.

<!-- section_id: "d7b2c984-9bfb-4a2e-9b63-870322c94b19" -->
### User Stories Format

Each `user_stories/US-NN_name.md` contains one story in standard format:
```
As a [agent/manager/user/system], I need [specific capability] so that [benefit/outcome].
```
Plus an acceptance line and back-reference to the need README.md.

The `user_stories/README.md` provides an index table and the actors section.

<!-- section_id: "0ffa098a-43de-492c-a197-837145d2155f" -->
## Inputs

What the request gathering agent reads:
- **Parent entity 0AGNOSTIC.md** — to understand what this entity IS and its domain
- **Parent entity .0agnostic/01_knowledge/** — for domain understanding (read selectively, not all at once)
- **User conversations** — primary source of requirements
- **Existing tree of needs** (if resuming) — `outputs/requests/tree_of_needs/`
- **Prior stage reports** — none (this is the first stage), but may re-enter after stage 08 (criticism) loops back

<!-- section_id: "49a6ab8b-9ba5-4a66-a746-497d48cca14d" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Tree of needs | `outputs/requests/tree_of_needs/` | Directory tree with requirements/ + user_stories/ subdirs per leaf need |
| Root need | `outputs/requests/tree_of_needs/00_{root_name}/` | README.md with branch overview |
| Meta | `outputs/requests/tree_of_needs/_meta/` | VERSION.md, CHANGELOG.md, DEPENDENCIES.md |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Standard stage report format |

<!-- section_id: "31ae3a9f-a37b-4ae9-b47c-d059edaa5b75" -->
## Success Criteria

This stage is complete when:
1. All identified needs have `requirements/` and `user_stories/` subdirectories with individual files
2. Requirements are testable (can be validated in stage 07)
3. User has validated the tree of needs (explicit sign-off)
4. Priority ordering exists across needs
5. No unresolved ambiguities in requirements
6. Dependencies between needs are documented

<!-- section_id: "1b76969b-2193-425f-8756-9f76d60a278b" -->
## Exit Protocol

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to **stage 02** (research): note which needs require investigation of the problem space
3. If handing off to **stage 04** (design): note which needs are well-understood and ready for architecture decisions
4. If returning from **stage 08** (criticism): note which requirements need revision based on critique feedback

<!-- section_id: "015f0223-975e-4f5b-ad8c-78ab00c3de0c" -->
## Common Patterns

- **Parallel with stage 02**: Requirements gathering and research often run in parallel — research reveals new needs, requirements clarify research scope
- **Loop from stage 08**: After criticism, new or revised requirements may be needed — the agent re-enters to update the tree
- **Incremental growth**: The tree of needs grows over time — don't try to capture everything in one pass
- **User validation is mandatory**: Never hand off to later stages without user confirmation that requirements are correct

<!-- section_id: "960db239-00cd-4edf-8095-64ba65677fb5" -->
## Anti-Patterns

- Designing solutions while gathering requirements (scope creep into stage 04/05)
- Writing overly detailed requirements that constrain implementation unnecessarily
- Skipping user validation — requirements must be confirmed
- Loading all parent knowledge at once instead of reading selectively
- Treating requirements as final — they evolve as understanding deepens
