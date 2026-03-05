---
resource_id: "c1d2ae3a-6a61-49da-bb2a-f1c634f20f6f"
resource_type: "output"
resource_name: "28_supporting_data_structures_deep_dive"
---
# Supporting Data Structures Deep Dive

<!-- section_id: "b4004902-f66b-4e13-b463-1e41eb8134cb" -->
## Purpose

This document provides a comprehensive analysis of the **supporting (optimization) data structures** used in AI agent memory systems. While the core three structures (vector databases, relational tables, knowledge graphs) form the foundation (see `22_core_data_structure_hierarchy.md`), production systems layer these additional structures on top for performance, caching, deduplication, and specialized indexing. Each structure is presented with time/space complexity, concrete Python code, and specific AI memory use cases.

---

<!-- section_id: "84727a9e-7263-4181-96dc-051ee5bf5406" -->
## 1. Bloom Filters

<!-- section_id: "8c8fbcdd-7f5e-43ce-b82c-45cc66705d14" -->
### What It Is

A **probabilistic data structure** for fast membership testing. It answers the question: "Have I seen this before?" Uses a fixed-size bit array with multiple hash functions that map inputs to bit positions.

<!-- section_id: "5c4e4b48-7996-4245-b939-fe17da23df83" -->
### How It Works

- A bit array of fixed size (e.g., 1 million bits) starts with all zeros
- Multiple hash functions (typically 3-7) map each input to bit positions
- **Insert**: Set all hashed bit positions to 1
- **Query**: Check if all hashed bit positions are 1

<!-- section_id: "9ba580c9-2b75-44a8-b45a-30b040213355" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(k) where k = number of hash functions | ~10 bits per element |
| Lookup | O(k) effectively O(1) | Fixed allocation |
| Delete | Not supported (standard) | N/A |

<!-- section_id: "23b28967-f660-4097-b9e3-7f1d4264be32" -->
### Key Properties

- **No false negatives**: If the filter says "not present," the item is definitively absent
- **False positives possible**: If the filter says "maybe present," verification is needed
- **Space efficient**: ~10 bits per element vs hundreds of bytes for storing actual data
- **Cannot delete**: Standard bloom filters do not support removal (counting bloom filters can)

<!-- section_id: "7e5db9ec-69e6-42e3-becf-7ef1e0ecfcf3" -->
### AI Memory Use Case: Duplicate Memory Detection

Before running an expensive vector similarity search, check the bloom filter first. This can eliminate ~90% of unnecessary database queries.

```python
# Before expensive vector search, check bloom filter
if not bloom_filter.might_contain(query_hash):
    return "Definitely not in memory"  # Skip database query entirely
else:
    return expensive_vector_search(query)  # Maybe exists, verify in DB
```

<!-- section_id: "7fb7386f-36cc-424d-af6a-a8ce288f295b" -->
### Other AI Memory Applications

- **Cache penetration prevention**: Filter out queries for data that definitely does not exist
- **Deduplication**: Prevent storing duplicate episodes or facts
- **Web crawl memory**: Avoid re-visiting URLs during knowledge gathering

---

<!-- section_id: "dc99f5ac-becb-4810-8606-bb28385a2a2b" -->
## 2. Inverted Indexes

<!-- section_id: "9bb23766-28f0-487f-9fed-8181e2f7f17d" -->
### What It Is

A data structure that maps **terms to document IDs** (the reverse of the normal document-to-terms mapping). The backbone of full-text search engines like Elasticsearch and PostgreSQL GIN indexes.

<!-- section_id: "aa1edb84-f409-40cb-a64d-e3e737b2319a" -->
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

<!-- section_id: "ccb2873a-e1d3-46b3-9625-b284ed27029f" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Dictionary lookup | O(log n) via B-tree or O(1) via hash | Proportional to vocabulary size |
| Result retrieval | O(k) where k = number of matches | Posting lists grow with corpus |
| Full query | O(log n + k) | N/A |

<!-- section_id: "975174a4-9e98-4399-bc90-63664c287d05" -->
### Performance Impact

