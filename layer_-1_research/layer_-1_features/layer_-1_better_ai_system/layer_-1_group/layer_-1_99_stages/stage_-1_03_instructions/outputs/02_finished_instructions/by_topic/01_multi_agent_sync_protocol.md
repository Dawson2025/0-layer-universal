# Multi-Agent Sync Protocol

**Date**: 2026-01-30
**Stage**: stage_-1_03_instructions
**Status**: FINISHED - Ready for Design
**Revision**: 1.0

---

## Overview

Your system implements TRUE parallel multi-agent execution where:
- CLI tools can instantiate other CLI tools
- Multiple agents run simultaneously in parallel
- Filesystem is the shared context and communication medium
- Each layer/stage can be an entry point for a new agent

This protocol defines how to safely manage conflicts, synchronize changes, and maintain consistency when multiple agents write to shared locations.

---

## Constraint 1: File Locking (Conflict Prevention)

### Purpose
Prevent concurrent writes to the same file when multiple agents operate in parallel.

### Protocol

**Before writing to shared locations:**

1. **Create lock file** with agent identity
   ```bash
   # Format: .locks/[scope]_[agent_id].lock
   # Example: .locks/layer_2_outputs_agent_research_01.lock

   echo "agent_id=research_01" > .locks/outputs_agent_research_01.lock
   ```

2. **Check existing locks**
   ```bash
   # Fail if lock exists and is not stale
   if [ -f .locks/outputs_agent_research_01.lock ]; then
     # Check age - fail if < 5 minutes old
     age=$(($(date +%s) - $(stat -f%m .locks/outputs_agent_research_01.lock)))
     if [ $age -lt 300 ]; then
       echo "ERROR: Lock exists and is fresh. Another agent is writing."
       exit 1
     fi
   fi
   ```

3. **Do work** - Write all changes while holding lock

4. **Release lock** - Remove lock file when done
   ```bash
   rm .locks/outputs_agent_research_01.lock
   ```

### Lock Locations

- **Per agent session**: Create lock before starting work
- **Per shared scope**: One lock per directory being modified
- **Scope examples**:
  - `.locks/hand_off_documents_layer2.lock`
  - `.locks/outputs_episodic_layer2.lock`
  - `.locks/outputs_synthesis_layer2.lock`

### Lock Expiration

- Default TTL: 5 minutes
- If lock older than TTL, consider agent crashed
- Clean up stale locks before writing

---

## Constraint 2: Atomic Writes (Consistency)

### Purpose
Ensure incomplete writes don't corrupt files when agent crashes mid-operation.

### Protocol

**For every file write:**

1. **Write to temporary file**
   ```bash
   # WRONG: echo "data" > file.md
   # RIGHT:
   echo "data" > file.md.tmp
   ```

2. **Atomic rename**
   ```bash
   # After verifying temp file is valid:
   mv file.md.tmp file.md  # Atomic on most filesystems
   ```

3. **Verify success**
   ```bash
   if [ -f file.md ]; then
     echo "Write successful"
   else
     echo "ERROR: Write failed"
     exit 1
   fi
   ```

### Handoff Atomicity

For critical handoff documents:

1. Write to `incoming/[timestamp]_draft_[agent_id].md`
2. Verify content is valid
3. Atomic rename to `incoming/[timestamp]_[agent_id].md` (final)
4. Other agents ignore `_draft_` files

### Temporary File Cleanup

- Clean up `.tmp` files older than 1 hour during agent startup
- Log cleanup to episodic memory

---

## Constraint 3: Change Detection (Divergence Awareness)

### Purpose
Efficiently track what changed across parallel agent work to maintain consistency.

### Protocol

**Using Git-based Merkle-DAG equivalent:**

```bash
# Before agent starts work:
hash_before=$(git hash-object -t tree layer_2/ 2>/dev/null || echo "initial")

# ... agent does work ...

# After agent finishes:
hash_after=$(git hash-object -t tree layer_2/ 2>/dev/null || echo "final")

if [ "$hash_before" != "$hash_after" ]; then
  # Something in layer_2 changed
  # Notify dependent agents
  echo "layer_2 modified" >> outputs/episodic/changes/divergence.log
fi
```

**For each layer/scope:**

1. Store hash before agent work begins
2. Compare hash after agent work completes
3. If changed, trigger propagation to dependent scopes
4. Record in episodic change log

### Change Tracking File

**Location**: `outputs/episodic/changes/divergence.log`

**Format**:
```
2026-01-30T14:23:45Z | agent_research_01 | layer_2_outputs | MODIFIED | hash_abc123→hash_def456
2026-01-30T14:25:12Z | agent_design_01 | hand_off_documents | MODIFIED | hash_xyz789→hash_uvw012
```

### Propagation Trigger

When agent detects change in dependency:

1. Read divergence.log
2. Check if any changed scopes are in dependencies
3. If yes, signal dependent agent: "layer_N changed, re-read context"

---

## Constraint 4: Conflict Resolution (CRDT-Style Merge)

### Purpose
When two agents modify the same file, resolve conflicts deterministically.

### Scenarios

**Scenario A: Both agents append to handoff document**

```markdown
# File: hand_off_documents/incoming/task.md

Agent A writes:
- Task: Feature X development
- Status: In progress

Agent B writes:
- Task: Feature X review
- Status: Pending

Result conflict: Two different task descriptions for same file
```

**Resolution Strategy**: Last-write-wins with timestamp

