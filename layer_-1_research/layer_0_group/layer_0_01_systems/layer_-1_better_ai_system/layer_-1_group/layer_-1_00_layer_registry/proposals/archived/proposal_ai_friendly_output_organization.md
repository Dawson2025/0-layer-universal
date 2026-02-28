# Proposal v1: AI-Agent-Friendly Output Organization

**Date**: 2026-02-02
**Version**: 1.0
**Status**: ⚠️ SUPERSEDED by v2
**Superseded By**: `proposal_ai_friendly_output_organization_v2.md`
**Reason**: v2 uses layer-stage hierarchy with features instead of organizing within stage outputs

---

> **Note**: This proposal has been superseded. See v2 for the recommended approach that uses the layer-stage system with features.

---

**Applies To**: Stage outputs, particularly research stages (02)
**Registries to Update**:
- `stage_registry.yaml` - Stage output patterns
- `layer_registry.yaml` - Layer-wide output conventions

---

## Problem Statement

Current `by_topic/` flat file organization has limitations for AI agents:

| Gap | Problem for Agents |
|-----|-------------------|
| No entry point instructions | Agent doesn't know its role in each folder |
| No "what's here" index | Agent must glob/scan to discover content |
| No "where to contribute" guidance | Agent doesn't know where to add new research |
| No status tracking | Agent doesn't know what's done vs needs work |
| No cross-reference map | Agent can't see how topics connect |
| No triggers | Agent doesn't know WHEN to load this content |

---

## Proposed Solution

### 1. Nested Thematic Directories

Organize files into numbered thematic directories with sub-directories where appropriate:

```
by_topic/
├── 01_memory_systems/
│   ├── 01_claude_code_memory/
│   └── 02_anthropic_api/
├── 02_agent_amnesia/
├── 03_external_frameworks/
│   ├── 01_shimi/
│   └── 02_comparison/
└── ...
```

**Rationale**:
- Agents can load focused context without loading everything
- Numbered prefixes provide clear ordering
- Nesting allows progressive detail loading

---

### 2. CLAUDE.md at Each Folder Level

Each folder gets a `CLAUDE.md` that tells the agent:
- **Identity**: What role the agent plays here
- **Scope**: What topics are covered
- **Triggers**: When to load this context
- **Contribution**: Where to add new work

**Template**:

```markdown
# CLAUDE.md - [Topic Name]

## Identity
You are a research agent focused on **[topic]**.

## Scope
- Topic area 1
- Topic area 2

## Triggers: When to Load This Context
- When user asks about [keywords]
- When working on [related tasks]

## On Entry
1. Read `0INDEX.md` to see current state
2. Read `synthesis/` for overview
3. Check sub-folders if diving deeper

## Where to Contribute
| Type of Work | Location |
|--------------|----------|
| [work type 1] | [location] |
| [work type 2] | [location] |

## Parent Context
- [link to parent CLAUDE.md]
```

---

### 3. 0INDEX.md at Each Folder Level

Each folder gets a `0INDEX.md` that provides:
- **Contents table**: What files/folders exist
- **Status tracking**: What's complete, in-progress, or empty
- **Cross-references**: How this topic relates to others
- **Open questions**: What still needs research

**Template**:

```markdown
# Index: [Topic Name]

## Contents

| Item | Type | Status | Description |
|------|------|--------|-------------|
| `file.md` | file | ✅ Complete | Description |
| `folder/` | folder | ⚠️ Partial | Description |

## Status Legend
- ✅ Complete - Ready for instructions stage
- ⚠️ Partial - Has content but needs more work
- 🔄 In Progress - Actively being worked on
- ❌ Empty - Placeholder only

## Cross-References

| This Topic | Relates To | Why |
|------------|------------|-----|
| [topic] | [related folder] | [relationship] |

## Open Questions
- [ ] Question 1
- [ ] Question 2

## Last Updated
[Date] by [session/agent]
```

---

### 4. Synthesis Folder at Each Level

Each folder gets a `synthesis/` subfolder containing a synthesis document:

```
01_memory_systems/
├── synthesis/
│   └── memory_systems_synthesis.md
├── 01_claude_code_memory/
│   ├── synthesis/
│   │   └── claude_code_memory_synthesis.md
│   └── ...
└── ...
```

