---
resource_id: "c4923dfc-e095-49fa-a749-270fdf19968f"
resource_type: "output"
resource_name: "referencing_methods_and_skill_invocation"
---
# Design — Referencing Methods & Getting Agents to Use Skills

## Purpose

A comprehensive survey of every mechanism available for referencing information, instructions, and skills to AI agents — and design approaches for making agents reliably use them.

---

## Part 1: All Available Referencing Methods

### 1. CLAUDE.md Chain (Static Context)

**What it is:** Markdown files named `CLAUDE.md` placed at every directory level. Claude Code automatically walks upward from the working directory to the filesystem root, loading every `CLAUDE.md` it finds.

**How it references context:**
- Content is injected directly into the system prompt (always present)
- Child directory `CLAUDE.md` files load on-demand when the agent accesses those directories
- `CLAUDE.local.md` variant for machine-specific content (gitignored)

**Strengths:**
- Guaranteed to be loaded — the agent always sees it
- Hierarchical — parent context inherited, child context additive
- Survives context compaction (re-loaded as foundational context)

**Weaknesses:**
- Budget pressure — every line costs tokens in every message
- No selectivity — everything in the file is always loaded
- Bloat accumulates — easy to add lines, hard to remove them

**Best used for:** Critical rules, identity, navigation pointers, trigger tables. NOT for detailed procedures.

---

### 2. @import References

**What it is:** Inline references in CLAUDE.md using `@path/to/file` syntax. Claude Code resolves these and loads the referenced file's content.

**How it references context:**
- `@path/to/detailed_guide.md` in CLAUDE.md → file content loaded into context
- Supports both relative and absolute paths
- Maximum 5 hops deep (import chains)
- First external import triggers a user approval dialog

**Strengths:**
- Moves detail OUT of CLAUDE.md while keeping it reachable
- Progressive — only loads when the agent encounters the reference
- Supports chaining (file A imports file B imports file C, up to 5 levels)

**Weaknesses:**
- 5-hop limit constrains deep reference chains
- First external import requires user approval (interrupts flow)
- Still adds to context once loaded — not truly on-demand

**Best used for:** Detailed guides, rule documents, knowledge base articles that are referenced from CLAUDE.md but don't need to be in every message.

---

### 3. Skills (.claude/skills/)

**What it is:** Markdown files or folders in `.claude/skills/` that define reusable procedures the agent can invoke with `/skill-name`.

**How it references context:**
- **Listing phase:** Skill names and short descriptions are included in the system prompt (within ~16K char budget)
- **Invocation phase:** Full skill content loaded only when the agent invokes it
- Folder-based skills can include multiple files, templates, supporting resources

**Two invocation paths:**
1. **User-invoked:** User types `/skill-name` → full content loaded
2. **Agent-invoked:** Agent decides a skill matches the situation → invokes it autonomously

**Strengths:**
- On-demand loading — full content only when needed
- Reusable and shareable (community format)
- Can include templates, examples, multi-file workflows
- Small static footprint (only description in system prompt)

**Weaknesses:**
- Agent invocation is probabilistic — LLM matches description to intent (non-deterministic)
- ~16K character budget for all skill descriptions combined — skills silently dropped if exceeded
- Descriptions must be good enough for the LLM to match (vague descriptions = missed invocations)

**Best used for:** Reusable procedures, workflows with templates, anything the agent should do the same way every time.

---

### 4. Path-Specific Rules (.claude/rules/)

**What it is:** Markdown files in `.claude/rules/` with optional `paths:` YAML frontmatter. Rules without `paths:` load globally. Rules with `paths:` load only when the agent works with matching file patterns.

**How it references context:**
- `paths: layer_-1_research/**` → rule loads only when working in research directories
- Content injected into context alongside the matching files
- Can contain instructions that point to other resources (skills, integration docs, etc.)

**Strengths:**
- Targeted — loads only for matching directories/files (no global bloat)
- Automatic — no agent decision needed, loads by path match
- Can serve as a trigger for other mechanisms ("when in this directory, read X, use /skill-Y")

**Weaknesses:**
- Glob patterns only — can't trigger on content or task type, only file paths
- Must be in `.claude/rules/` (repository root), not distributed through the hierarchy
- Less discoverable — agents may not know rules exist unless they match

**Best used for:** Directory-specific context injection, workflow hints for specific areas of the codebase, triggering skill usage for specific contexts.

---

### 5. JSON-LD Agent Definitions (.gab.jsonld)

**What it is:** Structured agent definitions in JSON-LD format (AALang/GAB). Define modes, actors, personas, state management, transitions, and constraints.

**How it references context:**
- NOT automatically loaded — agent must be told to read them
- Can be navigated selectively via `jq` (loading 2-5% of the file)
- Full graph structure with `@id` references enabling precise node lookups

