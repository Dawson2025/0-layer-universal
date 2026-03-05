---
resource_id: "94c41d63-7b6a-423e-8ac4-190cf905a540"
resource_type: "output"
resource_name: "25_ai_agent_implementations_per_memory_type"
---
# AI Agent Implementations Per Memory Type

## Purpose

This document catalogs the **concrete data structures and methods** used in modern AI agent systems for episodic, time-based, and procedural memory. While doc 24 covers biological/neuroscience structures, this document maps how those concepts are realized in production AI systems with specific technologies, frameworks, and code patterns.

---

## 1. Episodic Memory in AI Agents

Episodic memory is the most actively developed area for AI agents, enabling them to learn from their own experiences.

### 1.1 Vector Database + Embedding Storage

The **dominant approach** uses vector databases with embedding-based retrieval.

| Component | Implementation |
|-----------|---------------|
| **Encoding** | Each episode encoded as a vector embedding (typically from a transformer model) |
| **Storage** | Specialized vector databases: FAISS, Pinecone, Weaviate, ChromaDB, Redis |
| **Metadata** | Timestamp, entities involved, actions taken, outcomes, context |
| **Retrieval** | k-nearest neighbor (kNN) search for semantic similarity |

**Retrieval mechanism**: Semantic similarity matching finds conceptually related experiences even when surface details differ. Query like "What happened when I tried X?" retrieves the top-k most similar episodes.

```python
class EpisodicMemoryAgent:
    def __init__(self):
        self.memory = []
        self.vector_store = FAISS()

    def store_episode(self, context, action, outcome):
        embedding = embed(context + action + outcome)
        episode = {
            'timestamp': now(),
            'context': context,
            'action': action,
            'outcome': outcome,
            'embedding': embedding
        }
        self.memory.append(episode)
        self.vector_store.add(embedding)
```

### 1.2 Time-Indexed Logs

Many systems use **timestamped append-only logs**.

| Property | Description |
|----------|-------------|
| **Structure** | Time-ordered entries: `{timestamp, state, action, reward, next_state}` |
| **Organization** | Chronological for efficient range queries |
| **Key advantage** | Supports temporal queries: "What happened in the last 50 interactions?" or "Show me yesterday's conversation" |

### 1.3 Key-Value Stores with Temporal Metadata

Dictionary-style storage with rich metadata:

- **Keys**: Episode identifiers or context hashes
- **Values**: Full episode details (state, action, outcome, reasoning trace)
- **Metadata**: Timestamp, importance score, entities, tags
- **Retrieval**: Query by time range, entity, or similarity

### 1.4 Graph-Based Episode Storage

More sophisticated systems use **temporal knowledge graphs**:

- **Nodes** represent events, entities, or states
- **Edges** represent temporal relationships ("before", "caused", "part_of")
- **Temporal validity** attached to facts: "This was true from T1 to T2"
- **Advantage**: Supports complex queries like "What caused X?" and handles fact updates/invalidations

### 1.5 Two-Stage Episode Extraction (AWS Bedrock AgentCore)

Amazon's AgentCore uses a **two-stage extraction + reflection** system:

| Stage | What Happens |
|-------|-------------|
| **Stage 1: Raw Capture** | Stores complete reasoning paths, tool calls, and outcomes (full "experience" not just I/O) |
| **Stage 2: Processing** | Extracts key insights and patterns, adds semantic tags and categorizations |
| **Stage 3: Reflection** | Generates learnings: "What worked? What failed? Why?" — stored alongside raw episode |

### 1.6 Selective / Sparse Storage

To avoid overwhelming storage, many agents use **significance filtering**:

| Filter Criterion | Description |
|-----------------|-------------|
| **Prediction error threshold** | Only store experiences where outcome was surprising |
| **Novelty detection** | Store only new or rare situations |
| **Explicit importance** | User-marked or outcome-based importance (high reward/penalty) |
| **Event boundaries** | Store when context significantly changes |

This mimics how human brains prioritize unusual or emotionally significant events.

---

## 2. Time-Based Memory in AI Agents

Time-based memory is less explicitly separated in AI systems but appears in several forms.

### 2.1 Sliding Window Buffers

The simplest temporal structure — a **fixed-size FIFO buffer**:

| Property | Description |
|----------|-------------|
| **Structure** | Maintains last N interactions in order |
| **Mechanism** | New entries push out oldest entries |
| **Maps to** | LLM context window management |
| **Use case** | Short-term conversational coherence |

### 2.2 Temporal Context Vectors

Some systems implement **gradually updating context representations**, directly inspired by the biological Temporal Context Model (doc 24):

```python
context_t = alpha * new_input + (1 - alpha) * context_(t-1)
```

This creates a "temporal fingerprint" that changes smoothly, enabling "when" retrieval by matching context similarity.

### 2.3 Time-Series Databases

For production agents handling high-volume interactions:

| Database | Optimized For |
|----------|---------------|
| **InfluxDB** | Time-range queries, aggregations |
| **TimescaleDB** | PostgreSQL-compatible time-series |

