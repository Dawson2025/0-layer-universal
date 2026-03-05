---
resource_id: "47ef2597-0853-4206-a3c6-11a7bfea06cd"
resource_type: "output"
resource_name: "agent_amnesia_and_context_systems_conversation"
---
# Agent Amnesia and Context Systems - Research Conversation

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Date**: 2026-01-30
**Session Topic**: Making AI agents remember their identity, traversal, instantiation, and communication protocols

---

## Problem Statement

AI agents in the layer-stage system "forget" critical information:
1. **Who they are** (identity at their layer/stage)
2. **How to traverse** the AI system hierarchy
3. **How to instantiate** new things at their level
4. **How to communicate** with other agents via handoffs

The prompts in `sub_layer_0_01_prompts/` are outdated and don't address these issues.

---

## Research Conducted

### Internal System Exploration

**What Already Exists (Strong Foundation):**

| Component | Status | Location |
|-----------|--------|----------|
| Layer-Stage Framework | Defined | `layer_1_feature_layer_stage_system/` |
| Handoff Protocol Schema | Defined | `things_learned/ideal_ai_manager_hierarchy_system/` |
| CLAUDE.md Cascade | Working | Throughout system |
| Context Gathering Rules | Fragmented | `layer_0_01_ai_manager_system/agnostic/` |
| Manager/Worker Patterns | ~57% researched | `layer_0_feature_ai_manager_hierarchy_system/` |
| Persona Library | Defined | `things_learned/ideal_ai_manager_hierarchy_system/persona_library.md` |
| Instantiation Guide | Defined | `layer_1_feature_layer_stage_system/.../instantiation_guide.md` |

**Key Gaps Identified:**

1. **Identity is implicit, not explicit** - Agents derive identity from filesystem position but don't have explicit identity declaration
2. **No mandatory traversal protocol** - Context gathering rules exist but aren't enforced
3. **Instantiation not discoverable** - Guide exists but agents don't know how to find it
4. **Handoffs missing types** - No acknowledgment, query, or context negotiation handoffs

### External Research

**Document Created**: `agent_amnesia_external_approaches.md`

**Key Findings:**

1. **Context-related failures = 41.8% of all agent failures** (largest category)

2. **Industry convergence on three-layer memory:**
   | Layer | Purpose | Implementation |
   |-------|---------|----------------|
   | Immediate | Current session | Messages list, checkpoints |
   | Episodic | Completed tasks | Vector DB + metadata |
   | Semantic | General knowledge | Knowledge graphs |

3. **Framework Approaches:**
   - LangGraph: Explicit graph-based state with dual memory
   - AutoGen: Event-driven architecture with persistable events
   - CrewAI: Role-based agents with crew-level memory sharing
   - OpenAI: Session abstraction with automatic compaction
   - Anthropic: Tool search pattern, programmatic tool calling, Claude Code harness

4. **Critical Insight**: Claude Code uses:
   - TODO lists injected into system prompt
   - Mandatory verification before task completion
   - Self-awareness context (remaining tokens, available tools)

---

## Proposed Solution: Agent Awakening Protocol

### 1. Self-Referential System Prompt Template

Every CLAUDE.md should inject dynamic identity:

```markdown
## Agent Identity

You are an agent operating in the Layer-Stage Framework.

**Current Position:**
- Layer: {layer_number} ({layer_name})
- Stage: {stage_number} ({stage_name})
- Role: {role_from_CLAUDE.md}
- Scope: {what_you_can_and_cannot_do}

**Available Actions:**
- TRAVERSE UP: Escalate to {parent_layer_or_stage}
- TRAVERSE DOWN: Delegate to {child_layers_or_stages}
- INSTANTIATE: Create {what_can_be_created_here}
- COMMUNICATE: Write handoffs to {handoff_locations}

**Mandatory First Steps:**
1. Verify you understand your identity
2. Check hand_off_documents/incoming/ for tasks
3. Read status.json for current state
```

### 2. Mandatory Traversal Protocol

