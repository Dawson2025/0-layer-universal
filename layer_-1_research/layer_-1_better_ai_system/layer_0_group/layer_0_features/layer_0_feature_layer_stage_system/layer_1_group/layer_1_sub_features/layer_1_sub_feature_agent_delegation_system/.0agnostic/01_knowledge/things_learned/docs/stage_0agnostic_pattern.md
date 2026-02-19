# What We Learned: Stage 0AGNOSTIC.md Pattern

## Discovery Date
2026-02-19

## The Pattern

Stage 0AGNOSTIC.md files need **two halves**:

### 1. Operational Guidance (written once, rarely changes)
- **Identity**: Role, scope, parent reference, domain
- **Scope boundaries**: What this stage IS and IS NOT (the NOT list is critical)
- **Methodology**: How the agent works (e.g., tree of needs for stage 01)
- **Domain context pointers**: Where to find parent knowledge (don't load it, just point)
- **Stage report requirement**: Update `outputs/stage_report.md` before exiting
- **Success criteria**: When is this stage done?
- **Exit protocol**: What to do before leaving

### 2. Current State Summary (updated as work progresses)
- **Status**: active / scaffolded / complete
- **Summary**: 2-3 sentences on what's been accomplished
- **Key outputs**: Named files/structures with brief descriptions
- **Key findings**: Distilled insights (not process descriptions)
- **Open items**: What's unresolved or needs attention
- **Handoff status**: Ready for next stage? What does next stage need to know?
- **Detailed references**: Links to specific outputs for deeper reading

## Why This Matters

Without the current state half, an agent landing in a stage must:
1. Read the stage_report.md (if it exists)
2. Explore outputs/ manually
3. Piece together what's been done

This wastes context window tokens on exploration instead of productive work.

With the current state half in 0AGNOSTIC.md, the agent gets immediate orientation from the **pointer tier** — the same file it reads for operational guidance also tells it what's already here.

## Where This Is Codified

- Universal template: `layer_0/.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md`
- Example (context_chain_system stage 01): `.../stage_3_01_request_gathering/0AGNOSTIC.md`
- Example (agent_delegation_system stage 01): `.../stage_1_01_request_gathering/0AGNOSTIC.md`

## Relationship to Stage Reports

The current state section in 0AGNOSTIC.md and the stage_report.md are complementary:
- **0AGNOSTIC.md current state**: Pointer-tier summary — loaded automatically as static context
- **stage_report.md**: More detailed, follows a strict protocol format, written specifically for the entity manager

The current state section can be derived from the stage report but is more concise and embedded in the context file that agents read first.
