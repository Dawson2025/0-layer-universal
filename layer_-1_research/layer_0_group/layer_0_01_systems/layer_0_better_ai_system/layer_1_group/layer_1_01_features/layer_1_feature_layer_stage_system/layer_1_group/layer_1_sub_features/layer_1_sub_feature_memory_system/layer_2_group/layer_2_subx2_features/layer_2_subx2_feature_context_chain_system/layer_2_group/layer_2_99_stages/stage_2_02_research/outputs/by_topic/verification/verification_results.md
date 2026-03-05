---
resource_id: "0cc202c3-3dd3-4f00-90e9-255784a6ad48"
resource_type: "output"
resource_name: "verification_results"
---
# Verification Results

Research conducted 2026-02-07 across 5 parallel research agents. This file documents what was verified as true, what was false, and what needs correction in our other research files.

---

<!-- section_id: "22a4175b-4644-48cc-9685-176e48796344" -->
## CORRECTIONS NEEDED (Things We Got Wrong)

<!-- section_id: "22d551ad-8633-4f02-bdb9-c81fbaf0ff37" -->
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

<!-- section_id: "5fc9e22b-4877-4d81-8f2e-58bbb2dca089" -->
### C2: AALang Annotations in CLAUDE.md Are Plain Text

**Our assumption**: `@agent ctx:ContextLoadingAgent` and `ctx:ContextLoadingStateActor.loadedFiles` constructs in CLAUDE.md are recognized by Claude Code.

**Reality**: Claude Code treats CLAUDE.md as **plain markdown** with only two extensions:
1. `@path/to/file` import syntax (max 5 hops)
2. YAML frontmatter `paths:` field (for `.claude/rules/` files only)

The AALang state actor annotations, context chain position numbering, and `@agent` directives are read as text that Claude interprets through natural language understanding — not as executable directives. Claude Code has no concept of numbered chain positions.

**Impact**: Our entire CLAUDE.md chain with "Position: 1 of 5" and state actor updates is cosmetic. It may help the LLM understand structure through natural language, but it's not mechanically enforced.

**Source**: Claude Code official docs (code.claude.com/docs/en/memory)

---

<!-- section_id: "4bf161e8-a1a4-4a33-8bd8-711ba1760508" -->
### C3: Skills-to-JSON-LD Pipeline is Counterproductive

**Our assumption**: Converting skills to JSON-LD format would improve precision.

**Reality**: Since JSON-LD performs worse than markdown for LLMs, converting skills to JSON-LD would make them:
- Harder for the LLM to follow (lower accuracy)
- More expensive (3-5x more tokens)
- Harder for humans to read and maintain

**Impact**: The "Approach A: Skills → AALang Pipeline" in `skills_integration.md` should be abandoned. Focus on better markdown descriptions and routing instead.

---

<!-- section_id: "33738e8f-bda0-45cc-8778-7f64a61ed88f" -->
## CONFIRMED (Things We Got Right)

<!-- section_id: "c63ed19d-d1a1-4df9-964a-5d79e7a0d0e4" -->
### V1: Agent Teams Context is Not Reusable

**Confirmed**: Teammates are terminated on cleanup. `/resume` and `/rewind` don't restore teammates. Fresh teammates must be spawned each session. Team config/task files persist as metadata but conversation context is lost.

**Source**: Claude Code Agent Teams docs, Anthropic engineering blog

<!-- section_id: "4330975f-fe97-4b0b-8338-362a744092e9" -->
### V2: Users Can Enter Any Running Agent

**Confirmed**: Shift+Up/Down in in-process mode, click panes in split-pane mode. Each teammate is a full, independent Claude Code session.

**Source**: Agent Teams official docs

<!-- section_id: "c2aafe07-89b6-4a2e-8c65-fed17a612744" -->
### V3: Skills Controllability Problem is Real and Well-Documented