```bash
# Each agent includes timestamp in handoff:
---
timestamp: 2026-01-30T14:25:12Z
agent: research_01
---

# If conflict detected, keep version with LATEST timestamp
# (Last agent to write is authoritative)
```

**Scenario B: Both agents modify same output file**

```bash
# outputs/synthesis/recommendations.md modified by both agents
# Git can detect this as a merge conflict
```

**Resolution Strategy**: Use 3-way merge with common base

```bash
# If conflict in git:
git merge-base agent_research_01/branch agent_design_01/branch
# Then manual merge based on agent responsibilities
# - Research agent handles: data/findings sections
# - Design agent handles: architecture/decision sections
```

### Conflict Log

**Location**: `outputs/episodic/changes/conflicts.log`

**Format**:
```
2026-01-30T14:30:00Z | CONFLICT | hand_off_documents/task.md | agent_research_01 vs agent_design_01 | RESOLVED | last-write-wins | research_01_timestamp=14:25:12, design_01_timestamp=14:27:45 | winner=design_01
```

**Process**:
1. Detect conflict (file modified by multiple agents simultaneously)
2. Log conflict with timestamps
3. Apply resolution rule (deterministic)
4. Document resolution in conflict log
5. Notify affected agents

---

## Implementation Phases

### Phase 1: Conflict Prevention (CRITICAL - NOW)

Implement immediately:

- [ ] File locking mechanism (`.locks/` directory, lock/unlock protocol)
- [ ] Atomic write pattern (`.tmp` files, atomic rename)
- [ ] Setup `.locks/` directories at each shared scope
- [ ] Document locking protocol in each agent's CLAUDE.md

**Benefit**: Prevents 80% of conflicts through prevention, not resolution

### Phase 2: Change Tracking (IMPORTANT - NEXT)

Implement after Phase 1 stabilizes:

- [ ] Git-based hash tracking before/after agent work
- [ ] Divergence log creation and maintenance
- [ ] Propagation triggers for dependent agents
- [ ] Change tracking in episodic memory

**Benefit**: Enables efficient detection of what changed, avoids scanning all files

### Phase 3: Conflict Resolution (AS-NEEDED)

Implement when conflicts actually occur:

- [ ] Conflict detection automation
- [ ] CRDT merge rule implementation
- [ ] Conflict logging
- [ ] Automated resolution or notification

**Benefit**: Graceful recovery when prevention fails

### Phase 4: Performance Optimization (FUTURE)

Implement if needed for speed:

- [ ] Bloom filters for "what files changed?" queries
- [ ] Selective sync (only changed portions)
- [ ] Parallel initialization optimization

---

## CLAUDE.md Instructions

Each agent CLAUDE.md should include:

```markdown
## Multi-Agent Sync Protocol

### Before Writing
1. Acquire lock: Create `.locks/[scope]_[agent_id].lock`
2. Verify no conflicting locks exist
3. Read divergence.log for changes in dependencies
4. Proceed with work

### During Writing
1. Use atomic writes: Write to `.tmp`, then atomic rename
2. Log all changes to episodic memory

### After Writing
1. Release lock: Remove `.locks/[scope]_[agent_id].lock`
2. Record hash changes to divergence.log
3. Trigger propagation to dependent agents
4. Update episodic memory with completion timestamp
```

---

## Error Handling

### Lock Acquisition Failure

```
ERROR: Cannot acquire lock (another agent writing)
REMEDIATION:
  1. Wait 5 seconds and retry
  2. If still locked after 3 retries, check lock age
  3. If lock is stale (>10 min), remove it and retry
  4. If still failing, escalate to Stages Manager
```

### Write Failure

```
ERROR: Atomic rename failed (permissions, disk full, etc.)
REMEDIATION:
  1. Clean up .tmp file
  2. Release lock
  3. Log error to episodic memory
  4. Escalate to Stages Manager
```

### Conflict Detection

```
DETECTED: File modified by multiple agents
REMEDIATION:
  1. Log conflict with timestamps
  2. Apply last-write-wins resolution
  3. Verify both versions are correct
  4. Continue execution
  5. Note: If critical data lost, merge manually
```

---

## Testing the Protocol

### Test 1: Single Agent Lock

- [ ] Agent acquires lock
- [ ] Agent writes file
- [ ] Agent releases lock
- [ ] No deadlock

### Test 2: Sequential Agents

- [ ] Agent A acquires lock
- [ ] Agent B waits (lock exists)
- [ ] Agent A releases lock
- [ ] Agent B acquires lock immediately

### Test 3: Stale Lock Cleanup

- [ ] Create stale lock (>5 min old)
- [ ] Agent detects staleness
- [ ] Agent removes stale lock
- [ ] Agent acquires lock

### Test 4: Atomic Write Failure

- [ ] Simulate write failure (disk full simulation)
- [ ] Verify `.tmp` file exists
- [ ] Verify original file unchanged
- [ ] Verify cleanup works

### Test 5: Conflict Resolution

- [ ] Two agents modify same file simultaneously
- [ ] Conflict detected
- [ ] Last-write-wins resolution applied
- [ ] Both agents can read resolved file

---

## Success Criteria

✅ **Protocol is working when:**

1. Multiple agents can run in parallel without deadlock
2. File integrity maintained even if agent crashes
3. No silent data loss from concurrent writes
4. Conflicts detected and logged systematically
5. Conflict resolution is deterministic and repeatable

❌ **Protocol needs review if:**

1. Deadlock occurs (agent waits indefinitely for lock)
2. File corruption detected (incomplete writes)
3. Silent conflicts (files modified without detection)
4. Inconsistent resolution (same conflict resolved differently)

