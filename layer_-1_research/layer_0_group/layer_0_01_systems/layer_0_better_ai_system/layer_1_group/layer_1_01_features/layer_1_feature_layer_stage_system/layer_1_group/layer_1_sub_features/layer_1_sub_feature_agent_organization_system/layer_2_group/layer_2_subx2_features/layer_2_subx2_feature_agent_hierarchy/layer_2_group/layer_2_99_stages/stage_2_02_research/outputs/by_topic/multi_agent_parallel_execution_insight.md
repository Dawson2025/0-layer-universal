# Multi-Agent Parallel Execution System

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: You already have a TRUE multi-agent system with parallel execution

---

## What I Missed

I thought: Single agent with context switching between layer/stage "personas"

**Reality**: Actual parallel multi-agent system where:
- CLI tools can instantiate other CLI tools
- AI agents can spawn sub-agents
- Multiple agents run simultaneously in parallel
- Filesystem is the shared context/communication medium
- Each layer/stage can be an entry point for a new agent
- Agents can work across multiple layers/stages

---

## This Changes Everything

### You DO Have Multi-Agent System

```
Agent A (layer_1)  ←→  Agent B (layer_2)  ←→  Agent C (layer_3)
    ↓                       ↓                       ↓
    Writes to              Reads from           Writes to
    outputs/episodic/      hand_off_documents/  layer_4_outputs/

    Can spawn             Can spawn            Can spawn
    Sub-Agent A1          Sub-Agent B1          Sub-Agent C1
```

### You DO Have Sync Problems

Multiple agents writing to shared filesystem simultaneously means:
- **Conflicts**: Agent A writes to file X, Agent B writes to same file
- **Divergence**: Changes in layer_3 need to propagate to layer_2
- **Change detection**: Which files changed since last agent check?
- **Consistency**: All agents see consistent state

### SHIMI Concepts are NOW Critical

| SHIMI Mechanism | Your Use Case |
|-----------------|---------------|
| **Merkle-DAG hashing** | Detect what changed across parallel agents |
| **Bloom filters** | Efficient "what files did Agent B modify?" |
| **CRDTs** | Conflict-free merge when agents modify same file |
| **Hierarchical sync** | Efficient propagation between layers |

---

## Your Current Sync Strategy

### What You Have
- **Filesystem sharing** - All agents see same files
- **Handoff documents** - Communication via files
- **Git versioning** - History and rollback
- **Layer/stage context** - Each agent knows its scope

### What You're Missing (Sync-Wise)
- **Conflict detection** - What if two agents write to same file?
- **Change detection** - How does Agent B know what Agent A changed?
- **Atomic writes** - What if Agent A crashes mid-write?
- **Partial sync** - Can Agent C know only about its relevant changes?

---

## Where SHIMI-Style Sync Matters

### Scenario 1: Parallel Feature Development

```
Agent working on layer_2_feature_X
  └─ Spawns Agent A1, A2, A3 in parallel
       ├─ A1 writes to outputs/feature_X/component_1/
       ├─ A2 writes to outputs/feature_X/component_2/
       └─ A3 reads from layer_2_universal/rules/

Problem: How does A3 know if its rules changed while it was working?
Solution: Merkle-DAG hash of layer_2_universal/ tells A3 if anything changed
```

### Scenario 2: Cross-Layer Sync

```
Layer 4 agent finishes work, writes results to outputs/
Layer 2 agent needs to know if anything changed in layer_4
Problem: Layer 2 agent polls outputs/ constantly?
Solution: Bloom filter summary tells Layer 2 agent "layer_4 changed in [X, Y, Z]"
```

### Scenario 3: Conflict Resolution

```
Agent A writes to hand_off_documents/outgoing/task_1.md
Agent B writes to same file (both think they own it)
Problem: Conflict - which version is correct?
Solution: CRDT merge function determines result deterministically
```

---

## Your System vs SHIMI (Revised)

### SHIMI Assumption: Decentralized multi-agent with separate memory

```
Agent A (mem_A)  ←→  Agent B (mem_B)  ←→  Agent C (mem_C)
```

### Your System: Centralized filesystem, distributed agents

