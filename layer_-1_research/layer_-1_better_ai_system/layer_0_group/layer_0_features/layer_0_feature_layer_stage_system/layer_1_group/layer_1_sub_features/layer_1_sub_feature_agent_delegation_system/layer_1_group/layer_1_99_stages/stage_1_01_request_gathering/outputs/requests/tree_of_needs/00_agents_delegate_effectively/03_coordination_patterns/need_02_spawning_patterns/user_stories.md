# Need: Spawning Patterns -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent spawned to work on a specific stage
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Manager decides to delegate

**As a** manager that needs design work done,
**I want** clear criteria telling me to spawn a stage agent (because design requires stage methodology),
**So that** I delegate consistently rather than sometimes doing stage work myself.

**Acceptance**: Spawning criteria documentation answers "should I spawn?" for common scenarios.

---

### US-2: Manager spawns with Task tool

**As a** manager delegating to a stage agent,
**I want** a standard prompt template for the Task tool that includes task description and directory pointer,
**So that** spawned agents receive consistent, sufficient context to begin work.

**Acceptance**: Template exists and spawned agent can start work from the template alone.

---

### US-3: Stage agent follows lifecycle

**As a** stage agent finishing my work,
**I want** a clear lifecycle protocol (read 0AGNOSTIC.md -> do work -> write stage report -> exit),
**So that** I leave the stage in a clean state for the next agent.

**Acceptance**: Stage agent follows the lifecycle steps in order, with stage report written before exit.

---

### US-4: Manager coordinates parallel work

**As a** manager that needs independent research on two topics,
**I want** rules telling me I can spawn parallel agents for independent work but not for dependent work,
**So that** I use parallelism when it helps and avoid it when it causes conflicts.

**Acceptance**: Parallel spawning rules clearly distinguish independent vs dependent work.

---