**Confirmed**: Multiple sources document that skills don't auto-invoke reliably:
- No algorithmic trigger system — purely semantic LLM reasoning (non-deterministic)
- ~16K char budget for all skill descriptions combined (silently drops skills when exceeded)
- Character budget overrideable via `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var
- Known workarounds: explicit `/skill-name` invocation, listing skills in CLAUDE.md, better descriptions with "WHEN + WHEN NOT" patterns

**Source**: paddo.dev, mikhail.io, blog.fsck.com, Claude Code official docs

<!-- section_id: "1662f8d3-98be-431f-8055-2c78524e77ba" -->
### V4: CLAUDE.md Loads Upward from CWD

**Confirmed**: Claude Code recurses upward from current working directory to (not including) filesystem root. Child directory CLAUDE.md files are loaded on-demand when Claude accesses files in those subtrees.

**Source**: Claude Code official docs

<!-- section_id: "8a5b6cb9-47ae-4388-919d-7523d1657a42" -->
### V5: @import Syntax Exists

**Confirmed**: CLAUDE.md supports `@path/to/file` references. Both relative and absolute paths. Max 5 hops deep. First external import triggers approval dialog. We should be using this.

**Source**: Claude Code official docs, builder.io guide

<!-- section_id: "92e9f56c-49d4-4c4c-bca0-e645f8ec8fc4" -->
### V6: Static vs Dynamic Context Distinction Exists

**Confirmed**:
- **Static** (always loaded): Parent CLAUDE.md files, `.claude/rules/*.md` without paths, `~/.claude/CLAUDE.md`, first 200 lines of MEMORY.md, tool definitions, skill metadata listings
- **Dynamic** (on-demand): Child directory CLAUDE.md files, auto memory topic files, skill full content, deferred MCP tools, path-specific rules

**Source**: Claude Code official docs

<!-- section_id: "808abfba-31f8-4c89-b542-08664fc3f9e2" -->
### V7: Teams Are Ad-Hoc Only

**Confirmed**: No declarative config file for team creation. Teams are created via natural language prompts. No auto-creation from directory structures.

**Source**: Agent Teams official docs

<!-- section_id: "0341f3ee-76d7-4ee1-9b18-2f5c9a831826" -->
### V8: No Custom CLAUDE.md Per Teammate

**Confirmed**: All teammates load the standard project CLAUDE.md. Customization is through **spawn prompts** — detailed natural language instructions given when spawning each teammate.

**Source**: Agent Teams official docs

---

<!-- section_id: "b588b6d0-7452-47f9-9be3-a5cdc9661a44" -->
## NEW DISCOVERIES

<!-- section_id: "0c8ced6e-8eb3-4e05-ab77-2f9f1d952c61" -->
### N1: Official Recommendation — Keep CLAUDE.md Under ~500 Lines

Anthropic recommends moving detailed instructions to **skills** for on-demand loading and keeping CLAUDE.md concise. Key quote from docs: "Claude doesn't need verbose documentation upfront — it needs triggers to know WHEN to load detailed context."

<!-- section_id: "85d28951-be58-4726-8b9c-8bc9ff655b57" -->
### N2: `.claude/rules/*.md` with `paths:` Frontmatter

Rules can be path-specific — only activated when Claude works with matching files. This is a mechanism for targeted context injection we should use.

<!-- section_id: "92e84ee0-bdcb-4163-bc48-d872ce1c250e" -->
### N3: Context Survives Compaction

CLAUDE.md files are re-loaded after context compaction (summarization). They are part of "foundational context" that persists through the process. However, conversational context (what was discussed) is summarized.

<!-- section_id: "c055a044-3c6d-4961-a965-ff230f8301da" -->
### N4: Skill Metadata Has a Character Budget (~16K)

All skill descriptions combined must fit within ~16K characters (2% of context window). Skills that exceed this are **silently excluded**. Overrideable with `SLASH_COMMAND_TOOL_CHAR_BUDGET`.

<!-- section_id: "e3c0aae0-f5b0-4cce-85c0-a310c3a6e119" -->
### N5: Gemini CLI Also Has @import and /memory add

Gemini CLI supports `@file.md` import syntax and a `/memory add` command to append context on-the-fly. Similar patterns are converging across tools.

<!-- section_id: "120a168d-c750-4d60-8339-14cb50a12ac5" -->
### N6: Codex CLI Has the Most Structured Skill System

OpenAI Codex CLI uses `SKILL.md` with YAML frontmatter, progressive disclosure, hierarchical discovery, and a remote skill marketplace with `$skill-installer`. More structured than Claude Code's skill system.

<!-- section_id: "882258b5-c199-4c0f-ae30-904be5ac867f" -->
### N7: Cursor Has Glob-Pattern Rule Targeting

Cursor's `.cursor/rules/*.mdc` files support `globs:` in frontmatter to target rules to specific file patterns. Four application modes: always, intelligent, glob-matched, manual.

<!-- section_id: "d5ed6404-7fbd-4ac1-90b3-41df243d3d8a" -->
### N8: Spawn Prompts Are the Agent Teams Customization Vector

Since custom CLAUDE.md per teammate isn't supported, the spawn prompt is where you inject role-specific context. This can include layer-stage context if we pass it in the prompt.

---

<!-- section_id: "bb2e1ce8-0b9f-42e5-be05-261c94e64760" -->
## PROFESSOR'S DOCUMENTATION REVIEW (2026-02-07)

After the initial verification research, we pulled from upstream and reviewed ALL of the professor's documentation in the AALang-Gab repository. This section documents how those findings extend or modify our verified results.

<!-- section_id: "21033a46-5bc0-4ddb-87de-cead54fedcf7" -->
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

<!-- section_id: "d3b717eb-a578-475b-86db-8751c1bb7a0a" -->
### P1: Definition Adoption Model (Extends C2)

The professor explicitly describes the execution model: **"Definition Adoption, Not Instance Creation."** LLMs don't create actor processes — they read the JSON-LD definition and dynamically ADOPT the behavior. All state lives in the conversation context window. No external runtime.

**Impact on C2**: This confirms our finding that AALang annotations in CLAUDE.md are "plain text" — but reframes it positively. The professor's model is that the LLM reading structured text IS the execution model. The annotations aren't "cosmetic" — they're instructions the LLM interprets semantically. They just aren't mechanically enforced by Claude Code's parser.

<!-- section_id: "d56d816f-0c87-4297-8241-0a2dcd384606" -->
### P2: "Explicit Over Implicit" Philosophy (Extends V3)

The professor's #1 best practice: replace vague terms ("reasonable", "appropriate") with exact specifications. Self-check actors catch ambiguity before deployment. This directly addresses our Problem 1 (instructions lost across sessions) — AALang's precision IS the solution to natural language ambiguity.

**Impact on V3**: The skills controllability problem (V3) could benefit from AALang-style precision in skill descriptions. Instead of vague "use when appropriate" triggers, use explicit conditions modeled after AALang's mode transition gates.

<!-- section_id: "c90d7d60-b931-424e-8541-5fc9755130c3" -->
### P3: Professor Acknowledges Context Window Pressure (Extends C1)

From the README: "Stateful AALang tools created by GAB need significant context windows to not lose the instructions and states."

**Impact on C1**: This validates our finding that JSON-LD is expensive for LLMs. The professor knows the context window is the bottleneck but hasn't explored alternatives (transpiler, selective navigation). These remain our unique research contributions.

<!-- section_id: "5f7ac090-e293-4232-ab8d-aa8e8ebca194" -->
### P4: Self-Check and AATest Systems (New Finding)

GAB includes a built-in quality assurance system:
- Self-check actors analyze their own instructions for vagueness, missing instructions, inconsistencies, logic errors
- AATest framework: 3 test types (MessageResponseTest, MessageFlowTest, AgentWorkflowTest)
- GAB itself tested: 138 tests, 100% pass rate

**Impact**: AALang is more mature than initially assumed. It has formalized QA processes that could inform our approach to skill and rule validation.

<!-- section_id: "805c0b0e-7f2d-4afb-beb7-d186313d84cc" -->
### P5: MCP/A2A Ready But Not Tested in Practice (New Finding)

AALang is "architecturally concurrent" — multiple actors, message passing, concurrent state management. MCP and A2A support is documented but described as architecture-ready, not yet battle-tested in distributed scenarios.

**Impact on Agent Teams convergence**: AALang's distributed execution model via MCP could theoretically power Agent Teams persistence. But this is future work — the professor hasn't tested it with Claude Code specifically.

<!-- section_id: "f437b1c3-0730-4a1c-a5a0-a0e4993402fc" -->
### P6: Resolution Mapping — How Professor's Docs Address Our 5 Concerns

| Problem | Professor's Resolution | Status |
|---------|----------------------|--------|
| 1. Instructions lost across sessions | AALang's explicit mode constraints + "Explicit Over Implicit" philosophy + self-check QA | **PARTIAL** — solves definition precision, not session persistence |
| 2. Agent Teams ephemeral | MCP/A2A ready architecture, state actors, file I/O | **NOT DIRECTLY ADDRESSED** — no Claude Code Agent Teams integration |
| 3. Skills not being used | Not addressed. AALang model is: load .jsonld, LLM follows it. No skill discovery concept. | **NOT ADDRESSED** — Claude Code-specific problem |
| 4. Context chain efficiency | Not directly addressed. Professor loads entire .jsonld. Acknowledges context window pressure. | **PARTIALLY VALIDATED** — our selective navigation idea is novel |
| 5. Markdown vs JSON-LD | Professor firmly in JSON-LD camp. Claims structure reduces hallucinations. | **TENSION REMAINS** — research contradicts for LLM accuracy, but professor may be right for complex orchestration |

<!-- section_id: "ebeb1beb-bf47-4525-8417-778e9b38ce5a" -->
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

<!-- section_id: "5e29555a-787b-471e-8483-9812af6b8dd8" -->
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
