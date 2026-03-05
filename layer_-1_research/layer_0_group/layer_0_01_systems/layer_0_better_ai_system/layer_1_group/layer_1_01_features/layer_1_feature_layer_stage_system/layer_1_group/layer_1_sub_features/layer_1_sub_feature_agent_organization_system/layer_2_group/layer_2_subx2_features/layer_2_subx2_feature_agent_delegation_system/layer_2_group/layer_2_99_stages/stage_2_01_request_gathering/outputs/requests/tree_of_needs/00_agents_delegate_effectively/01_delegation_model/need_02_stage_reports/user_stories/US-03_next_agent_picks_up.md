---
resource_id: "61b95788-e0a2-4b3f-ad32-c52448bcc74a"
resource_type: "output"
resource_name: "US-03_next_agent_picks_up"
---
# US-3: Next agent picks up where the last left off

**Need**: [Stage Reports](../README.md)

---

**As a** user who returns to a project after a break and tells the AI to continue working on a stage,
**I want** the new agent to read the previous report and know exactly what to do first,
**So that** I don't waste time re-explaining what was already done.

<!-- section_id: "2a9b5477-5a48-4a02-b978-1a65af2be6f3" -->
### What Happens

1. User returns to a project and says "continue the research" or "pick up where we left off"
2. Manager spawns a stage agent for the appropriate stage
3. Stage agent reads the previous `stage_report.md` in `outputs/`
4. Stage agent reads the "next steps" section and knows its immediate first task
5. Stage agent resumes work without re-discovering what has already been done

<!-- section_id: "fbf3580f-5c66-4dbc-8d73-639db24623a1" -->
### Acceptance Criteria

- Stage report's "next steps" section gives an actionable first task
- New agent starts productive work immediately, not re-exploration
- User does not need to summarize prior progress to the new agent
