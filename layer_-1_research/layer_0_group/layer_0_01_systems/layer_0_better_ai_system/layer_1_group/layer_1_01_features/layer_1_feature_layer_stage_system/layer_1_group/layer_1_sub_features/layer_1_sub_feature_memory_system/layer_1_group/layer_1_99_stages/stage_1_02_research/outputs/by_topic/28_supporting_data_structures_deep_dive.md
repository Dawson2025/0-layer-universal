---
resource_id: "c1d2ae3a-6a61-49da-bb2a-f1c634f20f6f"
resource_type: "output"
resource_name: "28_supporting_data_structures_deep_dive"
---
# Supporting Data Structures Deep Dive

## Purpose

This document provides a comprehensive analysis of the **supporting (optimization) data structures** used in AI agent memory systems. While the core three structures (vector databases, relational tables, knowledge graphs) form the foundation (see `22_core_data_structure_hierarchy.md`), production systems layer these additional structures on top for performance, caching, deduplication, and specialized indexing. Each structure is presented with time/space complexity, concrete Python code, and specific AI memory use cases.

---

## 1. Bloom Filters

### What It Is

A **probabilistic data structure** for fast membership testing. It answers the question: "Have I seen this before?" Uses a fixed-size bit array with multiple hash functions that map inputs to bit positions.

### How It Works

- A bit array of fixed size (e.g., 1 million bits) starts with all zeros
- Multiple hash functions (typically 3-7) map each input to bit positions
- **Insert**: Set all hashed bit positions to 1
- **Query**: Check if all hashed bit positions are 1

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(k) where k = number of hash functions | ~10 bits per element |
| Lookup | O(k) effectively O(1) | Fixed allocation |
| Delete | Not supported (standard) | N/A |

### Key Properties

- **No false negatives**: If the filter says "not present," the item is definitively absent
- **False positives possible**: If the filter says "maybe present," verification is needed
- **Space efficient**: ~10 bits per element vs hundreds of bytes for storing actual data
- **Cannot delete**: Standard bloom filters do not support removal (counting bloom filters can)

### AI Memory Use Case: Duplicate Memory Detection

Before running an expensive vector similarity search, check the bloom filter first. This can eliminate ~90% of unnecessary database queries.

```python
# Before expensive vector search, check bloom filter
if not bloom_filter.might_contain(query_hash):
    return "Definitely not in memory"  # Skip database query entirely
else:
    return expensive_vector_search(query)  # Maybe exists, verify in DB
```

### Other AI Memory Applications

- **Cache penetration prevention**: Filter out queries for data that definitely does not exist
- **Deduplication**: Prevent storing duplicate episodes or facts
- **Web crawl memory**: Avoid re-visiting URLs during knowledge gathering

---

## 2. Inverted Indexes

### What It Is

A data structure that maps **terms to document IDs** (the reverse of the normal document-to-terms mapping). The backbone of full-text search engines like Elasticsearch and PostgreSQL GIN indexes.

### How It Works

- A **term dictionary** (hash table or B-tree) maps each unique term to a **posting list**
- Each posting list is an array of document IDs where the term appears
- Queries intersect posting lists to find documents matching all terms

```
Term Dictionary:
"meeting" -> [doc_5, doc_12, doc_89]   # Posting list
"urgent"  -> [doc_12, doc_45]
"budget"  -> [doc_5, doc_78]

Query: "urgent meeting"
-> Intersect [12, 45] ^ [5, 12, 89] = [doc_12]
-> Return doc_12
```

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Dictionary lookup | O(log n) via B-tree or O(1) via hash | Proportional to vocabulary size |
| Result retrieval | O(k) where k = number of matches | Posting lists grow with corpus |
| Full query | O(log n + k) | N/A |

### Performance Impact

- **40x speedup** over full table scans for keyword queries
- Highly efficient for Boolean queries (AND, OR, NOT)

### AI Memory Use Case: Semantic Memory Text Search

Fast keyword search across episodic memories, combined with vector similarity for hybrid retrieval.

```python
# Hybrid search: inverted index for keywords + vectors for semantics
keyword_results = inverted_index.search("budget meeting")  # Fast text match
vector_results = vector_db.similarity_search(query_embedding, k=20)  # Semantic

# Combine results with weighted scoring
combined = merge_results(keyword_results, vector_results, weights=[0.3, 0.7])
```

### Other AI Memory Applications

