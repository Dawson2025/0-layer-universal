---
resource_id: "8797deca-8b76-43f5-82ca-aa5f7e99bce9"
resource_type: "output"
resource_name: "36_technology_integration_roadmap"
---
# Technology Integration Roadmap: Where and How Each Technology Fits the Layer-Stage System

<!-- section_id: "77dc5d4f-789e-42c5-bf30-41d3ea010bd6" -->
## Purpose

This document maps four key technologies -- relational databases (PostgreSQL), vector embeddings (pgvector), knowledge graphs (Neo4j/SQL), and SHIMI (Semantic Hierarchical Memory Index) -- onto the specific directories, workflows, and data patterns within the user's layer-stage system. For each technology, it identifies concrete integration points across the `.0agnostic/` hierarchy, the 0AGNOSTIC.md chain, CLAUDE.md sync, skills matching, and agent delegation. The goal is a practical roadmap: not "should we use vectors?" but "where exactly would a pgvector column go, and what query would it serve?"

---

<!-- section_id: "e7051c95-2aa0-4a3d-8740-c04857ac368d" -->
## 1. User's System Architecture Summary

<!-- section_id: "372fa605-4284-4812-b289-5f32db1b26fb" -->
### The Layer-Stage Hierarchy

The system organizes AI agent context as a tree of entities, each with:
- **0AGNOSTIC.md**: Source of truth, split into STATIC (always loaded) and DYNAMIC (on-demand) halves
- **.0agnostic/**: On-demand resources in 7 numbered categories (01_knowledge through 07+_setup_dependant)
- **layer_N_group/**: Child entities and stages (01-11)
- **agnostic-sync.sh**: Generates tool-specific files (CLAUDE.md, GEMINI.md, etc.) from 0AGNOSTIC.md

<!-- section_id: "b35a6b86-f60b-4607-a1d3-572052055bbf" -->
### Key Data Patterns

| Pattern | Current Implementation | Data Characteristics |
|---------|----------------------|---------------------|
| **Context chain** | Deterministic path traversal (root to leaf) | 5-8 markdown files, read sequentially |
| **Three-tier knowledge** | Pointer -> Distilled -> Full detail | Progressive disclosure across 3 file layers |
| **Stage reports** | `outputs/reports/stage_report.md` per stage | Structured markdown with status, findings, handoff |
| **Episodic memory** | `04_episodic_memory/sessions/` and `changes/` | Session logs with dates, files changed, decisions |
| **Rules** | `02_rules/static/` and `02_rules/dynamic/` | Short markdown files with trigger conditions |
| **Skills** | `06_context_avenue_web/05_skills/SKILL.md` | WHEN/WHEN NOT conditions + instructions |
| **Agent definitions** | `.gab.jsonld` files with modes, actors, personas | JSON-LD graphs with 3-13 actors per entity |
| **Knowledge docs** | `01_knowledge/` per-topic directories | Research documents (35+ in memory_system alone) |

<!-- section_id: "f0c4c976-dd63-4ffa-9d57-76b45a3b0243" -->
### Current Retrieval Methods

- **Path-based**: Agent knows the directory, reads the file
- **Pattern-based**: `find` and `jq` commands to locate .gab.jsonld files
- **Convention-based**: Same-name matching (e.g., `layer_1.orchestrator.gab.jsonld` -> `layer_1.orchestrator.integration.md`)
- **No semantic search**: No similarity-based retrieval exists

---

<!-- section_id: "8e0de384-fe1e-49fc-be0b-a45845c5d0af" -->
## 2. Technology A: Relational Tables (PostgreSQL)

<!-- section_id: "ed91eb42-51e1-422a-a946-1b9f937ee9fc" -->
### Where It Integrates

#### 2A.1 Stage Reports Index

**Target**: All `outputs/reports/stage_report.md` files across the hierarchy

```sql
CREATE TABLE stage_reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_path TEXT NOT NULL,          -- '/layer_-1_research/.../memory_system'
    stage_number INTEGER NOT NULL,      -- 2
    stage_name VARCHAR(50) NOT NULL,    -- 'research'
    status VARCHAR(20) NOT NULL,        -- 'completed', 'active', 'empty'
    last_updated TIMESTAMPTZ,
    summary TEXT,                       -- First paragraph of report
    key_outputs JSONB,                  -- [{name, path, type}]
    handoff_notes TEXT,                 -- What next stage needs
    file_path TEXT NOT NULL             -- Absolute path to stage_report.md
);

CREATE INDEX idx_stage_reports_entity ON stage_reports(entity_path);
CREATE INDEX idx_stage_reports_status ON stage_reports(status);
```

**What it enables**: `SELECT * FROM stage_reports WHERE entity_path LIKE '%memory_system%' AND status = 'completed'` -- instantly find all completed stages for an entity without traversing the filesystem.

#### 2A.2 Entity Registry

**Target**: All entities in the hierarchy (tracked via 0AGNOSTIC.md files)

```sql
CREATE TABLE entities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,         -- 'memory_system'
    layer INTEGER NOT NULL,             -- 2
    entity_type VARCHAR(50),            -- 'sub_feature', 'feature', 'project'
    parent_id UUID REFERENCES entities(id),
    agnostic_path TEXT NOT NULL,        -- Absolute path to 0AGNOSTIC.md
    role TEXT,                          -- From Identity section
    scope TEXT,                         -- From Identity section
    status VARCHAR(20),                 -- 'active', 'empty', 'archived'
    last_updated TIMESTAMPTZ,
    children_count INTEGER DEFAULT 0,
    active_stage INTEGER                -- Currently active stage number
);

CREATE INDEX idx_entities_parent ON entities(parent_id);
CREATE INDEX idx_entities_layer ON entities(layer);
```

**What it enables**: Recursive queries to find all descendants of an entity, count active entities per layer, identify which entities have no active work.

#### 2A.3 Episodic Memory Tracking

**Target**: `.0agnostic/04_episodic_memory/sessions/` across all entities

```sql
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID REFERENCES entities(id),
    session_date DATE NOT NULL,
    agent_type VARCHAR(50),             -- 'claude', 'gemini', 'cursor'
    summary TEXT,
    files_changed TEXT[],               -- Array of absolute paths
    decisions_made JSONB,               -- [{decision, rationale}]
    duration_minutes INTEGER,
    file_path TEXT NOT NULL
);

SELECT create_hypertable('sessions', 'session_date');
CREATE INDEX idx_sessions_entity ON sessions(entity_id);
```

**What it enables**: `SELECT * FROM sessions WHERE session_date > NOW() - INTERVAL '7 days' ORDER BY session_date DESC` -- find recent work across all entities without scanning every episodic directory.

#### 2A.4 Rules Index

**Target**: All rules in `.0agnostic/02_rules/` (static, dynamic, scenario-based)

```sql
CREATE TABLE rules (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    importance_level INTEGER DEFAULT 2, -- 0=critical, 1=high, 2=standard
    rule_type VARCHAR(20) NOT NULL,     -- 'static', 'dynamic', 'scenario'
    scope_entity_id UUID REFERENCES entities(id), -- NULL = universal
    trigger_conditions TEXT,
    file_path TEXT NOT NULL,
    content_hash CHAR(64)               -- SHA-256 for change detection
);

CREATE INDEX idx_rules_importance ON rules(importance_level);
CREATE INDEX idx_rules_scope ON rules(scope_entity_id);
```

**What it enables**: `SELECT * FROM rules WHERE importance_level = 0 AND (scope_entity_id IS NULL OR scope_entity_id = ?)` -- load all critical rules applicable to the current entity, combining universal and scoped rules.

<!-- section_id: "7e40485e-0c9d-46fe-b640-f09e84ffc55a" -->
### How PostgreSQL Integrates With Existing Workflows

| Workflow | Current | With PostgreSQL |
|----------|---------|----------------|
| "What stage is entity X at?" | Read 0AGNOSTIC.md manually | `SELECT active_stage FROM entities WHERE name = 'X'` |
| "What work happened this week?" | Scan all episodic dirs | `SELECT * FROM sessions WHERE session_date > NOW() - INTERVAL '7 days'` |
| "Which rules apply here?" | Read file paths from CLAUDE.md | `SELECT * FROM rules WHERE scope_entity_id = ? OR scope_entity_id IS NULL` |
| "Show entity tree" | `find` + `ls` commands | Recursive CTE on entities table |

<!-- section_id: "c11c7e28-ab21-4038-a1ca-c06120f3463a" -->
### Integration Mechanism

A **sync script** (extending `agnostic-sync.sh`) runs on commit hooks:
1. Parses all `0AGNOSTIC.md` files to populate `entities` table
2. Scans `outputs/reports/` for stage reports
3. Scans `04_episodic_memory/sessions/` for session records
4. Scans `02_rules/` for rules inventory
5. Updates `content_hash` to detect changes

The filesystem remains the source of truth; PostgreSQL is a queryable index.

---

<!-- section_id: "6b2061ec-24c9-46f8-bb30-351761782fb8" -->
## 3. Technology B: Vector Embeddings (pgvector)

<!-- section_id: "780ec782-8eaa-490a-a110-52a9269d0af2" -->
### Where It Integrates

#### 3B.1 Knowledge Document Search

**Target**: All 35+ research documents in `outputs/by_topic/` and all `01_knowledge/` docs

```sql
ALTER TABLE stage_reports ADD COLUMN embedding VECTOR(1536);

CREATE TABLE knowledge_documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID REFERENCES entities(id),
    title TEXT NOT NULL,
    file_path TEXT NOT NULL,
    content_summary TEXT,               -- First 500 chars or LLM summary
    embedding VECTOR(1536),             -- Embedding of full content
    doc_type VARCHAR(50),               -- 'research', 'knowledge', 'report'
    word_count INTEGER,
    created_at TIMESTAMPTZ,
    last_modified TIMESTAMPTZ
);

CREATE INDEX idx_knowledge_embedding ON knowledge_documents
    USING diskann (embedding);
```

**Concrete example**: A pgvector column in the `knowledge_documents` table enables semantic search across all 35+ research documents. Query: "How do commercial systems handle memory decay?" returns `07_commercial_ai_memory.md` and `32_comparison_context_chain_vs_commercial_memory.md` by similarity, without requiring the agent to know those file names.

#### 3B.2 0AGNOSTIC.md Content Search

**Target**: All 0AGNOSTIC.md files in the hierarchy

```sql
CREATE TABLE agnostic_sections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_id UUID REFERENCES entities(id),
    section_type VARCHAR(50),           -- 'identity', 'key_behaviors', 'triggers', etc.
    section_content TEXT,
    embedding VECTOR(1536),
    is_static BOOLEAN DEFAULT true      -- STATIC or DYNAMIC half
);

CREATE INDEX idx_agnostic_sections_embedding ON agnostic_sections
    USING diskann (embedding);
```

**What it enables**: An agent in `memory_system/` asking "how does delegation work?" finds the agent_delegation_system's Key Behaviors section by semantic similarity, even though it is a sibling entity the agent might not know to look at.

#### 3B.3 Skill Matching via Vectors

**Target**: `.0agnostic/06_context_avenue_web/05_skills/*/SKILL.md`

```sql
CREATE TABLE skills (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    skill_name VARCHAR(100) NOT NULL,   -- 'entity-creation'
    when_conditions TEXT,               -- WHEN section from SKILL.md
    when_not_conditions TEXT,           -- WHEN NOT section
    description TEXT,
    embedding VECTOR(1536),             -- Embedding of full SKILL.md
    entity_scope UUID REFERENCES entities(id), -- NULL = universal
    file_path TEXT NOT NULL
);

