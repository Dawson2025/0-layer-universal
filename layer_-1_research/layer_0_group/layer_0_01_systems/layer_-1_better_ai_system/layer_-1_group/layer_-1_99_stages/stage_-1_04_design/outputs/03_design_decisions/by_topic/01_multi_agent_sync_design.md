# Multi-Agent Sync Design

**Date**: 2026-01-30
**Stage**: stage_-1_04_design
**Status**: FINISHED - Ready for Planning
**Revision**: 1.0

---

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────┐
│                    Multi-Agent Sync System                        │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐ │
│  │  Agent A         │  │  Agent B         │  │  Agent C        │ │
│  │  (Research 01)   │  │  (Design 01)     │  │  (Review 01)    │ │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬────────┘ │
│           │                     │                     │           │
│           └─────────────────────┼─────────────────────┘           │
│                                 ▼                                 │
│              ┌──────────────────────────────────┐                │
│              │   Lock Manager (Component 1)     │                │
│              │  - Acquire lock                 │                │
│              │  - Release lock                 │                │
│              │  - Detect stale locks           │                │
│              │  - Clean up old locks           │                │
│              └──────────────────────────────────┘                │
│                         ▼                                        │
│              ┌──────────────────────────────────┐                │
│              │   Filesystem (Shared)           │                │
│              │  - .locks/ directory            │                │
│              │  - outputs/ directory           │                │
│              │  - hand_off_documents/          │                │
│              └──────────────────────────────────┘                │
│                         ▼                                        │
│              ┌──────────────────────────────────┐                │
│              │   Change Detector (Component 2)  │                │
│              │  - Compute hashes               │                │
│              │  - Detect divergence            │                │
│              │  - Update divergence.log        │                │
│              └──────────────────────────────────┘                │
│                         ▼                                        │
│              ┌──────────────────────────────────┐                │
│              │   Conflict Resolver (Component 3)│                │
│              │  - Detect conflicts             │                │
│              │  - Apply merge rules            │                │
│              │  - Log resolutions              │                │
│              └──────────────────────────────────┘                │
│                         ▼                                        │
│              ┌──────────────────────────────────┐                │
│              │   Episodic Logger (Component 4)  │                │
│              │  - Log changes                  │                │
│              │  - Record conflicts             │                │
│              │  - Update session file          │                │
│              └──────────────────────────────────┘                │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

---

## Component 1: Lock Manager

### Purpose
Prevent concurrent writes to shared files when multiple agents work in parallel.

### Design

**Lock File Location**: `.locks/[scope]_[agent_id].lock`

**Lock File Content**:
```json
{
  "agent_id": "research_01",
  "scope": "outputs",
  "acquired_at": "2026-01-30T14:23:45Z",
  "expires_at": "2026-01-30T14:28:45Z",
  "pid": 12345
}
```

### Behavior

**Acquire Lock**:

```
Function: acquire_lock(scope, agent_id, timeout_sec=5):
  max_retries = 10
  for retry in range(max_retries):
    lock_file = ".locks/" + scope + "_" + agent_id + ".lock"

    if file_exists(lock_file):
      age_seconds = now() - file_mtime(lock_file)
      if age_seconds < 300:  # 5 minutes
        wait(0.5 seconds)
        continue retry
      else:
        # Stale lock, remove it
        delete(lock_file)

    # Try to create lock file
    write_atomic(lock_file, json.dumps({
      "agent_id": agent_id,
      "scope": scope,
      "acquired_at": iso8601_now(),
      "expires_at": iso8601_future(5 * 60),  # 5 min TTL
      "pid": getpid()
    }))

    if file_exists(lock_file):
      return SUCCESS

  return FAILED_TIMEOUT
```

**Release Lock**:

```
Function: release_lock(scope, agent_id):
  lock_file = ".locks/" + scope + "_" + agent_id + ".lock"

  if file_exists(lock_file):
    # Verify our lock (safety check)
    content = read_json(lock_file)
    if content["agent_id"] != agent_id:
      log_error("Attempted to release someone else's lock!")
      return FAILED

    delete(lock_file)
    return SUCCESS

  log_warning("Lock file doesn't exist (may have been cleaned up)")
  return SUCCESS
```

**Cleanup Stale Locks**:

```
Function: cleanup_stale_locks(scope, max_age_seconds=300):
  lock_dir = ".locks/"
  cleaned = []

  for lock_file in glob(lock_dir + scope + "_*.lock"):
    age = now() - file_mtime(lock_file)
    if age > max_age_seconds:
      delete(lock_file)
      cleaned.append(lock_file)

  return cleaned
```

### Lock Scopes

| Scope | Purpose | Path |
|-------|---------|------|
| `outputs_research` | Research outputs | outputs/01_understanding_in_progress/ |
| `outputs_design` | Design outputs | outputs/03_design_decisions/ |
| `episodic_changes` | Change logs | outputs/episodic/changes/ |
| `handoff_incoming` | Incoming handoffs | hand_off_documents/incoming/ |
| `handoff_outgoing` | Outgoing handoffs | hand_off_documents/outgoing/ |

---

## Component 2: Change Detector

### Purpose
Detect what changed since agent last checked, enabling efficient propagation to dependent agents.

### Design

**Hash-Based Divergence Detection** (using Git):

```
Function: compute_hash(path):
  // Compute Merkle-DAG-style hash
  if is_file(path):
    return sha256_file(path)

  if is_directory(path):
    hashes = []
    for each file in directory (sorted):
      hashes.append(compute_hash(file))

    combined = concatenate(hashes)
    return sha256(combined)

Function: detect_changes(scope):
  hash_before = read_from_log(scope + "_hash_before")
  path = resolve_scope_to_path(scope)
  hash_after = compute_hash(path)

  if hash_before != hash_after:
    return CHANGED
  else:
    return UNCHANGED
```

**Divergence Log Format**:

```
# outputs/episodic/changes/divergence.log

Timestamp | Agent | Scope | Action | Hash Before | Hash After
2026-01-30T14:23:45Z | agent_research_01 | outputs_research | CREATED | initial | hash_abc123
2026-01-30T14:25:12Z | agent_research_01 | outputs_research | MODIFIED | hash_abc123 | hash_def456
2026-01-30T14:27:33Z | agent_design_01 | outputs_design | CREATED | initial | hash_xyz789
```

### Propagation Trigger

```
Function: propagate_changes(agent_id, dependencies=[]):
  // Called after agent completes work

  changed_scopes = []

  for scope in get_all_scopes():
    if is_changed(scope):
      changed_scopes.append(scope)
      log_to_divergence_log(agent_id, scope, "MODIFIED")

  // Notify dependent agents
  for dependent in dependencies:
    notify_agent(dependent, "Scopes changed: " + changed_scopes)

  return changed_scopes
```

---

## Component 3: Conflict Resolver

### Purpose
When multiple agents modify the same file, resolve conflicts deterministically.

### Design

**Conflict Detection**:

```
Function: detect_conflict(file_path):
  // Check if multiple agents modified this file in last update

  change_log = read_divergence_log()

  file_modifications = filter(change_log, lambda x: x.scope == file_path)

  if count(file_modifications) > 1:
    // Multiple agents touched this file
    // Extract their timestamps
    timestamps = [m.timestamp for m in file_modifications]
    agents = [m.agent_id for m in file_modifications]

    return {
      "conflict": true,
      "agents": agents,
      "timestamps": timestamps,
      "affected_file": file_path
    }

  return {"conflict": false}
```

**Conflict Resolution Strategy: Last-Write-Wins**:

