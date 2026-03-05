---
resource_id: "375e55f8-e29a-4e82-a28f-6e251e232452"
resource_type: "output"
resource_name: "multi_agent_parallel_execution_insight"
---
# Multi-Agent Parallel Execution System

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: You already have a TRUE multi-agent system with parallel execution

---

<!-- section_id: "c573e9be-85c9-4a6d-9c42-389e7be0fa6c" -->
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

<!-- section_id: "40e5267f-7f1f-4d8b-ae80-5ab2cb56ce1f" -->
## This Changes Everything

<!-- section_id: "a38a2f17-84ab-43cf-8749-cbd5cf052cda" -->
### You DO Have Multi-Agent System

```
Agent A (layer_1)  ←→  Agent B (layer_2)  ←→  Agent C (layer_3)
    ↓                       ↓                       ↓
    Writes to              Reads from           Writes to
    outputs/episodic/      hand_off_documents/  layer_4_outputs/

    Can spawn             Can spawn            Can spawn
    Sub-Agent A1          Sub-Agent B1          Sub-Agent C1
```

<!-- section_id: "a82f0a3b-8545-4328-9983-6b147feced2d" -->
### You DO Have Sync Problems

Multiple agents writing to shared filesystem simultaneously means:
- **Conflicts**: Agent A writes to file X, Agent B writes to same file
- **Divergence**: Changes in layer_3 need to propagate to layer_2
- **Change detection**: Which files changed since last agent check?
- **Consistency**: All agents see consistent state

<!-- section_id: "d13507c3-eaa0-46f0-9f7a-17bf41dd9d1e" -->
### SHIMI Concepts are NOW Critical

| SHIMI Mechanism | Your Use Case |
|-----------------|---------------|
| **Merkle-DAG hashing** | Detect what changed across parallel agents |
| **Bloom filters** | Efficient "what files did Agent B modify?" |
| **CRDTs** | Conflict-free merge when agents modify same file |
| **Hierarchical sync** | Efficient propagation between layers |

---

<!-- section_id: "1c4adbe5-06dd-4fdc-9f27-a486c38d100b" -->
## Your Current Sync Strategy

<!-- section_id: "72281734-f3c2-44b0-84f8-fda7849819b1" -->
### What You Have
- **Filesystem sharing** - All agents see same files
- **Handoff documents** - Communication via files
- **Git versioning** - History and rollback
- **Layer/stage context** - Each agent knows its scope

<!-- section_id: "74290053-0a06-455e-bace-9878f8c88f46" -->
### What You're Missing (Sync-Wise)
- **Conflict detection** - What if two agents write to same file?
- **Change detection** - How does Agent B know what Agent A changed?
- **Atomic writes** - What if Agent A crashes mid-write?
- **Partial sync** - Can Agent C know only about its relevant changes?

---

<!-- section_id: "f9c7a8e1-29c1-445b-be43-d42600e0a35f" -->
## Where SHIMI-Style Sync Matters

<!-- section_id: "9e3e695d-680a-42cc-aae3-920ed07fefd6" -->
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

<!-- section_id: "7e17f08a-52fb-472a-9e05-d44cb564a28a" -->
### Scenario 2: Cross-Layer Sync

```
Layer 4 agent finishes work, writes results to outputs/
Layer 2 agent needs to know if anything changed in layer_4
Problem: Layer 2 agent polls outputs/ constantly?
Solution: Bloom filter summary tells Layer 2 agent "layer_4 changed in [X, Y, Z]"
```

<!-- section_id: "93687cbc-f0b2-4d03-96c8-ea214a0eaf06" -->
### Scenario 3: Conflict Resolution

```
Agent A writes to hand_off_documents/outgoing/task_1.md
Agent B writes to same file (both think they own it)
Problem: Conflict - which version is correct?
Solution: CRDT merge function determines result deterministically
```

---

<!-- section_id: "99a1df19-21e6-4868-8f83-4186b4d98824" -->
## Your System vs SHIMI (Revised)

<!-- section_id: "c94e9e69-cf0b-40cc-95bf-be272ec17055" -->
### SHIMI Assumption: Decentralized multi-agent with separate memory

```
Agent A (mem_A)  ←→  Agent B (mem_B)  ←→  Agent C (mem_C)
```

<!-- section_id: "3bc3629e-4a85-4940-b059-4b63b55c0921" -->
### Your System: Centralized filesystem, distributed agents

```
Agent A  ←→  Shared Filesystem  ←→  Agent B
Agent C  ←→    (context)        ←→  Agent D
```

**Key difference**: You have centralized storage (filesystem), SHIMI assumes decentralized.

