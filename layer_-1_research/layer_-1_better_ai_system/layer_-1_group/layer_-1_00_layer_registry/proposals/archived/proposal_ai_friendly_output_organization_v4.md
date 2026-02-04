# Proposal v4: Complete AI System Architecture with Inventory

**Date**: 2026-02-02
**Version**: 4.0
**Status**: ⚠️ SUPERSEDED by v5
**Superseded By**: `proposal_ai_friendly_output_organization_v5.md`
**Reason**: v5 corrects content/config separation, adds full entity structure, fixes proposal location
**Previous Versions**:
- v1: Nested folders within stage outputs (SUPERSEDED)
- v2: Layer-stage hierarchy with features (SUPERSEDED)
- v3: Added agnostic system, three-tier architecture, sync script (SUPERSEDED)
**Supersedes**: v1, v2, and v3

---

> **Note**: This proposal has been superseded. See v5 for corrections:
> - Content (rules, prompts, knowledge) in sub-layers, NOT .0agnostic/
> - Full entity structure with layer_N/ + layer_N+1/ groups
> - 0AGNOSTIC.md should be SHORT (identity + triggers + pointers)
> - Proposals for organization changes go in parent registry

---

---

## What v4 Adds Over v3

| Gap in v3 | v4 Solution |
|-----------|-------------|
| Didn't account for existing feature content | Full inventory of all 2,229 files |
| Vague distribution mapping | Specific file-by-file mapping |
| No cleanup plan | Phase 0: Cleanup (sync conflicts, duplicates) |
| Missing stage content inventory | 31,000 lines mapped by stage |
| No reconciliation plan | How to merge stage research with feature content |

---

## Part 1: Current State Inventory

### 1.1 Project Structure Overview

```
layer_-1_better_ai_system/
├── layer_-1_group/                         # PROJECT INTERNALS (31,000+ lines)
│   ├── layer_-1_99_stages/           # 12 stages with all research
│   │   ├── stage_-1_00_registry/     # 64 lines
│   │   ├── stage_-1_01_request_gathering/  # 7,481 lines
│   │   ├── stage_-1_02_research/     # 12,591 lines ← HEAVIEST
│   │   ├── stage_-1_03_instructions/ # 2,554 lines
│   │   ├── stage_-1_04_design/       # 4,544 lines
│   │   ├── stage_-1_05_planning/     # 289 lines
│   │   ├── stage_-1_06_development/  # 0 lines (empty)
│   │   ├── stage_-1_07_testing/      # 671 lines
│   │   ├── stage_-1_08_criticism/    # 1,248 lines
│   │   ├── stage_-1_09_fixing/       # 186 lines
│   │   ├── stage_-1_10_current_product/  # 1,077 lines
│   │   └── stage_-1_11_archives/     # minimal
│   ├── layer_-1_03_sub_layers/       # Prompts, knowledge, rules
│   └── ...
│
└── layer_0_group/                          # FEATURES (2,229 files)
    └── layer_0_features/
        ├── layer_0_feature_better_layer_stage_system/     # 876 files
        ├── layer_0_feature_better_setup_system/           # 488 files
        ├── layer_0_feature_ai_manager_hierarchy_system/   # 466 files
        ├── layer_0_feature_ai_dynamic_memory_system/      # 375 files
        ├── layer_0_feature_ai_automation_system/          # 6 files (minimal)
        ├── layer_0_feature_ai_context_system/             # 6 files (minimal)
        ├── layer_0_feature_ai_documentation_system/       # 6 files (minimal)
        └── layer_0_feature_ai_rules_system/               # 6 files (minimal)
```

### 1.2 Feature Content Status

| Feature | Files | Content Status | Has Stages? |
|---------|-------|----------------|-------------|
| `better_layer_stage_system` | 876 | **Substantial** - has research, knowledge | Yes |
| `better_setup_system` | 488 | **Substantial** - has sub-project (multi_os) | Yes |
| `ai_manager_hierarchy_system` | 466 | **Substantial** - has research, designs | Yes |
| `ai_dynamic_memory_system` | 375 | **Substantial** - has research | Yes |
| `ai_automation_system` | 6 | **Minimal** - mostly sync conflicts | No |
| `ai_context_system` | 6 | **Minimal** - mostly sync conflicts | No |
| `ai_documentation_system` | 6 | **Minimal** - mostly sync conflicts | No |
| `ai_rules_system` | 6 | **Minimal** - mostly sync conflicts | No |