```
Function: resolve_conflict_last_write_wins(file_path, conflict_info):
  // Keep version with latest timestamp

  agents = conflict_info.agents
  timestamps = conflict_info.timestamps

  winning_agent = agents[timestamps.index(max(timestamps))]
  winning_timestamp = max(timestamps)

  // Read both versions
  version_A = read_file(file_path + ".agent_A")
  version_B = read_file(file_path + ".agent_B")

  if timestamp_A > timestamp_B:
    final_content = version_A
    winner = "agent_A"
  else:
    final_content = version_B
    winner = "agent_B"

  // Write resolved version
  write_atomic(file_path, final_content)

  // Log resolution
  log_conflict_resolution(file_path, winner, winning_timestamp)

  return winner
```

**Conflict Log Format**:

```
# outputs/episodic/changes/conflicts.log

Timestamp | File | Agents | Resolution | Winner | Winner Timestamp
2026-01-30T14:30:00Z | hand_off_documents/task.md | agent_research_01, agent_design_01 | last-write-wins | agent_design_01 | 2026-01-30T14:27:45Z
```

---

## Component 4: Episodic Logger

### Purpose
Record all multi-agent sync events for session continuity and debugging.

### Design

**Event Logging**:

```
Function: log_event(event_type, details):
  timestamp = iso8601_now()

  event = {
    "timestamp": timestamp,
    "type": event_type,  // LOCK_ACQUIRED, LOCK_RELEASED, CONFLICT, RESOLVED
    "agent_id": current_agent(),
    "scope": current_scope(),
    "details": details
  }

  append_to_file("outputs/episodic/changes/sync_events.log", event)

  if event_type == "CONFLICT":
    append_to_file("outputs/episodic/changes/conflicts.log", event)

Function: end_session():
  // Create session summary
  events = read_all_events_this_session()

  session_summary = {
    "timestamp": iso8601_now(),
    "agent_id": current_agent(),
    "start_time": session_start_time,
    "duration": now() - session_start_time,
    "events": events,
    "files_modified": count_modified_files(),
    "conflicts_detected": count_conflicts(),
    "conflicts_resolved": count_resolutions()
  }

  write_to_episodic("outputs/episodic/sessions/YYYY-MM-DD_session_NNN.md", session_summary)
```

---

## Data Flow

### Parallel Execution Scenario

```
Timeline:

T=0:   Agent A starts → Acquires lock on outputs_research
T=1:   Agent B starts → Waits for lock (already acquired)
T=2:   Agent A writes to file → Uses atomic write (.tmp + rename)
T=3:   Agent A updates divergence.log → MODIFIED hash_x → hash_y
T=4:   Agent A releases lock

T=5:   Agent B acquires lock
T=6:   Agent B reads divergence.log → Sees hash changed!
T=7:   Agent B re-reads modified files to update context
T=8:   Agent B writes to own files → No conflict
T=9:   Agent B updates divergence.log → CREATED hash_z
T=10:  Agent B releases lock

Result: Agent B correctly incorporated Agent A's changes
```

### Conflict Scenario

```
Timeline:

T=0:    Agent A acquires lock for hand_off_documents
T=1:    Agent A writes task.md → Updates divergence.log
T=2:    Agent A releases lock

T=3:    Agent B acquires lock for hand_off_documents
T=4:    Agent B modifies task.md (same file!) → Updates divergence.log

Conflict Detection:
T=5:    divergence.log shows:
        - Agent A modified task.md at T=1
        - Agent B modified task.md at T=4
        - CONFLICT DETECTED

Resolution:
T=6:    Apply last-write-wins
        - Agent B's version (T=4) is newer
        - Keep Agent B's content
        - Log resolution in conflicts.log

Result: Conflict resolved, no data loss, decision recorded
```

---

## Error Cases & Recovery

### Case 1: Agent Crashes Mid-Write

**Scenario**: Agent A acquires lock, starts writing, then crashes.

**Detection**:
```
Lock file exists: .locks/outputs_research_agent_A.lock
Lock age: 10 minutes (> 5 minute TTL)
→ Lock is stale
```

