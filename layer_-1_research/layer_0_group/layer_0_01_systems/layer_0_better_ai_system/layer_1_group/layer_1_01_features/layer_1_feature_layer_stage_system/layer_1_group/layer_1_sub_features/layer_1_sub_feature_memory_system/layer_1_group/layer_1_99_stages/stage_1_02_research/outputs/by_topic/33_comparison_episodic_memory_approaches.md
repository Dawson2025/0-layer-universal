---
resource_id: "d8bcdcec-71b6-417b-83d0-0d08fc077d8e"
resource_type: "output"
resource_name: "33_comparison_episodic_memory_approaches"
---
# Comparison: Episodic Memory Approaches

## Purpose

This document compares the user's file-based episodic memory system (`.0agnostic/04_episodic_memory/` with session files, index.md, divergence.log, and episodic-sync.sh) against research and commercial approaches to episodic memory: vector DB episodes, time-indexed logs, scene-based grouping, AWS Bedrock two-stage extraction, and MongoDB cognitive dynamics.

---

## 1. Overview of User's Episodic Memory System

### How It Works

The user's episodic memory lives in `.0agnostic/04_episodic_memory/` directories at every entity and stage level in the layer-stage hierarchy. The structure uses two subdirectories:

- **`sessions/`**: Individual session records — one file per work session
- **`changes/`**: Records of modifications to outputs or shared state

### Session Files

After significant work, agents create a session file in `sessions/` containing:
- **Date**: When the session occurred
- **What was done**: Summary of work performed
- **Files changed**: List of added, modified, or removed files
- **Decisions made**: Key choices and their rationale

These are plain markdown files, created manually by the agent at session end.

### Index and Aggregation

- **`index.md`**: A manually maintained index at each entity's `outputs/episodic/` directory that summarizes recent sessions, enabling quick resumption of multi-session work
- **`divergence.log`**: Updated when shared outputs are modified, tracking what changed and when so concurrent agents can detect conflicts
- **`episodic-sync.sh`**: A script at `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` that aggregates episodic session files across the hierarchy into a single `memory/episodic.md` auto-memory topic file at `~/.claude/projects/<project>/memory/`

### Key Properties

- **Human-readable**: All session records are markdown
- **Agent-agnostic**: Works with any AI tool (Claude, Gemini, GPT, Cursor)
- **Git-versioned**: Session files are tracked in the repository
- **Hierarchically scoped**: Each entity maintains its own episodic memory
- **No database dependency**: Pure filesystem
- **Manual creation**: Agents must explicitly write session records; nothing is automatic

---

## 2. Overview of Research/Commercial Episodic Memory Systems

### Vector DB Episodes (FAISS, ChromaDB)

Vector database episodic memory stores each episode as an embedding vector alongside metadata (timestamp, participants, outcome). Retrieval uses semantic similarity: given a current context, the system finds past episodes that are most semantically similar.

**How it works**:
1. At the end of each interaction, the system embeds the episode content using a language model
2. The embedding is stored in FAISS or ChromaDB with metadata tags
3. On retrieval, the current query is embedded and compared against stored episodes via approximate nearest neighbor search
4. Top-k most similar episodes are returned, typically with their full content

**Example (Self-Healing Codebase from GenAI_Agents)**:
ChromaDB stores bug patterns as episodes. When a new error occurs, the system searches for similar past bugs and retrieves the fixes that worked. Each episode contains the error description, the solution code, and a timestamp.

**Strengths**: Fast semantic retrieval, automatic relevance ranking, handles large volumes
**Weaknesses**: Opaque (no human-readable records), requires embedding infrastructure, no inherent temporal ordering

### Time-Indexed Logs (InfluxDB, TimescaleDB)

Time-series databases store episodes as time-ordered records with automatic partitioning by time range. Retrieval is primarily temporal: "what happened in the last hour/day/week" or "what happened between these two timestamps."

**How it works**:
1. Each event is stored with a precise timestamp and structured metadata
2. The database automatically partitions data into time-based chunks (hypertables in TimescaleDB)
3. Queries filter by time range, then optionally by metadata fields
4. Aggregation functions (count, average, percentile) operate efficiently over time windows

