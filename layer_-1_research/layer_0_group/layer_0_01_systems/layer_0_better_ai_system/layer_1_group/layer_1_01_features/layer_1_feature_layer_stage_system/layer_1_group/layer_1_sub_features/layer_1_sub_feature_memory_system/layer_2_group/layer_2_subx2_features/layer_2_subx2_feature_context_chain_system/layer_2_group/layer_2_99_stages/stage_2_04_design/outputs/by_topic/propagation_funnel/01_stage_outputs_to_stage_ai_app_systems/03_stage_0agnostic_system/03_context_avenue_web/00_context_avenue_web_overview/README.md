---
resource_id: "ad1a7c10-1e47-4f85-a518-0191141ae610"
resource_type: "readme
output"
resource_name: "README"
---
# Context Avenue Web — Complete Overview with Ordering Principle

<!-- section_id: "125f227c-d771-4b03-8806-8290990ed1b6" -->
## What Is the Context Avenue Web?

The context avenue web is the **layer where core system content (01-05) and setup-dependent content (02-08) are formatted into avenue-specific representations**. Each avenue is an independent delivery mechanism capable of carrying the complete context to any AI system.

<!-- section_id: "aabcf724-36bf-416f-bf25-bcdbc8c208b5" -->
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

<!-- section_id: "c807ccc2-aa25-471a-b96d-c8672865cc4b" -->
## Ordering Principle: Most Comprehensive → Most Fragmented

**The fundamental organizing principle of the context avenue web is ordering by comprehensiveness**.

<!-- section_id: "43258117-fc06-419d-b927-b13fe8a7c201" -->
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

<!-- section_id: "3be0ee17-a49c-487f-8c26-4bacf80c224f" -->
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

<!-- section_id: "8345de1e-1bd6-41f4-a1a3-91e6d1f885f6" -->
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

<!-- section_id: "5435c29f-251e-4a2c-a3a2-70a5a3b1b166" -->
### Why This Ordering?

**Comprehensiveness principle**: Start with the most complete representation, and allow drill-down to more specific ones.

Think of it like a telescope:
- **Wide view** (01): Full agent structure, all capabilities
- **Zoom in** (02): Readable summaries, mode-by-mode detail
- **Focus on task** (05): Skills with step-by-step execution
- **Navigate** (07): Rules and shortcuts for this directory
- **Trigger** (08): Specific event hooks for automation

An AI system can start at 01 (most detailed) and work down to 08 (most specific) until finding what it needs.

<!-- section_id: "f5c52f59-5e13-41fa-8ba2-1289d8d39f9b" -->
## The Eight File-Based Avenues (01-08)

<!-- section_id: "d8c2ccba-c261-4f35-8834-42d7ccb74cea" -->
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

<!-- section_id: "7490f691-acc9-4637-99ee-2ed3854e9a89" -->
### Avenue 02: AALang Markdown Integration — High Detail

**Comprehensiveness**: ~80% of JSON-LD detail

**Content**: Readable markdown summaries
- Mode descriptions (what it does)
- State actor roles
- Constraint translations
- Mode flow diagrams
- Skill integration points

**Example**: `layer_2_orchestrator.integration.md` (readable summary of full JSON-LD)

<!-- section_id: "ce598829-fac3-4ae5-8f4b-3b571fd356d0" -->
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

<!-- section_id: "260899ad-b159-41eb-8d86-c761f368a922" -->
### Avenue 04: @Import References — Medium Detail

**Comprehensiveness**: Curated, indexed, navigational

**Content**: Curated reference collections
- Entity structure canonical tree
- Compliance checklists
- Architecture decision indexes
- Knowledge graphs and tables
- Cross-referenced guides

**Example**: `entity_structure.md`, `compliance_checklist.md`

<!-- section_id: "a84ee1fa-bcaa-4038-906f-e58576728e7c" -->
### Avenue 06: Agents — Medium-Low Detail

**Comprehensiveness**: Lightweight, identity-focused

**Content**: Agent stubs and summaries
- Agent identity and purpose
- Available modes/capabilities (summary only)
- Delegation patterns
- Quick reference cards
- Links to full definitions (Avenue 01)

**Example**: `stage_delegator.agent.jsonld`, `orchestrator.md` stub

<!-- section_id: "2b6f05e9-1cac-496e-bca5-814e16c0e21d" -->
### Avenue 07: Path-Specific Rules — Low Detail

