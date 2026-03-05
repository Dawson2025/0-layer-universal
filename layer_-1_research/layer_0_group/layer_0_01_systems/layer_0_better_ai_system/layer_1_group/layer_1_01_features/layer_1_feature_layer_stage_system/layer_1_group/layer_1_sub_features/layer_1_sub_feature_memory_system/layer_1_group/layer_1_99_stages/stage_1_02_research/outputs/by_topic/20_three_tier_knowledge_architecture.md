---
resource_id: "ce55555a-e0b7-4ddd-b57d-a259927e72d9"
resource_type: "output"
resource_name: "20_three_tier_knowledge_architecture"
---
# Three-Tier Knowledge Architecture: Where Content Lives

<!-- section_id: "f0ea1f17-50e3-4456-9274-b59f98037b1f" -->
## The Problem

Agents lose their place across compaction boundaries and session transitions. The layer-stage system splits work across context windows, but:

1. **Too much in static context** → blows up the context window, wastes tokens on irrelevant content
2. **Too little in static context** → agent starts every session clueless, has to re-read everything
3. **Everything in stage outputs only** → agent doesn't know what's there unless it reads them all
4. **Everything in .0agnostic/knowledge/ only** → duplicates stage outputs, two sources of truth that drift apart

The question: **Where do research findings, design decisions, and accumulated understanding go?**

---

<!-- section_id: "60f2a035-243b-4bb5-a1a1-3197feecb2fd" -->
## The Three-Tier Pattern

<!-- section_id: "4b09c8f9-1ceb-4634-bf47-005cd026a232" -->
### Tier 1: Navigation Pointers (0AGNOSTIC.md → CLAUDE.md)

**What goes here**: Identity, scope, parent/child relationships, triggers, and **pointers to where substantive content lives**. Nothing else.

**When loaded**: Always — this is static context, loaded into every API message via the CLAUDE.md chain.

**Size budget**: Keep as lean as possible. Every line here costs tokens in every single message. The "lean static context" principle (already in `context_chain_system/.0agnostic/knowledge/principles/lean_static_context.md`) applies.

**Example**:
```markdown
## Identity
- Role: Memory System Research
- Scope: How AI agents remember, load, and navigate context

## Knowledge
- Domain understanding: `.0agnostic/knowledge/`
- Full research (19 files): `stage_02_research/outputs/by_topic/`
- Research index: `stage_02_research/outputs/by_topic/00_overview_and_taxonomy.md`

## Current State
- Research phase: complete (19 documents)
- Prototype: layer-stage system (see `19_prototype_specification.md`)
- Next: stage 03 (instructions)
```

**What does NOT go here**:
- Substantive explanations of concepts
- Design details
- Research findings
- Long lists or tables

**Brain analog**: Prefrontal cortex executive function — knows what you know and where to look, but doesn't store the actual knowledge itself.

---

<!-- section_id: "3fcdd41b-72ee-43d7-b84f-db094ace9723" -->
### Tier 2: Distilled Knowledge (.0agnostic/knowledge/)

**What goes here**: Actionable summaries of what the agent needs to understand to work competently in this entity. Distilled from stage outputs, not copied.

**When loaded**: On-demand — agent reads these when entering the entity or when it needs domain understanding. Triggered by 0AGNOSTIC.md pointers.

**Size budget**: Medium. Each knowledge file should be self-contained and readable in one context window load. Aim for 50-200 lines per file — enough to give competence, short enough to not waste context.

**What makes a good knowledge file**:
- **Principles** — "These are the rules that govern this domain" (already done: `principles/` directory)
- **Decision summaries** — "We decided X because Y" (distilled from research + design stages)
- **Current architecture** — "This is how things work right now" (distilled from design + development stages)
- **State of the world** — "This is where we are, what's done, what's next" (distilled from current stage)

**What does NOT go here**:
- Complete research with all sources and citations (that stays in stage outputs)
- Full design specifications with every detail (that stays in stage outputs)
- Raw conversation logs or session transcripts (those are episodic memory)
- Content that only matters during one stage and never again

