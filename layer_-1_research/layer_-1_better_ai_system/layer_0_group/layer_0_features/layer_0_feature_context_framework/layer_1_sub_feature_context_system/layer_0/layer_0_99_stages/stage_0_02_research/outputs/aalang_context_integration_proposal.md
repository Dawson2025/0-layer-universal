# AALang Context Integration Proposal

**Date**: 2026-02-05
**Author**: AI Agent (Claude)
**Status**: Draft Proposal
**Related Research**: gab.jsonld analysis, better_ai_system context_framework

---

## Executive Summary

This document proposes integrating AALang patterns from `gab.jsonld` into the layer-stage system's AI context chaining, loading sequence, and context flow. The goal is to address the identified context system problems while leveraging AALang's proven patterns for state management, mode transitions, and systematic verification.

---

## 1. Analysis: AALang Patterns Applicable to Context Chaining

### 1.1 Mode-Based Workflow Pattern

**In AALang (gab.jsonld)**:
```
Clarification → Discussion → Formalization → Generation
```

**Application to Layer-Stage System**:
```
Context Loading → Context Validation → Context Propagation → Context Delivery
```

Each "mode" would have:
- **State Actors**: Track loading progress, validation status, propagation completeness
- **Transition Validations**: Confidence thresholds before proceeding
- **Isolated State**: Each phase maintains its own context

### 1.2 State Actor Pattern

**AALang State Actors**:
- `UnderstandingIndicatorsStateActor` - tracks understanding confidence
- `SatisfactionIndicatorsStateActor` - tracks workflow satisfaction
- `DebugModeStateActor` - toggleable debug output
- `DecisionLogStateActor` - tracks decisions

**Proposed Context State Actors**:

| Actor | Purpose | Tracks |
|-------|---------|--------|
| `ContextLoadingStateActor` | Track what context has been loaded | CLAUDE.md chain, rules, protocols |
| `ContextConfidenceStateActor` | Track agent's context confidence | Understanding of current layer/stage |
| `NavigationStateActor` | Track current position | Layer, stage, sub_layer, depth |
| `DebugContextStateActor` | Context loading debug mode | Show/hide loading details |

### 1.3 Confidence-Based Transitions

**AALang Pattern**:
- Don't proceed to next mode until `overallConfidence >= 0.8`
- Validate prerequisites before transition

**Context Application**:
- Don't proceed with work until context confidence >= 0.8
- Validate that required context files have been read
- Track which CLAUDE.md files in the chain have been loaded

### 1.4 Isolated State Management

**AALang Pattern**:
- Each mode has private state (ClarificationModeState, DiscussionModeState, etc.)
- Shared communication only via message interface

**Context Application**:
- Each layer/stage has isolated context scope
- Shared context only via defined interfaces (CLAUDE.md chain, hand_off_documents)
- Clear boundaries between universal (layer_0) and project-specific (layer_1) context

### 1.5 Quality Checklist Pattern

**AALang Pattern**:
- Systematic verification before finalizing
- Categories: randomness/variability, startup behavior, system command prevention, edge case handling, state management

**Context Quality Checklist**:
1. ✅ Root CLAUDE.md chain loaded (global → project)
2. ✅ Current layer identified
3. ✅ Current stage identified (if applicable)
4. ✅ Relevant sub_layers checked (rules, protocols, knowledge)
5. ✅ status.json read (if exists)
6. ✅ Context conflicts resolved
7. ✅ Universal rules applied

---

## 2. Proposed Context Loading Sequence

### 2.1 Current Loading Sequence (Problems)

```
Session Start
    ↓
Claude Code auto-loads CLAUDE.md chain (tool-specific)
    ↓
??? (No defined sequence after initial load)
```

**Problems Identified**:
- No confidence tracking
- No validation of completeness
- No state management for what was loaded
- No systematic traversal

