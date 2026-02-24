# Scope Boundary Rule

**Type**: Static (always applies)
**Scope**: All agents across all entities
**Previously**: "Stage Boundary Rule" — expanded to cover layer boundaries too

## Rule

An agent MUST NOT perform work that belongs to another stage or another layer/entity without making an explicit **scope decision**.

Scope boundaries exist at two levels:
- **Stage boundaries**: Work belonging to another stage within the same entity (e.g., designing in stage 01, or coding in stage 04)
- **Layer boundaries**: Work belonging to a sibling entity, parent entity, or child entity (e.g., a memory_system agent doing multi_agent_system work)

## The Scope Decision

When an agent encounters out-of-scope work, it evaluates:

| Factor | Favor doing it yourself | Favor delegating |
|--------|------------------------|-----------------|
| Size of work | Small (1 note, 1 flag) | Significant (multiple files, complex reasoning) |
| Coupling | Tightly coupled to current task | Loosely coupled or independent |
| Context window | Plenty of room | Already loaded with in-scope context |
| Agent exists? | No agent for target scope | Agent already exists and can be messaged |
| Domain knowledge | You already have the needed context | Would need to load new domain knowledge |

**Default**: delegate. The cost of spawning an agent is low; the cost of a bloated, confused context is high.

## Stage Boundary Examples

| If you're in... | And you find yourself... | Decision |
|-----------------|------------------------|----------|
| Stage 01 (request gathering) | Designing a solution | Note the design need, hand off to stage 04 |
| Stage 02 (research) | Making architecture decisions | Present options, hand off to stage 04 |
| Stage 04 (design) | Writing implementation code | Document the design, hand off to stage 06 |
| Stage 06 (development) | Redesigning the architecture | Flag the design issue, hand off to stage 04 |
| Stage 07 (testing) | Fixing a bug you found | Document the failure, hand off to stage 09 |

## Layer Boundary Examples

| If you're in... | And you find yourself... | Decision |
|-----------------|------------------------|----------|
| memory_system entity | Designing orchestration patterns | That's multi_agent_system's scope — delegate or flag |
| context_chain_system (layer 3) | Changing universal rules (layer 0) | Propose the change, escalate to layer 0 manager |
| A child entity | Making decisions for the parent | Document the recommendation, escalate to parent manager |

## Instantiation Decision

When no agent exists for the target scope:

1. **Significant work** → Instantiate a new agent: spawn it with a Task tool call pointing to the target 0AGNOSTIC.md
2. **Trivial work** → Document it in your stage report for the manager to route later
3. **Unsure** → Ask the manager or user — instantiating has overhead, so it should be justified

## Rationale

Scope boundaries prevent:
- **Context overflow**: One agent trying to hold everything from multiple domains/stages
- **Scope creep**: One agent doing everything poorly instead of its job well
- **Lost context**: Work done in the wrong stage/entity becomes unfindable
- **Skipped validation**: Building without designing, or deploying without testing

## Enforcement

The entity manager verifies stage reports for out-of-scope work. The `/stage-workflow` skill checks stage boundaries when transitioning between stages.
