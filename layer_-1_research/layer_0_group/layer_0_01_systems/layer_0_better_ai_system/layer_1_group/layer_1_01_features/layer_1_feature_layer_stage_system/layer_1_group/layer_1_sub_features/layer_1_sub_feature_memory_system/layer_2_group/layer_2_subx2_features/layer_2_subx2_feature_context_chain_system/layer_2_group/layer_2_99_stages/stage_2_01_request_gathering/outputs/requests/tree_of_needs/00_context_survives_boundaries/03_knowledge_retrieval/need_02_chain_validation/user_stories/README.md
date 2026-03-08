---
resource_id: "63802c72-d205-4b9e-9032-d3a1e0894e14"
resource_type: "readme_output"
resource_name: "README"
---
# Chain Validation Enhancement -- User Stories Index

**Need**: [Chain Validation Enhancement](../README.md)

<!-- section_id: "19c2b024-0ecb-4537-9a79-c7ed5693cb83" -->
## Overview

These stories cover upgrading chain validation to check relationship integrity against the knowledge graph, not just file existence. They validate that the developer can run a comprehensive health check covering integrity, validity, and staleness in one report, that agents detect broken references before following them and failing silently, and that CI hooks or pre-commit checks catch chain breakage automatically before changes are merged.

<!-- section_id: "77663401-12cf-4ce0-8f75-57e9a1a6b8f3" -->
## Actors

- **User (Developer)**: Human developer (Dawson) who gives instructions to the AI system, reviews outputs, and validates behavior
- **Manager**: Entity-level AI agent that coordinates stages (internal system behavior)
- **Stage Agent**: AI agent spawned for specific stage work (internal system behavior)

---

| US# | Title | Scenario | File |
|-----|-------|----------|------|
| US-01 | Developer runs full chain health check | Developer executes validation covering integrity, validity, and staleness | [US-01_developer_runs_health_check.md](./US-01_developer_runs_health_check.md) |
| US-02 | Agent detects broken reference before failing | Agent checks reference validity before following a link | [US-02_agent_detects_broken_reference.md](./US-02_agent_detects_broken_reference.md) |
| US-03 | CI/hook catches chain breakage on commit | Pre-commit hook or CI pipeline detects chain breaks before merge | [US-03_ci_catches_chain_breakage.md](./US-03_ci_catches_chain_breakage.md) |