**Synthesis documents**:
- Summarize all content at that level
- Point UP to parent synthesis
- Point DOWN to child syntheses
- Include triggers for when to read

---

### 5. Root-Level Cross-Reference Map

A `_crossref.md` at the `by_topic/` root showing topic relationships:

```markdown
## Topic Relationships

| Topic | Depends On | Feeds Into |
|-------|------------|------------|
| Agent Amnesia | - | Memory Systems |
| Memory Systems | Agent Amnesia | Agnostic Design |
| ...
```

---

### 6. Contribution Template

A `_template.md` for creating new research files with consistent format:

```markdown
# Research: [Topic]

**Date**: YYYY-MM-DD
**Status**: Draft | In Progress | Complete
**Related**: [links to related files]

---

## Question
## Findings
## Sources
## Implications
## Open Questions
```

---

## Full Proposed Structure

```
by_topic/
├── CLAUDE.md                              # Root agent entry point
├── 0INDEX.md                              # Root discovery/status
├── _crossref.md                           # Topic relationship map
├── _template.md                           # New file template
├── synthesis/
│   └── research_synthesis.md              # Master synthesis
│
├── 01_memory_systems/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   │   └── memory_systems_synthesis.md
│   ├── 01_claude_code_memory/
│   │   ├── CLAUDE.md
│   │   ├── 0INDEX.md
│   │   ├── synthesis/
│   │   │   └── claude_code_memory_synthesis.md
│   │   └── [research files]
│   └── 02_anthropic_api/
│       ├── CLAUDE.md
│       ├── 0INDEX.md
│       ├── synthesis/
│       └── [research files]
│
├── 02_agent_amnesia/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   └── [research files]
│
├── 03_external_frameworks/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   ├── 01_shimi/
│   │   ├── CLAUDE.md
│   │   ├── 0INDEX.md
│   │   ├── synthesis/
│   │   └── [research files]
│   └── 02_comparison/
│       ├── CLAUDE.md
│       ├── 0INDEX.md
│       ├── synthesis/
│       └── [research files]
│
├── 04_multi_agent_systems/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   └── [research files]
│
├── 05_tool_context_systems/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   ├── 01_tool_configs/
│   ├── 02_tool_rankings/
│   └── 03_agnostic_mapping/
│
├── 06_agnostic_system_design/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   └── [research files]
│
├── 07_layer_stage_architecture/
│   ├── CLAUDE.md
│   ├── 0INDEX.md
│   ├── synthesis/
│   ├── 01_core_patterns/
│   └── 02_hierarchy_patterns/
│
└── 08_automation_tooling/
    ├── CLAUDE.md
    ├── 0INDEX.md
    ├── synthesis/
    └── [research files]
```

---

## Proposed File Mapping

### Files to Move

| Original File | New Location |
|---------------|--------------|
| `agnostic_memory_system_research.md` | `01_memory_systems/` |
| `memory_systems.md` | `01_memory_systems/` |
| `memory_system_recommendation.md` | `01_memory_systems/` |
| `claude_code_memory_gap_analysis.md` | `01_memory_systems/01_claude_code_memory/` |
| `why_claude_code_lacks_memory_research.md` | `01_memory_systems/01_claude_code_memory/` |
| `anthropic_memory_tool_api_research.md` | `01_memory_systems/02_anthropic_api/` |
| `agent_amnesia_and_context_systems_conversation.md` | `02_agent_amnesia/` |
| `session_2026-01-30_agent_amnesia_research.md` | `02_agent_amnesia/` |
| `existing_solutions.md` | `03_external_frameworks/` |
| `shimi_framework_research.md` | `03_external_frameworks/01_shimi/` |
| `shimi_sync_mechanisms_explained.md` | `03_external_frameworks/01_shimi/` |
| `system_comparison_and_recommendations.md` | `03_external_frameworks/02_comparison/` |
| `why_not_use_existing_frameworks.md` | `03_external_frameworks/02_comparison/` |
| `can_custom_system_outperform_frameworks.md` | `03_external_frameworks/02_comparison/` |
| `is_your_system_multi_agent.md` | `04_multi_agent_systems/` |
| `multi_agent_parallel_execution_insight.md` | `04_multi_agent_systems/` |
| `updated_understanding_system_scale.md` | `04_multi_agent_systems/` |
| `ai_context_filesystem_locations.md` | `05_tool_context_systems/01_tool_configs/` |
| `agnostic_sync_system_design.md` | `06_agnostic_system_design/` |
| `system_context_hierarchy_research.md` | `07_layer_stage_architecture/01_core_patterns/` |
| `hierarchical_needs_tree_patterns.md` | `07_layer_stage_architecture/02_hierarchy_patterns/` |
| `rule_propagation_problem.md` | `07_layer_stage_architecture/02_hierarchy_patterns/` |
| `automated_traversal_for_your_system.md` | `08_automation_tooling/` |

