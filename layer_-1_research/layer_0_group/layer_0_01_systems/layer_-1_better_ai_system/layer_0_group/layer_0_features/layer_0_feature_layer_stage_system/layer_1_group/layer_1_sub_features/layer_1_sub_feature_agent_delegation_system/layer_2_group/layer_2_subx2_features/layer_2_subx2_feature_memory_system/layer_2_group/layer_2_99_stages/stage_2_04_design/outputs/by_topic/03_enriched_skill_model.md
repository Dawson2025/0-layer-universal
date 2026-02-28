# Enriched Skill Model

## Overview

Skills in the layer-stage system are currently flat: a `SKILL.md` file with WHEN/WHEN NOT conditions and a `references/` directory pointing to knowledge docs. This design enriches skills into "mini-entities" that incorporate knowledge, rules, protocols, trajectory stores, and temporal data — while remaining backward compatible and NOT becoming full entities.

## Current State

```
skill-name/
├── SKILL.md           # Identity, WHEN/WHEN NOT, protocol steps
└── references/        # Pointers to knowledge docs
```

Skills today have no memory of past usage, no success tracking, no scoped rules, and no execution history. An agent selects skills by matching WHEN keywords against the current task — exact string matching only.

## Proposed Structure

```
skill-name/
├── SKILL.md                      # Identity, WHEN/WHEN NOT, protocol (unchanged)
├── references/                   # Pointers to external knowledge docs (unchanged)
│
├── knowledge/                    # Skill-scoped knowledge (NEW)
│   ├── domain_concepts.md        # Concepts this skill needs to understand
│   └── examples/                 # Worked examples of skill usage
│       ├── example_01.md
│       └── example_02.md
│
├── rules/                        # Skill-scoped constraints (NEW)
│   ├── preconditions.md          # What must be true BEFORE invoking
│   └── postconditions.md         # What must be true AFTER completing
│
├── protocols/                    # Skill-scoped procedures (NEW)
│   └── execution_protocol.md     # Detailed step-by-step (deeper than SKILL.md)
│
├── trajectory/                   # Execution history (NEW)
│   ├── trajectory_store.json     # Past invocations with outcomes
│   └── patterns.md               # Extracted patterns from trajectory data
│
└── temporal/                     # Time-based data (NEW)
    ├── usage_stats.json          # Frequency, recency, success rate
    └── evolution_log.md          # How this skill changed over time
```

## Component Details

### knowledge/

Skill-scoped domain knowledge. Unlike entity-level `01_knowledge/` which has per-topic directories with `principles/docs/resources/`, skill knowledge is flat and focused.

- `domain_concepts.md`: Core concepts the skill assumes. For `/entity-creation`, this might cover: what an entity IS, the Stage Completeness Rule, canonical directory structure.
- `examples/`: Worked examples showing the skill in action. Each example includes: context, input, steps taken, output, quality assessment.

### rules/

Skill-scoped constraints that go beyond WHEN/WHEN NOT.

- `preconditions.md`: What must be true before the skill can execute successfully. Example for `/entity-creation`: "Parent entity must exist and have a layer registry."
- `postconditions.md`: What must be true after the skill completes. Example: "Entity has 0AGNOSTIC.md, all 12 stages exist, agnostic-sync.sh has been run."

### protocols/

Deeper procedural knowledge than what fits in SKILL.md's Steps section.

- `execution_protocol.md`: The full step-by-step with decision points, error handling, and variations. SKILL.md gives the high-level flow; this gives the detailed playbook.

### trajectory/

The core enrichment — execution history that enables procedural memory.

**trajectory_store.json** format:
```json
[
  {
    "id": "inv_001",
    "timestamp": "2026-02-21T14:30:00Z",
    "entity_path": "layer_-1_research/.../memory_system",
    "task_context": "Create new entity for dynamic memory sub-feature",
    "agent_type": "claude-opus-4-6",
    "steps_taken": 12,
    "result": "success",
    "quality_rating": 4,
    "notes": "Smooth execution, all 12 stages created",
    "files_created": 47,
    "duration_seconds": 180
  },
  {
    "id": "inv_002",
    "timestamp": "2026-02-20T09:15:00Z",
    "entity_path": "layer_1/.../project_school",
    "task_context": "Create stage entity inside submodule",
    "agent_type": "claude-opus-4-6",
    "steps_taken": 8,
    "result": "partial_failure",
    "quality_rating": 2,
    "notes": "Submodule boundaries caused git issues",
    "files_created": 23,
    "duration_seconds": 240
  }
]
```

