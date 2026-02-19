# Need: Stage Reports -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Next Agent**: The next stage agent (or the same stage agent in a future session)

---

### US-1: Stage agent writes a report before exiting

**As a** stage agent finishing a work session,
**I want to** write a `stage_report.md` summarizing what I did, what I produced, and what comes next,
**So that** the manager (or a future agent) can understand my stage's status without loading my detailed outputs.

**Acceptance**: Report exists at `outputs/stage_report.md` and is under 30 lines.

---

### US-2: Manager reads stage reports for status

**As a** manager deciding which stage needs work next,
**I want to** read stage reports from multiple stages and see their status at a glance,
**So that** I can prioritize delegation without loading each stage's full outputs.

**Acceptance**: Manager reads N stage reports (one per stage) and can rank priority, not N * M detail files.

---

### US-3: Next agent picks up where the last left off

**As a** stage agent entering a stage where another agent previously worked,
**I want to** read the stage report's "next steps" section and know exactly what to do first,
**So that** I don't waste time re-discovering what has already been done.

**Acceptance**: Stage report's "next steps" section gives actionable first task.

---

### US-4: Manager identifies blocked stages

**As a** manager reviewing stage reports,
**I want** blocked stages to clearly state what they are blocked on and what decision I need to make,
**So that** I can unblock the stage agent or escalate the issue.

**Acceptance**: Blocked stage reports include a "blockers" section with specific, actionable items.

---
