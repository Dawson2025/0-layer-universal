# Scope Boundary Traversal Patterns

## Research Question

When an agent hits a scope boundary (work outside its layer or stage), what information does it need to make the right traversal decision? What are the directional patterns, and what communication infrastructure must every agent have?

This matters because the minimal context model says agents get compact neighbor interfaces — but if scope boundary decisions require substantial knowledge about the hierarchy, traversal patterns, and communication protocols, that "compact" interface may need to be larger than initially assumed.

## Findings

### Every Agent Needs Traversal Infrastructure

Regardless of the minimal context model, every agent must know:

1. **Direction identification**: Which way does the out-of-scope work point? Up (parent/ancestor), down (child/descendant), left (earlier stage), right (later stage), sideways (sibling entity), or multi-location (spans several).

2. **Handling decision framework**: For the identified direction, should the agent do it itself, delegate to an existing agent, or instantiate a new one? The factors are: size, coupling, context window headroom, agent existence, domain knowledge.

3. **Communication protocol per direction**: How to actually communicate the decision. Up → stage report or escalation. Down → spawn agent with Task tool. Left/right → stage report for manager routing. Sideways → stage report for entity manager coordination. Multi-location → escalate to nearest common ancestor.

4. **Positional awareness**: Who is my parent? Who are my children? Who are my stage siblings? What does each provide/accept?

5. **Instantiation knowledge**: How to spawn a new agent (point to target 0AGNOSTIC.md + task description). When to instantiate vs. document for later routing.

### The Key Insight: Infrastructure vs. Content

This traversal knowledge falls into two categories:

**Universal infrastructure** (same for every agent, written once):
- The directional framework itself (up/down/left/right/sideways/multi)
- The handling decision factors (size, coupling, context window, etc.)
- The communication protocol per direction
- The instantiation procedure

**Per-agent positional content** (unique to each agent's position):
- Who MY specific parent/children/siblings are
- What MY specific neighbors provide/accept
- What topics I escalate vs. delegate down

The universal infrastructure is substantial but **shared** — it lives in Principle 8 and the Scope Boundary Rule, loaded on-demand when an agent hits a boundary. It does NOT need to be in every agent's STATIC context.

The per-agent positional content is compact — it's the Inputs/Outputs tables and Navigation sections already in 0AGNOSTIC.md.

### Multi-Location Work: The Hard Case

When work spans multiple locations simultaneously (not a clean handoff to one place):

- The question becomes: **who has scope to see all affected locations?**
- If the work spans stages within one entity → the entity manager coordinates
- If the work spans sibling entities → the parent entity manager coordinates
- If the work spans layers → the nearest common ancestor coordinates

This is a recursive pattern: escalate until you find an agent whose scope covers all affected locations. That agent then coordinates by delegating to individual agents at each location.

### Connection to Minimal Context Model

The scope boundary framework does NOT contradict the minimal context model:

- **Universal infrastructure** (Principle 8, Scope Boundary Rule) is loaded on-demand when boundary is hit — not pre-loaded into every agent's STATIC
- **Positional awareness** (parent/children/neighbors) IS in STATIC but is compact (few lines per neighbor)
- **Routing intelligence** lives in managers, not in every agent — a stage agent doesn't need a full hierarchy map, just knowledge of its direct parent to escalate to

The minimal context model holds: own STATIC (including compact positional awareness) + on-demand rules (Principle 8, Scope Boundary Rule when boundary hit) + delegation to managers for routing.

## Promoted Artifacts

These findings have been promoted to universal artifacts:

| Artifact | Location | What was promoted |
|----------|----------|-------------------|
| Principle 8 (expanded) | `.0agnostic/01_knowledge/principles/principles/STAGE_DELEGATION_PRINCIPLES.md` | Directional framework, communication protocol per direction, multi-location section |
| Scope Boundary Rule (expanded) | `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE/STAGE_BOUNDARY_RULE.md` | 3-step structure (direction → decide → communicate), direction column in examples, multi-location examples |

## Date

2026-02-26