**patterns.md**: Auto-generated (or manually curated) insights from trajectory data:
```markdown
# Patterns for /entity-creation

## Success Patterns
- Works best when 0INDEX.md of parent is read first (92% success rate)
- Faster when sibling entity exists to copy structure from (avg 120s vs 200s)

## Failure Patterns
- Fails when parent has no layer registry (73% failure rate)
- Submodule boundaries cause git staging issues (needs manual intervention)

## Recommendations
- Always verify parent registry before starting
- For submodule entities, commit/push child repo before updating parent gitlink
```

### temporal/

Time-based metadata for skill selection and evolution tracking.

**usage_stats.json** format:
```json
{
  "skill_name": "entity-creation",
  "total_invocations": 15,
  "last_invoked": "2026-02-21T14:30:00Z",
  "success_rate": 0.87,
  "avg_duration_seconds": 165,
  "avg_quality_rating": 3.8,
  "invocations_last_7_days": 3,
  "invocations_last_30_days": 8
}
```

**evolution_log.md**: How the skill changed over time (manual entries):
```markdown
# Evolution Log for /entity-creation

## 2026-02-20: Added .cursorrules and copilot-instructions.md generation
- agnostic-sync.sh v2 now generates 6 files instead of 4
- Updated post-creation step to mention all 6 outputs

## 2026-02-19: Migrated .0agnostic/ to unified numbering
- Old: 04_agents, 05_skills, 06_hooks, 07_episodic
- New: 04_episodic, 05_handoff, 06_avenue_web, 07+_setup
```

## How Trajectory Data Integrates with Data-Based Avenues

| Avenue | What It Gets from Skills | How |
|--------|--------------------------|-----|
| **09 Knowledge Graph** | Skill → entity_type edges (from WHEN conditions) | Parse WHEN conditions into MATCHES edges |
| **10 Relational Index** | Skill metadata rows (name, success_rate, last_used) | Parse usage_stats.json into skills table |
| **11 Vector Embeddings** | Skill description embeddings (from SKILL.md) | Embed full SKILL.md for semantic matching |
| **12 Temporal Index** | Invocation events (from trajectory_store.json) | Parse trajectory entries into events table |
| **13 SHIMI Structures** | N/A for skills specifically | — |

## Backward Compatibility

1. **Existing skills continue to work** — SKILL.md + references/ is the minimum viable structure
2. **New subdirectories are optional** — agents check for them but don't fail if absent
3. **Gradual enrichment** — add trajectory/ first (highest value), then knowledge/, then rules/, then temporal/
4. **No 0AGNOSTIC.md for skills** — skills are NOT entities. They don't get stages, layer_N_group, or the full entity machinery.

## Skill Selection Enhancement

### Current: Keyword Matching
Agent reads all SKILL.md files, checks WHEN conditions against task keywords. Exact match only.

### Future: Vector-Augmented Matching
1. Embed each SKILL.md description in avenue 11 (vector embeddings)
2. When a task comes in, embed the task description
3. Find top-3 skills by cosine similarity
4. Weight by usage_stats (recently successful skills rank higher)
5. Final score: `0.6 × cosine_similarity + 0.2 × success_rate + 0.2 × recency_score`

This enables fuzzy matching: "create a new research feature" matches `/entity-creation` even without the exact keyword "entity" in the WHEN clause.

## Sync Integration

After a skill execution completes:
1. Agent appends entry to `trajectory/trajectory_store.json`
2. `sync-main.sh --avenues` picks up the new trajectory data
3. Avenue 10 (relational) updates the skills table
4. Avenue 12 (temporal) adds the invocation event
5. Periodically, `trajectory/patterns.md` is regenerated from accumulated data

## Sources

- Research doc 25 (AI implementations per memory type — Mem^p procedural framework)
- Research doc 30 (complete agent systems — CrewAI memory, OASIS audit trails)
- Research doc 34 (agent delegation patterns — skill registries)
- Research doc 36 (technology integration roadmap — skill matching via pgvector)
- Mem^p paper: arXiv:2508.06433
