---
resource_id: "504a0041-1850-4490-a879-16108c5299ea"
resource_type: "output"
resource_name: "US-04_developer_validates_chain_integrity"
---
# US-04: Developer validates chain integrity

**Need**: [Knowledge Graph](../README.md)

---

**As a** user who wants to make sure the system is healthy before starting a work session,
**I want** to run chain-validate and get a report comparing the graph against the file system,
**So that** I fix broken references before the AI encounters them and gets confused.

<!-- section_id: "966c2169-1dbe-473f-ad24-d59fc959e7cd" -->
### What Happens

1. User runs the chain-validate command
2. Script compares the knowledge graph (expected relationships) against the actual file system (what exists)
3. Script produces a report listing orphaned nodes, missing nodes, and broken edges
4. User fixes the issues; next AI session starts with a clean, valid context chain

<!-- section_id: "81848c92-4d83-4676-88e7-bc78a29f9114" -->
### Acceptance Criteria

- Report identifies orphaned nodes (in graph but not on disk)
- Report identifies missing nodes (on disk but not in graph)
- Report identifies broken edges (relationships pointing to nonexistent targets)
- All issues are actionable (user knows exactly what to fix)