```
Agent A  ←→  Shared Filesystem  ←→  Agent B
Agent C  ←→    (context)        ←→  Agent D
```

**Key difference**: You have centralized storage (filesystem), SHIMI assumes decentralized.

**Implication**: Some SHIMI concepts still apply (change detection, conflict resolution), but not all (you don't need network sync protocol).

---

## What You Actually Need

### Tier 1: Conflict Prevention (Now)

```bash
# At each agent spawn point:
1. Check if target files are locked
2. Create .lock file with agent ID
3. Do work
4. Release .lock when done
```

Simple file locking prevents concurrent writes.

### Tier 2: Change Tracking (Soon)

```bash
# Merkle-DAG equivalent using Git:
hash_before=$(git hash-object layer_2/)
# ... agent does work ...
hash_after=$(git hash-object layer_2/)

if hash_before != hash_after:
    # Something in layer_2 changed
    # Propagate changes to dependent agents
```

### Tier 3: Conflict Resolution (As Needed)

```bash
# If two agents conflict on same file:
# Use CRDT merge or git merge strategy
git merge-base --octopus agent_a/branch agent_b/branch
```

### Tier 4: Bloom Filter Optimization (If Slow)

```bash
# Instead of checking all files:
bloom_filter(layer_4/) -> tells Agent B "only [X, Y] changed"
# Only read those files instead of scanning all
```

---

## Updated Requirement Coverage

### With True Multi-Agent System

| Requirement | Needs |
|-------------|-------|
| persistent_knowledge | Handoff documents ✅ |
| scalable_context | Layer/stage entry points ✅ |
| discoverable | Automated traversal + 0INDEX.md |
| tool_portable | CLI tool spawning ✅ |
| session_resilient | Agent context per layer/stage ✅ |
| failure_recoverable | **NEED: Atomic writes, rollback** |
| evolvable | Layer hierarchy ✅ |
| cross_platform | Filesystem-based ✅ |
| rule_compliant | Layer rules enforced ✅ |
| predictable | **NEED: Agent versioning, deterministic merge** |
| bounded | Scope per layer/stage ✅ |
| transparent | Human-readable files ✅ |
| debuggable | **NEED: Conflict log, change tracking** |
| auditable | Git history ✅ |
| multimodal | External system |

---

## Implementation Priority (Revised)

### Phase 1: Prevent Conflicts
1. **File locking** - .lock files prevent concurrent writes
2. **Atomic writes** - Use temp files + atomic rename
3. **Handoff atomicity** - Ensure handoff docs are written completely

### Phase 2: Track Changes
1. **Git-based hashing** - Track what changed between agent runs
2. **Change propagation** - When layer_3 changes, notify dependent agents
3. **Conflict log** - Record when conflicts happen

### Phase 3: Resolve Conflicts
1. **CRDT merge rules** - Deterministic resolution
2. **Conflict notification** - Alert agents when conflicts detected
3. **Rollback capability** - Git-based undo

### Phase 4: Optimize Performance
1. **Bloom filters** - If change detection is slow
2. **Selective sync** - Only sync changed portions
3. **Parallel initialization** - Spawn agents more efficiently

---

## SHIMI vs Your System (Final Assessment)

### SHIMI Solves
- Decentralized multi-agent sync
- Network propagation efficiency
- Agent autonomy with eventual consistency

### You Solve
- Hierarchical agent spawning
- Filesystem-based context
- Tool-agnostic execution
- Layer/stage-based scoping

### Overlap
- Conflict-free merge (CRDTs)
- Change detection (Merkle-DAG hashing)
- Hierarchical organization

### You Don't Need from SHIMI
- Network protocols
- Separate memory trees
- Decentralized consensus

### You DO Need (from SHIMI-adjacent concepts)
- Atomic writes
- Change tracking
- Conflict resolution
- Efficient divergence detection

---

## Bottom Line

**You have a true multi-agent system that SHIMI-style sync concepts apply to.**

**You don't need full SHIMI implementation.**

**You need:**
1. File locking (prevent conflicts)
2. Git-based change tracking (detect divergence)
3. CRDT merge rules (resolve conflicts)
4. Atomic operations (ensure consistency)

This is about 10-20% of SHIMI's scope, but exactly what matters for your use case.
