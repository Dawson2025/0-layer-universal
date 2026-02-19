# Underlying Data Structures for AI Agent Memory Systems

## Purpose

Memory types like "episodic," "semantic," "short-term," and "long-term" describe *what* is stored and *how long* it lasts. This document covers the **actual data structures** underneath — the technical building blocks that these memory types are implemented on top of.

The relationship: **Memory type** (episodic, semantic, etc.) is built on top of a **data structure** (vector store, key-value map, etc.), which is stored in a **storage backend** (database, file system, model weights, etc.).

---

## 1. Raw Message List (Array / Queue)

### What It Is
A simple ordered list of messages: `[msg1, msg2, msg3, ...]`. The most basic data structure possible — just an array that grows as the conversation continues.

### How It Works
- Messages are appended in order
- The entire list is injected into the LLM's context window
- No processing, no transformation, no indexing
- Retrieval = "load everything"

### Technical Details
- Data structure: Array, List, or Deque
- Storage: In-memory (session-scoped) or persisted to database rows
- Time complexity: O(1) append, O(n) to load everything
- Space: Grows linearly with conversation length

### Used By
- LangChain `ConversationBufferMemory`
- Any basic chatbot's conversation history
- Raw chat logs / transcripts

### Which Memory Types Use This
- **Short-term / working memory** (current conversation context)
- **Episodic memory** (raw session transcripts)

### Strengths
- Zero information loss — every word preserved
- Simplest possible implementation
- No extraction errors

### Weaknesses
- Overflows context window in long conversations
- Cost grows linearly (every token loaded = money)
- No selectivity — loads irrelevant information alongside relevant

### Brain Analogy
- Closest to **sensory memory buffer** — brief, unprocessed, everything captured before being selectively encoded

---

## 2. Sliding Window (Circular Buffer / Bounded Array)

### What It Is
A fixed-size list that drops the oldest entries when full. Only the most recent K messages are kept.

### How It Works
- New messages push in at one end
- When the buffer reaches size K, the oldest message is evicted (FIFO — first in, first out)
- Only the window contents are injected into context

### Technical Details
- Data structure: Deque with maxlen, or circular buffer (ring buffer)
- Storage: In-memory
- Time complexity: O(1) append and evict, O(K) to load window
- Space: Fixed at K items regardless of conversation length

### Used By
- LangChain `ConversationBufferWindowMemory(k=N)`
- Any framework with `max_turns` or `max_tokens` parameter

### Which Memory Types Use This
- **Short-term / working memory** with bounded capacity
- Mirrors Miller's Law (~7 items in human working memory)

### Strengths
- Fixed, predictable token cost
- Simple, no LLM calls needed for management
- Good for task-focused agents where only recent context matters

### Weaknesses
- Hard boundary — information outside the window is completely gone (not summarized, just deleted)
- Users who reference something said 50 turns ago will get no recall
- No importance-based retention — an important early message is treated the same as trivial chatter

### Brain Analogy
- Closest to **working memory** — limited capacity, recency-biased, items fall out when capacity is exceeded

---

## 3. Key-Value Store (Hash Map / Dictionary)

### What It Is
A lookup table mapping keys to values. The most common structure for entity memory.

```
{
  "Alice": "Senior engineer at Acme Corp, prefers Python, working on Project X",
  "Project X": "Due March 2026, uses React + FastAPI, Alice is lead",
  "user_preferences": "Dark mode, concise answers, no emojis"
}
```

### How It Works
- Entities or topics are keys
- Values are text summaries, fact lists, or structured data
- Lookup is by exact key match (O(1))
- Values get updated/overwritten as new information arrives

### Technical Details
- Data structure: Hash map / dictionary / associative array
- Storage: In-memory dict, Redis, SQLite, DynamoDB, or any KV store
- Time complexity: O(1) lookup, O(1) insert/update
- Space: Grows with number of distinct entities

### Used By
- LangChain `ConversationEntityMemory` with swappable store (in-memory, Redis, SQLite)
- Mem0's key-value component (alongside vector + graph)
- MemGPT/Letta core memory blocks (`human` block, `persona` block)
- User preference stores

