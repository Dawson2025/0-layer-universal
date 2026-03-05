---
resource_id: "4096ea5c-332e-400c-af2e-2915a18d36d7"
resource_type: "output"
resource_name: "22_core_data_structure_hierarchy"
---
# Core Data Structure Hierarchy: From Hardware Primitives to Application Composites

<!-- section_id: "6370648e-d81c-4e02-8ffd-bc79f47031d0" -->
## Purpose

This document presents the **10-level dependency hierarchy** of data structures used in AI agent memory systems — from hardware primitives (RAM, pointers) up to complete application-level memory stores. Unlike the flat listing in `18_underlying_data_structures.md`, this shows how each structure **builds upon** lower-level structures, revealing the full dependency chain.

Understanding this hierarchy is critical for memory system design: it shows which structures are foundational (must exist), which are optimization layers (can be added later), and how they compose into complete systems.

---

<!-- section_id: "81549048-8372-495c-a4c7-46637f835b73" -->
## 1. The 10-Level Hierarchy

<!-- section_id: "a0b672bd-27d4-4342-bdb8-056f5803e515" -->
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

<!-- section_id: "e8ff4a9a-3c51-4613-a193-c3b9f888a011" -->
## 2. Level 0: Hardware Primitives

The absolute foundation — what everything else is built on.

<!-- section_id: "09361b5a-6218-41aa-984e-6dd5719c47ba" -->
### Contiguous Memory Arrays (RAM)
- Raw bytes in memory
- Foundation for literally everything
- O(1) random access by index

<!-- section_id: "d34b812e-6490-47a3-adc3-bf3cc4c96562" -->
### Pointers / References
- Memory addresses linking data
- Enable all linked/dynamic structures
- Foundation for graphs, trees, linked lists

---

<!-- section_id: "e0c1c167-4afc-4218-8e51-a0420a4f0e16" -->
## 3. Level 1: Fundamental Building Blocks

Basic data structures that other structures use as components.

<!-- section_id: "d2e479e0-387c-4e1a-82f4-bbd7d3bb31f9" -->
### Arrays (Fixed / Dynamic)
- Ordered collection in contiguous memory
- **Used by**: heaps, hash tables, vectors, ring buffers, bloom filters
- O(1) access, O(n) insert/delete

<!-- section_id: "6771a54d-174d-4edd-8538-335c7cc6603d" -->
### Linked Lists (Singly / Doubly)
- Nodes connected via pointers
- **Used by**: LRU caches, skip lists, graph adjacency lists
- O(1) insert/delete at known position, O(n) search

<!-- section_id: "8f7ae2fa-056d-4366-9d97-acaf02f833fe" -->
### Hash Tables
- Array + hash function for O(1) lookups
- **Used by**: LRU caches, inverted indexes, entity lookups, key-value stores
- Foundation for key-value operations across all memory types

---

<!-- section_id: "b9d12447-8fa0-44bf-9b03-f783e285d265" -->
## 4. Level 2: Core Hierarchical Structures

Essential structures that organize data hierarchically for efficient search.

<!-- section_id: "4670de0a-3f6a-4a9d-a6b6-0c38ce11b63a" -->
### B-Trees / B+ Trees
- Self-balancing sorted tree
- **Foundation of SQL databases** — used for all indexes
- **Used by**: PostgreSQL primary keys, sorted indexes, range queries
- O(log n) search/insert/delete
- **Why foundational**: Every relational table uses B-trees under the hood

<!-- section_id: "056dcad2-72ef-4bb1-b1be-a1bd3134054f" -->
### Heaps (Binary Heap, Min/Max Heap)
- Complete binary tree with heap property (parent >= children)
- **Used by**: priority queues, memory consolidation, importance ranking
- O(log n) insert/delete, O(1) get min/max
- **Why foundational**: Powers priority-based operations in all memory types

<!-- section_id: "04077fd8-a80d-4ed8-8c98-e8a4e3087916" -->
### Tries (Prefix Trees)
- Tree where paths represent strings
- **Used by**: entity lookup, autocomplete, set operations
- O(m) operations (m = string length, independent of dataset size)
- **Why foundational**: Optimal for prefix-based retrieval

---

<!-- section_id: "2eaca4df-b797-4a2c-a486-482c7219dee4" -->
## 5. Level 3: Sorted / Ordered Structures

