# Core Data Structure Hierarchy: From Hardware Primitives to Application Composites

## Purpose

This document presents the **10-level dependency hierarchy** of data structures used in AI agent memory systems — from hardware primitives (RAM, pointers) up to complete application-level memory stores. Unlike the flat listing in `18_underlying_data_structures.md`, this shows how each structure **builds upon** lower-level structures, revealing the full dependency chain.

Understanding this hierarchy is critical for memory system design: it shows which structures are foundational (must exist), which are optimization layers (can be added later), and how they compose into complete systems.

---

## 1. The 10-Level Hierarchy

### Visual Overview

```
Level 9: Application Composites
         (Episodic Store, Semantic Store, Procedural Store)
                            ^
Level 8: Flexible Storage
         (JSONB, GIN indexes)
                            ^
Level 7: Caching & Optimization
         (LRU Cache, LFU Cache, Bloom Filters)
                            ^
Level 6: Temporal Structures
         (Hypertables, Ring Buffers)
                            ^
Level 5: AI Memory Indexes
         (HNSW, IVFFlat, Inverted Indexes)
                            ^
Level 4: Core AI Memory Structures
         (Relational Tables, Vectors, Knowledge Graphs)
                            ^
Level 3: Sorted/Ordered Structures
         (Skip Lists, Sorted Arrays)
                            ^
Level 2: Hierarchical Structures
         (B-Trees, Heaps, Tries)
                            ^
Level 1: Fundamental Building Blocks
         (Arrays, Linked Lists, Hash Tables)
                            ^
Level 0: Hardware Primitives
         (Contiguous Memory, Pointers)
```

---

## 2. Level 0: Hardware Primitives

The absolute foundation — what everything else is built on.

### Contiguous Memory Arrays (RAM)
- Raw bytes in memory
- Foundation for literally everything
- O(1) random access by index

### Pointers / References
- Memory addresses linking data
- Enable all linked/dynamic structures
- Foundation for graphs, trees, linked lists

---

## 3. Level 1: Fundamental Building Blocks

Basic data structures that other structures use as components.

### Arrays (Fixed / Dynamic)
- Ordered collection in contiguous memory
- **Used by**: heaps, hash tables, vectors, ring buffers, bloom filters
- O(1) access, O(n) insert/delete

### Linked Lists (Singly / Doubly)
- Nodes connected via pointers
- **Used by**: LRU caches, skip lists, graph adjacency lists
- O(1) insert/delete at known position, O(n) search

### Hash Tables
- Array + hash function for O(1) lookups
- **Used by**: LRU caches, inverted indexes, entity lookups, key-value stores
- Foundation for key-value operations across all memory types

---

## 4. Level 2: Core Hierarchical Structures

Essential structures that organize data hierarchically for efficient search.

### B-Trees / B+ Trees
- Self-balancing sorted tree
- **Foundation of SQL databases** — used for all indexes
- **Used by**: PostgreSQL primary keys, sorted indexes, range queries
- O(log n) search/insert/delete
- **Why foundational**: Every relational table uses B-trees under the hood

### Heaps (Binary Heap, Min/Max Heap)
- Complete binary tree with heap property (parent >= children)
- **Used by**: priority queues, memory consolidation, importance ranking
- O(log n) insert/delete, O(1) get min/max
- **Why foundational**: Powers priority-based operations in all memory types

### Tries (Prefix Trees)
- Tree where paths represent strings
- **Used by**: entity lookup, autocomplete, set operations
- O(m) operations (m = string length, independent of dataset size)
- **Why foundational**: Optimal for prefix-based retrieval

---

## 5. Level 3: Sorted / Ordered Structures

Structures specifically for maintaining order.

### Skip Lists
- Probabilistic multi-level linked list
- **Used by**: Redis sorted sets, time-ordered memories
- O(log n) search/insert/delete
- **Alternative to B-trees** — simpler implementation, better for concurrency
- Used in Redis for timeline/ranking operations

### Sorted Arrays with Binary Search
- Array maintained in sorted order
- **Used by**: small static indexes, embedding clustering
- O(log n) search, O(n) insert

---

## 6. Level 4: Core AI Memory Structures

The primary structures for AI memory systems — built on Levels 1-3.

