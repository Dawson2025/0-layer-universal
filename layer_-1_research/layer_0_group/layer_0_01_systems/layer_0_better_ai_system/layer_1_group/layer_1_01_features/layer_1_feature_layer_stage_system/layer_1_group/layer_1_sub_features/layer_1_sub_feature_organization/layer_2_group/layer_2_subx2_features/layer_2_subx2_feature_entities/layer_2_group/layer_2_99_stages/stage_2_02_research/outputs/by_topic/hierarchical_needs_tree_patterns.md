---
resource_id: "4b44904f-a65d-42e0-a280-ec6552f6223a"
resource_type: "output"
resource_name: "hierarchical_needs_tree_patterns"
---
# Research: Hierarchical Needs Tree Patterns from Critical Rules System

**Date**: 2026-01-28
**Source**: Layer 0 - Critical Rules Enforcement System
**Status**: Active Research
**Relevance**: Architectural patterns for organizing complex hierarchical requirements

---

<!-- section_id: "bba8216d-643f-4b64-a124-fd9df64e1cbc" -->
## Overview

The Layer 0 critical rules enforcement system has implemented a comprehensive hierarchical needs tree structure that successfully organizes complex, multi-layered requirements. This research documents the patterns, strengths, and lessons learned from that system to inform the better_ai_system design.

---

<!-- section_id: "d6833819-3961-4414-bdee-4310e36b9fd5" -->
## Existing Implementation: Critical Rules Enforcement Tree

**Location**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/sub_layer_0_04_99_stages/stage_0_01_request_gathering/outputs/tree_of_needs/`

**Structure**:
```
tree_of_needs/
├── CLAUDE.md                          (Tree manager)
├── README.md                          (Navigation guide)
├── root_need/                         (1 root need)
│   └── ROOT_NEED_enforce_critical_rules.md
├── O1_rule_identification_and_categorization/     (Overarching branch)
│   └── P1_overcome_discretionary_disclaimer/      (Parent tactical need)
│       ├── 1_1_understand_discretionary_wrapper.md
│       ├── 1_2_identify_system_prompt_architecture.md
│       ├── 1_3_evaluate_customization_approaches.md
│       ├── 1_4_select_viable_approach.md
│       └── 1_5_plan_implementation_path.md
├── O2_rule_management/
│   └── P2_extract_critical_rules_dynamically/
│       ├── 2_1_parse_critical_sections.md
│       ├── 2_2_handle_rule_hierarchy.md
│       ├── 2_3_validate_rule_syntax.md
│       ├── 2_4_cache_rules_for_performance.md
│       └── 2_5_support_rule_versioning.md
├── O3_rule_enforcement/
│   ├── P3_inject_rules_into_system_prompt/
│   │   ├── 3_1_format_rules_for_injection.md
│   │   ├── 3_2_use_agent_sdk_initialization.md
│   │   ├── 3_3_verify_rules_in_system_prompt.md
│   │   ├── 3_4_confirm_no_discretionary_wrapper.md
│   │   └── 3_5_test_rule_immutability.md
│   └── P4_create_execution_infrastructure/
│       ├── 4_1_build_rules_injector.md
│       ├── 4_2_create_wrapper_script.md
│       ├── 4_3_support_multiple_modes.md
│       ├── 4_4_add_shell_aliases.md
│       └── 4_5_create_installation_guide.md
└── O4_rule_verification_and_compliance/
    └── P5_ensure_reliability_and_maintenance/
        ├── 5_1_validate_api_call_enforcement.md
        ├── 5_2_test_edge_cases.md
        ├── 5_3_create_troubleshooting_guide.md
        ├── 5_4_plan_version_updates.md
        ├── 5_5_create_upgrade_procedure.md
        └── 5_6_document_limitations.md
