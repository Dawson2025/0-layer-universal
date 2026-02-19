# Need: Handoff Protocols -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Next Agent**: The agent that picks up work after a transition (could be same role, new session)
- **Child Agent**: Agent managing a child entity

---

### US-1: Stage agent hands off to next session

**As a** stage agent finishing a work session,
**I want to** write a stage report and update episodic memory with my progress,
**So that** the next agent working on this stage can continue without re-discovering my work.

**Acceptance**: Next agent reads stage report + episodic memory and starts where the previous agent left off.

---

### US-2: Manager delegates with sufficient context

**As a** manager delegating research work to a stage agent,
**I want to** provide a task description and point to the stage directory,
**So that** the stage agent has everything it needs to begin work.

**Acceptance**: Stage agent's first action is reading its 0AGNOSTIC.md, not asking the manager for clarification.

---

### US-3: Child entity receives handoff from parent

**As a** child entity agent starting work for the first time,
**I want to** read an incoming handoff document that explains why I was created and what is expected,
**So that** I understand my purpose in the broader hierarchy without reading the parent's full context.

**Acceptance**: Incoming handoff document exists and is under 50 lines with clear scope and expectations.

---

### US-4: Agent recovers after compaction

**As an** agent whose context was just compacted (lost all prior conversation),
**I want to** recover my working state by reading my 0AGNOSTIC.md, stage reports, and episodic memory,
**So that** compaction does not mean starting from scratch.

**Acceptance**: Agent recovers competence in under 5 minutes of reading, not 30 minutes of re-exploration.

---