### 1.3 Sync Conflicts (To Delete)

**Total**: ~50+ files across project

Pattern: `*.sync-conflict-20260126-*-IF2WOGZ.*`

| Location | Count |
|----------|-------|
| Project stages (layer_-1_99_stages) | ~24 |
| Features | ~26+ |

**Action**: Delete all sync conflict files in Phase 0.

### 1.4 Stage Content Detail

#### stage_-1_01_request_gathering (7,481 lines)
```
outputs/
├── DOCUMENTATION_STRATEGY.md
├── FEATURE_INTEGRATION_SUMMARY.md
├── STAGE_01_SUMMARY.md
├── overview/
│   ├── consolidated_requirements.md
│   ├── dependencies.md
│   ├── existing_infrastructure.md
│   ├── implementation_roadmap.md
│   └── system_vision.md
└── requests/tree_of_needs/
    └── 00_seamless_ai_collaboration/
        ├── 01_capable/
        ├── 02_continuous/
        ├── 03_trustworthy/
        ├── 04_observable/
        └── 05_engaging/
```

#### stage_-1_02_research (12,591 lines)
```
outputs/
├── agent_amnesia_external_approaches.md (672 lines)
├── 01_understanding_in_progress/
│   ├── by_topic/
│   │   ├── layer_stage_instantiation_understanding.md (2,300+ lines)
│   │   ├── agent_amnesia_and_context_systems_conversation.md (794 lines)
│   │   ├── proposal_ai_friendly_output_organization_v1.md
│   │   ├── proposal_ai_friendly_output_organization_v2.md
│   │   ├── proposal_ai_friendly_output_organization_v3.md
│   │   ├── memory_system_recommendation.md
│   │   ├── system_comparison_and_recommendations.md
│   │   ├── multi_agent_parallel_execution_insight.md
│   │   ├── ... (21 files total)
│   └── synthesis/
│       └── research_synthesis.md
├── 02_finished_understanding/
│   └── by_topic/
│       └── system_prompt_architecture.md (1,086 lines) ✅ APPROVED
└── episodic/
    ├── index.md
    ├── sessions/
    └── changes/
```

#### stage_-1_03_instructions (2,554 lines)
```
outputs/02_finished_instructions/by_topic/
├── 01_multi_agent_sync_protocol.md
├── 02_automated_traversal_instructions.md
├── 03_agnostic_system_implementation.md
├── 04_episodic_memory_instructions.md
├── 05_system_integration_guide.md
└── system_prompt_architecture_instructions.md
```

#### stage_-1_04_design (4,544 lines)
```
outputs/03_design_decisions/by_topic/
├── 01_multi_agent_sync_design.md
├── 02_automated_traversal_design.md
├── 03_agnostic_system_design.md
├── 04_episodic_memory_architecture.md
├── 05_system_integration_architecture.md
└── 06_shimi_concepts_to_implementation_mapping.md
```

#### stage_-1_05_planning (289 lines)
```
├── README.md (comprehensive planning doc)
└── outputs/
    ├── IMPLEMENTATION_PLAN.md
    └── system_prompt_architecture_plan.md
```

#### stage_-1_07_testing (671 lines)
```
outputs/
├── NAVIGATION_ANALYSIS_findings.md
├── NAVIGATION_ANALYSIS_test_plan.md
├── NAVIGATION_ANALYSIS_testing_results.md
└── TEST_REPORT.md
```

#### stage_-1_08_criticism (1,248 lines)
```
outputs/
├── CRITICISM_REPORT.md
├── NAVIGATION_ANALYSIS_criticism_findings.md
├── NAVIGATION_ANALYSIS_feasibility_review.md
└── NAVIGATION_ANALYSIS_improvement_recommendations.md
```

#### stage_-1_10_current_product (1,077 lines)
```
├── NOTES.md
├── README.md
└── outputs/
    ├── claude_code_enforcement_system.md
    ├── setup_checklist.md
    └── PRODUCT_RELEASE.md
```

---

## Part 2: Distribution Plan

### 2.1 Decision: What Stays vs What Moves

**STAY at Project Level (layer_-1_group/layer_-1_99_stages/)**:
- Cross-cutting research (affects multiple features)
- Project coordination documents
- Proposals (v1-v4)
- External framework comparisons
- Project-level synthesis

