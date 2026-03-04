# Context Avenue Web — Complete Overview with Ordering Principle

## What Is the Context Avenue Web?

The context avenue web is the **layer where core system content (01-05) and setup-dependent content (02-08) are formatted into avenue-specific representations**. Each avenue is an independent delivery mechanism capable of carrying the complete context to any AI system.

## Architecture

The context avenue web sits between the core .0agnostic/ system and the .1merge AI app-specific system:

```
Core System (01-05)
    + Setup-Dependent (02-08)
            ↓
    Context Avenue Web
    (8 file-based avenues
     ordered by comprehensiveness
     + 5 optional data-based)
            ↓
    .1merge System
    (Claude, Cursor, Gemini,
     Codex, Aider, Copilot)
```

## Ordering Principle: Most Comprehensive → Most Fragmented

**The fundamental organizing principle of the context avenue web is ordering by comprehensiveness**.

### File-Based Avenues (01-08): Ordered by Detail Level

From most comprehensive to most fragmented:

```
01 AALang JSON-LD
      ↓ (nearly complete detail)
02 AALang Markdown Integration
      ↓ (focused execution detail)
05 Skills
      ↓ (curated references)
04 @Import References
      ↓ (lightweight agents)
06 Agents
      ↓ (scoped rules)
07 Path-Specific Rules
      ↓ (event triggers)
08 Hooks
```

### Data-Based Avenues (09-13): Ordered by Type/Purpose

From most detailed to optimization/versioning:

```
09 Knowledge Graph (concepts & relationships)
      ↓
10 Relational Tables (SQL structured queries)
      ↓
13 SHIMI Structures (optimization primitives)
      ↓
11 Vector Embeddings (semantic similarity)
      ↓
12 Temporal Index (version history of all above)
```

### What Each Comprehensiveness Level Provides

#### File-Based Avenues

| Avenue | What It Provides | Level | Use When |
|--------|-----------------|-------|----------|
| 01 JSON-LD | Full agent definitions, all modes/actors/constraints, state machines | **Most comprehensive** | Need complete agent behavior |
| 02 Markdown | Readable summaries, mode purposes, constraint descriptions, ~80% of detail | High | Need readable reference |
| 05 Skills | Complete step-by-step execution, prerequisites, inputs/outputs, context | Medium-High | Need task instructions |
| 04 References | Curated collections, indexes, navigation pointers, references | Medium | Need to find related content |
| 06 Agents | Agent stubs, lightweight definitions, purpose statements | Medium-Low | Need quick identity lookup |
| 07 Path Rules | Directory-scoped rules, navigation hints, triggers | Low | Need context-specific guidance |
| 08 Hooks | Event scripts, specific triggers, minimal context | **Most fragmented** | Need to automate specific event |

#### Data-Based Avenues

| Avenue | What It Provides | Purpose |
|--------|-----------------|---------|
| 09 Knowledge Graph | Semantic relationships between concepts | Find related concepts |
| 10 Relational Tables | Structured metadata queryable via SQL | Fast queries across entities |
| 13 SHIMI | Performance budgets and optimization settings | Optimize performance per node |
| 11 Vector Embeddings | Semantic similarity representations | Find semantically similar contexts |
| 12 Temporal Index | Version history of all above structures | Track evolution and changes |

### Why This Ordering?

**Comprehensiveness principle**: Start with the most complete representation, and allow drill-down to more specific ones.

Think of it like a telescope:
- **Wide view** (01): Full agent structure, all capabilities
- **Zoom in** (02): Readable summaries, mode-by-mode detail
- **Focus on task** (05): Skills with step-by-step execution
- **Navigate** (07): Rules and shortcuts for this directory
- **Trigger** (08): Specific event hooks for automation

An AI system can start at 01 (most detailed) and work down to 08 (most specific) until finding what it needs.

## The Eight File-Based Avenues (01-08)

### Avenue 01: AALang JSON-LD — Most Detailed

**Comprehensiveness**: Maximum

**Content**: Complete agent definitions
- All modes and their purposes
- All actors in each mode
- Complete constraint definitions (MUST/MUST NOT)
- State machine transitions
- Skill mappings
- Persona definitions

**Example**: `layer_2_orchestrator.gab.jsonld` (816 lines, 38 graph nodes, 5 modes, 100% detail)

### Avenue 02: AALang Markdown Integration — High Detail

**Comprehensiveness**: ~80% of JSON-LD detail

**Content**: Readable markdown summaries
- Mode descriptions (what it does)
- State actor roles
- Constraint translations
- Mode flow diagrams
- Skill integration points

**Example**: `layer_2_orchestrator.integration.md` (readable summary of full JSON-LD)

### Avenue 05: Skills — Medium-High Detail

**Comprehensiveness**: Complete for specific tasks

**Content**: Task-focused execution details
- Skill description and trigger conditions
- WHEN to use / WHEN NOT to use
- Prerequisites (what must be true)
- Step-by-step execution
- Inputs and outputs
- References to related resources

**Example**: `/calc-dashboard` (full workflow for grade dashboards)

### Avenue 04: @Import References — Medium Detail

**Comprehensiveness**: Curated, indexed, navigational

**Content**: Curated reference collections
- Entity structure canonical tree
- Compliance checklists
- Architecture decision indexes
- Knowledge graphs and tables
- Cross-referenced guides

**Example**: `entity_structure.md`, `compliance_checklist.md`

### Avenue 06: Agents — Medium-Low Detail

**Comprehensiveness**: Lightweight, identity-focused

