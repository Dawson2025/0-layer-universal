# SHIMI Sync Mechanisms Explained

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Merkle-DAG, Bloom filters, CRDTs in SHIMI

---

## Context: What Are These For?

These mechanisms are for **decentralized sync** between multiple agents - NOT for retrieval.

```
Agent A (has memory tree)  ←→  Agent B (has memory tree)
                    ↓
         Need to sync changes
         Without sending everything
         Without conflicts breaking things
```

---

## 1. Merkle-DAG (Detecting What Changed)

### What It Is
A hash tree where each node's hash includes its children's hashes. If anything changes, the root hash changes.

### How SHIMI Uses It

```
Agent A: H_a = MerkleHash(Tree_A)
Agent B: H_b = MerkleHash(Tree_B)

If H_a ≠ H_b:
    Find smallest differing subtree by comparing child hashes
    Only sync that subtree
```

### Why It Matters
- Don't send entire memory tree
- Quickly find exactly what diverged
- Like Git's content-addressed storage

### Analogy
Git commit hashes work the same way. If two repos have same commit hash, they have same content. If different, you can walk the tree to find where they diverged.

---

## 2. Bloom Filters (Efficient "Do You Have This?")

### What It Is
A space-efficient probabilistic data structure that answers "is X in this set?" with:
- Definite NO (if filter says no)
- Probably YES (small false positive rate)

### How SHIMI Uses It

```
Agent A has divergent subtree T_d
Agent A: B = BloomFilter(nodes in T_d)
Agent A sends B to Agent B (tiny, ~1KB)

Agent B: Tests each of its nodes against B
Agent B: "I'm missing nodes X, Y, Z"
Agent B: Requests only X, Y, Z from Agent A
```

### Why It Matters
- Filter is tiny compared to actual data
- No need to list all node IDs
- Bandwidth efficient

### Analogy
Like asking "does this grocery list contain items starting with A-M?" instead of reading the whole list.

---

## 3. CRDTs (Conflict-Free Merge)

### What It Is
Conflict-Free Replicated Data Types - data structures that can be merged without conflicts, regardless of order.

### Properties Required
```
Commutativity:  merge(A, B) = merge(B, A)
Idempotence:    merge(A, A) = A
Associativity:  merge(merge(A, B), C) = merge(A, merge(B, C))
```

### How SHIMI Uses It

```
Agent A has node v_a: "Memory systems for AI"
Agent B has node v_b: "AI memory architectures"

Both modified the same node differently!

CRDT merge: μ(v_a, v_b) → picks one deterministically
Rule: "favor summary with greater abstraction depth or observed usage"
```

### Why It Matters
- No central server needed to resolve conflicts
- Eventual consistency guaranteed
- Order of sync doesn't matter

### Analogy
Like Google Docs - multiple people edit, changes merge without "which version wins?" dialogs.

---

## Relevance to Your System

### You're Using: Git

Git already provides:
| SHIMI Mechanism | Git Equivalent |
|-----------------|----------------|
| Merkle-DAG | Commit hashes, tree hashes |
| Bloom filters | Packfile negotiation |
| CRDTs | Manual merge (not automatic) |

### Key Difference

| SHIMI | Git |
|-------|-----|
| Automatic conflict resolution | Manual merge conflicts |
| Designed for many agents | Designed for human developers |
| Real-time sync | Pull/push when you want |

### Do You Need SHIMI's Mechanisms?

**Probably not, because:**

1. **Single agent** - You don't have multiple AI agents with separate memory trees
2. **Git works** - You already sync via Git across devices
3. **Conflicts are rare** - You control when changes happen
4. **Complexity cost** - Implementing Merkle-DAG + Bloom + CRDT is significant

### When You WOULD Need Them

- Multiple AI agents working in parallel on same memory
- Real-time collaboration without central server
- Massive scale where Git doesn't work

---

## Summary

| Mechanism | Purpose | Your Equivalent |
|-----------|---------|-----------------|
| Merkle-DAG | Detect divergence efficiently | Git commit hashes |
| Bloom filters | Identify missing nodes | Git packfile protocol |
| CRDTs | Conflict-free merge | Git merge (manual) |

**SHIMI's sync mechanisms solve multi-agent decentralized problems. You have single-agent with Git. These are interesting but not necessary for your use case.**

If you ever build a multi-agent system where agents have independent memory and need to sync, revisit these concepts.

---

## Sources

- [SHIMI Paper - arXiv:2504.06135](https://arxiv.org/abs/2504.06135)
