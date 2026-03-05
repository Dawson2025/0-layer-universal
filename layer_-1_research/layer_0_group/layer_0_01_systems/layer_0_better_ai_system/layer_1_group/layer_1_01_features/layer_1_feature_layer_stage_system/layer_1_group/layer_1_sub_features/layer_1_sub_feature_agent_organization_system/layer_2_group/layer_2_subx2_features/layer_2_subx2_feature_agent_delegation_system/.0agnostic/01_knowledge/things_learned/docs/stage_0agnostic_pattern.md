---
resource_id: "f921cded-519d-4547-9b60-202ee70f5709"
resource_type: "knowledge"
resource_name: "stage_0agnostic_pattern"
---
# What We Learned: Stage 0AGNOSTIC.md Pattern

<!-- section_id: "327479d7-3ee8-4351-a1d1-6cc55ced39bf" -->
## Discovery Date
2026-02-19

<!-- section_id: "681c7e94-1c3c-42c5-bae8-ee60a0e8f9e2" -->
## The Pattern

Stage 0AGNOSTIC.md files need **two halves**:

<!-- section_id: "75208815-2f9b-4548-8fb4-98650fc3bd21" -->
### 1. Operational Guidance (written once, rarely changes)
- **Identity**: Role, scope, parent reference, domain
- **Scope boundaries**: What this stage IS and IS NOT (the NOT list is critical)
- **Methodology**: How the agent works (e.g., tree of needs for stage 01)
- **Domain context pointers**: Where to find parent knowledge (don't load it, just point)
- **Stage report requirement**: Update `outputs/reports/stage_report.md` before exiting
- **Success criteria**: When is this stage done?
- **Exit protocol**: What to do before leaving

<!-- section_id: "d4dad6b7-3525-4cf0-a8fa-581e206bb9ba" -->
### 2. Current State Summary (updated as work progresses)
- **Status**: active / scaffolded / complete
- **Summary**: 2-3 sentences on what's been accomplished
- **Key outputs**: Named files/structures with brief descriptions
- **Key findings**: Distilled insights (not process descriptions)
- **Open items**: What's unresolved or needs attention
- **Handoff status**: Ready for next stage? What does next stage need to know?
- **Detailed references**: Links to specific outputs for deeper reading

<!-- section_id: "3a14637a-815b-49fe-9b8e-fc7667f4897d" -->
## Why This Matters

Without the current state half, an agent landing in a stage must:
1. Read the stage_report.md (if it exists)
2. Explore outputs/ manually
3. Piece together what's been done

This wastes context window tokens on exploration instead of productive work.

With the current state half in 0AGNOSTIC.md, the agent gets immediate orientation from the **pointer tier** — the same file it reads for operational guidance also tells it what's already here.

<!-- section_id: "a44d05f8-1f9a-4267-9ad1-4ff0751ec70c" -->
## Where This Is Codified

- Universal template: `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md`
- Example (context_chain_system stage 01): `.../stage_3_01_request_gathering/0AGNOSTIC.md`
- Example (agent_delegation_system stage 01): `.../stage_1_01_request_gathering/0AGNOSTIC.md`

<!-- section_id: "7c1a1368-d037-4195-97eb-ec93e2b01e7d" -->
## Relationship to Stage Reports

The current state section in 0AGNOSTIC.md and the stage_report.md are complementary:
- **0AGNOSTIC.md current state**: Pointer-tier summary — loaded automatically as static context
- **stage_report.md**: More detailed, follows a strict protocol format, written specifically for the entity manager (canonical: `outputs/reports/stage_report.md`)

The current state section can be derived from the stage report but is more concise and embedded in the context file that agents read first.

<!-- section_id: "8793d03e-601d-428d-b931-074a5a6c9f63" -->
## Formalized As

- **Principle 9** ("Two-Halves Context Pattern") in `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`

---

# What We Learned: Scope Boundary Decisions

<!-- section_id: "8fbb29b9-d735-40e5-895a-071627662f6d" -->
## Discovery Date
2026-02-19

<!-- section_id: "9bf71946-08f1-4c90-9420-22fd2d35c9e9" -->
## The Pattern

Scope boundaries are not just "stop and hand off" — they require an **active decision** about how to handle out-of-scope work. The decision has three options:

<!-- section_id: "30b17a4d-df65-4b58-8d41-a4b14bb9e1f5" -->
### Option 1: Do It Yourself (small, tightly coupled)
When the out-of-scope work is trivial and tightly coupled to what you're doing. Example: a stage 06 agent notices a typo in a stage 04 design doc while implementing — fixing it in-place is faster than a full handoff cycle.

<!-- section_id: "46e36213-ad5c-4645-9d69-b07f48ab1d30" -->
### Option 2: Delegate to Existing Agent (significant, agent exists)
When the work is significant and an agent already exists for the target scope. Send a message, create a task, or write a handoff document.

<!-- section_id: "9ad4eea8-467c-4a69-8486-ad89e65a923b" -->
### Option 3: Instantiate a New Agent (significant, no agent exists)
When the work is significant but no agent has been instantiated for the target layer/stage yet. Spawn a new agent with a Task tool call, pointing it to the target 0AGNOSTIC.md.

<!-- section_id: "bdf51693-1622-4caa-89d3-798f0770eaf4" -->
## The Key Factor: Context Window Preservation

The decision is ultimately about context window management. An agent that tries to work across too many layers/stages will:
- Overflow its context window
- Lose track of its own methodology
- Produce lower-quality work
- Make outputs unfindable (wrong stage/entity)

**Default to delegate.** The cost of spawning an agent is low; the cost of a bloated, confused context is high.

<!-- section_id: "082ff4c4-b22a-4623-ac13-055381525ae2" -->
## Where This Is Codified

- **Principle 8** ("Scope Boundary Decisions") in `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`
- **Scope Boundary Rule** (expanded from Stage Boundary Rule) in `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE.md`

---

# What We Learned: Cross-Layer Stage References

<!-- section_id: "95378992-96b8-4532-90ff-b6c83a5efd75" -->
## Discovery Date
2026-02-19

<!-- section_id: "e8174acc-33a0-4152-af4b-207359d03603" -->
## The Pattern

When content at one layer becomes detailed enough to warrant its own entity (child layer), both layers must maintain **bidirectional references** between their stages.

<!-- section_id: "a6b3f197-721f-4bb7-a55d-8a4c064388e0" -->
### Parent → Child (downward)
Parent layer stages have "Child Layer Detail" sections that map their content to child entity stages where the detailed work lives. Example: stage 01 branch "delegation_model" maps to memory_system stage 02 research topics and multi_agent_system stage 04 design decisions.

<!-- section_id: "ea176b16-28d9-4303-85aa-12bb3d61f923" -->
### Child → Parent (upward)
Child entities have "Parent Layer Context" sections in their 0AGNOSTIC.md that point back to parent stages providing broader context. A memory_system agent can find the original requirement (parent stage 01), the research context (parent stage 02), and the design rationale (parent stage 04).

<!-- section_id: "ae97c1be-ce51-4ae7-8273-dd19de2e57a1" -->
## When to Push to a Child Layer

Not every topic warrants its own entity. Decision factors:

| Stay at current layer | Push to child layer |
|----------------------|---------------------|
| Few files, shallow depth | Multiple files, deep investigation |
| Tightly coupled to parent | Can be worked on independently |
| Needs 1-2 stages | Needs its own full stage progression |
| Same agent handles it | Needs a specialized agent |

<!-- section_id: "6546a7cb-42e8-4907-8880-a625407dbb14" -->
## Why This Matters

Without bidirectional references:
- Parent agents don't know where detailed work lives (they explore blindly)
- Child agents lack context on WHY their entity exists (they miss the bigger picture)
- Cross-layer navigation requires traversing the entire hierarchy

With bidirectional references:
- Parent agents can orient immediately ("branch X is detailed at child entity Y, stages Z")
- Child agents can look up original requirements and design rationale at the parent level
- Navigation is direct — one hop instead of a full traversal

<!-- section_id: "7fa59ff6-8cc6-43df-a06f-8658a48924f2" -->
## Where This Is Codified

- **Principle 10** ("Cross-Layer Stage References") in `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`
- **Tree of knowledge topic**: `.0agnostic/01_knowledge/tree_of_knowledge/00_agent_delegation_knowledge/02_patterns_and_principles/cross_layer_stage_references.md`
- Applied at: agent_delegation_system stages 01-06 (downward), memory_system, multi_agent_system, context_chain_system (upward)
