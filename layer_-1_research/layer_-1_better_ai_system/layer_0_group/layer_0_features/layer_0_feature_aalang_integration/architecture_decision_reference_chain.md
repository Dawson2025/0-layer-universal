# Architecture Decision — Reference Chain & Three-Layer Redundancy Model

## Date: 2026-02-07

## Decision Summary

The reference chain architecture uses **three redundant layers** to maximize the probability that an agent correctly identifies and invokes the right skills at the right time. No single mechanism is sufficient — the solution is redundancy.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    THREE-LAYER REDUNDANCY MODEL                         │
│                                                                         │
│  Layer 1: jq-first (PRIMARY)                                           │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │ CLAUDE.md contains jq instructions                               │  │
│  │   → Agent runs jq on JSON-LD graph                               │  │
│  │     → JSON-LD output says: "use /skill-X, constraints: [...]"    │  │
│  │       → Agent invokes skill with full precision                  │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  Layer 2: Skill descriptions (FALLBACK)                                │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │ SKILL.md has WHEN/WHEN NOT patterns                              │  │
│  │   → Claude Code's native skill matcher reads descriptions        │  │
│  │     → If match, skill is invoked                                 │  │
│  │       → Skill internally uses jq for precision                   │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  Layer 3: Transpiled markdown (SECOND FALLBACK)                        │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │ .integration.md is auto-generated from JSON-LD via transpiler    │  │
│  │   → Human-readable markdown version of the same precision        │  │
│  │     → Agent reads this if jq doesn't run AND skill not invoked   │  │
│  │       → Still gets precise instructions, in native format        │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  + CLAUDE.md compact mapping table as additional safety net            │
│  + Path-specific rules (.claude/rules/) as directory-level hints       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Problem Being Solved

**Problem 3: Skills not being used when they should be.**

Claude Code's skill invocation is probabilistic, not deterministic. The LLM reads skill descriptions and decides — based on its own judgment — whether a situation matches. With vague descriptions, invocation is unreliable.

No single mechanism fixes this. The question is: what combination of mechanisms gives the highest probability of correct invocation?

---

## How We Got Here — Decision Evolution

### Initial proposal: Pattern B (Skills first)

```
CLAUDE.md → references skills → skills reference JSON-LD
```

**Rejected because**: If skills don't fire (the very problem we're solving), putting them first is circular logic.

### Counter-proposal: Pattern A with jq (JSON-LD first)

```
CLAUDE.md contains jq instructions → agent reads JSON-LD → JSON-LD says which skills to use
```

**Advantage**: "Run this jq command" is a concrete, actionable instruction. An LLM is more likely to follow "run this command" than to probabilistically match a vague skill description.

**Concern**: What if the agent doesn't run the jq command? What if it skips the instruction?

### Final architecture: Three-layer redundancy

Use ALL mechanisms. Each layer increases probability of correct behavior. If one fails, the next catches it.

---

## Layer 1: jq-First (PRIMARY Mechanism)

### How It Works

CLAUDE.md contains explicit jq instructions. The agent runs jq against the relevant JSON-LD file, gets back a small, precise output (~50 lines, 2-5% of the full file), and that output tells the agent exactly what mode it's in, what constraints apply, and which skills to use.

### Why This Is More Reliable

| Factor | Skill Description Matching | jq-First Approach |
|--------|---------------------------|-------------------|
| **Mechanism** | LLM probabilistically matches description to intent | LLM follows explicit instruction: "run this command" |
| **Precision** | Limited to ~16K char skill description | Full JSON-LD graph precision, loaded selectively |
| **Source of truth** | Descriptions can drift from JSON-LD | JSON-LD IS the source of truth |
| **Failure mode** | Agent doesn't recognize situation → skill never fires | Agent skips jq instruction → falls through to Layer 2 |
| **Agent decision** | "Does this situation match this description?" (vague) | "Run this command and follow its output" (concrete) |

### What jq Instructions Look Like in CLAUDE.md

**Draft — approximately 20-25 lines of static context:**