**Content**: Agent stubs and summaries
- Agent identity and purpose
- Available modes/capabilities (summary only)
- Delegation patterns
- Quick reference cards
- Links to full definitions (Avenue 01)

**Example**: `stage_delegator.agent.jsonld`, `orchestrator.md` stub

### Avenue 07: Path-Specific Rules — Low Detail

**Comprehensiveness**: Context-scoped, minimal

**Content**: Directory-specific rules
- Rules that apply in this directory
- Skills relevant to this path
- Navigation hints
- Contextual triggers
- Shortcuts and aliases

**Example**: `.claude/rules/agnostic-edits.md`

### Avenue 08: Hooks — Most Fragmented

**Comprehensiveness**: Event-specific, minimal context

**Content**: Automation scripts
- Pre-commit hooks
- Post-merge hooks
- Validation scripts
- Sync automations
- Event-triggered actions

**Example**: `.git/hooks/pre-commit`, `agnostic-sync.sh`

## The Five Data-Based Avenues (09-13) — Optional

Data-based avenues provide **semantic enhancements and specialized memory architectures** to file-based avenues:

| Avenue | Type | Purpose | Status |
|--------|------|---------|--------|
| 09 | Knowledge Graph | Semantic relationships (which concepts relate?) | Mature |
| 10 | Hierarchical Memory (SHIMI) | Semantic-aware hierarchical organization for decentralized agents with efficient top-down traversal | Advanced Research |
| 11 | Vector Embeddings | Semantic similarity (find similar contexts) | Mature |
| Optional | Relational Tables | Structured queries (find entity by type/status/criteria) | Mature |
| 12 | Temporal Versioning | Change history (how did structures evolve? — versions all above) | Meta-layer |

### About Avenue 10: SHIMI (Semantic Hierarchical Memory Index)

**SHIMI** is NOT just optimization metadata. It's a sophisticated hierarchical memory architecture designed for AI agents:

- **Organizes memory as hierarchical semantic nodes** with top-down traversal from abstract intent to specific entities
- **Natively designed for decentralized agent systems** with lightweight synchronization protocols (Merkle-DAG, Bloom filters, CRDT)
- **Most advanced hierarchical memory implementation** available (ArXiv 2504.06135)
- **Superior performance** across retrieval accuracy, traversal efficiency, synchronization cost, and scalability

---

## Data-Based Avenues: Comparative Rankings

### Rankings by Dimension (1st = Highest, 4th = Lowest)

| Dimension | 1st Place | 2nd Place | 3rd Place | 4th Place |
|-----------|-----------|-----------|-----------|-----------|
| **Reasoning Capabilities** | Knowledge Graph | SHIMI | Vector Embeddings | Relational Tables |
| **Comprehensiveness** | Knowledge Graph | SHIMI | Relational Tables | Vector Embeddings |
| **Retrieval Speed** | SHIMI | Vector Embeddings | Relational Tables | Knowledge Graph |
| **Scalability** | SHIMI | Vector Embeddings | Relational Tables | Knowledge Graph |
| **Semantic Awareness** | SHIMI | Knowledge Graph | Vector Embeddings | Relational Tables |
| **Decentralization Support** | SHIMI | Knowledge Graph | Vector Embeddings | Relational Tables |
| **Practical Adoption** | Vector Embeddings | Knowledge Graph | Relational Tables | SHIMI |
| **Maturity Level** | Relational Tables | Knowledge Graph | Vector Embeddings | SHIMI |

### Composite Rankings (by Use Case)

**For Complex Reasoning Tasks:**
1st: Knowledge Graph | 2nd: SHIMI | 3rd: Vector Embeddings | 4th: Relational Tables

**For Decentralized Agent Memory:**
1st: SHIMI | 2nd: Knowledge Graph | 3rd: Vector Embeddings | 4th: Relational Tables

**For Fast Semantic Retrieval (RAG):**
1st: Vector Embeddings | 2nd: SHIMI | 3rd: Knowledge Graph | 4th: Relational Tables

**For Scalable Multi-Agent Systems:**
1st: SHIMI | 2nd: Vector Embeddings | 3rd: Knowledge Graph | 4th: Relational Tables

**For Structured Fact Storage:**
1st: Relational Tables | 2nd: Knowledge Graph | 3rd: SHIMI | 4th: Vector Embeddings

### Hybrid Approach Performance (Research-Backed)

The research shows that combining multiple avenues provides superior performance:

- **Knowledge Graph + Vector Embeddings**: 2.8x accuracy improvement in complex queries
- **SHIMI + Vector Embeddings**: Superior scalability with semantic fidelity
- **All Three (Knowledge Graph + SHIMI + Vector Embeddings)**: Optimal reasoning + retrieval + scalability

## Any-One-Fires Resilience Model

**Key principle**: Any single avenue can deliver the complete context.

An AI system loading context can choose to start at ANY comprehensiveness level:

- **Start comprehensive**: Load Avenue 01 (JSON-LD) for complete detail
- **Start readable**: Load Avenue 02 (Markdown) for understandable summary
- **Start task-focused**: Load Avenue 05 (Skills) for execution steps
- **Start navigational**: Load Avenue 07 (Path Rules) for context hints
- **Start fragmented**: Load Avenue 08 (Hooks) for specific events

If the chosen avenue is unavailable, fall back to the next level. All avenues together form a **resilience mesh**.

## Subdirectories

- **01_file_based/** — Contains avenues 01-08 (primary delivery mechanisms, ordered by comprehensiveness)
- **02_data_based/** — Contains avenues 09-13 (optional semantic enhancements and optimization)

Read the overviews for each subdirectory to understand their specific structures and how avenues within each are organized.