**Implication**: Some SHIMI concepts still apply (change detection, conflict resolution), but not all (you don't need network sync protocol).

---

<!-- section_id: "67a71edd-f090-4874-989e-c73bca576409" -->
## What You Actually Need

<!-- section_id: "b697d7fd-a43d-43f0-b2cf-f1b64e80f6c0" -->
### Tier 1: Conflict Prevention (Now)

```bash
# At each agent spawn point:
1. Check if target files are locked
2. Create .lock file with agent ID
3. Do work
4. Release .lock when done
```

Simple file locking prevents concurrent writes.

<!-- section_id: "84e2c268-209d-4347-8160-b2be160debfc" -->
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

<!-- section_id: "5bff487e-1ac5-4ff0-b5a2-48ba1180e455" -->
### Tier 3: Conflict Resolution (As Needed)

```bash
# If two agents conflict on same file:
# Use CRDT merge or git merge strategy
git merge-base --octopus agent_a/branch agent_b/branch
```

<!-- section_id: "f7f340e9-3163-42f8-b6e6-c119f3ccd104" -->
### Tier 4: Bloom Filter Optimization (If Slow)

```bash
# Instead of checking all files:
bloom_filter(layer_4/) -> tells Agent B "only [X, Y] changed"
# Only read those files instead of scanning all
```

---

<!-- section_id: "0dfea5c6-1938-4c8c-ba02-32e61559eb83" -->
## Updated Requirement Coverage

<!-- section_id: "1874d7e4-c81f-488a-a7a7-b77ea981b0f6" -->
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

<!-- section_id: "b0596e78-33c0-438e-913a-0c0f270436e9" -->
## Implementation Priority (Revised)

<!-- section_id: "beea5428-761e-451b-9f84-b6b56bce5fea" -->
### Phase 1: Prevent Conflicts
1. **File locking** - .lock files prevent concurrent writes
2. **Atomic writes** - Use temp files + atomic rename
3. **Handoff atomicity** - Ensure handoff docs are written completely

<!-- section_id: "bbf9fe4d-d2e6-400f-8c3a-6900547397a6" -->
### Phase 2: Track Changes
1. **Git-based hashing** - Track what changed between agent runs
2. **Change propagation** - When layer_3 changes, notify dependent agents
3. **Conflict log** - Record when conflicts happen

<!-- section_id: "3f4e7392-2b6a-4436-8b16-6d9c912fda20" -->
### Phase 3: Resolve Conflicts
1. **CRDT merge rules** - Deterministic resolution
2. **Conflict notification** - Alert agents when conflicts detected
3. **Rollback capability** - Git-based undo

<!-- section_id: "525f3705-1c56-4242-a58d-de30763a0e8d" -->
### Phase 4: Optimize Performance
1. **Bloom filters** - If change detection is slow
2. **Selective sync** - Only sync changed portions
3. **Parallel initialization** - Spawn agents more efficiently

---

<!-- section_id: "a10d5177-9213-4cc2-940c-0397b213a8f2" -->
## SHIMI vs Your System (Final Assessment)

<!-- section_id: "2b008a78-1c07-41ae-80fa-35cd0e78e886" -->
### SHIMI Solves
- Decentralized multi-agent sync
- Network propagation efficiency
- Agent autonomy with eventual consistency

<!-- section_id: "5cc16a38-d018-42df-bc26-b025a4737fb5" -->
### You Solve
- Hierarchical agent spawning
- Filesystem-based context
- Tool-agnostic execution
- Layer/stage-based scoping

<!-- section_id: "c6ce48aa-657c-402d-94a8-a9c184d0a675" -->
### Overlap
- Conflict-free merge (CRDTs)
- Change detection (Merkle-DAG hashing)
- Hierarchical organization

<!-- section_id: "427f1755-dbea-470e-a668-e60309d9527b" -->
### You Don't Need from SHIMI
- Network protocols
- Separate memory trees
- Decentralized consensus

<!-- section_id: "6e49fd42-9aba-493b-8b87-c42dce908310" -->
### You DO Need (from SHIMI-adjacent concepts)
- Atomic writes
- Change tracking
- Conflict resolution
- Efficient divergence detection

---

<!-- section_id: "662efabb-8910-46ec-9fe3-add81568f403" -->
## Bottom Line

**You have a true multi-agent system that SHIMI-style sync concepts apply to.**

**You don't need full SHIMI implementation.**

**You need:**
1. File locking (prevent conflicts)
2. Git-based change tracking (detect divergence)
3. CRDT merge rules (resolve conflicts)
4. Atomic operations (ensure consistency)

This is about 10-20% of SHIMI's scope, but exactly what matters for your use case.
