# System Integration Architecture

**Date**: 2026-01-30
**Stage**: stage_-1_04_design
**Status**: FINISHED - Ready for Planning
**Revision**: 1.0

---

## System Overview

```
┌───────────────────────────────────────────────────────────────────┐
│         Complete AI Agent Memory & Execution System               │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Layer 1: Context Discovery                                       │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  0AGNOSTIC.md (lean context)                               │  │
│  │  ↓ Referenced by ↓                                          │  │
│  │  .0agnostic/ (detailed resources)                           │  │
│  │  ↓ Generated from ↓                                         │  │
│  │  CLAUDE.md / AGENTS.md / GEMINI.md (tool-specific)          │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  Layer 2: Discovery at Scale                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  /find skill (automated traversal)                          │  │
│  │  ↓ Reads ↓                                                  │  │
│  │  0INDEX.md at each level (semantic indices)                 │  │
│  │  ↓ Enabling ↓                                               │  │
│  │  Context discovery without manual navigation                │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  Layer 3: Safe Parallel Execution                                 │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Lock Manager (prevent conflicts)                           │  │
│  │  ↓ + ↓                                                      │  │
│  │  Atomic Writes (prevent data corruption)                    │  │
│  │  ↓ + ↓                                                      │  │
│  │  Change Detector (track what changed)                       │  │
│  │  ↓ + ↓                                                      │  │
│  │  Conflict Resolver (deterministic merge)                    │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│  Layer 4: Session Continuity                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Episodic Memory System                                     │  │
│  │  ├─ sessions/: timestamped session records                  │  │
│  │  ├─ changes/: divergence.log, conflicts.log                │  │
│  │  ├─ index.md: searchable memory                             │  │
│  │  └─ Compaction: archive old sessions                        │  │
│  │                                                              │  │
│  │  ↓ Enables ↓                                                │  │
│  │                                                              │  │
│  │  Next agent reads previous session                          │  │
│  │  → Understands context without "amnesia"                    │  │
│  │  → Continues work seamlessly                                │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                           ▼                                       │
│         Output: Full System Context Preservation                  │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

---

## Data Flow: Complete Workflow

### Session 1: Initial Research (Day 1)

```
┌─ START: research_01 enters stage_-1_02_research
│
├─ STEP 1: Context Discovery (AGNOSTIC System)
│  ├─ Read: 0AGNOSTIC.md (200 tokens)
│  │  └─ Identity: "I'm research agent"
│  │  └─ Navigation: ".0agnostic/ for details"
│  │  └─ Triggers: "Need research protocol? Load .0agnostic/rules/"
│  │
│  └─ Load: .0agnostic/rules/research_protocol.md (on-demand)
│
├─ STEP 2: Discovery at Scale (Automated Traversal)
│  ├─ Query: "What needs research?"
│  │
│  └─ /find traversal:
│     ├─ Level 0: ~/  →  0INDEX.md  → "layer_-1_research"
│     ├─ Level 1: layer_-1_group/ → "better_ai_system"
│     ├─ Level 2: layer_-1_99_stages/ → "stage_-1_02_research"
│     └─ Result: Discovered 15 requirements in Tree of Needs
│
├─ STEP 3: Safe Parallel Execution (Multi-Agent Sync)
│  ├─ Acquire lock: .locks/outputs_research_research_01.lock
│  │  └─ "I now have exclusive write access to outputs/"
│  │
│  ├─ Do work:
│  │  ├─ Write: outputs/01_understanding_in_progress/by_topic/shimi_research.md
│  │  ├─ Write: outputs/01_understanding_in_progress/by_topic/system_comparison.md
│  │  └─ Update: outputs/episodic/changes/progress.md
│  │
│  └─ Release lock: rm .locks/outputs_research_research_01.lock
│     └─ "Other agents can now acquire lock"
│
├─ STEP 4: Change Tracking (Divergence Detection)
│  ├─ Hash before: initial (no files)
│  ├─ Hash after: hash_abc123
│  ├─ Update divergence.log:
│  │  "2026-01-30T14:25:00 | research_01 | outputs | CREATED | initial → hash_abc123"
│  └─ Propagate to dependent agents: "outputs changed!"
│
└─ STEP 5: Session Continuity (Episodic Memory)
   ├─ Create: outputs/episodic/sessions/2026-01-30_session_001.md
   │  ├─ Summary: "Researched SHIMI framework and system comparison"
   │  ├─ Outputs Created: [list of files]
   │  ├─ Next Steps: "Move to instruction stage"
   │  └─ Status: COMPLETED
   │
   ├─ Update: outputs/episodic/index.md
   │  ├─ Add session entry with summary
   │  ├─ Update "Recent Sessions" table
   │  └─ Update "Key Decisions" section
   │
   └─ Commit & Push
      ├─ git add 0AGNOSTIC.md .0agnostic/
      ├─ git add outputs/01_understanding/ outputs/episodic/
      └─ git push


