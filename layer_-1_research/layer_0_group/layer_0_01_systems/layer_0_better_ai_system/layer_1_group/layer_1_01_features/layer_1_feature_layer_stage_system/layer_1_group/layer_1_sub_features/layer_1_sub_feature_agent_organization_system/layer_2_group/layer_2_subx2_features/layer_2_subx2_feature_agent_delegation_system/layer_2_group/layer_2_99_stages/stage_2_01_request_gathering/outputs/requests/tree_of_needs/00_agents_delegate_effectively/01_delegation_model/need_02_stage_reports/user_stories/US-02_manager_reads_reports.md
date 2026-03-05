---
resource_id: "fc85a2ca-40c5-4f55-860a-db0030d32ff8"
resource_type: "output"
resource_name: "US-02_manager_reads_reports"
---
# US-2: Manager reads stage reports for status

**Need**: [Stage Reports](../README.md)

---

**As a** user who asks "what's the status of this project?",
**I want** the system to read stage reports and give me a quick status across all stages,
**So that** I get a project-wide overview without the AI needing to load every output file.

### What Happens

1. User asks "what stage should we work on next?" or "what's the project status?"
2. Manager reads stage reports from multiple stages (one per stage)
3. Manager synthesizes a status overview: which stages are done, in-progress, or blocked
4. Manager recommends what to work on next based on priorities and blockers
5. User gets a clear answer without the system loading N * M detail files

### Acceptance Criteria

- Manager reads N stage reports (one per stage) and can rank priority
- Manager does not load full stage outputs to determine status
- User gets a concise, actionable status overview
