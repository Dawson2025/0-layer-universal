# Context Chain Mode Rule

**Type**: Dynamic (loaded when triggered)
**Importance**: 1 (High)
**Scope**: All agents at all levels

## Rule

The context chain operates in one of two modes: **Default** or **Research**.
The user controls which mode is active. Default mode is always the starting state.

### Default Mode (default)

Use ONLY production resources:
- `.0agnostic/` at the current entity and inherited from parents
- `entity_structure.md` for canonical structure
- Production protocols, rules, knowledge, tools
- No research entity content is loaded

This is the tried-and-true, stable context chain.

### Research Mode (user opt-in)

Use production resources AS THE BASE, then ADDITIONALLY load:
1. **Research Knowledge Index**: Read `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`
2. **Research entity 0AGNOSTIC.md files**: When working on topics covered by research entities, read their 0AGNOSTIC.md for experimental patterns and findings
3. **Research outputs**: Follow RESEARCH_KNOWLEDGE_INDEX.md references to load specific research documents relevant to the current task
4. **Experimental patterns**: When research has proven a pattern (marked "PROMOTED" or "Referenced" with test validation), prefer the research version over production if they differ

Research mode EXTENDS default — it never replaces it. Production rules and protocols still apply.
Research content provides additional context, experimental alternatives, and deeper rationale.

## Trigger Conditions

Switch to **Research Mode** when the user:
- Says "use research context chain" or "switch to research mode"
- Says "use research context" or "enable research mode"
- Says "I want to use the research version"
- Says "use experimental context chain"
- Mentions wanting to try research-based patterns or experimental approaches

Switch back to **Default Mode** when the user:
- Says "use default context chain" or "switch to default mode"
- Says "go back to default" or "use production context"
- Says "disable research mode"
- Starts a new session (default mode is always the starting state)

## What Changes in Research Mode

| Aspect | Default Mode | Research Mode |
|--------|-------------|---------------|
| Knowledge sources | Production `.0agnostic/01_knowledge/` only | Production + research entity knowledge |
| Entity structure | `entity_structure.md` (canonical) | Canonical + experimental variations from research |
| Protocols | Production `.0agnostic/03_protocols/` | Production + research-documented workflows |
| Rules | Production `.0agnostic/02_rules/` | Production + research-validated rules |
| Context depth | Standard (lean, optimized) | Extended (includes rationale docs from research) |
| Agent behavior | Follow proven patterns | May suggest experimental alternatives |
| Stage instantiation | Empty stage directories | Pre-scaffolded with stage templates (see below) |

## Stage Instantiation Templates (Research Mode Only)

In Research Mode, when creating new entities with stages, agents should pre-scaffold stage directories with experimental organizational patterns instead of leaving them empty.

### Stage 01: Request Gathering

Instantiate with directory-based tree of needs:

```
outputs/requests/tree_of_needs/
├── _meta/
│   ├── VERSION.md
│   ├── CHANGELOG.md
│   └── DEPENDENCIES.md
└── 00_{root_need}/
    ├── README.md
    ├── NN_{branch}/
    │   ├── README.md
    │   └── need_NN_{name}/
    │       ├── README.md
    │       ├── requirements/
    │       │   ├── README.md
    │       │   └── REQ-NN_{name}.md
    │       └── user_stories/
    │           ├── README.md
    │           └── US-NN_{name}.md
    └── ...
```

**Reference implementation**: `layer_1/layer_1_projects/layer_1_project_internship_prep/layer_1_group/layer_1_99_stages/stage_1_01_request_gathering/outputs/requests/tree_of_needs/`

### Stage 07: Testing

Instantiate with by-purpose organization:

```
outputs/by_purpose/
├── README.md            <- Testing taxonomy with purpose index
└── {purpose_name}/
    ├── design/          <- Test design docs
    ├── implementation/  <- Test scripts/code
    ├── runs/            <- Execution logs
    ├── results/         <- Parsed results
    └── insights/        <- Analysis and learnings
```

**Reference implementation**: `layer_1/layer_1_projects/layer_1_project_internship_prep/layer_1_group/layer_1_99_stages/stage_1_07_testing/outputs/by_purpose/`

### Other Stages

No experimental templates yet. In research mode, agents may propose new templates when patterns emerge from real usage.

**Status**: Experimental — these templates have been validated in one entity (internship_prep). They need broader testing before promotion to default mode.

## Agent Behavior in Research Mode

When in Research Mode, agents should:

1. **Announce the mode**: At session start, note "Operating in Research Context Chain Mode"
2. **Load the index**: Read RESEARCH_KNOWLEDGE_INDEX.md to know what research exists
3. **Cross-reference**: When working on a topic, check if research has findings on it
4. **Surface alternatives**: If research suggests a different approach than production, present both options to the user
5. **Track findings**: If new discoveries are made, suggest adding them to research entity outputs
6. **Never auto-promote**: Research findings are NOT automatically promoted to production — that requires the promotion protocol

## Related

- **Research Knowledge Index**: `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`
- **Promotion Protocol**: `.0agnostic/03_protocols/research_promotion_protocol.md`
- **Research entities**: See RESEARCH_KNOWLEDGE_INDEX.md for full paths