```
1. SYNC: git pull
2. LOCATE: Identify current layer + stage from path
3. LOAD CHAIN: Read CLAUDE.md from root → current
4. LOAD RULES: Read sub_layer_0_04_rules/ (always)
5. CHECK STATE: Read status.json if exists
6. CHECK HANDOFFS: Read hand_off_documents/incoming/
7. DECLARE: State your identity and understanding
```

### 3. Enhanced Handoff Types

| Type | Purpose | When |
|------|---------|------|
| **Task** | Assign work | Delegating down |
| **Result** | Report completion | Returning up |
| **Query** | Request clarification | Blocked/confused |
| **Acknowledgment** | Confirm receipt | After receiving any handoff |
| **Context** | Share understanding | Before starting work |

### 4. Instantiation Discovery

Each CLAUDE.md should include what can be created at that level.

### 5. Episodic Memory via Searchable Handoffs

Add keywords and summaries to handoff metadata for future retrieval.

---

## Current Discussion: AGNOSTIC.md System

### User Question

How to create an AGNOSTIC.md system that:
1. Feeds into different tools (Claude Code, Codex, Gemini, Cursor)
2. Uses Claude Code's .claude/ system efficiently
3. Manages context in the most token-efficient way

### Research Direction

Need to understand:
1. What goes in CLAUDE.md vs .claude/ for Claude Code
2. When each is loaded (every call vs on-demand)
3. How to design AGNOSTIC.md as source of truth that transforms to tool-specific formats

### Existing Research on Tool Quartets

From `os_and_quartets.md`:
- **Quartets** = tool-specific context files per OS:
  - `CLAUDE.md` - Claude Code
  - `AGENTS.md` - Codex CLI
  - `GEMINI.md` - Gemini CLI
  - `.cursor/rules/*.mdc` - Cursor IDE

- OS treated as separate dimension from layer/stage/tool
- `os/<os-id>/` subfolders contain OS-specific variants
- Tools cascade context from generic → OS-specific

### Open Questions

1. **Where should Agent Awakening Protocol live?**
   - In `universal_init_prompt.md`?
   - In each CLAUDE.md?
   - As a skill?

2. **How dynamic should identity injection be?**
   - Static templates per layer/stage?
   - Generated at runtime?