- **Tag/entity lookup**: Find all memories tagged with specific entities
- **Faceted search**: Filter memories by metadata fields (date, agent, category)
- **BM25 scoring**: Rank text relevance alongside vector similarity

---

## 3. Skip Lists

### What It Is

A **probabilistic alternative to balanced B-trees** for maintaining sorted data. Uses multiple levels of linked lists where upper levels act as "express lanes" that skip over elements for faster traversal.

### How It Works

- **Bottom level**: A sorted linked list of all elements
- **Upper levels**: Each element is promoted with probability p (typically 0.5)
- Search starts at the top level, moves right until overshooting, then drops down one level
- Resembles a multi-lane highway with express and local lanes

### Complexity

| Operation | Time (expected) | Space |
|-----------|----------------|-------|
| Search | O(log n) | O(n) expected |
| Insert | O(log n) | O(log n) levels per element |
| Delete | O(log n) | N/A |

### Key Properties

- Simpler to implement than self-balancing trees (AVL, red-black)
- Naturally supports concurrent access (used in Redis sorted sets)
- Probabilistic balancing rather than deterministic rotations
- Excellent for range queries

### AI Memory Use Case: Time-Ordered Memory (Redis Sorted Sets)

Redis sorted sets are implemented as skip lists internally, making them ideal for time-ordered episode retrieval.

```python
import redis

r = redis.Redis()

# Store memories with timestamps as scores
r.zadd("agent:memory:timeline", {
    "episode_001": 1708300000,  # Unix timestamp
    "episode_002": 1708300300,
    "episode_003": 1708300600,
})

# Range query: all memories from last hour
now = 1708300600
one_hour_ago = now - 3600
recent = r.zrangebyscore("agent:memory:timeline", one_hour_ago, now)

# Get top-N most recent
latest = r.zrevrange("agent:memory:timeline", 0, 4)  # Last 5 memories
```

### Other AI Memory Applications

- **Memory importance scoring**: Maintain sorted list of memories by importance/recency score
- **Range queries**: "Find all memories from last week" or "memories with score > 0.8"
- **Leaderboard-style ranking**: Track most-accessed memories for cache warming

---

## 4. Tries (Prefix Trees)

### What It Is

A tree data structure where each node represents a character (or token). Paths from root to leaves spell out complete strings. Common prefixes share nodes, making it extremely efficient for prefix-based operations.

### How It Works

```
        root
       /  |  \
      c   d   b
     /|   |    \
    a  n  o     u
    |     |     |
    t     g     d
    |           |
    s           g
         (words: cats, can, dog, budg...)
```

- Each edge represents a character
- Nodes may be marked as "end of word"
- All strings with a common prefix share the same path from root

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Search | O(m) where m = query length | O(ALPHABET * n * m) worst case |
| Insert | O(m) | Same |
| Prefix search | O(m + k) where k = results | Same |

**Key property**: Search time depends only on query length, NOT on the number of stored items.

### AI Memory Use Case: Entity Prefix Search and Autocomplete

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.memories = []  # Memories associated with this entity

class EntityTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, entity_name, memory_id):
        node = self.root
        for char in entity_name.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.memories.append(memory_id)

    def prefix_search(self, prefix):
        """Find all entities starting with prefix"""
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_all(node)

    def _collect_all(self, node):
        results = list(node.memories)
        for child in node.children.values():
            results.extend(self._collect_all(child))
        return results

# Usage
trie = EntityTrie()
trie.insert("John Smith", "mem_001")
trie.insert("John Doe", "mem_002")
trie.insert("Jane Doe", "mem_003")