**Strengths**: Optimal for temporal queries, automatic time partitioning, efficient aggregation, handles high write throughput
**Weaknesses**: No semantic understanding, requires structured schemas, no similarity-based retrieval

### Scene-Based Grouping (SQLite)

Scene-based episodic memory groups interactions into coherent "scenes" or episodes based on context boundaries (topic changes, time gaps, participant changes). Used in systems like CrewAI's long-term memory (SQLite3 backend).

**How it works**:
1. The system monitors interaction flow for episode boundaries (topic shift, long pause, new participants)
2. Related interactions are grouped into a single scene/episode record
3. Each scene gets a summary, participant list, and outcome
4. Retrieval queries the scene database by topic, participants, or outcome

**CrewAI implementation**: Short-term memory (current session RAG), long-term memory (SQLite3 for persistent scene records), entity memory (RAG for tracking entities across scenes), contextual memory (maintains conversation coherence).

**Strengths**: Natural grouping of related events, compact storage, clear episode boundaries
**Weaknesses**: Boundary detection is imperfect, loses fine-grained detail within scenes, requires boundary-detection logic

### AWS Bedrock Two-Stage Extraction

AWS's AgentCore implements a two-stage memory consolidation pipeline that separates extraction from storage.

**How it works**:
1. **Stage 1 (Extraction)**: An LLM reviews recent interactions and extracts what is worth remembering — key facts, decisions, user preferences, task outcomes
2. **Stage 2 (Consolidation)**: Extracted memories are compared against existing memories. The LLM decides: merge (combine with existing), update (replace outdated), or keep separate (new information)
3. Consolidated memories are stored with importance scores and timestamps
4. Retrieval combines semantic similarity with importance weighting

**Used in OASIS (AWS sample)**:
OpenSearch stores three categories: raw events (episodic), system metrics (time-series), and agent findings (semantic + procedural). Status transitions track episode lifecycle: initial_detection -> analysis_complete -> pending_approval -> approved -> mitigated.

**Strengths**: Intelligent extraction (only stores what matters), automatic conflict resolution, importance-based prioritization
**Weaknesses**: LLM-dependent (extraction quality varies), adds latency, expensive (requires LLM calls per interaction)

### MongoDB Cognitive Dynamics (Decay, Reinforcement, Merging)

MongoDB AI Memory Service implements biologically-inspired dynamics where episodic memories are living entities that change over time.

**How it works**:
1. **Storage**: Memories are stored with importance scores (0.0-1.0) and vector embeddings
2. **Decay**: A `DECAY_FACTOR` (e.g., 0.99) reduces importance scores over time — unused memories gradually fade
3. **Reinforcement**: When a concept is re-encountered, its `REINFORCEMENT_FACTOR` (e.g., 1.1) increases the importance score — frequently referenced memories grow stronger
4. **Merging**: Memories above a `SIMILARITY_THRESHOLD` (e.g., 0.7) are merged into consolidated records
5. **Pruning**: Memories below a minimum importance threshold are removed entirely
6. **Depth limit**: `MAX_DEPTH` caps the number of active memories per user

**Strengths**: Mimics biological memory behavior, automatically prioritizes important memories, prevents unbounded growth
**Weaknesses**: Tuning parameters is difficult, decay can remove important but infrequently accessed memories, merging can lose nuance

---

## 3. Comparison Table