**Critical rules**:
1. Knowledge files **reference** stage outputs: "For full details, see `stage_02_research/outputs/by_topic/15_vectors_graphs_and_neurology.md`"
2. Knowledge files are **distilled**, not copied — they're shorter, actionable, and focused on what an agent needs to know, not the full journey of how we learned it
3. Stage outputs are the **source of truth for content** — if a knowledge file and a stage output disagree, the stage output wins
4. Knowledge files **persist across stage transitions** — when research stage closes and design stage opens, the knowledge stays. This is the whole point.

**Brain analog**: Neocortex — consolidated semantic memory. You know that "LTP strengthens synapses via NMDA-dependent calcium cascades" without replaying the entire lecture. The knowledge is extracted, compressed, and stored in a way that supports future use.

---

<!-- section_id: "92b401ff-17bd-4dd2-8426-91b53411fb84" -->
### Tier 3: Full Content (stage_*/outputs/)

**What goes here**: Complete, detailed, traceable, authoritative content. Every source cited, every nuance preserved, every alternative considered.

**When loaded**: On-demand — only when the agent needs specific details that aren't in the knowledge summary. Referenced from knowledge files.

**Size budget**: Unlimited. These files can be as long as they need to be. They're only loaded when specifically requested.

**What belongs here**:
- Complete research with full source lists and citations
- Detailed design specifications
- Benchmark data and methodology
- Full comparison tables
- Learning paths and study guides
- Anything that would be too large or too detailed for a knowledge summary

