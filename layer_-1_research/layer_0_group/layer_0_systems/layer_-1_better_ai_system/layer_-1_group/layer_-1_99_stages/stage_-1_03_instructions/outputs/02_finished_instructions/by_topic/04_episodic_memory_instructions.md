# Episodic Memory Instructions

**Date**: 2026-01-30
**Stage**: stage_-1_03_instructions
**Status**: FINISHED - Ready for Design
**Revision**: 1.0

---

## Overview

**Episodic Memory** = Timestamped record of what agents did in past sessions.

Solves: "What did I work on before? What changed? What's the status?"

**Three-Layer Memory Architecture:**

1. **Immediate** (this session): Current CLAUDE.md + context files
2. **Episodic** (recent past): Completed work, timestamped, searchable
3. **Semantic** (deep past): Knowledge base, principles, patterns

This document focuses on **Episodic Memory** - what agents need to remember across sessions.

---

## Constraint 1: Episodic Memory Structure

### Purpose

Maintain a searchable history of past agent work so agents can:
- Answer "What did I work on last?" without re-reading everything
- Resume work mid-project
- Understand context from previous sessions
- Track changes and decisions over time

### Directory Structure

```
outputs/episodic/
├── 0INDEX.md              ← Navigate episodic memory
├── sessions/
│   ├── 2026-01-30_session_001.md
│   ├── 2026-01-30_session_002.md
│   └── 2026-01-31_session_001.md
├── changes/
│   ├── divergence.log     ← What files changed (for multi-agent sync)
│   ├── conflicts.log      ← Conflicts encountered and resolved
│   └── 2026-01-30_changes_summary.md
└── index.md               ← Quick search/navigation
```

### Session Files

**File naming**: `YYYY-MM-DD_session_NNN.md`

**Content**:

```markdown
# Session 2026-01-30_001

**Date**: 2026-01-30
**Time**: 14:23:45 UTC
**Duration**: 47 minutes
**Agent**: research_01 (stage_-1_02_research)
**Status**: COMPLETED

---

## Summary

Researched multi-agent sync mechanisms and SHIMI framework. Created documentation on conflict prevention, change tracking, and conflict resolution strategies.

---

## Tasks Completed

- [x] Research SHIMI framework (Merkle-DAG, Bloom filters, CRDTs)
- [x] Compare your system to SHIMI
- [x] Document multi-agent sync protocol
- [x] Analyze automated traversal requirements
- [x] Create system scale analysis

---

## Outputs Created

- `outputs/01_understanding_in_progress/by_topic/multi_agent_parallel_execution_insight.md`
- `outputs/01_understanding_in_progress/by_topic/system_comparison_and_recommendations.md`
- `outputs/01_understanding_in_progress/by_topic/updated_understanding_system_scale.md`

---

## Key Findings

1. System is TRUE multi-agent with parallel execution
2. 5,930+ nodes require automated traversal
3. SHIMI concepts relevant for sync (Merkle-DAG, CRDTs)
4. File locking + atomic writes prevent most conflicts

---

## Files Modified

| File | Change |
|------|--------|
| `agnostic-sync.sh` | Updated naming (AGNOSTIC→0AGNOSTIC) |
| `.0agnostic/` | Created template structure |

---

## Issues Encountered

| Issue | Resolution |
|-------|-----------|
| System scale misunderstood | User clarified: 5,930+ nodes, nested layers |
| Multi-agent nature unclear | User explained: CLI tools spawn agents in parallel |
| Path clickability | Researched: cursor://file/ URLs work in Cursor IDE |

---

## Next Steps

1. Move to instruction stage (03)
2. Create multi-agent sync protocol
3. Create automated traversal design
4. Move to design stage (04)

---

## Resources Used

- Perplexity: SHIMI research, Memory Tool API
- Internal: system_comparison_and_recommendations.md
- User clarification: Architecture explanations

---

## Notes

- Research is comprehensive but implementation not started
- Design will specify how to implement these protocols
- Multi-agent sync is critical for parallel execution safety
```

### Change Logs

**File**: `outputs/episodic/changes/divergence.log`

**Purpose**: Track what changed between sessions (for multi-agent sync)

**Format**:
```
2026-01-30T14:23:45Z | agent_research_01 | outputs/01_understanding | MODIFIED | hash_abc123→hash_def456
2026-01-30T14:45:12Z | agent_design_01 | outputs/02_finished_instructions | CREATED | none→hash_xyz789
2026-01-30T15:12:33Z | agent_research_01 | hand_off_documents/incoming | MODIFIED | hash_uvw012→hash_lmn345
```

