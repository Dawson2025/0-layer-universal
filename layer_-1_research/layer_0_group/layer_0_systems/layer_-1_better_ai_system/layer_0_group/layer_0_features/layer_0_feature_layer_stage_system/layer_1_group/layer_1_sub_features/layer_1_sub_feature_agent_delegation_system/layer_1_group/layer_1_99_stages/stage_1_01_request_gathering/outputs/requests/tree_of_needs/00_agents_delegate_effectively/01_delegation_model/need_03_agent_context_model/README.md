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

See [requirements/](./requirements/) for individual requirements.

---

## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

## Acceptance Criteria

- [ ] Context model is documented for all three agent types (manager, stage agent, sub-feature agent)
- [ ] Each model clearly separates static, dynamic, and never-loaded context
- [ ] Manager context model excludes stage-level operational knowledge
- [ ] Stage agent context model excludes peer stage and manager-level detail
- [ ] A new agent can be instantiated by following its context model without guessing what to load

---

## Research References

- Context chain research on static vs dynamic context dimensions
- Context chain system's three-tier architecture (pointers / distilled / full)
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- agent context model definition
