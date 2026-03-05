---
resource_id: "269df2b2-1fb9-4baa-9f9a-49768603259a"
resource_type: "knowledge"
resource_name: "jsonld_design_vs_runtime"
---
# Why AALang Uses JSON-LD (Design-Time vs Run-Time)

<!-- section_id: "6f166aa6-6b3f-4c05-9d80-61ed39f18e28" -->
## The Question

Research shows JSON-LD is the **worst-performing** format for LLM instruction following (0.34 accuracy vs 0.42 for plain JSON, 3-5x more tokens). So why does the professor's AALang/GAB system use JSON-LD?

---

<!-- section_id: "0ca60a3c-8399-4fe9-8e44-91729201bd1b" -->
## The Answer: Design-Time vs Run-Time

JSON-LD serves a different purpose in AALang than what we assumed. There are two distinct phases:

```
DESIGN-TIME (authoring agent definitions)          RUN-TIME (LLM executing behavior)
┌──────────────────────────────────────┐          ┌──────────────────────────────────┐
│                                      │          │                                  │
│  JSON-LD agent definitions           │          │  LLM context window              │
│  ├── Formal, unambiguous structure   │   ???    │  ├── Needs efficient tokens       │
│  ├── Machine-parseable              │ ───────► │  ├── Needs high comprehension     │
│  ├── Graph relationships captured   │  bridge   │  ├── Markdown performs best       │
│  └── Tooling can validate/compose   │          │  └── JSON-LD performs worst       │
│                                      │          │                                  │
│  Good format: JSON-LD               │          │  Good format: Markdown            │
│                                      │          │                                  │
└──────────────────────────────────────┘          └──────────────────────────────────┘
```

<!-- section_id: "8014521d-95be-46e0-86e3-63e0d4b23b3d" -->
### Why JSON-LD Works for Design-Time

1. **Formal agent structure**: AALang defines complex structures — modes contain actors, actors have personas, state actors persist across modes, modes reference runtime behaviors. JSON-LD's `@context`, `@type`, and `@id` linking captures these relationships unambiguously.

2. **Machine-parseable**: Tooling can read, validate, and compose agent definitions. A JSON-LD validator can check that all required fields are present, that mode references resolve, that state actors are properly declared.

3. **Language specification**: AALang is a LANGUAGE. Languages need formal grammars. JSON-LD provides a structured way to define the grammar and semantics that markdown cannot.

4. **Linked data**: Agent definitions reference other definitions (a project orchestrator `"extends"` the layer_0 orchestrator). JSON-LD's linking mechanism (`@id` references) makes these relationships explicit and followable.

5. **Disambiguation**: "The Senior persona validates the output" in markdown could mean many things. In JSON-LD, the persona's exact responsibilities, inputs, outputs, and conditions are structured data.

<!-- section_id: "df73cf9b-70d5-4caf-9381-0da32c730596" -->
### Why JSON-LD Fails for Run-Time

1. **Token cost**: A gab.jsonld file is ~170KB (~40K tokens). The equivalent behavioral instructions in markdown would be ~10-15K tokens.

2. **LLM comprehension**: LLMs process linear token sequences. JSON-LD's nested structure, namespace URIs, and `@context` declarations add noise that reduces comprehension accuracy.

3. **No graph processing**: LLMs don't traverse JSON-LD graphs — they read tokens left to right. The graph structure that helps machines parse relationships provides zero benefit to the LLM.

4. **Verbosity without benefit**: JSON-LD's boilerplate (`"@type"`, `"@context"`, full URI paths) consumes tokens that could be used for actual instructions.

---

<!-- section_id: "23cce0ab-6b35-407d-857f-c78a9c38e731" -->
## How AALang Actually Executes

Based on the README and gab.jsonld, AALang execution works like this:

1. **The agent definition (JSON-LD) is loaded into the LLM context window** — the entire gab.jsonld file goes into a message
2. **The LLM reads it as text** — it understands the structure through natural language comprehension of the JSON
3. **The LLM follows the described patterns** — mode transitions, persona behaviors, state tracking all happen through the LLM's reasoning, guided by the structure it read
4. **State is maintained in the conversation** — messages in the conversation history serve as state storage

This means the LLM IS reading the JSON-LD at runtime. The professor's design loads the full agent definition into context and relies on the LLM to follow it.

<!-- section_id: "a320099f-9b6c-48ad-a05d-c6cd93572a0b" -->
### The Tension