CREATE INDEX idx_skills_embedding ON skills USING diskann (embedding);
```

**What it enables**: Instead of an agent reading every SKILL.md and manually checking WHEN/WHEN NOT conditions, it embeds the current task description and finds the top-3 most relevant skills by cosine similarity. Example: task "create a new sub-feature for dynamic memory" matches `/entity-creation` with high similarity.

#### 3B.4 Context Chain Relevance Scoring

**Target**: The sequential 0AGNOSTIC.md chain from root to leaf

Currently, an agent loads ALL 0AGNOSTIC.md files in the path (5-8 files). With embeddings:

```sql
-- Score each level's relevance to current task
SELECT
    e.name,
    e.layer,
    1 - (a.embedding <=> query_embedding) AS relevance_score
FROM agnostic_sections a
JOIN entities e ON a.entity_id = e.id
WHERE a.is_static = true
  AND e.id IN (SELECT id FROM entity_ancestors(?))
ORDER BY relevance_score DESC;
```

**What it enables**: The agent can prioritize which ancestors to load DYNAMIC context from. If the current task is about "memory consolidation," the memory_system's 0AGNOSTIC.md scores highest; the root 0AGNOSTIC.md (about commit rules) scores low. Static context is still always loaded, but DYNAMIC context loads selectively based on relevance.

#### 3B.5 Cross-Entity Discovery

**Target**: Finding relevant context in sibling or cousin entities

```sql
-- Find entities with relevant knowledge for current task
SELECT e.name, e.agnostic_path,
    1 - (a.embedding <=> query_embedding) AS relevance