**MOVE to Features (layer_0_group/layer_0_features/)**:
- Feature-specific research
- Feature-specific instructions
- Feature-specific designs

### 2.2 File Distribution Mapping

#### To `ai_dynamic_memory_system` (Memory-Related)

| Source File | Source Stage | Action |
|-------------|--------------|--------|
| `memory_system_recommendation.md` | 02_research | MOVE |
| `agnostic_memory_system_research.md` | 02_research | MOVE |
| `claude_code_memory_gap_analysis.md` | 02_research | MOVE |
| `why_claude_code_lacks_memory_research.md` | 02_research | MOVE |
| `04_episodic_memory_instructions.md` | 03_instructions | MOVE |
| `04_episodic_memory_architecture.md` | 04_design | MOVE |

#### To `ai_context_system` (Context/Tool-Related)

| Source File | Source Stage | Action |
|-------------|--------------|--------|
| `system_prompt_architecture.md` | 02_research | MOVE ✅ |
| `agent_amnesia_and_context_systems_conversation.md` | 02_research | MOVE |
| `ai_context_filesystem_locations.md` | 02_research | MOVE |
| `agnostic_sync_system_design.md` | 02_research | MOVE |
| `system_prompt_architecture_instructions.md` | 03_instructions | MOVE |
| `03_agnostic_system_implementation.md` | 03_instructions | MOVE |
| `03_agnostic_system_design.md` | 04_design | MOVE |

#### To `ai_manager_hierarchy_system` (Multi-Agent)

| Source File | Source Stage | Action |
|-------------|--------------|--------|
| `multi_agent_parallel_execution_insight.md` | 02_research | MOVE |
| `shimi_framework_research.md` | 02_research | MOVE |
| `shimi_sync_mechanisms_explained.md` | 02_research | MOVE |
| `01_multi_agent_sync_protocol.md` | 03_instructions | MOVE |
| `01_multi_agent_sync_design.md` | 04_design | MOVE |
| `06_shimi_concepts_to_implementation_mapping.md` | 04_design | MOVE |

#### To `better_layer_stage_system` (Layer-Stage)

| Source File | Source Stage | Action |
|-------------|--------------|--------|
| `layer_stage_instantiation_understanding.md` | 02_research | SPLIT & MOVE |
| `hierarchical_needs_pattern_design.md` | 02_research | MOVE |

#### To `ai_automation_system` (Automation)

| Source File | Source Stage | Action |
|-------------|--------------|--------|
| `automated_traversal_for_your_system.md` | 02_research | MOVE |
| `02_automated_traversal_instructions.md` | 03_instructions | MOVE |
| `02_automated_traversal_design.md` | 04_design | MOVE |

#### STAY at Project Level (Cross-Cutting)

| File | Reason |
|------|--------|
| `agent_amnesia_external_approaches.md` | Compares external frameworks (all features) |
| `system_comparison_and_recommendations.md` | System-wide comparison |
| `existing_solutions.md` | External solutions survey |
| `can_custom_system_outperform_frameworks.md` | System-wide analysis |
| `why_not_use_existing_frameworks.md` | System-wide decision |
| `proposal_*.md` (all versions) | Project-level proposals |
| `research_synthesis.md` | Project-level synthesis |

### 2.3 Tree of Needs Distribution

The `requests/tree_of_needs/` structure maps to features:

| Tree Branch | Maps to Feature |
|-------------|-----------------|
| `01_capable/persistent_knowledge` | `ai_dynamic_memory_system` |
| `01_capable/discoverable` | `ai_context_system` |
| `01_capable/scalable_context` | `ai_manager_hierarchy_system` |
| `02_continuous/tool_portable` | `ai_context_system` |
| `02_continuous/session_resilient` | `ai_dynamic_memory_system` |
| `03_trustworthy/*` | `ai_rules_system` |
| `04_observable/*` | `ai_documentation_system` |
| `05_engaging/*` | Cross-cutting |

---

## Part 3: Architecture (From v3)

### 3.1 Three-Tier Folder Architecture

Every entity uses this pattern:

```
entity/
├── 0AGNOSTIC.md                 # SOURCE OF TRUTH
├── .0agnostic/                  # Tool-agnostic resources
│   ├── agents/
│   ├── episodic/                # Session memory
│   ├── hooks/scripts/
│   ├── skills/
│   └── sync-config.yaml
│
├── .1claude_merge/              # MERGE WORKSPACE (Claude)
├── .1cursor_merge/              # MERGE WORKSPACE (Cursor)
├── .1copilot_merge/             # MERGE WORKSPACE (Copilot)
├── .1gemini_merge/              # MERGE WORKSPACE (Gemini)
├── .1aider_merge/               # MERGE WORKSPACE (Aider)
│
├── CLAUDE.md                    # Generated
├── .claude/                     # Generated
├── .cursorrules                 # Generated
├── .cursor/rules/               # Generated
├── .github/copilot-instructions.md  # Generated
├── GEMINI.md                    # Generated
├── .aider.conf.yml              # Generated
│
└── 0INDEX.md                    # Discovery and status
```

### 3.2 Generation Flow

```
.0agnostic/ + 0AGNOSTIC.md
        │
        ├──→ .1claude_merge/   ──→ CLAUDE.md + .claude/
        ├──→ .1cursor_merge/   ──→ .cursorrules + .cursor/rules/
        ├──→ .1copilot_merge/  ──→ .github/copilot-instructions.md
        ├──→ .1gemini_merge/   ──→ GEMINI.md
        └──→ .1aider_merge/    ──→ .aider.conf.yml
```

### 3.3 Templates

(See v3 for full 0AGNOSTIC.md, 0INDEX.md, and sync-config.yaml templates)

---

## Part 3.5: Visual Architecture Diagrams

### 3.5.1 Current State vs After Reorganization

```
CURRENT STATE                              AFTER v4 REORGANIZATION
─────────────────────────────────────────────────────────────────────────────

layer_-1_better_ai_system/                 layer_-1_better_ai_system/
│                                          │
├── CLAUDE.md                              ├── 0AGNOSTIC.md          ← NEW (source)
│                                          ├── 0INDEX.md             ← NEW (discovery)
│                                          ├── CLAUDE.md             ← Generated
│                                          ├── .0agnostic/           ← NEW
│                                          │   ├── episodic/
│                                          │   ├── hooks/scripts/
│                                          │   └── sync-config.yaml
│                                          ├── .1claude_merge/       ← NEW
│                                          ├── .1cursor_merge/       ← NEW
│                                          ├── synthesis/            ← NEW
│                                          │
├── layer_-1_group/                              ├── layer_-1_group/
│   └── layer_-1_99_stages/                │   └── layer_-1_99_stages/
│       ├── stage_-1_02_research/          │       ├── stage_-1_02_research/
│       │   └── outputs/                   │       │   └── outputs/
│       │       ├── by_topic/              │       │       ├── cross_cutting/  ← Renamed
│       │       │   ├── 21 files ←─────────┼───────┼───────┤   (6 files stay)
│       │       │   └── (ALL research)     │       │       └── proposals/
│       │       └── episodic/ ←────────────┼───────┼─── MOVED to .0agnostic/
│       └── ...                            │       └── ...
│                                          │
└── layer_0_group/                               └── layer_0_group/
    └── layer_0_features/                      └── layer_0_features/
        ├── ai_dynamic_memory_system/              ├── ai_dynamic_memory_system/
        │   └── (375 files, no stages)             │   ├── 0AGNOSTIC.md      ← NEW
        │                                          │   ├── 0INDEX.md         ← NEW
        │                                          │   ├── .0agnostic/       ← NEW
        │                                          │   ├── layer_0_group/
        │                                          │   │   └── layer_0_99_stages/
        │                                          │   │       └── stage_0_02_research/
        │                                          │   │           └── outputs/  ← 6 files moved
        │                                          │   └── synthesis/        ← NEW
        │                                          │
        ├── ai_context_system/                     ├── ai_context_system/
        │   └── (6 files, minimal)                 │   ├── 0AGNOSTIC.md      ← NEW
        │                                          │   ├── stage_0_02_research/  ← 7 files moved
        │                                          │   └── ...
        │                                          │
        └── ... (6 more features)                  └── ... (6 more features, all enhanced)
```

