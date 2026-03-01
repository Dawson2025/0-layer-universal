# US-4: Manager identifies blocked stages

**Need**: [Stage Reports](../README.md)

---

**As a** user who asks the AI to figure out what's blocking progress,
**I want** blocked stages to clearly state what they are blocked on and what decision is needed,
**So that** I can make the decision and unblock the work without digging through output files.

### What Happens

1. User asks "what's blocked?" or "why isn't this stage progressing?"
2. Manager reads stage reports across all stages
3. Manager identifies stages with "blocked" status and reads their blockers section
4. Manager presents the blockers to the user with specific, actionable items
5. User makes a decision, and the manager can unblock the stage agent

### Acceptance Criteria

- Blocked stage reports include a "blockers" section with specific, actionable items
- Each blocker states what decision is needed and who needs to make it
- User can resolve the blocker from the report information alone
