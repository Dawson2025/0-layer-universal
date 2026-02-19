# Need: Stage Delegation -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages and makes cross-stage decisions
- **Stage Agent**: AI agent spawned to work on a specific stage (e.g., request gathering, research, design)
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Manager spawns a stage agent

**As a** manager that needs request gathering done,
**I want to** spawn a stage agent with just a task description and a pointer to the stage directory,
**So that** I don't need to carry the request gathering methodology in my own context.

**Acceptance**: Manager's prompt to the stage agent contains only the task and directory path, not methodology.

---

### US-2: Stage agent reads its own identity

**As a** stage agent entering a stage directory for the first time,
**I want to** read `0AGNOSTIC.md` in my stage directory and immediately know my role, methodology, output format, and success criteria,
**So that** I can begin work without asking the manager for instructions.

**Acceptance**: Stage agent reads one file and has everything needed to start working.

---

### US-3: Stage agent loads domain context from parent

**As a** stage agent that needs domain-specific understanding,
**I want** my `0AGNOSTIC.md` to tell me where to find domain knowledge (parent entity's `.0agnostic/knowledge/`),
**So that** I load only the specific knowledge file relevant to my current task.

**Acceptance**: Stage agent reads at most 1-2 knowledge files, not the entire knowledge directory.

---

### US-4: Manager stays out of stage-level work

**As the** developer reviewing a manager's context,
**I want** the manager to contain only status overview, cross-stage coordination, and priority decisions,
**So that** I can confirm the manager is not bloated with operational detail that belongs in stage agents.

**Acceptance**: Manager's 0AGNOSTIC.md contains zero stage-level methodology or procedure descriptions.

---