- **40x speedup** over full table scans for keyword queries
- Highly efficient for Boolean queries (AND, OR, NOT)

<!-- section_id: "d1c836f6-6e04-49f9-8684-8c47acbd47fa" -->
### AI Memory Use Case: Semantic Memory Text Search

Fast keyword search across episodic memories, combined with vector similarity for hybrid retrieval.

```python
# Hybrid search: inverted index for keywords + vectors for semantics
keyword_results = inverted_index.search("budget meeting")  # Fast text match
vector_results = vector_db.similarity_search(query_embedding, k=20)  # Semantic

# Combine results with weighted scoring
combined = merge_results(keyword_results, vector_results, weights=[0.3, 0.7])
```

<!-- section_id: "4caee7f8-1d86-4a31-89e7-c3c89499dfbc" -->
### Other AI Memory Applications

- **Tag/entity lookup**: Find all memories tagged with specific entities
- **Faceted search**: Filter memories by metadata fields (date, agent, category)
- **BM25 scoring**: Rank text relevance alongside vector similarity

---

<!-- section_id: "44826d14-fe77-431f-b848-92548007add4" -->
## 3. Skip Lists

<!-- section_id: "5a4b2b53-6e07-4929-84e8-ac08df1324bc" -->
### What It Is

A **probabilistic alternative to balanced B-trees** for maintaining sorted data. Uses multiple levels of linked lists where upper levels act as "express lanes" that skip over elements for faster traversal.

<!-- section_id: "fdff58f1-13aa-4675-bbf4-0a1b54d4669a" -->
### How It Works

- **Bottom level**: A sorted linked list of all elements
- **Upper levels**: Each element is promoted with probability p (typically 0.5)
- Search starts at the top level, moves right until overshooting, then drops down one level
- Resembles a multi-lane highway with express and local lanes

<!-- section_id: "abb96a2f-2f89-42b8-9c01-57e218f5664c" -->
### Complexity

| Operation | Time (expected) | Space |
|-----------|----------------|-------|
| Search | O(log n) | O(n) expected |
| Insert | O(log n) | O(log n) levels per element |
| Delete | O(log n) | N/A |

<!-- section_id: "25eb2eaf-2281-43ea-b556-68e967ab72c7" -->
### Key Properties

- Simpler to implement than self-balancing trees (AVL, red-black)
- Naturally supports concurrent access (used in Redis sorted sets)
- Probabilistic balancing rather than deterministic rotations
- Excellent for range queries

<!-- section_id: "1dd2effd-960e-49a1-9233-b3b6a6e23ced" -->
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

<!-- section_id: "336c530e-c97f-4301-986f-2832d76b5b9e" -->
### Other AI Memory Applications

- **Memory importance scoring**: Maintain sorted list of memories by importance/recency score
- **Range queries**: "Find all memories from last week" or "memories with score > 0.8"
- **Leaderboard-style ranking**: Track most-accessed memories for cache warming

---

<!-- section_id: "e607f168-1aed-4f3a-a50c-415d7883cf2d" -->
## 4. Tries (Prefix Trees)

<!-- section_id: "8bbe86f1-b5b8-4dce-a017-ee103af6e301" -->
### What It Is

A tree data structure where each node represents a character (or token). Paths from root to leaves spell out complete strings. Common prefixes share nodes, making it extremely efficient for prefix-based operations.

<!-- section_id: "49999dec-9524-4b50-8ed6-fe9f22720d7a" -->
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

<!-- section_id: "07c15c59-ebdb-4387-bfb1-67718339ea5e" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Search | O(m) where m = query length | O(ALPHABET * n * m) worst case |
| Insert | O(m) | Same |
| Prefix search | O(m + k) where k = results | Same |

**Key property**: Search time depends only on query length, NOT on the number of stored items.

<!-- section_id: "2f5149f2-1959-48f4-a687-9f7f462c353f" -->
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

<!-- section_id: "7235d1a2-165d-4a35-be8c-c0358b39e840" -->
### Other AI Memory Applications