**File**: `outputs/episodic/changes/conflicts.log`

**Purpose**: Document conflicts encountered and how they were resolved

**Format**:
```
2026-01-30T14:30:00Z | CONFLICT | hand_off_documents/task.md | agent_research_01 vs agent_design_01 | RESOLVED | last-write-wins | timestamps: research=14:25:12, design=14:27:45 | winner=design_01
```

---

## Constraint 2: Session Logging Protocol

### Purpose

Ensure every agent session creates a record that future agents can read to understand what happened.

### Before Session Starts

**Check incoming sessions log**:

```bash
# Read most recent session to understand context:
cat outputs/episodic/sessions/$(ls outputs/episodic/sessions/ | tail -1)
```

**This answers:**
- What was I working on?
- What's the current status?
- What did the last agent complete?

### During Session

**Log work as you go** (output-first protocol):

```bash
# In outputs/episodic/changes/2026-01-30_progress.md:

## 14:23 - Start session
- Read previous session notes
- Identified unfinished research tasks
- Starting multi-agent sync protocol document

## 14:35 - Research SHIMI
- Found April 2025 paper on hierarchical memory
- Documented Merkle-DAG, Bloom filters, CRDTs
- Started comparison to existing system

## 14:45 - Write multi_agent_sync_protocol.md
- Defined file locking constraint
- Defined atomic writes constraint
- Defined change detection constraint
```

### After Session Complete

**Create final session file**:

```bash
# Create outputs/episodic/sessions/YYYY-MM-DD_session_NNN.md
# Include:
# - Summary of what was accomplished
# - Tasks completed
# - Outputs created
# - Key findings
# - Issues encountered and resolutions
# - Next steps
```

### Episodic Index

**File**: `outputs/episodic/index.md`

**Purpose**: Quick search through episodic memory

**Content**:

```markdown
# Episodic Memory Index

## Recent Sessions

| Date | Agent | Duration | Status | Summary |
|------|-------|----------|--------|---------|
| 2026-01-30 | research_01 | 47m | COMPLETED | SHIMI research, multi-agent sync protocol |
| 2026-01-29 | research_01 | 32m | COMPLETED | Memory system analysis, framework comparison |
| 2026-01-28 | design_01 | 58m | IN_PROGRESS | Design phase for agent context system |

## By Topic

### Multi-Agent Sync
- Session 2026-01-30_001: Initial multi-agent sync protocol
- Session 2026-01-29_002: Conflict resolution strategies

### Memory Systems
- Session 2026-01-29_001: Framework analysis (MemGPT, Mem0, Chroma)
- Session 2026-01-28_003: Three-layer memory architecture

### Automated Traversal
- Session 2026-01-30_001: Includes traversal requirements section
- Session 2026-01-28_002: Initial 0INDEX.md design

## Open Issues

| Issue | Discovered | Status |
|-------|-----------|--------|
| System scale misunderstood | 2026-01-30 | RESOLVED (5,930+ nodes clarified) |
| Path clickability in terminal | 2026-01-30 | RESOLVED (cursor://file/ URLs) |

## Key Decisions

| Decision | Date | Rationale |
|----------|------|-----------|
| Don't adopt external frameworks | 2026-01-30 | Tool lock-in, lose agnostic advantage |
| Implement file locking Phase 1 | 2026-01-30 | Prevents 80% of conflicts |
| Add 0INDEX.md at branching points | 2026-01-30 | Enables automated traversal at scale |

## Resources Created

### Instructions (Completed)
- 01_multi_agent_sync_protocol.md
- 02_automated_traversal_instructions.md
- 03_agnostic_system_implementation.md
- 04_episodic_memory_instructions.md
- 05_system_integration_guide.md (pending)

### Research (Completed)
- SHIMI framework analysis
- System comparison to frameworks
- Memory architecture design
- Multi-agent execution understanding
```

---

## Constraint 3: Memory Compaction (When Session Notes Get Large)

### Problem

After 50+ sessions, episodic memory grows large. Old session files become less relevant.

### Solution: Episodic Compaction

**When to compact**:
- More than 50 session files
- Total episodic/ size > 10MB
- Quarterly (every 3 months)

**Compaction process**:

1. **Archive old sessions** (>3 months):
   ```bash
   mkdir outputs/episodic/sessions/archived_2026_Q1/
   mv outputs/episodic/sessions/2026-01-* outputs/episodic/sessions/archived_2026_Q1/
   ```

2. **Create summary** of archived sessions:
   ```markdown
   # Archived Sessions - Q1 2026

   ## Summary
   50 sessions completed, focus on research and design phases.

   ## Key Topics
   - Multi-agent system architecture: 18 sessions
   - Memory optimization: 15 sessions
   - Sync protocol design: 12 sessions
   - Other: 5 sessions

   ## Major Decisions
   - Adopted 0AGNOSTIC system (session 2026-01-27)
   - Determined file locking Phase 1 (session 2026-01-30)
   - Chose not to adopt external frameworks (session 2026-01-29)

   ## Open Issues Carried Forward
   - Automated traversal /find skill (in progress)
   - Design phase starting 2026-02-01
   ```

3. **Update index.md** to reference archived summaries

4. **Keep recent sessions** accessible (current + 3 months)

---

## Integration with Output-First Protocol

### Output-First Protocol Recap

**Before ANY response:**
1. Write output to file in `outputs/`
2. Update episodic memory
3. Then respond to user

### Episodic Memory + Output-First = Session Continuity

```
Session 1:
  └─ Writes: research_output.md to outputs/01_understanding/
  └─ Logs: session_001.md to outputs/episodic/sessions/
  └─ Updates: divergence.log with changes

Session 2 (weeks later):
  ├─ Reads: outputs/episodic/sessions/session_001.md (what happened before?)
  ├─ Reads: outputs/01_understanding/ (where did I leave off?)
  ├─ Reads: divergence.log (what changed since session 1?)
  └─ Resumes work without losing context
```

### CLAUDE.md Integration

Each agent CLAUDE.md should include:

```markdown
## Output-First + Episodic Memory Protocol

### Session Start
1. Read `outputs/episodic/index.md` - understand recent history
2. Read `outputs/episodic/sessions/[latest].md` - what was last session about?
3. Read relevant output files from `outputs/01_*`

### During Session
1. Write findings to `outputs/` FIRST
2. Update `outputs/episodic/changes/` with what changed
3. Keep `outputs/episodic/progress.md` (daily log)

### Session End
1. Finalize all output files
2. Create `outputs/episodic/sessions/YYYY-MM-DD_session_NNN.md`
3. Update `outputs/episodic/index.md`
4. Commit and push
```

---

## Success Criteria

✅ **Episodic memory is working when:**

1. Every session creates a record in outputs/episodic/sessions/
2. Agent can read previous session notes to understand context
3. Changes are logged and searchable in divergence.log
4. Conflicts are documented in conflicts.log
5. Index is up-to-date and makes memory searchable

❌ **Needs improvement if:**

1. Sessions don't get logged (gaps in history)
2. Agent can't find previous work (index is stale)
3. Changes tracked poorly (don't know what changed since last session)
4. Episodic memory grows too large (need compaction)
5. Old decisions forgotten (no decision log)

---

## Implementation Checklist

- [ ] Create outputs/episodic/ folder structure
- [ ] Create 0INDEX.md in outputs/episodic/
- [ ] Create index.md template
- [ ] Create session file template
- [ ] Update CLAUDE.md to include episodic logging
- [ ] Create divergence.log format specification
- [ ] Create conflicts.log format specification
- [ ] Document compaction process
- [ ] Set up quarterly compaction schedule
- [ ] Train all agents on episodic memory protocol

---

## Templates

### Session File Template

```markdown
# Session YYYY-MM-DD_NNN

**Date**: YYYY-MM-DD
**Start Time**: HH:MM:SS UTC
**Duration**: MM minutes
**Agent**: [agent_name]
**Status**: COMPLETED / IN_PROGRESS / BLOCKED

---

## Summary

[1-2 sentence summary of what was accomplished]

---

## Tasks

- [ ] Task 1
- [ ] Task 2

---

## Outputs

- New file: [path]
- Modified: [path]

---

## Key Findings

[Bullet list of major findings]

---

## Issues

| Issue | Resolution |
|-------|-----------|

---

## Next Steps

1. Next action
2. Next action
```

### Progress Log Template

```markdown
# Session Progress - YYYY-MM-DD

## Timestamp HH:MM
- Action taken
- Findings
- Decision

## Timestamp HH:MM
- Action taken
- Findings
- Decision
```