3. **AGNOSTIC.md design:**
   - Single source file that transpiles to tool-specific formats?
   - Shared core + tool-specific extensions?
   - How to handle tool-specific features (Claude Code's .claude/)?

4. **Context efficiency for Claude Code:**
   - What belongs in CLAUDE.md (always loaded)?
   - What belongs in .claude/ (on-demand)?
   - How to minimize token usage while maintaining agent coherence?

---

## Claude Code Context System Research

### Key Finding: CLAUDE.md Loaded EVERY Request

CLAUDE.md is NOT cached - it's loaded fresh every API call. This is critical for context efficiency.

### Loading Timing & Context Cost

| Component | When Loaded | Context Cost | On-Demand? |
|-----------|-------------|--------------|------------|
| **CLAUDE.md** | Every request | Very high | No |
| **.claude/rules/*.md** | Every request | Medium | No |
| **Skills** (descriptions) | Session start | Low | Yes (full content) |
| **Skills** (full content) | When invoked | High | Yes |
| **Subagents** | On delegation | Isolated | Yes |
| **Hooks** | On trigger | Zero | N/A |

### Cascade Order (Highest to Lowest Priority)

1. Managed policy (`/etc/claude-code/CLAUDE.md`)
2. Project root (`./CLAUDE.md`)
3. User level (`~/.claude/CLAUDE.md`)
4. Subdirectories (`./packages/foo/CLAUDE.md` - on-demand)
5. Local overrides (`./CLAUDE.local.md` - not git-tracked)

### What Goes Where - Decision Matrix

| Content Type | CLAUDE.md | Skills | Subagents | Hooks | Notes |
|--------------|-----------|--------|-----------|-------|-------|
| **Coding standards** | ✅ Yes | ❌ No | ❌ No | ❌ No | Always-on rules |
| **Build commands** | ✅ Yes | ❌ No | ❌ No | ❌ No | Bash commands Claude can't guess |
| **API style guide** | ⚠️ Brief | ✅ Yes | ❌ No | ❌ No | Load only when needed |
| **Domain knowledge** | ❌ No | ✅ Yes | ❌ No | ❌ No | Reference on-demand |
| **Workflow (deploy)** | ❌ No | ✅ Yes | ⚠️ Maybe | ❌ No | Use skill; subagent if reads many files |
| **Auto-formatting** | ❌ No | ❌ No | ❌ No | ✅ Yes | Must happen every time |
| **Read-only research** | ❌ No | ❌ No | ✅ Yes | ❌ No | Isolate file reads |

### Size Guidelines

- **CLAUDE.md**: Under 500 lines (~3,000-5,000 tokens)
- **Skills**: Per skill under 500 lines
- **Subagents**: For any investigation reading 10+ files
- **MCP servers**: Disable when not in use

### Key Optimization Strategies (Ranked by Impact)

1. **Aggressive context clearing** (`/clear` between tasks) - saves 30-50%
2. **Proactive compaction** (`/compact` at 70% full) - saves 20-40%
3. **Move instructions to skills** (not CLAUDE.md) - saves 5-15%
4. **Use subagents for verbose ops** - saves 10-30%
5. **Reduce MCP server overhead** - saves 5-10%

---

## AGNOSTIC.md System Design

### The Proposal

Create a single **AGNOSTIC.md** as the source of truth that:
1. Contains ALL context in a tool-agnostic format
2. Has clear sections that map to tool-specific structures
3. Can be transformed/extracted into:
   - `CLAUDE.md` + `.claude/` for Claude Code
   - `AGENTS.md` for Codex CLI
   - `GEMINI.md` for Gemini CLI
   - `.cursor/rules/*.mdc` for Cursor IDE

### Proposed AGNOSTIC.md Structure

```markdown
# AGNOSTIC.md

## @always
<!-- Content that should be in system prompt for ALL tools -->
<!-- Maps to: CLAUDE.md core, AGENTS.md core, GEMINI.md core -->
- Coding standards
- Build commands
- Critical rules

## @on-demand
<!-- Content loaded only when needed -->
<!-- Maps to: .claude/skills/, referenced from AGENTS.md -->
### @skill:deploy
Deploy workflow instructions...

### @skill:api-conventions
API style guide...

## @agent-definitions
<!-- Role definitions for isolated workers -->
<!-- Maps to: .claude/agents/ -->
### @agent:code-reviewer
Code review instructions...

## @file-rules
<!-- Path-specific rules -->
<!-- Maps to: .claude/rules/, .cursor/rules/ -->
### @paths: src/**/*.ts
TypeScript-specific rules...

## @automation
<!-- Deterministic automation hooks -->
<!-- Maps to: .claude/hooks/, shell scripts -->
### @hook:post-edit
Format code after editing...

## @os-specific
<!-- OS-variant content -->
### @os:wsl
WSL-specific instructions...

### @os:macos
macOS-specific instructions...
```

### Transformation Rules

| AGNOSTIC.md Section | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------------------|-------------|-----------|------------|--------|
| `@always` | CLAUDE.md (core) | AGENTS.md (core) | GEMINI.md | `.cursor/rules/core.mdc` |
| `@on-demand` | `.claude/skills/` | Inline reference | Manual merge | N/A |
| `@agent-definitions` | `.claude/agents/` | N/A | N/A | N/A |
| `@file-rules` | `.claude/rules/` | N/A | N/A | `.cursor/rules/` |
| `@automation` | `.claude/hooks/` | Shell scripts | Shell scripts | Shell scripts |
| `@os-specific` | `os/<id>/CLAUDE.md` | `os/<id>/AGENTS.md` | `os/<id>/GEMINI.md` | `os/<id>/.cursor/` |

### For Claude Code Specifically

**Most context-efficient approach:**

1. **CLAUDE.md** (always loaded, <500 lines):
   - Extract from `@always` section
   - Keep extremely lean
   - Focus on: coding standards, build commands, critical rules
   - Reference skills for details: "For API conventions, use /api-conventions skill"

2. **.claude/skills/** (on-demand):
   - Extract from `@on-demand` sections
   - All domain knowledge, reference material
   - Workflow instructions (deploy, review, etc.)

3. **.claude/agents/** (isolated):
   - Extract from `@agent-definitions`
   - Code reviewer, debugger, researcher, etc.
   - Each runs in isolated context

4. **.claude/rules/** (auto-loaded but path-specific):
   - Extract from `@file-rules`
   - TypeScript rules, Python rules, etc.
   - Only loads when working with matching files

5. **.claude/hooks/** (deterministic):
   - Extract from `@automation`
   - Formatting, validation, logging

### Implementation Options

**Option A: Manual Extraction**
- Write AGNOSTIC.md as source
- Manually copy/extract to tool-specific files
- Pro: Simple, no tooling needed
- Con: Can drift, maintenance overhead

**Option B: Build Script**
- Write AGNOSTIC.md with markers
- Script parses and generates tool-specific files
- Pro: Single source of truth, always in sync
- Con: Need to build/maintain script

**Option C: Symlinks + Includes**
- AGNOSTIC.md as main file
- Tool-specific files use @imports or symlinks
- Pro: DRY, no build step
- Con: Not all tools support imports equally

### Recommended Approach for Claude Code

**Option B with this structure:**

```
layer_X/
├── AGNOSTIC.md                    # Source of truth
├── CLAUDE.md                      # Generated: @always + tool shim
├── AGENTS.md                      # Generated: @always + tool shim
├── GEMINI.md                      # Generated: @always + tool shim
├── .claude/
│   ├── skills/                    # Generated from @on-demand
│   │   ├── deploy/SKILL.md
│   │   └── api-conventions/SKILL.md
│   ├── agents/                    # Generated from @agent-definitions
│   │   └── code-reviewer.md
│   ├── rules/                     # Generated from @file-rules
│   │   └── typescript.md
│   └── hooks/                     # Generated from @automation
│       └── format.sh
└── os/
    ├── wsl/CLAUDE.md              # Generated from @os-specific:wsl
    └── macos/CLAUDE.md            # Generated from @os-specific:macos
```

---

---

## Final Design: Dual AGNOSTIC.md + .agnostic/ System

### The Insight

The cleanest design has BOTH:
- **AGNOSTIC.md** = Lean, always-loaded content (like CLAUDE.md)
- **.agnostic/** = Structured, on-demand resources (like .claude/)

This mirrors exactly how Claude Code separates concerns.

### Complete Structure

```
layer_X/
├── AGNOSTIC.md                     # SOURCE: Always-loaded content
│   └── Identity, traversal, standards, commands (~300 lines)
│
├── .agnostic/                      # SOURCE: On-demand structured content
│   ├── skills/
│   │   ├── deploy/SKILL.md
│   │   └── api-conventions/SKILL.md
│   ├── agents/
│   │   └── code-reviewer.md
│   ├── rules/
│   │   └── typescript.md
│   ├── automation/
│   │   └── format.sh
│   └── os/
│       ├── wsl/
│       └── macos/
│
├── CLAUDE.md                       # GENERATED from AGNOSTIC.md + Claude shim
├── AGENTS.md                       # GENERATED from AGNOSTIC.md + Codex shim
├── GEMINI.md                       # GENERATED from AGNOSTIC.md + Gemini shim
│
├── .claude/                        # GENERATED from .agnostic/ + Claude-specific
│   ├── skills/                     # ← .agnostic/skills/
│   ├── agents/                     # ← .agnostic/agents/
│   ├── rules/                      # ← .agnostic/rules/
│   ├── hooks/                      # ← .agnostic/automation/
│   ├── settings.json               # Claude-only (not from .agnostic/)
│   └── mcp.json                    # Claude-only
│
├── .cursor/                        # GENERATED from .agnostic/ + Cursor-specific
│   └── rules/*.mdc                 # ← .agnostic/rules/ (converted)
│
└── os/
    ├── wsl/
    │   ├── CLAUDE.md               # ← .agnostic/os/wsl/ + AGNOSTIC.md
    │   └── AGENTS.md
    └── macos/
        └── ...
```

### Transformation Rules

| Source | → Target | Notes |
|--------|----------|-------|
| AGNOSTIC.md | CLAUDE.md | + Claude shim header |
| AGNOSTIC.md | AGENTS.md | + Codex first-message format |
| AGNOSTIC.md | GEMINI.md | + Gemini systemInstruction format |
| .agnostic/skills/ | .claude/skills/ | Direct copy |
| .agnostic/agents/ | .claude/agents/ | Direct copy |
| .agnostic/rules/ | .claude/rules/ | Direct copy |
| .agnostic/rules/ | .cursor/rules/*.mdc | Format conversion |
| .agnostic/automation/ | .claude/hooks/ | Direct copy |
| .agnostic/os/<id>/ | os/<id>/CLAUDE.md | Merge with AGNOSTIC.md |

### Why This Is Clean

1. **Clear separation**: AGNOSTIC.md = always-on, .agnostic/ = on-demand
2. **Mirrors tool architecture**: Same pattern as CLAUDE.md + .claude/
3. **Tool-specific additions work**: .claude/settings.json, .claude/mcp.json
4. **Single source of truth per concern**: No duplication, no drift

### AGNOSTIC.md Template

```markdown
# AGNOSTIC.md - Layer X, Stage Y

## Identity
You are an agent at Layer X (Project), Stage Y (Research).
- **Role**: [role description]
- **Scope**: [what you can and cannot do]
- **Parent**: [path to parent]
- **Children**: [paths to children]

## Navigation
- **UP**: Escalate to `../AGNOSTIC.md` when [conditions]
- **DOWN**: Delegate to `[child]/AGNOSTIC.md` when [conditions]
- **ACROSS**: Coordinate with `[sibling]/` when [conditions]

## Instantiation
You can create:
- New [entity type]: Use `/instantiation` skill
- New [entity type]: Use `/instantiation` skill

## Commands
- Build: `npm run build`
- Test: `npm run test`
- Lint: `npm run lint`

## Standards
- [Critical standard 1]
- [Critical standard 2]
- For details, use `/coding-standards` skill

## Skills Available
- `/stage-workflow` - How to work in this stage
- `/domain-knowledge` - Reference material for this domain
- `/instantiation` - How to create child entities
- `/handoff-protocol` - How to communicate via handoffs

## Handoffs
- **Check incoming**: `hand_off_documents/incoming/`
- **Write outgoing**: `hand_off_documents/outgoing/`
- **Format**: See `/handoff-protocol` skill
```

---

## Earlier Design: .agnostic/ Folder System

### The Problem with Context Gathering

Agents currently spend significant time/resources gathering context at session start. But with the layer-stage system, an agent instantiated at the correct location **should already have most of what it needs**.

**The insight**:
- CLAUDE.md at each layer/stage = lean pointer file
- .claude/skills/ = the actual content (loaded on-demand)
- Agent identity + traversal + instantiation instructions = in CLAUDE.md
- Domain knowledge + reference material = in skills

### Proposed .agnostic/ Folder Structure

Instead of AGNOSTIC.md as a single file, use a **folder structure** that mirrors what tools need:

```
layer_X/
├── .agnostic/                      # SOURCE OF TRUTH
│   ├── always/                     # Content for every request
│   │   ├── identity.md             # Agent identity at this layer
│   │   ├── traversal.md            # How to navigate hierarchy
│   │   ├── instantiation.md        # How to create children
│   │   ├── standards.md            # Coding standards
│   │   └── commands.md             # Build/test commands
│   ├── skills/                     # On-demand content
│   │   ├── deploy/
│   │   │   └── SKILL.md
│   │   ├── api-conventions/
│   │   │   └── SKILL.md
│   │   └── ...
│   ├── agents/                     # Role definitions
│   │   ├── code-reviewer.md
│   │   ├── researcher.md
│   │   └── ...
│   ├── rules/                      # Path-specific rules
│   │   ├── typescript.md
│   │   ├── python.md
│   │   └── ...
│   ├── automation/                 # Hooks/scripts
│   │   ├── post-edit.sh
│   │   └── ...
│   └── os/                         # OS-specific overrides
│       ├── wsl/
│       ├── macos/
│       └── ...
│
├── .claude/                        # GENERATED + CLAUDE-SPECIFIC
│   ├── settings.json               # Claude-specific settings
│   ├── skills/                     # Synced from .agnostic/skills/
│   ├── agents/                     # Synced from .agnostic/agents/
│   ├── rules/                      # Synced from .agnostic/rules/
│   ├── hooks/                      # Synced from .agnostic/automation/
│   └── claude-specific/            # Claude-only additions
│       └── mcp-servers.json
│
├── .cursor/                        # GENERATED + CURSOR-SPECIFIC
│   └── rules/                      # Synced from .agnostic/rules/
│       └── *.mdc                   # Cursor format
│
├── CLAUDE.md                       # GENERATED: .agnostic/always/* merged
├── AGENTS.md                       # GENERATED: .agnostic/always/* + Codex shim
├── GEMINI.md                       # GENERATED: .agnostic/always/* + Gemini shim
│
└── src/                            # ACTUAL CODE (not in .claude/)
    └── ...
```

### Sync Rules

| .agnostic/ Source | → Claude Code | → Codex | → Cursor | Notes |
|-------------------|---------------|---------|----------|-------|
| `always/` | CLAUDE.md | AGENTS.md | .cursor/rules/core.mdc | Merged into main file |
| `skills/` | .claude/skills/ | Inline in AGENTS.md | N/A | On-demand |
| `agents/` | .claude/agents/ | N/A | N/A | Claude-specific |
| `rules/` | .claude/rules/ | N/A | .cursor/rules/ | Path-specific |
| `automation/` | .claude/hooks/ | Shell scripts | Shell scripts | Deterministic |
| `os/<id>/` | os/<id>/CLAUDE.md | os/<id>/AGENTS.md | os/<id>/.cursor/ | OS variants |

### Tool-Specific Overrides

Each tool folder can have additions that don't exist in .agnostic/:

```
.claude/
├── skills/                     # Synced from .agnostic/
│   ├── deploy/                 # From .agnostic/skills/deploy/
│   └── claude-specific-skill/  # Claude-only (not in .agnostic/)
├── settings.json               # Claude-only (not in .agnostic/)
└── mcp.json                    # Claude-only (not in .agnostic/)
```

---

## Should Code Files Be Inside .claude/?

**Short answer: NO.**

### Why Not

1. **.claude/ is for meta-configuration**, not application code
2. **Build systems would break** - webpack, tsc, pytest don't look in .claude/
3. **IDEs would be confused** - file trees, go-to-definition, etc.
4. **Version control semantics** - .claude/ often has local overrides
5. **Other tools need the code** - linters, formatters, CI/CD
6. **Violates separation of concerns** - context ≠ code

### What DOES Help Claude Find Code

1. **@imports in CLAUDE.md**:
   ```markdown
   # Key Files
   @src/index.ts for entry point
   @src/api/routes.ts for API structure
   ```

2. **Explicit pointers**:
   ```markdown
   # Project Structure
   - Entry: src/index.ts
   - API routes: src/api/
   - Components: src/components/
   ```

3. **Skills with file references**:
   ```markdown
   # .claude/skills/codebase-overview/SKILL.md
   Key files to understand this codebase:
   - @src/index.ts - entry point
   - @src/api/ - all API routes
   ```

4. **Code intelligence via MCP** (if available):
   - Tree-sitter parsing
   - Symbol indexing
   - Semantic search

---

## The Optimal Pattern: Layer-Stage + .agnostic/

### At Each Layer/Stage

```
layer_X_stage_Y/
├── .agnostic/
│   ├── always/
│   │   ├── identity.md          # "You are at layer X, stage Y..."
│   │   ├── traversal.md         # "Go UP to..., DOWN to..., ACROSS to..."
│   │   └── instantiation.md     # "You can create..."
│   └── skills/
│       └── stage-specific/      # Domain knowledge for this stage
│
├── .claude/                     # Generated
├── CLAUDE.md                    # Generated (lean, references skills)
│
├── hand_off_documents/          # Communication
├── outputs/                     # Work products
└── status.json                  # Current state
```

### CLAUDE.md at Each Level (Generated, <300 lines)

```markdown
# Layer X - Stage Y

## Identity
You are an agent at Layer X (Project), Stage Y (Research).
Your role is: [role]
Your scope is: [scope]

## Navigation
- UP: Escalate to ../CLAUDE.md
- DOWN: Delegate to [children]
- ACROSS: Coordinate with [siblings]

## Available Actions
- INSTANTIATE: See /instantiation skill
- HANDOFF: Write to hand_off_documents/outgoing/

## Skills (use when needed)
- /stage-workflow - How to work in this stage
- /domain-knowledge - Reference material
- /instantiation - How to create children

## Commands
- Build: npm run build
- Test: npm run test

## Standards
[Brief, critical-only standards]
```

### Context Loading Efficiency

| What | Loaded When | Token Cost |
|------|-------------|------------|
| CLAUDE.md identity section | Every request | ~500 tokens |
| CLAUDE.md commands | Every request | ~200 tokens |
| CLAUDE.md standards | Every request | ~300 tokens |
| Skills (descriptions) | Session start | ~100 tokens each |
| Skills (full content) | On invocation | ~2000 tokens |
| Handoff documents | When checking | Variable |
| Code files | When needed | Variable |

**Total always-on**: ~1000-1500 tokens (vs ~5000+ if everything in CLAUDE.md)

---

## Sync Script Design

### What It Does

```bash
# sync-agnostic.sh

# 1. Merge .agnostic/always/* → CLAUDE.md
cat .agnostic/always/*.md > CLAUDE.md

# 2. Copy .agnostic/skills/ → .claude/skills/
rsync -av .agnostic/skills/ .claude/skills/

# 3. Copy .agnostic/agents/ → .claude/agents/
rsync -av .agnostic/agents/ .claude/agents/

# 4. Convert .agnostic/rules/ → .claude/rules/ AND .cursor/rules/
for rule in .agnostic/rules/*.md; do
  cp "$rule" ".claude/rules/"
  convert-to-mdc "$rule" > ".cursor/rules/$(basename $rule .md).mdc"
done

# 5. Copy .agnostic/automation/ → .claude/hooks/
rsync -av .agnostic/automation/ .claude/hooks/

# 6. Generate AGENTS.md, GEMINI.md with tool shims
generate-agents-md .agnostic/always/ > AGENTS.md
generate-gemini-md .agnostic/always/ > GEMINI.md

# 7. Handle OS variants
for os in .agnostic/os/*/; do
  os_id=$(basename "$os")
  mkdir -p "os/$os_id"
  cat "$os"/*.md > "os/$os_id/CLAUDE.md"
done
```

### When to Run

- **Git hook (post-checkout, post-merge)**: Auto-sync on pulls
- **File watcher**: Auto-sync on .agnostic/ changes
- **Manual**: Before committing

---

## Next Steps

1. ✅ Research Claude Code's .claude/ system in detail
2. ✅ Design .agnostic/ folder structure
3. Define exact sync rules and script
4. Create template .agnostic/ for layer-stage system
5. Implement sync script
6. Test with existing layers/stages
7. Document for other agents

---

## Sources

### Internal
- `layer_-1_research/layer_-1_better_ai_system/` - All feature research
- `sub_layer_0_01_prompts/universal_init_prompt.md` - Current init prompt
- `sub_layer_0_04_rules/` - Universal rules
- `things_learned/ideal_ai_manager_hierarchy_system/` - Manager hierarchy research

### External (from agent_amnesia_external_approaches.md)
- LangGraph Memory Documentation
- AutoGen Documentation
- CrewAI Memory Documentation
- OpenAI Agents SDK
- Anthropic Advanced Tool Use
- Anthropic Context Engineering
- Academic papers on LLM agent memory
