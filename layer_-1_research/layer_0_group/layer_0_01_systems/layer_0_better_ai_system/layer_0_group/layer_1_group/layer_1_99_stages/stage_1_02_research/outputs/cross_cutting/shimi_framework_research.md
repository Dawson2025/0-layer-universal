# SHIMI Framework Research

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: SHIMI (Semantic Hierarchical Memory Index) for AI agents

---

## What Is SHIMI?

**Paper**: "Decentralizing AI Memory: SHIMI, a Semantic Hierarchical Memory Index for Scalable Agent Reasoning"
**Published**: April 8, 2025 (arXiv:2504.06135)
**Author**: Tooraj Helmi

SHIMI is a memory architecture that:
- Models knowledge as a **hierarchical tree of concepts**
- Retrieves based on **meaning**, not surface similarity
- Designed for **decentralized** multi-agent systems

---

## How It Works

### Architecture

```
Abstract Intent (top)
       ↓
   Concept Nodes
       ↓
   Sub-concepts
       ↓
Specific Entities (bottom)
```

Each node contains:
- Semantic summary `s(v)`
- List of children `C(v)`
- Set of entities `Ev`
- Parent pointer

### Retrieval

**Top-down traversal**: Start from abstract intent, descend through hierarchy to specific entities.

This is different from vector search which:
- Embeds everything flat
- Finds nearest neighbors by similarity
- Loses hierarchical/conceptual relationships

### Decentralized Sync

SHIMI supports distributed agents with:
- **Merkle-DAG summaries** - Efficient diff detection
- **Bloom filters** - Fast membership testing
- **CRDT-style conflict resolution** - Eventual consistency

Agents maintain local memory trees and sync asynchronously.

---

## Why It Matters (vs RAG/Vector)

| Problem with RAG | How SHIMI Solves |
|------------------|------------------|
| Poor abstraction | Hierarchical concept organization |
| Scalability limits | Decentralized, partial sync |
| Semantic imprecision | Meaning-based traversal, not embedding similarity |
| Flat retrieval | Top-down from intent to entities |

---

## Comparison to Your System

| Aspect | SHIMI | Your System |
|--------|-------|-------------|
| **Structure** | Semantic hierarchy tree | Layer-stage hierarchy |
| **Organization** | Concepts → Sub-concepts → Entities | Layers → Stages → Outputs |
| **Retrieval** | Top-down semantic traversal | Explicit file reading |
| **Distribution** | Decentralized multi-agent | Single agent, git-synced |
| **Complexity** | Requires infrastructure | Simple files |
| **Tool-agnostic** | Framework-specific | Works with any tool |

### Similarities

1. **Both are hierarchical** - Not flat like vector stores
2. **Both organize by meaning** - Conceptual grouping
3. **Both support sync** - SHIMI uses CRDT, you use Git

### Differences

1. **SHIMI is automated** - Algorithm decides traversal
2. **Your system is explicit** - You decide what to read
3. **SHIMI needs infrastructure** - Merkle-DAG, Bloom filters
4. **Your system is simple** - Markdown + Git

---

## Should You Use SHIMI?

### Reasons to Consider

- If you need **multi-agent coordination** with shared memory
- If you have **massive amounts** of memory (beyond file browsing)
- If you want **automated semantic retrieval** instead of manual

### Reasons to Stick with Your Approach

- **Simpler** - No infrastructure needed
- **Tool-agnostic** - SHIMI would lock you to its implementation
- **Explicit control** - You know exactly what's loaded
- **Good enough** - Your hierarchy already provides conceptual organization

### Potential Hybrid

You could adopt SHIMI's **concepts** without the framework:
- Keep your layer-stage hierarchy
- Add semantic summaries to each level (like SHIMI nodes)
- Use explicit traversal (not automated)
- Sync via Git (not Merkle-DAG)

This gives you hierarchical semantic organization without the complexity.

---

## Key Insight

SHIMI validates your hierarchical approach. The research community is moving **away from flat vector stores** toward **hierarchical semantic organization**.

Your system already does this with:
- Layers (abstraction levels)
- Stages (workflow phases)
- Sub-layers (content types)

You're aligned with cutting-edge research, just implemented simply.

---

---

## SHIMI's Retrieval Mechanism (Technical Details)

### Does It Need LLM for Retrieval?

**Yes, but optimized.** SHIMI uses LLM-based semantic comparison, NOT pure embeddings.

### How It Works

```
Query arrives
    ↓
At each node: sim(query, node_summary) ≥ threshold?
    ↓
Yes → expand this branch
No → prune (don't descend)
    ↓
Repeat until leaves reached
```

### The `GetRelation()` Function

LLM-based function returns:
- `1` = ancestor relationship
- `0` = semantic equivalence
- `-1` = unrelated concepts

### Why They Claim It's Efficient

1. **Short summaries**: ~20 words per node (~26 tokens)
2. **Fast LLM calls**: "under 3 milliseconds" per comparison (GPT-4 Turbo)
3. **Hierarchical pruning**: Don't check everything, just the path down

### Comparison to Pure Embeddings

| Approach | LLM Calls | Accuracy | Speed |
|----------|-----------|----------|-------|
| Flat vector search | 0 (pre-computed) | Lower | Fastest |
| SHIMI | O(depth × branching) | Higher | Fast enough |
| Full LLM retrieval | O(n) for all docs | Highest | Slowest |

SHIMI is a middle ground: uses LLM for semantic precision, but hierarchy limits how many calls are needed.

---

## Sources

- [SHIMI Paper - arXiv:2504.06135](https://arxiv.org/abs/2504.06135)
- [SHIMI HTML Version](https://arxiv.org/html/2504.06135v1)
- [Literature Review - Moonlight](https://www.themoonlight.io/en/review/decentralizing-ai-memory-shimi-a-semantic-hierarchical-memory-index-for-scalable-agent-reasoning)
