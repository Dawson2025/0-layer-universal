# US-02: Agent detects broken reference before failing

**Need**: [Chain Validation Enhancement](../README.md)

---

**As an** agent following a reference from a knowledge file to a stage output,
**I want** the reference to be pre-validated (known good),
**So that** I don't waste context loading a file that doesn't exist.

**Acceptance**: Validation catches broken references before agents encounter them.