```markdown
## AALang Context Loading

Before starting any task, determine your current context by running:

### Step 1: Identify the nearest JSON-LD definition
Find the closest `.gab.jsonld` file to your working directory:
```bash
find [working-directory] -maxdepth 2 -name "*.gab.jsonld" -type f | head -5
```

### Step 2: Read the graph index
```bash
jq '."@graph"[] | {id: ."@id", type: ."@type", purpose: .purpose} | select(.purpose != null)' [file.jsonld]
```

This returns all nodes with their purposes (~20-30 lines). Identify which mode matches your current task.

### Step 3: Load the relevant mode's constraints
```bash
jq '."@graph"[] | select(."@id" == "[matched-mode-id]")' [file.jsonld]
```

This returns the mode's full definition including:
- **constraints**: What you MUST do and MUST NOT do
- **actors**: Who handles what
- **skills**: Which skills to invoke (`/skill-name`)
- **transitions**: When to move to the next mode

### Step 4: Follow the constraints as your instructions
The mode constraints are your operating instructions. If they reference a skill, invoke it.
```

### Cost-Benefit Analysis

| Metric | Value |
|--------|-------|
| **Static context cost** | ~20-25 lines in CLAUDE.md |
| **Dynamic context cost** | ~50 lines per jq output (2-5% of JSON-LD) |
| **Tool calls added** | 1-3 Bash calls (find + jq) at task start |
| **Precision gained** | Full JSON-LD mode/constraint/skill precision |
| **Budget impact** | After removing ~350 lines of bloat, adding 25 lines still nets ~325 line reduction |

---

## Layer 2: Skill Descriptions (FALLBACK Mechanism)

### How It Works

If the agent doesn't run the jq instructions (skips them, doesn't notice, or is in a context where CLAUDE.md jq instructions aren't loaded), Claude Code's native skill matching still operates. Well-written SKILL.md descriptions with explicit WHEN/WHEN NOT patterns serve as the fallback.

### What Good Skill Descriptions Look Like

The precision from JSON-LD mode transitions informs these descriptions at design-time:

```yaml
---
description: |
  Use when starting a new task AND current layer/stage is unknown.
  DO NOT use when layer/stage already identified in this session.
  TRIGGERS: user says "where am I", session start, task requires knowing project context.
  NEVER USE: when already in a stage workflow, when doing quick edits.
---
```

### Why This Is a Fallback, Not Primary

- Skill matching is probabilistic — the LLM decides based on description similarity
- Descriptions have a character budget (~16K default, configurable)
- Even perfect descriptions don't guarantee invocation
- But it's STILL valuable as a second chance when jq doesn't run

---

## Layer 3: Transpiled Markdown (SECOND FALLBACK Mechanism)

### The Transpiler Concept

A **transpiler** converts JSON-LD definitions into optimized markdown — the `.integration.md` files. But instead of writing these manually (which causes sync drift), they are **auto-generated from the JSON-LD source of truth**.

```
┌─────────────────────────┐      ┌──────────────────────┐      ┌─────────────────────┐
│  orchestrator.gab.jsonld │      │     TRANSPILER        │      │  orchestrator       │
│  (701 lines, 28KB)       │ ──→  │  (jsonld-to-md.sh    │ ──→  │  .integration.md    │
│  JSON-LD source of truth │      │   or similar)         │      │  (~50-80 lines)     │
│                          │      │                       │      │  Markdown summary   │
└─────────────────────────┘      └──────────────────────┘      └─────────────────────┘
```

### What the Transpiler Produces

Given `layer_0_orchestrator.gab.jsonld` (701 lines), the transpiler would produce something like:

```markdown
# Layer 0 Orchestrator — Integration Reference
<!-- AUTO-GENERATED from layer_0_orchestrator.gab.jsonld — do not edit directly -->
<!-- Last transpiled: 2026-02-07 -->

## Modes

| Mode | Purpose | Triggers |
|------|---------|----------|
| ReceiveMode | Parse incoming task | Task appears in incoming/from_above/ |
| DelegationMode | Split task, spawn agents | Task requires multiple sub-agents |
| MonitoringMode | Track child progress | Children spawned and running |
| AggregationMode | Collect and merge results | All children completed |
| ReportMode | Write final results | Aggregation complete |

## Mode Transitions

ReceiveMode → DelegationMode: when task is validated AND subtasks identified
DelegationMode → MonitoringMode: when all children spawned
MonitoringMode → AggregationMode: when all children report results OR timeout
AggregationMode → ReportMode: when merge complete AND confidence > 0.8

## State Actors

| Actor | Tracks | Persists |
|-------|--------|----------|
| LayerStateActor | Current layer (0, 1, -1) | Across modes |
| ChildRegistryStateActor | Spawned children and their status | Across modes |
| TaskStateActor | Task progress and subtask completion | Across modes |
| ResourceBudgetStateActor | Token/time/depth budgets | Across modes |
| StageStateActor | Current stage (01-11) | Across modes |

## Skills Referenced

| Situation | Skill | When |
|-----------|-------|------|
| Starting orchestration | /context-gathering | ReceiveMode entry |
| Spawning children | /entity-creation | DelegationMode, creating agents |
| Stage work | /stage-workflow | When delegating to a specific stage |
| Session end | /handoff-creation | ReportMode, preserving state |

## Source
- **JSON-LD**: `layer_0_01_ai_manager_system/personal/layer_0_orchestrator.gab.jsonld`
- **Transpiler**: `tools/jsonld-to-md.sh`
```

### Why This Is Valuable as a Third Layer

1. **Format the LLM reads best**: Markdown with tables scores highest for LLM accuracy (per KG-LLM-Bench research)
2. **Same precision, different format**: The transpiler extracts the same mode transitions, constraints, and skill mappings — just in markdown instead of JSON-LD
3. **Always in sync**: Auto-generated from JSON-LD, so it can't drift (unlike manually written markdown)
4. **No tool calls needed**: The agent can Read the file directly — no jq, no Bash, just the Read tool
5. **Catches the case where jq doesn't run AND skills don't match**: The agent can still find the `.integration.md` companion file and get precise instructions

### When Layer 3 Activates

- Agent is exploring the system (not yet in a task-specific workflow)
- Agent is in a context where CLAUDE.md jq instructions didn't load (deep nesting)
- Agent explicitly reads a CLAUDE.md that says "See: orchestrator.integration.md"
- A path-specific rule references the .integration.md file

### Transpiler Design

The transpiler could be:

**Option A: Shell script using jq** (simplest, available now)
```bash
#!/bin/bash
# jsonld-to-md.sh — transpile JSON-LD to markdown integration reference
INPUT="$1"
OUTPUT="${INPUT%.gab.jsonld}.integration.md"

echo "# $(basename $INPUT .gab.jsonld) — Integration Reference"
echo "<!-- AUTO-GENERATED from $(basename $INPUT) — do not edit directly -->"
echo ""
echo "## Modes"
echo ""
echo "| Mode | Purpose |"
echo "|------|---------|"
jq -r '."@graph"[] | select(."@type" == "gab:Mode") | "| \(."@id") | \(.purpose) |"' "$INPUT"
echo ""
echo "## State Actors"
echo ""
echo "| Actor | Purpose |"
echo "|-------|---------|"
jq -r '."@graph"[] | select(."@id" | test("StateActor")) | "| \(."@id") | \(.purpose) |"' "$INPUT"
# ... more sections
```

**Option B: Node.js/Python script** (richer, handles edge cases)
- Parses JSON-LD properly (handles @context, @type arrays, nested references)
- Generates richer markdown (mode transition diagrams, constraint lists)
- Could also generate SKILL.md descriptions from mode constraints

**Option C: Claude Code skill** (`/transpile-jsonld`)
- A skill that reads a JSON-LD file and produces .integration.md
- Uses jq internally for extraction
- Could be run on-demand or as part of entity-creation

**Recommended**: Start with Option A (shell script), evolve to Option C (skill) when the pattern is proven.

### Transpiler Integration with Build/Commit Workflow