FROM agnostic_sections a
JOIN entities e ON a.entity_id = e.id
WHERE a.section_type = 'key_behaviors'
ORDER BY relevance DESC
LIMIT 5;
```

**Concrete example**: An agent in `memory_system/` working on "how should multiple agents share context" discovers `multi_agent_system/` (a sibling entity) has relevant Key Behaviors, even though the agent did not know to look there. This directly addresses the "no cross-entity retrieval" weakness identified in doc 32.

<!-- section_id: "30bfaab0-6f70-4ae9-b6ea-e86ec0434a90" -->
### Integration Mechanism

Embeddings are generated:
1. **On commit**: A post-commit hook embeds new/changed files using OpenAI or local embedding model
2. **Stored alongside content**: In the same PostgreSQL database as the relational indexes
3. **Queryable via SQL**: Standard pgvector operators (`<=>` for cosine, `<->` for L2)
4. **Cache-friendly**: Embeddings only regenerate when content hash changes

---

<!-- section_id: "f0ed8f28-6fbd-43fa-beac-3793f8515cba" -->
## 4. Technology C: Knowledge Graphs (Neo4j/SQL)

<!-- section_id: "c23616ba-0680-4619-962a-22cde6555167" -->
### Where It Integrates

#### 4C.1 Entity Hierarchy as Explicit Graph

**Target**: The entity tree (layers, features, sub-features, stages)

The layer-stage hierarchy IS already a graph -- it just is not represented as one. Making it explicit:

```sql
-- SQL adjacency list approach
CREATE TABLE entity_relationships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_id UUID REFERENCES entities(id),
    target_id UUID REFERENCES entities(id),
    relationship_type VARCHAR(50) NOT NULL,  -- 'parent_of', 'delegates_to', 'depends_on'
    properties JSONB
);

