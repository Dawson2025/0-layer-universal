# US-2: Stage agent loads domain knowledge on demand

**Need**: [Agent Context Model](../README.md)

---

**As a** stage agent that needs to understand a domain concept,
**I want to** know exactly which knowledge file to read from the parent entity's `.0agnostic/knowledge/`,
**So that** I load one targeted file instead of the entire knowledge directory.

**Acceptance**: Stage agent reads at most 1-2 knowledge files per task, guided by its 0AGNOSTIC.md.
