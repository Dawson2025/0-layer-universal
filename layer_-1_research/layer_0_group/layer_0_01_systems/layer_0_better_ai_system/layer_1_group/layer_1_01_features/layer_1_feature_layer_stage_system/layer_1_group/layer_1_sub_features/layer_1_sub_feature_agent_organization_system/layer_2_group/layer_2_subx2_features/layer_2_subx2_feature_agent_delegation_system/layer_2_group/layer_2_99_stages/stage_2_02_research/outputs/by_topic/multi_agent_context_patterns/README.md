---
resource_id: "be0ec746-95ff-4f61-8a9d-422f812e7257"
resource_type: "readme_output"
resource_name: "README"
---
# Multi-Agent Context Patterns

<!-- section_id: "f864ee3e-21c8-42eb-91a9-bb3152141ca2" -->
## Research Question

How do existing multi-agent AI frameworks handle context sharing between agents? Specifically: does full context cascade (every agent sees everything above it) outperform selective/minimal context sharing? What patterns have emerged?

This matters for the agent delegation system because: the layer-stage hierarchy must decide how much parent context each agent receives. Full cascade is simple but potentially wasteful. Minimal sharing is lean but risks agents lacking needed information.

<!-- section_id: "cdf75e04-30b7-4705-a03f-e06b18d3f62c" -->
## Findings

<!-- section_id: "5c763a76-a091-432f-8d01-fcd31b939cf4" -->
### CrewAI

**Pattern**: Selective sharing + RAG retrieval.

- Agents have distinct roles with their own context
- Shared context is mediated through a "crew" coordinator
- Agents can query a shared knowledge base (RAG) on-demand
- Only task-relevant context is passed between agents
- No full cascade — each agent sees its role definition + task-specific inputs

**Key insight**: CrewAI treats agents as specialists. Context is scoped to the task, not the hierarchy. An agent doesn't need to know everything its manager knows — it needs to know what's relevant to its current task.

<!-- section_id: "86a61cbf-b15a-4db0-af75-babff0906b34" -->
### LangGraph

**Pattern**: Graph-based checkpointed state.

- State flows through a directed graph of agent nodes
- Each node receives only the state relevant to its edges
- State is checkpointed — agents can resume from any point
- The graph topology determines what each agent sees
- No broadcast of full state to all agents

**Key insight**: LangGraph's graph topology is an explicit model of "who needs to know what." State doesn't cascade — it flows along defined channels. This is closest to the interface-based model where agents only see their direct neighbors' outputs.

<!-- section_id: "2a3688a0-a970-494f-a776-11cf1b560a0f" -->
### AutoGen (Microsoft)

**Pattern**: Conversational delegation with message passing.

- Agents communicate through structured messages
- Each agent has a system message (static identity) + conversation history
- Delegation is explicit: one agent asks another for help
- The requesting agent decides what context to include in the request
- No global shared state — context is in the conversation

**Key insight**: AutoGen treats context as message content, not as inherited state. When Agent A delegates to Agent B, Agent A chooses what context to include. This is the relay pattern — context is passed explicitly, not inherited.

<!-- section_id: "8fbc6174-e73f-4d42-ac19-7d9bd0a81e33" -->
## Cross-Framework Comparison

| Framework | Context Model | Cascade? | Global State? | On-Demand Access? |
|-----------|--------------|----------|---------------|-------------------|
| CrewAI | Selective sharing + RAG | No | Shared knowledge base | Yes (RAG queries) |
| LangGraph | Graph-based flow | Along edges only | Checkpointed per-node | Yes (state queries) |
| AutoGen | Message passing | No | No | Yes (ask another agent) |

<!-- section_id: "3e93d797-f975-43a6-a26c-4c68e1e04498" -->
## The Consistent Pattern

All three frameworks converge on the same principle: **minimal context + on-demand access outperforms full cascade**.

None of the major multi-agent frameworks use full context inheritance. Instead:

1. **Each agent has its own identity** (role definition, system prompt)
2. **Shared context is mediated** (through a coordinator, graph edges, or messages)
3. **On-demand access exists** (RAG, state queries, delegation requests)
4. **Full cascade is avoided** because it:
   - Wastes context window tokens on irrelevant information
   - Reduces agent focus (more noise = worse performance)
   - Creates tight coupling (changing parent context affects all children)
   - Doesn't scale (deep hierarchies compound context size)

<!-- section_id: "a877307b-dab0-42b5-a8f0-88a9402bcafe" -->
## Design Implications

<!-- section_id: "f5db6d56-315c-48e5-9756-2118561b6aa7" -->
### For the Agent Delegation System

1. **The hybrid pattern is validated**: Own STATIC context + neighbor interfaces + on-demand DYNAMIC access matches what all three frameworks do. This isn't a novel design — it's the emergent best practice.

2. **The relay pattern is standard**: Agents communicating through neighbor chains (not direct cross-hierarchy queries) is how AutoGen and LangGraph work. CrewAI's coordinator is similar to the manager role.

3. **RAG/on-demand is the escape hatch**: When an agent needs context beyond its immediate scope, it queries for it — it doesn't pre-load everything. In the layer-stage system, this maps to reading parent `.0agnostic/01_knowledge/` files on-demand.

4. **Identity should be compact**: In all three frameworks, agent system prompts are focused role definitions, not comprehensive knowledge dumps. This supports keeping 0AGNOSTIC.md STATIC sections lean.

5. **Context propagation = explicit, not implicit**: Rather than inheriting parent context automatically, successful frameworks pass context explicitly through delegation requests, messages, or graph edges. The agent delegation system should follow suit — manager provides task description + directory pointer, agent discovers its own methodology.

<!-- section_id: "8c2afda4-8e6c-49a7-bc51-e6e6988da159" -->
## Connection to Tool Cascading Research

See also: `../tool_context_cascading/README.md`

There's an interesting tension: AI coding tools (Claude Code, Codex, Gemini CLI) DO cascade context files automatically, but multi-agent frameworks DO NOT cascade agent context. The resolution:

- **Tool cascading is for infrastructure context** (rules, conventions, project identity) — things every agent at every level needs
- **Agent context is for task context** (what to do, what's relevant) — this should be scoped per-agent

The layer-stage system bridges both: the CLAUDE.md files that tools cascade should contain infrastructure context (lean pointers, identity). The 0AGNOSTIC.md + .0agnostic/ content that agents load on-demand should contain task context (methodology, current state, domain knowledge).

<!-- section_id: "aae63662-9171-46bd-9b57-59420128119c" -->
## Sources

- Perplexity ask: "Multi-agent AI frameworks context sharing patterns CrewAI LangGraph AutoGen" (2026-02-26)
- CrewAI documentation on agent roles and shared knowledge
- LangGraph documentation on state management and checkpointing
- AutoGen documentation on conversational patterns

<!-- section_id: "1db1d5bc-9b3d-4970-bf68-3be1e39be7fe" -->
## Date

2026-02-26