### Which Memory Types Use This
- **Entity memory** (per-entity fact storage)
- **Profile / persona memory** (user and agent identity)
- **Core memory** (always-in-context editable blocks)
- **Factual / semantic memory** (simple fact lookup)

### Strengths
- Extremely fast lookup (O(1))
- Simple to implement and understand
- Human-readable and editable
- Easy to update specific entries without affecting others

### Weaknesses
- No similarity search — you must know the exact key
- No relationship modeling between entities (flat structure)
- Values can become stale or contradictory without maintenance
- Entity extraction (determining what keys to create) relies on LLM and can introduce errors

### Brain Analogy
- Closest to **semantic memory for specific entities** — "I know that Alice is an engineer" without remembering when or how you learned it

---

## 4. Vector Store (Embedding Database)

### What It Is
A collection of dense vector representations (embeddings) with an index for similarity search. Covered in depth in `15_vectors_graphs_and_neurology.md`.

### How It Works
- Text chunks are converted to vectors (arrays of floats) by an embedding model
- Vectors are stored with their original text and metadata
- Retrieval = embed the query, find the N nearest vectors by cosine similarity or dot product

### Technical Details
- Data structure: Arrays of float32/float16 vectors + approximate nearest neighbor (ANN) index (HNSW, IVF, etc.)
- Storage: Specialized vector databases (Pinecone, Qdrant, Weaviate, ChromaDB, FAISS, Milvus, pgvector)
- Time complexity: O(log n) to O(n) for search depending on index type; O(1) insert
- Space: ~1-4KB per vector (depends on dimensionality, typically 384-1536 dims)
- Vectors are opaque (not human-readable)

### Used By
- RAG systems (the dominant AI memory pattern)
- LangChain `VectorStoreRetrieverMemory`
- Mem0's vector component
- CrewAI's LanceDB-backed memory

### Which Memory Types Use This
- **Long-term semantic memory** (large knowledge bases)
- **Episodic memory** (searchable interaction history)
- **Contextual memory** (finding relevant background context)

### Strengths
- Scales to millions of memories
- Semantic search (finds conceptually related content, not just keyword matches)
- No need to know exact queries — fuzzy matching works

### Weaknesses
- No relationship types (only "similar" / "not similar")
- No multi-hop reasoning
- Embedding quality determines retrieval quality
- Binary blobs — not human-readable, not git-friendly
- Model-specific — embeddings from one model can't be used with another

### Brain Analogy
- Loosely like **distributed representations** — similar concepts have overlapping neural activation patterns. But the brain does associative activation through learned pathways, not nearest-neighbor search.

### Full Coverage
- See `15_vectors_graphs_and_neurology.md` → Sections 1 and 4 for deep comparison with knowledge graphs and neurology

---

## 5. Knowledge Graph (Graph Database)

### What It Is
Entities as nodes, relationships as typed directed edges. Covered in depth in `15_vectors_graphs_and_neurology.md`.

### How It Works
- Entities (nodes) have labels and properties
- Relationships (edges) have types, directions, and properties
- Retrieval = graph traversal via query languages (Cypher, SPARQL, Gremlin)

### Technical Details
- Data structure: Adjacency lists or adjacency matrices with typed edges
- Storage: Graph databases (Neo4j, Amazon Neptune, ArangoDB, FalkorDB)
- Time complexity: O(V + E) for traversal; pattern matching varies
- Space: Nodes + edges + properties

### Used By
- Mem0 (graph component)
- Zep (temporal knowledge graph)
- LangChain `ConversationKGMemory`
- Microsoft GraphRAG

### Which Memory Types Use This
- **Semantic / factual memory** (structured world knowledge)
- **Entity memory** (entity relationships)
- **Temporal memory** (event sequences with temporal edges)

### Strengths
- Explicit typed relationships (cause-effect, part-whole, etc.)
- Multi-hop reasoning ("who manages the person who wrote document X?")
- Human-readable and explainable
- Precise queries