END OF SESSION 1 → Research complete, full context preserved
```

### Session 2: Design Work (Days 3-5, different agent)

```
┌─ START: design_01 enters stage_-1_04_design
│
├─ STEP 1: Understand History (Episodic Memory)
│  ├─ Read: outputs/episodic/index.md
│  │  └─ "Recent session on 2026-01-30 did SHIMI research"
│  │
│  ├─ Read: outputs/episodic/sessions/2026-01-30_session_001.md
│  │  └─ "Research completed on multi-agent sync, AGNOSTIC system, episodic memory"
│  │
│  └─ Read: outputs/01_understanding_in_progress/by_topic/system_comparison.md
│     └─ "Research recommends file locking Phase 1, SHIMI concepts relevant"
│
├─ STEP 2: Context Setup (AGNOSTIC System)
│  ├─ Read: 0AGNOSTIC.md (200 tokens)
│  │  └─ Identity: "I'm design agent for stage 04"
│  │
│  └─ Load: .0agnostic/rules/design_protocol.md (on-demand)
│
├─ STEP 3: Dependency Awareness (Change Detection)
│  ├─ Read: outputs/episodic/changes/divergence.log
│  │  ├─ Hash of research outputs: hash_abc123
│  │  └─ Current hash: hash_abc123 (no changes since session 1)
│  │
│  └─ Decision: "Research stable, can proceed with design based on it"
│
├─ STEP 4: Do Design Work (Safe Execution)
│  ├─ Acquire lock: .locks/outputs_design_design_01.lock
│  │
│  ├─ Create design documents:
│  │  ├─ outputs/03_design_decisions/by_topic/multi_agent_sync_design.md
│  │  ├─ outputs/03_design_decisions/by_topic/traversal_design.md
│  │  └─ outputs/03_design_decisions/by_topic/agnostic_design.md
│  │
│  └─ Release lock: rm .locks/outputs_design_design_01.lock
│
├─ STEP 5: Track Changes (For Next Agent)
│  ├─ Update divergence.log:
│  │  "2026-01-31T10:45:00 | design_01 | outputs_design | CREATED | initial → hash_xyz789"
│  │
│  └─ Propagate: "Design outputs created!"
│
└─ STEP 6: Create Session Record (Episodic Memory)
   ├─ Create: outputs/episodic/sessions/2026-01-31_session_001.md
   │  ├─ Summary: "Designed multi-agent sync, traversal, AGNOSTIC systems"
   │  ├─ Dependencies: "Built on research from 2026-01-30_session_001"
   │  └─ Status: COMPLETED
   │
   └─ Next agent will read this and continue seamlessly


END OF SESSION 2 → Design complete, full history available for planning stage
```

### Session 3: Parallel Execution (Both agents running)

```
┌─ Timeline: 2026-02-01, 10:00 UTC
│
├─ 10:00:00 - Research Agent Starts
│  ├─ Acquire lock: .locks/research_outputs.lock ✓
│  └─ Start work
│
├─ 10:00:15 - Design Agent Starts (Parallel)
│  ├─ Try to acquire lock: .locks/design_outputs.lock ✓
│  │  └─ Different scope, no conflict
│  └─ Start work independently
│
├─ 10:05:00 - Research Agent Still Working
│  ├─ Still holds: .locks/research_outputs.lock
│  └─ Updates research findings
│
├─ 10:05:30 - Review Agent Starts (Also Parallel)
│  ├─ Try to acquire: .locks/review_outputs.lock ✓
│  │  └─ Different scope, no conflict
│  └─ Can work independently
│
├─ 10:08:45 - Research Agent Completes
│  ├─ Release: .locks/research_outputs.lock
│  ├─ Update divergence.log: research changed hash_a → hash_b
│  ├─ Notify dependents: "Research outputs changed!"
│  └─ Create: outputs/episodic/sessions/2026-02-01_session_001.md
│
├─ 10:09:00 - Design Agent Checks for Changes
│  ├─ Read divergence.log
│  ├─ See: research changed hash_a → hash_b
│  ├─ Action: Re-read research outputs to incorporate changes
│  ├─ Continue work with updated context
│  └─ (No need to acquire research lock, just read)
│
├─ 10:12:30 - Design Agent Completes
│  ├─ Release: .locks/design_outputs.lock
│  ├─ Update divergence.log
│  └─ Create: outputs/episodic/sessions/2026-02-01_session_002.md
│
└─ 10:15:00 - Review Agent Completes
   ├─ Release: .locks/review_outputs.lock
   ├─ Create: outputs/episodic/sessions/2026-02-01_session_003.md
   │
   └─ All three sessions (parallel execution) fully documented


