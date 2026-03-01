# Planning Stage (05) - Entry Point

**Date**: 2026-01-30
**Stage**: stage_-1_05_planning
**Input**: Design stage outputs (6 design documents, 5 instruction documents)
**Output**: Detailed implementation plan with tasks, phases, and dependencies
**Status**: Ready to begin planning

---

## What Planning Stage Does

Converts detailed designs into actionable implementation plans:

```
Design Stage Outputs              Planning Stage                  Development Stage (06)
─────────────────────────────────────────────────────────────────────────────────
6 Design Documents        →    Task Decomposition      →    30-40 Implementation Tasks
5 Instruction Documents   →    Phase Planning          →    4-week Phase 1 Schedule
4-layer Architecture      →    Dependency Mapping      →    Critical Path + Gantt Chart
10 SHIMI Concepts         →    Resource Allocation     →    Team structure
100% Traceability         →    Risk Management         →    Success Criteria
```

---

## Input: Design Stage Deliverables

### Design Documents (Use These for Task Breakdown)

Location: `../stage_-1_04_design/outputs/03_design_decisions/by_topic/`

| # | Document | Components | Tasks Expected |
|---|----------|-----------|---|
| 1 | 01_multi_agent_sync_design.md | Lock Manager, Change Detector, Resolver, Logger | 8-10 tasks |
| 2 | 02_automated_traversal_design.md | Preprocessor, Reader, Selector, Controller, Validator | 10-12 tasks |
| 3 | 03_agnostic_system_design.md | 0AGNOSTIC.md, .0agnostic/, sync script | 5-6 tasks |
| 4 | 04_episodic_memory_architecture.md | Session files, logs, index, compaction | 6-8 tasks |
| 5 | 05_system_integration_architecture.md | Layer integration, workflows, deployment | 3-4 tasks |
| 6 | 06_shimi_concepts_to_implementation_mapping.md | Verification of all SHIMI concepts | 1-2 tasks |

**Total Expected**: 33-42 implementation tasks

### Instruction Documents (Use These for Implementation Constraints)

Location: `../stage_-1_03_instructions/outputs/02_finished_instructions/by_topic/`

Each instruction document specifies:
- Implementation constraints (what must be true)
- Success criteria (how to verify)
- Integration points (how it connects)
- Protocol (exact behavior)

---

## Planning Stage Workflow

### Phase 1: Understand Design Details (1 day)

**For each design document:**

1. Read design document completely
2. Identify components (major pieces)
3. List algorithms and data structures
4. Note integration points with other systems
5. Mark error handling and edge cases

**Deliverable**: Mental model of complete system

### Phase 2: Decompose into Tasks (2-3 days)

**For each component:**

1. Create one task per implementable piece
2. Task should be "completable in 2-3 days"
3. Task should have clear input/output
4. Task should have success criteria

**Example Decomposition** (Multi-Agent Sync):

```
Design Component: Lock Manager
├─ Task 1: Implement lock acquisition
├─ Task 2: Implement lock release
├─ Task 3: Implement lock timeout/cleanup
├─ Task 4: Implement lock status queries
└─ Task 5: Create unit tests for lock manager

Design Component: Change Detector
├─ Task 6: Implement hash calculation (git hash-object)
├─ Task 7: Implement divergence tracking
├─ Task 8: Implement change notification system
└─ Task 9: Create unit tests for change detector
```

**Deliverable**: 30-40 detailed task specifications

### Phase 3: Map Dependencies (1-2 days)

**For each task:**

1. Identify tasks it depends on (blockedBy)
2. Identify tasks that depend on it (blocks)
3. Highlight critical path (longest dependency chain)

**Example Dependencies**:

```
Task 1: Lock Manager Acquisition
  ↓ (blocks)
Task 6: Hash Calculation
  ↓ (blocks)
Task 7: Divergence Tracking
  ↓ (blocks)
Task 10: /find skill (needs change notification)

Critical Path: 1 → 6 → 7 → 10
               (foundation before higher-level features)
```