Supports queries like "last 24 hours", "between dates X and Y", and aggregations like "How many times did event X occur this week?"

### 2.4 Temporal Validity Tracking

Advanced systems track **when facts are true**:

```python
{
    'fact': "User's job is Software Engineer",
    'valid_from': '2024-01-01',
    'valid_until': '2025-06-15',  # Changed jobs
}
{
    'fact': "User's job is Product Manager",
    'valid_from': '2025-06-15',
    'valid_until': None  # Current
}
```

Prevents agents from using outdated information and supports "what was true then vs now" queries.

### 2.5 Hierarchical Time Buckets

Some systems organize episodes into **temporal hierarchies** with progressive summarization:

| Bucket | Scope | Detail Level |
|--------|-------|-------------|
| **Recent** | Last hour | High detail (full content) |
| **Short-term** | Last day | Medium detail (key points) |
| **Long-term** | Last month+ | Summarized (patterns only) |

Balances recency bias with long-term pattern retention.

---

## 3. Procedural Memory in AI Agents

Procedural memory is gaining significant attention as the memory type that enables agents to "get better with practice."

### 3.1 Mem^p Framework (Distilled Trajectory Stores)

The most advanced approach stores procedural memory at **two granularities**:

**Fine-grained (Trajectory-level):**
- Complete step-by-step execution traces stored verbatim
- Format: `[(state_1, action_1, observation_1), (state_2, action_2, observation_2), ...]`
- Each trajectory is a successful task completion path
- Stored with vector embeddings for similarity-based retrieval

**Coarse-grained (Script-level):**
- High-level abstractions extracted from trajectories
- Generalized procedures: "To heat an item: locate item -> place in heating device -> activate for appropriate duration"
- Better for generalization to new but similar tasks

**Proceduralization (Combined):**
- Stores the abstract script alongside concrete example trajectories
- Achieves maximum effectiveness — the best-performing approach in benchmarks

**Performance impact (Mem^p benchmarks):**

| Metric | Without Procedural Memory | With Procedural Memory |
|--------|--------------------------|----------------------|
| Success rate (TravelPlanner) | 71.93% | **79.94%** (+8 pts) |
| Average steps | 17.84 | **14.62** (-18%) |
| Transfer learning | N/A | GPT-4o procedures boost Qwen-14B by 5% |

### 3.2 Production Rules / Rule-Based Systems

The classic AI approach using **IF-THEN production rules**:

```
IF (user asks for weather) AND (location known)
THEN (call weather API with location)
```

- Stored in rule databases where each rule is indexed
- Retrieval via pattern matching: current state matched against rule conditions
- Used in cognitive architectures like ACT-R and Soar

### 3.3 Skill Libraries / Tool Registries

Modern agents store procedural knowledge as **callable skills or tools**:

```python
skill_registry = {
    'web_search': {
        'function': search_function,
        'description': 'Search the web for information',
        'when_to_use': 'User asks factual question',
        'examples': [...]
    },
    'file_analysis': {
        'function': analyze_file,
        'description': 'Analyze uploaded files',
        'when_to_use': 'User uploads document',
        'examples': [...]
    }
}
```

Each skill contains: executable code/function, natural language description, usage conditions/triggers, and example invocations.

### 3.4 Hierarchical Chunk Structures

Complex procedures broken into **nested chunks**:

```
High-level skill: "Book travel"
+-- Mid-level chunk: "Search flights"
|   +-- Low-level: "Open booking site"
|   +-- Low-level: "Enter dates"
|   +-- Low-level: "Compare prices"
+-- Mid-level chunk: "Reserve hotel"
+-- Mid-level chunk: "Create itinerary"
```

Mimics how humans automatize complex skills through practice.

### 3.5 LangMem Framework

A practical framework implementing procedural memory with distillation:

```python
from langmem import ProceduralMemory

proc_memory = ProceduralMemory()

# Agent performs task
trajectory = agent.execute_task("book_flight")

# If successful, distill into procedure
if trajectory.success:
    procedure = proc_memory.distill(
        trajectory,
        abstraction_level="script"  # or "trajectory"
    )
    proc_memory.store(procedure)

# Later, retrieve for similar task
relevant_procedure = proc_memory.retrieve(
    "book_hotel",  # Similar to "book_flight"
    top_k=1
)

# Use retrieved procedure as context
agent.execute_with_prior(relevant_procedure)
```

### 3.6 Procedural Memory Update Strategies

Unlike episodic memory which simply accumulates, procedural memory has **sophisticated update mechanisms**:

| Strategy | Description |
|----------|-------------|
| **Vanilla Addition** | Append new successful procedures |
| **Validation Filtering** | Only store procedures exceeding success threshold (reward > 0.8) |
| **Reflection/Adjustment** | When a retrieved procedure fails, combine error with original and revise in-place |
| **Dynamic Discarding** | Remove outdated or low-performing procedures based on usage frequency and success rate |