```

**Total**: 38 files organized in 4 overarching branches with 5 parent tactical needs and 26 child tactical needs

---

<!-- section_id: "a9e98965-3be9-44fd-ae76-31230e602db3" -->
## Hierarchical Pattern: Four Levels

<!-- section_id: "307adedf-c4b8-4a92-82c6-77f8b105e13f" -->
### Level 1: Root Need
**Single, clear problem statement** that all requirements derive from.
- Problem: "Enforce Critical Rules Without Deprioritization"
- Impact: Why this matters
- Context: Anthropic's discretionary context filtering

<!-- section_id: "d3336dc5-885a-4a3b-9ec7-f89fa930ef08" -->
### Level 2: Overarching Branches (4)
**Strategic questions** that organize the solution space.

| Branch | Strategic Question | Purpose |
|--------|-------------------|---------|
| **O1** | "How do we identify and understand what a critical rule is?" | Foundational understanding |
| **O2** | "How are critical rules stored, organized, extracted, and maintained?" | Rule management |
| **O3** | "How are critical rules guaranteed to execute?" | Technical implementation |
| **O4** | "How do we know critical rules are working?" | Testing & maintenance |

**Characteristic**: Each overarching branch addresses a distinct strategic concern without overlap.

<!-- section_id: "005d84b3-2419-4e4b-999b-e00b51994e1f" -->
### Level 3: Parent Tactical Needs (5)
**Tactical objectives** that organize the work.

| Parent | Tactical Objective | Branch |
|--------|-------------------|--------|
| **P1** | "Understand and overcome Anthropic's discretionary context filtering" | O1 |
| **P2** | "Automatically discover, parse, and manage critical rules" | O2 |
| **P3** | "Get critical rules into the actual Claude Code system prompt" | O3 |
| **P4** | "Build user-friendly scripts and tools that apply rules" | O3 |
| **P5** | "Validate system reliability and plan for maintenance" | O4 |

**Characteristic**: Each parent need is a concrete, achievable objective that spans multiple child needs.

<!-- section_id: "d62db37e-3b2f-4610-96c4-80999426b680" -->
### Level 4: Child Tactical Needs (26)
**Specific, actionable requirements** with clear acceptance criteria.

Example (P1):
- 1.1: Understand Discretionary Wrapper Mechanism
- 1.2: Identify System Prompt vs. Foundational Context
- 1.3: Evaluate Customization Approaches
- 1.4: Select Viable Approach
- 1.5: Plan Implementation Path

**Characteristic**: Each child need is:
- Focused and testable
- Has clear acceptance criteria
- Specifies who owns it (stage)
- Lists dependencies
- Includes cross-references

---

<!-- section_id: "d6a4bca5-1869-42b3-bfdc-4ac85d517b54" -->
## Key Strengths of This Pattern

<!-- section_id: "650867f9-301c-4490-9981-0e5e081eb277" -->
### 1. Clear Separation of Concerns
- **O1**: Understanding the problem
- **O2**: Managing the data
- **O3**: Building the solution
- **O4**: Validating the solution

No overlap between branches. Easy to understand which bucket a requirement belongs to.

<!-- section_id: "d705dc65-88e4-40c1-bd93-ea9ca7548ac1" -->
### 2. Scalable Organization
- Root problem → Overarching branches → Parent needs → Child needs → Acceptance criteria
- 4 levels provides enough granularity without overwhelming complexity
- Easy to add new child needs without restructuring

<!-- section_id: "694bc77e-7093-4e5c-a45b-9916b8e3871b" -->
### 3. Navigability
- CLAUDE.md acts as manager/overview
- README.md provides navigation guide
- Each file includes parent, siblings, children links
- Clear cross-references between related needs

<!-- section_id: "7c00925e-926c-4904-9d9d-a22f037c9cf0" -->
### 4. Clarity of Purpose
- Each level answers a different question
- Strategic questions (O-level) are distinct from tactical objectives (P-level)
- Child needs are specific enough to be actionable

<!-- section_id: "a91e17a6-155d-490a-abda-68e1280abd25" -->
### 5. Acceptance Criteria Built-In
- Each need specifies what "done" looks like
- Checkboxes make progress visible
- Clear boundaries between needs

---

<!-- section_id: "805be487-b978-44d9-8045-2950c091c9a4" -->
## Lessons Learned for better_ai_system

<!-- section_id: "0b208da8-7ac3-4a86-b375-1fe38d5caf33" -->
### Pattern 1: Four-Level Hierarchy Works Well
- Root problem → Branches → Parents → Children is a proven structure
- Provides enough levels for complexity without creating chaos

<!-- section_id: "f928c4a3-c603-4c9e-a24f-c3d2ab2ddb8d" -->
### Pattern 2: Strategic vs. Tactical Separation
- Overarching branches (strategic) answer "what?" and "why?"
- Parent needs (tactical) answer "how do we achieve this?"
- Child needs are specific implementation items
- This separation prevents mixing levels of abstraction

<!-- section_id: "24bc34b1-6e78-4c9a-ace9-4834583a9263" -->
### Pattern 3: Cross-Functional Organization by Concern
- Don't organize by implementation order, organize by conceptual domain
- O1 (Understanding), O2 (Managing), O3 (Building), O4 (Validating) are conceptually clean
- Makes it easier to parallelize work

<!-- section_id: "2d63ef0f-5596-4f7b-a55f-58a5247fa759" -->
### Pattern 4: Navigation is Critical
- Needs tree gets large fast (38 files for one system)
- CLAUDE.md + README.md + internal links are essential
- Without navigation, tree becomes hard to navigate

<!-- section_id: "ff061262-1671-42a5-b124-b991040f5576" -->
### Pattern 5: Clear Ownership & Dependencies
- Each need should specify owner stage
- Each need should list what must be done first
- Enables clear work sequencing

---

<!-- section_id: "094a808e-f2a0-42f1-928b-0ad039485035" -->
## Application to better_ai_system

The better_ai_system could potentially adopt a similar structure:

<!-- section_id: "20a94465-00bc-43a2-9df2-543d10a3eb1e" -->
### Potential Hierarchical Organization

```
better_ai_system/
├── CLAUDE.md                          (Tree manager)
├── README.md                          (Navigation guide)
├── root_need/
│   └── ROOT_NEED_universal_ai_system.md
├── O1_universal_resilience/           (Survival & accessibility)
├── O2_universal_context/              (Knowledge & navigation)
├── O3_universal_tooling/              (Multi-tool support)
└── O4_universal_governance/           (Rules & compliance)
```

**Mapping to current work**:
- **O1_universal_resilience** → need_07_resilient_system_state
- **O2_universal_context** → need_08_universal_context_discovery
- **O3_universal_tooling** → need_09_universal_ai_tool_support
- **O4_universal_governance** → Rules and compliance (future branch)

---

<!-- section_id: "30e38edb-b985-4997-bba6-b9677bb4b49d" -->
## Current Better_AI_System Structure

**Current location**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_-1_better_ai_system/layer_-1_group/layer_-1_99_stages/stage_-1_01_request_gathering/outputs/requests/tree_of_needs/`

