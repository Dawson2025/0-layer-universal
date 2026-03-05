---
resource_id: "616e3692-1e02-4287-875b-d38d4e0b2c93"
resource_type: "knowledge"
resource_name: "STAGE_04_DESIGN"
---
# Stage 04: Design — Universal Guide

## Purpose

Make architecture decisions and write design specifications based on research findings and within instruction constraints. This is the **architecture stage** — decide what to build and how the pieces fit together.

## What This Stage IS

The design agent:
- Makes architecture decisions based on research trade-offs (from stage 02)
- Writes design documents that specify component structure, interfaces, and interactions
- Documents decision rationale (why this approach, not alternatives)
- Defines the system's layers, modules, data flows, and boundaries
- Creates diagrams when they clarify complex relationships

## What This Stage IS NOT

The design agent does NOT:
- **Gather requirements** — that's stage 01
- **Research alternatives** — that's stage 02 (design uses research outputs to decide)
- **Break work into tasks** — that's stage 05 (planning)
- **Write code or build artifacts** — that's stage 06 (development)
- **Test the design** — that's stage 07 (testing)
- **Critique the design** — that's stage 08 (criticism)

The agent decides **what the architecture is**, not **how to implement it step by step**.

## Methodology

Design outputs are organized by topic:

```
outputs/
├── by_topic/
│   ├── README.md                    <- Design index: all decisions and specs
│   ├── 01_design_topic.md           <- Architecture specification
│   ├── 02_design_topic.md           <- Another specification
│   └── NN_design_topic.md
└── stage_report.md
```

### Design Document Format

Each design document should contain:
- **Context**: What problem this design addresses (links to stage 01 needs and stage 02 research)
- **Decision**: The chosen approach
- **Alternatives considered**: What else was evaluated (from stage 02 research)
- **Rationale**: Why this approach was chosen
- **Architecture**: Components, interfaces, data flows
- **Constraints respected**: Which stage 03 constraints this design operates within
- **Risks**: Known risks and mitigations

## Inputs

- **Stage 01 outputs** — requirements defining what must be built
- **Stage 02 outputs** — research findings with trade-offs and options
- **Stage 03 outputs** — constraints that bound the design space
- **Parent entity .0agnostic/01_knowledge/** — domain knowledge

## Outputs

| Output | Location | Format |
|--------|----------|--------|
| Design specs | `outputs/by_topic/` | Architecture documents with decisions and rationale |
| Design index | `outputs/by_topic/README.md` | Overview of all design decisions |
| Stage report | `outputs/stage_report.md` | Standard stage report format |

## Success Criteria

This stage is complete when:
1. All requirements from stage 01 have a design that addresses them
2. Architecture decisions are documented with rationale
3. Constraints from stage 03 are respected
4. Design is detailed enough for stage 05 to break into tasks
5. Open design questions are resolved or explicitly deferred

## Exit Protocol

1. Update `outputs/stage_report.md` with current status
2. If handing off to **stage 05** (planning): highlight the major components that need implementation tasks
3. If handing off to **stage 02** (research): note design questions that need more investigation

## Available Tools

### Diagram Creation (Mermaid.js)

Design stages use Mermaid.js for architecture diagrams. Available tooling:

| Tool | Type | Purpose |
|------|------|---------|
| `claude-mermaid` MCP server | MCP | Live preview + export (SVG/PNG/PDF) via `mermaid_preview` and `mermaid_save` tools |
| `mermaid-diagrams` skill | Skill | Best practices and expert guidance for diagram creation |

**Full documentation**: `.0agnostic/01_knowledge/visualization_tools/docs/mermaid_tools_guide.md`

**Key syntax rules**:
- Use `flowchart` (not `graph`) for better renderer compatibility
- Use `<br/>` for line breaks in labels (not `\n`)
- Avoid HTML tags (`<i>`, `<b>`, `<code>`) in labels

**Diagram output location**: `outputs/design_decisions/{topic}/diagrams/` or `outputs/by_topic/diagrams/`

## Common Patterns

- **Design follows research**: Design decisions should trace back to research findings — don't design in a vacuum
- **Multiple design docs**: Complex entities may have multiple design documents for different aspects
- **Decision records**: Each major decision should have alternatives + rationale documented
- **Iterative refinement**: Design may loop back to research (02) when questions arise
- **Diagrams complement text**: Use Mermaid diagrams alongside design documents to visualize dependencies, data flows, and communication patterns

## Anti-Patterns

- Designing without reading research (stage 02) first
- Making decisions without documenting rationale
- Over-designing before validating core assumptions
- Confusing design with planning (design = what, planning = how/when)
- Creating diagrams without a companion design document
