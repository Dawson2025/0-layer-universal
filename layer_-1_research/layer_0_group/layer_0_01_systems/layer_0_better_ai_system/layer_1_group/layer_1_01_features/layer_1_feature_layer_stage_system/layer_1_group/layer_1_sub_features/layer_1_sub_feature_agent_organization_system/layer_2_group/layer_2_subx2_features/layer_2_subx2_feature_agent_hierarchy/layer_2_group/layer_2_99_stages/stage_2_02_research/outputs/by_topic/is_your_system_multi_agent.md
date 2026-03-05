---
resource_id: "2bc42616-f43c-484e-96f8-9356efd9ed0b"
resource_type: "output"
resource_name: "is_your_system_multi_agent"
---
# Is Your System Multi-Agent?

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Whether your layer-stage system constitutes multi-agent architecture

---

<!-- section_id: "b1625882-f05a-4884-a0eb-e79d1ad7ef21" -->
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

<!-- section_id: "1813e791-b194-436f-90de-eb52f65b9727" -->
## Two Ways to Look at It

<!-- section_id: "a2432b27-1160-4229-b9d6-41343574fb05" -->
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

<!-- section_id: "5de4ac7d-5568-417b-bfe5-1cf5e6a94d4f" -->
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

<!-- section_id: "ab74f892-ffcc-4089-9199-b051c5c72f2a" -->
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

<!-- section_id: "c0e474dc-48d1-4f14-b8b9-ca88e611d535" -->
## When You WOULD Need SHIMI-Style Sync

<!-- section_id: "048fc9e0-8320-4738-b664-e5b95fc82b29" -->
### Scenario 1: Parallel Claude Sessions

```
Terminal 1: Claude working on layer_0
Terminal 2: Claude working on layer_1
Terminal 3: Claude working on stage_-1_02

All running simultaneously, all writing to outputs/
```

→ **Conflict risk**: Multiple sessions writing to same or related files
→ **Would benefit from**: CRDT-style merge, conflict detection

<!-- section_id: "7623cfc7-9c97-424c-88f0-803a3e28f53b" -->
### Scenario 2: Distributed Across Machines

```
Machine A: Claude on layer_0 (Ubuntu)
Machine B: Claude on layer_1 (WSL)

Syncthing syncs filesystem, but...
Both write to hand_off_documents/ at same time
```

→ **Conflict risk**: Sync conflicts across devices
→ **Would benefit from**: Merkle-DAG for divergence detection

<!-- section_id: "5697dee4-5fad-4f65-b557-10e788cb00ba" -->
### Scenario 3: Autonomous Agent Swarm

```
Spawn agent for each stage
All work in parallel
Report back when done
```

→ **Real multi-agent**: Separate processes, parallel execution
→ **Would need**: Full SHIMI-style infrastructure

---

<!-- section_id: "a60e4d6b-2cc0-4249-ae74-117bf4473ce5" -->
## What You Actually Need (Probably)

<!-- section_id: "f74ce2ca-4040-4514-be1f-a275854ca940" -->
### Current State: Nothing Extra

- Single Claude session at a time
- Git handles cross-device sync
- Conflicts are rare and manual

<!-- section_id: "68275158-74c0-4e2c-96d2-5c8194ad2d61" -->
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

<!-- section_id: "00a30fcf-e384-4df0-a9c5-643b3fa74c30" -->
### Future: If True Multi-Agent

If you build actual parallel agents:

1. **Consider SHIMI concepts** - Hierarchical memory with sync
2. **Or simpler alternatives**:
   - Git branches per agent, merge when done
   - Message queue for handoffs (Redis, files)
   - Database with transactions

---

<!-- section_id: "d552572d-d6aa-4aa6-a250-5afa2d0ef3dd" -->
## Key Insight

Your system is **architecturally prepared** for multi-agent but **operationally single-agent**.

| Prepared | Operational |
|----------|-------------|
| Each layer has own identity | One Claude at a time |
| Handoff documents exist | Used sequentially |
| Hierarchical structure | Traversed by one agent |

**You could evolve to true multi-agent without restructuring.** The layer-stage-handoff architecture supports it. You'd just need to add sync mechanisms when parallel execution becomes real.

---

<!-- section_id: "ff4a96e2-3cdc-4c8b-87e4-7e0364e1ccde" -->
## Recommendation

1. **Don't add SHIMI sync now** - You don't have parallel agents yet
2. **Keep your architecture** - It's multi-agent ready
3. **Add locking if needed** - Simple `.lock` files for parallel sessions
4. **Revisit when scaling** - If you spawn actual parallel agents, then consider Merkle-DAG/CRDT

Your system is future-proof. The sync problem will become real when you have true parallelism, not before.

---

<!-- section_id: "9db740b8-e0ba-4a0a-a854-9c3f5a840978" -->
## Summary

| Question | Answer |
|----------|--------|
| Is your system multi-agent? | Conceptually yes, operationally no |
| Do you need SHIMI sync now? | No - single agent, shared filesystem |
| Could you use it later? | Yes - architecture supports it |
| What to do now? | Nothing, or simple locking if parallel sessions |