-- Or Neo4j Cypher
CREATE (root:Entity {name: '0_layer_universal', layer: 0})
CREATE (research:Entity {name: 'better_ai_system', layer: -1})
CREATE (lss:Entity {name: 'layer_stage_system', layer: 0})
CREATE (ads:Entity {name: 'agent_delegation_system', layer: 1})
CREATE (mem:Entity {name: 'memory_system', layer: 2})
CREATE (root)-[:CONTAINS]->(research)
CREATE (research)-[:HAS_FEATURE]->(lss)
CREATE (lss)-[:HAS_SUB_FEATURE]->(ads)
CREATE (ads)-[:HAS_CHILD]->(mem)
```

**What it enables**: Graph traversal queries that are awkward with filesystem navigation:
- "What are all entities at layer 2?" -- single query vs recursive `find`
- "What entities depend on memory_system?" -- follow incoming edges
- "What is the shortest path between memory_system and multi_agent_system?" -- graph algorithm vs manual navigation

#### 4C.2 Agent Delegation Graph

**Target**: GAB agent definitions (.gab.jsonld) and their delegation patterns

```sql
CREATE TABLE delegation_edges (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    delegator_id UUID REFERENCES entities(id),
    delegatee_id UUID REFERENCES entities(id),
    delegation_type VARCHAR(50),         -- 'stage_work', 'sub_feature', 'cross_entity'
    context_passed JSONB,                -- What context is provided
    context_discovered JSONB,            -- What context agent finds itself
    gab_mode VARCHAR(100)                -- Which GAB mode triggers this
);
```

**What it enables**: Visualizing and querying the delegation chain: "When the root manager delegates research, who does the work?" Follow the edge: root -> better_ai_system -> layer_stage_system -> agent_delegation_system -> memory_system -> stage_02_research.

#### 4C.3 Context Dependencies Graph

**Target**: Cross-references between 0AGNOSTIC.md files, stage outputs, and knowledge docs

```sql
CREATE TABLE context_dependencies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_doc TEXT NOT NULL,            -- File that references another
    target_doc TEXT NOT NULL,            -- File being referenced
    dependency_type VARCHAR(50),         -- 'imports', 'references', 'extends', 'overrides'
    line_number INTEGER                  -- Where the reference appears
);
```

**What it enables**: "What breaks if I rename `STAGE_AGENT_TEMPLATE.md`?" -- query all incoming edges to find every file that references it. Currently this requires grep across the entire tree.

#### 4C.4 Rule Applicability Graph

**Target**: Rules in `02_rules/` and which entities/stages they apply to

```sql
CREATE TABLE rule_applicability (
    rule_id UUID REFERENCES rules(id),
    entity_id UUID REFERENCES entities(id),
    applies_reason VARCHAR(50)           -- 'universal', 'inherited', 'local', 'stage_specific'
);
```

**What it enables**: "Which rules apply to stage_02_research of memory_system?" -- query returns: 3 universal (I0_FILE_CHANGE_REPORTING, AI_CONTEXT_MODIFICATION_PROTOCOL, CONTEXT_TRAVERSAL_RULE) + 1 local (research_output_standards) + 1 inherited (STAGE_REPORT_RULE).

<!-- section_id: "23a89c82-ec0b-42e2-83cc-99fd740318e3" -->
### How Knowledge Graphs Integrate With Existing Workflows

| Workflow | Current | With Knowledge Graph |
|----------|---------|---------------------|
| "Find all children of entity X" | `ls` the directory | `MATCH (x)-[:HAS_CHILD*]->(c) RETURN c` |
| "What references this file?" | `grep -r` across tree | `SELECT source_doc FROM context_dependencies WHERE target_doc = ?` |
| "Which stages delegate to which?" | Read each 0AGNOSTIC.md | `MATCH path = (m)-[:DELEGATES_TO*]->(s) RETURN path` |
| "Impact analysis for file change" | Manual review | Traverse all incoming edges to changed file |

---

<!-- section_id: "5b57e557-6cb3-4d4c-9b54-da8a24798152" -->
## 5. Technology D: SHIMI (Semantic Hierarchical Memory Index)

<!-- section_id: "f9cfb48a-0e26-4564-9fb8-53e005d3fe09" -->
### Where It Integrates

#### 5D.1 Structural Parallel: Layer-Stage Hierarchy vs SHIMI Tree

The user's system is already organized as a semantic tree:

```
User's system:                        SHIMI equivalent:
[0_layer_universal]                   [Abstract Root]
    |                                     |
    +-- [layer_-1_research]           [Research Domain]
    |       |                              |
    |       +-- [better_ai_system]    [AI System Improvement]
    |               |                      |
    |               +-- [layer_stage]  [Framework Architecture]
    |                       |              |
    |                       +-- [ADS]  [Agent Delegation]
    |                            |         |
    |                            +-- [mem] [Memory Systems]
