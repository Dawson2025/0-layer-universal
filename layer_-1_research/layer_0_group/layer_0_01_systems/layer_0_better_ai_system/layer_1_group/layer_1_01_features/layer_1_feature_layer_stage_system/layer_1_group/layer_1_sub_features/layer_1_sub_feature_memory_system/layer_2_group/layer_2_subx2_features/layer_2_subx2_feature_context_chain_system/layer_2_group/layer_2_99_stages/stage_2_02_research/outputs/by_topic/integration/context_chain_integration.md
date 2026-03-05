---
resource_id: "9981cd60-2014-4445-acbb-74d82b04c9ca"
resource_type: "output"
resource_name: "context_chain_integration"
---
# AALang & the Context Chain

<!-- section_id: "e5a44457-c419-424b-a067-e61ee1302f14" -->
## How AALang Fits the Context Chain

The context chain is the sequence of CLAUDE.md files from `~/.claude/CLAUDE.md` down to the working directory. AALang provides the **agent that manages this chain**: the Context Loading Agent.

---

<!-- section_id: "30d3d33b-2e7b-4ab9-bb71-0cd1af5b8158" -->
## The Context Loading Agent

**Source**: `layer_0/layer_0_03_context_agents/context_loading.gab.jsonld`
**Pattern**: 4-mode-13-actor

<!-- section_id: "1c58ca3c-7fdb-42c7-ad8e-3102b4705b4a" -->
### What It Does

The Context Loading Agent defines a structured process for:

1. **Discovering** CLAUDE.md files in the path hierarchy
2. **Parsing** each file for rules, triggers, navigation, and AALang integration sections
3. **Validating** the agent's position in the layer-stage system
4. **Resolving** inheritance (higher layers inherit from lower, with override support)
5. **Persisting** loaded state for cross-session continuity

<!-- section_id: "2bca4c3e-cf64-4ec1-9f71-8f9ae509768c" -->
### The 4-Phase Process

```
Phase 1: Loading (threshold 0.6)
├── Walk from ~/.claude/CLAUDE.md to working directory
├── Parse each file for structured sections
└── Populate ContextLoadingStateActor.loadedFiles[]

Phase 2: Validation (threshold 0.8)
├── Identify current layer (0, 1, -1, etc.)
├── Identify current stage (01-11)
├── Confirm layer-stage position
└── Update LayerStateActor, StageStateActor

Phase 3: Propagation
├── Resolve inheritance chain
├── Apply @override markers
├── Protect safety rules from unauthorized overrides
└── Update LayerInheritanceStateActor

Phase 4: Delivery
├── Confirm all context loaded
├── Calculate final confidence score
├── Persist to .claude/context_state.json
└── Report readiness
```

<!-- section_id: "388d4f95-4f88-4688-a682-82c9327c6864" -->
### Confidence Calculation

The agent tracks confidence via a weighted formula:

| Indicator | Weight | Source |
|-----------|--------|--------|
| `layerIdentified` | 0.25 | Validation mode — knows which layer we're in |
| `stageIdentified` | 0.15 | Validation mode — knows which stage we're in |
| `rulesAwareness` | 0.25 | Loading mode — [CRITICAL] rules loaded |
| `inheritanceResolved` | 0.15 | Propagation mode — overrides applied correctly |
| `requiredContextLoaded` | 0.20 | Delivery mode — all CLAUDE.md files parsed |

**Total confidence = sum of (indicator * weight)**

---

<!-- section_id: "b4b70594-b75a-4705-bcec-4f986f4ec82a" -->
## The AALang Integration Section

Every CLAUDE.md file in our system includes an `## AALang Integration` section:

```markdown
## AALang Integration

@agent ctx:ContextLoadingAgent

### Context Chain Position
- **Position**: N of M
- **Parent**: <path>
- **Children**: <path>
- **Priority**: <level>
- **Inherits**: <what>
- **Can Override**: <what>

### On Load
When this file is loaded, update state actors:
- ctx:ContextLoadingStateActor.loadedFiles += <this_file>
- ctx:NavigationStateActor.depth = <N>
```

This section tells the Context Loading Agent:
- Where this file sits in the chain (position)
- What it inherits from and what it can override
- What state actor updates to make when loaded

---

<!-- section_id: "e078675e-0416-422d-8995-64b9bf41b7ba" -->
## Layer Inheritance Model

AALang defines how context inheritance works across layers:

```
~/.claude/CLAUDE.md (global, position 1)
    │ inherits nothing (base)
    ▼
~/CLAUDE.md (user root, position 2)
    │ inherits from global
    ▼
~/dawson-workspace/CLAUDE.md (workspace, position 3)
    │ inherits from user root
    ▼
~/dawson-workspace/code/CLAUDE.md (code root, position 4)
    │ inherits from workspace
    ▼
.../0_layer_universal/CLAUDE.md (layer-stage root, position 5)
    │ inherits from code root
    ▼
layer_0/ → layer_1/ → layer_1/ → ... (deeper layers inherit from above)
```

<!-- section_id: "c6853f5f-fc77-435a-8ff1-03e4eb8126e9" -->
### Override Rules

