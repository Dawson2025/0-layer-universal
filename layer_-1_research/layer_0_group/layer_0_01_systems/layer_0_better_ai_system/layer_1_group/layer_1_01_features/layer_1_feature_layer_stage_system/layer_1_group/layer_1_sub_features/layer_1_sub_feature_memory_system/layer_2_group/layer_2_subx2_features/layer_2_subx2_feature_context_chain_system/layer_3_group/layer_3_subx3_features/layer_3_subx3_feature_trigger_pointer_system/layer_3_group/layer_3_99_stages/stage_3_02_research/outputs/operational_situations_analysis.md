---
resource_id: "a4b5c6d7-e8f9-4a0b-1c2d-3e4f5a6b7c8d"
resource_type: "output"
resource_name: "operational_situations_analysis"
---
# Operational Situations Analysis

> **Date**: 2026-03-07
> **Purpose**: Documents the real-world situations, conditions, and circumstances under which each system operation is needed. Goes beyond simple triggers to explain the full context of WHY an operation fires, WHAT the agent or system is doing at that moment, and HOW the interface should be shaped to match the agent's state of mind during that situation.

<!-- section_id: "b5c6d7e8-f9a0-4b1c-2d3e-4f5a6b7c8d9e" -->
## 1. Why Situational Analysis Matters

Understanding WHEN operations are needed — not just WHAT they do — is critical because:

1. **Agent behavior varies by context**: An agent in the middle of writing a new entity (creative, exploratory mode) has different tool preferences than an agent debugging a broken pointer (diagnostic, targeted mode)
2. **Interface design must match the moment**: A lookup interface used during rapid exploration should be ultra-fast (single Grep, <100 tokens). A lookup used during careful validation can afford more detail (Read, ~500 tokens)
3. **Automation decisions depend on workflow position**: Operations at the start of a workflow (index rebuilding) should be fully automated. Operations in the middle (entity search) need agent involvement because the agent has context the system doesn't
4. **Token budget allocation**: Knowing the situation tells us how much of the agent's token budget is already consumed and how much is available for our interface output

<!-- section_id: "c6d7e8f9-a0b1-4c2d-3e4f-5a6b7c8d9e0f" -->
## 2. Situation Categories

Operations cluster into five distinct workflow situations:

| # | Situation | Agent's State | Typical Token Budget Used | Tool Preference |
|---|-----------|--------------|---------------------------|-----------------|
| S1 | Session startup / orientation | Fresh context, exploring, not committed to any task | 5-15% | Read > Glob > Grep |
| S2 | Active development / writing | Deep in a task, creating or editing files | 30-60% | Edit > Write > Grep |
| S3 | Navigation / discovery | Looking for something specific, has a goal but not a path | 10-30% | Grep > Glob > Read |
| S4 | Validation / checking | Verifying correctness, debugging, confirming state | 20-50% | Grep > Read > Bash |
| S5 | Structural change | Moving, renaming, reorganizing directories | 15-40% | Bash > Glob > Write |

<!-- section_id: "d7e8f9a0-b1c2-4d3e-4f5a-6b7c8d9e0f1a" -->
## 3. Detailed Situation Profiles

### S1: Session Startup / Orientation

**What's happening**: The agent just started a session. It's reading CLAUDE.md files, loading context from the parent chain, and trying to understand what it's working on. It may be resuming work from a previous session or starting fresh.

**Agent's mindset**: Exploratory. Reading broadly. Not yet focused on a specific task. Wants to quickly understand the landscape.

**Operations triggered in this situation**:

| Operation | Category | Why It Fires | Best Interface | Rationale |
|-----------|----------|-------------|----------------|-----------|
| Index should be current | A (Auto) | Agent needs accurate lookup data from its first Grep call | Pre-built `.entity-lookup.tsv` + `.uuid-index.json` | Agent shouldn't need to manually rebuild indexes — they should always be current when the agent arrives |
| Entity search by name | B (Agent) | Agent reads a reference like "memory_system" and needs to find where it is | `Grep pattern="memory_system" path=".entity-lookup.tsv"` | Single tool call, returns name + UUID + path + parent. Agent scans 1-6 rows and picks the right one |
| Parent chain traversal | B (Agent) | Agent needs to understand where this entity sits in the hierarchy | `Grep pattern="<parent_UUID>" path=".entity-lookup.tsv"` (repeated) | Agent follows parent_UUID column up the chain. Each step is one Grep call (~80 tokens) |
| Read episodic memory | B (Agent) | Agent needs to know what happened in previous sessions | `Read .0agnostic/04_episodic_memory/index.md` | Standard Read, low cost |