```

Both organize knowledge from abstract (root) to specific (leaf). The difference: the user's tree is navigated by directory path; SHIMI navigates by semantic similarity at each level.

#### 5D.2 Semantic Traversal for Context Loading

**Target**: The context chain loading process

Currently, loading context for `memory_system/` means reading ALL 0AGNOSTIC.md files in the path. SHIMI-style traversal would:

1. Start at root node (0_layer_universal)
2. Compute `sim(task_query, child_summaries)` for each child
3. Descend into the most semantically relevant branch
4. Repeat until reaching the target entity

**What this enables**: Dynamic context loading that adapts to the task. If the task is "research memory architectures," the traversal naturally follows the research branch. If the task is "fix a git submodule issue," the traversal might stop at the root level (where submodule rules live) without descending into research at all.

```
Task: "How do commercial memory systems handle decay?"

SHIMI traversal:
  [root] -> sim("decay", children) -> [research branch] (0.82)
    [research] -> sim("decay", children) -> [better_ai_system] (0.79)
      [better_ai] -> sim("decay", children) -> [layer_stage_system] (0.71)
        [lss] -> sim("decay", children) -> [agent_delegation] (0.68)
          [ads] -> sim("decay", children) -> [memory_system] (0.91)
            [mem] -> stage_02_research/outputs/by_topic/07_commercial_ai_memory.md
