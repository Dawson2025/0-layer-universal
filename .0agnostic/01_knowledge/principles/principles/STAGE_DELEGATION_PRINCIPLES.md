---
resource_id: "fd74fa0e-fe35-478c-baad-48e7c444dc79"
resource_type: "knowledge"
resource_name: "STAGE_DELEGATION_PRINCIPLES"
---
# Stage Delegation Principles

These principles govern how agents delegate and operate across the layer-stage hierarchy.

<!-- section_id: "849c6344-193e-4544-aeab-49bea3d5930f" -->
## 1. Managers Delegate, Agents Operate

Entity managers maintain the big picture. Stage agents do the work. A manager reads stage reports and decides what to delegate next — it does not carry operational methodology for any stage.

<!-- section_id: "2a6c8e3d-8895-40a7-aadd-6462295c691f" -->
## 2. Explicit Scope Boundaries (Layer AND Stage)

Every agent knows what it IS and what it IS NOT. Scope boundaries exist at **two levels**:

- **Layer boundaries**: Each entity (feature, sub-feature, etc.) has a scope defined in its 0AGNOSTIC.md. Work belonging to a sibling or parent entity is out of scope.
- **Stage boundaries**: Each stage (01-11) within an entity has a scope. Work belonging to another stage is out of scope.

The "NOT" list is as important as the "IS" description. When work falls outside either boundary, the agent must make a **scope decision** (see Principle 8).

<!-- section_id: "39e75665-135b-49dd-8c53-2c45b91f1baf" -->
## 3. Three-Tier Knowledge

Knowledge flows through three tiers:
- **Pointers** (0AGNOSTIC.md) — what this entity IS, where things are
- **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, key docs
- **Full** (stage outputs) — complete research, design specs, test results

Managers work at the pointer tier. Stage agents load distilled knowledge on demand. Full detail stays within stages.

<!-- section_id: "71e85a68-4aa2-4fd9-b778-511c76c06e66" -->
## 4. Stage Reports Are the Communication Channel

Stage agents communicate with managers through stage reports, not through shared context. The report is the async handoff — it tells the manager what was done, what's left, and what the next stage needs.

<!-- section_id: "9b11dadb-6532-4e52-bf87-1feea8231e99" -->
## 5. Stages Are Reentrant

Stages can be entered multiple times. Research can loop back from design. Testing can loop through criticism and fixing. Requirements can be revised after criticism. Each reentry starts by reading the stage's current state (0AGNOSTIC.md, existing outputs, stage report).

<!-- section_id: "668d74d2-d090-498b-991d-b56c6c4ea45e" -->
## 6. Output-First, Not Process-First

Stage agents produce deliverables, not process logs. The value is in the outputs/ directory — the requirements, research findings, design specs, test results. Process notes are secondary.

<!-- section_id: "8dcc374e-5348-4db3-846d-bd6ab439f68b" -->
## 7. Selective Context Loading

Never load all parent knowledge at once. Read the specific file relevant to the task at hand. Context windows are finite — every byte loaded must earn its place.

<!-- section_id: "82e1ea8d-3892-4965-a19c-bc94b9e38709" -->
## 8. Scope Boundary Decisions

When an agent reaches the boundary of its layer or stage scope, it must make a **delegation decision** that includes both WHAT to do and WHERE to go.

<!-- section_id: "0ee24d7a-5b1f-40df-801a-664dbc31ebe7" -->
### Step 1: Determine Direction

Every scope boundary has a direction. The agent must identify which way the out-of-scope work points:

| Direction | Meaning | Example |
|-----------|---------|---------|
| **Up** | Work belongs to a parent or ancestor entity | Stage agent finds entity-level policy issue |
| **Down** | Work belongs to a child or descendant entity | Entity agent finds work that needs a specialized sub-feature |
| **Left** | Work belongs to an earlier stage (lower number) | Design agent discovers missing requirements → stage 01 |
| **Right** | Work belongs to a later stage (higher number) | Research agent makes an architecture decision → stage 04 |
| **Sideways (layer)** | Work belongs to a sibling entity at the same layer | memory_system agent finds multi_agent_system concern |
| **Multi-location** | Work spans multiple layers, stages, or entities | Refactoring that requires research + design + development |

