# Need: Agent Context Model

**Branch**: [01_delegation_model](../)
**Question**: "What does each agent type know in its static vs dynamic context?"
**Version**: 1.0.0

---

## Definition

Each agent type (manager, stage agent, sub-feature agent) has a defined context model specifying what is in its static context (always loaded), what is in its dynamic context (loaded on demand), and what it never loads. This prevents context overflow and ensures agents operate within their scope.

---

## Why This Matters

- Without a context model, agents load too much (overflow) or too little (incompetence)
- Managers that load stage details lose room for cross-stage coordination
- Stage agents that load peer stage outputs lose room for their own methodology
- The context model is the contract between the hierarchy and the agent's context window

---

## Requirements

### Context Model Definition
- MUST define the context model for three agent types: manager, stage agent, sub-feature agent
- MUST specify for each type: what is in static context (always loaded via context chain)
- MUST specify for each type: what is in dynamic context (loaded on demand when needed)
- MUST specify for each type: what is never loaded (out of scope)

### Manager Context Model
- MUST include in static: entity identity (0AGNOSTIC.md), stage overview table, children list
- MUST include in dynamic: stage reports, child entity summaries, episodic memory
- MUST NOT include: stage methodology, stage output details, child entity internals
- SHOULD include in static: triggers for when to delegate, escalation paths

### Stage Agent Context Model
- MUST include in static: stage identity (stage 0AGNOSTIC.md), parent entity identity
- MUST include in dynamic: parent knowledge files (only relevant ones), prior stage report
- MUST NOT include: peer stage outputs, sibling stage methodology, manager-level coordination
- SHOULD include in dynamic: relevant sub-layer rules (static rules always, dynamic rules when triggered)

### Sub-Feature Agent Context Model
- MUST include in static: entity identity (0AGNOSTIC.md), children list, stage overview
- MUST include in dynamic: parent context chain, own stage reports, own knowledge files
- MUST NOT include: sibling entity internals, parent's other children details
- SHOULD define how sub-feature agents relate to their parent manager

---

## Acceptance Criteria

- [ ] Context model is documented for all three agent types (manager, stage agent, sub-feature agent)
- [ ] Each model clearly separates static, dynamic, and never-loaded context
- [ ] Manager context model excludes stage-level operational knowledge
- [ ] Stage agent context model excludes peer stage and manager-level detail
- [ ] A new agent can be instantiated by following its context model without guessing what to load

---

## User Stories

See [user_stories.md](./user_stories.md)

---

## Research References

- Context chain research on static vs dynamic context dimensions
- Context chain system's three-tier architecture (pointers / distilled / full)
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- agent context model definition