**Interface design implications**:
- Indexes must be pre-built (automated rebuild on git checkout/merge)
- TSV must be available immediately — no setup step
- First-Grep experience should return everything needed in one call
- Token cost must be minimal — the agent is about to load a LOT of context

**What agents DON'T want in this situation**:
- Being asked to run a script to set up indexes
- Multiple tool calls to answer a simple "where is X?" question
- Bash commands to query data
- Large JSON files that consume significant context

---

### S2: Active Development / Writing

**What's happening**: The agent is deep in creating or modifying files. It's writing 0AGNOSTIC.md content, editing pointer files, creating new entities, or updating stage outputs. The agent has significant context loaded and is in "flow."

**Agent's mindset**: Focused, creative, productive. Doesn't want to be interrupted. Wants to finish its current edit, not switch to a different task.

**Operations triggered in this situation**:

| Operation | Category | Why It Fires | Best Interface | Rationale |
|-----------|----------|-------------|----------------|-----------|
| Pointer edit notification | C (Hybrid) | Agent just wrote/edited a pointer file — system detects this and reminds about validation | PostToolUse hook → `additionalContext` injection | Non-blocking. Agent sees "TIP: validate pointers" AFTER completing its edit, not before. Agent can choose to act on it or defer |
| UUID lookup mid-write | B (Agent) | Agent needs a UUID while writing a reference in a document | `Grep pattern="entity_name" path=".entity-lookup.tsv"` | Must be fast. Agent is mid-thought. Single Grep, grab UUID from column 2, continue writing |
| Create pointer file | B (Agent) | Agent needs to create a pointer to another entity | `Write` with frontmatter template | Agent writes directly. Template is simple enough to remember. No script needed |
| Assign UUID to new file | A (Auto) | Agent just created a new file without a resource_id header | `assign-file-uuids.sh` on next sync/hook | Agent shouldn't have to manually generate UUIDs — the system assigns them automatically on the next pass |