**Deliverable**: Dependency graph with critical path

### Phase 4: Plan Phases & Timeline (1 day)

**Phase 1 (4 weeks): Core Systems**
- All 8 SHIMI core concepts
- 20-25 tasks
- 2-3 developers

**Phase 2 (2 weeks): Optimization**
- Bloom filters
- Performance tuning
- 5-8 tasks

**Phase 3 (2 weeks): Advanced**
- Full CRDT
- Vector clocks
- 3-5 tasks

**Deliverable**: Phase schedule with task assignment

### Phase 5: Resource & Risk Planning (1 day)

**Resource Planning:**
- Assign developers to components
- Balance workload
- Plan ramp-up time

**Risk Management:**
- Identify blockers
- Plan mitigation
- Define fallback strategies

**Deliverable**: Resource allocation matrix, risk register

---

## Planning Stage Outputs

### Deliverable 1: Task Breakdown Document

**Create**: `outputs/04_task_specifications/detailed_tasks.md`

```markdown
# Implementation Tasks

## Phase 1: Core Systems

### Component: Multi-Agent Sync

#### Task 1.1: Implement Lock Manager
- **Input**: None (foundation)
- **Output**: Lock module with functions:
  - acquire_lock(scope, agent_id) → bool
  - release_lock(scope, agent_id) → bool
  - check_lock(scope) → {agent_id, timestamp, ttl}
- **Tests**: Unit tests for acquire/release/timeout
- **Depends**: Nothing (foundation)
- **Blocks**: Task 1.6 (Change Detector)
- **Effort**: 2-3 days
- **Success Criteria**:
  - [ ] Lock file created in .locks/
  - [ ] 5-minute TTL enforced
  - [ ] Multiple acquisitions blocked
  - [ ] Stale locks cleaned up

#### Task 1.2: Implement Lock Release
- ...

[Continue for each task]
```

### Deliverable 2: Dependency & Phase Plan

**Create**: `outputs/04_planning_artifacts/phase_schedule.md`

```markdown
# Phase Schedule & Dependencies

## Critical Path (Phase 1)

1. Lock Manager (days 1-3)
2. Atomic Write Implementation (days 3-5)
3. Hash Calculation (days 5-7)
4. Change Detection (days 7-10)
5. /find Skill Basic (days 10-14)

Total Phase 1: ~20 days (4 weeks with parallel work)

## Phase Dependencies

Phase 1 (core systems) → Phase 2 (optimization)
Phase 2 (optimization) → Phase 3 (advanced)

Phase 1 can be parallelized:
- Sync tasks (1-5 parallel with traversal tasks)
- AGNOSTIC system can start anytime
- Episodic memory can start after sync foundation
```

### Deliverable 3: Team Structure & Assignment

**Create**: `outputs/04_planning_artifacts/team_structure.md`

```markdown
# Team Structure

## Phase 1 Team (2-3 developers)

- **Developer A**: Multi-Agent Sync (Lock, Atomic, Detection, Resolution)
  - Effort: 80% Phase 1
  - Tasks: 1.1-1.5
  - Duration: 4 weeks

- **Developer B**: Traversal System (0INDEX.md, /find skill, LLM selector)
  - Effort: 80% Phase 1
  - Tasks: 2.1-2.7
  - Duration: 4 weeks

- **Developer C**: AGNOSTIC + Episodic (can start concurrently)
  - Effort: 40% Phase 1 (lighter tasks)
  - Tasks: 3.1-3.4, 4.1-4.5
  - Duration: 2-3 weeks

## Ramp-Up Schedule

Week 1: Dev A + B start foundation tasks
Week 2: Dev C joins after foundation tasks clear
Week 3: All three working, some tasks in parallel
Week 4: Final integration and testing
```

### Deliverable 4: Success Criteria & Metrics

**Create**: `outputs/04_planning_artifacts/success_criteria.md`

