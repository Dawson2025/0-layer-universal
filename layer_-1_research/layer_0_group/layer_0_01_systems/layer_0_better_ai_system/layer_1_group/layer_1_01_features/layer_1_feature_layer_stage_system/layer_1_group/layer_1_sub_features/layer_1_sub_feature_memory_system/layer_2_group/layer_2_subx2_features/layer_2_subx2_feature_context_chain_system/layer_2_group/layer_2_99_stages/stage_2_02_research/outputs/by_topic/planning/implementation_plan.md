---
resource_id: "cb475f58-7404-47f8-99cb-cf91dd0a5a1d"
resource_type: "output"
resource_name: "implementation_plan"
---
# Implementation Plan — AALang/GAB + Claude Code Integration

<!-- section_id: "de2612c4-550d-4fea-b231-b1b205989ca4" -->
## Context

This plan addresses the 5 core problems identified in `problems_and_vision.md` and verified in `verification_results.md` (including professor's documentation review on 2026-02-07). It implements the **hybrid approach with three-layer redundancy**: JSON-LD as source of truth (design-time), skills and markdown as runtime interface, compact CLAUDE.md references connecting them, and a transpiler keeping everything in sync.

**Architecture decision**: See `architecture_decision_reference_chain.md` for the full analysis of the three-layer redundancy model (jq-first + skill descriptions + transpiled markdown).

**Research location**: `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_aalang_integration/`

---

<!-- section_id: "39b8d104-ebd1-4dbf-8dea-6d1505e329dd" -->
## Problems Being Solved

| # | Problem | Root Cause | Solution Approach |
|---|---------|-----------|-------------------|
| 1 | Instructions lost across sessions | CLAUDE.md bloat (717 lines in static chain), duplication, verbose ceremonial content | Slim CLAUDE.md chain, @imports, path-specific rules |
| 2 | Agent Teams ephemeral | No persistence layer for team state | Hand-off documents + spawn prompts backed by AALang orchestrator definitions |
| 3 | Skills not being used | Vague descriptions, no explicit trigger conditions | JSON-LD defines precise triggers → translated to SKILL.md with WHEN/WHEN NOT patterns |
| 4 | Context chain efficiency | Entire context loaded every session regardless of task | Selective loading via path-specific rules, @imports, skills that load on-demand |
| 5 | Markdown vs JSON-LD tension | Research shows JSON-LD worst for LLM accuracy, but best for definition precision | Hybrid: JSON-LD for design-time precision, markdown for runtime communication |

---

<!-- section_id: "86fa8840-e9be-41b6-bdf6-8945cd76f6d8" -->
## Key Research Findings

<!-- section_id: "c09ccc76-a4bf-4d06-86c0-c4d8bda8c3d4" -->
### Finding 1: JSON-LD Precision vs Runtime Comprehension

**Question**: Is AALang/GAB's JSON-LD format better at getting agents to understand WHEN to use skills?

**Answer**: JSON-LD is better at *defining* precision, not at *communicating* it to the LLM directly. But agents CAN navigate JSON-LD selectively via jq (proven — see `selective_jsonld_navigation.md`), loading only 2-5% of the file.

<!-- section_id: "c922f7f5-edd8-4242-95ff-acfacc7af8d0" -->
### Finding 2: Selective JSON-LD Graph Navigation (PROVEN)

Agents can use `jq` to navigate JSON-LD as a graph, extracting only what they need:
- **Index**: `jq '."@graph"[]."@id"'` → all node IDs (2.5% of file)
- **Specific node**: `jq '... | select(."@id" == "mode:X")'` → one mode's full definition (2.8%)
- **Filter by type**: `jq '... | select(."@type" == "gab:Mode")'` → all modes with purposes (1.8%)

This directly enables the jq-first approach (Layer 1 of the redundancy model).

<!-- section_id: "74d3ebad-be0c-425e-81ed-dfe900e34562" -->
### Finding 3: Three-Layer Redundancy Model (DECIDED)

No single mechanism reliably solves skill invocation. The solution is redundancy:

```
Layer 1 (PRIMARY):   CLAUDE.md jq instructions → agent reads JSON-LD → gets skill mappings
Layer 2 (FALLBACK):  SKILL.md WHEN/WHEN NOT patterns → Claude Code's native matcher
Layer 3 (FALLBACK):  Transpiled .integration.md → auto-generated markdown from JSON-LD
```

See `architecture_decision_reference_chain.md` for the full decision analysis.

<!-- section_id: "565f9224-e92a-4b19-a323-e69ab086d1a4" -->
### Finding 4: Transpiler Concept

A transpiler converts JSON-LD → optimized markdown (`.integration.md`). This provides:
- Same precision as JSON-LD, in the format LLMs read best (markdown)
- Auto-generated, so it can't drift from the source of truth
- No tool calls needed — agent uses Read tool directly
- Third redundancy layer for when jq doesn't run AND skills don't match

---

<!-- section_id: "5420baeb-28f4-4349-93cc-5d9650838dc2" -->
## Structural Requirement: JSON-LD at Every Level

Every layer, stage, sub-layer, sub-stage, and subxn layer/stage should have:

```
any_directory/
├── CLAUDE.md                    ← Lean, references the JSON-LD
├── orchestrator.gab.jsonld      ← For layers (coordinates children)
├── agent.gab.jsonld             ← For stages (executes work)
└── .claude/skills/              ← Skills backed by the JSON-LD
    └── workflow/SKILL.md        ← Markdown translation of JSON-LD precision
```

<!-- section_id: "7cacffd0-d514-459b-8542-5e631194c519" -->
### Scale Analysis

| Level | Count | JSON-LD Exists | Strategy |
|-------|-------|----------------|----------|
| Root + layer_0 + layer_1 + layer_-1 | ~5 | 2 orchestrators | Manual creation |
| Key stages (01-11 per active layer) | ~30 | 67 agent stubs (17 lines each) | Expand stubs with real content |
| Sub-layers | ~20 | 0 | Template-based creation |
| Project-level (school, better_ai_system, etc.) | ~10 | 6 orchestrators (286 lines each) | Already exist, enhance |
| Deeply nested (subxn layers/stages) | ~21,500 | Some stubs | Auto-generate via entity-creation skill |

**Practical approach**: Manual for ~35 key definitions, templates for ~50 more, auto-generate the rest.

---

<!-- section_id: "41125fa4-8684-46c4-a392-5639d8e64495" -->
## Phase 1: CLAUDE.md Chain Optimization (Immediate)

<!-- section_id: "c937bb3e-1754-4222-9edd-e0e8609a45d3" -->
### 1.1 Slim the Static Chain

**Current**: 717 lines across 5 files. **Target**: ~350 lines.

| File | Current | Target | Changes |
|------|---------|--------|---------|
| `~/.claude/CLAUDE.md` | 268 | ~120 | Condense CRITICAL rules (3-5 lines each), remove AALang pseudo-code, move compliance check + scenario table to @imports |
| `~/CLAUDE.md` | 115 | ~30 | Remove ALL duplicate CRITICAL rules, keep only key locations + session start |
| `~/dawson-workspace/CLAUDE.md` | 54 | ~30 | Remove AALang pseudo-code |
| `~/dawson-workspace/code/CLAUDE.md` | 55 | ~30 | Remove AALang pseudo-code |
| `0_layer_universal/CLAUDE.md` | 225 | ~130 | Remove duplicate universal rules, move ASCII structure to @import, replace AALang pseudo-code with references |

<!-- section_id: "b34a9831-59dc-41c9-89a1-6db03687978d" -->
### 1.2 Add Context Loading Instructions for ALL Three Layers

Add ~35-45 lines to the primary CLAUDE.md with instructions that tell the agent to read from ALL three layers AND rules. **Critical**: every layer needs its own explicit "read this" trigger — the agent won't discover skills, `.integration.md` files, or rules on its own.

**Root CLAUDE.md draft** (`~/.claude/CLAUDE.md` or `0_layer_universal/CLAUDE.md`, ~35-45 lines):

```markdown
## AALang Context Loading

Before starting any task, load your context through these steps:

### Step 1: Read JSON-LD graph (primary)
Find and read the nearest AALang agent definition:
  find [working-directory] -maxdepth 2 -name "*.gab.jsonld" -type f | head -5

Read its graph index:
  jq '."@graph"[] | {id: ."@id", type: ."@type", purpose: .purpose} | select(.purpose != null)' [file.jsonld]

Load the mode matching your task:
  jq '."@graph"[] | select(."@id" == "[matched-mode-id]")' [file.jsonld]

Output contains: constraints (MUST/MUST NOT), skills to invoke, transitions.

### Step 2: Review available skills (fallback)
- Read .claude/skills/*/SKILL.md files — each has WHEN/WHEN NOT conditions
- Match conditions to your current task. If a match, invoke with /skill-name
- Key skills: /context-gathering, /stage-workflow, /entity-creation, /handoff-creation

### Step 3: Read integration summaries (second fallback)
- Look for .integration.md files next to any .gab.jsonld files
- These are markdown summaries: modes, constraints, skill mappings, state actors
- Read with the Read tool — no jq needed

### Step 4: Check path-specific rules
- Read applicable rules in .claude/rules/
- Rules contain: directory-specific context, skill references, workflow hints

### Step 5: Follow what you found
- Mode constraints from Step 1 are primary instructions
- Skills matched in Step 2 should be invoked
- Integration summaries (Step 3) provide additional context
- Rules (Step 4) provide directory-specific overrides
```

**Layer-level CLAUDE.md draft** (e.g., `layer_0/CLAUDE.md`, ~20-25 lines):

```markdown
## AALang
- **Agent definition**: ./orchestrator.gab.jsonld
- **Integration summary**: ./orchestrator.integration.md — read for modes, constraints, skill mappings
- **Skills**: /context-gathering (task start), /stage-workflow (stage work), /entity-creation (new entities)
- **Rules**: Check .claude/rules/ for path-specific context

To discover modes: jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose}' ./orchestrator.gab.jsonld
```

**Stage-level CLAUDE.md draft** (e.g., `stage_0_02_research/CLAUDE.md`, ~10-15 lines):

```markdown
## AALang
- **Agent**: ./stage_agent.gab.jsonld
- **Summary**: ./stage_agent.integration.md — read for constraints and skill mappings
- **Skills**: /stage-workflow (primary for this stage)

Run to see this stage's modes: jq '."@graph"[] | select(."@type" == "gab:Mode") | {id: ."@id", purpose: .purpose, skills: .skills}' ./stage_agent.gab.jsonld
```

See `architecture_decision_reference_chain.md` for the complete analysis of why all layers need explicit triggers.

<!-- section_id: "6fcd30b5-5d75-403c-8a9a-190f2333ee4f" -->
### 1.3 Replace Ceremonial AALang with Real References

**Before** (15-25 lines per file):
```markdown
## AALang Integration
@agent ctx:ContextLoadingAgent
### Context Chain Position
- Position: 1 of 5 (User Global)
...
### On Load
ctx:ContextLoadingStateActor.loadedFiles += ~/.claude/CLAUDE.md
ctx:ContextConfidenceStateActor.rulesAwareness += 0.3
```

**After**: Replaced by the layer-appropriate variant from 1.2 above (root, layer, or stage level).

<!-- section_id: "0506f544-f8e7-4ef1-a798-3be048b0c26b" -->
### 1.4 Create @import Targets

```
0_layer_universal/.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/
├── structure_overview.md       ← Full ASCII directory tree (from 0_layer_universal/CLAUDE.md)
├── session_workflow.md         ← Session start protocol (from layer_0/CLAUDE.md)
├── compliance_checklist.md     ← Self-compliance check (from ~/.claude/CLAUDE.md)
└── scenario_rules_index.md    ← Scenario-based rules with paths (from ~/.claude/CLAUDE.md)
```

---

<!-- section_id: "43101404-38e0-41f1-ac8c-a3943dcc96ef" -->
## Phase 2: Path-Specific Rules (Short-term)

Create `.claude/rules/` directory (currently missing). **Critical**: each rules file must contain explicit "read this" instructions that re-trigger all three layers — not just directory-specific hints.

```
.claude/rules/
├── research-context.md
│   paths: layer_-1_research/**
│
├── school-context.md
│   paths: layer_1/layer_1_projects/layer_1_project_school/**
│
├── universal-layer.md
│   paths: layer_0/**
│
├── aalang-context.md
│   paths: layer_0/layer_0_01_ai_manager_system/**
│
└── development-stages.md
    paths: **/stage_*_06_development/**
```

<!-- section_id: "10ee78a6-7098-4bcc-aa9f-e130e9e05b97" -->
### What Rules Files Must Contain

Each rules file includes THREE sections, not just context hints:

**Section 1: Required Reading** (re-triggers all layers)
```markdown
## Required Reading
When working in this directory:
1. Find the `.gab.jsonld` for your role — read the matching `.integration.md` (same base name) for agent behavior context (Layer 3)
2. For precise mode constraints, query the `.gab.jsonld` via jq (Layer 1)
3. Read .claude/skills/*/SKILL.md — check WHEN/WHEN NOT conditions (Layer 2)
```

**Section 2: Skill Usage Table** (explicit skill-to-situation mapping)
```markdown
## Skill Usage
| Situation | Skill | When |
|-----------|-------|------|
| Starting work | /context-gathering | First action in any task |
| Stage transitions | /stage-workflow | When moving between stages |
| Creating entities | /entity-creation | When new features/directories needed |
| Ending session | /handoff-creation | Before closing, to preserve state |
```

**Section 3: Directory-Specific Context** (varies per rules file)
- `research-context.md`: research stage workflow, output-first protocol, source citation rules
- `school-context.md`: writing style rules, assignment structure, Canvas integration hints
- `universal-layer.md`: universal rules enforcement, sub-layer awareness
- `aalang-context.md`: AALang conventions, GAB development workflow, JSON-LD formatting
- `development-stages.md`: implementation standards, testing requirements, commit conventions

**Impact**: Rules load automatically when in matching directories AND they re-trigger all three layers. Even if the agent didn't follow CLAUDE.md's Steps 1-4, entering a matching directory re-injects the same instructions via the rules file.

---

<!-- section_id: "1ec08178-65da-4af5-8016-50531a54beff" -->
## Phase 3: Transpiler + Integration Markdown Companions (Short-term)

**This is Layer 3 of the three-layer redundancy model.**

<!-- section_id: "1c7597ca-233f-478b-a81c-a105322c1636" -->
### 3.1 Build the Transpiler

Create a tool that converts JSON-LD → optimized markdown (`.integration.md`):

```
tools/
└── jsonld-to-md.sh     ← Shell script using jq to extract and format
```

The transpiler extracts from any `.gab.jsonld` file:
- All modes with purposes and trigger conditions
- Mode transition conditions (gates) in plain English
- State actors and what they track
- Skill references (which skills to invoke in which modes)
- Constraints (MUST/MUST NOT) per mode

**Implementation options** (in order of priority):
1. **Shell script using jq** — works today, produces clean markdown tables
2. **Claude Code skill** (`/transpile-jsonld`) — invokable on demand, uses jq internally
3. **Node.js/Python script** — richer handling of edge cases, for later

<!-- section_id: "6432d817-afe8-4105-856a-b83ac5e86b24" -->
### 3.2 Generate Integration Companions

Run the transpiler on key JSON-LD files:

```
layer_0/layer_0_01_ai_manager_system/personal/
├── layer_0_orchestrator.gab.jsonld           ← Source of truth (701 lines)
└── layer_0_orchestrator.integration.md        ← AUTO-GENERATED: ~50-80 lines

layer_0/layer_0_03_context_agents/
├── context_loading.gab.jsonld                ← Source of truth (1065 lines)
└── context_loading.integration.md             ← AUTO-GENERATED: ~40-60 lines
```

The `.integration.md` contains (auto-generated, not hand-written):
- Header noting it's auto-generated with timestamp and source file
- Modes table: mode ID, purpose, trigger conditions
- Mode transitions: from → to with gate conditions in plain English
- State actors table: actor ID, what it tracks, persistence scope
- **Skill mapping table**: situation → skill → when to use (critical for Layer 3 fallback)
- Constraints per mode: MUST/MUST NOT lists
- Source reference back to the JSON-LD file

<!-- section_id: "e9593de0-9a12-41fc-a247-6d2a70c7398e" -->
### 3.3 Keep in Sync

The transpiler runs:
- On entity-creation (new layer/stage → generate JSON-LD → immediately transpile)
- On JSON-LD modification (pre-commit hook or manual step)
- Both files are committed together — JSON-LD + .integration.md in same commit

**Key principle**: `.integration.md` is NEVER hand-edited. It's always regenerated from JSON-LD. This prevents sync drift — the markdown always matches the source of truth.

---

<!-- section_id: "6c540529-9498-446b-9c0d-714c990258cc" -->
## Phase 4: Enhance Existing Skills (Medium-term)

<!-- section_id: "1d580419-ff98-4078-af10-c9f6f83ba338" -->
### 4.1 Improve Root Skills with WHEN/WHEN NOT Patterns

| Skill | Current Lines | Enhancement |
|-------|--------------|-------------|
| `context-gathering` | 24 | Add: references `context_loading.gab.jsonld`, WHEN/WHEN NOT triggers, mode transition conditions |
| `handoff-creation` | 26 | Add: references orchestrator handoff patterns, standardized format template, validation checklist |
| `entity-creation` | 85 | Add: references `gab.jsonld` for proper actor creation, auto-generate JSON-LD stubs for new entities |
| `stage-workflow` | 91 | Add: references stage agent definitions, mode-specific instructions per stage |

<!-- section_id: "aeda3b59-c171-4d98-8196-b03fbd09eec5" -->
### 4.2 Create New Skills

| Skill | Purpose | Backed By |
|-------|---------|-----------|
| `aalang-load` | Reads a `.jsonld` file, extracts key patterns, presents as markdown | `gab.jsonld`, `gab-runtime.jsonld` |
| `aalang-navigate` | Selective navigation of JSON-LD graphs — reads top-level, drills into specific nodes | `index.jsonld` |
| `team-create` | Creates Agent Team from layer structure — generates spawn prompts with context | orchestrator definitions |

<!-- section_id: "a630b08a-faf0-4a57-a6c7-c415b6bbf173" -->
### 4.3 Improve Skill Descriptions for Better Invocation

Current problem: skills exist but Claude Code doesn't invoke them because descriptions are vague.

JSON-LD-informed improvement pattern:
```markdown
# Before (vague)
description: "Use this skill when you need to understand the current location"

# After (precise, from JSON-LD mode conditions)
description: "Use when starting a new task AND current layer/stage is unknown.
DO NOT use when layer/stage already identified in this session.
TRIGGERS: user says 'where am I', session start, task requires knowing project context."
```

---

<!-- section_id: "3ac9147a-3eea-4874-b20a-24edd575102e" -->
## Phase 5: Fill JSON-LD Definitions (Medium-term)

<!-- section_id: "f46a4156-17da-4cbb-a1bf-04b8a3eacf31" -->
### 5.1 Manual Creation (~35 key definitions)

| Location | Type | Priority |
|----------|------|----------|
| `0_layer_universal/` | Root orchestrator | HIGH |
| `layer_0/` | Layer 0 orchestrator | HIGH |
| `layer_1/` | Layer 1 orchestrator | HIGH |
| `layer_-1_research/` | Research layer orchestrator | HIGH |
| `stage_*_01` through `stage_*_11` (layer 0) | Stage agents | HIGH |
| Key sub-layers (`sub_layer_0_01` through `sub_layer_0_05`) | Sub-layer agents | MEDIUM |

<!-- section_id: "f9484e24-81df-4643-9d3a-10601c3d1124" -->
### 5.2 Template-Based Creation (~50 definitions)

Create GAB templates that can be parameterized:
- `orchestrator_template.gab.jsonld` — for new layers
- `stage_agent_template.gab.jsonld` — for new stages
- `sub_layer_agent_template.gab.jsonld` — for new sub-layers

<!-- section_id: "9199f8c0-5b5a-4026-b495-49830943b8dc" -->
### 5.3 Auto-Generation (ongoing)

Update `entity-creation` skill to:
1. Create the directory structure
2. Generate JSON-LD from template with layer/stage parameters
3. Generate CLAUDE.md with references to the JSON-LD
4. Generate `.integration.md` companion
5. Generate SKILL.md if it's a stage (workflow skill)

---

<!-- section_id: "a0b0563d-f078-4434-b971-35d396d28089" -->
## Phase 6: Agent Teams Persistence (Longer-term)

Bridge AALang orchestrator definitions with Claude Code Agent Teams:

1. Orchestrator JSON-LD defines team structure (who spawns, who coordinates, what state to track)
2. `/team-create` skill reads the orchestrator, generates spawn prompts with proper context
3. Hand-off documents persist team state between sessions
4. State actors defined in JSON-LD map to `context_state.json` or similar persistence

---

<!-- section_id: "1381bfed-edde-4781-9b9d-2debbf7d2d10" -->
## Implementation Priority

| Phase | Impact | Effort | Do When |
|-------|--------|--------|---------|
| 1: CLAUDE.md optimization | HIGH | LOW | **Immediate** |
| 2: Path-specific rules | HIGH | LOW | **Immediate** |
| 3: Integration companions | MEDIUM | LOW | Short-term |
| 4: Skill enhancement | HIGH | MEDIUM | Short-term |
| 5: JSON-LD definitions | MEDIUM | HIGH | Medium-term |
| 6: Agent Teams persistence | HIGH | HIGH | Longer-term |

---

<!-- section_id: "31396327-4d2b-48cf-9187-32099c74b807" -->
## Success Criteria

| Problem | Metric | Target |
|---------|--------|--------|
| 1. Instructions lost | Static chain line count | <400 lines (from 717) |
| 2. Agent Teams ephemeral | Teams can resume from hand-off docs | Manual test: spawn team, close session, resume |
| 3. Skills not being used | Skill invocation rate | Claude Code invokes skills when conditions match (manual testing) |
| 4. Context efficiency | On-demand vs static ratio | >60% of context loaded dynamically (via skills/rules) |
| 5. Markdown vs JSON-LD | Both formats coexist | JSON-LD definitions exist alongside markdown runtime docs |

---

<!-- section_id: "3d24d4e6-ce8d-4690-94a8-461d551de9e0" -->
## Dependencies

| Depends On | For |
|-----------|-----|
| Professor's upstream AALang (synced) | Latest language spec for JSON-LD definitions |
| Claude Code @import feature | CLAUDE.md @imports to work |
| Claude Code path-specific rules | `.claude/rules/*.md` with `paths:` frontmatter |
| Research verification (completed 2026-02-07) | Understanding what works and what doesn't |

---

*Implementation plan for: layer_0_feature_aalang_integration*
*Created: 2026-02-07*
*Status: APPROVED — ready for phased execution*
*Approach: Hybrid (JSON-LD source-of-truth + markdown runtime + skills bridge)*
