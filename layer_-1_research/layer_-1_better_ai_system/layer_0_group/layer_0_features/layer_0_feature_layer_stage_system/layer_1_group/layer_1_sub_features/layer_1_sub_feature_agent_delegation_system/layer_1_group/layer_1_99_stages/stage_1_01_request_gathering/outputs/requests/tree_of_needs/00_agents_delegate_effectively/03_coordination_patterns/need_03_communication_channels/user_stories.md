# Need: Communication Channels -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Parallel Agent**: Another agent working concurrently on a different task
- **Future Agent**: An agent in a future session that needs to understand what happened

---

### US-1: Stage agent communicates status via report

**As a** stage agent that has completed my work,
**I want to** write a stage report that my manager will read,
**So that** the manager knows my status without needing a real-time conversation.

**Acceptance**: Manager reads stage report and understands status; no direct communication needed.

---

### US-2: Parallel agents coordinate in real time

**As a** stage agent working in parallel with another agent on independent tasks,
**I want to** use team tools (SendMessage) to notify the other agent of a shared concern,
**So that** we avoid conflicting outputs without waiting for the manager to mediate.

**Acceptance**: Parallel agents use SendMessage for real-time coordination, not stage reports.

---

### US-3: Future agent discovers session history

**As an** agent starting a new session on an entity I have not worked on before,
**I want to** read episodic memory and stage reports to understand what has been done previously,
**So that** I can contribute meaningfully without repeating prior work.

**Acceptance**: Episodic memory + stage reports provide enough context to understand history.

---

### US-4: Agent knows which channel to use

**As an** agent that needs to communicate something,
**I want** clear rules telling me which channel to use (stage report for status, handoff doc for entity transfer, team tools for real-time, episodic for session history),
**So that** I put information in the right place and it reaches the right audience.

**Acceptance**: Channel selection rules are unambiguous for common communication scenarios.

---
