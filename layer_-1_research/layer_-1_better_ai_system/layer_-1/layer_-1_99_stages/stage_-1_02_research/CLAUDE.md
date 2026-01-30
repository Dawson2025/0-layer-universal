# stage_-1_02_research

## Purpose
Explore problem space, gather information, analyze options for each need in the Tree of Needs.

## Context
- **Project**: better_ai_system
- **Layer**: -1 (Research)
- **Stage**: 02 - Research
- **Status**: Active
- **Input**: Tree of Needs v1.4.0 (15 needs across 5 branches)

---

## Incoming Handoff

**From**: stage_-1_01_request_gathering
**Document**: `hand_off_documents/incoming/20260126_to_research_handoff.md`

### Key Inputs
- Tree of Needs (DAG structure, 5 branches, 15 needs)
- Guiding Principles (P1-P5)
- Dependencies map
- Open questions for research

---

## Research Priorities

### Phase 1: Foundation (HIGH)
| Need | Research Focus |
|------|----------------|
| `persistent_knowledge` | System prompt hierarchies, CLAUDE.md cascade patterns |
| `discoverable` | Self-describing structures, AI navigation patterns |
| `scalable_context` | Agent delegation, progressive disclosure techniques |

### Phase 2: Continuity (HIGH)
| Need | Research Focus |
|------|----------------|
| `tool_portable` | Agnostic architecture, tool abstraction layers |
| `session_resilient` | Handoff mechanisms, state persistence patterns |

### Phase 3: Supporting (MEDIUM)
| Need | Research Focus |
|------|----------------|
| `failure_recoverable` | Idempotent patterns, rollback mechanisms |
| `evolvable` | Modular design, forward-compatible formats |
| `cross_platform` | OS abstraction, config portability |
| `rule_compliant` | Rule hierarchy systems, conflict resolution |
| `debuggable` | Validation tooling, error diagnosis |

### Phase 4: Enhancement (LOWER)
| Need | Research Focus |
|------|----------------|
| `predictable`, `bounded` | Scope definitions, permission models |
| `transparent`, `auditable` | State inspection, audit trails |
| `multimodal` | Voice I/O, diagram generation |

---

## Output Structure

```
outputs/
├── by_need/                      Research organized by need
│   ├── 01_persistent_knowledge/
│   │   ├── options_analysis.md
│   │   ├── recommended_approach.md
│   │   └── implementation_sketch.md
│   ├── 02_discoverable/
│   └── ...
│
├── by_topic/                     Cross-cutting research
│   ├── existing_solutions.md    What's already out there
│   ├── technology_choices.md    Tool/format decisions
│   └── patterns.md              Reusable patterns discovered
│
└── synthesis/                    Combined insights
    ├── architecture_overview.md
    └── research_summary.md
```

---

## Research Template (Per Need)

For each need, produce:

### 1. Options Analysis (`options_analysis.md`)
```markdown
# Options Analysis: [Need Name]

## Option A: [Name]
- **Description**: ...
- **Pros**: ...
- **Cons**: ...
- **Complexity**: Low/Medium/High

## Option B: [Name]
...

## Comparison Matrix
| Criteria | Option A | Option B | Option C |
|----------|----------|----------|----------|
```

### 2. Recommended Approach (`recommended_approach.md`)
```markdown
# Recommended Approach: [Need Name]

## Selected Option
[Which option and why]

## Justification
[Why this option best satisfies the need]

## Trade-offs Accepted
[What we're giving up]
```

### 3. Implementation Sketch (`implementation_sketch.md`)
```markdown
# Implementation Sketch: [Need Name]

## High-Level Design
[Architecture/structure]

## Key Components
[What needs to be built]

## Integration Points
[How it connects to other needs]

## Open Questions
[Remaining unknowns]
```

---

## Skills Available

| Skill | Purpose |
|-------|---------|
| `/02_research-workflow` | Research workflow guidance |

---

## Working in This Stage

### Starting Research on a Need
1. Read the need's `requirements.md` from Tree of Needs
2. Check dependencies in `_meta/DEPENDENCIES.md`
3. Create folder in `outputs/by_need/[need_name]/`
4. Research existing solutions, patterns, tools
5. Document options, recommend approach, sketch implementation

### Using External Research
- Use Perplexity for academic/industry research
- Document sources in research files
- Validate findings against our principles (P1-P5)

### Cross-Need Insights
When research reveals patterns applicable to multiple needs:
1. Document in `outputs/by_topic/`
2. Reference from individual need research

---

## Next Stage

When research is complete, transition to **Stage 03: Instructions** to create detailed implementation guides.

See: `../stage_-1_03_instructions/`

---

## Key Files

| File | Purpose |
|------|---------|
| `hand_off_documents/incoming/20260126_to_research_handoff.md` | Input from request gathering |
| `outputs/by_need/` | Research organized by need |
| `outputs/by_topic/` | Cross-cutting research |
| `outputs/synthesis/` | Combined insights |
