# Need: Session Resilient

**Branch**: [02_continuous](../)
**Question**: "What if I run out of tokens or need to take a break?"

---

## Definition

Pick up where you left off, regardless of session boundaries or tool switches.
- Handoff documents capture session state
- Self-describing system structure
- Work survives token limits, breaks, tool switches

---

## Why This Matters

- Token limits run out
- Context windows have maximums
- Users take breaks (hours, days, weeks)
- Work should not be lost or require re-explaining

---

## Requirements

### Cross-Tool Session Continuity (from request_04)
- MUST be able to switch AI apps mid-task without losing progress or context
- MUST have system structure be self-describing (any AI can understand where things are)
- MUST have clear indicators of current work state (what project, what task, where to pick up)
- MUST allow new AI session to quickly navigate to the right context
- SHOULD make it easy to say "I'm working on X" and have AI find the right place
- SHOULD leverage the layer-stage hierarchy for navigation and context discovery

### Handoff Protocol (from request_03)
- MUST define handoff document schema
- MUST specify what context transfers between agents/sessions
- MUST provide incoming/outgoing handoff templates
- MUST support both sync and async handoffs
- MUST include: what was being worked on, what's done, what's next
- MUST be structured enough for AI to parse
- SHOULD be generated/updated as work progresses

### Session Continuity (from request_03)
- MUST enable work resumption across sessions
- MUST track what was done and what remains
- SHOULD support partial completion states

### State Persistence (from request_04)
- MUST persist important decisions and learnings
- MUST save project-specific conventions discovered
- MUST maintain task/todo state across sessions
- SHOULD prioritize what to remember vs what to discard

---

## Acceptance Criteria

- [ ] Can switch from one AI app to another mid-task without starting over
- [ ] System structure allows any AI to quickly understand current state
- [ ] Handoff documents capture session state
- [ ] Handoff schema is defined and validated
- [ ] Example handoff documents demonstrate usage
- [ ] Layer-stage hierarchy enables navigation to current work context
- [ ] New AI session can find "where to pick up" within minutes
- [ ] Work continues after hours/days/weeks away

---

## Integrated From

- request_04: REQ-04-F00d, REQ-04-F01
- request_03: REQ-03-F04, REQ-03-F05