**What does NOT go here**:
- Navigation pointers (that's Tier 1)
- Distilled summaries (that's Tier 2)
- Content from other entities (each entity has its own stages)

**Critical rules**:
1. Never delete stage outputs to "consolidate" into knowledge — the full content is the authoritative record
2. Stage outputs are immutable after the stage closes (archived, not edited)
3. Each stage output should be self-contained — it shouldn't require reading other stage outputs to understand

**Brain analog**: Hippocampus — detailed episodic records. The full memory of learning something: who said it, when, what the context was, what sources were consulted. You can replay the episode if needed, but day-to-day you rely on the consolidated neocortical version.

---

<!-- section_id: "0d6087b2-faaa-4f43-b097-26c9446764e7" -->
## How the Tiers Work Together

<!-- section_id: "451d8be6-ee99-49b6-b37a-4dfc8e3af18a" -->
### New Session Starts

```
1. Agent reads CLAUDE.md (auto-generated from 0AGNOSTIC.md)
   → "I'm in memory_system research. Knowledge is in .0agnostic/knowledge/.
      Full research is in stage_02_research/outputs/by_topic/.
      Current state: research complete, 19 docs, prototype is layer-stage system."

2. Agent reads .0agnostic/knowledge/ files (if it needs domain understanding)
   → Gets distilled understanding of the domain, decisions made, current architecture.
   → Enough to be competent. Does NOT need to read all 19 research files.

3. Agent reads specific stage outputs (only if it needs details)
   → "The user asked about STDP timing windows. Let me read file 15 Section 3.5 Level 2."
   → Targeted read, not a full re-read of everything.
```

<!-- section_id: "eb0ebd78-dccf-4427-b6fa-9b005a1aee3a" -->
### After Compaction

```
1. Compaction summary preserves: what task was being worked on, what files were being edited
2. Agent reads CLAUDE.md → re-orients to entity and scope
3. Agent reads relevant knowledge files → re-acquires domain understanding
4. Agent reads specific stage outputs → re-acquires details needed for current task
5. Agent continues working
```

<!-- section_id: "e6b234a8-aead-4347-9d03-4f14dd03af4c" -->
### Stage Transition (e.g., Research → Instructions)

```
1. Before closing research stage:
   - Distill key findings into .0agnostic/knowledge/ files
   - Update 0AGNOSTIC.md pointers to reference both knowledge files and stage outputs

2. Opening instructions stage:
   - Agent reads knowledge files (Tier 2) → understands domain
   - Agent reads specific research outputs (Tier 3) only when writing requirements that need details
   - Agent does NOT need to re-read all 19 research files to write instructions
```

---

<!-- section_id: "0fa9620f-ea1f-40bc-8b41-4224020956d6" -->
## The Consolidation Process

This is the key maintenance activity. It happens at **stage boundaries** — when significant work is completed.

<!-- section_id: "55b88a61-e984-43eb-92b3-bae64ad3a59f" -->
### When to Consolidate

| Trigger | What to Distill | Into Which Knowledge File |
|---|---|---|
| Research stage substantially complete | Key findings, taxonomies, design-relevant insights | `domain_landscape.md`, `design_principles.md` |
| Design decisions made | What was decided and why | `architecture_decisions.md` |
| Prototype reaches a milestone | Current state, what works, what doesn't | `prototype_status.md` |
| Major learning or insight | The insight and its implications | Add to relevant existing knowledge file |
| Criticism stage findings | What's wrong and what needs fixing | `known_issues.md` |

<!-- section_id: "d3295930-c378-40d1-abdc-b6192d20726a" -->
### How to Consolidate

1. **Read** the stage outputs that contain the findings
2. **Distill** into a knowledge file:
   - Lead with the actionable conclusion, not the journey
   - Include "For details, see [specific file and section]" references
   - Keep it to what an agent needs to know to work competently
   - Omit the research process, alternative approaches considered, sources (those stay in stage outputs)
3. **Update** 0AGNOSTIC.md pointers if new knowledge files were created
4. **Validate** that knowledge files don't contradict stage outputs

<!-- section_id: "ca4b383c-b171-42ba-b045-02ed290a7a65" -->
### Example: Consolidating Our Current Research

**Stage outputs (Tier 3)** — 19 files, ~5,000 lines total. An agent cannot read all of this in one context window.

**Distilled knowledge (Tier 2)** — what we'd create in `memory_system/.0agnostic/knowledge/`:

| Knowledge File | Distilled From | Purpose | Estimated Size |
|---|---|---|---|
| `memory_landscape.md` | Files 00-12 | What exists in the AI memory world: taxonomy, key systems, benchmarks | ~80 lines |
| `design_principles.md` | Files 13-15 | What matters for building a memory system: best practices, pitfalls, brain insights | ~60 lines |
| `data_structures_reference.md` | File 18 | The 16 building blocks with one-line descriptions and "use when" guidance | ~50 lines |
| `prototype_status.md` | File 19 | Where we are: what's built, what's missing, next steps | ~40 lines |
| `learning_resources.md` | Files 15, 17 | Where to go deeper: learning path, video resources | ~30 lines |

**Total distilled**: ~260 lines (fits easily in context)
**Replaces loading**: ~5,000 lines of stage outputs
**Compression ratio**: ~19:1

The agent that opens stage 03 (instructions) reads 260 lines of knowledge files and is competent. It only goes to the 5,000-line research outputs when it needs a specific detail.

---

<!-- section_id: "9af7b39b-35b8-403a-9027-c4d4dd075362" -->
## How This Answers the Original Question

> "Should I keep it only in the research and design stages and reference those files from 0AGNOSTIC.md and CLAUDE.md, or should I also put it into .0agnostic/knowledge?"

**Both. But with different content and a clear directional flow:**

```
Stage outputs (FULL content, authoritative, detailed)
       ↓ distill at stage boundaries
.0agnostic/knowledge/ (DISTILLED summaries, actionable, compact)
       ↓ pointer from
0AGNOSTIC.md (NAVIGATION only — "knowledge is here, details are there")
       ↓ auto-generates
CLAUDE.md (loaded into every session as static context)
```

**Stage outputs** = the library (complete, detailed, go here when you need the full story)
**Knowledge files** = the textbook summary (enough to be competent, references the library)
**0AGNOSTIC.md** = the card catalog (tells you what exists and where to find it)

> "Or should I have both, and also have .0agnostic/knowledge reference the stages you can find more things in?"

**Yes — this is exactly right.** Knowledge files reference stage outputs, not the other way around. The flow is: `stages → knowledge → pointers`. Each tier references the one below it (more detailed), and is referenced by the one above it (more compressed).

---

<!-- section_id: "c3fee74c-3af9-47de-99a7-7da2ba9d88fc" -->
## Connection to Research Findings

| Research Finding | How It Applies Here |
|---|---|
| **Memory consolidation** (file 04) — raw episodic → semantic knowledge | Stage outputs are raw episodes; knowledge files are consolidated semantic memory |
| **LLM-generated summary** (file 18, #6) — lossy compression preserving gist | Knowledge files are the "summary" tier — lossy but sufficient for competence |
| **Hierarchical/tiered memory** (file 18 summary) — multiple structures in tiers | The three tiers ARE hierarchical memory: pointer → summary → full |
| **Semantic tree** (file 18, #12) — O(log n) retrieval by descending | Agent descends: CLAUDE.md → knowledge file → specific stage output |
| **Sleep consolidation** (file 15, Section 3.5 Level 3) — hippocampus → neocortex transfer via replay | Stage boundaries are "sleep" — the moment to consolidate episodes into knowledge |
| **Working memory limits** (file 02) — ~7 items, bounded capacity | Context windows are bounded like working memory — tier the content to fit |
| **Lean static context** principle (context chain knowledge) | Already documented — keep static (CLAUDE.md) lean, push detail to dynamic (on-demand reads) |

---

<!-- section_id: "facd671e-6c20-4c9b-b5dc-2bd2fa8b2014" -->
## Anti-Patterns to Avoid

<!-- section_id: "c66b0b0b-2ce0-4310-8376-8c0816d99dfe" -->
### 1. Copying Stage Outputs into Knowledge
**Wrong**: Copy-pasting research file 15 into `.0agnostic/knowledge/vectors_and_graphs.md`
**Right**: Distilling the key findings into a 50-line summary that references file 15 for details

<!-- section_id: "ac7b80a9-9c51-477c-8850-e3588fdb60d8" -->
### 2. Putting Details in 0AGNOSTIC.md
**Wrong**: Writing research findings or design specs directly in 0AGNOSTIC.md
**Right**: 0AGNOSTIC.md says "Domain knowledge in `.0agnostic/knowledge/`" and nothing more

<!-- section_id: "9a5ef860-dd78-4b44-a52d-7d951b1b0be9" -->
### 3. Knowledge Files Without References
**Wrong**: A knowledge file that contains conclusions with no pointer to where they came from
**Right**: Every claim in a knowledge file has a "See [file] for details" reference

<!-- section_id: "1e003454-a405-4364-8745-ccf2ab3b1684" -->
### 4. Referencing Stage Outputs from 0AGNOSTIC.md Directly
**Wrong**: 0AGNOSTIC.md lists all 19 research files with descriptions
**Right**: 0AGNOSTIC.md points to the knowledge directory and to the stage index file (`00_overview_and_taxonomy.md`)

<!-- section_id: "09286c99-6dd0-4485-a8dd-8680e1e94169" -->
### 5. Duplicating Knowledge Across Entities
**Wrong**: The same domain knowledge in both `memory_system/.0agnostic/knowledge/` and `context_chain_system/.0agnostic/knowledge/`
**Right**: Each entity's knowledge is scoped to its domain. Cross-references use pointers, not copies.

---

<!-- section_id: "08c83362-7ecb-4f81-8588-142eab0e2822" -->
## Sources

- Memory consolidation dynamics: `04_memory_dynamics_and_operations.md`
- Hierarchical/tiered memory and data structures: `18_underlying_data_structures.md`
- Sleep consolidation and episodic→semantic transfer: `15_vectors_graphs_and_neurology.md` Section 3.5
- Working memory limits: `02_memory_by_duration.md`
- Lean static context principle: `context_chain_system/.0agnostic/knowledge/principles/lean_static_context.md`
- Context chain architecture: `context_chain_system/.0agnostic/knowledge/context_chain_architecture.md`
