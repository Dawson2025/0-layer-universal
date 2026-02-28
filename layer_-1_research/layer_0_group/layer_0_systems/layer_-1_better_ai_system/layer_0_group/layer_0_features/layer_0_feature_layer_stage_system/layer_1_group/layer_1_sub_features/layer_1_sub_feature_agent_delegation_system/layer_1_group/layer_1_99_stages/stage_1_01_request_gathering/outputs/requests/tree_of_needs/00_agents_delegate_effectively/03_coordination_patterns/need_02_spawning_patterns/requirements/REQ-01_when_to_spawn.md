# When to Spawn

**Need**: [Spawning Patterns](../README.md)

---

- MUST define criteria for when a manager should spawn a stage agent vs do work directly
- MUST define the rule: if the work requires stage methodology, spawn a stage agent
- MUST define the rule: if the work is a quick status check or decision, the manager can do it directly
- SHOULD define thresholds: work expected to take more than N steps should be delegated
- MUST NOT allow managers to spawn agents for cross-stage coordination (that is the manager's job)
