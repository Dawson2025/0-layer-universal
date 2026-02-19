# Need: Chain Validation Enhancement — User Stories

---

### US-1: Developer runs full chain health check
**As the** developer,
**I want to** run one command and see a unified report of chain integrity, broken references, and stale knowledge,
**So that** I fix everything in one pass rather than running separate checks.

**Acceptance**: Single invocation produces unified report covering all three dimensions.

---

### US-2: Agent detects broken reference before failing
**As an** agent following a reference from a knowledge file to a stage output,
**I want** the reference to be pre-validated (known good),
**So that** I don't waste context loading a file that doesn't exist.

**Acceptance**: Validation catches broken references before agents encounter them.

---

### US-3: CI/hook catches chain breakage on commit
**As the** developer,
**I want** chain validation to run as a git hook or CI check,
**So that** broken references are caught before they're pushed.

**Acceptance**: Hook/CI integration defined, runs validation on structural changes.
