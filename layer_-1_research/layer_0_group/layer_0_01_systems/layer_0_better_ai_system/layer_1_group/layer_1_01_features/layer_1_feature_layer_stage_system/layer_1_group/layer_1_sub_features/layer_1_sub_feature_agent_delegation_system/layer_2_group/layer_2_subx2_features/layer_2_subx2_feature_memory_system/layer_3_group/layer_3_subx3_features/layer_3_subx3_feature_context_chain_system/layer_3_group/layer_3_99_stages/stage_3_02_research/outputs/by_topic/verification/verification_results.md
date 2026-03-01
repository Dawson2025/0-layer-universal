# Verification Results

Research conducted 2026-02-07 across 5 parallel research agents. This file documents what was verified as true, what was false, and what needs correction in our other research files.

---

## CORRECTIONS NEEDED (Things We Got Wrong)

### C1: JSON-LD is WORSE for LLMs, Not Better

**Our assumption**: JSON-LD's graph structure would be more precise for agent instructions than markdown.

**Reality**: Research shows JSON-LD is the **worst-performing** structured format for LLMs:
- KG-LLM-Bench (arXiv:2504.07087): JSON-LD scored 0.34 avg accuracy vs 0.42 for plain JSON
- JSON-LD consumes 3-5x more tokens than equivalent markdown
- LLMs process linear token sequences, not graph structures — the linked-data overhead provides no comprehension benefit
- Zero major agent frameworks (LangChain, AutoGPT, CrewAI, MCP, Claude Code) use JSON-LD for instructions
- Recommended format hierarchy: **Markdown > YAML > JSON Schema > XML tags > JSON > JSON-LD**

**Impact**: The "markdown as surface, JSON-LD as depth" vision in `problems_and_vision.md` is invalid. Need a different approach.

**Source**: arXiv:2504.07087, arXiv:2411.10541, shshell.com token benchmarks

---

### C2: AALang Annotations in CLAUDE.md Are Plain Text

**Our assumption**: `@agent ctx:ContextLoadingAgent` and `ctx:ContextLoadingStateActor.loadedFiles` constructs in CLAUDE.md are recognized by Claude Code.

**Reality**: Claude Code treats CLAUDE.md as **plain markdown** with only two extensions:
1. `@path/to/file` import syntax (max 5 hops)
2. YAML frontmatter `paths:` field (for `.claude/rules/` files only)

The AALang state actor annotations, context chain position numbering, and `@agent` directives are read as text that Claude interprets through natural language understanding — not as executable directives. Claude Code has no concept of numbered chain positions.

**Impact**: Our entire CLAUDE.md chain with "Position: 1 of 5" and state actor updates is cosmetic. It may help the LLM understand structure through natural language, but it's not mechanically enforced.

**Source**: Claude Code official docs (code.claude.com/docs/en/memory)

---

### C3: Skills-to-JSON-LD Pipeline is Counterproductive

**Our assumption**: Converting skills to JSON-LD format would improve precision.

**Reality**: Since JSON-LD performs worse than markdown for LLMs, converting skills to JSON-LD would make them:
- Harder for the LLM to follow (lower accuracy)
- More expensive (3-5x more tokens)
- Harder for humans to read and maintain

**Impact**: The "Approach A: Skills → AALang Pipeline" in `skills_integration.md` should be abandoned. Focus on better markdown descriptions and routing instead.

---

## CONFIRMED (Things We Got Right)

### V1: Agent Teams Context is Not Reusable

**Confirmed**: Teammates are terminated on cleanup. `/resume` and `/rewind` don't restore teammates. Fresh teammates must be spawned each session. Team config/task files persist as metadata but conversation context is lost.

**Source**: Claude Code Agent Teams docs, Anthropic engineering blog

### V2: Users Can Enter Any Running Agent

**Confirmed**: Shift+Up/Down in in-process mode, click panes in split-pane mode. Each teammate is a full, independent Claude Code session.

**Source**: Agent Teams official docs

### V3: Skills Controllability Problem is Real and Well-Documented

**Confirmed**: Multiple sources document that skills don't auto-invoke reliably:
- No algorithmic trigger system — purely semantic LLM reasoning (non-deterministic)
- ~16K char budget for all skill descriptions combined (silently drops skills when exceeded)
- Character budget overrideable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var
- Known workarounds: explicit `/skill-name` invocation, listing skills in CLAUDE.md, better descriptions with "WHEN + WHEN NOT" patterns

**Source**: paddo.dev, mikhail.io, blog.fsck.com, Claude Code official docs

### V4: CLAUDE.md Loads Upward from CWD

**Confirmed**: Claude Code recurses upward from current working directory to (not including) filesystem root. Child directory CLAUDE.md files are loaded on-demand when Claude accesses files in those subtrees.

**Source**: Claude Code official docs

### V5: @import Syntax Exists

**Confirmed**: CLAUDE.md supports `@path/to/file` references. Both relative and absolute paths. Max 5 hops deep. First external import triggers approval dialog. We should be using this.