| Dimension | User's System | Vector DB (FAISS/ChromaDB) | Time-Series (InfluxDB/TimescaleDB) | Scene-Based (SQLite) | AWS Bedrock Two-Stage | MongoDB Cognitive |
|-----------|--------------|---------------------------|-----------------------------------|--------------------|----------------------|-------------------|
| **Storage format** | Markdown files | Vector embeddings + metadata | Structured time-indexed rows | SQLite records | Vector + structured | MongoDB documents + vectors |
| **Episode creation** | Manual (agent writes at session end) | Automatic (embed every interaction) | Automatic (timestamp on ingest) | Automatic (boundary detection) | Automatic (LLM extraction) | Automatic (on interaction) |
| **Retrieval method** | Read `index.md` or navigate to session files | Semantic similarity (k-NN) | Time-range queries | Scene lookup by topic/participant | Similarity + importance weighting | Similarity + importance + recency |
| **Temporal ordering** | Implicit (file dates, date in content) | Metadata-only (not primary) | Native (primary dimension) | Scene-level (not fine-grained) | Metadata timestamps | Metadata timestamps |
| **Memory decay** | None | None | Retention policies (TTL) | None | None | Automatic decay factor |
| **Memory reinforcement** | None | None | None | None | Consolidation updates | Automatic reinforcement factor |
| **Memory consolidation** | Manual (`episodic-sync.sh` aggregates) | None (append-only) | Downsampling | Scene summaries | LLM-driven merge/update/keep | Automatic merging above threshold |
| **Human readability** | Full (plain markdown) | None (vectors are opaque) | Low (structured rows) | Low (DB records) | Low (API access) | Low (DB records) |
| **Cross-session continuity** | `index.md` + `divergence.log` | Persistent vector store | Continuous time-series | Persistent scene DB | Persistent memory store | Persistent + dynamic |
| **Multi-agent awareness** | `divergence.log` detects conflicts | Shared vector store | Shared time-series | Shared DB | Shared extraction | Shared memory pool |
| **Infrastructure needed** | None (filesystem) | Vector DB + embedding model | Time-series DB | SQLite | AWS Bedrock + OpenSearch | MongoDB Atlas |
| **Scale (episodes)** | Hundreds (file-based) | Millions (indexed) | Billions (time-partitioned) | Thousands (SQLite) | Millions (cloud) | Millions (cloud) |
| **Agent agnosticism** | Full (any AI tool) | API-dependent | API-dependent | Framework-dependent | AWS-locked | MongoDB-locked |

---

## 4. Analysis

### Where User's System Excels

**1. Simplicity and zero dependencies**
The user's system requires nothing beyond a filesystem. No vector database to configure, no embedding models to run, no cloud services to provision. A new agent session starts by reading markdown files. This is the lowest possible barrier to entry and the most portable approach — it works on any machine with a file system.

**2. Full human readability and editability**
Every session record is a markdown file that a human can read, edit, correct, or delete. When an agent makes a mistake in a session record, a human can fix it with a text editor. Vector embeddings in FAISS or ChromaDB are opaque numbers that cannot be meaningfully inspected or corrected by humans.

**3. Agent-agnostic portability**
Session files work with Claude, Gemini, GPT, Cursor, or any future AI tool. The episodic memory is not locked into any framework's memory API. Switching AI tools does not require migrating memory stores or adapting to new APIs.

**4. Git-versioned history**
Session files are tracked in git, providing a complete audit trail with branching, merging, and rollback capabilities. No commercial system provides this level of version control over episodic memory. You can see exactly when a session record was created, who created it, and what it said at any point in history.

**5. Hierarchical scoping**
Episodic memory is scoped to the entity where the work happened. Stage-level sessions stay in stage directories; entity-level sessions stay at the entity level. This prevents a global memory pool from becoming cluttered with irrelevant episodes from unrelated parts of the system.

**6. Conflict detection via divergence.log**
The `divergence.log` mechanism provides a simple but effective way for concurrent agents to detect when shared outputs have been modified. While less sophisticated than database-level conflict resolution, it is explicit, human-readable, and requires no infrastructure.

### Where User's System Falls Short

**1. No semantic retrieval**
This is the most fundamental limitation. To find a relevant past session, an agent must either know where to look (navigate to the right directory) or read the index file. If a relevant episode is in a different entity's episodic memory, the agent will not find it unless explicitly directed. Vector DB systems find relevant episodes regardless of where they are stored.

**2. No automatic episode creation**
Every session record must be manually written by the agent at session end. If the agent forgets or the session ends abruptly, the episode is lost. Commercial systems automatically capture every interaction. This means the user's system has gaps wherever manual recording was missed.

