# US-01: Agent regains competence after compaction

**Need**: [Three-Tier Architecture](../README.md)

---

**As an** agent whose context was just compacted,
**I want to** read Tier 1 (pointers) then Tier 2 (distilled knowledge) and be competent,
**So that** I don't need to re-read all stage outputs to continue working.

**Acceptance**: Agent reads ~260 lines (not ~5,000) and can answer domain questions correctly.