**Selective navigation pattern:**
```bash
# Read the index (all node IDs) — ~2.5% of file
jq '."@graph"[]."@id"' file.gab.jsonld

# Read a specific mode's constraints — ~2.8% of file
jq '."@graph"[] | select(."@id" == "orch:DelegationMode")' file.gab.jsonld
```

**Strengths:**
- Maximum precision — explicit constraints, transitions, conditions
- Graph-navigable — load only what you need
- Single source of truth for agent behavior (transpiler generates markdown from it)

**Weaknesses:**
- JSON-LD is the worst format for LLM comprehension (0.34 accuracy, per KG-LLM-Bench)
- 3-5x more tokens than equivalent markdown
- Requires jq tool calls to navigate (extra steps)
- Agent must be explicitly instructed to read them

**Best used for:** Design-time agent architecture definitions. NOT for runtime LLM instructions. Use transpiler output (.integration.md) for runtime.

---

### 6. Integration Summaries (.integration.md)

**What it is:** Auto-generated markdown files that summarize JSON-LD agent definitions. Same base name as the `.gab.jsonld` file (e.g., `orchestrator.gab.jsonld` → `orchestrator.integration.md`).

**How it references context:**
- Agent reads them with the Read tool (no jq needed)
- Contains: modes table, transitions, state actors, skill mappings, constraints
- Auto-generated by transpiler (`tools/jsonld-to-md.sh`) — never hand-edited

**Strengths:**
- Markdown format — highest LLM accuracy
- Same precision as JSON-LD source (auto-generated, always in sync)
- No tool calls needed beyond a simple file read
- Compact (~50-80 lines vs 300-700 lines of JSON-LD)

**Weaknesses:**
- Must be regenerated when JSON-LD changes (transpiler dependency)
- Agent must be told to look for them (not auto-loaded)

**Best used for:** Runtime agent behavior reference. The bridge between design-time precision (JSON-LD) and runtime comprehension (markdown).

---

### 7. Episodic Memory (outputs/episodic/)

**What it is:** Session records stored in `outputs/episodic/index.md` within each layer. Documents what was done, files changed, decisions made.

**How it references context:**
- Agent reads `index.md` when resuming work
- Topic file (`memory/episodic.md`) aggregates across layers (auto-generated by `tools/episodic-sync.sh`)
- First 200 lines of `MEMORY.md` loaded into system prompt (auto-memory)

**Strengths:**
- Cross-session continuity — the agent knows what happened before
- Tool-agnostic — plain markdown, works with any AI tool
- Syncable to auto-memory for automatic loading

**Weaknesses:**
- Manual creation (agent must be reminded to write session records)
- Can become stale if not maintained

**Best used for:** Session continuity, resuming multi-session work, hand-off between agents.

---

### 8. Auto Memory (~/.claude/projects/*/memory/)

**What it is:** Claude Code's built-in persistent memory. `MEMORY.md` (first 200 lines) loads into every session. Topic files alongside it load on-demand.

**How it references context:**
- `MEMORY.md` first 200 lines → system prompt (static)
- Topic files (e.g., `debugging.md`, `patterns.md`) → loaded on-demand
- Per-project, not shared across team

**Strengths:**
- Automatic loading (no agent action needed for MEMORY.md)
- Persistent across sessions
- Good for operational learnings and gotchas

**Weaknesses:**
- 200-line limit for static loading
- Claude Code-specific (not tool-agnostic)

**Best used for:** Operational learnings, gotchas, conventions that apply to every session.

---

### 9. Hand-Off Documents

**What it is:** Structured documents created at session end to preserve context for the next session or agent. Stored in layer-stage directories.

**How it references context:**
- Agent reads hand-off doc at session start (pointed to by CLAUDE.md or episodic memory)
- Contains: what was done, what's next, blockers, decisions, file references

**Best used for:** Cross-session and cross-agent context transfer.

---

### 10. Status Files (status.json)

**What it is:** JSON files tracking stage progress, task completion, and blockers within each entity.

**How it references context:**
- Agent reads on session start to understand current state
- Updated as work progresses

**Best used for:** Progress tracking, knowing where things stand without reading full episodic history.

---

### 11. 0AGNOSTIC.md (Agnostic Source of Truth)

**What it is:** The tool-neutral source file from which all tool-specific context files are generated.

**How it references context:**
- `agnostic-sync.sh` generates CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md from it
- `.0agnostic/` directory contains on-demand resources (rules, skills, agents, knowledge, scripts)
- `.1merge/` provides tool-specific overrides (3-tier merge)

**Best used for:** Maintaining a single source of truth that works across all AI tools.

---

## Part 2: Getting Agents to Actually Use Skills

### The Core Problem

Skill invocation in Claude Code is non-deterministic. The LLM reads skill descriptions and decides — based on semantic judgment — whether a situation matches. There is no algorithmic trigger system. This means skills are missed, misapplied, or ignored depending on how well the description matches the agent's interpretation of the task.

