---
resource_id: "5a8ff40c-e54d-4394-88e8-da5334e1bea4"
resource_type: "output"
resource_name: "US-01_developer_runs_health_check"
---
# US-01: Developer runs full chain health check

**Need**: [Chain Validation Enhancement](../README.md)

---

**As a** user who wants a single command to check the entire context chain's health,
**I want** to run one command and get a unified report covering chain integrity, broken references, and stale knowledge,
**So that** I fix everything in one pass rather than running three separate checks.

<!-- section_id: "f39d21b4-58b2-4083-91d0-4f408eae7c14" -->
### What Happens

1. User runs the chain health check command
2. Script validates chain integrity (graph vs file system), reference validity, and knowledge freshness
3. Script produces a unified report with all three dimensions in one output
4. User sees everything that needs fixing and addresses it in a single maintenance pass

<!-- section_id: "a082c358-5f9b-4916-8c5d-a2ffeb3615e9" -->
### Acceptance Criteria

- Single command invocation produces a unified report
- Report covers all three dimensions: integrity, broken references, staleness
- Report is actionable: each item tells the user what to fix and where
