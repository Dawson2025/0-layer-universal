---
resource_id: "0acf5a3b-610f-4015-9bae-e65af3b8e03d"
resource_type: "output"
resource_name: "06_open_questions"
---
# Open Questions: Decisions Needed Before Design

## Questions That Need Answers

These questions must be resolved during design (stage 04) or earlier. They represent genuine decision points where multiple valid approaches exist.

---

## Architecture Questions

### Q1: Where should entity-scoped memory physically live?

**Options**:
| Option | Path | Pro | Con |
|--------|------|-----|-----|
| A | `<entity>/.0agnostic/memory/` | Aligned with agnostic system, auto-discovered | Adds to .0agnostic/ which is already busy |
| B | `<entity>/memory/` | Clean, obvious location | New top-level directory pattern |
| C | Within stage outputs only | Stage-aligned, naturally organized | Loses entity-level memory (only stage-level) |
| D | `<entity>/.0agnostic/episodic_memory/` (existing) | Uses what exists, no new dirs | Conflates episodic with all memory types |

**Leaning**: Option A — extends the agnostic system pattern naturally.

### Q2: Should memory files have a standard schema?

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Free-form Markdown | Maximum flexibility, human-friendly | Hard to query programmatically |
| B | Structured JSON | Machine-queryable, consistent | Less human-friendly, harder to diff |
| C | Markdown with YAML frontmatter | Human-readable body + machine-readable metadata | Requires parser, mixed format |
| D | JSON-LD (like GAB agents) | Richly typed, semantic web compatible | Verbose, high overhead |

**Leaning**: Option C — Markdown body with YAML frontmatter gives both readability and structure.

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

## Automation Questions

### Q4: How much recording should be automatic?

**Options**:
| Option | Description | Pro | Con |
|--------|-------------|-----|-----|
| A | Fully manual | User/agent decides what to record | Won't happen consistently |
| B | Prompt at session end | Agent asks "should I record this session?" | Interrupts flow, easy to dismiss |
| C | Auto-record, manual review | Everything captured, user prunes later | May record noise |
| D | Smart auto-record | Heuristics decide what's significant | Heuristics may be wrong |

**Leaning**: Option C with good defaults — capture broadly, consolidate later.

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

## Scope Questions

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

## Content Questions

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

### Q9: How do we handle memory for entities that span multiple stages?

An entity might be in stage 02 (research) but have useful memories from stage 01 (request gathering). Should stage-specific memory be accessible from other stages?

**Leaning**: Yes — all stage outputs should be accessible from any stage within the entity. The stage structure organizes creation, not access.

---

## Quality Questions

### Q10: How do we prevent memory degradation?

Memories can become stale, contradictory, or irrelevant over time. What maintenance mechanisms do we need?

**Considerations**:
- Staleness detection (memory not accessed in N sessions)
- Contradiction detection (two memories with conflicting facts)
- Consolidation threshold (when N similar memories exist, merge them)
- Manual review triggers (flag for human review when confidence is low)

### Q11: How do we measure memory system effectiveness?

How will we know if the memory system is actually helping?

**Candidate metrics**:
- Time to context (how quickly can agent orient in a session?)
- Session continuity score (does agent remember what happened last time?)
- Cross-session error reduction (do repeated mistakes decrease?)
- User intervention rate (how often must user re-explain context?)
- Memory utilization (what % of stored memories are actually retrieved and used?)