**Recovery**:
```
1. Clean up stale lock: rm .locks/outputs_research_agent_A.lock
2. Check outputs_research/ for .tmp files: *.tmp
3. If .tmp files exist, delete them (incomplete writes)
4. Next agent (B) can now acquire lock
5. Log to episodic: "Stale lock cleaned for agent_A"
```

### Case 2: Network Sync Conflict (Syncthing)

**Scenario**: Two machines sync with conflicting changes (both modified same file).

**Detection**:
```
Syncthing creates: hand_off_documents/task.md.sync-conflict-20260130-142345.md
```

**Recovery**:
```
1. Detect .sync-conflict files
2. Try 3-way merge: git merge-base
3. If automatic merge fails:
   - Log to conflicts.log: "Manual merge needed"
   - Alert human: "Sync conflict in [file]"
   - Don't auto-resolve (too risky)
```

### Case 3: Divergence Log Corruption

**Scenario**: divergence.log is truncated or unreadable.

**Detection**:
```
read_divergence_log() throws exception
```

**Recovery**:
```
1. Restore from git: git checkout outputs/episodic/changes/divergence.log
2. Recompute hash of all scopes from current filesystem state
3. Rebuild divergence.log with computed hashes
4. Log: "Divergence log rebuilt from filesystem state"
```

---

## Testing Strategy

### Unit Tests

1. **Lock Manager**
   - [ ] acquire_lock succeeds
   - [ ] acquire_lock fails when already held
   - [ ] acquire_lock succeeds after cleanup of stale lock
   - [ ] release_lock succeeds
   - [ ] release_lock fails for wrong agent

2. **Change Detector**
   - [ ] Hash changes when file modified
   - [ ] Hash unchanged when file not modified
   - [ ] Detects changes in directories recursively
   - [ ] Handles missing files gracefully

3. **Conflict Resolver**
   - [ ] Detects conflicts in divergence.log
   - [ ] Applies last-write-wins resolution
   - [ ] Logs resolution correctly
   - [ ] Handles edge cases (both same timestamp)

### Integration Tests

1. **Sequential Agents**
   - [ ] Agent A locks, writes, releases
   - [ ] Agent B acquires immediately after
   - [ ] No conflicts, data correct

2. **Concurrent Agents**
   - [ ] Agent A and B start together
   - [ ] One blocks until other releases lock
   - [ ] No deadlock after 5 minutes
   - [ ] Change propagation works

3. **Crash Recovery**
   - [ ] Agent A crashes while holding lock
   - [ ] Agent B detects stale lock
   - [ ] Agent B continues without deadlock

---

## Performance Considerations

| Operation | Expected Time | Scalability |
|-----------|---------------|-------------|
| Acquire lock (no contention) | <100ms | O(1) |
| Detect stale lock | <500ms | O(num_locks) |
| Compute hash (10GB data) | ~5s | O(n) where n=bytes |
| Detect change | <1s | O(1) lookup |
| Resolve conflict | <100ms | O(1) |
| Clean stale locks | <1s | O(num_stale) |

---

## Configuration Parameters

| Parameter | Default | Purpose |
|-----------|---------|---------|
| Lock TTL | 5 min | How long before stale lock considered abandoned |
| Max retries | 10 | How many times to retry lock acquisition |
| Retry delay | 0.5s | How long to wait between retries |
| Conflict log | unlimited | Size limit for conflicts.log |
| Divergence log | unlimited | Size limit for divergence.log |

---

## Implementation Checklist

- [ ] Design lock file format and locking semantics
- [ ] Implement acquire_lock() function
- [ ] Implement release_lock() function
- [ ] Implement cleanup_stale_locks() function
- [ ] Design divergence.log format
- [ ] Implement compute_hash() function
- [ ] Implement detect_changes() function
- [ ] Implement conflict detection
- [ ] Implement last-write-wins resolution
- [ ] Implement conflict logging
- [ ] Design and create episodic logging system
- [ ] Create unit tests for each component
- [ ] Create integration tests for scenarios
- [ ] Create crash recovery tests
- [ ] Performance profiling and optimization

