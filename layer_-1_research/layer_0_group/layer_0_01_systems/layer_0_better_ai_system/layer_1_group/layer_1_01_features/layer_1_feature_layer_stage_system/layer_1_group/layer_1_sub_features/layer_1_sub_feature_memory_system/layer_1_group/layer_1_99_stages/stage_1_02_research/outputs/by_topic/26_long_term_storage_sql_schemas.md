---
resource_id: "1c4a055f-311a-43b2-ac68-0dd82eaa25f3"
resource_type: "output"
resource_name: "26_long_term_storage_sql_schemas"
---
# Long-Term Storage Architecture: SQL Schemas

## Purpose

This document presents the complete SQL schema designs for persistent long-term memory storage across all four memory types (semantic, episodic, time-based, procedural), the 4-stage consolidation pipeline that populates them, the unified PostgreSQL architecture that houses them, and performance benchmarks from production systems.

---

## 1. Semantic Memory SQL

### Vector Database (pgvector)

The dominant approach for persistent semantic memory uses pgvector to store embeddings as native PostgreSQL column types with specialized indexing for similarity search.

```sql
CREATE TABLE semantic_memory (
    id UUID PRIMARY KEY,
    embedding VECTOR(1536),  -- pgvector type
    content TEXT,
    entity TEXT,
    fact_type VARCHAR(50),
    created_at TIMESTAMP,
    last_accessed TIMESTAMP,
    confidence_score FLOAT
);

CREATE INDEX ON semantic_memory USING diskann (embedding);  -- DiskANN for scale
```

Key characteristics:
- Embeddings stored as fixed-length float arrays via the pgvector extension
- DiskANN index enables disk-optimized graph-based similarity search (471 QPS at 99% recall on 50M vectors)
- Semantic similarity search finds related facts even with different phrasing
- Alternative index types include IVFFlat (cluster-based) and HNSW (multi-layer graph)

### Knowledge Graph Schema

For explicit entity relationships, knowledge graphs are represented as relational adjacency lists:

```sql
CREATE TABLE entities (
    id UUID PRIMARY KEY,
    name TEXT,
    type VARCHAR(50)
);

CREATE TABLE relationships (
    id UUID PRIMARY KEY,
    source_id UUID REFERENCES entities(id),
    target_id UUID REFERENCES entities(id),
    relationship_type VARCHAR(100),
    properties JSONB
);
```

This stores graph structure using foreign keys, which effectively creates adjacency lists. Graph traversal is performed via recursive CTEs (see doc 27 for details).

### Hybrid PostgreSQL (Unified Semantic)

Modern systems consolidate vectors and knowledge graphs in one PostgreSQL database:
- 66% cost reduction vs multi-database approach
- Single-query joins across all memory types
- ACID transactions ensure consistency
- One backup strategy, one connection pool

---

## 2. Episodic Memory SQL

### Hypertable with Vector Extensions (TimescaleDB)

Episodic memory requires both temporal ordering and semantic search, combining time-series partitioning with vector similarity:

```sql
CREATE TABLE episodes (
    id UUID,
    user_id UUID,
    timestamp TIMESTAMPTZ NOT NULL,
    context TEXT,
    action TEXT,
    outcome TEXT,
    embedding VECTOR(1536),  -- For semantic retrieval
    entities TEXT[],
    emotional_valence FLOAT,
    importance_score FLOAT
);

-- Convert to hypertable for time-based partitioning
SELECT create_hypertable('episodes', 'timestamp');

-- Indexes for hybrid retrieval
CREATE INDEX ON episodes USING diskann (embedding);  -- Semantic
CREATE INDEX ON episodes (user_id, timestamp DESC);  -- Temporal
```

Query capabilities:
- Temporal range: `WHERE timestamp > now() - interval '7 days'`
- Semantic: `ORDER BY embedding <=> query_vector LIMIT 5`
- Combined: filter by time window, then rank by semantic similarity

### Scene-Based Grouping (SQLite)

For self-organizing memory systems that group interactions into coherent scenes:

```sql
CREATE TABLE scenes (
    scene_id INTEGER PRIMARY KEY,
    user_id TEXT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    summary TEXT,
    key_entities TEXT,
    consolidated BOOLEAN DEFAULT FALSE
);

CREATE TABLE interactions (
    interaction_id INTEGER PRIMARY KEY,
    scene_id INTEGER REFERENCES scenes(scene_id),
    timestamp TIMESTAMP,
    user_message TEXT,
    agent_response TEXT,
    extracted_facts TEXT
);
```