### 2.2 Proposed AALang-Enhanced Loading Sequence

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 1: CONTEXT LOADING MODE                                          │
│                                                                         │
│  1.1 Load Root Chain (confidence += 0.2 per file)                      │
│      ~/.claude/CLAUDE.md → ~/CLAUDE.md → project/CLAUDE.md             │
│                                                                         │
│  1.2 Update ContextLoadingStateActor                                   │
│      - Record which files loaded                                        │
│      - Track layer-stage system awareness                               │
│                                                                         │
│  1.3 Calculate initial confidence                                       │
│      - If layer-stage system mentioned: confidence += 0.3               │
│      - If AALang mentioned: confidence += 0.2                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
          [Confidence check: >= 0.6 to proceed, else load more context]
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: CONTEXT VALIDATION MODE                                       │
│                                                                         │
│  2.1 Identify current position                                          │
│      - Determine layer (0, 1, -1, etc.)                                 │
│      - Determine stage (01-11, if applicable)                           │
│      - Determine sub_layer (if nested)                                  │
│                                                                         │
│  2.2 Validate required context                                          │
│      - sub_layer_0_04_rules loaded? (CRITICAL)                          │
│      - sub_layer_0_05_protocols loaded? (at session start)              │
│      - Relevant knowledge loaded?                                       │
│                                                                         │
│  2.3 Update ContextConfidenceStateActor                                │
│      - Score each aspect (0.0-1.0)                                      │
│      - Calculate weighted average                                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
          [Confidence check: >= 0.8 to proceed, else identify gaps]
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 3: CONTEXT PROPAGATION MODE                                      │
│                                                                         │
│  3.1 Resolve context priority                                           │
│      - Layer 0 rules override project-specific                          │
│      - Later in chain overrides earlier (for same scope)                │
│      - Universal sub_layers apply everywhere                            │
│                                                                         │
│  3.2 Apply context transformations                                      │
│      - Substitute path variables                                        │
│      - Resolve relative references                                      │
│      - Merge configurations                                             │
│                                                                         │
│  3.3 Detect conflicts                                                   │
│      - Flag contradictory rules                                         │
│      - Escalate to user if unresolvable                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 4: CONTEXT DELIVERY MODE                                         │
│                                                                         │
│  4.1 Present context summary (if debug mode ON)                        │
│      - Files loaded                                                     │
│      - Current position                                                 │
│      - Confidence scores                                                │
│                                                                         │
│  4.2 Ready for task execution                                          │
│      - All prerequisites satisfied                                      │
│      - Context confidence >= 0.8                                        │
│      - Agent knows where it is and what rules apply                     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Addressing Identified Context Problems

### 3.1 Problem: Context Gathering Rules Scattered

**AALang Solution**: Single authoritative source with explicit references

**Implementation**:
- **Authoritative source**: `sub_layer_0_04_rules/context_gathering_rules.md`
- **References**: All other locations point to this source
- **Pattern**: Like AALang's `See gab-runtime.jsonld` pattern

### 3.2 Problem: Multiple CLAUDE.md Entry Points Unclear

**AALang Solution**: Defined loading chain with explicit ordering

**Implementation**:
- Document official loading order: `~/.claude/CLAUDE.md` → `~/CLAUDE.md` → `project/CLAUDE.md`
- Add `nav:parent` links (JSON-LD pattern from navigation_system)
- Track loading state in `ContextLoadingStateActor`

### 3.3 Problem: No Context Priority System

**AALang Solution**: Severity levels (absolute, critical, standard)

**Implementation**:
```yaml
context_priority:
  absolute:
    - Universal rules (layer_0/rules)
    - Safety governance
  critical:
    - Project-specific rules
    - Stage-specific protocols
  standard:
    - Knowledge references
    - Optional guidance
```

### 3.4 Problem: No Context Caching

**AALang Solution**: Session-consistent actors with state persistence

**Implementation**:
- `sessionConsistent: true` pattern
- State actors maintain loaded context across the session
- Avoid reloading same files within session

### 3.5 Problem: No Scope Boundaries

**AALang Solution**: Isolated state per mode with explicit readability rules

**Implementation**:
```yaml
scope_boundaries:
  layer_0:
    scope: "applies to ALL"
    readableBy: ["layer_0", "layer_1", "layer_-1", "all_subxn"]
  layer_1:
    scope: "project-specific"
    readableBy: ["layer_1", "layer_1_children"]
    unreadableBy: ["other_layer_1_projects"]
```