Structures specifically for maintaining order.

<!-- section_id: "fd0ced4d-04eb-4a81-bc80-fd1b66fd888b" -->
### Skip Lists
- Probabilistic multi-level linked list
- **Used by**: Redis sorted sets, time-ordered memories
- O(log n) search/insert/delete
- **Alternative to B-trees** — simpler implementation, better for concurrency
- Used in Redis for timeline/ranking operations

<!-- section_id: "a49017dc-3fd3-40b7-a776-cebea8302c4c" -->
### Sorted Arrays with Binary Search
- Array maintained in sorted order
- **Used by**: small static indexes, embedding clustering
- O(log n) search, O(n) insert

---

<!-- section_id: "0e8cd852-b94e-4b63-93d5-59dc4b3c226c" -->
## 6. Level 4: Core AI Memory Structures

The primary structures for AI memory systems — built on Levels 1-3.

<!-- section_id: "d544bc66-eb95-418f-bfbc-3df5699043d9" -->
### Relational Tables (SQL)
- **Built on**: B-trees (indexes) + Heaps (table storage) + Hash tables (hash indexes)
- Stores structured data with ACID guarantees
- Foundation for semantic facts, user preferences, entity data
- **Why here**: Combines lower-level structures into a unified queryable system

<!-- section_id: "a03387a6-18f1-4713-8851-efde7c542cd2" -->
### Vector Embeddings (Arrays of Floats)
- **Built on**: Arrays (the embeddings themselves)
- Fixed-length numerical representations encoding semantic meaning
- Typically 1536-4096 dimensional float arrays
- **Used by**: All memory types for semantic similarity search
- **Why here**: Raw vectors are just arrays, but critical for AI memory

<!-- section_id: "5ff195ae-d817-4884-acee-5a9217c940c5" -->
### Knowledge Graphs (Adjacency Lists / Matrices)
- **Built on**: Linked lists (adjacency lists) or 2D arrays (matrices) or B-trees (SQL foreign keys)
- Nodes = entities, Edges = typed relationships
- **Used by**: Semantic memory for explicit entity relationships
- **Why here**: Represents relationships — fundamental to semantic memory

---

<!-- section_id: "4c46e871-429d-43b4-b0fa-eddad901de51" -->
## 7. Level 5: Specialized AI Memory Indexes

Advanced indexing structures built on Level 4 for fast retrieval at scale.

<!-- section_id: "550421d0-ac8d-46ad-8c13-b660e74d125e" -->
### HNSW (Hierarchical Navigable Small World) Graphs
- **Built on**: Graphs + vectors
- Multi-layer proximity graph for fast vector similarity search
- Upper layers for coarse navigation, lower layers for precision
- O(log n) approximate nearest neighbor search
- **Key insight**: Vector databases are actually graphs — the "vectors" are node values; the index uses graph traversal to find neighbors

<!-- section_id: "db289e71-e479-4d27-ab98-aa933cb2fc39" -->
### IVFFlat (Inverted File Index)
- **Built on**: Hash tables (clustering) + arrays (posting lists)
- Clusters vectors into buckets using k-means, searches only relevant buckets
- Used by pgvector for approximate similarity search

<!-- section_id: "434e33d3-ed9c-4dee-83df-977bebca8f78" -->
### Inverted Indexes
- **Built on**: Hash tables (term dictionary) + arrays (posting lists)
- Maps terms -> document IDs (reverse of normal document -> terms)
- O(log n) + O(k) where k = result count
- **Used by**: Full-text search across episodic and semantic memory
- 40x speedup over full table scans

---

<!-- section_id: "1595a932-4556-4ba9-9617-14272ac51b9c" -->
## 8. Level 6: Temporal / Time-Series Structures

Structures specifically for time-ordered data.

<!-- section_id: "32952e28-d9b5-4eef-ade7-3debca8afd27" -->
### Time-Series Tables (Hypertables)
- **Built on**: B-trees + relational tables + time-based partitioning
- Automatic chunking by time intervals
- Supports retention policies, continuous aggregates, compression for older data
- **Used by**: Episodic memory, temporal events, interaction timelines