trie.prefix_search("John")  # Returns ["mem_001", "mem_002"]
```

### Other AI Memory Applications

- **Command completion**: Agent suggests commands or actions based on typed prefix
- **Set-trie variant**: Stores entire sets efficiently for dependency checking across memory items

---

## 5. Ring Buffers (Circular Buffers)

### What It Is

A **fixed-size array** with read and write pointers that wrap around when reaching the end. When full, new items overwrite the oldest data automatically. The fundamental data structure for sliding-window memory.

### How It Works

- Fixed-size array allocated at initialization
- Write pointer advances with each insertion, wrapping to position 0 after the last slot
- When full, the oldest item is silently overwritten
- No memory allocation after initialization

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push (write) | O(1) | Fixed at initialization |
| Read (by index) | O(1) | Fixed |
| Eviction | Automatic (O(0)) | No extra space |

### Key Properties

- **Constant memory**: Never grows beyond the fixed size
- **Cache-friendly**: Contiguous memory layout, excellent CPU cache behavior
- **Automatic eviction**: Old data naturally drops off without explicit garbage collection
- **Zero allocation overhead**: No malloc/free after initialization

### AI Memory Use Case: Working Memory Sliding Window

```python
class WorkingMemoryBuffer:
    """Ring buffer for maintaining the last N interactions in working memory."""

    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.head = 0      # Oldest item position
        self.tail = 0      # Next write position
        self.size = 0

    def push(self, interaction):
        """Add a new interaction, evicting oldest if full."""
        self.buffer[self.tail] = interaction
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity  # Oldest moves forward

    def get_recent(self, n=None):
        """Get the N most recent interactions."""
        count = min(n or self.size, self.size)
        result = []
        for i in range(count):
            idx = (self.tail - 1 - i) % self.capacity
            result.append(self.buffer[idx])
        return list(reversed(result))

    def __len__(self):
        return self.size

# Usage
working_memory = WorkingMemoryBuffer(capacity=10)

# Simulate conversation turns
for i in range(15):
    working_memory.push({"turn": i, "content": f"Message {i}"})

# Only last 10 are retained
recent = working_memory.get_recent(5)
# [{"turn": 10, ...}, {"turn": 11, ...}, ..., {"turn": 14, ...}]
print(len(working_memory))  # 10 (never exceeds capacity)
```

### Other AI Memory Applications

- **Recent events buffer**: Keep a sliding window of recent episodes before consolidation
- **Sensor data streams**: Store last N readings for pattern detection in embodied agents
- **Token context window**: Manage the most recent tokens within a fixed context budget

---

## 6. Priority Queues / Heaps

### What It Is

A **binary heap** (complete binary tree) that maintains a priority ordering. Max-heaps keep the highest-priority element at the root; min-heaps keep the lowest. Typically implemented as an array for cache efficiency.

### How It Works

- **Binary heap property**: Parent >= children (max-heap) or Parent <= children (min-heap)
- **Insert**: Add at the bottom, "bubble up" to restore heap property
- **Extract**: Remove root, move last element to root, "bubble down"
- **Array representation**: For node at index i, children are at 2i+1 and 2i+2

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(log n) | O(n) total |
| Extract min/max | O(log n) | N/A |
| Peek min/max | O(1) | N/A |
| Build heap | O(n) | N/A |

### AI Memory Use Case: Memory Consolidation Queue

```python
import heapq

class MemoryConsolidationQueue:
    """Priority queue for processing memories by importance during consolidation."""

    def __init__(self):
        self.heap = []
        self.counter = 0  # Tie-breaker for equal priorities

    def add_memory(self, memory, importance):
        """Add memory with importance score (higher = more important)."""
        # Use negative importance for max-heap behavior with Python's min-heap
        heapq.heappush(self.heap, (-importance, self.counter, memory))
        self.counter += 1

    def get_next(self):
        """Get the most important memory for consolidation."""
        if self.heap:
            neg_importance, _, memory = heapq.heappop(self.heap)
            return memory, -neg_importance
        return None, None

    def peek_importance(self):
        """Check the importance of the next memory without removing it."""
        if self.heap:
            return -self.heap[0][0]
        return None

# Usage
queue = MemoryConsolidationQueue()
queue.add_memory({"content": "User's name is Alice"}, importance=0.95)
queue.add_memory({"content": "Weather was sunny"}, importance=0.30)
queue.add_memory({"content": "User is allergic to peanuts"}, importance=0.90)
queue.add_memory({"content": "Mentioned liking jazz"}, importance=0.60)

# Process in importance order
while queue.heap:
    memory, score = queue.get_next()
    print(f"Consolidating (importance={score}): {memory['content']}")