### 3.5.2 Three-Tier Architecture Detail (Per Entity)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ENTITY (any level)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    TIER 0: SOURCE (edit here)                        │   │
│  │                                                                      │   │
│  │   0AGNOSTIC.md          .0agnostic/                                 │   │
│  │   ┌──────────────┐      ┌─────────────────────────────┐             │   │
│  │   │ Identity     │      │ agents/                     │             │   │
│  │   │ Triggers     │      │ episodic/                   │             │   │
│  │   │ Navigation   │      │   ├── index.md              │             │   │
│  │   │ Behaviors    │      │   ├── sessions/             │             │   │
│  │   │ Rules ref    │      │   └── changes/              │             │   │
│  │   └──────────────┘      │ hooks/scripts/              │             │   │
│  │                         │   └── agnostic-sync.sh      │             │   │
│  │                         │ skills/                     │             │   │
│  │                         │ sync-config.yaml            │             │   │
│  │                         └─────────────────────────────┘             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                TIER 1: MERGE WORKSPACES (tool overrides)             │   │
│  │                                                                      │   │
│  │   .1claude_merge/    .1cursor_merge/    .1copilot_merge/    ...     │   │
│  │   ┌────────────┐     ┌────────────┐     ┌────────────┐              │   │
│  │   │ 0_synced/  │     │ 0_synced/  │     │ 0_synced/  │              │   │
│  │   │ 1_overrides│     │ 1_overrides│     │ 1_overrides│              │   │
│  │   │ 2_additions│     │ 2_additions│     │ 2_additions│              │   │
│  │   └────────────┘     └────────────┘     └────────────┘              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│                         agnostic-sync.sh                                    │
│                                      │                                      │
│                                      ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                 TIER 2: GENERATED (tools read these)                 │   │
│  │                                                                      │   │
│  │   CLAUDE.md     .cursorrules    .github/           GEMINI.md        │   │
│  │   .claude/      .cursor/rules/  copilot-*.md       .aider.conf.yml  │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    OTHER ENTITY CONTENTS                             │   │
│  │                                                                      │   │
│  │   0INDEX.md         synthesis/           layer_N/                   │   │
│  │   ┌──────────┐      ┌──────────┐         ┌──────────────────────┐   │   │
│  │   │ Status   │      │ Overview │         │ layer_N_99_stages/   │   │   │
│  │   │ Contents │      │ Findings │         │ layer_N_03_sub_layers│   │   │
│  │   │ X-refs   │      │ Insights │         │ ...                  │   │   │
│  │   └──────────┘      └──────────┘         └──────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.5.3 Full Project Structure After v4

```
layer_-1_better_ai_system/
│
├── 0AGNOSTIC.md                          # Project identity, triggers, navigation
├── 0INDEX.md                             # Project status, contents, cross-refs
├── CLAUDE.md                             # Generated from 0AGNOSTIC.md
├── GEMINI.md                             # Generated
├── .0agnostic/                           # Agnostic resources
│   ├── agents/
│   ├── episodic/                         # Project-level session memory
│   │   ├── index.md
│   │   ├── sessions/
│   │   └── changes/
│   ├── hooks/
│   │   └── scripts/
│   │       └── agnostic-sync.sh
│   ├── skills/
│   └── sync-config.yaml
├── .1claude_merge/                       # Claude-specific overrides
│   ├── 0_synced/
│   ├── 1_overrides/
│   └── 2_additions/
├── .1cursor_merge/                       # Cursor-specific overrides
├── .1copilot_merge/                      # Copilot-specific overrides
├── .claude/                              # Generated
├── .cursor/                              # Generated
├── .github/                              # Generated
├── synthesis/                            # Project-level synthesis
│   └── project_synthesis.md
│
├── layer_-1_group/                             # PROJECT INTERNALS
│   ├── layer_-1_99_stages/
│   │   ├── stage_-1_02_research/
│   │   │   └── outputs/
│   │   │       ├── cross_cutting/        # Multi-feature research STAYS
│   │   │       │   ├── agent_amnesia_external_approaches.md
│   │   │       │   ├── system_comparison_and_recommendations.md
│   │   │       │   └── ...
│   │   │       ├── proposals/            # All proposal versions
│   │   │       │   ├── v1.md
│   │   │       │   ├── v2.md
│   │   │       │   ├── v3.md
│   │   │       │   └── v4.md
│   │   │       └── synthesis/
│   │   │           └── research_synthesis.md
│   │   └── ... (other stages)
│   └── layer_-1_03_sub_layers/
│
└── layer_0_group/                              # FEATURES
    └── layer_0_features/
        │
        ├── layer_0_feature_ai_dynamic_memory_system/
        │   ├── 0AGNOSTIC.md              # Feature identity
        │   ├── 0INDEX.md                 # Feature status
        │   ├── CLAUDE.md                 # Generated
        │   ├── .0agnostic/
        │   │   └── episodic/             # Feature session memory
        │   ├── synthesis/
        │   │   └── feature_synthesis.md
        │   └── layer_0_group/
        │       ├── layer_0_99_stages/
        │       │   └── stage_0_02_research/
        │       │       └── outputs/
        │       │           └── by_topic/  # MOVED: 6 memory files
        │       │               ├── memory_system_recommendation.md
        │       │               ├── agnostic_memory_system_research.md
        │       │               ├── claude_code_memory_gap_analysis.md
        │       │               ├── why_claude_code_lacks_memory_research.md
        │       │               ├── 04_episodic_memory_instructions.md
        │       │               └── 04_episodic_memory_architecture.md
        │       └── layer_0_03_sub_layers/
        │           └── (existing content KEPT)
        │
        ├── layer_0_feature_ai_context_system/
        │   ├── 0AGNOSTIC.md
        │   ├── 0INDEX.md
        │   ├── .0agnostic/
        │   ├── synthesis/
        │   └── layer_0_group/
        │       └── layer_0_99_stages/
        │           └── stage_0_02_research/
        │               └── outputs/by_topic/  # MOVED: 7 context files
        │                   ├── system_prompt_architecture.md ✅
        │                   ├── agent_amnesia_and_context_systems_conversation.md
        │                   └── ...
        │
        ├── layer_0_feature_ai_manager_hierarchy_system/
        │   └── ... (same pattern, 6 multi-agent files)
        │
        ├── layer_0_feature_better_layer_stage_system/
        │   └── ... (same pattern, layer-stage research)
        │
        ├── layer_0_feature_ai_automation_system/
        │   └── ... (same pattern, 3 automation files)
        │
        ├── layer_0_feature_ai_documentation_system/
        │   └── ... (enhanced, minimal moves)
        │
        ├── layer_0_feature_ai_rules_system/
        │   └── ... (enhanced, minimal moves)
        │
        └── layer_0_feature_better_setup_system/
            └── ... (enhanced, existing content kept)
```

