# US-01: Developer runs full chain health check

**Need**: [Chain Validation Enhancement](../README.md)

---

**As a** user who wants a single command to check the entire context chain's health,
**I want** to run one command and get a unified report covering chain integrity, broken references, and stale knowledge,
**So that** I fix everything in one pass rather than running three separate checks.

### What Happens

1. User runs the chain health check command
2. Script validates chain integrity (graph vs file system), reference validity, and knowledge freshness
3. Script produces a unified report with all three dimensions in one output
4. User sees everything that needs fixing and addresses it in a single maintenance pass

### Acceptance Criteria

- Single command invocation produces a unified report
- Report covers all three dimensions: integrity, broken references, staleness
- Report is actionable: each item tells the user what to fix and where
