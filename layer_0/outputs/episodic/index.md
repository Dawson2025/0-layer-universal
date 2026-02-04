# Episodic Memory Index

**Layer**: layer_0 (universal)
**Last Updated**: 2026-01-30
**Total Sessions**: 1

---

## Purpose

This index provides quick access to session history, enabling agents to:
- Resume work without amnesia
- Understand previous decisions
- Continue seamlessly across sessions

---

## Recent Sessions

| Date | Session | Summary | Status |
|------|---------|---------|--------|
| 2026-01-30 | [001](sessions/2026-01-30_session_001.md) | Initial AGNOSTIC + episodic system setup | COMPLETED |

---

## Key Decisions

| Date | Decision | Rationale | Session |
|------|----------|-----------|---------|
| 2026-01-30 | Implement 0AGNOSTIC.md system | Tool portability, lean context | 001 |
| 2026-01-30 | Implement episodic memory | Solve agent amnesia | 001 |
| 2026-01-30 | Use file locking for sync | Prevent multi-agent conflicts | 001 |

---

## Active Work

| Topic | Last Session | Status | Next Steps |
|-------|--------------|--------|------------|
| AGNOSTIC system | 001 | COMPLETED | Deploy to all layers |
| Episodic memory | 001 | IN PROGRESS | Create templates, deploy |
| Multi-agent sync | - | PENDING | Implement file locking |
| Automated traversal | - | PENDING | Create 0INDEX.md system |

---

## Change Tracking

Recent changes are logged in:
- `changes/divergence.log` - All file modifications
- `changes/conflicts.log` - Detected conflicts
- `changes/progress.md` - Current status

---

## How to Use This Index

### Starting a New Session
1. Read this index to understand recent activity
2. Check "Active Work" for current state
3. Read relevant session files for context
4. Begin work with full awareness

### Ending a Session
1. Create session file in `sessions/`
2. Update this index with new session entry
3. Update "Key Decisions" if applicable
4. Update "Active Work" status

### Finding Information
- **What happened yesterday?** → Check Recent Sessions
- **Why was X decided?** → Check Key Decisions
- **What's currently being worked on?** → Check Active Work
- **What files changed?** → Check changes/divergence.log

---

## Session File Location

All session files are in: `sessions/YYYY-MM-DD_session_NNN.md`

Naming convention:
- YYYY-MM-DD = Date of session
- NNN = Session number for that day (001, 002, ...)

---

*This index is part of the episodic memory system.*
*It prevents agent amnesia by preserving context across sessions.*