- Higher-numbered layers CAN override lower layers with `@override` marker
- **Exception**: Safety rules with `absolute` severity require user approval to override
- Override is explicit — must be marked, not implicit

<!-- section_id: "6fbd7f07-e144-4525-9779-a91e0f012b7a" -->
### Cross-Session Persistence

The agent persists state to `.claude/context_state.json` so that:
- Subsequent sessions don't re-traverse the full chain if nothing changed
- Layer/stage position is remembered
- Loaded files list persists

---

<!-- section_id: "40648e27-021c-4c75-9abf-ccf131712526" -->
## Current Integration Status (VERIFIED 2026-02-07)

<!-- section_id: "788e2259-61dc-4d96-9963-7fcdd58a8668" -->
### What Works

- CLAUDE.md chain exists from `~/.claude/CLAUDE.md` to deepest layers
- Claude Code **automatically loads** all parent CLAUDE.md files at session start (verified)
- Child directory CLAUDE.md files load on-demand when accessing those directories (verified)
- `@path/to/file` import syntax works for referencing detailed docs (max 5 hops, verified)
- CLAUDE.md content survives context compaction (re-loaded as foundational context, verified)

<!-- section_id: "1b7d3ec8-8c9f-4077-a9b5-55018f9e004e" -->
### What Doesn't Work As Assumed

1. **The context loading agent is NOT executed.** The `context_loading.gab.jsonld` is a complete AALang agent definition, but Claude Code does NOT load or execute it. Claude Code has its own built-in CLAUDE.md loading mechanism. The AALang agent definition serves as a formal specification of what SHOULD happen, not what DOES happen.

2. **AALang annotations are plain text.** The `@agent ctx:ContextLoadingAgent` and `ctx:ContextLoadingStateActor.loadedFiles` annotations in our CLAUDE.md files are read as natural language by the LLM. Claude Code has no concept of state actors, confidence thresholds, or chain position numbering. These may still influence LLM behavior through natural language comprehension, but they are not mechanically enforced.

3. **Confidence thresholds are NOT computed.** The agent defines thresholds (0.6, 0.8) but these are aspirational — no runtime calculates them.

4. **`.claude/context_state.json` is NOT created.** The cross-session persistence mechanism described in the AALang spec does not exist in Claude Code. Claude Code uses its own persistence mechanisms (CLAUDE.md files, auto memory in `~/.claude/projects/`).

<!-- section_id: "a2884e57-d133-48ab-bf4c-a7c51e384e4e" -->
### What Claude Code Actually Does

| Mechanism | How It Works |
|-----------|-------------|
| **Parent CLAUDE.md loading** | Recurses upward from CWD to filesystem root, loads all CLAUDE.md + CLAUDE.local.md |
| **Child CLAUDE.md loading** | On-demand when Claude accesses files in subdirectories |
| **@import references** | `@path/to/file` in CLAUDE.md, max 5 hops, first external import requires approval |
| **Rules files** | `.claude/rules/*.md` loaded; `paths:` frontmatter for targeted activation |
| **Auto memory** | First 200 lines of `MEMORY.md` loaded; topic files on-demand |
| **Priority** | More specific (child/project) overrides more general (parent/user) |
| **Compaction** | CLAUDE.md is "foundational context" that persists through summarization |

<!-- section_id: "ac80d7b9-d93b-4425-a30a-01890a68e6d1" -->
### The AALang Context Loading Agent's Real Value

The `context_loading.gab.jsonld` is valuable as:
- **Design documentation**: Formally describes what the context loading process SHOULD do
- **Pattern reference**: The 4-mode pattern (Loading → Validation → Propagation → Delivery) is a good conceptual framework
- **Inheritance model**: The layer inheritance rules and @override semantics are useful concepts
- **Future tooling target**: If a transpiler converts this to markdown instructions, those instructions could guide the LLM's actual behavior

It is NOT valuable as:
- A runtime executable (Claude Code doesn't execute it)
- A JSON-LD document loaded into LLM context (too expensive, lower accuracy)

---

<!-- section_id: "0df580ac-e301-42de-9cb5-d0144d745d9b" -->
## Relationship to Other Research

- **Context Framework** (`layer_0_feature_context_framework`): Defines what the context chain IS. Claude Code's native CLAUDE.md loading IS the implementation.
- **Context Visualization** (`layer_1_subx2_feature_context_visualization`): Diagrams the chain. Still valid.
- **Verification Results** (`verification_results.md`): Full evidence for claims above.

---

<!-- section_id: "176532e1-1b12-49f9-ac48-7ce5504f1c81" -->
## Sources

- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)
- [Claude Code Best Practices (Anthropic Engineering)](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Builder.io CLAUDE.md Guide](https://www.builder.io/blog/claude-md-guide)
- [GitHub Issue #2714 — CLAUDE.md persistence after compact](https://github.com/anthropics/claude-code/issues/2714)
- [GitHub Issue #5171 — Scoped context feature request](https://github.com/anthropics/claude-code/issues/5171)

---

*Research feature: layer_0_feature_aalang_integration/context_chain*
*Last updated: 2026-02-07 (verified)*