**Current structure**:
```
tree_of_needs/
├── README.md
├── 00_seamless_ai_collaboration/      (Root need)
│   ├── 01_capable/                    (Branch: Can AI do the work?)
│   ├── 02_continuous/                 (Branch: Does work keep going?)
│   │   ├── need_01_tool_portable
│   │   ├── need_02_session_resilient
│   │   ├── ...
│   │   ├── need_07_resilient_system_state
│   │   ├── need_08_universal_context_discovery
│   │   └── need_09_universal_ai_tool_support
│   ├── 03_trustworthy/
│   ├── 04_observable/
│   └── 05_engaging/
```

**Observation**: This uses a **different organization pattern**:
- Root need is "seamless AI collaboration"
- Branches are defined by questions about the user experience (01_capable, 02_continuous, etc.)
- Needs are numbered sequentially within branches (need_01, need_02, etc.)
- Does NOT use the Overarching + Parent + Child pattern

---

<!-- section_id: "fd4f4f38-cede-44bd-a35d-4bca1f2eb12a" -->
## Comparison: Two Patterns

<!-- section_id: "79ef1598-5e6f-40c9-914d-a620afa55785" -->
### Critical Rules Pattern (O/P/C structure)
- **Branches**: O1-O4 (strategic domains)
- **Parents**: P1-P5 (tactical objectives)
- **Children**: 1.1-5.6 (specific needs)
- **Advantage**: Very clear conceptual organization
- **Drawback**: Requires 3-4 levels to reach specificity