```markdown
# Success Criteria

## Phase 1 Completion Criteria

✅ Multi-Agent Sync
- [ ] Lock manager prevents concurrent writes
- [ ] Change detection identifies all modifications
- [ ] Conflict resolution is deterministic
- [ ] No data loss in multi-agent scenario
- [ ] Unit tests pass (100% coverage)
- [ ] Integration tests pass (multi-agent coordination)

✅ Traversal System
- [ ] /find query completes in 3-5 seconds
- [ ] Finds target in 5,930 node hierarchy
- [ ] LLM selection works with keyword fallback
- [ ] All error cases handled
- [ ] Unit tests pass

✅ AGNOSTIC System
- [ ] 0AGNOSTIC.md loads <100ms
- [ ] .0agnostic/ resources available on-demand
- [ ] agnostic-sync.sh generates CLAUDE.md correctly
- [ ] Works with Claude, AutoGen, Gemini formats

✅ Episodic Memory
- [ ] Session files created automatically
- [ ] Divergence.log tracks all changes
- [ ] Agent can resume from previous session
- [ ] Compaction archives old sessions
- [ ] Index.md searchable

## Metrics

- Code coverage: >80%
- Test pass rate: 100%
- Performance: Within targets (see design)
- Integration: All 4 layers working together
```

---

## Using Design Documents for Planning

### 01_multi_agent_sync_design.md

```
Use for:
├─ Component list (Lock, Detector, Resolver, Logger)
├─ Algorithm specifications (algorithms 1.1-1.4)
├─ Data formats (.locks/*, divergence.log, conflicts.log)
├─ Error handling (8+ error cases per component)
└─ Testing strategy (unit + integration tests)

Create tasks from:
├─ Each component → 1-2 implementation tasks
├─ Each algorithm → 1 task
├─ Each format → 1 task
└─ Each error case → test tasks
```

### 02_automated_traversal_design.md

```
Use for:
├─ Component list (5 components)
├─ 0INDEX.md format specification
├─ LLM prompt design
├─ Recursive traversal algorithm
├─ Error handling and fallbacks
└─ Performance targets (3-5 second traversal)

Create tasks from:
├─ 0INDEX.md implementation
├─ /find command implementation
├─ LLM selector implementation
├─ Recursive traversal controller
├─ Fallback keyword matching
└─ Performance optimization
```

### 03_agnostic_system_design.md

```
Use for:
├─ 0AGNOSTIC.md structure (310/400 token budget)
├─ .0agnostic/ folder organization
├─ agnostic-sync.sh algorithm
├─ Tool-specific format rules (CLAUDE.md, AGENTS.md, GEMINI.md)
└─ File preservation and git integration

Create tasks from:
├─ Create 0AGNOSTIC.md template
├─ Organize .0agnostic/ structure
├─ Implement agnostic-sync.sh
├─ Generate CLAUDE.md from 0AGNOSTIC.md
└─ Test tool-specific formats
```

### 04_episodic_memory_architecture.md

```
Use for:
├─ Session file structure
├─ Divergence.log format
├─ Conflicts.log format
├─ Index.md structure
├─ Compaction algorithm
└─ Session retrieval queries

Create tasks from:
├─ Session file creation system
├─ Divergence tracking system
├─ Conflict detection and logging
├─ Index generation and updates
└─ Compaction scheduler
```

### 05_system_integration_architecture.md

```
Use for:
├─ 4-layer architecture overview
├─ Integration points between layers
├─ Multi-session workflow examples
├─ Error recovery procedures
├─ Performance targets
└─ Deployment checklist

Create tasks from:
├─ System integration tests (layer connections)
├─ Multi-session scenario tests
├─ Error recovery tests
├─ Performance benchmarking
└─ Deployment procedures
```

### 06_shimi_concepts_to_implementation_mapping.md