### Weaknesses
- Expensive to build (entity/relationship extraction is error-prone)
- Schema must be designed upfront (or dynamically, which adds complexity)
- No fuzzy/semantic matching (can't find "similar" things, only connected things)
- Graph traversal can be slow on very large graphs

### Brain Analogy
- Closest to **semantic memory in temporal cortex** — structured, declarative knowledge with explicit relationships. See `15_vectors_graphs_and_neurology.md` for full comparison.

### Full Coverage
- See `15_vectors_graphs_and_neurology.md` → Sections 2, 3, and 4
- See `09_rag_and_knowledge_graphs.md` → Sections 3-6

---

## 6. LLM-Generated Summary (Compressed Text)

### What It Is
A single text string (or short document) that replaces a larger body of content. The LLM itself performs the compression by summarizing.

### How It Works
- After N messages (or on a schedule), the LLM is asked: "Summarize this conversation so far"
- The summary replaces the raw messages in context
- Some implementations keep a hybrid: recent messages raw + older messages summarized
- Summaries can be recursive (summary of summaries)

### Technical Details
- Data structure: A single text string, periodically regenerated
- Storage: In-memory string, or persisted as a text file / database entry
- Time complexity: O(1) to load (it's just one string); O(n) to generate (LLM must read all content)
- Space: Roughly constant regardless of conversation length (summary stays a similar size)
- Requires an LLM call to produce — adds latency and cost

### Used By
- LangChain `ConversationSummaryMemory`
- LangChain `ConversationSummaryBufferMemory` (hybrid: summary + recent window)
- MemoryOS MTM segments (summarized topic clusters)
- Any system with "rolling summaries"

### Which Memory Types Use This
- **Long-term memory** (compressed history)
- **Medium-term memory** (summarized recent sessions)
- **Consolidated memory** (merging multiple sources)

### Strengths
- Bounded token cost regardless of conversation length
- Captures the gist of long interactions
- Human-readable output

### Weaknesses
- **Lossy compression** — details are permanently lost
- **Summarization errors** — LLM can misrepresent, omit, or hallucinate during summarization
- **Compounds over time** — summary of a summary of a summary degrades quality
- Latency — requires an LLM call to produce
- Not suitable for exact-wording-matters contexts (legal, compliance)

### Brain Analogy
- Closest to **memory consolidation** — the brain's progressive summarization where raw episodic memories gradually become abstract semantic knowledge, losing specific details but retaining the gist. Sleep replay compresses sequences similarly.

---

## 7. Relational Database (SQL Tables)

### What It Is
Structured tables with rows (records) and columns (attributes), queried via SQL.

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    content TEXT,
    source VARCHAR(50),
    importance FLOAT,
    entity VARCHAR(100),
    memory_type VARCHAR(20)
);
```

### How It Works
- Each memory is a row with structured attributes
- Columns provide indexable metadata (timestamp, importance, source, type)
- SQL queries for filtered retrieval: `SELECT * FROM memories WHERE entity='Alice' AND importance > 0.7 ORDER BY timestamp DESC`
- JOINs can connect related tables (memories → entities → relationships)

### Technical Details
- Data structure: B-tree indexed tables
- Storage: PostgreSQL, SQLite, MySQL
- Time complexity: O(log n) for indexed queries, O(n) for full scans
- Space: Efficient for structured data with fixed schemas

### Used By
- LangChain entity stores (SQLite option)
- Custom memory systems needing complex filtered queries
- Logging and audit trail systems
- Any production system that needs ACID transactions

### Which Memory Types Use This
- **Episodic memory** (timestamped event records)
- **Entity memory** (structured entity attributes)
- **Metadata-heavy memory** (when you need to query by importance, source, timestamp, etc.)

### Strengths
- Rich querying (filter by any combination of attributes)
- ACID transactions (reliable, consistent)
- Mature tooling, widely understood
- Good for temporal queries (WHERE timestamp BETWEEN ...)

### Weaknesses
- Fixed schema — adding new attributes requires migrations
- No semantic search (keyword only, unless combined with vector extension like pgvector)
- No relationship traversal (JOINs are flat, not graph-native)

### Brain Analogy
- Not a natural brain analog — the brain doesn't store information in tabular form. Closest to a **structured external memory aid** like a spreadsheet or ledger.

---

## 8. Document Store (JSON/BSON Documents)

### What It Is
A collection of self-contained documents with flexible schemas. Each memory is a JSON-like document that can have different fields.

```json
{
  "id": "mem_001",
  "content": "Alice prefers Python for backend work",
  "metadata": {
    "timestamp": "2026-02-17T10:30:00Z",
    "source": "conversation",
    "confidence": 0.9,
    "tags": ["preference", "technology", "Alice"]
  },
  "embedding": [0.82, -0.14, ...]
}
```

### How It Works
- Each memory is a self-contained document
- Documents in the same collection can have different fields (schema-flexible)
- Queries filter by any field or nested field
- Can combine with text search and (in some engines) vector search

### Technical Details
- Data structure: B-tree indexed documents (JSON/BSON)
- Storage: MongoDB, CouchDB, Elasticsearch, Firebase
- Time complexity: O(log n) for indexed queries
- Space: Variable per document (flexible schema)

### Used By
- Mem0 internal storage
- Custom memory systems needing flexible schemas
- Systems that store heterogeneous memory types (some have embeddings, some have entity lists, some have raw text)

### Which Memory Types Use This
- **Any memory type** where entries have varying structures
- **Mixed-type memory stores** (one collection for episodic, entity, and factual memories with different fields)

### Strengths
- Schema flexibility — different memories can have different structures
- Easy to evolve over time (add fields without migrations)
- Good for heterogeneous memory (mix of types in one store)
- Native JSON — easy to work with in code

### Weaknesses
- No relationship modeling (flat documents)
- No native semantic search (unless the DB supports vector extensions)
- Can become a "dumping ground" without discipline

### Brain Analogy
- Not a natural brain analog. Closest to **a filing cabinet where each folder can contain different types of documents**.

---

## 9. Plain Text Files (Markdown / JSON on Disk)

### What It Is
Memory stored as human-readable files in a directory structure. Our framework's primary approach.

```
memory/
  episodic/
    2026-02-17_session.md
    2026-02-18_session.md
  entities/
    alice.md
    project_x.md
  learnings/
    gotcha_jq_comments.md
```

### How It Works
- Each memory is a file (Markdown for human-readable, JSON for structured)
- Directory structure provides organization and scoping
- Files can have YAML frontmatter for metadata
- Retrieval = read relevant files (by name, path, or grep search)
- Git provides versioning, history, and collaboration for free

### Technical Details
- Data structure: Files + directory tree (a hierarchical namespace)
- Storage: Local filesystem, synced via git or file sync tools
- Time complexity: O(1) to read a specific file; O(n) to search across files
- Space: Minimal overhead — just the text

### Used By
- Letta filesystem baseline (74% LoCoMo with just file tools + GPT-4o mini)
- Our layer-stage framework (CLAUDE.md chain, episodic directories, 0AGNOSTIC.md)
- Claude Code auto-memory (`~/.claude/projects/*/memory/`)
- Any tool-agnostic memory system

### Which Memory Types Use This
- **All of them** — any memory type can be stored as files
- Particularly good for: episodic memory (session logs), semantic memory (knowledge files), profile memory (identity files), procedural memory (skill files)

### Strengths
- **Human-readable and editable** — the user can read, write, and audit memories directly
- **Tool-agnostic** — any AI tool can read files (Claude, Gemini, Cursor, etc.)
- **Git-friendly** — version history, diffs, merges, branching all come free
- **Simple** — no database to set up, no API to learn
- **The baseline to beat** — if a fancy system doesn't outperform files + a good LLM, it's over-engineered

### Weaknesses
- **No semantic search** (only filename and grep-based retrieval)
- **Doesn't scale to millions of entries** (file system slows down)
- **No built-in indexing** (must maintain indexes manually)
- **Retrieval depends on good naming and organization** — badly organized files = bad retrieval

### Brain Analogy
- Closest to **external memory aids** — notebooks, journals, diaries. Not a brain structure, but an augmentation of memory that the brain can interact with.

---

## 10. KV Cache (Attention Key-Value Cache)

### What It Is
The key and value matrices computed during the LLM's self-attention mechanism, cached to avoid recomputation. This is the model's **latent working memory** — it exists only during inference and is not normally persisted.

### How It Works
- As the LLM processes each token, every attention layer computes key (K) and value (V) vectors
- These are cached so that when generating the next token, previous tokens don't need to be reprocessed
- The KV cache grows with each token generated
- When context window is full, the cache must be managed (dropped, compressed, or evicted)

### Technical Details
- Data structure: Tensors (3D arrays of floats) — one K matrix and one V matrix per attention layer per attention head
- Storage: GPU memory (VRAM) during inference
- Size: Grows linearly with sequence length × number of layers × hidden dimension
- For a 200K context model, KV cache can consume many GB of VRAM

### KV Cache Management Strategies
| Strategy | How | Trade-off |
|---|---|---|
| **Dropping** | Remove cache entries for less important tokens | Loses information but frees memory |
| **Compression** | Low-rank approximation or quantization of cached values | Reduces memory with some quality loss |
| **Selective loading** | Only load relevant KV pairs via approximate nearest neighbor | Faster but may miss relevant context |
| **Offloading** | Move to CPU RAM or disk, reload when needed | Slower but retains all information |

### Used By
- Every LLM during inference (this is always happening under the hood)
- MemOS manipulates KV cache directly (freezing, selective loading, priority eviction)
- Memory3 injects external knowledge as KV pairs into attention layers

### Which Memory Types Use This
- **Working memory** — the active context the model is currently processing
- **Latent memory** — hidden state representations that encode meaning in a non-human-readable form

### Strengths
- Zero additional infrastructure — it's built into the model
- Fastest possible "retrieval" — information is already in the attention computation
- Rich representation — captures nuanced contextual meaning

### Weaknesses
- **Not persistent** — destroyed when the session ends (unless explicitly saved)
- **Not human-readable** — opaque tensors, no way to inspect what's stored
- **Not transferable** — KV cache from one model can't be used by another
- **Memory-hungry** — consumes significant GPU VRAM
- **No selective access** — everything in the cache influences everything else through attention

### Brain Analogy
- Closest to **active neural firing patterns** — the dynamic, fleeting state of neurons currently active in working memory. Just as neural firing patterns are lost when you stop thinking about something (unless consolidated to long-term storage), KV cache is lost when the session ends.

---

## 11. Model Parameters (Neural Network Weights)

### What It Is
The billions of floating-point numbers that make up the LLM's neural network. Everything the model "knows" from pretraining is encoded here — distributed across layers, not localized to specific parameters.

### How It Works
- During pretraining, the model processes trillions of tokens
- Statistical patterns from this training data get encoded as weight values
- When you ask a question, the weights produce the answer through forward passes
- The knowledge is distributed — no single weight stores a specific fact

### How to Modify It (Adding New Memories to Parametric Storage)
| Method | How | When to Use |
|---|---|---|
| **Fine-tuning** | Train on new data, adjust all weights | Large-scale knowledge updates |
| **LoRA adapters** | Train small additional weight matrices that layer on top | Efficient task-specific adaptation |
| **Knowledge editing (ROME, MEMIT)** | Surgically modify specific weights to change specific facts | Correcting individual facts ("The president of X is now Y") |
| **Continual learning** | Ongoing training on new data without forgetting old | Keeping model up-to-date over time |
| **Machine unlearning** | Removing specific knowledge from weights | Privacy, compliance, removing harmful content |

### Technical Details
- Data structure: Multi-dimensional tensors (weight matrices) organized into layers
- Storage: Model checkpoint files (often 10-100+ GB)
- Access: Forward pass through the entire network
- Not directly queryable — you can't ask "what do you know about X?" and get a reliable answer

### Used By
- Every LLM (this IS the model)
- Fine-tuned domain models
- LoRA adapters for task-specific customization

### Which Memory Types Use This
- **Long-term semantic memory** — general world knowledge from pretraining
- **Procedural memory** — learned patterns for how to respond, reason, use tools

### Strengths
- Instant retrieval — no database lookup, knowledge flows through the forward pass
- Massive capacity — billions of parameters can store enormous amounts of knowledge
- Generalizes — can answer novel questions by combining stored patterns

### Weaknesses
- **Opaque** — cannot inspect, audit, or verify what's stored
- **Expensive to update** — fine-tuning requires compute and data
- **Catastrophic forgetting** — updating can overwrite existing knowledge
- **Hallucination** — the model can generate plausible-sounding but false information
- **Stale** — knowledge is frozen at training cutoff (unless updated)

### Brain Analogy
- Closest to **synaptic weights** — the strength of connections between neurons, shaped by lifetime of experience (training). Just as you can't open someone's brain and read out "what they know about trees," you can't inspect model weights for specific facts.

---

## 12. Semantic Tree (Hierarchical Tree Structure)

### What It Is
A tree data structure where nodes represent semantic categories at different levels of abstraction, and memories are stored as leaves. SHIMI is the primary implementation.

```
Root
├── Science
│   ├── Biology
│   │   ├── Botany
│   │   │   ├── "Oak trees produce acorns"
│   │   │   └── "Photosynthesis requires sunlight"
│   │   └── Zoology
│   └── Physics
├── People
│   ├── Colleagues
│   └── Family
└── Projects
    ├── Project X
    └── Project Y
```

### How It Works
- New memories are classified by an LLM into the appropriate branch
- Retrieval descends from root, choosing the most relevant branch at each level
- Like a library's Dewey Decimal system — narrow down level by level
- Each node stores a summary of its children for efficient traversal

### Technical Details
- Data structure: N-ary tree with LLM-classified node routing
- Storage: Tree nodes can be in-memory, database-backed, or file-based
- Time complexity: O(log n) retrieval (descend tree) vs O(n) for flat search
- Decentralized sync possible via Merkle-DAG + Bloom filters + CRDT (SHIMI)

### Used By
- SHIMI (Semantic Hierarchical Memory Index)
- Custom semantic organization systems

### Which Memory Types Use This
- **Long-term semantic memory** (organized knowledge at scale)
- **Multi-agent shared memory** (SHIMI supports decentralized peer-to-peer sync)

### Strengths
- **Sublinear retrieval** — O(log n) vs O(n) for flat vector search
- **Explainable** — you can trace exactly why something was retrieved (show the path)
- **Hierarchical organization** — natural for knowledge that has categorical structure
- **Benchmark results** — 90% top-1 accuracy vs 65% for flat RAG

### Weaknesses
- Tree restructuring is expensive when knowledge doesn't fit the current hierarchy
- LLM classification at each node adds latency
- Requires well-defined categories — messy, overlapping knowledge is hard to tree-ify
- Not suitable for small memory sets (tree overhead not justified)

### Brain Analogy
- Closest to **categorical organization in temporal cortex** — the brain organizes concepts hierarchically (animal → mammal → dog → Labrador). Category-specific brain injuries (e.g., losing knowledge of living things but not tools) suggest hierarchical storage.

---

## 13. Scored List / Priority Queue (Composite Scoring)

### What It Is
A single flat list of memories where each entry has a composite score calculated from multiple factors. Retrieval simply sorts by score and returns the top K.

### How It Works
```
score = (recency_weight × recency_score) +
        (semantic_weight × semantic_similarity) +
        (importance_weight × importance_score)
```
- Each memory has attributes: creation time, embedding, importance rating
- At retrieval time, all three factors are computed and combined
- Top-scoring entries are returned
- Weights are tunable (more recency-biased vs more relevance-biased)

### Technical Details
- Data structure: List/array with per-entry metadata, sorted on demand
- Storage: Any database that can store the fields (often LanceDB, SQLite, or in-memory)
- Time complexity: O(n) to score all entries, O(n log n) to sort, or use a heap for O(n log K) top-K
- CrewAI default: `recency_half_life_days = 30`

### Used By
- CrewAI's unified Memory class
- Generative Agents (recency × relevance × importance)
- Any system that combines multiple retrieval signals

### Which Memory Types Use This
- **Unified memory** (single store replacing multiple memory types)
- **Experiential memory** (where recency, relevance, and importance all matter)

### Strengths
- Simple — one store, one scoring function, one API
- Adaptive — weights can be tuned for different use cases
- Balances multiple factors without maintaining separate systems

### Weaknesses
- Scoring function quality determines system quality — bad weights = bad retrieval
- Harder to debug than separate stores (why was this retrieved? which factor dominated?)
- Doesn't support fundamentally different query types (temporal vs semantic vs structural)

### Brain Analogy
- Loosely like **memory retrieval competition** — in ACT-R, memories compete for activation based on base-level activation (recency/frequency) + spreading activation (relevance) + noise. The highest-activation memory "wins" retrieval.

---

## 14. Stack (LIFO — Last In, First Out)

### What It Is
A data structure where the last item added is the first one retrieved. Used for goal management and nested reasoning.

### How It Works
- Push a goal onto the stack → it becomes the current focus
- Completing or abandoning a goal → pop it, return to the previous one
- Supports nesting: main_goal → sub_goal → sub_sub_goal

### Technical Details
- Data structure: Stack (array with push/pop at one end)
- Storage: In-memory
- Time complexity: O(1) push, O(1) pop
- Space: Proportional to nesting depth

### Used By
- SOAR's goal stack (central to its decision cycle)
- Agent planning systems with goal decomposition
- Chain-of-thought reasoning with nested sub-problems

### Which Memory Types Use This
- **Working memory / task state** (current goals and subgoals)
- **Prospective memory** (planned future actions)

### Strengths
- Natural for hierarchical task decomposition
- Ensures you return to the parent goal after completing a subgoal
- Simple, well-understood data structure

### Weaknesses
- Only tracks the current path — no history of completed or abandoned goals
- Strictly LIFO — can't easily switch to a sibling goal without unwinding

### Brain Analogy
- Loosely like **the prefrontal cortex's goal maintenance system** — maintaining the current goal hierarchy, with the ability to push subgoals and return to the parent goal.

---

## 15. Production Rule Database (IF-THEN Rule Sets)

### What It Is
A collection of condition-action pairs that encode procedural knowledge — "how to do things" rather than "what things are."

```
Rule 1: IF (goal = navigate) AND (obstacle = detected) → THEN (turn left)
Rule 2: IF (goal = answer_question) AND (confidence < 0.5) → THEN (search_web)
Rule 3: IF (user_said = "thank you") → THEN (respond_politely, close_task)
```

### How It Works
- Each rule has a condition (pattern to match against current state) and an action (what to do)
- Rules are tested against working memory
- Matching rules compete for activation (utility-based selection)
- Selected rules fire, modifying working memory or producing actions
- New rules can be learned through experience (chunking in SOAR)

### Technical Details
- Data structure: Set of (condition, action, utility) tuples
- Storage: Rule database (custom format, often in-memory)
- Matching: Pattern matching against current state (can be expensive for large rule sets)
- Learning: Utility values updated through reinforcement; new rules created through chunking

### Used By
- SOAR procedural memory
- ACT-R production memory
- Expert systems
- ReAct-style agent patterns (implicitly — the LLM's learned patterns function as soft production rules)

### Which Memory Types Use This
- **Procedural memory** (skills, habits, how-to knowledge)
- **Policy memory** (decision-making rules)

### Strengths
- Interpretable — you can read and understand each rule
- Learnable — new rules emerge from experience
- Fast execution once matched
- Supports complex conditional behavior

### Weaknesses
- Rule sets can become unmanageable at scale (thousands of rules)
- Rule conflicts require resolution mechanisms
- Brittle — slight variations in conditions can prevent matching
- Hard to cover all cases (combinatorial explosion)

### Brain Analogy
- Closest to **procedural memory in the basal ganglia** — automatic, habitual responses triggered by specific conditions. Like how you don't think about the steps of riding a bike — the procedure fires automatically when the conditions match.

---

## 16. Activation-State Snapshots (Serialized Tensors)

### What It Is
A saved copy of the LLM's internal hidden states at a specific point in processing. Like a save-state in a video game — you can reload the model's exact internal state later.

### How It Works
- At a chosen point during inference, the model's KV cache and/or hidden layer activations are serialized (saved to disk)
- Later, these states can be loaded back, restoring the model to exactly where it was
- No need to re-process the entire context — just load the snapshot and continue

### Technical Details
- Data structure: Serialized tensors (multi-dimensional float arrays)
- Storage: Disk files, typically in model-specific formats
- Size: Can be very large (GB) depending on model size and context length
- Requires the exact same model architecture to reload

### Used By
- MemOS's "activation memory" (MemCube abstraction)
- Memory3 (injecting knowledge as KV pairs)
- Prompt caching systems (Anthropic's prompt caching, etc.)
- Checkpoint/resume systems for long-running tasks

### Which Memory Types Use This
- **Latent memory** (hidden state representations)
- **Working memory snapshots** (saving and restoring processing state)

### Strengths
- **Instant context restoration** — no reprocessing needed
- **Preserves nuance** — captures the full internal state, including subtleties lost in text summaries
- Enables "memory transplants" between sessions

### Weaknesses
- **Model-locked** — snapshots only work with the exact same model
- **Opaque** — can't inspect or edit what's in the snapshot
- **Large** — significant storage requirements
- **Fragile** — model updates invalidate all saved snapshots

### Brain Analogy
- Loosely like **state-dependent memory** — the phenomenon where you remember things better when you're in the same mental/physical state as when you learned them. Restoring the model's hidden states recreates the "mental state" it was in.

---

## Summary: Which Memory Types Use Which Data Structures

| Memory Type | Typical Data Structures |
|---|---|
| **Conversation buffer (short-term)** | Raw message list, sliding window |
| **Working memory / scratchpad** | KV cache, stack, in-memory variables |
| **Entity memory** | Key-value store, knowledge graph |
| **Episodic memory** | Raw message list, relational DB, files, document store |
| **Semantic / factual memory** | Vector store, knowledge graph, key-value store, files |
| **Procedural memory** | Production rules, model parameters |
| **Summary memory** | LLM-generated summary (compressed text) |
| **Profile / persona memory** | Key-value store, files |
| **Reflection memory** | Vector store, files, document store |
| **Hierarchical / tiered memory** | Multiple data structures in tiers (window → scored list → vector store → files) |
| **Unified / scored memory** | Scored list / priority queue |
| **Shared / collaborative memory** | Files, document store, knowledge graph |
| **Latent memory** | KV cache, activation snapshots |
| **Parametric memory** | Model parameters (weights) |

---

## Sources

- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
- [Rethinking Memory in AI: Taxonomy, Operations, Topics (arXiv:2505.00675)](https://arxiv.org/html/2505.00675v2)
- [MemOS: A Memory OS for AI System (arXiv:2507.03724)](https://arxiv.org/abs/2507.03724)
- [Mem0: Building Production-Ready AI Agents (arXiv:2504.19413)](https://arxiv.org/abs/2504.19413)
- [Comparing File Systems and Databases for AI Agent Memory (Oracle)](https://blogs.oracle.com/developers/comparing-file-systems-and-databases-for-effective-ai-agent-memory-management)
- [AI Agents: Memory Systems and Graph Database Integration (FalkorDB)](https://www.falkordb.com/blog/ai-agents-memory-systems/)
- [SHIMI: Semantic Hierarchical Memory Index (arXiv:2504.06135)](https://arxiv.org/abs/2504.06135)
- All related research docs in this directory (see `00_overview_and_taxonomy.md` for index)