This creates a tension:
- JSON-LD is the **right format for defining** the agent (formal, precise, machine-parseable)
- JSON-LD is the **wrong format for instructing** the LLM (expensive, lower accuracy)
- But AALang currently loads the JSON-LD definition directly into the LLM context

<!-- section_id: "609a3151-da7b-4617-92d9-c1a68c946a04" -->
### Possible Reconciliation

The professor may be prioritizing **precision over efficiency**. The argument would be: even though JSON-LD costs more tokens and scores lower on generic benchmarks, the specific structural patterns it provides (modes, actors, state actors, transition gates) may be worth the overhead because they create a consistent execution framework that the LLM can follow.

This is unverified. It's possible that:
- The professor has tested this and found the structure worth the cost
- The professor hasn't tested markdown alternatives
- The JSON-LD format is intended for future tooling that doesn't exist yet
- The JSON-LD format is the formal specification, and a markdown "compiled" version is expected for actual LLM consumption

---

<!-- section_id: "907c426b-e9de-443b-97f6-0614df678fd3" -->
## The Missing Bridge

What doesn't exist yet is a **design-time to run-time bridge** — a way to take a JSON-LD agent definition and produce markdown instructions optimized for LLM consumption:

```
gab.jsonld (formal definition)
       │
       │ compiler / transpiler
       ▼
agent_instructions.md (optimized for LLM)
├── Same behavioral specification
├── 3-5x fewer tokens
├── Higher LLM comprehension accuracy
└── Markdown format
```

This bridge would:
- Preserve the precision of AALang's formal definitions
- Produce token-efficient markdown for actual LLM execution
- Allow tooling to work with JSON-LD (validation, composition, inheritance)
- Allow LLMs to work with markdown (comprehension, execution)

This is potentially the most important integration opportunity.

---

<!-- section_id: "ced64626-194f-4384-94fa-9a73b54c5a47" -->
## What This Means for Our System

1. **Keep AALang .jsonld files as design artifacts** — they define HOW agents should work
2. **Don't load .jsonld files directly into LLM context** — they're too expensive
3. **Create markdown translations for LLM consumption** — either manually or via a transpiler
4. **Use the AALang vocabulary in our markdown** — modes, actors, state, transitions are useful concepts even in markdown
5. **Build toward the bridge** — a tool that takes a .gab.jsonld and produces optimized .md instructions

---

<!-- section_id: "84dc3574-ee4f-4625-99c4-182c595885f2" -->
## Alternative: JSON-LD as Navigable Graph (Selective Reading)

The analysis above assumes the entire JSON-LD file is loaded into context at once. But there's another approach: **use JSON-LD as a structured index that the AI navigates selectively**.

<!-- section_id: "64bbcdd0-083e-402f-9dbc-7d24dc04995d" -->
### The Idea

Instead of:
```
Load entire gab.jsonld (1300 lines, ~40K tokens) → LLM reads everything
```

Do this:
```
1. Read top-level structure only (~50 lines)
   → See mode names, actor names, @id references

2. Identify which section is needed for current task
   → "I need the Generation Mode details"

3. Read only that section (~100 lines)
   → Get exact persona, transition gates, behaviors

4. Follow @id references to related sections as needed
   → "GeneratorBot references gab-runtime.jsonld behaviors"
```

Total tokens consumed: ~200-300 lines instead of 1300. The AI reads **10-25% of the file** instead of 100%.

<!-- section_id: "bb16fd7c-17fc-4329-882f-6ded54d3fae5" -->
### Why JSON-LD's Graph Structure Helps

JSON-LD has properties that make selective navigation more precise than markdown:

| Property | JSON-LD | Markdown |
|----------|---------|----------|
| **Node identity** | Every node has `@id` — exact reference | Headers are navigable but not linked |
| **Typed nodes** | `@type` tells you what a node IS before reading it | Must read content to understand what a section is |
| **Explicit references** | `"extends": "layer_0_orchestrator"` is machine-precise | "See the layer 0 orchestrator for details" is prose |
| **Navigable links** | `@id` references can be followed to exact locations | Cross-references rely on section names |
| **Predictable structure** | Schema-defined fields — AI knows what to look for | Freeform — AI must scan to understand structure |

<!-- section_id: "3b54b07e-9375-436a-b341-1cb7a2e49080" -->
### How It Would Work in Practice

The AI uses the Read tool with line offsets to navigate the JSON-LD:

```
Step 1: Read gab.jsonld lines 1-30 (top-level structure)
→ Sees: 4 modes listed, 5 state actors, execution instructions
→ Gets @id for each mode: "ClarificationMode", "DiscussionMode", etc.

Step 2: User asks about code generation
→ AI identifies: need "GenerationMode" details
→ Read gab.jsonld lines 900-1050 (just the Generation mode)

Step 3: Generation mode references "QualityBot" persona
→ Read gab.jsonld lines 1050-1120 (just QualityBot)

Step 4: QualityBot references "gab-runtime.jsonld" behaviors
→ Read gab-runtime.jsonld lines 80-120 (just the quality checklist)
```

Total: ~300 lines read across 4 Read operations instead of 1300 lines in one load.

<!-- section_id: "53fd8cad-4ea2-4829-99ee-2c3a290cfa28" -->
### The Key Insight

This reframes the JSON-LD question entirely:

- **OLD framing**: JSON-LD as instruction format (load it all, let LLM follow it) → bad, proven by research
- **NEW framing**: JSON-LD as structured database/index (navigate selectively, read only what's needed) → potentially good

In this model, JSON-LD's overhead (`@context`, `@type`, URIs) is NOT a problem because it's never loaded wholesale. It's a navigation aid — the boilerplate helps the AI understand what each section contains WITHOUT reading the full content.

<!-- section_id: "714f8961-91f1-4848-b8ed-dcb3a0ed12d3" -->
### Comparison: JSON-LD Graph Navigation vs Markdown Index

Could you achieve the same selective reading with markdown? Yes, but with less precision:

**Markdown approach**:
```markdown
## Modes
- [Clarification Mode](#clarification) — understand requirements
- [Discussion Mode](#discussion) — explore design
- [Formalization Mode](#formalization) — formal spec
- [Generation Mode](#generation) — produce output
```
The AI reads the index, then navigates to the section it needs. This works, but:
- Headers don't convey type information
- Cross-references are text-based, not machine-linked
- The AI must infer structure from formatting conventions

**JSON-LD approach**:
```json
{
  "modes": [
    { "@id": "ClarificationMode", "@type": "Mode", "purpose": "understand requirements" },
    { "@id": "GenerationMode", "@type": "Mode", "purpose": "produce output", "mandatory": true }
  ]
}
```
The AI reads the same index, but:
- `@type` immediately tells it this IS a mode (not ambiguous)
- `@id` gives an exact reference to follow
- Properties like `"mandatory": true` are structured data, not prose to interpret
- Links to other nodes are explicit, not inferred

<!-- section_id: "501ea810-83f2-4847-b3c2-617f575b558a" -->
### Is It Worth It?

The advantage of JSON-LD graph navigation over markdown index navigation is **marginal for simple cases** but **significant for complex agent definitions** with many cross-references:

- **Simple skills** (5-10 steps): Markdown is fine. No need for graph navigation.
- **Complex agents** (GAB compiler, orchestrators): Multiple modes referencing multiple actors referencing runtime behaviors referencing format specs. The graph structure prevents the AI from getting lost in cross-references.

<!-- section_id: "d242298f-1c41-418c-8597-ca6cad76257f" -->
### Open Questions

1. **Does Claude actually navigate JSON-LD efficiently?** Need to test: give it a top-level read of a .jsonld file, then ask it to find specific details. Does it correctly follow @id references?

2. **What's the optimal "index" size?** How much of the top-level structure should the AI read to know where everything is?

3. **Can we create a compact index format?** A small JSON-LD "table of contents" file that points to sections in larger files — combining the benefits of selective reading with minimal initial token cost.

4. **How does this compare to @import?** CLAUDE.md's @import (max 5 hops) is a simpler reference mechanism. Is JSON-LD graph navigation worth the additional complexity?

---

<!-- section_id: "57b804b7-618e-4a49-98ed-a249d32ca9f0" -->
## Evidence and Sources

- KG-LLM-Bench (arXiv:2504.07087): JSON-LD scored 0.34 avg accuracy
- Prompt formatting study (arXiv:2411.10541): JSON underperforms Markdown by ~7 percentage points
- Token efficiency benchmarks (shshell.com): Markdown is 34-38% more token-efficient than JSON
- No major agent framework uses JSON-LD for LLM instructions

---

*Knowledge area: aalang_gab_system/jsonld_design_vs_runtime*
*Last updated: 2026-02-07*