### Design Approaches

#### Approach A: Multi-Avenue Redundancy

Don't rely on a single mechanism. Use multiple independent avenues so that if one fails, another catches it.

```
Avenue 1: Explicit jq instructions in CLAUDE.md
  → Agent runs jq on JSON-LD → output says "use /skill-X"
  → Most reliable: "run this command" is concrete and actionable

Avenue 2: Improved skill descriptions with WHEN/WHEN NOT
  → YAML frontmatter with explicit trigger conditions
  → Fallback: if jq didn't run, descriptions catch the case

Avenue 3: Integration summaries (.integration.md)
  → Markdown tables mapping situations to skills
  → Second fallback: readable reference with no tool calls needed

Avenue 4: Path-specific rules (.claude/rules/)
  → Auto-load when entering matching directories
  → Reinforcement: rules say "use /skill-X when in this context"
```

Each avenue independently points to the same skill. The more avenues that fire, the higher the probability of correct invocation.

#### Approach B: Strong Skill Descriptions

Make descriptions so precise that the LLM can't miss the match.

**Weak description (current):**
```
Use when working with context.
```

**Strong description (target):**
```yaml
---
description: |
  Use when starting a new task AND current layer/stage is unknown.
  DO NOT use when layer/stage already identified in this session.
  TRIGGERS: user says "where am I", session start, task requires knowing project context.
  NEVER USE: when already in a stage workflow, when doing quick edits.
---
```

Key patterns:
- Explicit WHEN conditions (positive triggers)
- Explicit WHEN NOT conditions (negative filters)
- Example trigger phrases
- Explicit exclusions

#### Approach C: CLAUDE.md Trigger Tables

A compact table in static context that maps situations to skills:

```markdown
## Triggers

| Situation | Action |
|-----------|--------|
| Creating entities with stages | Load skill: /entity-creation |
| Modifying AI context files | Show diagram first (critical rule) |
| Starting a new task | Load skill: /context-gathering |
| Working through stages | Load skill: /stage-workflow |
| Ending a session | Load skill: /handoff-creation |
```

This gives the agent an explicit lookup table without loading full skill content.

#### Approach D: Rules as Skill Triggers

Path-specific rules that explicitly tell the agent which skills to use:

```markdown
---
paths: layer_-1_research/**
---
## Research Context

When working in research directories:
- Start with `/context-gathering` to identify layer/stage
- Use `/stage-workflow` when advancing through stages
- End with `/handoff-creation` to preserve session state
```

The rule auto-loads when the agent enters a research directory, and explicitly names the skills to use.

#### Approach E: Skill Char Budget Increase

Override the default ~16K character budget for skill descriptions:

```bash
export SLASH_COMMAND_TOOL_CHAR_BUDGET=32000
```

This prevents skills from being silently dropped when there are many skills. However, more descriptions = more tokens in every message, so this trades context efficiency for coverage.

### Recommended Design: Combine A + B + C + D

No single approach is sufficient. The recommended design combines all four:

1. **Multi-avenue redundancy (A)** — structural insurance against any single mechanism failing
2. **Strong descriptions (B)** — each skill's own defense against being missed
3. **Trigger tables (C)** — compact static lookup for common situations
4. **Rules as triggers (D)** — automatic, path-based skill activation

Approach E (budget increase) is a tactical fix, not a design solution — use it as needed but don't depend on it.

---

## Part 3: Design Considerations for the Full System

### What Needs to Be Decided

1. **How many lines should static context use?** Target <400, but what's the right balance between navigation pointers and actual rules?

2. **Which referencing methods are primary vs. supplementary?**
   - Primary: CLAUDE.md chain, skills, path-specific rules
   - Supplementary: @import, integration summaries, episodic memory
   - Design-time only: JSON-LD agent definitions

3. **How do we keep derived files in sync?**
   - Transpiler for JSON-LD → .integration.md
   - agnostic-sync.sh for 0AGNOSTIC.md → tool-specific files
   - Pre-commit hooks? On-demand scripts? CI pipeline?

4. **How deep should reference chains go?**
   - @import supports 5 hops — is that enough?
   - Skills can @import too — how deep before it's fragile?

5. **How do we measure if skills are being invoked correctly?**
   - Test sessions with known trigger scenarios
   - Log skill invocations and compare to expected
   - A/B test different description styles

### Design Constraints

- All context must work in markdown (the format LLMs read best)
- Static context budget is limited (~4-8% of context window)
- Skill description budget defaults to ~16K chars combined
- Reference chains must terminate within 5 hops
- The system must work when the agent ignores some instructions (graceful degradation)
- Tool-agnostic core must remain clean (tool-specific additions in .1merge/ only)

---

*Design document for referencing methods and skill invocation*
*Created: 2026-02-16*