```

#### 5D.3 Bloom Filters for Context Relevance Pre-Check

**Target**: Deciding whether to load DYNAMIC context from a 0AGNOSTIC.md

Currently: agents always load STATIC, and must decide whether to read DYNAMIC. With Bloom filters:

Each entity maintains a Bloom filter encoding the key concepts in its DYNAMIC section. Before loading DYNAMIC context, the agent checks:

```python
if entity_bloom_filter.might_contain("memory_decay"):
    load_dynamic_context(entity)
else:
    skip_dynamic_context(entity)  # Saves reading irrelevant DYNAMIC sections
```

**Concrete example**: The root entity's Bloom filter contains concepts like "commit," "push," "stages," "submodule." When the task is about memory decay, the Bloom filter says "probably not relevant" -- so the agent skips the root's DYNAMIC section entirely. This saves context window tokens.

**Implementation**: Generate Bloom filters per-entity on commit. Store as compact binary alongside 0AGNOSTIC.md (e.g., `.0agnostic/07+_setup_dependant/bloom_filter.bin`). Regenerate when 0AGNOSTIC.md content hash changes.

#### 5D.4 CRDTs for agnostic-sync Conflict Resolution

**Target**: `agnostic-sync.sh` and multi-device synchronization via Syncthing

Currently, `agnostic-sync.sh` regenerates tool files from 0AGNOSTIC.md. When two devices edit 0AGNOSTIC.md simultaneously and Syncthing merges them, conflicts arise (`.sync-conflict-*` files).

CRDTs (Conflict-free Replicated Data Types) from SHIMI could improve this:

- **G-Counter CRDT** for stage completion tracking: each device increments its local counter; merging takes the maximum per device
- **LWW-Register CRDT** for status fields: "last write wins" with timestamps, resolving concurrent status updates
- **OR-Set CRDT** for file lists (children, key_outputs): concurrent additions/removals merge correctly

```python
# Example: CRDT-based status tracking
class EntityStatus:
    """LWW-Register for entity status"""
    def __init__(self):
        self.value = "empty"
        self.timestamp = 0
        self.device_id = get_device_id()

    def update(self, new_status):
        self.value = new_status
        self.timestamp = time.time()

    def merge(self, other):
        if other.timestamp > self.timestamp:
            self.value = other.value
            self.timestamp = other.timestamp
