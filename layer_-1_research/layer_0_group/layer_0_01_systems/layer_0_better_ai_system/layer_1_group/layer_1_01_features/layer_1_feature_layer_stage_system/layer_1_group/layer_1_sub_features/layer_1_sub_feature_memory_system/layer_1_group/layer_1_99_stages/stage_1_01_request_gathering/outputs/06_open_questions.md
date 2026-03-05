---
resource_id: "0acf5a3b-610f-4015-9bae-e65af3b8e03d"
resource_type: "output"
resource_name: "06_open_questions"
---
# Open Questions: Decisions Needed Before Design

<!-- section_id: "845f4008-d062-41aa-9f68-64a46ffad7cf" -->
## Questions That Need Answers

These questions must be resolved during design (stage 04) or earlier. They represent genuine decision points where multiple valid approaches exist.

---

<!-- section_id: "39d02001-f24f-40ab-9a4f-2c3b7d869c36" -->
## Architecture Questions

<!-- section_id: "39a81caf-844e-463b-b5fa-0998e9bcbc1a" -->
### Q1: Where should entity-scoped memory physically live?

**Options**:
| Option | Path | Pro | Con |
|--------|------|-----|-----|
| A | `<entity>/.0agnostic/memory/` | Aligned with agnostic system, auto-discovered | Adds to .0agnostic/ which is already busy |
| B | `<entity>/memory/` | Clean, obvious location | New top-level directory pattern |
| C | Within stage outputs only | Stage-aligned, naturally organized | Loses entity-level memory (only stage-level) |
| D | `<entity>/.0agnostic/episodic_memory/` (existing) | Uses what exists, no new dirs | Conflates episodic with all memory types |

**Leaning**: Option A — extends the agnostic system pattern naturally.

<!-- section_id: "84cf6046-85f2-45a6-b679-b3cf30115479" -->
### Q2: Should memory files have a standard schema?

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Free-form Markdown | Maximum flexibility, human-friendly | Hard to query programmatically |
| B | Structured JSON | Machine-queryable, consistent | Less human-friendly, harder to diff |
| C | Markdown with YAML frontmatter | Human-readable body + machine-readable metadata | Requires parser, mixed format |
| D | JSON-LD (like GAB agents) | Richly typed, semantic web compatible | Verbose, high overhead |

**Leaning**: Option C — Markdown body with YAML frontmatter gives both readability and structure.

<!-- section_id: "31f5fdf7-ad6c-40d6-831d-26daab09aa3f" -->
### Q3: How should memory hierarchy work?

Does memory at a parent entity automatically include all children's memories? Or is memory strictly scoped?

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Strict scoping | Each entity's memory is isolated | Misses cross-entity connections |
| B | Upward inheritance | Children inherit parent memory (like CLAUDE.md) | Only parent→child, not sibling |
| C | Full hierarchy access | Any entity can query any other's memory | Privacy/relevance concerns |
| D | Scoped + explicit cross-refs | Default isolated, explicit links to related entities | Requires maintaining links |

**Leaning**: Option B with explicit cross-refs (D-style) — matches existing CLAUDE.md pattern.

---

<!-- section_id: "5008b302-b1f0-419f-bdb1-489c617cafe8" -->
## Automation Questions

<!-- section_id: "4005dc6a-7902-4e2b-9878-121be44f5d9c" -->
### Q4: How much recording should be automatic?

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Fully manual | User/agent decides what to record | Won't happen consistently |
| B | Prompt at session end | Agent asks "should I record this session?" | Interrupts flow, easy to dismiss |
| C | Auto-record, manual review | Everything captured, user prunes later | May record noise |
| D | Smart auto-record | Heuristics decide what's significant | Heuristics may be wrong |

**Leaning**: Option C with good defaults — capture broadly, consolidate later.

<!-- section_id: "b7868cdf-24d6-4752-be08-3d69ae61e390" -->
### Q5: Should memory sync happen automatically or manually?

Syncing between tool-specific memory (e.g., `~/.claude/` auto-memory) and agnostic memory.

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Manual script (`memory-sync.sh`) | Full control, predictable | Forgotten, becomes stale |
| B | Git hook (pre-commit or post-commit) | Natural cadence | Adds commit overhead |
| C | Session start/end hook | Bounded timing | Requires tool-specific hooks |
| D | Bidirectional watcher | Always current | Complexity, potential loops |