- **Command completion**: Agent suggests commands or actions based on typed prefix
- **Set-trie variant**: Stores entire sets efficiently for dependency checking across memory items

---

<!-- section_id: "3cfcc976-f3e3-43c1-a3fc-e6accd4d585f" -->
## 5. Ring Buffers (Circular Buffers)

<!-- section_id: "6d5e6ef1-b258-4b6d-a28e-68a2a2a70fb3" -->
### What It Is

A **fixed-size array** with read and write pointers that wrap around when reaching the end. When full, new items overwrite the oldest data automatically. The fundamental data structure for sliding-window memory.

<!-- section_id: "c111f764-6afa-4b98-856a-6c085490e9ec" -->
### How It Works

- Fixed-size array allocated at initialization
- Write pointer advances with each insertion, wrapping to position 0 after the last slot
- When full, the oldest item is silently overwritten
- No memory allocation after initialization

<!-- section_id: "07edca4b-8d2d-4fda-990b-32d4d839fad9" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Push (write) | O(1) | Fixed at initialization |
| Read (by index) | O(1) | Fixed |
| Eviction | Automatic (O(0)) | No extra space |

<!-- section_id: "5fec0da4-001b-44ed-b709-2e2b21902cca" -->
### Key Properties

- **Constant memory**: Never grows beyond the fixed size
- **Cache-friendly**: Contiguous memory layout, excellent CPU cache behavior
- **Automatic eviction**: Old data naturally drops off without explicit garbage collection
- **Zero allocation overhead**: No malloc/free after initialization

<!-- section_id: "bbeaadf8-2116-4cf2-9eaa-0de7e6694df5" -->
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

<!-- section_id: "a4c24894-d697-494d-8f9c-934a61aad568" -->
### Other AI Memory Applications

- **Recent events buffer**: Keep a sliding window of recent episodes before consolidation
- **Sensor data streams**: Store last N readings for pattern detection in embodied agents
- **Token context window**: Manage the most recent tokens within a fixed context budget

---

<!-- section_id: "4513d150-b2ef-4731-bcc5-1f4e3773cc4e" -->
## 6. Priority Queues / Heaps

<!-- section_id: "43405147-db04-48d7-ab9f-5a9275f88a37" -->
### What It Is

A **binary heap** (complete binary tree) that maintains a priority ordering. Max-heaps keep the highest-priority element at the root; min-heaps keep the lowest. Typically implemented as an array for cache efficiency.

<!-- section_id: "af7b55c2-1445-4b92-b41e-abe63f1d8a06" -->
### How It Works

- **Binary heap property**: Parent >= children (max-heap) or Parent <= children (min-heap)
- **Insert**: Add at the bottom, "bubble up" to restore heap property
- **Extract**: Remove root, move last element to root, "bubble down"
- **Array representation**: For node at index i, children are at 2i+1 and 2i+2

<!-- section_id: "e4cd07c9-e760-4cce-9c6a-a9ab1d6fc106" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Insert | O(log n) | O(n) total |
| Extract min/max | O(log n) | N/A |
| Peek min/max | O(1) | N/A |
| Build heap | O(n) | N/A |

<!-- section_id: "b2ab7149-bfc0-462a-8583-69ab2f0152a4" -->
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

<!-- section_id: "bdde4bfe-3a5f-4ef0-b767-8911e2f0deae" -->
### Other AI Memory Applications

- **Retrieval ranking**: Sort candidate memories by combined relevance score
- **Eviction candidates**: Maintain a min-heap of low-importance memories for deletion under memory pressure
- **Attention mechanisms**: Prioritize which memories to load into a limited context window

---

<!-- section_id: "bc915d21-5420-457b-a65e-a639a2c78577" -->
## 7. LRU/LFU Caches

<!-- section_id: "a9115275-8815-4d44-89a5-1704ab745474" -->
### What It Is

**Intelligent eviction caches** that decide which items to remove when the cache is full. LRU (Least Recently Used) evicts the item not accessed for the longest time. LFU (Least Frequently Used) evicts the item accessed the fewest total times.

