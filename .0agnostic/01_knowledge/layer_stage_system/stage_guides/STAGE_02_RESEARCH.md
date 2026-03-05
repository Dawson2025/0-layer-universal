---
resource_id: "c4f1589d-a70e-470a-b948-441326249d91"
resource_type: "knowledge"
resource_name: "STAGE_02_RESEARCH"
---
# Stage 02: Research — Universal Guide

<!-- section_id: "b802a018-fe94-44f0-a568-3348d8834c7a" -->
## Purpose

Investigate the problem space, gather information, and produce findings that inform design decisions. This is the **exploration stage** — understand what exists, what's possible, and what constraints apply.

<!-- section_id: "6afab15c-04e7-400d-b1bb-b21491e68c58" -->
## What This Stage IS

The research agent:
- Investigates the problem domain using web search, documentation, codebase exploration, and prior art analysis
- Organizes findings by topic in a structured directory hierarchy
- Produces a research index (README.md) that maps all findings
- Identifies key decisions, trade-offs, and open questions
- Verifies assumptions through testing or evidence gathering
- Documents what was found to be true/false/uncertain

<!-- section_id: "bf1a0b1f-2aed-4d9a-9002-32d296b26148" -->
## What This Stage IS NOT

The research agent does NOT:
- **Gather requirements** — that's stage 01 (request_gathering)
- **Define constraints or guidelines** — that's stage 03 (instructions)
- **Make architecture decisions** — that's stage 04 (design) — research presents options and trade-offs, design makes the call
- **Break work into tasks** — that's stage 05 (planning)
- **Build anything** — that's stage 06 (development)
- **Validate implementations** — that's stage 07 (testing)

The agent discovers **what's possible and what exists**, not **what to build**.

<!-- section_id: "74cbb70e-ffc2-4ea1-bb93-c7676d45f059" -->
## Methodology: Topic-Based Research

Research outputs are organized by topic:

```
outputs/
├── by_topic/
│   ├── README.md                 <- Master index: all topics, key findings, open questions
│   ├── 01_topic_name/            <- Numbered topic areas
│   │   ├── finding_01.md
│   │   └── finding_02.md
│   ├── 02_topic_name/
│   └── NN_topic_name/
└── stage_report.md               <- Status for the entity manager
```

<!-- section_id: "7c9b8739-9f55-407e-bc6f-529a22a389ff" -->
### Research File Format

Each research file should contain:
- **Question**: What was being investigated
- **Findings**: What was discovered (with evidence)
- **Sources**: Links to references, documentation, prior art
- **Implications**: How this affects the entity's design/implementation
- **Open Questions**: What remains unknown

<!-- section_id: "23402e7d-e201-4459-a574-983cda50e855" -->
### Research Index (README.md)

The master index maps all topics and their key findings:
- Topic name and description
- Key findings per topic (1-2 sentences each)
- Cross-references between topics
- Open questions that need further investigation or that inform design

<!-- section_id: "8615b84c-3849-4d5e-b583-16ad8f820008" -->
## Inputs

What the research agent reads:
- **Stage 01 outputs** — `../stage_{LL}_01_request_gathering/outputs/requests/tree_of_needs/` — what needs to be researched
- **Parent entity 0AGNOSTIC.md** — domain understanding
- **Parent entity .0agnostic/01_knowledge/** — existing domain knowledge (read selectively)
- **Web sources** — via search tools (always include Sources: section)
- **Codebase** — existing implementations to learn from

<!-- section_id: "d9ca9af7-11a4-43d7-8e20-968c1027214e" -->
## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Research by topic | `outputs/by_topic/` | Directory tree with .md files per finding |
| Research index | `outputs/by_topic/README.md` | Master table of contents with key findings |
| Verification results | `outputs/by_topic/verification/` | What was tested/verified |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

<!-- section_id: "cfdff93f-d57b-42a5-91cd-e9df0398a3e8" -->
## Success Criteria

This stage is complete when:
1. All needs from stage 01 have been investigated (or flagged as not requiring research)
2. Key findings are documented with evidence and sources
3. Trade-offs between approaches are identified
4. Open questions are explicitly listed
5. Research index (README.md) maps all findings
6. Findings are sufficient for stage 04 (design) to make informed decisions

<!-- section_id: "3cce4db3-1daa-444c-ab17-1eb99f5a2d88" -->
## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 04** (design): summarize key decisions to be made, list the trade-offs research revealed
3. If handing off to **stage 01** (request_gathering): note new needs discovered during research
4. If handing off to **stage 03** (instructions): note constraints discovered that should become guidelines

<!-- section_id: "c40f66e4-ae60-42be-8e32-286b315f978d" -->
## Common Patterns

- **Parallel with stage 01**: Research often reveals new requirements — feed these back to request_gathering
- **Iterative deepening**: Start broad, then dive deep into specific topics as they prove important
- **Evidence-based**: Always cite sources — don't assert without evidence
- **Verification**: When possible, test claims through prototypes or experiments (but keep these minimal — full implementation is stage 06)

<!-- section_id: "eed6899e-aac6-4ee4-b087-2fa8600b2ac1" -->
## Anti-Patterns

- Making design decisions during research (that's stage 04's job — research presents options)
- Researching without clear questions from stage 01 (research needs direction)
- Loading all parent knowledge at once instead of reading selectively
- Producing research without a clear index (findings become unfindable)
- Skipping the Sources: section (unverifiable claims)
