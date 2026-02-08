# AALang & the Context Chain

## How AALang Fits the Context Chain

The context chain is the sequence of CLAUDE.md files from `~/.claude/CLAUDE.md` down to the working directory. AALang provides the **agent that manages this chain**: the Context Loading Agent.

---

## The Context Loading Agent

**Source**: `layer_0/layer_0_03_context_agents/context_loading_gab.jsonld`
**Pattern**: 4-mode-13-actor

### What It Does

The Context Loading Agent defines a structured process for:

1. **Discovering** CLAUDE.md files in the path hierarchy
2. **Parsing** each file for rules, triggers, navigation, and AALang integration sections
3. **Validating** the agent's position in the layer-stage system
4. **Resolving** inheritance (higher layers inherit from lower, with override support)
5. **Persisting** loaded state for cross-session continuity

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
layer_0/ → layer_1/ → layer_2/ → ... (deeper layers inherit from above)
```

### Override Rules

- Higher-numbered layers CAN override lower layers with `@override` marker
- **Exception**: Safety rules with `absolute` severity require user approval to override
- Override is explicit — must be marked, not implicit

### Cross-Session Persistence

The agent persists state to `.claude/context_state.json` so that:
- Subsequent sessions don't re-traverse the full chain if nothing changed
- Layer/stage position is remembered
- Loaded files list persists

---

## Current Integration Status (VERIFIED 2026-02-07)

### What Works

- CLAUDE.md chain exists from `~/.claude/CLAUDE.md` to deepest layers
- Claude Code **automatically loads** all parent CLAUDE.md files at session start (verified)
- Child directory CLAUDE.md files load on-demand when accessing those directories (verified)
- `@path/to/file` import syntax works for referencing detailed docs (max 5 hops, verified)
- CLAUDE.md content survives context compaction (re-loaded as foundational context, verified)

### What Doesn't Work As Assumed

1. **The context loading agent is NOT executed.** The `context_loading_gab.jsonld` is a complete AALang agent definition, but Claude Code does NOT load or execute it. Claude Code has its own built-in CLAUDE.md loading mechanism. The AALang agent definition serves as a formal specification of what SHOULD happen, not what DOES happen.

2. **AALang annotations are plain text.** The `@agent ctx:ContextLoadingAgent` and `ctx:ContextLoadingStateActor.loadedFiles` annotations in our CLAUDE.md files are read as natural language by the LLM. Claude Code has no concept of state actors, confidence thresholds, or chain position numbering. These may still influence LLM behavior through natural language comprehension, but they are not mechanically enforced.

3. **Confidence thresholds are NOT computed.** The agent defines thresholds (0.6, 0.8) but these are aspirational — no runtime calculates them.

4. **`.claude/context_state.json` is NOT created.** The cross-session persistence mechanism described in the AALang spec does not exist in Claude Code. Claude Code uses its own persistence mechanisms (CLAUDE.md files, auto memory in `~/.claude/projects/`).

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

### The AALang Context Loading Agent's Real Value

The `context_loading_gab.jsonld` is valuable as:
- **Design documentation**: Formally describes what the context loading process SHOULD do
- **Pattern reference**: The 4-mode pattern (Loading → Validation → Propagation → Delivery) is a good conceptual framework
- **Inheritance model**: The layer inheritance rules and @override semantics are useful concepts
- **Future tooling target**: If a transpiler converts this to markdown instructions, those instructions could guide the LLM's actual behavior

It is NOT valuable as:
- A runtime executable (Claude Code doesn't execute it)
- A JSON-LD document loaded into LLM context (too expensive, lower accuracy)

---

## Relationship to Other Research

- **Context Framework** (`layer_0_feature_context_framework`): Defines what the context chain IS. Claude Code's native CLAUDE.md loading IS the implementation.
- **Context Visualization** (`layer_1_sub_feature_context_visualization`): Diagrams the chain. Still valid.
- **Verification Results** (`verification_results.md`): Full evidence for claims above.

---

## Sources

- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)
- [Claude Code Best Practices (Anthropic Engineering)](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Builder.io CLAUDE.md Guide](https://www.builder.io/blog/claude-md-guide)
- [GitHub Issue #2714 — CLAUDE.md persistence after compact](https://github.com/anthropics/claude-code/issues/2714)
- [GitHub Issue #5171 — Scoped context feature request](https://github.com/anthropics/claude-code/issues/5171)

---

*Research feature: layer_0_feature_aalang_integration/context_chain*
*Last updated: 2026-02-07 (verified)*
