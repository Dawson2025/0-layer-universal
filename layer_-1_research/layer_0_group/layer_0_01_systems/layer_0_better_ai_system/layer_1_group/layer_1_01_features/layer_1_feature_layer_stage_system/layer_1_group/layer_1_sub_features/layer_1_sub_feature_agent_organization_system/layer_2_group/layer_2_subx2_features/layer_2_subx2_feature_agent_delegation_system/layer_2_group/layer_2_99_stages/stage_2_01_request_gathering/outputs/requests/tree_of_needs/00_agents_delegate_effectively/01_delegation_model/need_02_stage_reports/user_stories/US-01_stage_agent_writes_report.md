---
resource_id: "767f8ab9-f6b8-4b01-88dc-05f13f5856c5"
resource_type: "output"
resource_name: "US-01_stage_agent_writes_report"
---
# US-1: Stage agent writes a report before exiting

**Need**: [Stage Reports](../README.md)

---

**As a** user who wants to check on a stage's progress without reading all its output files,
**I want** the stage agent to write a concise report summarizing what it did and what comes next,
**So that** I can understand stage status at a glance.

<!-- section_id: "bd42b90f-43d9-435d-95ba-6ea2ba6bc435" -->
### What Happens

1. User asks the AI to work on a stage (e.g., "do the research")
2. Stage agent performs the work and produces outputs
3. Before exiting, stage agent writes a `stage_report.md` in `outputs/`
4. Report summarizes: status, what was produced, blockers, and next steps
5. User (or manager) can read the report without loading detailed output files

<!-- section_id: "894b8d3d-2a4c-4823-b7e0-efd5f70aecd0" -->
### Acceptance Criteria

- Report exists at `outputs/stage_report.md` and is under 30 lines
- Report includes status, summary, outputs list, blockers, and next steps
- User can understand the stage's state by reading only the report