### 3.5.4 Generation Flow Diagram

```
                     ┌──────────────────────────────────┐
                     │        0AGNOSTIC.md              │
                     │   (Source of Truth - edit here)  │
                     └───────────────┬──────────────────┘
                                     │
                     ┌───────────────┼───────────────┐
                     │               │               │
                     ▼               ▼               ▼
         ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
         │  .0agnostic/  │  │  .0agnostic/  │  │  .0agnostic/  │
         │   agents/     │  │   episodic/   │  │   rules/      │
         │   skills/     │  │   hooks/      │  │   ...         │
         └───────┬───────┘  └───────┬───────┘  └───────┬───────┘
                 │                  │                  │
                 └──────────────────┼──────────────────┘
                                    │
                                    ▼
                     ┌──────────────────────────────────┐
                     │        agnostic-sync.sh          │
                     │   (Run on SessionStart or manual)│
                     └───────────────┬──────────────────┘
                                     │
       ┌─────────────┬───────────────┼───────────────┬─────────────┐
       │             │               │               │             │
       ▼             ▼               ▼               ▼             ▼
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│.1claude_   │ │.1cursor_   │ │.1copilot_  │ │.1gemini_   │ │.1aider_    │
│  merge/    │ │  merge/    │ │  merge/    │ │  merge/    │ │  merge/    │
│ 1_overrides│ │ 1_overrides│ │ 1_overrides│ │ 1_overrides│ │ 1_overrides│
└─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
      │              │              │              │              │
      ▼              ▼              ▼              ▼              ▼
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│ CLAUDE.md  │ │.cursorrules│ │  .github/  │ │ GEMINI.md  │ │.aider.     │
│  .claude/  │ │  .cursor/  │ │copilot-*.md│ │            │ │ conf.yml   │
│            │ │   rules/   │ │            │ │            │ │            │
│  (Claude   │ │  (Cursor   │ │  (Copilot  │ │  (Gemini   │ │  (Aider    │
│   reads)   │ │   reads)   │ │   reads)   │ │   reads)   │ │   reads)   │
└────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘
```

