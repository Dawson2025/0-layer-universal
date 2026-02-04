# Episodic Memory Architecture

**Date**: 2026-01-30
**Stage**: stage_-1_04_design
**Status**: FINISHED - Ready for Planning
**Revision**: 1.0

---

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────┐
│                  Episodic Memory System                           │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │          Session Start (Agent Checks History)              │  │
│  │  - Read outputs/episodic/index.md (quick summary)          │  │
│  │  - Read outputs/episodic/sessions/[latest].md (context)   │  │
│  │  - Read relevant output files from previous session        │  │
│  └────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         During Session (Agent Logs Work)                   │  │
│  │  - Write outputs to files FIRST (output-first protocol)   │  │
│  │  - Update outputs/episodic/changes/progress.md            │  │
│  │  - Log to divergence.log if multi-agent                   │  │
│  │  - Log conflicts if detected                              │  │
│  └────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │         Session End (Agent Creates Record)                 │  │
│  │  - Create outputs/episodic/sessions/[session].md          │  │
│  │  - Update outputs/episodic/index.md                       │  │
│  │  - Archive old sessions if needed (>50 sessions)          │  │
│  │  - Commit and push                                         │  │
│  └────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │    Next Session (Agent Reads History, Resumes)            │  │
│  │  - Cycle repeats with full context from episodic memory   │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

---

## Component 1: Session Logging

### Design

**Session File Location**: `outputs/episodic/sessions/YYYY-MM-DD_session_NNN.md`

**Session File Format**:

```markdown
# Session YYYY-MM-DD_NNN

**Date**: YYYY-MM-DD
**Start Time**: HH:MM:SS UTC
**End Time**: HH:MM:SS UTC
**Duration**: MM minutes
**Agent**: [agent_role/stage]
**Status**: COMPLETED / IN_PROGRESS / BLOCKED

---

## Summary

[1-2 sentence summary of what was accomplished]

## Objectives

- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

## Accomplishments

- [x] Completed task 1: [description]
- [x] Completed task 2: [description]
- [ ] Partial task 3: [what remains]

---

## Findings

### Major Findings
- Finding 1 with impact
- Finding 2 with implications

### Technical Discoveries
- Discovery 1
- Discovery 2

---

## Outputs Created

| File | Type | Description |
|------|------|-------------|
| `outputs/01_understanding/file1.md` | Research | Topic 1 analysis |
| `outputs/02_finished/file2.md` | Documentation | Topic 2 guide |

---

## Files Modified

| File | Change Type | What Changed |
|------|------------|--------------|
| `agnostic-sync.sh` | Updated | Changed naming convention |
| `0AGNOSTIC.md` | Updated | Added new section |

---

## Issues & Resolutions

| Issue | Severity | Resolution | Status |
|-------|----------|-----------|--------|
| System scale misunderstood | HIGH | User clarified: 5,930+ nodes | RESOLVED |
| Path clickability | MEDIUM | Implemented cursor://file/ URLs | RESOLVED |

---

## Decisions Made

| Decision | Rationale | Impact |
|----------|-----------|--------|
| Don't adopt external frameworks | Tool lock-in risk | Keep custom system |
| Implement file locking Phase 1 | Prevents conflicts | Deferred complex CRDT |

---

## Next Steps

1. Move to instruction stage (03)
2. Create [specific instruction documents]
3. Transition to design stage (04)

---

## Resources Used

- Perplexity: SHIMI research
- Internal: Previous session files
- User: Clarifications on architecture

---

## Related Sessions

- [Previous session date]: [link to notes]
- [Next session date]: [link to notes]

---

## Notes & Observations

[Any additional notes about this session]
```

### Session Naming

**Format**: `YYYY-MM-DD_session_NNN.md`

**Rules**:
- `YYYY-MM-DD`: Date of session start
- `NNN`: Sequential number (001, 002, etc.)
- If multiple sessions per day: increment NNN
- Example: `2026-01-30_session_001.md`, `2026-01-30_session_002.md`

---

## Component 2: Change Tracking

### Design

**Location**: `outputs/episodic/changes/`

**Files**:

1. **divergence.log** (Multi-agent sync tracking)
   ```
   Timestamp | Agent | Scope | Action | Hash Before | Hash After
   2026-01-30T14:23:45Z | agent_research | outputs_research | CREATED | initial | abc123
   2026-01-30T14:25:12Z | agent_research | outputs_research | MODIFIED | abc123 | def456
   ```