### Relational Tables (SQL)
- **Built on**: B-trees (indexes) + Heaps (table storage) + Hash tables (hash indexes)
- Stores structured data with ACID guarantees
- Foundation for semantic facts, user preferences, entity data
- **Why here**: Combines lower-level structures into a unified queryable system

### Vector Embeddings (Arrays of Floats)
- **Built on**: Arrays (the embeddings themselves)
- Fixed-length numerical representations encoding semantic meaning
- Typically 1536-4096 dimensional float arrays
- **Used by**: All memory types for semantic similarity search
- **Why here**: Raw vectors are just arrays, but critical for AI memory

### Knowledge Graphs (Adjacency Lists / Matrices)
- **Built on**: Linked lists (adjacency lists) or 2D arrays (matrices) or B-trees (SQL foreign keys)
- Nodes = entities, Edges = typed relationships
- **Used by**: Semantic memory for explicit entity relationships
- **Why here**: Represents relationships — fundamental to semantic memory

---

## 7. Level 5: Specialized AI Memory Indexes

Advanced indexing structures built on Level 4 for fast retrieval at scale.

### HNSW (Hierarchical Navigable Small World) Graphs
- **Built on**: Graphs + vectors
- Multi-layer proximity graph for fast vector similarity search
- Upper layers for coarse navigation, lower layers for precision
- O(log n) approximate nearest neighbor search
- **Key insight**: Vector databases are actually graphs — the "vectors" are node values; the index uses graph traversal to find neighbors

### IVFFlat (Inverted File Index)
- **Built on**: Hash tables (clustering) + arrays (posting lists)
- Clusters vectors into buckets using k-means, searches only relevant buckets
- Used by pgvector for approximate similarity search

### Inverted Indexes
- **Built on**: Hash tables (term dictionary) + arrays (posting lists)
- Maps terms -> document IDs (reverse of normal document -> terms)
- O(log n) + O(k) where k = result count
- **Used by**: Full-text search across episodic and semantic memory
- 40x speedup over full table scans

---

## 8. Level 6: Temporal / Time-Series Structures

Structures specifically for time-ordered data.

### Time-Series Tables (Hypertables)
- **Built on**: B-trees + relational tables + time-based partitioning
- Automatic chunking by time intervals
- Supports retention policies, continuous aggregates, compression for older data
- **Used by**: Episodic memory, temporal events, interaction timelines

### Ring Buffers (Circular Buffers)
- **Built on**: Arrays + modulo arithmetic
- Fixed-size buffer that overwrites oldest data when full
- O(1) all operations, constant space
- **Used by**: Working memory, recent interaction windows, sliding context

---

## 9. Level 7: Caching & Fast Access Layers

Structures for performance optimization — not storage, but speed.

### LRU Cache (Least Recently Used)
- **Built on**: Hash table + doubly linked list
- Evicts least recently accessed items
- O(1) access and eviction
- **Used by**: Keeping "hot" memories in fast storage

### LFU Cache (Least Frequently Used)
- **Built on**: Hash tables + heaps + frequency counters
- Evicts least frequently accessed items
- O(log n) operations
- **Used by**: Frequency-based memory retention

### Bloom Filters
- **Built on**: Bit arrays + hash functions
- Probabilistic membership testing — "Have I seen this before?"
- O(1) operations, ~10 bits per element
- Can have false positives but **never** false negatives
- **Used by**: Duplicate detection before expensive vector search (saves ~90% of DB queries), cache penetration prevention, SHIMI sync protocol

---

## 10. Level 8: Flexible / Semi-Structured Storage

Structures for varying schemas and nested data.

### JSONB / Document Stores
- **Built on**: B-trees (indexing JSON paths) + Binary JSON encoding
- Flexible schema for nested data — no migrations needed for new attributes
- **Used by**: Episode metadata, procedural trajectories, arbitrary properties

### GIN (Generalized Inverted Index)
- **Built on**: Inverted indexes + B-trees
- Indexes array/JSONB contents for containment queries
- **Used by**: Querying within JSON fields, array containment searches

---

## 11. Level 9: Application-Specific Composite Structures

High-level combinations that form complete memory systems.