<!-- section_id: "be720de3-74fb-453e-ab65-536087f3f874" -->
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

<!-- section_id: "9f037d51-f2ec-4ab6-b369-e84bd46d984e" -->
### Complexity

| Operation | LRU Time | LFU Time | Space |
|-----------|----------|----------|-------|
| Get | O(1) | O(1) with bucket optimization | O(n) |
| Put | O(1) | O(log n) or O(1) with buckets | O(n) |
| Evict | O(1) | O(1) with min-freq pointer | N/A |

<!-- section_id: "22a6f050-2e78-4bf6-89aa-8af2e1b4be5c" -->
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

<!-- section_id: "e2714326-fee2-42e1-be0e-ab27597018da" -->
### Adaptive Caching with Reinforcement Learning

Modern systems go beyond fixed LRU/LFU policies. **Reinforcement learning** can learn optimal eviction policies that adapt to workload patterns, outperforming both LRU and LFU by learning which memories are likely to be accessed in the near future based on contextual signals.

<!-- section_id: "a068f005-7f34-4ea6-897b-d696284e8d09" -->
### Other AI Memory Applications

- **Context window optimization**: Keep the most relevant memories in fast RAM storage
- **Working memory**: Maintain "hot" memories in-process, cold memories on disk
- **Multi-tier caching**: L1 (in-process LRU) -> L2 (Redis) -> L3 (persistent DB)

---

<!-- section_id: "9ecfbd24-09d2-4975-be59-e1d73d7f33da" -->
## 8. JSONB / Document Stores (GIN Indexes)

<!-- section_id: "db3b5ed3-8ad3-4347-ad2e-5f2e8b6879b5" -->
### What It Is

**Binary JSON** stored in a database column (typically PostgreSQL JSONB) with specialized indexing. Combines the flexibility of schema-free documents with the query power of relational databases. GIN (Generalized Inverted Index) enables efficient containment and existence queries on JSON paths.

<!-- section_id: "d41e0760-a353-4a6c-be71-9f41caeee7f9" -->
### How It Works

- JSONB stores JSON in a decomposed binary format (not plain text)
- B-tree indexes on specific JSON paths for equality/range queries
- GIN indexes for containment queries (`@>`) and key existence (`?`)
- Supports indexing nested objects and arrays

<!-- section_id: "405886f4-0988-4542-aaef-d1158ca6dcc5" -->
### Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Path lookup (B-tree indexed) | O(log n) | Index proportional to data |
| Containment query (GIN) | O(log n + k) | GIN index ~2-3x data size |
| Full document read | O(1) by primary key | Document size |
| Schema change | O(0) - no migration needed | N/A |

<!-- section_id: "52fc95a3-ed54-44f6-b724-edaf79819094" -->
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

<!-- section_id: "624f5cba-a471-4082-96e1-9fb19f7b1354" -->
### Other AI Memory Applications

- **Nested structures**: Store hierarchical memories (episodes with sub-events) without table joins
- **Dynamic properties**: Add new memory attributes (emotion scores, decay rates) without migrations
- **Multi-modal metadata**: Store image dimensions, audio duration, text stats alongside embeddings
- **Agent state snapshots**: Serialize complex agent state as JSONB for checkpointing

---

<!-- section_id: "71cd2c26-39bf-4ff3-bb6b-0050fe63413f" -->
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

<!-- section_id: "dfbcb4b2-e7de-48aa-a3d0-e1f839b717bc" -->
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

<!-- section_id: "7a6b5b92-8a34-43e2-b0d8-5b6729fbc091" -->
## Cross-References

- **Core data structures (vectors, relations, graphs)**: `22_core_data_structure_hierarchy.md`
- **Memory type hierarchy these structures support**: `21_core_memory_structure_hierarchy.md`
- **AI system tiers that use these structures**: `23_core_ai_memory_systems.md`
- **Open-source implementations using these structures**: `29_open_source_memory_implementations.md`

---

<!-- section_id: "9335ced6-a267-4a41-bbe9-0dc3191c4303" -->
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
