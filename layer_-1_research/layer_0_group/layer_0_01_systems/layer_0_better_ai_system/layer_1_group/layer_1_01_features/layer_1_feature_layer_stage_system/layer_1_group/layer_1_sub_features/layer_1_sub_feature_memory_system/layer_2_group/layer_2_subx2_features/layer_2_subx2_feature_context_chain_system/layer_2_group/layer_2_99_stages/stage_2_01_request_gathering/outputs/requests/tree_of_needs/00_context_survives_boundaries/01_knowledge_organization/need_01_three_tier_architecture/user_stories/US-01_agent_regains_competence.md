---
resource_id: "2f003608-3558-4175-9fda-42fdadfa27f6"
resource_type: "output"
resource_name: "US-01_agent_regains_competence"
---
# US-01: Agent regains competence after compaction

**Need**: [Three-Tier Architecture](../README.md)

---

**As a** user whose AI session just ran out of context,
**I want** the AI to recover competence quickly by reading structured knowledge,
**So that** I don't lose 30 minutes to the AI re-exploring files it already knew.

<!-- section_id: "7c69a97f-e708-4d85-bacc-8f1b1fac32bd" -->
### What Happens

1. User's conversation hits context limit, system compacts prior messages
2. Agent reads Tier 1 pointers (0AGNOSTIC.md) -- knows identity and where to look
3. Agent reads Tier 2 knowledge files (~260 lines of distilled summaries)
4. Agent is competent: can answer domain questions, make decisions, continue work

<!-- section_id: "42d422bc-273c-44f7-a75c-944d92e75420" -->
### Acceptance Criteria

- Agent reads ~260 lines (not ~5,000) and can answer domain questions correctly
- Recovery takes under 5 minutes, not 30
