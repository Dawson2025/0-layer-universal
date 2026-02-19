# US-02: Agent knows where to find details

**Need**: [Three-Tier Architecture](../README.md)

---

**As an** agent that needs a specific detail (e.g., STDP timing window),
**I want** the knowledge file to tell me exactly which stage output file and section has the full explanation,
**So that** I load one targeted file instead of searching across all outputs.

**Acceptance**: Every knowledge file claim has a "See [file] Section [X]" reference.