```

**What this enables**: Multiple developers (or AI agents on different devices) can update entity status, session logs, and stage progress concurrently without conflict resolution failures.

#### 5D.5 Merkle-DAG for Content Integrity

**Target**: The entity hierarchy and its sync state

A Merkle-DAG assigns each entity a hash based on its content AND its children's hashes:

```
hash(memory_system) = SHA256(
    content(0AGNOSTIC.md) +
    hash(context_chain_system) +
    hash(navigation) +
    hash(dynamic_memory) +
    hash(stage_reports)
)
```

**What this enables**:
- **Change detection**: If `memory_system`'s hash changed, something in its subtree changed
- **Sync efficiency**: Only sync subtrees where hashes differ (Syncthing already does this at the file level; Merkle-DAGs do it at the entity level)
- **Integrity verification**: Detect if a file was modified without going through the proper 0AGNOSTIC.md -> agnostic-sync pipeline

---

<!-- section_id: "4c325dc2-b7b8-41c5-a200-dd44c7d27c01" -->
## 6. Integration Matrix: Technology x System Component

| System Component | PostgreSQL (Relational) | pgvector (Semantic) | Knowledge Graph | SHIMI |
|-----------------|------------------------|--------------------|-----------------| ------|
| **01_knowledge/** | Index all docs by topic, type, entity | Semantic search across 35+ research docs | Cross-reference graph between docs | Hierarchical topic traversal |
| **02_rules/** | Rules inventory with importance + scope | "Find rules about X" by similarity | Rule applicability graph (which rules apply where) | Bloom filter pre-check for rule relevance |
| **04_episodic_memory/** | Time-series index of sessions | "Find sessions where we discussed X" | Session-to-entity-to-decision graph | N/A (episodic is temporal, not hierarchical) |
| **06_context_avenue_web/** | Registry of all avenues and their contents | Skill matching by task embedding | Avenue dependency graph | Avenue traversal by semantic relevance |
| **0AGNOSTIC.md chain** | Entity registry with hierarchy | Content search + relevance scoring | Entity hierarchy as explicit graph | Semantic traversal + Bloom filter gating |
| **CLAUDE.md sync** | Track sync state + content hashes | N/A (sync is deterministic) | Dependency graph for propagation chain | Merkle-DAG for integrity verification |
| **Skills matching** | Skill inventory with WHEN conditions | Semantic matching of task to skill | N/A | N/A |
| **Agent delegation** | Delegation history + patterns | N/A | Delegation chain graph | Semantic delegation routing |

---

<!-- section_id: "76b3dd80-b6c0-4b68-8751-1f9a1d642537" -->
## 7. Phased Integration Recommendations

<!-- section_id: "248c2756-af4b-4ec6-89b1-f6b1b0b9bab2" -->
### Phase 1: Relational Foundation (Lowest Risk, Highest Immediate Value)

**Priority**: PostgreSQL entity registry + stage reports index + episodic sessions

**Why first**:
- Provides queryable metadata without changing any existing workflows
- Filesystem remains source of truth; SQL is a read-only index
- Answers questions like "what's the status of everything?" instantly
- Enables dashboards and monitoring

**Implementation**: Extend `agnostic-sync.sh` to also update a local SQLite or PostgreSQL database on each run.

<!-- section_id: "9632a5a9-e0f8-4a96-9bed-1ed058706aff" -->
### Phase 2: Vector Search Overlay (Highest Research Impact)

**Priority**: Embed all knowledge documents + 0AGNOSTIC.md sections + skills

**Why second**:
- Directly addresses the "no semantic search" weakness (doc 32)
- Enables cross-entity discovery (the biggest current gap)
- Does not replace path-based loading; augments it with similarity-based fallback
- pgvector lives in the same PostgreSQL instance as Phase 1

**Implementation**: Post-commit hook that embeds changed files, stores in `knowledge_documents` table.

<!-- section_id: "74e2a496-f9c1-412c-83bf-41ec9250cd0f" -->
### Phase 3: Knowledge Graph for Structural Queries (Deepest Understanding)

**Priority**: Entity hierarchy graph + context dependency graph + delegation edges

**Why third**:
- Most valuable after relational and vector foundations exist
- Enables impact analysis ("what breaks if I change X?")
- Can be built on SQL (adjacency lists) or Neo4j depending on query complexity
- Visualization of the entity tree becomes trivial

**Implementation**: Parse 0AGNOSTIC.md `Parent`/`Children` fields + grep cross-references to build edge list.

<!-- section_id: "fd502ad7-ec6c-4715-a5da-27524ad81a39" -->
### Phase 4: SHIMI Concepts for Intelligent Navigation (Most Ambitious)

**Priority**: Bloom filter pre-checks + semantic traversal + Merkle-DAG integrity

**Why last**:
- Requires Phases 1-3 as foundation
- Most complex to implement but highest long-term payoff
- SHIMI's hierarchical tree maps naturally onto the existing entity tree
- CRDTs for sync only matter once multi-device collaboration is frequent

**Implementation**: Generate Bloom filters on commit, implement traversal scoring in the context-gathering skill.

---

<!-- section_id: "cb41eada-fd63-4516-a9d9-eb684114f91f" -->
## 8. Concrete Integration Examples

<!-- section_id: "c01670a4-b145-44ad-8828-1bad4921856a" -->
### Example 1: "Find all research about memory decay across the entire system"

**Today**: Agent must know to look in `stage_1_02_research/outputs/by_topic/` and manually scan 35 filenames.

**With Phase 2 (pgvector)**:
```sql
SELECT title, file_path, 1 - (embedding <=> embed('memory decay patterns')) AS score
FROM knowledge_documents
WHERE doc_type = 'research'
ORDER BY score DESC
LIMIT 5;
-- Returns: 07_commercial_ai_memory.md (0.89), 04_memory_dynamics_and_operations.md (0.86),
--          32_comparison_context_chain_vs_commercial_memory.md (0.81), ...
```

<!-- section_id: "b593c3ff-19d7-4e6c-85ab-820b6e35cbad" -->
### Example 2: "Which entities have unfinished stage work?"

**Today**: Read every 0AGNOSTIC.md in the tree and check Current Status sections.

**With Phase 1 (PostgreSQL)**:
```sql
SELECT e.name, e.layer, sr.stage_name, sr.status
FROM entities e
JOIN stage_reports sr ON sr.entity_path LIKE '%' || e.name || '%'
WHERE sr.status = 'active'
ORDER BY e.layer, sr.stage_number;
-- Returns: memory_system (layer 2, stage 02 research, active)
```

<!-- section_id: "6dc31912-9d91-4c88-84a3-f0256c0aa977" -->
### Example 3: "What would break if I restructured .0agnostic/ numbering?"

**Today**: Grep for all references to `.0agnostic/01_knowledge/`, `.0agnostic/02_rules/`, etc. across hundreds of files. Manual and error-prone.

**With Phase 3 (Knowledge Graph)**:
```sql
SELECT source_doc, line_number, dependency_type
FROM context_dependencies
WHERE target_doc LIKE '%.0agnostic/01_knowledge%'
ORDER BY source_doc;
-- Returns every file that references 01_knowledge/, with exact line numbers
```

<!-- section_id: "e799695c-9872-415f-975c-699130aa6bbd" -->
### Example 4: "Should the root entity's DYNAMIC context be loaded for this memory research task?"

**Today**: Always loaded (wastes context window tokens on irrelevant root-level details).

**With Phase 4 (SHIMI Bloom Filter)**:
```python
task = "research how commercial systems implement memory consolidation"
root_bloom = load_bloom_filter('0_layer_universal/.0agnostic/07+_setup_dependant/bloom_filter.bin')