To keep `.integration.md` files always in sync:

```
On any change to *.gab.jsonld:
  1. Run transpiler to regenerate .integration.md
  2. Include both files in the same commit
  3. Pre-commit hook could enforce this

OR:

On entity-creation (creating new layer/stage/sub-layer):
  1. Generate .gab.jsonld from template
  2. Immediately transpile to .integration.md
  3. Generate CLAUDE.md with references to both
```

---

## How the Three Layers Work Together

### Best case: All three fire

```
1. Agent reads CLAUDE.md → finds jq instructions
2. Agent runs jq → gets precise mode/skill mapping from JSON-LD
3. Agent invokes correct skill with full constraints
   (Layers 2 and 3 exist but weren't needed)
```

### Partial failure: jq doesn't run

```
1. Agent reads CLAUDE.md → skips jq instructions (didn't notice, didn't prioritize)
2. Claude Code's skill matcher reads SKILL.md descriptions
3. Description matches situation → skill invoked
   (Layer 1 failed, Layer 2 caught it)
```

### Double failure: jq skipped AND skill not matched

```
1. Agent reads CLAUDE.md → skips jq instructions
2. Skill descriptions don't match well enough → no skill invoked
3. Agent reads .integration.md (referenced in CLAUDE.md or path-specific rule)
4. Markdown clearly states: "In this situation, use /skill-X"
5. Agent follows the markdown instruction → invokes skill
   (Layers 1 and 2 failed, Layer 3 caught it)
```

### Complete failure: None fire

```
1. All three layers miss
2. Agent operates without AALang precision — falls back to default Claude Code behavior
3. This is the CURRENT state (what we have today) — so no regression
```

The three-layer model means we have three chances to get it right, versus zero chances today.

---

## Comparison to Current State

| Metric | Current (no redundancy) | Three-Layer Model |
|--------|------------------------|-------------------|
| Skill invocation mechanism | Vague descriptions only | jq + descriptions + transpiled markdown |
| Probability of correct invocation | Low (vague descriptions) | High (three independent chances) |
| Precision of instructions | Whatever fits in SKILL.md | Full JSON-LD precision via any of three paths |
| Source of truth | None (descriptions written ad-hoc) | JSON-LD (transpiler + jq keep everything in sync) |
| Static context cost | 717 lines (mostly bloat) | ~350 lines (lean + jq instructions) |
| Dynamic context cost | 0 (nothing loads dynamically) | ~50-80 lines per task (targeted, precise) |
| Sync/drift risk | N/A (nothing to sync) | Low (transpiler auto-generates from source of truth) |

---

## Implementation Sequence

1. **Write jq instructions for CLAUDE.md** — draft the 20-25 lines, test in a real session
2. **Build transpiler v1** (shell script) — generate .integration.md from existing JSON-LD files
3. **Improve SKILL.md descriptions** — use JSON-LD mode constraints to write WHEN/WHEN NOT patterns
4. **Add CLAUDE.md mapping table** — compact skill reference as additional safety net
5. **Create path-specific rules** — directory-level hints that reference skills and .integration.md files
6. **Test all three layers** — verify each layer independently, then test failover behavior

---

## Open Questions

1. **How often will agents actually run jq?** — Needs real-world testing. If agents reliably follow "run this command" instructions in CLAUDE.md, Layer 1 may be sufficient alone.
2. **Transpiler scope**: Should the transpiler also generate SKILL.md descriptions from JSON-LD mode constraints? This would automate the design-time → runtime translation.
3. **Pre-commit hook**: Should we enforce that every `.gab.jsonld` change triggers a transpile? Or is on-demand sufficient?
4. **CLAUDE.md jq instructions — generic or path-specific?** Generic instructions (find nearest .jsonld) are more flexible but less precise than path-specific instructions (read THIS file).

---

*Architecture decision: reference chain and three-layer redundancy model*
*Decided: 2026-02-07*
*Status: DOCUMENTED — ready for implementation*
*Approach: jq-first (primary) + skill descriptions (fallback) + transpiled markdown (second fallback)*
