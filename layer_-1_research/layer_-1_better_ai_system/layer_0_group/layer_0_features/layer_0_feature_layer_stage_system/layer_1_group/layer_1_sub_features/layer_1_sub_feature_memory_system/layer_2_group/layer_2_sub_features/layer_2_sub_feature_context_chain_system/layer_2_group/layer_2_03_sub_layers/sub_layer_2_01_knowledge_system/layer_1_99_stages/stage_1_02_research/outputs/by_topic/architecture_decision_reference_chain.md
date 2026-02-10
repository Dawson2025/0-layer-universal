# Architecture Decision — Reference Chain & Three-Layer Redundancy Model

## Date: 2026-02-07

## Decision Summary

The reference chain architecture uses **three redundant layers** to maximize the probability that an agent correctly identifies and invokes the right skills at the right time. No single mechanism is sufficient — the solution is redundancy.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    THREE-LAYER REDUNDANCY MODEL                               │
│                                                                              │
│  CLAUDE.md tells the agent to read ALL of these (Steps 1-4):                │
│                                                                              │
│  Step 1 → Layer 1: jq-first (PRIMARY)                                       │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ CLAUDE.md says: "Find your .gab.jsonld, read matching .integration.md" │  │
│  │   → Agent runs jq on JSON-LD graph                                    │  │
│  │     → JSON-LD output says: "use /skill-X, constraints: [...]"         │  │
│  │       → Agent invokes skill with full precision                       │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Step 2 → Layer 2: Skill descriptions (FALLBACK)                            │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ CLAUDE.md says: "Read .claude/skills/*/SKILL.md — check WHEN/WHEN NOT"│  │
│  │   → Agent reads SKILL.md files, evaluates trigger conditions          │  │
│  │     → If conditions match, agent invokes the skill                    │  │
│  │   + Claude Code's native matcher also runs in parallel (passive)      │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Step 3 → Layer 3: Transpiled markdown (SECOND FALLBACK)                    │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ CLAUDE.md says: "Read .integration.md files next to any .gab.jsonld"  │  │
│  │   → Agent reads auto-generated markdown summary                       │  │
│  │     → Summary contains modes, constraints, AND skill mappings         │  │
│  │       → Agent follows instructions in native markdown format          │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Step 4 → Path-specific rules (REINFORCEMENT)                               │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │ CLAUDE.md says: "Check .claude/rules/ for path-specific context"      │  │
│  │ Rules auto-load by directory AND contain:                             │  │
│  │   → "Read the matching .integration.md"  (re-triggers Layer 3)        │  │
│  │   → "Check skills: /skill-X, /skill-Y"  (re-triggers Layer 2)       │  │
│  │   → "Run jq on [file]"                  (re-triggers Layer 1)        │  │
│  │   → Directory-specific constraints and workflow hints                 │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
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

### What CLAUDE.md Instructions Look Like — ALL Layers

**Critical insight**: Every layer needs explicit "read this" instructions in the CLAUDE.md. The agent won't discover skills, `.integration.md` files, or rules on its own unless told to look. The CLAUDE.md must contain triggers for ALL three layers plus rules.

**Complete draft — approximately 35-45 lines of static context:**