RESULT: Three agents executed in parallel, all changes tracked, all sessions recorded
         No conflicts, no data loss, full audit trail
```

---

## Architecture Layers

### Layer 1: Tool Portability (AGNOSTIC System)

**Problem**: Lock into one AI tool (Claude, AutoGen, Gemini, etc.)

**Solution**:
```
0AGNOSTIC.md (source of truth)
  ↓ (agnostic-sync.sh transformation)
  ├─ CLAUDE.md (Claude Code)
  ├─ AGENTS.md (AutoGen)
  ├─ GEMINI.md (Google Gemini)
  └─ OPENAI.md (OpenAI)

Same context, different tool. No lock-in.
```

**Design Specifications**:
- 0AGNOSTIC.md: 200-400 tokens max (fits all context windows)
- .0agnostic/: Detailed resources (loaded on-demand)
- agnostic-sync.sh: Transformation script (deterministic)

### Layer 2: Discovery at Scale (Automated Traversal)

**Problem**: 5,930+ nodes, manual navigation doesn't scale

**Solution**:
```
0INDEX.md at key branching points
  ↓ (semantic indices with keywords)
/find skill (LLM-based child selection)
  ↓ (recursive descent)
Automatic discovery in 3-5 steps

No manual "read this file, then that file"
```

**Design Specifications**:
- 0INDEX.md format: markdown tables with keywords
- /find algorithm: preprocess → select → recurse → validate
- LLM fallback: keyword overlap if LLM selection invalid

### Layer 3: Safe Parallel Execution (Multi-Agent Sync)

**Problem**: Multiple agents writing simultaneously → conflicts, data loss

**Solution**:
```
File locking (prevent concurrent writes)
  + Atomic writes (prevent data corruption)
  + Change detection (track divergence)
  + Conflict resolution (deterministic merge)

4-tier approach: prevent > detect > resolve > optimize
```

**Design Specifications**:
- Locks: .locks/[scope]_[agent].lock (5 min TTL)
- Writes: temp file → atomic rename
- Detection: Merkle-DAG hash before/after
- Resolution: last-write-wins with timestamps

### Layer 4: Session Continuity (Episodic Memory)

**Problem**: Agent amnesia - no memory of previous sessions

**Solution**:
```
Every session creates timestamped record
  + Previous agent can read it
  + Current context preserved across gaps
  + No context loss, full audit trail

Agents don't restart from scratch
```

**Design Specifications**:
- Session files: YYYY-MM-DD_session_NNN.md
- Episodic index: Searchable summary (index.md)
- Change tracking: divergence.log, conflicts.log
- Compaction: Archive >90 day old sessions

---

## Integration Points

### AGNOSTIC → TRAVERSAL

```
0AGNOSTIC.md mentions:
  "For detailed resources, see .0agnostic/"

Agent uses /find:
  /find "Find detailed resources"
  → Navigates to .0agnostic/ directory
  → Discovers available skills, rules, agents
```

### TRAVERSAL → SYNC

```
/find discovers research outputs
  → Agent reads outputs/01_understanding/

Before modifying outputs/:
  → Acquire lock (multi-agent sync)
  → Read divergence.log (what changed?)
  → Proceed with work
```

### SYNC → EPISODIC

```
Agent modifies outputs/
  → Updates divergence.log (change tracking)
  → Creates session file (episodic record)

Next agent:
  → Reads episodic/sessions/
  → Understands what happened
  → Resumes with full context