**Source**: Claude Code official docs, builder.io guide

### V6: Static vs Dynamic Context Distinction Exists

**Confirmed**:
- **Static** (always loaded): Parent CLAUDE.md files, `.claude/rules/*.md` without paths, `~/.claude/CLAUDE.md`, first 200 lines of MEMORY.md, tool definitions, skill metadata listings
- **Dynamic** (on-demand): Child directory CLAUDE.md files, auto memory topic files, skill full content, deferred MCP tools, path-specific rules

**Source**: Claude Code official docs

### V7: Teams Are Ad-Hoc Only

**Confirmed**: No declarative config file for team creation. Teams are created via natural language prompts. No auto-creation from directory structures.

**Source**: Agent Teams official docs

### V8: No Custom CLAUDE.md Per Teammate

**Confirmed**: All teammates load the standard project CLAUDE.md. Customization is through **spawn prompts** — detailed natural language instructions given when spawning each teammate.

**Source**: Agent Teams official docs

---

## NEW DISCOVERIES

### N1: Official Recommendation — Keep CLAUDE.md Under ~500 Lines

Anthropic recommends moving detailed instructions to **skills** for on-demand loading and keeping CLAUDE.md concise. Key quote from docs: "Claude doesn't need verbose documentation upfront — it needs triggers to know WHEN to load detailed context."

### N2: `.claude/rules/*.md` with `paths:` Frontmatter

Rules can be path-specific — only activated when Claude works with matching files. This is a mechanism for targeted context injection we should use.

### N3: Context Survives Compaction

CLAUDE.md files are re-loaded after context compaction (summarization). They are part of "foundational context" that persists through the process. However, conversational context (what was discussed) is summarized.

### N4: Skill Metadata Has a Character Budget (~16K)

