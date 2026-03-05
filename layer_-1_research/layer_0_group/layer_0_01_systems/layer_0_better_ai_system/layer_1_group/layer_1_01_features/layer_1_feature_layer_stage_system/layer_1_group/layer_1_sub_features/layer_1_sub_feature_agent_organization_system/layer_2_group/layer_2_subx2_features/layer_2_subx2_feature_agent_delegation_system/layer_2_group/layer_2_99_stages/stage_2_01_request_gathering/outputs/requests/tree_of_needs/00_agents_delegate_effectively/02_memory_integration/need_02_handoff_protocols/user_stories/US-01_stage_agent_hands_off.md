---
resource_id: "6437b5b3-68d1-4ad6-80d4-6aa3018c4fa4"
resource_type: "output"
resource_name: "US-01_stage_agent_hands_off"
---
# US-1: Stage agent hands off to next session

**Need**: [Handoff Protocols](../README.md)

---

**As a** user who ends a session and expects to resume later without losing progress,
**I want** the stage agent to write a stage report and update episodic memory before exiting,
**So that** the next session can continue where I left off without re-doing previous work.

### What Happens

1. User finishes a work session (or the session ends due to context limits)
2. Stage agent writes a `stage_report.md` summarizing: status, outputs, next steps
3. Stage agent updates episodic memory with session details
4. User returns later and says "continue working on this"
5. New agent reads stage report + episodic memory and resumes from the right place

### Acceptance Criteria

- Next agent reads stage report + episodic memory and starts where the previous agent left off
- No re-discovery or duplicate work occurs in the new session
- User does not need to re-explain what was done in the previous session