### Files to Split

`layer_stage_instantiation_understanding.md` (2300+ lines) splits into:

| New File | Content | Location |
|----------|---------|----------|
| `tool_context_systems.md` | Tool configs section (~500 lines) | `05_tool_context_systems/01_tool_configs/` |
| `tool_rankings.md` | Rankings section (~300 lines) | `05_tool_context_systems/02_tool_rankings/` |
| `agnostic_mapping.md` | Mapping section (~130 lines) | `05_tool_context_systems/03_agnostic_mapping/` |
| `layer_stage_instantiation.md` | Core patterns (~1400 lines) | `07_layer_stage_architecture/01_core_patterns/` |

---

## Registry Updates Required

### 1. Stage Registry (`stage_registry.yaml`)

Add to Stage 02 (Research) output patterns:

```yaml
stages:
  02_research:
    outputs:
      by_topic:
        structure: "nested_thematic"
        required_files:
          - "CLAUDE.md"      # Agent entry point
          - "0INDEX.md"      # Discovery/status
        required_folders:
          - "synthesis/"     # Contains synthesis.md
        patterns:
          - "Numbered directories (01_, 02_, ...)"
          - "Sub-directories for sub-topics"
          - "CLAUDE.md + 0INDEX.md at each level"
          - "synthesis/ folder at each level"
```

### 2. Layer Registry (`layer_registry.yaml`)

Add output organization conventions:

```yaml
conventions:
  output_organization:
    ai_agent_friendly:
      entry_point: "CLAUDE.md"
      discovery: "0INDEX.md"
      synthesis: "synthesis/"
      cross_reference: "_crossref.md"
      template: "_template.md"
    status_tracking:
      complete: "✅"
      partial: "⚠️"
      in_progress: "🔄"
      empty: "❌"
```

---

## Benefits Summary

| Benefit | How Achieved |
|---------|--------------|
| **Discoverability** | `0INDEX.md` lists contents and status |
| **Context Loading** | `CLAUDE.md` tells agent what/when to load |
| **Navigation** | Cross-references show topic relationships |
| **Continuity** | Status tracking shows what's done/pending |
| **Contribution** | Guidelines tell agent where to add work |
| **Scalability** | Nested structure handles growing research |

---

## Implementation Steps

1. **Create directory structure** - Make all numbered folders
2. **Move files** - Relocate existing research to new locations
3. **Split large file** - Break up `layer_stage_instantiation_understanding.md`
4. **Create CLAUDE.md files** - At each folder level
5. **Create 0INDEX.md files** - At each folder level
6. **Create synthesis files** - At each folder level
7. **Update registries** - Add patterns to stage/layer registries
8. **Update master synthesis** - Point to new structure

---

## Open Questions

1. Should this pattern apply to ALL stages or just research (02)?
2. Should `0INDEX.md` be auto-generated from folder contents?
3. How to handle the existing `synthesis/` folder already created?
4. Should there be a script to validate the structure?

---

## Related Research

- `system_prompt_architecture.md` - Container-as-Manager pattern
- `agent_amnesia_and_context_systems_conversation.md` - Identity/Triggers/Pointers
- `layer_stage_instantiation_understanding.md` - Stage output patterns

---

## Decision Needed

- [ ] Approve proposal as-is
- [ ] Modify proposal (specify changes)
- [ ] Reject proposal (provide alternative)

Once approved, move to Stage 03 (Instructions) for formal specification.
