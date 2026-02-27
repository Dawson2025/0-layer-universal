# Stage Delegation Principles

These principles govern how agents delegate and operate across the layer-stage hierarchy.

## 1. Managers Delegate, Agents Operate

Entity managers maintain the big picture. Stage agents do the work. A manager reads stage reports and decides what to delegate next — it does not carry operational methodology for any stage.

## 2. Explicit Scope Boundaries (Layer AND Stage)

Every agent knows what it IS and what it IS NOT. Scope boundaries exist at **two levels**:

- **Layer boundaries**: Each entity (feature, sub-feature, etc.) has a scope defined in its 0AGNOSTIC.md. Work belonging to a sibling or parent entity is out of scope.
- **Stage boundaries**: Each stage (01-11) within an entity has a scope. Work belonging to another stage is out of scope.

The "NOT" list is as important as the "IS" description. When work falls outside either boundary, the agent must make a **scope decision** (see Principle 8).

## 3. Three-Tier Knowledge

Knowledge flows through three tiers:
- **Pointers** (0AGNOSTIC.md) — what this entity IS, where things are
- **Distilled** (.0agnostic/01_knowledge/) — domain knowledge, principles, key docs
- **Full** (stage outputs) — complete research, design specs, test results

Managers work at the pointer tier. Stage agents load distilled knowledge on demand. Full detail stays within stages.

## 4. Stage Reports Are the Communication Channel

Stage agents communicate with managers through stage reports, not through shared context. The report is the async handoff — it tells the manager what was done, what's left, and what the next stage needs.

## 5. Stages Are Reentrant

Stages can be entered multiple times. Research can loop back from design. Testing can loop through criticism and fixing. Requirements can be revised after criticism. Each reentry starts by reading the stage's current state (0AGNOSTIC.md, existing outputs, stage report).

## 6. Output-First, Not Process-First

Stage agents produce deliverables, not process logs. The value is in the outputs/ directory — the requirements, research findings, design specs, test results. Process notes are secondary.

## 7. Selective Context Loading

Never load all parent knowledge at once. Read the specific file relevant to the task at hand. Context windows are finite — every byte loaded must earn its place.

## 8. Scope Boundary Decisions

When an agent reaches the boundary of its layer or stage scope, it must make a **delegation decision** that includes both WHAT to do and WHERE to go.

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

### Step 2: Decide How to Handle

| Question | If Yes | If No |
|----------|--------|-------|
| Is the out-of-scope work small and tightly coupled to my current work? | Do it yourself across stages/layers, but document what you touched outside your scope | Delegate to the responsible agent |
| Does an agent already exist for the target layer/stage? | Delegate to it (send message, create task, or write handoff) | Consider instantiating one |
| Would handling this myself overflow my context window? | Always delegate — context window preservation is paramount | You may handle it if it's small |

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

### Instantiation Decision

When no agent exists for the target scope:
1. **If the work is significant** (multiple files, complex reasoning): Instantiate a new agent for that layer/stage by spawning it with a pointer to the target 0AGNOSTIC.md
2. **If the work is trivial** (one note, one flag): Document it in your stage report for the manager to route later
3. **If you're unsure**: Ask the manager (or user) — instantiating agents has overhead, so it should be justified

When instantiating:
- The new agent reads its own 0AGNOSTIC.md to self-orient (not YOUR context)
- Provide a clear task description + any findings that prompted the instantiation
- The new agent may itself hit scope boundaries and make its own delegation decisions

### Multi-Location Work

When work genuinely spans multiple locations (not just a clean handoff to one place):

1. **Can one agent orchestrate it?** If you're the entity manager and the work spans your stages, coordinate it yourself — spawn stage agents as needed
2. **Does it span sibling entities?** Escalate to the parent entity manager who has scope over both siblings
3. **Does it span layers?** Escalate to the nearest ancestor with scope over all affected layers
4. **Should you work across multiple stages yourself?** Only if ALL are small, tightly coupled, AND you have context window headroom. Otherwise, delegate to each stage's agent and let the manager coordinate

The key question for multi-location: **who has the scope to see all affected locations?** That's the agent who should coordinate.

### Why This Matters

Context windows are the fundamental constraint. An agent that tries to work across too many layers/stages will:
- Lose track of its own scope and methodology
- Overflow its context window with knowledge from multiple domains
- Produce lower-quality work in each area than a specialized agent would
- Make outputs harder to find (work done in the wrong stage is unfindable)

The default should be **delegate**, not **do it yourself**. The cost of spawning an agent is low; the cost of a bloated, confused context is high.

## 9. Two-Halves Context Pattern

Every 0AGNOSTIC.md (whether for an entity or a stage) needs **two halves**:

### Half 1: Operational Guidance (written once, rarely changes)
- **Identity**: Role, scope, parent reference, domain
- **Scope boundaries**: What this IS and IS NOT (the NOT list is critical)
- **Methodology**: How the agent works
- **Domain context pointers**: Where to find parent knowledge (point, don't load)
- **Success criteria**: When is this done?
- **Exit protocol**: What to do before leaving

### Half 2: Current State Summary (updated as work progresses)
- **Status**: pending / active / complete / scaffolded
- **Summary**: 2-3 sentences on what's been accomplished
- **Key outputs**: Named files/structures with brief descriptions
- **Key findings**: Distilled insights (conclusions, not process)
- **Open items**: What's unresolved — specific and actionable
- **Handoff**: Ready for next stage? What should next stage prioritize?

### Why Both Halves Are Needed

Without the current state half, an agent landing in a stage must explore outputs/ manually to understand what exists — wasting context window tokens on orientation instead of productive work.

The operational half tells the agent **how to work**. The current state half tells the agent **what's already here**. Together, they make the pointer tier functional: 0AGNOSTIC.md is the single file an agent reads to be immediately oriented and productive.

## 10. Cross-Layer Stage References

When content at one layer becomes detailed enough to warrant its own entity (child layer), both layers must maintain **bidirectional references** between their stages.

### The Pattern

- **Parent layer stages → child**: Overviews and summaries pointing to child entity stages where the detailed work lives. The parent stage is the "pointer tier" for its child's stages.
- **Child layer → parent stages**: References back to the parent layer stages that provide broader context, the original requirement, or the design decision being implemented.

### When to Push to a Child Layer

| Factor | Stay at current layer | Push to child layer |
|--------|----------------------|---------------------|
| Depth of detail | A few files, shallow | Multiple files, deep investigation |
| Scope independence | Tightly coupled to parent | Can be worked on independently |
| Stage breadth | Needs 1-2 stages | Needs its own full stage progression (01-11) |
| Agent specialization | Same agent handles it | Needs a specialized agent with domain knowledge |

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

### Why Both Directions

- **Parent → child**: Managers reading the parent layer can find where detailed work lives without discovering child entities by exploration
- **Child → parent**: Agents in child entities can navigate up to understand the broader context and the original need they're addressing
- **Cross-stage traceability extends across layers**: A need at the parent layer connects to research/design/development at the child layer

Without bidirectional references, agents either don't know child layers exist (lost detail) or don't know where their work fits (lost context).