2. **conflicts.log** (Conflict history)
   ```
   Timestamp | File | Agents | Resolution | Winner | Timestamp
   2026-01-30T14:30:00Z | task.md | research, design | last-write-wins | design | 14:27:45
   ```

3. **[date]_progress.md** (Intra-session progress)
   ```
   # Session Progress - 2026-01-30

   ## 14:23 - Session Start
   - Read previous session notes
   - Identified current tasks
   - Started research phase

   ## 14:35 - Research SHIMI
   - Found April 2025 paper
   - Documented three mechanisms
   - Created comparison table

   ## 14:50 - Write Documentation
   - Created multi_agent_sync_protocol.md
   - Defined constraints
   - Ready to move to instruction stage
   ```

---

## Component 3: Episodic Index

### Design

**Location**: `outputs/episodic/index.md`

**Purpose**: Quick navigation through episodic memory

**Content**:

```markdown
# Episodic Memory Index

**Last Updated**: 2026-01-30
**Total Sessions**: 5
**Archive Size**: 2 archives (Q1 2026, Q2 2026)

---

## Recent Sessions

| Date | Agent | Duration | Status | Summary |
|------|-------|----------|--------|---------|
| 2026-01-30 | research_01 | 47m | COMPLETED | SHIMI research + multi-agent design |
| 2026-01-29 | research_01 | 32m | COMPLETED | Framework comparison |
| 2026-01-28 | design_01 | 58m | IN_PROGRESS | Context system design |

---

## By Topic

### Multi-Agent Sync
- Session 2026-01-30_001: Initial protocol design
- Session 2026-01-29_002: Conflict resolution

### Memory Systems
- Session 2026-01-29_001: Framework analysis
- Session 2026-01-28_003: Memory architecture

### AGNOSTIC System
- Session 2026-01-30_001: Includes AGNOSTIC design section

---

## Key Decisions

| Decision | Date | Status | Impact |
|----------|------|--------|--------|
| Multi-agent sync Phase 1 | 2026-01-30 | APPROVED | Implement file locking |
| Use 0AGNOSTIC naming | 2026-01-30 | APPROVED | Explicit ordering in listings |
| Don't adopt frameworks | 2026-01-30 | APPROVED | Keep custom system |

---

## Open Issues

| Issue | Discovered | Status | Next Action |
|-------|-----------|--------|-------------|
| System scale | 2026-01-30 | RESOLVED | Document architectural implications |
| Automated traversal | 2026-01-30 | IN_PROGRESS | Design /find skill |

---

## Archives

- `archived_2026_Q1/`: 40+ sessions from Jan-Mar 2026
- `archived_2026_Q2/`: 35+ sessions from Apr-Jun 2026

---

## How to Use Episodic Memory

### To Understand History
1. Read index.md (this file)
2. Find relevant session
3. Read YYYY-MM-DD_session_NNN.md

### To Resume Work
1. Read latest session
2. Check what was accomplished
3. Read outputs created in that session
4. Continue from where you left off

### To Find Something Specific
1. Use /find skill to navigate
2. Or search index.md for keywords
3. Check related sessions
```

---

## Component 4: Compaction

### Design

**When to Compact**:
- More than 50 session files
- Total episodic/ directory > 10MB
- Quarterly (every 3 months)

**Compaction Process**:

```
Function: compact_episodic_memory(age_threshold_days=90):
  old_sessions = []

  // Find sessions older than threshold
  for session_file in outputs/episodic/sessions/:
    if file_age(session_file) > age_threshold_days:
      old_sessions.append(session_file)

  if not old_sessions:
    log("No sessions to archive")
    return

  // Create archive directory
  quarter = determine_quarter(old_sessions[0].date)
  archive_dir = f"outputs/episodic/sessions/archived_{quarter}/"
  mkdir(archive_dir)

  // Move old sessions
  for session in old_sessions:
    move(session, archive_dir + session.name)

  // Create summary of archived sessions
  summary = {
    "period": quarter,
    "session_count": len(old_sessions),
    "key_topics": extract_topics(old_sessions),
    "major_decisions": extract_decisions(old_sessions),
    "open_issues": extract_issues(old_sessions)
  }

  write(archive_dir + "SUMMARY.md", summary)

  // Update index
  update_index(archive_dir)

  log(f"Archived {len(old_sessions)} sessions to {archive_dir}")
```

**Archive Summary Format**:

