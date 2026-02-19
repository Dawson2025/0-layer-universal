# Need: Staleness Detection — User Stories

---

### US-1: Developer checks freshness before a session
**As the** developer starting a new work session,
**I want to** run a staleness check and see which knowledge files need updating,
**So that** I don't send agents into sessions with outdated knowledge.

**Acceptance**: Command produces a report listing stale files with time deltas.

---

### US-2: Agent flags potentially stale knowledge
**As an** agent reading a knowledge file,
**I want** a way to check if the file's sources have been updated since the knowledge was written,
**So that** I can warn the developer or re-read the source directly.

**Acceptance**: Agent can compare knowledge file date against source file dates.