Consolidation process:
- Raw interactions stored in real-time
- Background process groups interactions into "scenes" (conversation segments)
- Scenes get summarized and consolidated
- Old raw interactions can be compressed or archived

---

## 3. Time-Based Memory SQL

### Hypertables (TimescaleDB)

Purpose-built for time-series data with automatic partitioning:

```sql
CREATE TABLE temporal_events (
    event_id UUID,
    timestamp TIMESTAMPTZ NOT NULL,
    event_type VARCHAR(50),
    temporal_context JSONB,  -- Stores TCM vector or time cell state
    sequence_position INTEGER,
    duration_ms INTEGER
);

SELECT create_hypertable('temporal_events', 'timestamp',
    chunk_time_interval => INTERVAL '1 day');
```

Features:
- Automatic data retention policies
- Continuous aggregates for summaries
- Compression for older data

### Temporal Validity Tracking

For facts that change over time, tracking when each fact was valid:

```sql
CREATE TABLE temporal_facts (
    fact_id UUID PRIMARY KEY,
    entity_id UUID,
    attribute VARCHAR(100),
    value TEXT,
    valid_from TIMESTAMPTZ NOT NULL,
    valid_until TIMESTAMPTZ,  -- NULL = currently valid
    superseded_by UUID REFERENCES temporal_facts(fact_id)
);

-- Query what was true at a specific point in time
SELECT * FROM temporal_facts
WHERE entity_id = ?
  AND valid_from <= '2025-06-15'
  AND (valid_until IS NULL OR valid_until > '2025-06-15');
```

This enables temporal queries like "what did we know about entity X as of date Y?" and tracks the supersession chain when facts are updated.

---

## 4. Procedural Memory SQL

### Trajectory Store with Metadata

Stores complete execution paths with success metrics for learned procedures:

```sql
CREATE TABLE procedures (
    procedure_id UUID PRIMARY KEY,
    task_description TEXT,
    trajectory JSONB,  -- Full step-by-step sequence
    script TEXT,       -- High-level abstracted procedure
    embedding VECTOR(1536),  -- For similarity search
    success_rate FLOAT,
    avg_execution_time_ms INTEGER,
    times_used INTEGER,
    last_used TIMESTAMP,
    created_at TIMESTAMP
);
```

Example trajectory format in JSONB:

```json
{
  "steps": [
    {"state": "initial", "action": "open_browser", "observation": "browser_open"},
    {"state": "browser_open", "action": "navigate_to('booking.com')", "observation": "page_loaded"},
    {"state": "page_loaded", "action": "search_flights('NYC', 'LAX')", "observation": "results_shown"}
  ],
  "outcome": "success",
  "reward": 0.95
}
```

### Skill Registry and Invocation Tracking

For callable functions and tools with usage analytics:

```sql
CREATE TABLE skills (
    skill_id UUID PRIMARY KEY,
    skill_name VARCHAR(100) UNIQUE,
    description TEXT,
    function_code TEXT,  -- Or reference to code file
    parameters JSONB,
    when_to_use TEXT,
    examples JSONB,
    usage_count INTEGER DEFAULT 0,
    success_rate FLOAT,
    avg_latency_ms INTEGER
);

CREATE TABLE skill_invocations (
    invocation_id UUID PRIMARY KEY,
    skill_id UUID REFERENCES skills(skill_id),
    timestamp TIMESTAMPTZ,
    input_params JSONB,
    output JSONB,
    success BOOLEAN,
    execution_time_ms INTEGER
);
```

The `skill_invocations` table provides a feedback loop: track which skills succeed, how fast they run, and what inputs they handle, enabling the system to improve skill selection over time.

---

## 5. Four-Stage Consolidation Pipeline

Production systems implement a four-stage pipeline to move raw interactions into persistent long-term memory:

### Stage 1: Extraction (~20-40 seconds)

Identify what is worth remembering from raw interactions. An LLM extracts meaningful information (facts, preferences, insights) while ignoring filler content. Extraction time is approximately 20-40 seconds for standard conversations.

### Stage 2: Consolidation (LLM-powered)

Merge related information and resolve conflicts. The system:
1. Finds related existing memories via vector similarity search (top-k)
2. Uses an LLM to decide: merge (same fact, different phrasing), update (supersede old fact), or store as new
3. Produces a deduplicated, coherent knowledge base

### Stage 3: Storage (PostgreSQL)

Persist to the appropriate table with proper indexes:

```sql
-- Semantic memory insertion
INSERT INTO semantic_memory (embedding, content, entity, created_at)
VALUES (?, ?, ?, NOW());

-- Episodic memory insertion
INSERT INTO episodes (timestamp, context, action, embedding)
VALUES (NOW(), ?, ?, ?);
```

