---
resource_id: "20eb49e6-07a5-47b4-a630-21f247c7aea0"
resource_type: "output"
resource_name: "US-01_developer_checks_freshness"
---
# US-01: Developer checks freshness before a session

**Need**: [Staleness Detection](../README.md)

---

**As a** user about to start a new AI work session,
**I want** to run a staleness check and see which knowledge files need updating,
**So that** I don't send the AI into a session with outdated knowledge that leads to wrong decisions.

<!-- section_id: "f54b8506-2d7e-4f3b-acbc-b730c97fd802" -->
### What Happens

1. User runs the staleness check command before starting a work session
2. Script compares each knowledge file's last-modified date against its source files' dates
3. Script produces a report listing stale files, their sources, and the time delta
4. User updates the stale knowledge files (or flags them) before starting the AI session

<!-- section_id: "dcf111c1-ac48-418e-a059-3ee364c65a2f" -->
### Acceptance Criteria

- Command produces a report listing stale files with time deltas
- Report shows which source files changed and when
- User can act on the report (knows exactly what to update)