<!-- section_id: "2df7a7ca-ee2d-4460-a020-41e4c8eb9587" -->
### Step 2: Decide How to Handle

| Question | If Yes | If No |
|----------|--------|-------|
| Is the out-of-scope work small and tightly coupled to my current work? | Do it yourself across stages/layers, but document what you touched outside your scope | Delegate to the responsible agent |
| Does an agent already exist for the target layer/stage? | Delegate to it (send message, create task, or write handoff) | Consider instantiating one |
| Would handling this myself overflow my context window? | Always delegate — context window preservation is paramount | You may handle it if it's small |

<!-- section_id: "c17728f7-6229-455a-9835-23044d3c597d" -->
### Step 3: Communicate

How the agent communicates depends on the direction and the handling decision:

| Situation | Communication Method |
|-----------|---------------------|
| Delegating **up** (to parent/ancestor) | Write finding in stage report; if urgent, escalate to entity manager directly |
| Delegating **down** (to child/descendant) | Spawn agent with Task tool pointing to child's 0AGNOSTIC.md + task description |
| Delegating **left/right** (to sibling stage) | Document in stage report with cross-reference; manager routes in next delegation cycle |
| Delegating **sideways** (to sibling entity) | Document in stage report; entity manager coordinates with sibling entity's manager |
| **Multi-location** work | Escalate to the nearest common ancestor manager who can coordinate across all locations |
| Doing it **yourself** across boundaries | Document ALL out-of-scope changes in your stage report with exact paths and rationale |

<!-- section_id: "86eee15f-29bc-4396-b07f-2919694ab06b" -->
### Instantiation Decision

When no agent exists for the target scope:
1. **If the work is significant** (multiple files, complex reasoning): Instantiate a new agent for that layer/stage by spawning it with a pointer to the target 0AGNOSTIC.md
2. **If the work is trivial** (one note, one flag): Document it in your stage report for the manager to route later
3. **If you're unsure**: Ask the manager (or user) — instantiating agents has overhead, so it should be justified

When instantiating:
- The new agent reads its own 0AGNOSTIC.md to self-orient (not YOUR context)
- Provide a clear task description + any findings that prompted the instantiation
- The new agent may itself hit scope boundaries and make its own delegation decisions

<!-- section_id: "5da20d18-1303-42a4-8aef-3f5553da6e16" -->
### Multi-Location Work

When work genuinely spans multiple locations (not just a clean handoff to one place):

1. **Can one agent orchestrate it?** If you're the entity manager and the work spans your stages, coordinate it yourself — spawn stage agents as needed
2. **Does it span sibling entities?** Escalate to the parent entity manager who has scope over both siblings
3. **Does it span layers?** Escalate to the nearest ancestor with scope over all affected layers
4. **Should you work across multiple stages yourself?** Only if ALL are small, tightly coupled, AND you have context window headroom. Otherwise, delegate to each stage's agent and let the manager coordinate

The key question for multi-location: **who has the scope to see all affected locations?** That's the agent who should coordinate.

<!-- section_id: "ab945e3c-3f3b-42b9-98c8-e72022d380c8" -->
### Why This Matters

Context windows are the fundamental constraint. An agent that tries to work across too many layers/stages will:
- Lose track of its own scope and methodology
- Overflow its context window with knowledge from multiple domains
- Produce lower-quality work in each area than a specialized agent would
- Make outputs harder to find (work done in the wrong stage is unfindable)

The default should be **delegate**, not **do it yourself**. The cost of spawning an agent is low; the cost of a bloated, confused context is high.

<!-- section_id: "623f060b-1b8e-4287-b30a-6fc2795e67a3" -->
## 9. Two-Halves Context Pattern

Every 0AGNOSTIC.md (whether for an entity or a stage) needs **two halves**:

<!-- section_id: "d76ae077-6ca4-4e31-ad74-252a9c22e2af" -->
### Half 1: Operational Guidance (written once, rarely changes)
- **Identity**: Role, scope, parent reference, domain
- **Scope boundaries**: What this IS and IS NOT (the NOT list is critical)
- **Methodology**: How the agent works
- **Domain context pointers**: Where to find parent knowledge (point, don't load)
- **Success criteria**: When is this done?
- **Exit protocol**: What to do before leaving

<!-- section_id: "ab99edfd-c98c-459d-b966-58d28e065509" -->
### Half 2: Current State Summary (updated as work progresses)
- **Status**: pending / active / complete / scaffolded
- **Summary**: 2-3 sentences on what's been accomplished
- **Key outputs**: Named files/structures with brief descriptions
- **Key findings**: Distilled insights (conclusions, not process)
- **Open items**: What's unresolved — specific and actionable
- **Handoff**: Ready for next stage? What should next stage prioritize?

<!-- section_id: "36fc90ef-b5d9-4642-af62-8a69685596b7" -->
### Why Both Halves Are Needed

Without the current state half, an agent landing in a stage must explore outputs/ manually to understand what exists — wasting context window tokens on orientation instead of productive work.

The operational half tells the agent **how to work**. The current state half tells the agent **what's already here**. Together, they make the pointer tier functional: 0AGNOSTIC.md is the single file an agent reads to be immediately oriented and productive.

<!-- section_id: "89b48c02-dddb-40bc-a1de-8f771969c81e" -->
## 10. Cross-Layer Stage References

When content at one layer becomes detailed enough to warrant its own entity (child layer), both layers must maintain **bidirectional references** between their stages.

<!-- section_id: "ae2b9711-b458-4bd5-a111-ac5b30346287" -->
### The Pattern

- **Parent layer stages → child**: Overviews and summaries pointing to child entity stages where the detailed work lives. The parent stage is the "pointer tier" for its child's stages.
- **Child layer → parent stages**: References back to the parent layer stages that provide broader context, the original requirement, or the design decision being implemented.

<!-- section_id: "ed089f69-412c-4e16-a4a2-857a72068fb2" -->
### When to Push to a Child Layer

| Factor | Stay at current layer | Push to child layer |
|--------|----------------------|---------------------|
| Depth of detail | A few files, shallow | Multiple files, deep investigation |
| Scope independence | Tightly coupled to parent | Can be worked on independently |
| Stage breadth | Needs 1-2 stages | Needs its own full stage progression (01-11) |
| Agent specialization | Same agent handles it | Needs a specialized agent with domain knowledge |

<!-- section_id: "f3ac10ec-4741-40ca-b1f7-e9e64ef4d61a" -->
### Bidirectional References

**Parent pointing down** (in parent stage 0AGNOSTIC.md):

| Branch/Need | Child Entity | Child Stages with Detail | Path |
|-------------|-------------|-------------------------|------|
| Branch 02 | memory_system | Stages 01-07 active | `child_entity/layer_N_group/layer_N_99_stages/` |

**Child pointing up** (in child entity 0AGNOSTIC.md):

| Parent Stage | What It Provides | Path |
|-------------|-----------------|------|
| Stage 01 (needs) | Original requirements this entity details | `parent_entity/.../stage_NN/` |
| Stage 04 (design) | Design decisions governing this entity | `parent_entity/.../stage_NN/` |

<!-- section_id: "a30c478e-ad9d-40f0-9aff-d587d76d3169" -->
### Why Both Directions

- **Parent → child**: Managers reading the parent layer can find where detailed work lives without discovering child entities by exploration
- **Child → parent**: Agents in child entities can navigate up to understand the broader context and the original need they're addressing
- **Cross-stage traceability extends across layers**: A need at the parent layer connects to research/design/development at the child layer

Without bidirectional references, agents either don't know child layers exist (lost detail) or don't know where their work fits (lost context).

<!-- section_id: "9eeb1530-4105-4a17-8174-2ce9bf49e053" -->
## Canonical Workspace

These principles are maintained at the **agent_delegation_system** entity:

`layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/`

Changes to agent delegation principles should be researched (stage 02), designed (stage 04), and developed (stage 06) there, then propagated to this universal artifact via the entity's consolidation funnel. See the update protocol at that entity's `.0agnostic/03_protocols/agent_delegation_update_protocol.md`.
