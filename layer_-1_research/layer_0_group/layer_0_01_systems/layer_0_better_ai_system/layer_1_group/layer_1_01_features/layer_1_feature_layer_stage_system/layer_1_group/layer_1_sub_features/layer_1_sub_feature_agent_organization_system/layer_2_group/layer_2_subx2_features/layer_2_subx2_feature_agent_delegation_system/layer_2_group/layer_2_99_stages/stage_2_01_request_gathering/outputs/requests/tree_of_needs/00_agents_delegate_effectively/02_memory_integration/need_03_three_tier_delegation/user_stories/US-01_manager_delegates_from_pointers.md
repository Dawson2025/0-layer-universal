# US-1: Manager delegates from pointers alone

**Need**: [Three-Tier Delegation](../README.md)

---

**As a** user who asks the AI which stage needs work next,
**I want** the manager to make that decision using only high-level pointers (Tier 1), not by loading detailed stage outputs,
**So that** the AI responds quickly without needing to read through all the raw work files.

### What Happens

1. User asks "which stage needs work next?" or "what should we prioritize?"
2. Manager reads only Tier 1 content: 0AGNOSTIC.md, stage overview table, stage reports
3. Manager identifies the highest-priority stage based on status and blockers
4. Manager delegates to a stage agent without ever loading Tier 3 (full stage outputs)
5. User gets a fast, informed delegation decision

### Acceptance Criteria

- Manager's delegation decision uses only Tier 1 content; no Tier 3 files are read
- Decision quality is sufficient from Tier 1 alone (status, blockers, priorities)
- Response time is fast because the manager loads minimal content