### Episodic Memory Store
- **Built on**: Vector embeddings + Time-series tables + Inverted indexes + LRU cache
- Complete system for "what happened when"
- Supports: semantic similarity search, temporal range queries, keyword search

### Semantic Memory Store
- **Built on**: Knowledge graphs + Vector embeddings + Relational tables + Tries
- Complete system for facts and concepts
- Supports: graph traversal, similarity search, prefix lookup, structured queries

### Procedural Memory Store
- **Built on**: Vector embeddings + JSONB + Priority queues + Bloom filters
- Complete system for skills and trajectories
- Supports: task similarity matching, trajectory replay, success-weighted retrieval

---

## 12. Summary: The Dependency Flow

**Bottom -> Top flow:**

1. **Hardware** provides raw memory and pointers
2. **Fundamentals** (arrays, lists, hashes) organize that memory
3. **Hierarchical** (B-trees, heaps, tries) add efficient search/ordering
4. **Sorted structures** (skip lists) provide alternatives with different tradeoffs
5. **Core AI structures** (SQL tables, vectors, graphs) combine lower levels into memory-appropriate formats
6. **AI indexes** (HNSW, IVFFlat, inverted) make those core structures fast at scale
7. **Temporal structures** (hypertables, ring buffers) specialize for time-ordered data
8. **Caching** (LRU, bloom filters) adds performance layers
9. **Flexible storage** (JSONB) adds schema adaptability
10. **Application composites** combine everything into complete memory systems

**Key insight**: Each level depends on and builds upon the level below it. You can't have HNSW graphs without basic graphs. You can't have B-trees without arrays. Everything ultimately reduces to Level 0 primitives.

---

## 13. Quick Reference: When to Use What

| Structure | Memory Type | Use Case | Performance |
|-----------|-------------|----------|-------------|
| **Bloom Filter** | All (preprocessing) | "Already seen this?" before vector search | O(1), 10 bits/item |
| **Inverted Index** | Episodic, Semantic | Keyword search across memories | O(log n + k) |
| **Skip List** | Time-based, Episodic | Time-ordered retrieval (Redis) | O(log n) |
| **Trie** | Semantic | Entity prefix search, autocomplete | O(m), m=query length |
| **Ring Buffer** | Working memory | Sliding window of recent interactions | O(1), fixed size |
| **Priority Queue** | All (metadata) | Consolidation queue, importance ranking | O(log n) |
| **LRU Cache** | All (caching layer) | Recently-accessed memory in fast storage | O(1) |
| **JSONB** | Episodic, Procedural | Flexible episode metadata, nested structures | O(log n) on paths |

---

## Cross-References

- **Flat listing of individual structures**: `18_underlying_data_structures.md`
- **Vectors vs graphs deep comparison**: `15_vectors_graphs_and_neurology.md`
- **Memory types these structures implement**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers using these structures**: `23_core_ai_memory_systems.md`

---

## Sources

- Perplexity AI research conversation (Feb 2026) — synthesis of data structure and AI memory literature
- [8 Data Structures That Power Your Databases](https://blog.bytebytego.com/p/8-data-structures-that-power-your) — B-trees, skip lists, LSM trees
- [Building AI Agents with Persistent Memory (TigerData)](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach) — unified PostgreSQL approach, pgvector benchmarks
- [Efficient Cache Design with Bloom Filters](https://dev.to/leapcell/efficient-cache-design-with-bloom-filters-in-go-3j56) — bloom filter mechanics
- [Inverted Index (VeloDB)](https://www.velodb.io/glossary/inverted-index-1) — inverted index performance
- [LFU vs LRU (Redis)](https://redis.io/blog/lfu-vs-lru-how-to-choose-the-right-cache-eviction-policy/) — cache eviction strategies
- [Priority Queue Implementations (Heap)](https://www.linkedin.com/pulse/why-do-priority-queue-implementations-often-use-heap-islam-ashiq-p5g4c) — heap-based priority queues
- [Trie Data Structure (LinkedIn)](https://www.linkedin.com/pulse/trie-data-structure-unleashing-power-prefix-based-search-a-szcsc) — prefix trees
- [Mem^p: Procedural Memory in AI Agents (arXiv:2508.06433)](https://arxiv.org/html/2508.06433v2) — procedural memory structures
