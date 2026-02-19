# Is Your System Multi-Agent?

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Whether your layer-stage system constitutes multi-agent architecture

---

## The Question

You have:
- Different agent identities per layer (layer_0, layer_1, layer_-1)
- Different agent identities per stage (01-11)
- Different agent identities per sub-layer
- Each with its own CLAUDE.md / 0AGNOSTIC.md
- Each with its own outputs/memory
- Handoff documents for communication

**Does this count as multi-agent? Would you benefit from SHIMI-style sync?**

---

## Two Ways to Look at It

### View 1: Conceptual Multi-Agent (What You Have)

```
┌─────────────────────────────────────────┐
│            Same Claude Instance          │
│                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │ Layer 0  │  │ Layer 1  │  │Layer -1│ │
│  │  Agent   │  │  Agent   │  │ Agent  │ │
│  └──────────┘  └──────────┘  └────────┘ │
│         ↑           ↑            ↑       │
│         └───────────┴────────────┘       │
│              Context Switching           │
└─────────────────────────────────────────┘
```

- **Same process** - One Claude instance
- **Sequential** - One context active at a time
- **Shared filesystem** - All agents see same files instantly
- **No sync needed** - Changes are immediate

### View 2: True Multi-Agent (What SHIMI Assumes)

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Agent A  │    │ Agent B  │    │ Agent C  │
│ (own mem)│    │ (own mem)│    │ (own mem)│
└────┬─────┘    └────┬─────┘    └────┬─────┘
     │               │               │
     └───────────────┴───────────────┘
              Network / Async Sync
```

- **Separate processes** - Independent Claude instances
- **Parallel** - Multiple agents working simultaneously
- **Separate memory** - Each has own copy
- **Sync required** - Need Merkle-DAG, Bloom, CRDT

---

## Your Current Reality

| Aspect | Your System | True Multi-Agent |
|--------|-------------|------------------|
| Processes | 1 Claude instance | N separate instances |
| Execution | Sequential (one context) | Parallel |
| Memory | Shared filesystem | Separate per agent |
| Sync | Instant (same files) | Needed (network) |
| Conflicts | Rare (you control) | Common (parallel writes) |

**Right now: Conceptual multi-agent, but implemented as single agent with context switching.**

---

## When You WOULD Need SHIMI-Style Sync

### Scenario 1: Parallel Claude Sessions

```
Terminal 1: Claude working on layer_0
Terminal 2: Claude working on layer_1
Terminal 3: Claude working on stage_-1_02

All running simultaneously, all writing to outputs/
```

→ **Conflict risk**: Multiple sessions writing to same or related files
→ **Would benefit from**: CRDT-style merge, conflict detection

### Scenario 2: Distributed Across Machines

```
Machine A: Claude on layer_0 (Ubuntu)
Machine B: Claude on layer_1 (WSL)

Syncthing syncs filesystem, but...
Both write to hand_off_documents/ at same time
```

→ **Conflict risk**: Sync conflicts across devices
→ **Would benefit from**: Merkle-DAG for divergence detection

### Scenario 3: Autonomous Agent Swarm

```
Spawn agent for each stage
All work in parallel
Report back when done
```

→ **Real multi-agent**: Separate processes, parallel execution
→ **Would need**: Full SHIMI-style infrastructure

---

## What You Actually Need (Probably)

### Current State: Nothing Extra

- Single Claude session at a time
- Git handles cross-device sync
- Conflicts are rare and manual

### Near-Term: Lightweight Conflict Prevention

If you start running parallel sessions:

```markdown
# In each CLAUDE.md / 0AGNOSTIC.md

## Locking Protocol
Before writing to shared locations:
1. Check for .lock file
2. Create .lock with session ID
3. Write changes
4. Remove .lock
```

Simple file locking, no complex infrastructure.

### Future: If True Multi-Agent

If you build actual parallel agents:

1. **Consider SHIMI concepts** - Hierarchical memory with sync
2. **Or simpler alternatives**:
   - Git branches per agent, merge when done
   - Message queue for handoffs (Redis, files)
   - Database with transactions

---

## Key Insight

Your system is **architecturally prepared** for multi-agent but **operationally single-agent**.

| Prepared | Operational |
|----------|-------------|
| Each layer has own identity | One Claude at a time |
| Handoff documents exist | Used sequentially |
| Hierarchical structure | Traversed by one agent |

**You could evolve to true multi-agent without restructuring.** The layer-stage-handoff architecture supports it. You'd just need to add sync mechanisms when parallel execution becomes real.

---

## Recommendation

1. **Don't add SHIMI sync now** - You don't have parallel agents yet
2. **Keep your architecture** - It's multi-agent ready
3. **Add locking if needed** - Simple `.lock` files for parallel sessions
4. **Revisit when scaling** - If you spawn actual parallel agents, then consider Merkle-DAG/CRDT

Your system is future-proof. The sync problem will become real when you have true parallelism, not before.

---

## Summary

| Question | Answer |
|----------|--------|
| Is your system multi-agent? | Conceptually yes, operationally no |
| Do you need SHIMI sync now? | No - single agent, shared filesystem |
| Could you use it later? | Yes - architecture supports it |
| What to do now? | Nothing, or simple locking if parallel sessions |