root_bloom.might_contain("memory")        # False -- root is about commits, stages, submodules
root_bloom.might_contain("consolidation") # False
# Result: skip root DYNAMIC context, save ~2000 tokens

memory_bloom = load_bloom_filter('memory_system/.0agnostic/07+_setup_dependant/bloom_filter.bin')
memory_bloom.might_contain("memory")        # True
memory_bloom.might_contain("consolidation") # True
# Result: load memory_system DYNAMIC context
```

<!-- section_id: "0dee8b47-c080-4aed-84a9-c1a04079d84c" -->
### Example 5: "Match the right skill for 'create a new entity for dynamic memory'"

**Today**: Agent reads all SKILL.md files, manually checks WHEN conditions.

**With Phase 2 (pgvector skill matching)**:
```sql
SELECT skill_name, when_conditions,
    1 - (embedding <=> embed('create a new entity for dynamic memory')) AS match_score
FROM skills
ORDER BY match_score DESC
LIMIT 3;
-- Returns: entity-creation (0.93), context-gathering (0.71), stage-workflow (0.65)
```

---

<!-- section_id: "9c3b0751-bb29-49d9-8c92-20f59adc3a81" -->
## Sources

- [pgvector: Open-source vector similarity search for PostgreSQL](https://github.com/pgvector/pgvector) -- extension providing VECTOR type and similarity operators
- [TimescaleDB](https://www.timescale.com/) -- time-series extension for PostgreSQL with hypertables
- [Neo4j Graph Database](https://neo4j.com/) -- native graph database with Cypher query language
- [SHIMI: Semantic Hierarchical Memory Index (arXiv)](https://arxiv.org/) -- hierarchical semantic memory with Merkle-DAG sync
- [CRDTs: Conflict-free Replicated Data Types](https://crdt.tech/) -- distributed data structures for concurrent editing
- [DiskANN: Fast Accurate Billion-point Nearest Neighbor Search](https://github.com/microsoft/DiskANN) -- vector index achieving 471 QPS at 99% recall
- Perplexity AI research conversations (Feb 2026) -- source data on tier hierarchy, nesting analysis, and SHIMI placement
