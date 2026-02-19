# Branch: Coordination Patterns

**Parent**: [00_agents_delegate_effectively](../)

---

## Core Question

> "How do agents coordinate in practice?"

---

## Description

Beyond the delegation model (who does what) and memory integration (what each agent knows), agents need practical coordination mechanisms. This branch defines the hierarchy of agents, the rules for when and how to spawn new agents, and the communication channels agents use to share information.

The three failure modes without coordination patterns:
1. **Flat hierarchy** -- no clear parent-child relationships, agents overlap or contradict each other
2. **Ad-hoc spawning** -- agents are created without clear criteria, leading to orphaned or redundant agents
3. **No communication standard** -- agents produce outputs but nobody reads them, or agents duplicate effort because they cannot see what others have done

---

## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| [need_01_agent_hierarchy](./need_01_agent_hierarchy/) | "Who manages whom in the agent tree?" | Clear parent-child management relationships |
| [need_02_spawning_patterns](./need_02_spawning_patterns/) | "When and how should specialized agents be created?" | Rules for Task tool, team creation, agent lifecycle |
| [need_03_communication_channels](./need_03_communication_channels/) | "How do agents share information?" | Stage reports, handoff docs, team tools, episodic memory |

---

## Key Insight

Coordination patterns mirror the layer-stage hierarchy itself. The entity tree defines the management tree. Stages define work boundaries. The existing layer-stage structure is not just an organizational pattern -- it is the coordination pattern. The challenge is making this implicit structure explicit in agent behavior.