**3. No decay, reinforcement, or dynamic prioritization**
All session records have equal weight regardless of age, relevance, or frequency of access. A session from six months ago about a since-abandoned approach sits alongside yesterday's critical decision. MongoDB's cognitive dynamics automatically surface what matters and fade what does not.

**4. No automatic extraction of key facts**
AWS Bedrock's two-stage extraction uses an LLM to identify what is worth remembering. The user's system stores whatever the agent decides to write, which may miss important details or include unnecessary verbosity. There is no distillation step between raw session interaction and stored memory.

**5. Scale limitations**
As the number of sessions grows into the hundreds per entity, reading index files and navigating directory trees becomes unwieldy. Vector databases handle millions of episodes with sub-200ms retrieval. The user's system has no indexing beyond the manually maintained `index.md`.

**6. No cross-entity episode retrieval**
If an agent working on `memory_system/` needs to find a past session from `multi_agent_system/` that discussed a relevant topic, there is no mechanism to discover it. The `episodic-sync.sh` script aggregates into a single `memory/episodic.md` file, but this is a flat summary, not a searchable index.

### Potential Hybrid Improvements

**1. Automatic session capture with human review**
Add a post-session hook that uses an LLM to generate a draft session record from the conversation transcript. The draft is saved as a pending file in `sessions/drafts/`. A human reviews and approves (or edits) before the file is moved to `sessions/`. This preserves human oversight while eliminating the risk of forgotten sessions.

**2. Lightweight vector index alongside files**
Keep session files as the source of truth, but maintain a small vector index (e.g., a local ChromaDB or SQLite with embeddings) that points to file paths. When an agent needs to find relevant past sessions, it queries the vector index to get file paths, then reads the actual markdown files. The index is regenerated from files on any change, making files authoritative.

**3. Importance annotations on session records**
Add a simple importance field (high/medium/low) to session records, either assigned by the agent at creation time or updated by humans later. Retrieval prioritizes high-importance sessions. Over time, a script could automatically downgrade importance of old, unaccessed sessions — a simple form of decay.

**4. Cross-entity session index**
Extend `episodic-sync.sh` to produce a searchable index that maps topics to session file paths across all entities. Instead of a flat summary, the aggregated file would be a topic-keyed lookup table. An agent could search for "vector databases" and find relevant sessions across memory_system, multi_agent_system, and other entities.

**5. Structured session format with metadata**
Standardize session files with a YAML frontmatter block containing: date, duration, entity path, topics covered, files changed, importance, and status (active/archived). This enables programmatic querying without a database — a simple script can filter sessions by date range, topic, or importance.

**6. Time-based archival**
Implement a simple archival policy: sessions older than N months are moved from `sessions/` to `sessions/archive/`. The `index.md` retains one-line summaries of archived sessions with pointers. This keeps the active session directory manageable while preserving history. This is a manual form of the decay that MongoDB implements automatically.

---

## Sources

- [Mem0 GitHub Repository](https://github.com/mem0ai/mem0) -- vector-based memory extraction and retrieval
- [CrewAI Memory Documentation](https://docs.crewai.com/en/concepts/memory) -- scene-based grouping with SQLite backend
- [MongoDB AI Memory Service](https://github.com/mongodb-partners/ai-memory) -- cognitive dynamics (decay, reinforcement, merging)
- [AWS OASIS Agent System](https://github.com/aws-samples/sample-operational-ai-agent) -- two-stage extraction with OpenSearch
- [NirDiamant/GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents) -- self-healing codebase with ChromaDB episodic memory
- [AI Agent Memory Comparison (dev.to)](https://dev.to/foxgem/ai-agent-memory-a-comparative-analysis-of-langgraph-crewai-and-autogen-31dp) -- comparative analysis of agent memory systems
- [TimescaleDB Documentation](https://docs.timescale.com/) -- time-series hypertable architecture
- [Episodic Memory in AI (DigitalOcean)](https://www.digitalocean.com/community/tutorials/episodic-memory-in-ai) -- episodic memory implementation patterns
- [AWS AgentCore Long-Term Memory](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/) -- consolidation pipeline architecture
- Perplexity AI research conversation (Feb 2026) -- source data for system architectures