All skill descriptions combined must fit within ~16K characters (2% of context window). Skills that exceed this are **silently excluded**. Overrideable with `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

### N5: Gemini CLI Also Has @import and /memory add

Gemini CLI supports `@file.md` import syntax and a `/memory add` command to append context on-the-fly. Similar patterns are converging across tools.

### N6: Codex CLI Has the Most Structured Skill System

OpenAI Codex CLI uses `SKILL.md` with YAML frontmatter, progressive disclosure, hierarchical discovery, and a remote skill marketplace with `$skill-installer`. More structured than Claude Code's skill system.

### N7: Cursor Has Glob-Pattern Rule Targeting

Cursor's `.cursor/rules/*.mdc` files support `globs:` in frontmatter to target rules to specific file patterns. Four application modes: always, intelligent, glob-matched, manual.

### N8: Spawn Prompts Are the Agent Teams Customization Vector

Since custom CLAUDE.md per teammate isn't supported, the spawn prompt is where you inject role-specific context. This can include layer-stage context if we pass it in the prompt.

---

## PROFESSOR'S DOCUMENTATION REVIEW (2026-02-07)

After the initial verification research, we pulled from upstream and reviewed ALL of the professor's documentation in the AALang-Gab repository. This section documents how those findings extend or modify our verified results.

### Documents Reviewed

**Substantive** (detailed content):
- `README.md` — User-facing overview, tested platforms, actor/persona model, MCP/A2A readiness
- `aalang-actor-execution-mechanics.md` — **Definition Adoption model** (critical finding)
- `is-aalang-a-language.md` — Formal argument for AALang as a programming language
- `is-gab-a-compiler.md` — Formal argument for GAB as a compiler
- `agent-creation-best-practices.md` — 20+ best practices, self-check actors, "Explicit Over Implicit" philosophy
- `gab-development-workflow.md` — Complete development lifecycle
- `concurrent-parallel.md` — Concurrency analysis, MCP/A2A distributed execution
- `turing-complete.md` — Probabilistic Turing machine analysis
- `AATest/README_AATest.md` — Testing framework with 3 test types
- `Compressor/huffman-v2-compressor.jsonld` — Real 15-mode-19-actor product example

**Test Results**:
- `gab-test-results.md` — 138 tests, 100% pass rate
- `aatest-test-results.md` — 42 tests, 90.5% pass rate (4 env setup failures)
- `gab-test-gap-analysis.md` — ~65 missing tests identified

### P1: Definition Adoption Model (Extends C2)

The professor explicitly describes the execution model: **"Definition Adoption, Not Instance Creation."** LLMs don't create actor processes — they read the JSON-LD definition and dynamically ADOPT the behavior. All state lives in the conversation context window. No external runtime.

**Impact on C2**: This confirms our finding that AALang annotations in CLAUDE.md are "plain text" — but reframes it positively. The professor's model is that the LLM reading structured text IS the execution model. The annotations aren't "cosmetic" — they're instructions the LLM interprets semantically. They just aren't mechanically enforced by Claude Code's parser.

### P2: "Explicit Over Implicit" Philosophy (Extends V3)

The professor's #1 best practice: replace vague terms ("reasonable", "appropriate") with exact specifications. Self-check actors catch ambiguity before deployment. This directly addresses our Problem 1 (instructions lost across sessions) — AALang's precision IS the solution to natural language ambiguity.

**Impact on V3**: The skills controllability problem (V3) could benefit from AALang-style precision in skill descriptions. Instead of vague "use when appropriate" triggers, use explicit conditions modeled after AALang's mode transition gates.

### P3: Professor Acknowledges Context Window Pressure (Extends C1)

From the README: "Stateful AALang tools created by GAB need significant context windows to not lose the instructions and states."

**Impact on C1**: This validates our finding that JSON-LD is expensive for LLMs. The professor knows the context window is the bottleneck but hasn't explored alternatives (transpiler, selective navigation). These remain our unique research contributions.

### P4: Self-Check and AATest Systems (New Finding)

GAB includes a built-in quality assurance system:
- Self-check actors analyze their own instructions for vagueness, missing instructions, inconsistencies, logic errors
- AATest framework: 3 test types (MessageResponseTest, MessageFlowTest, AgentWorkflowTest)
- GAB itself tested: 138 tests, 100% pass rate

**Impact**: AALang is more mature than initially assumed. It has formalized QA processes that could inform our approach to skill and rule validation.

### P5: MCP/A2A Ready But Not Tested in Practice (New Finding)

AALang is "architecturally concurrent" — multiple actors, message passing, concurrent state management. MCP and A2A support is documented but described as architecture-ready, not yet battle-tested in distributed scenarios.

**Impact on Agent Teams convergence**: AALang's distributed execution model via MCP could theoretically power Agent Teams persistence. But this is future work — the professor hasn't tested it with Claude Code specifically.

### P6: Resolution Mapping — How Professor's Docs Address Our 5 Concerns

| Problem | Professor's Resolution | Status |
|---------|----------------------|--------|
| 1. Instructions lost across sessions | AALang's explicit mode constraints + "Explicit Over Implicit" philosophy + self-check QA | **PARTIAL** — solves definition precision, not session persistence |
| 2. Agent Teams ephemeral | MCP/A2A ready architecture, state actors, file I/O | **NOT DIRECTLY ADDRESSED** — no Claude Code Agent Teams integration |
| 3. Skills not being used | Not addressed. AALang model is: load .jsonld, LLM follows it. No skill discovery concept. | **NOT ADDRESSED** — Claude Code-specific problem |
| 4. Context chain efficiency | Not directly addressed. Professor loads entire .jsonld. Acknowledges context window pressure. | **PARTIALLY VALIDATED** — our selective navigation idea is novel |
| 5. Markdown vs JSON-LD | Professor firmly in JSON-LD camp. Claims structure reduces hallucinations. | **TENSION REMAINS** — research contradicts for LLM accuracy, but professor may be right for complex orchestration |

### P7: Gaps That Are Our Unique Research Contributions

The professor's docs do NOT address:
1. JSON-LD vs markdown accuracy comparison for LLM instruction following
2. Token efficiency analysis of different instruction formats
3. Integration with Claude Code's native context loading (CLAUDE.md chain, @import, rules)
4. Skills ecosystem and skill discovery/invocation
5. Agent Teams integration with persistent context
6. Selective JSON-LD graph navigation (reading 10-25% of file instead of 100%)
7. AALang-to-markdown transpiler (design-time precision → runtime efficiency)
8. Path-specific rules for targeted context injection
9. Cross-platform CLI agent integration (Claude Code, Codex, Gemini CLI)

---

## REVISED APPROACH

Based on all verification results and professor's documentation review, the architecture should be:

```
CLAUDE.md (markdown, <500 lines)
├── Critical rules (always enforced)
├── @import references to detailed docs (max 5 hops)
├── Skill trigger hints ("when X happens, use /skill-name")
└── Navigation pointers to layer-specific context

Skills (.claude/skills/*/SKILL.md) (markdown + YAML frontmatter)
├── Detailed execution instructions (loaded on-demand)
├── Strong "WHEN + WHEN NOT" descriptions
└── Templates and supporting files

.claude/rules/*.md (with paths: frontmatter)
├── Path-specific rules (only load when working in matching paths)
└── Targeted context injection

Agent Teams (for live multi-agent work)
├── Spawn prompts inject layer-stage context
├── Hand-off documents persist results between sessions
└── Status files track progress across sessions

AALang/GAB .jsonld Files (knowledge reference, NOT instruction format)
├── Useful as structured documentation of agent patterns
├── Useful for GAB compiler to create new agents
├── NOT loaded into LLM context as instructions
└── Referenced from CLAUDE.md as "see X for pattern details"
```

Key shift: **AALang/GAB stays as a design/knowledge system, not an instruction format.** The instruction format remains markdown (CLAUDE.md + skills + rules). AALang provides the patterns and vocabulary we use when designing agent behavior, but the actual instructions to the LLM are in markdown.

---

*Verification conducted: 2026-02-07*
*Professor's docs review: 2026-02-07*
*Research agents: 5 parallel (Agent Teams, Skills, Context Chain, JSON-LD, CLI Comparison)*
