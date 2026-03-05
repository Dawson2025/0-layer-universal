---
resource_id: "b7c2e2b7-5a43-4df4-9ceb-f317bdc5647c"
resource_type: "readme
output"
resource_name: "README"
---
# Need: Agent Context Model

**Branch**: [01_delegation_model](../)
**Question**: "What does each agent type know in its static vs dynamic context?"
**Version**: 1.0.0

---

<!-- section_id: "5ef827f8-7e61-4909-9db6-1463de4f1da8" -->
## Definition

Each agent type (manager, stage agent, sub-feature agent) has a defined context model specifying what is in its static context (always loaded), what is in its dynamic context (loaded on demand), and what it never loads. This prevents context overflow and ensures agents operate within their scope.

---

<!-- section_id: "6515fa52-c473-4dc2-b663-fb4608bd78a8" -->
## Why This Matters

- Without a context model, agents load too much (overflow) or too little (incompetence)
- Managers that load stage details lose room for cross-stage coordination
- Stage agents that load peer stage outputs lose room for their own methodology
- The context model is the contract between the hierarchy and the agent's context window

---

<!-- section_id: "7b56718a-d919-49aa-955a-55f920114a08" -->
## Requirements

See [requirements/](./requirements/) for individual requirements.

---

<!-- section_id: "9d17f012-bd9b-4258-811c-07b2a181d030" -->
## User Stories

See [user_stories/](./user_stories/) for individual stories.

---

<!-- section_id: "9a9be331-ce5b-4bff-8a89-b1241909d9e4" -->
## Acceptance Criteria

- [ ] Context model is documented for all three agent types (manager, stage agent, sub-feature agent)
- [ ] Each model clearly separates static, dynamic, and never-loaded context
- [ ] Manager context model excludes stage-level operational knowledge
- [ ] Stage agent context model excludes peer stage and manager-level detail
- [ ] A new agent can be instantiated by following its context model without guessing what to load

---

<!-- section_id: "0877b714-fd0c-438b-ae2e-a942e875d666" -->
## Research References

- Context chain research on static vs dynamic context dimensions
- Context chain system's three-tier architecture (pointers / distilled / full)
- Domain concepts in `agent_delegation_system/0AGNOSTIC.md` -- agent context model definition