```
Use for:
├─ Verification of SHIMI concept coverage
├─ Phase assignments (Phase 1, 2, 3)
├─ Implementation approaches
├─ Success criteria per concept

Create tasks from:
├─ Verification that each concept implemented
├─ Testing for each SHIMI mechanism
├─ Phase 2-3 deferred features
└─ Traceability verification tests
```

---

## Template for Task Specifications

Create a task specification for each implementation task:

```markdown
# Task [Number]: [Title]

## Overview
[1-2 sentence description]

## Input/Output
- **Input**: What does this task receive?
- **Output**: What should this task produce?

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Dependencies
- **Blocked By**: Which tasks must complete first?
- **Blocks**: Which tasks depend on this?

## Effort Estimate
- **Complexity**: Low / Medium / High
- **Days**: X-Y days
- **Deliverables**: Code, tests, documentation

## Design Reference
- Reference design document: `XX_...design.md`
- Relevant sections: Section X, Algorithm Y

## Implementation Notes
- Key algorithms to implement
- Data structures to create
- Integration points
- Error handling requirements

## Testing
- Unit tests: List test cases
- Integration tests: How to test with other components

## Success Metrics
- Code passes linter
- Unit tests pass (100% coverage)
- Integration tests pass
- Meets performance targets (if applicable)
```

---

## Next Steps

### Immediate (Today-Tomorrow)

1. **Understand all 6 design documents**
   - Read each one thoroughly
   - Build mental model of system
   - Identify components and integration points

2. **Start task decomposition**
   - Break each design into 5-7 implementation tasks
   - Create task specification for each
   - Target: 30-40 detailed task specs

### This Week

3. **Map dependencies**
   - List task dependencies
   - Identify critical path
   - Find parallelizable work

4. **Plan phases & timeline**
   - Assign tasks to Phase 1/2/3
   - Create 4-week Phase 1 schedule
   - Estimate Phase 2-3 durations

5. **Resource & risk planning**
   - Assign developers to components
   - Identify potential blockers
   - Plan mitigation strategies

### Deliverables for This Week

- [ ] 30-40 detailed task specifications
- [ ] Dependency graph with critical path
- [ ] Phase schedule (4 weeks Phase 1)
- [ ] Team structure and assignments
- [ ] Risk register and mitigation plan

---

## Resources

### Design Documents
`../stage_-1_04_design/outputs/03_design_decisions/by_topic/`

### Instruction Documents
`../stage_-1_03_instructions/outputs/02_finished_instructions/by_topic/`

### Handoff Document
`../stage_-1_04_design/hand_off_documents/outgoing/to_above/design_stage_complete_handoff.md`

### Status Reports
`../../DESIGN_STAGE_COMPLETE_STATUS.md` (overview)

---

## Questions to Clarify

As you read the designs, ask:

1. **Sequencing**: Which system should be built first?
   - Recommendation: AGNOSTIC → Episodic → Sync → Traversal (enables each other)

2. **MVP Definition**: What's minimum viable product for Phase 1?
   - Recommendation: All 8 SHIMI core concepts, even if simple

3. **Testing Strategy**: Unit first or integration first?
   - Recommendation: Unit tests → integration tests → system tests

4. **Staffing**: 2 developers or 3?
   - Recommendation: 3 developers for 4-week timeline (A + B full-time, C part-time)

5. **Risk Mitigation**: Top blockers?
   - Recommendation: LLM selection accuracy, file locking robustness

---

## Success Indicator

Planning stage is complete when:

✅ Each design document has 5-7 clear implementation tasks
✅ Each task has dependencies specified
✅ Critical path identified
✅ Phase 1 (4 weeks) fully scheduled
✅ Phase 2-3 estimated and planned
✅ Risk register created
✅ Team structure defined
✅ All success criteria specified

**Estimated duration**: 1 week of planning work

---

## Ready to Begin?

1. Start by reading all 6 design documents
2. Identify components in each
3. Create task specifications
4. Map dependencies
5. Build schedule

Good luck! The design stage has given you everything you need. Now it's time to turn designs into a detailed implementation plan.