```markdown
# Archived Sessions - Q1 2026

**Period**: January 1 - March 31, 2026
**Session Count**: 42
**Time Span**: 90 days

---

## Summary

Intensive research and design phase. Major focus on multi-agent architecture and SHIMI framework analysis.

---

## Key Topics

| Topic | Sessions | Major Finding |
|-------|----------|---------------|
| Multi-agent sync | 18 | File locking prevents 80% of conflicts |
| Memory systems | 15 | Three-layer architecture recommended |
| AGNOSTIC system | 9 | 0AGNOSTIC + .0agnostic/ dual approach |

---

## Major Decisions

- Adopted 0AGNOSTIC naming convention (2026-01-28)
- Chose not to use external frameworks (2026-01-30)
- File locking Phase 1 priority (2026-01-30)

---

## Open Issues Carried Forward

- Automated traversal /find skill (design in progress)
- Design stage implementation (starting 2026-02-01)
- Performance optimization (future work)
```

---

## Component 5: Integration with Output-First Protocol

### Design

**Flow**:

```
Session Starts:
  1. Agent reads episodic memory
     └─ outputs/episodic/index.md
     └─ outputs/episodic/sessions/[latest].md
     └─ Relevant output files

  2. Agent understands context
     └─ What was accomplished last session?
     └─ What's in progress?
     └─ What are open issues?

During Work:
  3. Agent writes to outputs/ FIRST
     └─ outputs/01_understanding_in_progress/
     └─ outputs/02_finished_instructions/
     └─ outputs/03_design_decisions/

  4. Agent updates episodic tracking
     └─ outputs/episodic/changes/progress.md
     └─ outputs/episodic/changes/divergence.log

Session Ends:
  5. Agent creates session record
     └─ outputs/episodic/sessions/YYYY-MM-DD_NNN.md
     └─ Updates index.md
     └─ Commits and pushes

Next Session:
  6. Agent resumes (cycle repeats)
     └─ Reads episodic memory from previous session
     └─ Continues with full context
     └─ No "amnesia" - continuity preserved
```

---

## Data Structure

### Session File Fields

| Field | Type | Required | Purpose |
|-------|------|----------|---------|
| Date | String | Yes | When did this session occur? |
| Start Time | Timestamp | Yes | When did agent start? |
| Duration | Integer | Yes | How long was the session? |
| Agent | String | Yes | Who/what ran this session? |
| Status | Enum | Yes | Completed/In-Progress/Blocked? |
| Summary | Text | Yes | 1-2 sentence overview |
| Outputs Created | List | Yes | What files were created? |
| Files Modified | List | No | What was changed? |
| Issues | Table | No | Problems encountered |
| Next Steps | List | Yes | What's next? |

### Divergence Log Format

| Field | Type | Purpose |
|-------|------|---------|
| Timestamp | ISO8601 | When did this change occur? |
| Agent | String | Which agent made the change? |
| Scope | String | What area was affected? |
| Action | Enum | CREATED / MODIFIED / DELETED? |
| Hash Before | String | Hash before change |
| Hash After | String | Hash after change |

---

## Query Patterns

### "What happened in the last session?"

```
SELECT * FROM sessions ORDER BY date DESC LIMIT 1
→ Read: outputs/episodic/sessions/[latest].md
```

### "What topics have been researched?"

```
SELECT DISTINCT topic FROM index.md topics section
→ Read: outputs/episodic/index.md
```

### "Have I worked on X before?"

```
SEARCH sessions FOR keywords matching X
→ Use /find skill or search index.md
```

### "What changed since I last checked?"

```
SELECT * FROM divergence.log WHERE timestamp > last_checked_time
→ Read: outputs/episodic/changes/divergence.log
```

---

## Testing Strategy

### Unit Tests

- [ ] Session file created with correct format
- [ ] Session file has all required fields
- [ ] Index.md updates correctly
- [ ] Divergence.log entries parse correctly
- [ ] Conflict.log entries parse correctly

### Integration Tests

- [ ] Session → Index linking works
- [ ] Archive → Summary generation works
- [ ] Old sessions → Archive migration works
- [ ] Restoration from archive works

### Continuity Tests

- [ ] Agent can read previous session and understand context
- [ ] Agent can find outputs from previous session
- [ ] Agent can resume work mid-project
- [ ] Multi-session projects maintain consistency

---

## Implementation Checklist

- [ ] Design session file format and template
- [ ] Implement session file creation
- [ ] Create index.md template
- [ ] Implement index.md updates
- [ ] Create divergence.log format
- [ ] Create conflicts.log format
- [ ] Implement compaction algorithm
- [ ] Create archive summary generator
- [ ] Integrate with output-first protocol
- [ ] Create session retrieval functions
- [ ] Test session continuity across gaps

