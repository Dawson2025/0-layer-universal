# System Integration Guide

**Date**: 2026-01-30
**Stage**: stage_-1_03_instructions
**Status**: FINISHED - Ready for Design
**Revision**: 1.0

---

## Overview

This document ties together the four constraints from previous instructions:

1. **Multi-Agent Sync Protocol** - Safe parallel execution
2. **Automated Traversal** - Discovery at scale
3. **AGNOSTIC System** - Tool-portable context
4. **Episodic Memory** - Session continuity

Shows how they work together to solve "agent amnesia."

---

## The Problem Statement (From Research)

Your system has:

- ✅ Multi-agent parallel execution capability
- ✅ 5,930+ nodes organized hierarchically
- ✅ Filesystem as shared context medium
- ✅ Three-layer memory architecture concept

But missing:

- ❌ Safe conflict prevention (multiple agents writing simultaneously)
- ❌ Automatic context discovery (what's relevant at 5,930 nodes?)
- ❌ Tool portability (locked into one AI tool)
- ❌ Session continuity (what happened in previous sessions?)

**These four constraints solve all four gaps.**

---

## How They Integrate

### Scenario: Multi-Session Research Project

**Session 1 (Day 1) - Research Agent**

```
START: Agent enters stage_-1_02_research

Step 1: EPISODIC MEMORY
  → Read: outputs/episodic/index.md (first time, empty)
  → No previous work, starting fresh

Step 2: AGNOSTIC CONTEXT
  → Read: 0AGNOSTIC.md (200 tokens)
  → Understands: role=research, scope=02_research, parent=stages_manager

Step 3: AUTOMATED TRAVERSAL
  → Query: "What needs research?"
  → Use /find skill to navigate Tree of Needs
  → Discovers 15 requirements to explore

Step 4: MULTI-AGENT SYNC
  → Acquire lock: .locks/outputs_research_01.lock
  → Start research work

Step 5: OUTPUT-FIRST
  → Write findings to: outputs/01_understanding_in_progress/by_topic/
  → Update: outputs/episodic/changes/divergence.log
  → Create: outputs/episodic/sessions/2026-01-30_session_001.md

RESULT: Comprehensive research documented with session record
```

**Session 2 (Day 3) - Design Agent Enters**

```
START: Agent enters stage_-1_04_design

Step 1: EPISODIC MEMORY
  → Read: outputs/episodic/index.md
  → "Research completed on 2026-01-30, covered 15 needs, recommended 5 priorities"

Step 2: AGNOSTIC CONTEXT
  → Read: 0AGNOSTIC.md (different stage, different role)
  → Understands: role=design, scope=04_design, parent=stages_manager
  → Load: .0agnostic/rules/design_decision_protocol.md (on-demand)

Step 3: AUTOMATED TRAVERSAL
  → Query: "Show me finished research"
  → /find navigates to: stage_-1_02_research/outputs/02_finished_instructions/

Step 4: DEPENDENCY AWARENESS
  → Read: outputs/episodic/changes/divergence.log
  → "Research outputs modified 2026-01-30, design depends on these"
  → Get hash of research outputs from divergence.log

Step 5: MULTI-AGENT SYNC
  → Before writing design docs
  → Acquire lock: .locks/outputs_design_01.lock
  → Check divergence.log: did research change since I started?

RESULT: Design work builds on research findings, no conflicts
```

**Session 3 (Day 5) - Parallel Agents (Research + Design)**

```
SCENARIO: Research agent continues, Design agent starts simultaneously

Agent A (Research):
  → Lock acquired: .locks/outputs_research_01.lock
  → Writing new findings
  → Updates divergence.log with hash_abc123→hash_def456

Agent B (Design):
  → Waits for lock: .locks/outputs_research_01.lock
  → Retries every 2 seconds
  → Lock released after 5 minutes

Agent B Resumes:
  → Lock acquired: .locks/outputs_design_01.lock
  → Reads divergence.log: research changed!
  → Hash changed from hash_abc123→hash_def456
  → Re-reads research outputs to incorporate new findings
  → Continues with updated context

RESULT: Safe parallel execution, changes propagated automatically
```

---

## Reference Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Agent Session                        │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  1. EPISODIC MEMORY (Session Start)                          │
│     └─ outputs/episodic/index.md                             │
│        outputs/episodic/sessions/[latest].md                 │
│                                                               │
│  2. AGNOSTIC CONTEXT (Setup)                                 │
│     ├─ Read: 0AGNOSTIC.md (200 tokens) ← Always loaded       │
│     ├─ Load: .0agnostic/rules/* (on-demand)                  │
│     └─ Generate: CLAUDE.md via agnostic-sync.sh              │
│                                                               │
│  3. AUTOMATED TRAVERSAL (Discovery)                          │
│     ├─ Query: "What's relevant?"                             │
│     └─ Use /find skill → reads 0INDEX.md at each level       │
│                                                               │
│  4. MULTI-AGENT SYNC (Safety)                                │
│     ├─ Acquire lock: .locks/[scope]_[agent].lock             │
│     ├─ Read divergence.log: what changed since last access?  │
│     ├─ Do work (atomic writes with .tmp files)               │
│     └─ Release lock + update divergence.log                  │
│                                                               │
│  5. OUTPUT-FIRST (Persistence)                               │
│     ├─ Write all outputs to outputs/ first                   │
│     ├─ Update episodic/changes/[type].log                    │
│     └─ Create outputs/episodic/sessions/[session].md         │
│                                                               │
│  6. HANDOFF (Communication)                                  │
│     └─ Write to hand_off_documents/outgoing/                 │
│                                                               │
│  7. COMMIT & PUSH (Sync)                                     │
│     ├─ Commit: git add [outputs, episodic, 0AGNOSTIC]        │
│     └─ Don't commit: CLAUDE.md, .tmp files, .locks/          │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Implementation Timeline

### Phase 1: Foundation (Immediate)

**Goal**: Enable multi-agent sync safely

**Tasks**:

1. **Multi-Agent Sync Protocol**
   - [ ] Create .locks/ directories at shared scopes
   - [ ] Implement lock/unlock in agent CLAUDE.md
   - [ ] Test single-agent locking behavior
   - [ ] Test stale lock cleanup
   - [ ] Create lock/unlock helper scripts

2. **Episodic Memory**
   - [ ] Create outputs/episodic/ structure
   - [ ] Create session file template
   - [ ] Update CLAUDE.md with episodic logging
   - [ ] Train first agents on session logging

**Duration**: 1 week
**Benefit**: Safe parallel execution without deadlock

### Phase 2: Discovery (Next)

**Goal**: Enable context discovery at scale

**Tasks**:

1. **Automated Traversal**
   - [ ] Identify 20-30 key branching points
   - [ ] Create 0INDEX.md for each
   - [ ] Test manual /find workflow
   - [ ] Implement /find skill
   - [ ] Validate with 20 test queries

2. **AGNOSTIC System**
   - [ ] Create 0AGNOSTIC.md templates
   - [ ] Implement agnostic-sync.sh
   - [ ] Create first .0agnostic/ structures
   - [ ] Test CLAUDE.md generation

**Duration**: 2 weeks
**Benefit**: Discover context without manual navigation

### Phase 3: Convergence (Month 2)

**Goal**: Full system operational

**Tasks**:

1. **Test Multi-Agent Scenario**
   - [ ] Run two agents in parallel
   - [ ] Verify lock prevents conflicts
   - [ ] Verify change tracking works
   - [ ] Verify conflict resolution handles edge cases

2. **Test Session Continuity**
   - [ ] Run agent in session 1
   - [ ] Run different agent in session 2
   - [ ] Verify agent 2 understands session 1's work
   - [ ] Verify episodic memory enables context recovery

3. **Optimize Performance**
   - [ ] Profile lock contention
   - [ ] Optimize divergence.log scanning
   - [ ] Consider Bloom filter optimization (if needed)

**Duration**: Ongoing
**Benefit**: Full system operational end-to-end

---

## Success Metrics

### Metric 1: Multi-Agent Sync

**Measure**: Lock effectiveness

- [ ] No deadlock (lock released within 5 minutes)
- [ ] No silent conflicts (conflicts detected 100% of time)
- [ ] No data loss (atomic writes maintained)
- [ ] File integrity (no corrupted files after agent crashes)

**Target**: All metrics pass

### Metric 2: Context Discovery

**Measure**: Traversal efficiency

- [ ] Agent finds any context in ≤5 steps
- [ ] Agent understands its role from 0AGNOSTIC.md alone
- [ ] /find skill succeeds for 95%+ of queries
- [ ] No agent needs manual navigation help

**Target**: 95% success rate

### Metric 3: Session Continuity

**Measure**: Memory retention

- [ ] Every session creates a record
- [ ] Agent can resume work from previous session notes
- [ ] Episodic memory searchable and up-to-date
- [ ] No information loss between sessions

**Target**: 100% session coverage

### Metric 4: System Integration

**Measure**: End-to-end behavior

- [ ] Multiple agents run in parallel without blocking
- [ ] Changes in one layer propagate to dependent layers
- [ ] Same source (0AGNOSTIC.md) works across tools
- [ ] New agent onboards in <5 minutes

**Target**: All working smoothly

---

## Troubleshooting Guide

### Problem: Agents Deadlock (Waiting for Lock Forever)

**Symptoms**:
- Agent waits >5 minutes for lock
- Multiple agents block each other
- System appears frozen

**Root Causes**:
1. Lock file not released (agent crashed)
2. Lock TTL too long
3. Multiple agents trying to acquire same lock unnecessarily

**Solution**:
1. Check `.locks/` for stale files: `find .locks -mmin +5`
2. Remove stale locks: `rm .locks/*`
3. Restart agents
4. If persistent, review lock acquisition logic

### Problem: Silent Conflicts (Files Modified Without Detection)

**Symptoms**:
- Two agents modify same file
- divergence.log shows no conflict
- File content seems merged incorrectly

**Root Causes**:
1. divergence.log not updated
2. Multiple agents not using hash tracking
3. Lock not preventing simultaneous writes

**Solution**:
1. Verify lock protocol in use: `cat hand_off_documents/outgoing/*/status.md`
2. Manually check divergence.log: `tail -20 outputs/episodic/changes/divergence.log`
3. If lock not used, enforce lock acquisition before all writes

### Problem: Traversal Fails (Can't Find Relevant Context)

**Symptoms**:
- Agent searches for context but can't find it
- Query "Where is X?" returns no result
- Manual navigation works, /find doesn't

**Root Causes**:
1. 0INDEX.md missing at decision point
2. Keywords in 0INDEX.md don't match query
3. /find skill doesn't navigate deeply enough

**Solution**:
1. Add missing 0INDEX.md files at branching points
2. Review keywords: do they match what agents search for?
3. Test /find with sample queries, improve if needed

### Problem: Episodic Memory Corruption (Session Files Missing/Unreadable)

**Symptoms**:
- Session files disappear
- outputs/episodic/ becomes corrupted
- Can't read previous session records

**Root Causes**:
1. Atomic write failed mid-session
2. Filesystem sync issue
3. Git conflict in episodic files

**Solution**:
1. Check git status: `git status outputs/episodic/`
2. If conflicts, resolve via `git merge`
3. If missing files, restore from git: `git checkout outputs/episodic/`
4. Verify atomic write protocol is followed

---

## Migration Checklist

For existing systems adopting these constraints:

- [ ] Understand all four constraints (read all five instruction documents)
- [ ] Start Phase 1: Multi-agent sync + episodic memory
- [ ] Test with single agent first (verify no deadlock)
- [ ] Test with two agents in sequence (verify lock works)
- [ ] Move to Phase 2: Automated traversal + AGNOSTIC system
- [ ] Create 0INDEX.md at key branching points
- [ ] Create 0AGNOSTIC.md for each layer/stage
- [ ] Test /find skill with sample queries
- [ ] Run Phase 3: Full system operational tests
- [ ] Document any customizations or extensions

---

## Design Stage Inputs

The Design stage will use these instructions to create:

1. **Sync Protocol Implementation Design**
   - Lock manager component
   - Divergence detector component
   - Conflict resolver component

2. **Traversal System Design**
   - /find skill architecture
   - 0INDEX.md structure specification
   - Search algorithm design

3. **AGNOSTIC System Design**
   - agnostic-sync.sh detailed implementation
   - CLAUDE.md → AGENTS.md → GEMINI.md transformation rules
   - Resource loading mechanism

4. **Memory System Design**
   - Episodic storage architecture
   - Session file format specification
   - Compaction algorithm design

5. **Integration Architecture**
   - Data flow between components
   - Error handling and recovery
   - Performance optimization opportunities

---

## Key Principles for Implementation

1. **Fail Safe, Not Fail Open**
   - When in doubt about conflicts, deny and escalate
   - Don't try to automatically resolve complex conflicts
   - Log everything for human review

2. **Simple Over Clever**
   - File locking is simpler than CRDT
   - Markdown indices better than vector databases
   - .tmp files simpler than transaction logs

3. **Tool Agnostic Always**
   - No hard dependency on Claude, AutoGen, Gemini
   - Every component should work with multiple tools
   - Test regularly with different tools

4. **Session Continuity First**
   - Every agent action should create a record
   - Next session should understand what happened
   - Episodic memory is the source of truth for history

5. **Scale Aware**
   - Test at 100, 1000, 5930 nodes
   - Identify bottlenecks early
   - Optimize only when necessary

