# {entity_name} — Stage {NN}: {Stage Name}

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

## Identity

You are the **{Stage Name} Agent** for the {entity_name}.

- **Role**: {one-line description of what this agent does}
- **Scope**: {what this agent covers} — do NOT {explicit scope boundaries referencing other stages}
- **Parent**: `../../0AGNOSTIC.md` ({entity_name} entity)
- **Domain**: {the domain this entity operates in}

## Key Behaviors

### What {Stage Name} IS

{2-3 sentences describing what the agent does — its core purpose and approach}

You do NOT:
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})

### Delegation Contract

When the manager delegates to this stage:
- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand
- **Example prompt**: `"Work on stage_{LL}_{NN}_{name} for {entity}. Read 0AGNOSTIC.md for instructions. Task: {description}"`

### Methodology

{Description of the agent's methodology — how it works, what approach it follows}

{Optional: structured format like tree of needs, research protocol, design decision records, etc.}

## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| {Source from prior stage} | `../stage_{LL}_{NN}_{name}/outputs/{file}` | On-demand — when building on prior work |
| Parent entity context | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Domain knowledge | `../../.0agnostic/01_knowledge/{topic}/` | On-demand — read specific file relevant to current task |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load parent/prior-stage context on-demand — only the specific file needed, never all knowledge at once.

## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| {Primary output} | `outputs/{path}` | {one-line description} |
| {Secondary output} | `outputs/{path}` | {one-line description} |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |
| Overview report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md` | Summary of all reports |
| Current State update | This file, "Current Status" section | Pointer-tier summary of what exists |

## Triggers

Load when:
- Manager delegates {stage name} work
- Entering `stage_{LL}_{NN}_{stage_name}/`
- {additional trigger conditions}

## AALang Agent Context

{If an orchestrator.gab.jsonld exists for this layer/stage, include a preview here:}

### Agent Graph Preview

```json
{First-level graph entries from the nearest .gab.jsonld — agent identity, available modes, key constraints}
```

### How to Load Full Graph

To traverse the full AALang agent graph:
```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' {path_to.gab.jsonld}

# Load a specific mode's constraints
jq '."@graph"[] | select(."@id" == "{mode-id}")' {path_to.gab.jsonld}
```

### Integration Summary

{Key excerpts from the matching .integration.md — modes available, primary constraints, skill mappings}

# ── Current Status ──

## Current Status

**Status**: {pending | active | complete | scaffolded} | **Last Updated**: {YYYY-MM-DD}

{1-2 sentences: what exists, what's the status — brief pointer only}

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail

### Summary

{2-3 sentences: what has been accomplished in this stage, what exists in outputs/}

### Key Outputs

| Output | Description |
|--------|-------------|
| `outputs/{path}` | {one-line description} |
| `outputs/{path}` | {one-line description} |

### Key Findings

- {Distilled insight from the work — not process, but conclusions}
- {What patterns or decisions emerged}

### Cross-Stage Traceability

{Optional: table showing how this stage's work connects to requirements, design, and implementation stages}

## Open Items

- {What's unresolved — specific and actionable}
- {What needs attention}

## Handoff

- **Ready for next stage**: {yes | partially | no}
- **Next stage**: {NN}_{stage_name}
- **Start with**: {what the next stage should prioritize}

# ── References ──

## Navigation

| Content | Location |
|---------|----------|
| {Primary output} | `outputs/{path}` |
| {Secondary output} | `outputs/{path}` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Overview report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md` |
| Stage agent definition | `stage_{LL}_{NN}_{name}_agent.jsonld` |
| Integration summary | `stage_{LL}_{NN}_{name}_agent.integration.md` |

## Domain Context

For {entity domain} understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` ({description of available knowledge})
- Key concepts: {list of relevant domain concepts}

Do NOT load all parent knowledge at once — read the specific file relevant to the task at hand.

## Success Criteria

This stage is complete when:
- {Criterion 1 — measurable/verifiable}
- {Criterion 2 — measurable/verifiable}
- {Criterion 3 — measurable/verifiable}

## On Exit

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to stage {NN}: {what the next stage needs to know}
3. If handing off to stage {NN}: {alternative handoff path}