<!-- section_id: "81b96834-4f73-46df-be17-b6847c49d5b9" -->
### Better_AI_System Pattern (Capability questions)
- **Root need**: Seamless collaboration
- **Branches**: 01-05 (user experience questions)
- **Needs**: Numbered sequentially
- **Advantage**: User-centric framing, clear questions
- **Drawback**: Less clear conceptual organization at finer levels

---

<!-- section_id: "1629676f-ba47-4679-a1c3-e11efe905c1f" -->
## Recommendation: Hybrid Approach

Consider elements from both patterns:

1. **Keep the user-centric framing** (01_capable, 02_continuous, etc.) - this is excellent
2. **Add overarching branches within each** where complexity warrants it
3. **Use consistent numbering** where it applies
4. **Add navigation documents** like the critical rules system
5. **Ensure each level has a clear question** it's answering

Example:
```
02_continuous/
├── README.md (answers: "Does work keep going?")
├── need_07_resilient_system_state/
│   ├── feature_specification.md
│   └── requirements.md
├── need_08_universal_context_discovery/
│   ├── PARENT_NEED_context_discovery.md
│   ├── 1_1_discovery_protocol.md
│   ├── 1_2_system_wide_locations.md
│   └── ...
└── need_09_universal_ai_tool_support/
    ├── PARENT_NEED_multi_tool.md
    ├── 2_1_unified_api.md
    ├── 2_2_tool_adapters.md
    └── ...
```

---

<!-- section_id: "7c6afc64-a237-47cc-b716-2acb395a4cb3" -->
## Benefits of Adopting Patterns

<!-- section_id: "3245e79e-eb2f-4805-93e2-e8dbb2439955" -->
### Organization
- Prevents requirements from becoming scattered
- Makes it easy to find related requirements
- Scales to 100+ needs without confusion

<!-- section_id: "d33cb97f-45d2-43d2-bae9-df41b7f94b9a" -->
### Communication
- Clear language at each level
- Easy to explain to new team members
- Shared vocabulary (strategic vs. tactical)

<!-- section_id: "966eceab-ea61-4d54-b29e-95766cfda3d9" -->
### Implementation
- Clear ownership boundaries
- Dependencies are explicit
- Work can be parallelized

<!-- section_id: "4821d53d-7d6e-4e04-a99d-d885672d117e" -->
### Maintenance
- Easy to add new requirements
- Easy to track progress
- Easy to handle evolving requirements

---

<!-- section_id: "b08a089c-e887-448d-a875-a591a5801a34" -->
## Files to Create/Enhance

Based on this research, the better_ai_system should consider:

1. **Enhanced navigation** documents (like CLAUDE.md for the critical rules tree)
2. **Branch overviews** that explain the strategic purpose of each branch
3. **Parent needs** for complex requirements (like need_08, need_09)
4. **Cross-references** between related needs across branches
5. **README files** at each level to explain the organization

---

<!-- section_id: "a9546071-7370-4974-8fcd-fccad0edf79e" -->
## Key Takeaway

The critical rules enforcement system demonstrates that **hierarchical organization with clear strategic/tactical separation works well for complex requirement sets**. The better_ai_system can benefit from similar patterns while maintaining its user-centric framing.

This is a case of **Layer 0 (working systems) informing Layer -1 (research)** to improve design quality.