### 3.6 Problem: Layer Navigation Incomplete

**AALang Solution**: Explicit communication rules (canMessage, canReceiveFrom)

**Implementation**:
- Define navigation rules per layer/stage
- Horizontal (sibling) rules: Use JSON-LD `nav:siblings`
- Vertical rules: Use `nav:parent`, `nav:children`

---

## 4. Proposed File Structure Changes

### 4.1 New Context State Files

```
layer_0/layer_0_03_sub_layers/sub_layer_0_05_protocols/
├── context_loading_protocol.md       # Defines the 4-phase loading sequence
├── context_state_actors.jsonld       # State actor definitions (AALang-style)
└── context_quality_checklist.md      # Quality verification checklist
```

### 4.2 New Rules Files

```
layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/
├── context_priority_rules.md         # Priority system documentation
├── context_scope_boundaries.md       # Scope definitions
└── context_traversal_rule.md         # How to traverse the chain
```

### 4.3 Updated CLAUDE.md Pattern

Each CLAUDE.md should include:
```markdown
## Context Chain Position
- **Position in chain**: [N of M]
- **Parent**: [path to parent CLAUDE.md]
- **Children**: [paths to child CLAUDE.md files]
- **Load priority**: [absolute|critical|standard]

## Context Confidence Scoring
- Layer identification: [0.0-1.0]
- Stage identification: [0.0-1.0]
- Rules awareness: [0.0-1.0]
- Required context loaded: [0.0-1.0]
```

---

## 5. Integration with AALang AI System

Since AALang is the PRIMARY AI SYSTEM used throughout the layer-stage framework, the context loading sequence should:

1. **Recognize AALang context**: When entering `sub_layer_0_01_ai_system/`, load AALang-specific context
2. **Use AALang patterns**: Apply mode-based workflow for context operations
3. **Reference gab.jsonld**: Use as specification for state management patterns
4. **Follow AALang conventions**: JSON-LD, @id references, persona patterns

---

## 6. Implementation Roadmap

### Phase 1: Documentation (Week 1)
- [ ] Create context_loading_protocol.md
- [ ] Create context_priority_rules.md
- [ ] Update universal rules to reference new protocol

### Phase 2: State Actors (Week 2)
- [ ] Design state actor schema (JSON-LD)
- [ ] Define state transitions
- [ ] Create quality checklist

### Phase 3: Integration (Week 3)
- [ ] Update CLAUDE.md files with context chain position
- [ ] Add nav:parent links to existing index.jsonld files
- [ ] Test loading sequence with sample sessions

### Phase 4: Validation (Week 4)
- [ ] Create confidence scoring tool
- [ ] Test context propagation
- [ ] Document lessons learned

---

## 7. Open Questions

1. **Should confidence scores be explicit or implicit?**
   - Explicit: Agent reports scores to user
   - Implicit: Agent tracks internally, only shows on debug mode

2. **How to handle submodule context (AALang)?**
   - Submodule has its own CLAUDE.md (on dawson branch)
   - Should parent context override submodule context?

3. **Context caching persistence?**
   - Session-only (current approach)
   - Cross-session (requires persistent storage)

---

## 8. References

- **AALang/Gab Specification**: `/layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/gab.jsonld`
- **Context Problems Analysis**: `/layer_-1_research/.../things_learned/01_context_problems.md`
- **Navigation System**: `/layer_-1_research/.../layer_1_sub_feature_navigation_system/index.jsonld`
- **Implementation Roadmap**: `/layer_-1_research/.../outputs/overview/implementation_roadmap.md`
- **Tree of Needs (06_context_flow)**: `/layer_-1_research/.../tree_of_needs/00_seamless_ai_collaboration/06_context_flow/`

---

## 9. Next Steps

1. Review this proposal with user
2. Prioritize which patterns to implement first
3. Create detailed implementation specs for approved patterns
4. Begin Phase 1 documentation