### Stage 4: Retrieval (~200ms)

Fetch relevant memories for the current context using hybrid retrieval:

```sql
-- Hybrid retrieval: semantic + temporal + filtering
SELECT content FROM semantic_memory
WHERE user_id = ?
ORDER BY embedding <=> ?
LIMIT 3;

SELECT context, action FROM episodes
WHERE user_id = ?
  AND timestamp > NOW() - INTERVAL '7 days'
ORDER BY embedding <=> ?
LIMIT 5;
```

Retrieval latency is approximately 200ms for semantic search operations.

---

## 6. Unified PostgreSQL Architecture

Modern production systems consolidate all memory types in a single PostgreSQL database:

```sql
-- Semantic memory
CREATE TABLE semantic_facts (
    id UUID PRIMARY KEY,
    content TEXT,
    embedding VECTOR(1536),
    created_at TIMESTAMPTZ
);

-- Episodic memory (hypertable for time-series)
CREATE TABLE episodes (
    id UUID,
    timestamp TIMESTAMPTZ NOT NULL,
    content TEXT,
    embedding VECTOR(1536)
);
SELECT create_hypertable('episodes', 'timestamp');

-- Procedural memory
CREATE TABLE procedures (
    id UUID PRIMARY KEY,
    task TEXT,
    trajectory JSONB,
    embedding VECTOR(1536),
    success_rate FLOAT
);

-- Single query joins all memory types
SELECT
    s.content as semantic_knowledge,
    e.content as recent_episodes,
    p.trajectory as relevant_procedures
FROM semantic_facts s
CROSS JOIN LATERAL (
    SELECT * FROM episodes
    WHERE timestamp > NOW() - INTERVAL '7 days'
    ORDER BY embedding <=> s.embedding LIMIT 3
) e
LEFT JOIN procedures p ON p.embedding <=> s.embedding < 0.2
WHERE s.embedding <=> query_embedding < 0.3
LIMIT 10;
```

Benefits of the unified approach:
- Single transaction across all memory types (ACID guarantees)
- One backup/restore strategy
- 66% infrastructure cost reduction vs multi-database
- No network hops between databases
- Cross-type JOINs in a single query

---

## 7. Performance Benchmarks

### Mem0 Long-Term Memory System
- 91% lower p95 latency vs full-context prompting
- 90% token reduction
- Scales to hundreds of sessions without re-reading history

### PostgreSQL Unified Approach (pgvector/pgvectorscale)
- 471 QPS at 99% recall on 50M vectors
- Competitive with specialized vector databases
- ACID guarantees for consistency

### Key Insight

Long-term memory is not about better algorithms -- it is about persistent storage with hybrid retrieval combining semantic similarity (vectors), temporal ordering (hypertables), and relational constraints (PostgreSQL) in a unified system that survives restarts and scales to production workloads.

---

## Cross-References

- **Core data structure hierarchy**: `22_core_data_structure_hierarchy.md`
- **AI memory system tiers**: `23_core_ai_memory_systems.md`
- **How vectors, graphs, and SQL nest together**: `27_core_structures_nesting_analysis.md`
- **Memory type hierarchy (biological buildup)**: `21_core_memory_structure_hierarchy.md`

---

## Sources

- [Mem0: Long-Term Memory for AI Agents](https://mem0.ai/blog/long-term-memory-ai-agents)
- [Redis: AI Agent Memory for Stateful Systems](https://redis.io/blog/ai-agent-memory-stateful-systems/)
- [TigerData: Building AI Agents with Persistent Memory](https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach)
- [IBM: AI Agent Memory](https://www.ibm.com/think/topics/ai-agent-memory)
- [MarkTechPost: Self-Organizing Agent Memory System](https://www.marktechpost.com/2026/02/14/how-to-build-a-self-organizing-agent-memory-system-for-long-term-ai-reasoning/)
- [Procedural Memory in AI Agents (arXiv:2508.06433)](https://arxiv.org/html/2508.06433v2)
- [TheSys: Agent Skills](https://www.thesys.dev/blogs/agent-skill)
- [AWS: AgentCore Long-Term Memory Deep Dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [CloudThat: AI Agents with Long-Term Memory in Amazon Bedrock](https://www.cloudthat.com/resources/blog/building-smarter-ai-agents-with-long-term-memory-in-amazon-bedrock/)
- [Memory in the Age of AI Agents (arXiv:2512.13564)](https://arxiv.org/abs/2512.13564)
