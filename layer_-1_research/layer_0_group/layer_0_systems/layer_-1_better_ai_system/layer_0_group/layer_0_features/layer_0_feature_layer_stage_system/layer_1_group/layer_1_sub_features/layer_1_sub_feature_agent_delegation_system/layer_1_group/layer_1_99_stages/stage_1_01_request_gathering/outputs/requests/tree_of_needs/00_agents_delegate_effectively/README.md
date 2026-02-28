# Root Need: Agents Delegate Effectively

**The fundamental goal all agent delegation requirements derive from.**

---

## Definition

> Managers delegate work to specialized stage agents and sub-feature agents without carrying operational knowledge. Memory and multi-agent systems work together coherently.

---

## The Problem

Current AI agents do everything in one context -- no delegation, no specialization:
- A single agent carries all methodology, all domain knowledge, all operational detail
- Context windows overflow because one agent tries to hold everything
- Agents lose track of scope -- a manager starts doing stage-level work
- There is no handoff protocol between sessions or between agents
- No clear model for what a manager knows vs what a stage agent knows
- When agents do spawn sub-agents, context is lost in translation

---

## The Vision

A system where:
- Managers read pointers and stage reports, then delegate -- they never carry stage methodology
- Each stage agent has its own `0AGNOSTIC.md` with identity, methodology, output format, and success criteria
- Stage reports (`stage_report.md`) enable async status without the manager loading stage details
- Context flows through the hierarchy predictably: parent context chains load automatically, domain knowledge loads on demand
- Agent types (manager, stage agent, sub-feature agent) have clearly defined static and dynamic context models
- Handoff protocols preserve context across session boundaries and agent transitions

---

## Three Branches

| Branch | Question | Description |
|--------|----------|-------------|
| [**01_delegation_model**](./01_delegation_model/) | "How do managers delegate without carrying operational knowledge?" | Stage delegation, stage reports, agent context model |
| [**02_memory_integration**](./02_memory_integration/) | "How does what agents remember support delegation?" | Context chains, handoff protocols, three-tier delegation |
| [**03_coordination_patterns**](./03_coordination_patterns/) | "How do agents coordinate in practice?" | Agent hierarchy, spawning patterns, communication channels |

---

## Branch Structure

```
00_agents_delegate_effectively/              (this folder - the root)
|
+-- 01_delegation_model/                     How managers delegate
|   +-- need_01_stage_delegation             Manager hands off to stage agent
|   +-- need_02_stage_reports                Async status via stage_report.md
|   +-- need_03_agent_context_model          What each agent type knows
|
+-- 02_memory_integration/                   How memory supports delegation
|   +-- need_01_context_chain_support        Context chains inform delegation
|   +-- need_02_handoff_protocols            Context preserved across transitions
|   +-- need_03_three_tier_delegation        Pointers / distilled / full for delegation
|
+-- 03_coordination_patterns/                How agents coordinate
    +-- need_01_agent_hierarchy              Who manages whom
    +-- need_02_spawning_patterns            When and how to spawn agents
    +-- need_03_communication_channels       Channels for agent communication
```

---

## Success Criteria

The root need is satisfied when:
- [ ] Managers can delegate to stage agents without carrying stage methodology
- [ ] Each stage agent has a complete 0AGNOSTIC.md (identity, methodology, output format, success criteria)
- [ ] Stage reports provide sufficient status for manager decision-making
- [ ] Agent context models clearly define static vs dynamic context per agent type
- [ ] Handoff protocols preserve context across session boundaries
- [ ] Context chains load the right information at the right hierarchy level
- [ ] Agent hierarchy is clear: who manages whom, who spawns whom
- [ ] Spawning patterns are documented and repeatable
- [ ] Communication channels (reports, handoffs, team tools, episodic memory) are defined and used consistently

---

## Research Grounding

All needs trace to the agent delegation system's parent research:
- `memory_system/` research on context chains, three-tier architecture, knowledge organization
- `multi_agent_system/` research on agent hierarchies, orchestration, delegation patterns
- Domain concepts defined in `agent_delegation_system/0AGNOSTIC.md`
