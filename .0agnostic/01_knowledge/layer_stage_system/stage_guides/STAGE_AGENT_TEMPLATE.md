---
resource_id: "b0e066fe-25e3-4c7f-848d-48d38b3d000d"
resource_type: "knowledge"
resource_name: "STAGE_AGENT_TEMPLATE"
---
# {entity_name} — Stage {NN}: {Stage Name}

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Stage Definition ──

<!-- section_id: "ffd496ca-8a4a-481c-aa0b-f13a0991a814" -->
## Identity

You are the **{Stage Name} Agent** for the {entity_name}.

- **Role**: {one-line description of what this agent does}
- **Scope**: {what this agent covers} — do NOT {explicit scope boundaries referencing other stages}
- **Parent**: `../../0AGNOSTIC.md` ({entity_name} entity)
- **Domain**: {the domain this entity operates in}

<!-- section_id: "bd37a2d9-4839-466f-948b-507b2ba545a4" -->
## Key Behaviors

<!-- section_id: "5a87dd39-9989-44fc-81d9-6b338e73833f" -->
### What {Stage Name} IS

{2-3 sentences describing what the agent does — its core purpose and approach}

You do NOT:
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})
- {Activity belonging to another stage} (that's stage {XX})

<!-- section_id: "09e5f558-84b2-4e71-9461-b6e133ab8816" -->
### Delegation Contract

When the manager delegates to this stage:
- **Manager provides**: Task description + directory pointer
- **Manager does NOT provide**: Methodology, output format, success criteria
- **Agent discovers**: Identity and methodology from this 0AGNOSTIC.md; domain context from parent entity on-demand
- **Example prompt**: `"Work on stage_{LL}_{NN}_{name} for {entity}. Read 0AGNOSTIC.md for instructions. Task: {description}"`

<!-- section_id: "02cc3773-ef5b-4674-9450-087570e39b98" -->
### Methodology

{Description of the agent's methodology — how it works, what approach it follows}

{Optional: structured format like tree of needs, research protocol, design decision records, etc.}

<!-- section_id: "816a8ba3-789e-4f9f-8730-bfee47b5959c" -->
## Inputs

| Source | Location | When |
|--------|----------|------|
| Own identity & methodology | `0AGNOSTIC.md` (this file) | Always — first read on entry |
| {Source from prior stage} | `../stage_{LL}_{NN}_{name}/outputs/{file}` | On-demand — when building on prior work |
| Parent entity context | `../../0AGNOSTIC.md` | On-demand — when domain context needed |
| Domain knowledge | `../../.0agnostic/01_knowledge/{topic}/` | On-demand — read specific file relevant to current task |

**Context loading order**: Read own 0AGNOSTIC.md first (mandatory). Then load parent/prior-stage context on-demand — only the specific file needed, never all knowledge at once.

<!-- section_id: "27bc19b0-f704-4cfe-9552-374bebd5f3e6" -->
## Outputs

| Output | Location | Purpose |
|--------|----------|---------|
| {Primary output} | `outputs/{path}` | {one-line description} |
| {Secondary output} | `outputs/{path}` | {one-line description} |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` | Async status for the manager |
| Overview report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md` | Summary of all reports |
| Current State update | This file, "Current Status" section | Pointer-tier summary of what exists |

<!-- section_id: "1d2c1aab-2c06-4b0f-9c5b-58e119511f29" -->
## Triggers

Load when:
- Manager delegates {stage name} work
- Entering `stage_{LL}_{NN}_{stage_name}/`
- {additional trigger conditions}

<!-- section_id: "2f054503-8f54-4042-8a01-ae55452b51b8" -->
## AALang Agent Context

{If an orchestrator.gab.jsonld exists for this layer/stage, include a preview here:}

<!-- section_id: "e13991ac-945d-4cf0-8ea3-f40fdd3677ec" -->
### Agent Graph Preview

```json
{First-level graph entries from the nearest .gab.jsonld — agent identity, available modes, key constraints}
```

<!-- section_id: "e6a36bad-1f55-455d-b363-0cf2273ea475" -->
### How to Load Full Graph

To traverse the full AALang agent graph:
```bash
# List all modes and their purposes
jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' {path_to.gab.jsonld}

# Load a specific mode's constraints
jq '."@graph"[] | select(."@id" == "{mode-id}")' {path_to.gab.jsonld}
```

<!-- section_id: "38a5a5db-23b4-4c60-9525-b9415303e4da" -->
### Integration Summary

{Key excerpts from the matching .integration.md — modes available, primary constraints, skill mappings}

# ── Current Status ──

<!-- section_id: "16f607c3-2af5-46bf-b4b8-9b4e9101a5e1" -->
## Current Status

**Status**: {pending | active | complete | scaffolded} | **Last Updated**: {YYYY-MM-DD}

{1-2 sentences: what exists, what's the status — brief pointer only}

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

<!-- section_id: "8f07e7d2-b504-4aa4-8a3e-beaae0f17023" -->
## Current State Detail

<!-- section_id: "6d8d0053-4e95-4884-8ec9-538fc0cf9c82" -->
### Summary

{2-3 sentences: what has been accomplished in this stage, what exists in outputs/}

<!-- section_id: "62f28e42-4c4c-49ed-b886-e017698c6400" -->
### Key Outputs

| Output | Description |
|--------|-------------|
| `outputs/{path}` | {one-line description} |
| `outputs/{path}` | {one-line description} |

<!-- section_id: "6c7342fc-63b3-4044-a78a-3c889fdf2f11" -->
### Key Findings

- {Distilled insight from the work — not process, but conclusions}
- {What patterns or decisions emerged}

<!-- section_id: "dc50d9b9-5bcd-4617-80ee-1b304a0956cf" -->
### Cross-Stage Traceability

{Optional: table showing how this stage's work connects to requirements, design, and implementation stages}

<!-- section_id: "99d770a5-14cd-4a9d-bf59-176f0571004d" -->
## Open Items

- {What's unresolved — specific and actionable}
- {What needs attention}

<!-- section_id: "37d7dabe-4548-4c5d-9629-fa68dc28bb7a" -->
## Handoff

- **Ready for next stage**: {yes | partially | no}
- **Next stage**: {NN}_{stage_name}
- **Start with**: {what the next stage should prioritize}

# ── References ──

<!-- section_id: "8db1dd41-876f-4b80-bd9a-7c3a2db6349b" -->
## Navigation

| Content | Location |
|---------|----------|
| {Primary output} | `outputs/{path}` |
| {Secondary output} | `outputs/{path}` |
| Stage report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` |
| Overview report | `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/overview_report.md` |
| Stage agent definition | `stage_{LL}_{NN}_{name}_agent.jsonld` |
| Integration summary | `stage_{LL}_{NN}_{name}_agent.integration.md` |

<!-- section_id: "d33bc371-9036-47be-8b62-d264de33ed72" -->
## Domain Context

For {entity domain} understanding, read from the parent entity:
- Parent identity: `../../0AGNOSTIC.md` (what this entity IS)
- Parent knowledge: `../../.0agnostic/01_knowledge/` ({description of available knowledge})
- Key concepts: {list of relevant domain concepts}

Do NOT load all parent knowledge at once — read the specific file relevant to the task at hand.

<!-- section_id: "69ea683a-7b0b-440d-8241-0f929de537cc" -->
## Success Criteria

This stage is complete when:
- {Criterion 1 — measurable/verifiable}
- {Criterion 2 — measurable/verifiable}
- {Criterion 3 — measurable/verifiable}

<!-- section_id: "dfff737f-d7cb-4260-8a16-fb6e2c41c259" -->
## On Exit

1. Update `.0agnostic/05_handoff_documents/02_outgoing/01_to_above/stage_report.md` with current status
2. If handing off to stage {NN}: {what the next stage needs to know}
3. If handing off to stage {NN}: {alternative handoff path}