# Output:
# Consolidating (importance=0.95): User's name is Alice
# Consolidating (importance=0.9): User is allergic to peanuts
# Consolidating (importance=0.6): Mentioned liking jazz
# Consolidating (importance=0.3): Weather was sunny
```

### Other AI Memory Applications

- **Retrieval ranking**: Sort candidate memories by combined relevance score
- **Eviction candidates**: Maintain a min-heap of low-importance memories for deletion under memory pressure
- **Attention mechanisms**: Prioritize which memories to load into a limited context window

---

## 7. LRU/LFU Caches

### What It Is

**Intelligent eviction caches** that decide which items to remove when the cache is full. LRU (Least Recently Used) evicts the item not accessed for the longest time. LFU (Least Frequently Used) evicts the item accessed the fewest total times.

### How They Work

**LRU (Least Recently Used):**
- **Structure**: Hash map + doubly linked list
- Hash map provides O(1) lookup by key
- Doubly linked list maintains access order (most recent at head)
- On access: move item to head of list
- On eviction: remove item from tail of list

**LFU (Least Frequently Used):**
- **Structure**: Hash map + frequency counter + min-heap (or frequency buckets)
- Tracks how many times each item has been accessed
- Evicts the item with the lowest access frequency

### Complexity

| Operation | LRU Time | LFU Time | Space |
|-----------|----------|----------|-------|
| Get | O(1) | O(1) with bucket optimization | O(n) |
| Put | O(1) | O(log n) or O(1) with buckets | O(n) |
| Evict | O(1) | O(1) with min-freq pointer | N/A |

### AI Memory Use Case: Hot Memory Management

```python
from collections import OrderedDict

class MemoryLRUCache:
    """LRU cache for keeping frequently accessed memories in fast storage."""

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.hits = 0
        self.misses = 0

    def get(self, memory_id):
        """Retrieve memory, promoting it to most-recently-used."""
        if memory_id in self.cache:
            self.cache.move_to_end(memory_id)
            self.hits += 1
            return self.cache[memory_id]
        self.misses += 1
        return None

    def put(self, memory_id, memory_data):
        """Store memory, evicting least-recently-used if at capacity."""
        if memory_id in self.cache:
            self.cache.move_to_end(memory_id)
        else:
            if len(self.cache) >= self.capacity:
                evicted_id, _ = self.cache.popitem(last=False)
                self._move_to_cold_storage(evicted_id)
        self.cache[memory_id] = memory_data

    def _move_to_cold_storage(self, memory_id):
        """Evicted memories go to disk/database, not deleted."""
        pass  # Write to persistent store

    @property
    def hit_rate(self):
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0

# Usage
hot_memory = MemoryLRUCache(capacity=100)
hot_memory.put("mem_001", {"content": "User prefers dark mode"})
hot_memory.put("mem_002", {"content": "Last project: ML pipeline"})

result = hot_memory.get("mem_001")  # Promotes to most-recently-used
```

### Adaptive Caching with Reinforcement Learning

Modern systems go beyond fixed LRU/LFU policies. **Reinforcement learning** can learn optimal eviction policies that adapt to workload patterns, outperforming both LRU and LFU by learning which memories are likely to be accessed in the near future based on contextual signals.

### Other AI Memory Applications

- **Context window optimization**: Keep the most relevant memories in fast RAM storage
- **Working memory**: Maintain "hot" memories in-process, cold memories on disk
- **Multi-tier caching**: L1 (in-process LRU) -> L2 (Redis) -> L3 (persistent DB)

---

## 8. JSONB / Document Stores (GIN Indexes)

### What It Is

**Binary JSON** stored in a database column (typically PostgreSQL JSONB) with specialized indexing. Combines the flexibility of schema-free documents with the query power of relational databases. GIN (Generalized Inverted Index) enables efficient containment and existence queries on JSON paths.

### How It Works

- JSONB stores JSON in a decomposed binary format (not plain text)
- B-tree indexes on specific JSON paths for equality/range queries
- GIN indexes for containment queries (`@>`) and key existence (`?`)
- Supports indexing nested objects and arrays

### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Path lookup (B-tree indexed) | O(log n) | Index proportional to data |
| Containment query (GIN) | O(log n + k) | GIN index ~2-3x data size |
| Full document read | O(1) by primary key | Document size |
| Schema change | O(0) - no migration needed | N/A |

### AI Memory Use Case: Flexible Metadata Storage

```sql
-- Store memories with arbitrary metadata (no schema migrations needed)
CREATE TABLE agent_memories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    metadata JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- GIN index for fast metadata queries
CREATE INDEX idx_memories_metadata ON agent_memories USING GIN (metadata);

-- Store memory with rich metadata
INSERT INTO agent_memories (content, metadata) VALUES (
    'User prefers morning meetings',
    '{"importance": 0.8, "source": "conversation", "entities": ["user_123"],
      "tags": ["preference", "scheduling"], "confidence": 0.92}'
);

-- Query by metadata containment
SELECT content FROM agent_memories
WHERE metadata @> '{"tags": ["preference"]}';

