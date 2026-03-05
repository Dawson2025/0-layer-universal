---
resource_id: "d71e5d87-4cd6-4573-994f-1bf18045f58c"
resource_type: "output"
resource_name: "US-02_agent_detects_broken_reference"
---
# US-02: Agent detects broken reference before failing

**Need**: [Chain Validation Enhancement](../README.md)

---

**As a** user whose AI is following references between knowledge files and stage outputs,
**I want** references to be pre-validated (known good) so the AI never wastes context on a dead link,
**So that** the AI doesn't hit a dead end mid-task and lose time on a file that doesn't exist.

### What Happens

1. User runs validation as part of regular maintenance (or it runs automatically)
2. Validation catches broken references (moved files, renamed sections) before any AI session
3. During a session, the AI follows only pre-validated references
4. User never sees the AI fail on a dead link -- all references resolve correctly

### Acceptance Criteria

- Validation catches broken references before agents encounter them at runtime
- No agent session wastes context loading a file that doesn't exist
- Broken references found by validation are reported with enough detail to fix