### 3.5.5 File Flow Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FILE DISTRIBUTION FLOW                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PROJECT STAGES (layer_-1_group/layer_-1_99_stages/)                            │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │  stage_-1_02_research/outputs/                                      │  │
│   │  ┌─────────────────┐                                                │  │
│   │  │ 21 research     │                                                │  │
│   │  │ files           │                                                │  │
│   │  │ (12,591 lines)  │                                                │  │
│   │  └────────┬────────┘                                                │  │
│   │           │                                                         │  │
│   │           ├── 6 files ────→ STAY (cross_cutting/)                   │  │
│   │           │                                                         │  │
│   │           ├── 6 files ────→ ai_dynamic_memory_system                │  │
│   │           ├── 7 files ────→ ai_context_system                       │  │
│   │           ├── 6 files ────→ ai_manager_hierarchy_system             │  │
│   │           ├── 2 files ────→ better_layer_stage_system               │  │
│   │           └── 3 files ────→ ai_automation_system                    │  │
│   │                                                                     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   FEATURES (layer_0_group/layer_0_features/)                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                                                                     │  │
│   │   ┌──────────────────────┐  ┌──────────────────────┐               │  │
│   │   │ ai_dynamic_memory    │  │ ai_context_system    │               │  │
│   │   │ (375 existing +      │  │ (6 existing +        │               │  │
│   │   │  6 moved = 381)      │  │  7 moved = 13)       │               │  │
│   │   └──────────────────────┘  └──────────────────────┘               │  │
│   │                                                                     │  │
│   │   ┌──────────────────────┐  ┌──────────────────────┐               │  │
│   │   │ ai_manager_hierarchy │  │ better_layer_stage   │               │  │
│   │   │ (466 existing +      │  │ (876 existing +      │               │  │
│   │   │  6 moved = 472)      │  │  2 moved = 878)      │               │  │
│   │   └──────────────────────┘  └──────────────────────┘               │  │
│   │                                                                     │  │
│   │   ┌──────────────────────┐  ┌──────────────────────┐               │  │
│   │   │ ai_automation_system │  │ + 3 more features    │               │  │
│   │   │ (6 existing +        │  │ (minimal changes)    │               │  │
│   │   │  3 moved = 9)        │  │                      │               │  │
│   │   └──────────────────────┘  └──────────────────────┘               │  │
│   │                                                                     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Part 4: Implementation Plan

### Phase 0: Cleanup (NEW)

**Goal**: Clean slate before reorganization

1. **Delete sync conflicts**
   ```bash
   find /path/to/layer_-1_better_ai_system -name "*.sync-conflict-*" -delete
   ```

2. **Remove empty directories**
   ```bash
   find /path/to/layer_-1_better_ai_system -type d -empty -delete
   ```

3. **Commit cleanup**
   ```bash
   git add -A && git commit -m "[AI Context] Phase 0: Cleanup sync conflicts and empty dirs"
   ```

**Estimated files deleted**: ~50+ sync conflicts

### Phase 1: Agnostic Infrastructure

**Goal**: Set up agnostic system at project root

1. Create `.0agnostic/` folder structure
2. Create `0AGNOSTIC.md` for project root
3. Create `sync-config.yaml`
4. Create `agnostic-sync.sh` script
5. Create `0INDEX.md` for project root

**Files created**: 5-10

### Phase 2: Merge Workspaces

**Goal**: Set up tool-specific merge folders

1. Create `.1claude_merge/` with 0_synced/, 1_overrides/, 2_additions/
2. Create `.1cursor_merge/` structure
3. Create `.1copilot_merge/` structure
4. Create other merge folders as needed

**Files created**: ~15

### Phase 3: Move Episodic Memory

**Goal**: Relocate episodic from outputs/ to .0agnostic/

1. Move `stage_-1_02_research/outputs/episodic/` → `.0agnostic/episodic/`
2. Move `stage_-1_04_design/outputs/episodic/` → feature episodic
3. Update all references

**Files moved**: ~10

### Phase 4: Feature Enhancement

**Goal**: Add agnostic system to each feature

For each of 8 features:
1. Create `0AGNOSTIC.md`
2. Create `0INDEX.md`
3. Create `.0agnostic/` folder
4. Create `synthesis/` folder

**Files created**: ~40 (5 per feature × 8 features)

### Phase 5: Research Distribution

**Goal**: Move files from project stages to features

1. Move memory research → `ai_dynamic_memory_system`
2. Move context research → `ai_context_system`
3. Move multi-agent research → `ai_manager_hierarchy_system`
4. Move layer-stage research → `better_layer_stage_system`
5. Move automation research → `ai_automation_system`
6. Split large files (layer_stage_instantiation_understanding.md)
7. Create cross-cutting folder for remaining files

