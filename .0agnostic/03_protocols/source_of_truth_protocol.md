---
resource_id: "e6996966-ff4b-4f9e-b771-f7f94435d4a1"
resource_type: "protocol"
resource_name: "source_of_truth_protocol"
---
# Source of Truth Protocol

**Scope**: Universal — applies to all agents when asked to trace or show the source of truth for any concept, artifact, or system component

## Purpose

When asked "where is the source of truth for X?" or "show me the context chain for X", agents follow a structured 3-tier response that traces from the canonical detail location, through the 0AGNOSTIC pointer layer, to the full propagation chain showing how that knowledge reaches each AI tool.

## When to Use

- User asks: "where is the source of truth for X?"
- User asks: "show the context chain for X"
- User asks: "how does X get into context?"
- User says: `/source-of-truth X` or similar command
- Agent needs to verify where authoritative content lives before making changes

## Response Format

### Tier 1: Canonical Source (the detailed location)

The **specific file or directory** where the full, authoritative content lives. This is the place you edit to change the truth.

```markdown
### Source of Truth

**Canonical location**: `{full/path/to/file_or_directory}`
**Type**: {file | directory | stage output | rule | protocol | template}
**Last updated**: {date if known}
**Description**: {1-2 sentences: what this contains and why it's authoritative}
```

### Tier 2: 0AGNOSTIC Reference (the pointer)

The **0AGNOSTIC.md** that references, summarizes, or points to the canonical source. This is where agents first learn about the source.

```markdown
### 0AGNOSTIC Reference

**Referencing 0AGNOSTIC.md**: `{path/to/0AGNOSTIC.md}`
**Section**: {which section contains the reference — e.g., "Navigation > Key Locations", "Key Behaviors > Domain Concepts"}
**What it says**: {brief quote or paraphrase of how the 0AGNOSTIC.md references this source}
**Relationship**: {summary | pointer | excerpt | full inclusion}
```

If the source IS the 0AGNOSTIC.md itself (i.e., the 0AGNOSTIC.md is the canonical location), say so:

```markdown
### 0AGNOSTIC Reference

**The 0AGNOSTIC.md IS the source of truth**: `{path/to/0AGNOSTIC.md}`
**Section**: {which section is authoritative}
```

### Tier 3: Propagation Chain (how it reaches agents)

Show how the knowledge propagates from the 0AGNOSTIC.md reference (Tier 2) outward through the avenue web into static and dynamic context for each AI tool.

**Structure the chain in this order:**

1. **0AGNOSTIC.md → agnostic-sync.sh → tool files** (the primary propagation path)
2. **Additional static avenues** that carry this knowledge
3. **Dynamic avenues** that can load this knowledge on-demand

```markdown
### Propagation Chain

**Primary path** (0AGNOSTIC.md → agnostic-sync.sh):
| Generated File | Timing | Tool |
|----------------|--------|------|
| CLAUDE.md | Static | Claude Code |
| AGENTS.md | Static | AutoGen |
| GEMINI.md | Static | Gemini |
| OPENAI.md | Static | OpenAI |

**Additional static avenues**:
| Avenue | Mechanism | Tool |
|--------|-----------|------|
| Path rules | {.claude/rules/*.md} | Claude Code |
| Skills listing | {.claude/skills/*/SKILL.md — WHEN section} | Claude Code |
| Auto memory | {~/.claude/projects/*/memory/MEMORY.md} | Claude Code |

**Dynamic avenues** (loaded on-demand):
| Avenue | Mechanism | Tool |
|--------|-----------|------|
| .0agnostic/ resources | {01_knowledge/, 02_rules/, 03_protocols/} | Any |
| Parent chain | {0AGNOSTIC.md Parent: refs, traversed upward} | Any |
| JSON-LD agent | {.gab.jsonld mode constraints} | AALang |
| Integration summary | {.integration.md} | Any |
| Skill content | {Full SKILL.md on invocation} | Claude Code |
| Episodic memory | {.0agnostic/07_episodic_memory/} | Any |
```

Only include rows that actually apply to this specific piece of knowledge. Most items will use the primary path plus 2-3 additional avenues.

## Example

**Query**: "Where is the source of truth for the stage report format?"

### Source of Truth

**Canonical location**: `.0agnostic/03_protocols/stage_report_protocol.md`
**Type**: protocol
**Description**: Defines the exact markdown format for stage reports, including required sections (Status, Summary, Key Outputs, Findings, Open Items, Handoff) and the 6 rules governing their creation.

### 0AGNOSTIC Reference

**Referencing 0AGNOSTIC.md**: `layer_0/0AGNOSTIC.md` (root entity) — does not currently reference this protocol directly.
**Nearest reference**: Each entity's 0AGNOSTIC.md that uses stage delegation mentions stage reports in "Key Behaviors > Stage Delegation" (e.g., context_chain_system/0AGNOSTIC.md line ~85).
**Relationship**: pointer (0AGNOSTIC mentions "writes a stage_report.md" and links to the protocol)

### Propagation Chain

| Avenue | Mechanism | Timing | Tool |
|--------|-----------|--------|------|
| CLAUDE.md cascade | context_chain_system/CLAUDE.md includes "stage reports" in Key Behaviors | Static | Claude Code |
| .0agnostic/ protocol | `.0agnostic/03_protocols/stage_report_protocol.md` — read on-demand | Dynamic | Any |
| .0agnostic/ rule | `.0agnostic/02_rules/static/STAGE_REPORT_RULE.md` — mandates writing reports | Dynamic | Any |
| Parent chain | Entity 0AGNOSTIC.md → parent 0AGNOSTIC.md (inherited behavior) | Dynamic | Any |

## Rules

1. Always start with Tier 1 (the canonical file) — agents need to know where to look and where to edit
2. If you don't know the canonical location, say so and describe how you would find it (search .0agnostic/, check 0INDEX.md, read stage reports)
3. Tier 3 only needs avenues that actually carry this knowledge — don't list all 13 avenues every time
4. When the user asks to "change" the source of truth, the edit goes to Tier 1, then agnostic-sync.sh propagates to Tier 3
5. If the source of truth is duplicated (appears authoritatively in multiple places), flag this as a problem — there should be one source

## Related

- **Mandatory Rule**: `../02_rules/dynamic/I0_source_of_truth_rule.md` — importance-0 rule mandating this protocol
- **Context Loading Protocol**: `context_loading_protocol.md` — how agents load context on session start
- **Avenue Web Architecture**: `layer_-1_research/.../context_chain_system/.0agnostic/01_knowledge/avenue_web_architecture.md` — the 8-avenue model
- **Static/Dynamic Context**: `layer_-1_research/.../context_chain_system/.0agnostic/01_knowledge/static_dynamic_context.md` — the 2x2 matrix
- **Agnostic Sync**: `.0agnostic/agnostic-sync.sh` — the propagation mechanism