-- Query by nested path
SELECT content FROM agent_memories
WHERE (metadata->>'importance')::float > 0.7;
```

### Other AI Memory Applications

- **Nested structures**: Store hierarchical memories (episodes with sub-events) without table joins
- **Dynamic properties**: Add new memory attributes (emotion scores, decay rates) without migrations
- **Multi-modal metadata**: Store image dimensions, audio duration, text stats alongside embeddings
- **Agent state snapshots**: Serialize complex agent state as JSONB for checkpointing

---

## 9. Comparison Table

| Structure | Time Complexity | Space | Best For | Memory Type |
|-----------|----------------|-------|----------|-------------|
| **Bloom Filter** | O(1) lookup | ~10 bits/item | "Already seen?" pre-check before vector search | All types (preprocessing) |
| **Inverted Index** | O(log n + k) | Proportional to vocabulary | Keyword search across memory corpus | Episodic, Semantic |
| **Skip List** | O(log n) search/insert/delete | O(n) | Time-ordered retrieval, sorted scoring | Time-based, Episodic |
| **Trie** | O(m) where m = query length | O(ALPHABET * n * m) | Entity prefix search, autocomplete | Semantic |
| **Ring Buffer** | O(1) push/read, fixed size | Fixed at init | Sliding window of recent interactions | Working Memory |
| **Priority Queue** | O(log n) insert/extract, O(1) peek | O(n) | Consolidation queue, importance ranking | All types (metadata) |
| **LRU Cache** | O(1) get/put/evict | O(n) capacity-bounded | Hot memory management, recently-accessed | All types (caching layer) |
| **LFU Cache** | O(1) with bucket optimization | O(n) capacity-bounded | Frequently-accessed memory, stable hot set | All types (caching layer) |
| **JSONB/GIN** | O(log n) on indexed paths | Index ~2-3x data | Flexible metadata, nested structures | Episodic, Procedural |

---

## 10. How Supporting Structures Layer on Core Structures

These supporting structures are not standalone memory systems. They are **optimization layers** on top of the core three (vectors, relations, graphs):

```
Query Flow with Supporting Structures:

User Query
    |
    v
[Bloom Filter] --> "Definitely not in memory" --> STOP (saves 90% of DB queries)
    |
    v (maybe exists)
[Inverted Index] --> Keyword candidates (40x faster than scan)
    |
    v
[Vector DB] --> Semantic similarity candidates
    |
    v
[Priority Queue] --> Rank and merge results by relevance
    |
    v
[LRU Cache] --> Cache result for future access
    |
    v
Return to Agent
```

**Consolidation Flow:**

```
Working Memory (Ring Buffer)
    |
    v (buffer full or consolidation trigger)
[Priority Queue] --> Process highest-importance memories first
    |
    v
[Bloom Filter] --> Check for duplicates before storing
    |
    v (new memory)
[Vector DB + Relational DB + Knowledge Graph] --> Persist to long-term storage
    |
    v
[Inverted Index] --> Update text search index
```

---

## Cross-References

- **Core data structures (vectors, relations, graphs)**: `22_core_data_structure_hierarchy.md`
- **Memory type hierarchy these structures support**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers that use these structures**: `23_core_ai_memory_systems.md`
- **Open-source implementations using these structures**: `29_open_source_memory_implementations.md`

---

## Sources

- Perplexity AI research conversation (Feb 2026) — synthesis of data structure and AI memory literature
- [Bloom Filters by Example](https://llimllib.github.io/bloomfilter-tutorial/) — bloom filter tutorial and visualization
- [Redis Sorted Sets Internals (Skip Lists)](https://redis.io/docs/data-types/sorted-sets/) — skip list implementation in Redis
- [PostgreSQL GIN Index Documentation](https://www.postgresql.org/docs/current/gin-intro.html) — GIN index for JSONB
- [Python heapq Documentation](https://docs.python.org/3/library/heapq.html) — priority queue implementation
- [LRU Cache Design (LeetCode)](https://leetcode.com/problems/lru-cache/) — classic LRU cache implementation
- [Inverted Index in Information Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/a-first-take-at-building-an-inverted-index-1.html) — Manning et al., Introduction to Information Retrieval
- [Trie Data Structure](https://en.wikipedia.org/wiki/Trie) — prefix tree fundamentals
- [Reinforcement Learning for Cache Replacement](https://arxiv.org/abs/2007.14558) — RL-guided eviction policies