**Update formula**: `M(t+1) = Add(M_new) - Remove(M_obsolete) + Update(M_existing)`

---

## 4. Memory Architecture Integration Cycle

Modern AI agents coordinate these memory types in a **unified architecture**:

```
Working Memory (context window)
    | consolidate significant events
    v
Episodic Memory (vector DB + time index)
    | extract patterns/rules
    v
Semantic Memory (knowledge graph/facts)
    ^ retrieve for context
    |
Working Memory (next interaction)
```

**Flow**:
1. Agent interacts with user (working memory)
2. Conversation stored as episode in vector DB with timestamp
3. If significant, episode triggers consolidation into semantic facts
4. Next query retrieves relevant episodes via similarity + time range
5. Retrieved episodes + semantic facts loaded into working memory

---

## 5. Implementation Patterns Summary

| Memory Type | Primary Data Structure | Retrieval Method | Used For |
|-------------|----------------------|------------------|----------|
| **Episodic** | Vector database (FAISS, Pinecone) | kNN similarity search | "What happened when..." |
| **Episodic** | Time-indexed log | Temporal range queries | "Show last 50 messages" |
| **Episodic** | Key-value store with metadata | Hash lookup + filtering | "Find episode X" |
| **Time-Based** | Sliding window buffer | Direct array access | Recent context |
| **Time-Based** | Temporal validity annotations | Time range filtering | "What was true when" |
| **Time-Based** | Time-series database | Optimized time queries | Event timelines |
| **Procedural** | Distilled trajectories (Mem^p) | Task similarity matching | "How to do X" |
| **Procedural** | Production rules | Pattern matching | Condition-action triggers |
| **Procedural** | Skill libraries | Name/description lookup | Tool selection |

### Key Insight

AI agents use **hybrid storage** — vector databases for semantic similarity (episodic), time-series structures for temporal ordering (time-based), skill registries and trajectory stores for procedures (procedural), and knowledge graphs for facts (semantic). Unlike human memory which integrates these in neural tissue, AI systems keep them architecturally separate but coordinate during retrieval.

Procedural memory is the most actively **learned and refined** type: while episodic memory passively records experiences and semantic memory stores static facts, procedural memory has dynamic update mechanisms that improve procedures based on successes and failures.

---

## Cross-References

- **Biological data structures (neuroscience basis)**: `24_biological_data_structures_per_memory_type.md`
- **Memory type hierarchy**: `21_core_memory_structure_hierarchy.md`
- **Data structure hierarchy (computational)**: `22_core_data_structure_hierarchy.md`
- **AI memory system tiers**: `23_core_ai_memory_systems.md`
- **Cognitive science foundations**: `01_cognitive_science_foundations.md`

---

## Sources

- [Episodic Memory in AI Agents (GeeksforGeeks)](https://www.geeksforgeeks.org/artificial-intelligence/episodic-memory-in-ai-agents/)
- [AWS Bedrock AgentCore Episodic Memory](https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)
- [Episodic Memory in AI (DigitalOcean)](https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai)
- [Beyond Short-Term Memory: 3 Types of Long-Term Memory AI Agents Need (ML Mastery)](https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/)
- [Build Smarter AI Agents with Redis Memory](https://redis.io/blog/build-smarter-ai-agents-manage-short-term-and-long-term-memory-with-redis/)
- [Building AI Agents with Persistent Memory (TigerData)](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach)
- [Long-Term Memory: Unlocking Smarter Agents (AI Practitioner)](https://aipractitioner.substack.com/p/long-term-memory-unlocking-smarter-38d)
- [Selective Memory Storage in AI (PMC11449156)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11449156/)
- [Agent Memory (MongoDB)](https://www.mongodb.com/resources/basics/artificial-intelligence/agent-memory)
- [Agent Memory: Why Your AI Has Amnesia (Oracle)](https://blogs.oracle.com/developers/agent-memory-why-your-ai-has-amnesia-and-how-to-fix-it)
- [AWS AgentCore Long-Term Memory Deep Dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Mem^p: Procedural Memory for AI Agents (arXiv:2508.06433)](https://arxiv.org/html/2508.06433v2)
- [How Procedural Memory Can Cut Cost and Complexity of AI Agents (VentureBeat)](https://venturebeat.com/ai/how-procedural-memory-can-cut-the-cost-and-complexity-of-ai-agents)
- [Procedural Knowledge (ScienceDirect)](https://www.sciencedirect.com/topics/computer-science/procedural-knowledge)
- [Defining the Autonomous Enterprise (Unstructured.io)](https://unstructured.io/blog/defining-the-autonomous-enterprise-reasoning-memory-and-the-core-capabilities-of-agentic-ai)
- [Agent Skills (Thesys)](https://www.thesys.dev/blogs/agent-skill)
- [Building a Procedural Memory Agent (TechLing)](https://techling.ai/blog/a-coding-guide-to-build-a-procedural-memory-agent/)
- [LangMem Procedural Memory (YouTube)](https://www.youtube.com/watch?v=WW-v5mO2P7w)
