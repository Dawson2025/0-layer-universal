---
resource_id: "ac9b14dd-f414-4cd2-a159-b87397447749"
resource_type: "rule"
resource_name: "STAGE_BOUNDARY_RULE"
---
# Scope Boundary Rule

**Type**: Static (always applies)
**Scope**: All agents across all entities
**Previously**: "Stage Boundary Rule" — expanded to cover layer boundaries, directional traversal, and multi-location work
**Detailed framework**: See Principle 8 in `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md`

## Rule

An agent MUST NOT perform work that belongs to another stage or another layer/entity without making an explicit **scope decision** that covers: (1) which direction the work points, (2) whether to do it yourself or delegate, (3) how to communicate the decision.

Scope boundaries exist at two levels:
- **Stage boundaries**: Work belonging to another stage within the same entity (e.g., designing in stage 01, or coding in stage 04)
- **Layer boundaries**: Work belonging to a sibling entity, parent entity, or child entity (e.g., a memory_system agent doing multi_agent_system work)

## Step 1: Identify Direction

| Direction | What it means | Go to... |
|-----------|--------------|----------|
| **Up** | Parent/ancestor entity scope | Parent entity's manager or relevant stage |
| **Down** | Child/descendant entity scope | Child entity's 0AGNOSTIC.md (spawn agent if needed) |
| **Left** | Earlier stage (lower number) | Sibling stage within same entity (e.g., stage 04 → stage 01) |
| **Right** | Later stage (higher number) | Sibling stage within same entity (e.g., stage 02 → stage 04) |
| **Sideways** | Sibling entity at same layer | Sibling entity's manager (coordinated by parent) |
| **Multi-location** | Spans multiple directions | Escalate to nearest common ancestor with scope over all locations |

## Step 2: Decide — Do It Yourself or Delegate

| Factor | Favor doing it yourself | Favor delegating |
|--------|------------------------|-----------------|
| Size of work | Small (1 note, 1 flag) | Significant (multiple files, complex reasoning) |
| Coupling | Tightly coupled to current task | Loosely coupled or independent |
| Context window | Plenty of room | Already loaded with in-scope context |
| Agent exists? | No agent for target scope | Agent already exists and can be messaged |
| Domain knowledge | You already have the needed context | Would need to load new domain knowledge |

**Default**: delegate. The cost of spawning an agent is low; the cost of a bloated, confused context is high.

## Step 3: Communicate

| Direction | Communication method |
|-----------|---------------------|
| Up | Stage report (async) or direct escalation to entity manager (urgent) |
| Down | Spawn agent via Task tool with pointer to target 0AGNOSTIC.md + task |
| Left/Right | Document in stage report; entity manager routes in next cycle |
| Sideways | Document in stage report; entity manager coordinates with sibling's manager |
| Multi-location | Escalate to common ancestor manager who coordinates all locations |
| Did it yourself | Document ALL out-of-scope changes in stage report with paths and rationale |

## Stage Boundary Examples

| If you're in... | And you find yourself... | Direction | Decision |
|-----------------|------------------------|-----------|----------|
| Stage 01 (request gathering) | Designing a solution | Right → 04 | Note the design need, hand off to stage 04 |
| Stage 02 (research) | Making architecture decisions | Right → 04 | Present options, hand off to stage 04 |
| Stage 04 (design) | Writing implementation code | Right → 06 | Document the design, hand off to stage 06 |
| Stage 06 (development) | Redesigning the architecture | Left → 04 | Flag the design issue, hand off to stage 04 |
| Stage 07 (testing) | Fixing a bug you found | Right → 09 | Document the failure, hand off to stage 09 |
| Stage 04 (design) | Needs missing requirements AND implementation | Multi | Escalate to entity manager to coordinate stages 01 + 06 |

## Layer Boundary Examples

| If you're in... | And you find yourself... | Direction | Decision |
|-----------------|------------------------|-----------|----------|
| memory_system entity | Designing orchestration patterns | Sideways | That's multi_agent_system's scope — delegate or flag |
| context_chain_system (layer 3) | Changing universal rules (layer 0) | Up | Propose the change, escalate to layer 0 manager |
| A child entity | Making decisions for the parent | Up | Document the recommendation, escalate to parent manager |
| Entity manager | Finding work needs a specialized sub-feature | Down | Instantiate child entity agent or delegate to existing one |
| Entity manager | Refactoring spans research + design + dev | Multi | Coordinate yourself (you have scope over your stages) |

## Instantiation Decision

When no agent exists for the target scope:

1. **Significant work** → Instantiate a new agent: spawn it with a Task tool call pointing to the target 0AGNOSTIC.md
2. **Trivial work** → Document it in your stage report for the manager to route later
3. **Unsure** → Ask the manager or user — instantiating has overhead, so it should be justified

When instantiating, provide: (1) pointer to target 0AGNOSTIC.md, (2) clear task description, (3) any findings that prompted the delegation. The new agent self-orients from its own 0AGNOSTIC.md — do not dump your context into it.

## Rationale

Scope boundaries prevent:
- **Context overflow**: One agent trying to hold everything from multiple domains/stages
- **Scope creep**: One agent doing everything poorly instead of its job well
- **Lost context**: Work done in the wrong stage/entity becomes unfindable
- **Skipped validation**: Building without designing, or deploying without testing

## Enforcement

The entity manager verifies stage reports for out-of-scope work. The `/stage-workflow` skill checks stage boundaries when transitioning between stages.

## Canonical Workspace

This rule is maintained at the **agent_delegation_system** entity:

`layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/`

Changes to scope boundary rules should be researched (stage 02), designed (stage 04), and developed (stage 06) there, then propagated to this universal artifact via the entity's consolidation funnel. See the update protocol at that entity's `.0agnostic/03_protocols/agent_delegation_update_protocol.md`.
