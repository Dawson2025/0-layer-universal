---
resource_id: "b05662b0-dc17-438c-b973-8ddf15ec4f63"
resource_type: "readme_output"
resource_name: "README"
---
# Stage Reports -- User Stories Index

**Need**: [Stage Reports](../README.md)

<!-- section_id: "009090ff-5eb7-4a7f-bae9-fa0523587324" -->
## Overview

These stories cover the async communication loop between stage agents and managers through structured reports. They validate that stage agents produce concise reports before exiting, that managers can make informed delegation decisions from reports alone without loading stage details, and that subsequent agents can resume work from where the previous agent left off.

<!-- section_id: "72d354c0-cc16-48c1-ac68-3b8ea72ef239" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Stage agent writes a report before exiting | Agent produces a structured stage_report.md on completion | [US-01_stage_agent_writes_report.md](./US-01_stage_agent_writes_report.md) |
| US-02 | Manager reads stage reports for status | Manager assesses cross-stage progress from reports alone | [US-02_manager_reads_reports.md](./US-02_manager_reads_reports.md) |
| US-03 | Next agent picks up where the last left off | New session agent resumes work using the previous report | [US-03_next_agent_picks_up.md](./US-03_next_agent_picks_up.md) |
| US-04 | Manager identifies blocked stages | Manager detects blockers from report content and re-prioritizes | [US-04_manager_identifies_blocked.md](./US-04_manager_identifies_blocked.md) |
