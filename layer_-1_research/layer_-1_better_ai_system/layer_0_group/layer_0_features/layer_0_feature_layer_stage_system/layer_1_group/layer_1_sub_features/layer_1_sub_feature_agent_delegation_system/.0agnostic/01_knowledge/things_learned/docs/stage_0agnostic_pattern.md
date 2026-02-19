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

## Formalized As

- **Principle 9** ("Two-Halves Context Pattern") in `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`

---

# What We Learned: Scope Boundary Decisions

## Discovery Date
2026-02-19

## The Pattern

Scope boundaries are not just "stop and hand off" — they require an **active decision** about how to handle out-of-scope work. The decision has three options:

### Option 1: Do It Yourself (small, tightly coupled)
When the out-of-scope work is trivial and tightly coupled to what you're doing. Example: a stage 06 agent notices a typo in a stage 04 design doc while implementing — fixing it in-place is faster than a full handoff cycle.

### Option 2: Delegate to Existing Agent (significant, agent exists)
When the work is significant and an agent already exists for the target scope. Send a message, create a task, or write a handoff document.

### Option 3: Instantiate a New Agent (significant, no agent exists)
When the work is significant but no agent has been instantiated for the target layer/stage yet. Spawn a new agent with a Task tool call, pointing it to the target 0AGNOSTIC.md.

## The Key Factor: Context Window Preservation

The decision is ultimately about context window management. An agent that tries to work across too many layers/stages will:
- Overflow its context window
- Lose track of its own methodology
- Produce lower-quality work
- Make outputs unfindable (wrong stage/entity)

**Default to delegate.** The cost of spawning an agent is low; the cost of a bloated, confused context is high.

## Where This Is Codified

- **Principle 8** ("Scope Boundary Decisions") in `layer_0/.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`
- **Scope Boundary Rule** (expanded from Stage Boundary Rule) in `layer_0/.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`