**Interface design implications**:
- Notifications must be POST-action, not pre-action (don't block the edit)
- Lookups must be achievable in a single tool call (Grep on TSV)
- Templates should be memorizable, not requiring a Read call every time
- UUID assignment should be fully automated — never interrupt the agent's flow

**What agents DON'T want in this situation**:
- PreToolUse hooks that block their edit
- Being told to "first validate, then edit" (reverses the natural flow)
- Needing to switch from Write/Edit tools to Bash tools mid-task
- Verbose output from automated systems (brief tips only)

---

### S3: Navigation / Discovery

**What's happening**: The agent knows WHAT it's looking for but not WHERE it is. It might be looking for "the design document for context chain architecture" or "all children of the memory_system entity" or "which stage has the tree of needs."

**Agent's mindset**: Goal-directed search. Has a specific question. Wants an answer, not a process.

**Operations triggered in this situation**:

| Operation | Category | Why It Fires | Best Interface | Rationale |
|-----------|----------|-------------|----------------|-----------|
| Find entity by name | B (Agent) | Agent needs to locate an entity's directory | `Grep pattern="entity_name" path=".entity-lookup.tsv"` | Returns path in column 3. One call, done |
| Find all children | B (Agent) | Agent needs to know what's under an entity | `Grep pattern="<entity_UUID>" path=".entity-lookup.tsv"` (match in parent column) | Returns all rows where parent_UUID matches. Each row is a child |
| Resolve UUID to path | B (Agent) | Agent has a UUID from a reference and needs the current filesystem path | `Grep pattern="UUID" path=".entity-lookup.tsv"` | UUID in column 2, path in column 3. Unambiguous, one call |
| Find resources for entity | B (Agent) | Agent needs to know what files/knowledge/rules exist for an entity | `Read <entity>/.0agnostic/resource_index.json` | Per-entity JSON with all resources. Read once, scan mentally |
| Navigate to stage | B (Agent) | Agent needs to find a specific stage directory | `Glob pattern="**/stage_*_04_design"` in entity path | Glob is natural for directory patterns. Returns path directly |

**Interface design implications**:
- TSV is the primary interface — every navigation question maps to a Grep on the TSV
- Results must be self-contained (path included, not just UUID or name)
- Parent/child traversal should never require more than 2-3 Grep calls
- Resource lookups should have a per-entity file (not one global file)

**What agents DON'T want in this situation**:
- Having to construct complex `find` or `jq` commands
- Multi-step processes (search index, get UUID, then resolve UUID, then navigate)
- Results that require another lookup to be useful (e.g., returning UUID but not path)
- Scripts that output to stdout requiring parsing

---

### S4: Validation / Checking

**What's happening**: The agent is verifying that pointers are valid, checking if an index is current, confirming that a structural change didn't break anything, or debugging a stale reference.

**Agent's mindset**: Diagnostic. Careful. Wants clear pass/fail signals. May need to drill into details if something is broken.

**Operations triggered in this situation**:

| Operation | Category | Why It Fires | Best Interface | Rationale |
|-----------|----------|-------------|----------------|-----------|
| Validate all pointers | A (Auto) | Agent wants to confirm all pointers resolve correctly | `pointer-sync.sh --validate` via Bash (exit 0 = pass, exit 1 = fail with details) | This is the ONE place where Bash is the right tool. Binary pass/fail with optional detail output. Agent checks exit code |
| Check specific pointer | B (Agent) | Agent suspects one pointer is broken | `Read` the pointer file → check `canonical_entity:` → `Grep` the TSV for that entity name → compare paths | 2-3 tool calls, but agent is in diagnostic mode and willing to investigate |
| Stale pointer report | C (Hybrid) | After validation fails, agent sees which pointers are broken | `pointer-sync.sh --validate` stderr output | Script lists broken pointers with their targets. Agent decides which to fix |
| Post-sync validation | A (Auto) | After agnostic-sync.sh runs, automatically validate pointers | End-of-script inline call to `pointer-sync.sh --validate` | No agent involvement — purely automated |
| Pre-commit validation | A (Auto) | Before commit, ensure no broken pointers are committed | pre-commit hook calling `pointer-sync.sh --validate` | Blocks commit if broken. Agent sees the failure message and fixes before retrying |

**Interface design implications**:
- Validation must be invocable via Bash (it's a script, not a lookup)
- Exit codes must be clear: 0 = all good, 1 = broken pointers found
- Error output should list exactly what's broken and suggest fixes
- Automated validation (post-sync, pre-commit) should require zero agent involvement

**What agents DON'T want in this situation**:
- Silent failures (validation passes but pointers are actually broken)
- Verbose output when everything is fine (just exit 0, no output needed)
- Having to manually run validation after every edit (hooks should handle this)
- Unclear error messages ("validation failed" without saying WHICH pointer)

---

### S5: Structural Change

**What's happening**: Someone (human or agent) is reorganizing the directory structure — moving entities, renaming directories, restructuring layers. This is the most impactful situation because it can break many pointers at once.

**Agent's mindset**: Cautious, systematic. Knows changes will cascade. Wants confidence that the system will handle the aftermath.

**Operations triggered in this situation**:

| Operation | Category | Why It Fires | Best Interface | Rationale |
|-----------|----------|-------------|----------------|-----------|
| Rebuild UUID index | A (Auto) | Directory structure changed — index paths are now stale | `pointer-sync.sh --rebuild-index` (or git hook auto-trigger) | Must be automated. Agent shouldn't need to remember to rebuild after every move |
| Rebuild entity lookup TSV | A (Auto) | Same trigger as index rebuild — TSV paths are stale | Part of `--rebuild-index` | Generated from the index, so rebuilds automatically |
| Detect moved entities | A (Auto) | Git operation (checkout, merge) changed file locations | post-checkout / post-merge hook compares old vs new paths | Automated detection. Agent may not even know something moved |
| Sync all pointer paths | A (Auto) | After index rebuild, update all pointer files' relative paths | `pointer-sync.sh` (full sync mode) | Deterministic path computation. No judgment needed |
| Move impact notification | C (Hybrid) | After automated rebuild, agent should know what changed | Summary output: "N entities moved, M pointers updated, K broken" | Agent sees the impact without having to investigate. Can drill in if something looks wrong |
| Validate post-move | A (Auto) | After sync, confirm everything resolved correctly | `pointer-sync.sh --validate` | Final check. If pass, move is complete. If fail, agent sees what's still broken |

**Interface design implications**:
- The entire move workflow should be automated end-to-end
- Agent's only role is to see the summary and decide if anything needs manual attention
- Git hooks should chain: detect move → rebuild index → sync pointers → validate → report
- The report should be concise (3-5 lines) unless errors exist

**What agents DON'T want in this situation**:
- Having to manually rebuild indexes after every `mv` or `git checkout`
- Running a sequence of 4 scripts in the right order
- Debugging path computation errors (the script should handle all edge cases)
- Being held responsible for updating pointer paths — that's the system's job

<!-- section_id: "e8f9a0b1-c2d3-4e4f-5a6b-7c8d9e0f1a2b" -->
## 4. Agent Tool Preferences by Situation

Cross-referencing situations with the agent tool preference hierarchy (from `agent_tool_preferences_research.md`):

| Situation | Primary Tool | Secondary Tool | Avoid | Why |
|-----------|-------------|----------------|-------|-----|
| S1: Startup | Read (CLAUDE.md chain) | Grep (TSV lookups) | Bash | Agent is loading context — Read and Grep are natural |
| S2: Development | Edit / Write | Grep (quick lookups) | Bash, Task | Agent is in flow — minimize context switches |
| S3: Navigation | Grep (TSV) | Glob (directory patterns) | Bash, Read (large files) | Agent needs fast, targeted answers |
| S4: Validation | Bash (for scripts) | Read (pointer files) | Write (don't auto-fix) | Bash is acceptable here — validation IS a script |
| S5: Structural Change | Bash (for git/mv) | Read (impact reports) | Manual multi-step processes | Agent expects automation — Bash triggers the chain |

**Key insight**: Bash is avoided in S1-S3 but acceptable in S4-S5 because validation and structural changes are inherently script-driven operations. The interface should match the situation, not impose a single preference everywhere.

<!-- section_id: "f9a0b1c2-d3e4-4f5a-6b7c-8d9e0f1a2b3c" -->
## 5. Conditions Matrix

For each operation, the conditions under which it SHOULD vs SHOULD NOT run:

### Automated Operations (Category A)

| Operation | SHOULD Run When | SHOULD NOT Run When |
|-----------|----------------|---------------------|
| Rebuild index | After git checkout/merge, after `mv` operations, after entity creation, when agent requests it | During active editing (wait for a natural break), when index file is locked |
| Validate pointers | After agnostic-sync.sh, before git commit, after full pointer sync, when agent requests it | During index rebuild (wait for rebuild to complete first), on non-pointer file edits |
| Assign UUIDs | After new file/entity creation, during periodic maintenance, when bulk-creating entities | On files that already have UUIDs, on generated files (CLAUDE.md), on files outside the repo |
| Pre-commit check | On every `git commit` that touches pointer files or entity structure | On commits that only touch non-structural files (documentation typos, etc.) — performance optimization |

### Agent-Assisted Operations (Category B)

| Operation | Agent SHOULD Do This When | Agent SHOULD NOT Do This When |
|-----------|--------------------------|-------------------------------|
| Entity search | When encountering an entity name in documentation, when navigating to a new entity, when resolving a reference | When the path is already known (just use Read), when working on the current entity (path is in context) |
| UUID resolution | When following a UUID reference, when creating cross-entity links, when verifying pointer targets | When already at the target entity, when the UUID was just looked up (cache in context) |
| Hierarchy navigation | When understanding entity relationships, when finding siblings/children, when tracing parent chains | For entities already loaded in context, when the hierarchy is documented in 0AGNOSTIC.md (just Read it) |
| Create pointer file | When a deduplication pattern is needed, when referencing a canonical document from multiple locations | When a simple relative link suffices, when the target is in the same directory |

### Hybrid Operations (Category C)

| Operation | System Triggers When | Agent Should Act When | Agent Can Ignore When |
|-----------|---------------------|----------------------|----------------------|
| Pointer edit notification | Agent edits/writes a file with `pointer_to:` frontmatter | The notification reminds them to validate and they haven't validated recently | They just validated, or the edit was trivial (typo fix in description, not path) |
| Entity search hint | Agent Globs/Greps entity-like patterns without using the TSV | The hint offers a more efficient approach than what they're doing | They already know the path and are just confirming it exists |
| Stale pointer report | `pointer-sync.sh --validate` finds broken pointers | Pointers are broken in files the agent cares about | The broken pointers are in unrelated entities the agent isn't working on |

<!-- section_id: "a0b1c2d3-e4f5-4a6b-7c8d-9e0f1a2b3c4d" -->
## 6. Relationship to Interface Design

This situational analysis directly informs the interface design in `stage_3_04_design/outputs/operations_and_interface_design.md`:

| Situation Finding | Interface Design Implication |
|-------------------|------------------------------|
| S1 agents want zero-setup | Indexes must be pre-built by automated operations (A1, A2) |
| S2 agents hate interruptions | Notifications must be PostToolUse, not PreToolUse (C1, C2) |
| S3 agents want one-call answers | TSV must include all columns needed (name, UUID, path, parent) |
| S4 agents accept Bash for validation | `pointer-sync.sh --validate` is the right interface for validation |
| S5 agents expect full automation | Git hooks must chain rebuild → sync → validate → report |
| Token budgets vary by situation | TSV (~80-530 tokens) for S1-S3; script output for S4-S5 |
| Agent never wants to rebuild manually | Auto-rebuild on git operations (A10) is high priority |
