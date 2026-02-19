# US-3: Stage agent loads domain context from parent

**Need**: [Stage Delegation](../README.md)

---

**As a** stage agent that needs domain-specific understanding,
**I want** my `0AGNOSTIC.md` to tell me where to find domain knowledge (parent entity's `.0agnostic/knowledge/`),
**So that** I load only the specific knowledge file relevant to my current task.

**Acceptance**: Stage agent reads at most 1-2 knowledge files, not the entire knowledge directory.