**Files moved**: ~25
**Files created** (from splits): ~5

### Phase 6: Sync Testing

**Goal**: Verify agnostic-sync.sh works

1. Run `agnostic-sync.sh all` at project root
2. Verify CLAUDE.md generated correctly
3. Verify .claude/ generated correctly
4. Test with other tools if available

### Phase 7: Registry Updates

**Goal**: Update registries to reflect new architecture

1. Update `entity_registry.yaml` (or create if missing)
2. Update `stage_registry.yaml`
3. Update `layer_registry.yaml`

### Phase 8: Documentation Update (NEW)

**Goal**: Update project CLAUDE.md and related docs

1. Update `/layer_-1_better_ai_system/CLAUDE.md` with new architecture
2. Update feature CLAUDE.md files (will be auto-generated after sync)
3. Update `research_synthesis.md` with v4 status
4. Archive v1-v3 proposals

---

## Part 5: Reconciliation Strategy

### 5.1 Handling Existing Feature Content

For features that already have substantial content (876, 488, 466, 375 files):

**Strategy**: MERGE, don't replace

1. **Keep existing feature structure** - Don't delete what's there
2. **Add to existing stages** - Put moved research in feature's stage_0_02_research
3. **Create synthesis** - New synthesis combines existing + moved content
4. **Update 0INDEX.md** - Reflect merged state

### 5.2 Example: ai_dynamic_memory_system

**Before** (375 files):
```
layer_0_feature_ai_dynamic_memory_system/
├── CLAUDE.md
├── layer_0_group/
│   ├── layer_0_03_sub_layers/
│   │   └── sub_layer_0_02_knowledge_system/
│   │       └── things_learned/  ← Existing content
│   └── layer_0_99_stages/       ← May or may not exist
```

**After** (375 + 6 moved + new files):
```
layer_0_feature_ai_dynamic_memory_system/
├── 0AGNOSTIC.md                 # NEW
├── 0INDEX.md                    # NEW
├── CLAUDE.md                    # Generated
├── .0agnostic/                  # NEW
│   └── episodic/
├── layer_0_group/
│   ├── layer_0_03_sub_layers/
│   │   └── sub_layer_0_02_knowledge_system/
│   │       └── things_learned/  ← KEEP existing
│   └── layer_0_99_stages/
│       └── stage_0_02_research/
│           └── outputs/
│               └── by_topic/    ← MOVED research goes here
│                   ├── memory_system_recommendation.md
│                   ├── agnostic_memory_system_research.md
│                   └── ...
└── synthesis/                   # NEW
    └── feature_synthesis.md
```

---

## Part 6: Open Questions

1. **Split strategy for large files**: How to split `layer_stage_instantiation_understanding.md` (2,300 lines)?
   - By topic (tool context, rankings, architecture)?
   - By stage (research, instructions, design)?

2. **Sync conflict root cause**: Why are there so many? Multi-device Syncthing issue?

3. **Feature stage creation**: Should minimal features (6 files) get full stage structure?

4. **Generated files in git**: Commit CLAUDE.md/.claude/ or gitignore?

---

## Part 7: Metrics

| Metric | Count |
|--------|-------|
| Total files in project | ~2,500+ |
| Sync conflicts to delete | ~50 |
| Files to move to features | ~25 |
| Files to stay at project level | ~15 |
| New files to create (agnostic system) | ~60 |
| Features to enhance | 8 |
| Phases in implementation | 8 |

---

## Part 8: Success Criteria

- [ ] All sync conflicts deleted
- [ ] Every entity has 0AGNOSTIC.md
- [ ] Every entity has 0INDEX.md
- [ ] Every entity has .0agnostic/ folder
- [ ] agnostic-sync.sh generates correct output
- [ ] Research distributed to appropriate features
- [ ] Cross-cutting research in project-level folder
- [ ] Registries updated
- [ ] Project CLAUDE.md reflects new architecture

---

## Decision Needed

**Approve v4 to begin implementation?**

If approved, we start with:
1. Phase 0: Delete ~50 sync conflicts
2. Phase 1: Create agnostic infrastructure at project root

---

*Created: 2026-02-02*
*Based on: Complete inventory of 2,500+ files across project*
