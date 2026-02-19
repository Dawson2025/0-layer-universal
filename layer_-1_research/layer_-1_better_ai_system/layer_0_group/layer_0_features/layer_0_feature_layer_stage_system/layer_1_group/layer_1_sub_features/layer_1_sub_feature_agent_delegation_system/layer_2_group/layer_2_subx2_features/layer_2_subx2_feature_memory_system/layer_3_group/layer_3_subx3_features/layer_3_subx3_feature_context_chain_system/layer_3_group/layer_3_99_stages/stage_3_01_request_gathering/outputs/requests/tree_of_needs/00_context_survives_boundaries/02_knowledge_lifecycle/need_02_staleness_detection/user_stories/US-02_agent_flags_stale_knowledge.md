# US-02: Agent flags potentially stale knowledge

**Need**: [Staleness Detection](../README.md)

---

**As an** agent reading a knowledge file,
**I want** a way to check if the file's sources have been updated since the knowledge was written,
**So that** I can warn the developer or re-read the source directly.

**Acceptance**: Agent can compare knowledge file date against source file dates.