```

### EPISODIC → TRAVERSAL (Full Cycle)

```
Next session starts:
  → Read episodic/index.md (what happened before?)
  → Use /find to navigate to relevant outputs/
  → Read discovered outputs
  → Continue work

No amnesia. Full context. Seamless continuity.
```

---

## Error Handling & Recovery

### Deadlock

**Scenario**: Agent A holds lock for 10 minutes (frozen)

**Detection**:
```
Agent B tries to acquire lock
Lock age check: 10 min > 5 min TTL
→ Lock is stale
```

**Recovery**:
```
1. Clean up stale lock (rm .locks/...)
2. Log: "Cleaned stale lock for agent_A"
3. Agent B acquires lock
4. Continue
```

### Data Corruption

**Scenario**: Agent A crashes while writing

**Prevention**:
```
Write to .tmp file first
Atomic rename to final file
If crash during write:
  → .tmp file exists but .final doesn't
  → Recovery: delete .tmp, try again
```

**Recovery**:
```
1. Detect .tmp files on startup
2. Delete orphaned .tmp files
3. Verify data integrity
4. Continue
```

### Sync Conflict (Multi-Device)

**Scenario**: Two machines modify same file (Syncthing sync)

**Detection**:
```
Syncthing creates: file.md.sync-conflict-[timestamp]
```

**Recovery**:
```
1. Detect .sync-conflict files
2. Attempt 3-way merge
3. If fails, log to conflicts.log
4. Alert human: "Manual merge needed"
5. Don't auto-resolve (too risky)
```

---

## Testing Strategy

### Unit Tests

- [ ] AGNOSTIC system: 0AGNOSTIC.md parses correctly
- [ ] Traversal: /find skill finds all test paths
- [ ] Sync: Lock acquisition/release works
- [ ] Episodic: Session files create correctly

### Integration Tests

- [ ] Single agent: AGNOSTIC → Traversal → Sync → Episodic
- [ ] Sequential agents: Agent A finishes, Agent B resumes
- [ ] Parallel agents: Multiple agents work simultaneously without conflicts
- [ ] Multi-session: Agent resumes work days later with full context

### Failure Tests

- [ ] Deadlock recovery: Agent crashes, lock cleaned up
- [ ] Data corruption: Write fails mid-operation, rollback works
- [ ] Conflict resolution: Two agents modify same file, conflict detected and logged
- [ ] Amnesia prevention: Agent reads previous session, understands context

---

## Performance Targets

| Operation | Target | Notes |
|-----------|--------|-------|
| Read 0AGNOSTIC.md | <100ms | Lean file, always fast |
| /find query | 3-5s | 3-5 levels, 1s per level |
| Acquire lock (no contention) | <100ms | Fast file I/O |
| Create session file | <500ms | Write + formatting |
| Read episodic index | <50ms | Markdown file |

**Scalability**:
- 5,930 nodes: /find works in 3-5 steps (not 5,930 steps)
- 100+ sessions: Episodic index still fast (<50ms)
- 1000+ changes: divergence.log still searchable

---

## Deployment Checklist

### Phase 1: Foundation (Week 1-2)
- [ ] Implement AGNOSTIC system (0AGNOSTIC.md + .0agnostic/)
- [ ] Run agnostic-sync.sh for each layer/stage
- [ ] Verify CLAUDE.md generation works
- [ ] Test with single agent

### Phase 2: Discovery (Week 2-3)
- [ ] Add 0INDEX.md at 20-30 branching points
- [ ] Implement /find skill
- [ ] Test /find with sample queries
- [ ] Verify keyword matching works

### Phase 3: Safety (Week 3-4)
- [ ] Implement file locking
- [ ] Implement atomic writes
- [ ] Create .locks/ directories
- [ ] Test lock acquisition/release

### Phase 4: Continuity (Week 4-5)
- [ ] Create episodic memory structure
- [ ] Implement session file creation
- [ ] Test session continuity
- [ ] Test multi-session scenario

### Phase 5: Integration (Week 5-6)
- [ ] Test all layers together
- [ ] Test multi-agent scenarios
- [ ] Test recovery procedures
- [ ] Performance optimization

### Phase 6: Production (Week 6+)
- [ ] Deploy to main system
- [ ] Monitor for issues
- [ ] Refine based on real usage
- [ ] Document best practices

