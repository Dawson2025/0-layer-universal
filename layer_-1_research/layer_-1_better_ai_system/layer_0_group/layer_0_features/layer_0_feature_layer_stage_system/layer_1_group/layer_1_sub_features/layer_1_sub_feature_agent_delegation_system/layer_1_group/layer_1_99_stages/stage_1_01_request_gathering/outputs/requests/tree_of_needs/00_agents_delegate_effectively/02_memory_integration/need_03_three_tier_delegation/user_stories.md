# Need: Three-Tier Delegation -- User Stories

## Actors

- **Manager**: Entity-level AI agent that coordinates stages
- **Stage Agent**: AI agent working within a specific stage
- **Developer**: Human maintaining the system (Dawson)

---

### US-1: Manager delegates from pointers alone

**As a** manager deciding which stage needs work,
**I want to** make that decision by reading only Tier 1 content (0AGNOSTIC.md, stage overview, stage reports),
**So that** I never need to load Tier 3 stage outputs to determine priorities.

**Acceptance**: Manager's delegation decision uses only Tier 1 content; no Tier 3 files are read.

---

### US-2: Stage agent works from distilled knowledge

**As a** stage agent working on design,
**I want to** read Tier 2 knowledge files (.0agnostic/knowledge/) for domain understanding,
**So that** I have actionable summaries rather than raw research from prior stages.

**Acceptance**: Stage agent reads distilled knowledge files, not raw stage_02 research outputs.

---

### US-3: Active stage agent accesses its own full content

**As a** stage agent actively producing outputs in stage 06 (development),
**I want** access to my own Tier 3 content (my stage's outputs and work-in-progress files),
**So that** I can build on my previous work within this stage.

**Acceptance**: Stage agent reads its own stage outputs, not other stages' outputs.

---

### US-4: Developer verifies tier-agent alignment

**As the** developer reviewing the system,
**I want** a clear mapping of which agent type accesses which tier,
**So that** I can audit whether agents are staying within their intended context scope.

**Acceptance**: Tier-to-agent mapping document exists with clear rules and no ambiguity.

---