```markdown
## AALang Context Loading

Before starting any task, load your context through these steps:

### Step 1: Read JSON-LD graph (Layer 1 — primary)
Find and read the nearest AALang agent definition:
```bash
find [working-directory] -maxdepth 2 -name "*.gab.jsonld" -type f | head -5
```

Read its graph index to discover available modes:
```bash
jq '."@graph"[] | {id: ."@id", type: ."@type", purpose: .purpose} | select(.purpose != null)' [file.jsonld]
```

Identify which mode matches your task, then load that mode's constraints:
```bash
jq '."@graph"[] | select(."@id" == "[matched-mode-id]")' [file.jsonld]
```

The output contains: constraints (MUST/MUST NOT), skills to invoke, and transitions.

### Step 2: Review available skills (Layer 2 — fallback)
List and read the available skills for this context:
- Read `.claude/skills/*/SKILL.md` files to understand what skills exist
- Each SKILL.md contains WHEN/WHEN NOT conditions — match these to your current task
- If a skill's trigger conditions match, invoke it with `/skill-name`
- Key skills: `/context-gathering`, `/stage-workflow`, `/entity-creation`, `/handoff-creation`

### Step 3: Read integration summaries (Layer 3 — second fallback)
If `.integration.md` files exist alongside JSON-LD files, read them:
- These are markdown summaries of the JSON-LD agent definitions
- They contain: modes, constraints, skill mappings, state actors
- Read with the Read tool — no jq needed
- Look for: `[name].integration.md` next to any `[name].gab.jsonld`

### Step 4: Check path-specific rules
Read any applicable rules in `.claude/rules/`:
- Rules auto-load by directory path, but also read them explicitly
- They contain: directory-specific context, skill references, workflow hints
- Key rules files: `research-context.md`, `universal-rules.md`, `aalang-integration.md`

### Step 5: Follow what you found
- Mode constraints from JSON-LD (Step 1) are your primary instructions
- Skills matched in Step 2 should be invoked
- Integration summaries (Step 3) provide additional context
- Rules (Step 4) provide directory-specific overrides
```

### Per-Layer CLAUDE.md Variants

Not every CLAUDE.md needs all 45 lines. Use the appropriate variant based on depth:

**Root-level CLAUDE.md** (~35-45 lines): All 5 steps, full jq instructions, all skill references, all rules references. Used in `~/.claude/CLAUDE.md` or `0_layer_universal/CLAUDE.md`.

**Layer-level CLAUDE.md** (~20-25 lines): Steps 1, 2, 3 only. Points to the specific JSON-LD, lists relevant skills, references the specific `.integration.md`. Used in `layer_0/CLAUDE.md`, `layer_1/CLAUDE.md`, etc.

```markdown
## AALang
- **Agent definition**: `./orchestrator.gab.jsonld`
- **Integration summary**: `./orchestrator.integration.md` — read this for modes, constraints, skill mappings
- **Skills**: `/context-gathering` (on task start), `/stage-workflow` (stage work), `/entity-creation` (new entities)
- **Rules**: Check `.claude/rules/` for path-specific context

To discover modes: `jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' ./orchestrator.gab.jsonld`
```

**Stage-level CLAUDE.md** (~10-15 lines): Steps 1 and 2 only. Points to the stage agent JSON-LD, lists stage-relevant skills, references the `.integration.md`.

```markdown
## AALang
- **Agent**: `./stage_agent.gab.jsonld`
- **Summary**: `./stage_agent.integration.md` — read for constraints and skill mappings
- **Skills**: `/stage-workflow` (primary for this stage)

Run to see this stage's modes: `jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose, skills: .skills}' ./stage_agent.gab.jsonld`
```

### What Goes in `.claude/rules/` Files

The `.claude/rules/` files are NOT just hints — they contain explicit instructions to read and use specific resources:

```markdown
---
paths: layer_-1_research/**
---
# Research Context Rules

## Required Reading
When working in research directories:
1. Find the `.gab.jsonld` for your role (e.g., `agent_orchestrator.gab.jsonld`)
2. Read the matching `.integration.md` (same base name) for agent behavior context
3. For precise mode constraints, query the `.gab.jsonld` via jq
4. Check available skills: `/context-gathering`, `/stage-workflow`

## Skill Usage
| Situation | Skill | When |
|-----------|-------|------|
| Starting research | /context-gathering | First action in any research task |
| Following research stages | /stage-workflow | When stage transitions needed |
| Creating research entities | /entity-creation | When new features/sub-features needed |
| Ending session | /handoff-creation | Before closing, to preserve state |

## Research-Specific Constraints
- Always include Sources: section with research output
- Use Perplexity/WebSearch for facts, not assumptions
- Document findings in the correct stage directory (stage_02_research)
```

Each rules file serves as BOTH a context injector AND a trigger for the other layers. When the agent enters a matching directory, the rules file tells it: "read the JSON-LD," "check these skills," "read the .integration.md."

### Cost-Benefit Analysis

| Metric | Value |
|--------|-------|
| **Static context cost** | ~35-45 lines in root CLAUDE.md, ~10-25 in descendants |
| **Dynamic context cost** | ~50 lines per jq output (2-5% of JSON-LD) |
| **Tool calls added** | 1-3 Bash calls (find + jq) + 1-2 Read calls (.integration.md, rules) |
| **Precision gained** | Full JSON-LD mode/constraint/skill precision across all 3 layers |
| **Budget impact** | After removing ~350 lines of bloat, adding 45 lines still nets ~300 line reduction |
| **Reliability** | 3 independent layers + rules, vs 0 layers currently |

---

## Layer 2: Skill Descriptions (FALLBACK Mechanism)

### How It Works

Layer 2 is NOT just passive probabilistic matching. The CLAUDE.md instructions (Step 2) **explicitly tell the agent to read through SKILL.md files** and match their WHEN/WHEN NOT conditions to the current task. This makes skill discovery active, not passive.

Two sub-mechanisms:
1. **Active discovery** (from CLAUDE.md Step 2): Agent reads SKILL.md files, evaluates WHEN/WHEN NOT conditions
2. **Passive matching** (Claude Code native): Skill descriptions in system prompt, matcher runs automatically

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

- Passive skill matching is probabilistic — the LLM decides based on description similarity
- Descriptions have a character budget (~16K default, configurable)
- Even perfect descriptions don't guarantee invocation via the passive matcher
- But ACTIVE discovery (agent reads SKILL.md files per CLAUDE.md instructions) is much more reliable
- Combined, active + passive gives Layer 2 reasonable reliability as a fallback

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

**Key design**: CLAUDE.md contains explicit "read this" instructions for ALL layers, not just Layer 1. The agent is told to: run jq (Layer 1), read SKILL.md files (Layer 2), read .integration.md (Layer 3), AND check .claude/rules/. Every layer has its own trigger.

### Best case: Agent follows all steps

```
1. Agent reads CLAUDE.md → follows Step 1 (jq)
   → Gets precise mode/skill mapping from JSON-LD
2. Agent reads CLAUDE.md → follows Step 2 (skills)
   → Reads SKILL.md files, confirms which skills match
3. Agent reads CLAUDE.md → follows Step 3 (.integration.md)
   → Gets readable summary confirming the same instructions
4. Agent reads CLAUDE.md → follows Step 4 (rules)
   → Gets directory-specific context reinforcing the same skills
5. Agent has FOUR reinforcing sources all pointing to the same behavior
   → Maximum confidence in correct action
```

### Partial failure: Agent skips some steps

```
1. Agent reads CLAUDE.md → runs jq (Step 1) but skips Steps 2-4
   → Still gets precise instructions from JSON-LD alone
   → Correct behavior (Layer 1 sufficient)

OR:

1. Agent reads CLAUDE.md → skips Step 1 (jq) but reads SKILL.md files (Step 2)
   → Finds matching WHEN/WHEN NOT conditions
   → Correct behavior (Layer 2 sufficient)

OR:

1. Agent reads CLAUDE.md → skips Steps 1-2 but reads .integration.md (Step 3)
   → Gets full mode/skill/constraint summary in markdown
   → Correct behavior (Layer 3 sufficient)
```

### Path-specific rules as catch-all

```
1. Agent enters a directory matching a .claude/rules/ path pattern
   → Rules auto-load AND contain explicit "read these files" instructions
   → Rules say: "Read the matching .integration.md (same base name), check these skills, run jq on [file]"
   → Even if the agent didn't follow CLAUDE.md steps, the rules re-trigger them
```

### Complete failure: None fire

```
1. Agent ignores all CLAUDE.md steps AND rules don't load
2. Agent operates without AALang precision — falls back to default Claude Code behavior
3. This is the CURRENT state (what we have today) — so no regression
```

The model provides **multiple independent triggers** for each layer. Even if the agent doesn't follow the CLAUDE.md steps, the rules files re-inject the same instructions when the agent enters a matching directory.

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