**Leaning**: Option B or C — tied to natural workflow events.

---

<!-- section_id: "078740f5-a451-40b9-bd4c-3dd3e09bf7e7" -->
## Scope Questions

<!-- section_id: "12e44106-3eaa-46b4-b464-46bc677b7d19" -->
### Q6: Should the memory system handle vector embeddings?

Some queries benefit from semantic search. But embeddings are binary, model-specific, and don't fit in git.

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | No embeddings — text search only | Simple, git-friendly, tool-agnostic | Misses semantic connections |
| B | Local embeddings (.gitignored) | Best of both worlds | Not synced, per-machine |
| C | External embedding service | Scalable, shared | Dependency, cost, not agnostic |
| D | Defer — design for it but don't implement yet | Keeps options open | May influence design poorly |

**Leaning**: Option A for now, with D as future-proofing. File-based memory + smart file naming/organization may be sufficient.

<!-- section_id: "a43ae709-7a88-4fd0-9e7f-8c892b8852aa" -->
### Q7: What's the scope boundary for multi-agent memory?

When agents collaborate, what memory is shared vs. private?

**Options**:
| Option | Description |
|--------|-------------|
| A | Everything shared | All agents see all memory within the entity |
| B | Task-scoped sharing | Only memory related to current task is shared |
| C | Role-based access | Leader sees all, workers see assigned scope |
| D | Explicit sharing | Agent must actively share memory with peers |

**Leaning**: Option A for simplicity — within an entity, all agents working there share the entity's memory.

---

<!-- section_id: "593811e2-8ff1-40d4-87b8-cc55ccb2f96a" -->
## Content Questions

<!-- section_id: "42ad6e23-6a02-4fd4-bacd-9571cb17f5c9" -->
### Q8: What memory types do we actually need?

From the research, there are many memory types. Which ones apply to our framework?

| Memory Type | Do We Need It? | Current Implementation | Gap |
|-------------|----------------|----------------------|-----|
| Static context (factual) | YES | CLAUDE.md chain | Needs relevance filtering |
| Episodic (session records) | YES | Episodic structure (empty) | Needs automation |
| Semantic (facts/entities) | MAYBE | None | May be overkill |
| Procedural (how-to) | YES | Skills (.claude/skills/) | Could expand |
| Working (scratchpad) | PARTIAL | Context window | No persistent scratchpad |
| Profile (identity) | YES | 0AGNOSTIC.md identity sections | Good enough? |
| Reflection (insights) | YES | Auto-memory (Claude-specific) | Needs agnostic version |
| Summary (consolidation) | YES | None | Needed for growth |

<!-- section_id: "5d4921a6-8ed7-43e4-b591-df4e6fbc4bf2" -->
### Q9: How do we handle memory for entities that span multiple stages?

An entity might be in stage 02 (research) but have useful memories from stage 01 (request gathering). Should stage-specific memory be accessible from other stages?

**Leaning**: Yes — all stage outputs should be accessible from any stage within the entity. The stage structure organizes creation, not access.

---

<!-- section_id: "327472fa-b4f7-4409-bcbc-01b71902aa43" -->
## Quality Questions

<!-- section_id: "5967d834-558d-4fc4-992f-e408f4e5e0c0" -->
### Q10: How do we prevent memory degradation?

Memories can become stale, contradictory, or irrelevant over time. What maintenance mechanisms do we need?

**Considerations**:
- Staleness detection (memory not accessed in N sessions)
- Contradiction detection (two memories with conflicting facts)
- Consolidation threshold (when N similar memories exist, merge them)
- Manual review triggers (flag for human review when confidence is low)

<!-- section_id: "9b728f5a-4d1e-49ae-ac28-3517da357bc5" -->
### Q11: How do we measure memory system effectiveness?

How will we know if the memory system is actually helping?

**Candidate metrics**:
- Time to context (how quickly can agent orient in a session?)
- Session continuity score (does agent remember what happened last time?)
- Cross-session error reduction (do repeated mistakes decrease?)
- User intervention rate (how often must user re-explain context?)
- Memory utilization (what % of stored memories are actually retrieved and used?)