<!-- section_id: "0feda6a8-3a20-432c-9aa0-48f3aac28f3f" -->
### Ring Buffers (Circular Buffers)
- **Built on**: Arrays + modulo arithmetic
- Fixed-size buffer that overwrites oldest data when full
- O(1) all operations, constant space
- **Used by**: Working memory, recent interaction windows, sliding context

---

<!-- section_id: "6e7440f3-105a-4e53-ae6c-f78dfbbec081" -->
## 9. Level 7: Caching & Fast Access Layers

Structures for performance optimization — not storage, but speed.

<!-- section_id: "41fcccd1-685d-405e-9595-f0048e305931" -->
### LRU Cache (Least Recently Used)
- **Built on**: Hash table + doubly linked list
- Evicts least recently accessed items
- O(1) access and eviction
- **Used by**: Keeping "hot" memories in fast storage

<!-- section_id: "58df73b9-6fd1-474f-91b4-72c99683b502" -->
### LFU Cache (Least Frequently Used)
- **Built on**: Hash tables + heaps + frequency counters
- Evicts least frequently accessed items
- O(log n) operations
- **Used by**: Frequency-based memory retention

<!-- section_id: "ab5b4a12-77e4-4ee0-910c-3cc86cbc017a" -->
### Bloom Filters
- **Built on**: Bit arrays + hash functions
- Probabilistic membership testing — "Have I seen this before?"
- O(1) operations, ~10 bits per element
- Can have false positives but **never** false negatives
- **Used by**: Duplicate detection before expensive vector search (saves ~90% of DB queries), cache penetration prevention, SHIMI sync protocol

---

<!-- section_id: "8a3ec430-8888-4ce0-8e51-0868c0883a41" -->
## 10. Level 8: Flexible / Semi-Structured Storage

Structures for varying schemas and nested data.

<!-- section_id: "4ccb0173-99e7-4dc6-a4be-4aabc6f700ed" -->
### JSONB / Document Stores
- **Built on**: B-trees (indexing JSON paths) + Binary JSON encoding
- Flexible schema for nested data — no migrations needed for new attributes
- **Used by**: Episode metadata, procedural trajectories, arbitrary properties

<!-- section_id: "20593bc2-d51f-4f5e-a755-ca0a6c7214e6" -->
### GIN (Generalized Inverted Index)
- **Built on**: Inverted indexes + B-trees
- Indexes array/JSONB contents for containment queries
- **Used by**: Querying within JSON fields, array containment searches

---

<!-- section_id: "d71b37ad-c2e0-4bb8-836d-13cb84e581d4" -->
## 11. Level 9: Application-Specific Composite Structures

High-level combinations that form complete memory systems.

<!-- section_id: "9d4c47dc-5e75-49e6-a1a9-5331ba7b9e60" -->
### Episodic Memory Store
- **Built on**: Vector embeddings + Time-series tables + Inverted indexes + LRU cache
- Complete system for "what happened when"
- Supports: semantic similarity search, temporal range queries, keyword search

<!-- section_id: "9b4f4c94-8240-455c-86c0-42abd8ffc347" -->
### Semantic Memory Store
- **Built on**: Knowledge graphs + Vector embeddings + Relational tables + Tries
- Complete system for facts and concepts
- Supports: graph traversal, similarity search, prefix lookup, structured queries

<!-- section_id: "0e84b8d8-040d-4945-9dcf-d87384efc873" -->
### Procedural Memory Store
- **Built on**: Vector embeddings + JSONB + Priority queues + Bloom filters
- Complete system for skills and trajectories
- Supports: task similarity matching, trajectory replay, success-weighted retrieval

---

<!-- section_id: "77429a69-8eb4-4ba3-b56f-0d83714b0fb9" -->
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

<!-- section_id: "8bc384e9-be82-4bf4-a49d-d36cb79207a8" -->
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

<!-- section_id: "ea694734-df19-4a6d-8b21-69167bd10d94" -->
## Cross-References

- **Flat listing of individual structures**: `18_underlying_data_structures.md`
- **Vectors vs graphs deep comparison**: `15_vectors_graphs_and_neurology.md`
- **Memory types these structures implement**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers using these structures**: `23_core_ai_memory_systems.md`

---

<!-- section_id: "7e2f406b-1a3c-4f1f-a1b3-59c25f8513bc" -->
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