**Comprehensiveness**: Context-scoped, minimal

**Content**: Directory-specific rules
- Rules that apply in this directory
- Skills relevant to this path
- Navigation hints
- Contextual triggers
- Shortcuts and aliases

**Example**: `.claude/rules/agnostic-edits.md`

<!-- section_id: "7f49184c-101a-48e7-8d83-e4e9454c6555" -->
### Avenue 08: Hooks — Most Fragmented

**Comprehensiveness**: Event-specific, minimal context

**Content**: Automation scripts
- Pre-commit hooks
- Post-merge hooks
- Validation scripts
- Sync automations
- Event-triggered actions

**Example**: `.git/hooks/pre-commit`, `agnostic-sync.sh`

<!-- section_id: "12a96722-1705-4846-862a-171a51013be6" -->
## The Five Data-Based Avenues (09-13) — Optional

Data-based avenues provide **semantic enhancements and specialized memory architectures** to file-based avenues:

| Avenue | Type | Purpose | Status |
|--------|------|---------|--------|
| 09 | Knowledge Graph | Semantic relationships (which concepts relate?) | Mature |
| 10 | Hierarchical Memory (SHIMI) | Semantic-aware hierarchical organization for decentralized agents with efficient top-down traversal | Advanced Research |
| 11 | Vector Embeddings | Semantic similarity (find similar contexts) | Mature |
| Optional | Relational Tables | Structured queries (find entity by type/status/criteria) | Mature |
| 12 | Temporal Versioning | Change history (how did structures evolve? — versions all above) | Meta-layer |

<!-- section_id: "61a0508a-c536-4c0c-a301-901d691aeffc" -->
### About Avenue 10: SHIMI (Semantic Hierarchical Memory Index)

**SHIMI** is NOT just optimization metadata. It's a sophisticated hierarchical memory architecture designed for AI agents:

- **Organizes memory as hierarchical semantic nodes** with top-down traversal from abstract intent to specific entities
- **Natively designed for decentralized agent systems** with lightweight synchronization protocols (Merkle-DAG, Bloom filters, CRDT)
- **Most advanced hierarchical memory implementation** available (ArXiv 2504.06135)
- **Superior performance** across retrieval accuracy, traversal efficiency, synchronization cost, and scalability

---

<!-- section_id: "31bcc68a-4487-4057-9b2d-35c695202d1d" -->
## Data-Based Avenues: Comparative Rankings

<!-- section_id: "04864d6d-bf37-477e-898a-ed007c8f97c4" -->
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

<!-- section_id: "0b933167-6727-49f8-9138-ad01cb74fef6" -->
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

<!-- section_id: "4f6eb01c-9848-4acb-bd78-e904ee6e4544" -->
### Hybrid Approach Performance (Research-Backed)

The research shows that combining multiple avenues provides superior performance:

- **Knowledge Graph + Vector Embeddings**: 2.8x accuracy improvement in complex queries
- **SHIMI + Vector Embeddings**: Superior scalability with semantic fidelity
- **All Three (Knowledge Graph + SHIMI + Vector Embeddings)**: Optimal reasoning + retrieval + scalability

<!-- section_id: "04250c4d-4a6a-415d-83d0-9e4f0fdf5a86" -->
## Any-One-Fires Resilience Model

**Key principle**: Any single avenue can deliver the complete context.

An AI system loading context can choose to start at ANY comprehensiveness level:

- **Start comprehensive**: Load Avenue 01 (JSON-LD) for complete detail
- **Start readable**: Load Avenue 02 (Markdown) for understandable summary
- **Start task-focused**: Load Avenue 05 (Skills) for execution steps
- **Start navigational**: Load Avenue 07 (Path Rules) for context hints
- **Start fragmented**: Load Avenue 08 (Hooks) for specific events

If the chosen avenue is unavailable, fall back to the next level. All avenues together form a **resilience mesh**.

<!-- section_id: "4dfd14c8-bc83-40cf-a771-e45bef1ea57d" -->
## Subdirectories

- **01_file_based/** — Contains avenues 01-08 (primary delivery mechanisms, ordered by comprehensiveness)
- **02_data_based/** — Contains avenues 09-13 (optional semantic enhancements and optimization)

Read the overviews for each subdirectory to understand their specific structures and how avenues within each are organized.
