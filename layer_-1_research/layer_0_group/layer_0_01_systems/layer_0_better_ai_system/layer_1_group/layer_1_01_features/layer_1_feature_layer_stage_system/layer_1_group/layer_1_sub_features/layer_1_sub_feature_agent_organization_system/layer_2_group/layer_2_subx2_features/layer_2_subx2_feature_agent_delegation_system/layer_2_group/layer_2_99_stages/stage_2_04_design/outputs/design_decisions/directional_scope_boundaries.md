---
resource_id: "5d16311e-7c09-4315-be1f-5a9eb0864297"
resource_type: "output"
resource_name: "directional_scope_boundaries"
---
# Design Decision: Directional Scope Boundary Framework

<!-- section_id: "9b1d14e3-5b21-402c-9e46-20f147b5f0a8" -->
## Decision

Expand the scope boundary decision framework (Principle 8) from a simple "do it yourself / delegate / instantiate" choice into a three-step process: (1) identify direction, (2) decide how to handle, (3) communicate per direction. Add explicit support for multi-location work that spans multiple layers, stages, or entities simultaneously.

<!-- section_id: "510bc9b5-41ec-4dce-8fe1-08c0a6a47bd7" -->
## Status

**Decided** — 2026-02-26

<!-- section_id: "d9ca8f30-08c7-4799-9b9a-d4f9af29ec80" -->
## Context

The original Principle 8 and Scope Boundary Rule defined three options (do it yourself, delegate, instantiate) and examples for stage and layer boundaries. But they lacked:

- **Directional awareness**: No framework for identifying WHETHER to go up, down, left, right, or sideways
- **Communication per direction**: No guidance on HOW to communicate differently depending on direction (escalate up vs. spawn down vs. report sideways)
- **Multi-location work**: No handling for work that spans multiple locations simultaneously
- **Infrastructure vs. content distinction**: No clarity on what is universal (same for all agents) vs. per-agent (unique to position)

This gap was identified when analyzing what agents truly need in their context: the minimal context model says "compact neighbor interfaces," but agents also need the traversal framework itself.

<!-- section_id: "f9f1acab-3a88-497b-897c-e5d87bfa098e" -->
## The Design

<!-- section_id: "cb02cf46-648c-49fa-80fa-0db4aca1484c" -->
### Three-Step Scope Decision

1. **Identify direction**: Up (parent/ancestor), down (child/descendant), left (earlier stage), right (later stage), sideways (sibling entity), multi-location (spans several)

2. **Decide how to handle**: Same factors as before — size, coupling, context window, agent existence, domain knowledge. Default: delegate.

3. **Communicate per direction**: Each direction has a specific communication method:
   - Up → stage report or escalation
   - Down → spawn agent with Task tool
   - Left/right → stage report, manager routes
   - Sideways → stage report, entity manager coordinates
   - Multi-location → escalate to nearest common ancestor
   - Did it yourself → document all out-of-scope changes

<!-- section_id: "1bc07c06-1b4b-45f3-8801-1c3d6765efe3" -->
### Multi-Location Coordination

The key question: **who has scope to see all affected locations?**

- Stages within one entity → entity manager coordinates
- Sibling entities → parent entity manager coordinates
- Across layers → nearest common ancestor coordinates

This is recursive — escalate until scope covers all locations, then that manager delegates to individual agents at each location.

<!-- section_id: "22b2db04-aa3f-4359-871d-cb58bb4d8603" -->
### Where This Lives

| Content | Where | How loaded |
|---------|-------|-----------|
| Directional framework (universal) | Principle 8, Scope Boundary Rule | On-demand — when agent hits boundary |
| Positional awareness (per-agent) | Own 0AGNOSTIC.md Inputs/Outputs/Navigation | Always — in STATIC |
| Routing intelligence | Entity managers | Managers have scope over their stages/children |

This separation confirms the minimal context model: the framework is loaded on-demand, the positional awareness is compact STATIC, and routing is delegated to managers.

<!-- section_id: "8a1dcaba-c623-4dfb-9870-dc06e1d4b94d" -->
## Alternatives Considered

<!-- section_id: "819af537-520d-4df5-89f8-98ba0da52117" -->
### Every Agent Carries Full Hierarchy Map

Give every agent a complete map of the entire entity tree with all agents, their scopes, and routing paths.

**Rejected because**: Violates minimal context. Most of the map is irrelevant to any single agent. The relay pattern (ask your parent, who asks their parent) achieves the same routing without pre-loading the full map.

<!-- section_id: "da028221-b254-482a-9d9e-0c1594c4fa52" -->
### Direction-Agnostic Decision (Status Quo)

Keep the original three-option framework without directional awareness.

**Rejected because**: Agents were making scope decisions without knowing the right communication method. Escalating up requires a stage report; delegating down requires spawning an agent. Without directional awareness, agents used the wrong communication method.

<!-- section_id: "81b4ef35-65e9-483e-a1f2-ef0c0c413274" -->
### Separate Rules Per Direction

Create individual rules for up-traversal, down-traversal, left/right-traversal, etc.

**Rejected because**: The decision framework is the same regardless of direction — only the communication method differs. A single rule with a direction table is cleaner than 5 separate rules.

<!-- section_id: "72b57d4d-3061-4495-a56e-069fb37f446d" -->
## Trade-offs Accepted

1. **Slightly more complex rule**: The 3-step process is more to learn than the old 3-option choice. Justified because the old rule was underspecified — agents didn't know HOW to communicate their decisions.

2. **Manager bottleneck for multi-location**: All multi-location work routes through the nearest common ancestor manager. If managers are overloaded, this creates a bottleneck. Mitigated by: managers coordinate (decide who does what) but don't execute — they delegate back to specialized agents.

3. **Multi-location still requires judgment**: "Escalate to nearest common ancestor" is a pattern, not a mechanical rule. Agents must judge what counts as multi-location vs. a clean handoff with a side note. This is intentional — mechanical rules for nuanced decisions produce worse outcomes than judgment-based frameworks.

<!-- section_id: "29db9e42-f7ae-4505-ba22-8ae3f916512a" -->
## Cross-Stage Traceability

| Stage | Connection |
|-------|-----------|
| Stage 01 (Requirements) | need_01: stage_delegation — how agents cross boundaries |
| Stage 01 (Requirements) | need_02: stage_reports — communication method for scope decisions |
| Stage 02 (Research) | `scope_boundary_traversal/` — findings about directional patterns |
| Stage 02 (Research) | `multi_agent_context_patterns/` — framework communication patterns validate relay model |
| Stage 06 (Development) | Principle 8 (expanded), Scope Boundary Rule (expanded) — promoted universal artifacts |

<!-- section_id: "97700401-bbae-4b67-b40e-9fbd50cee316" -->
## Related Decisions

- **Minimal context model** — directional framework is on-demand infrastructure, not STATIC
- **Stage reports for async communication** — stage reports are the primary communication for left/right/up directions
- **Scope boundary decisions (original Principle 8)** — this decision EXPANDS, not replaces
