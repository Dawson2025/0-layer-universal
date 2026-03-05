---
resource_id: "eeffd6a2-011f-4582-8a6c-449d3192ac49"
resource_type: "output"
resource_name: "aalang_context_integration_proposal"
---
# AALang Context Integration Proposal v2

**Date**: 2026-02-05
**Author**: AI Agent (Claude)
**Status**: Draft Proposal v2
**Related Research**: gab.jsonld analysis, better_ai_system context_framework

---

<!-- section_id: "f14c8870-dd35-446f-8836-f3784b7f2518" -->
## Executive Summary

This document proposes a deep integration of AALang/GAB patterns into the layer-stage system's context chaining. This goes beyond documentation to create **actual AALang agents** that implement context loading, validation, and propagation - making the context system itself powered by AALang.

**Key Changes from v1**:
- AALang agent definitions (JSON-LD) for context operations
- GAB-style state actors for tracking context state
- CLAUDE.md files that reference and invoke AALang agents
- Bidirectional integration: agents inform CLAUDE.md, CLAUDE.md invokes agents

---

<!-- section_id: "ea51f1aa-6a23-4b98-b9fc-a23024d8d25d" -->
## Part 1: Analysis (from v1)

<!-- section_id: "f4c8f727-92dd-4596-9dfc-1090a3d6a585" -->
### 1.1 AALang Patterns Applicable to Context Chaining

| Pattern | In AALang (gab.jsonld) | Application to Context System |
|---------|------------------------|------------------------------|
| Mode-Based Workflow | Clarification → Discussion → Formalization → Generation | Loading → Validation → Propagation → Delivery |
| State Actors | UnderstandingIndicators, SatisfactionIndicators, DebugMode | ContextLoading, ContextConfidence, Navigation, DebugContext |
| Confidence Thresholds | >= 0.8 before mode transition | >= 0.8 before task execution |
| Isolated State | Each mode has private state | Each layer/stage has isolated context scope |
| Quality Checklists | Systematic verification before completion | Context quality checklist before work |
| Prohibitions/Requirements | Severity levels (absolute, critical, standard) | Context priority system |

<!-- section_id: "148d2988-b31e-4f44-8587-9361f6de1b4a" -->
### 1.2 Problems to Solve

1. **Context gathering rules scattered** - no single authoritative source
2. **Multiple CLAUDE.md entry points** - unclear reading order
3. **No context priority system** - which context overrides which?
4. **No context caching** - agents reload same context repeatedly
5. **No scope boundaries** - what context applies where?
6. **Layer navigation incomplete** - unclear horizontal/vertical rules
7. **No agent-driven context loading** - passive files, no active agents

---

<!-- section_id: "16a17090-def7-4c88-bd28-f83f7aa027a1" -->
## Part 2: AALang Agent Definitions

<!-- section_id: "c391c277-b571-4aa3-b637-c03638abcbe0" -->
### 2.1 Context Loading Agent (JSON-LD)

**File**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/context_agents/context_loading_agent.jsonld`

```jsonld
{
  "@context": {
    "@vocab": "https://aalang.org/",
    "gab": "https://aalang.org/gab/",
    "ctx": "https://layer-stage.dev/context/"
  },
  "@id": "ctx:ContextLoadingAgent",
  "@type": "gab:Agent",

  "name": "Context Loading Agent",
  "description": "Manages the 4-phase context loading sequence for layer-stage system sessions",

  "inheritsFrom": "gab:BaseAgent",

  "stateActors": [
    { "@ref": "ctx:ContextLoadingStateActor" },
    { "@ref": "ctx:ContextConfidenceStateActor" },
    { "@ref": "ctx:NavigationStateActor" },
    { "@ref": "ctx:DebugContextStateActor" }
  ],

  "modes": [
    { "@ref": "ctx:ContextLoadingMode" },
    { "@ref": "ctx:ContextValidationMode" },
    { "@ref": "ctx:ContextPropagationMode" },
    { "@ref": "ctx:ContextDeliveryMode" }
  ],

  "workflow": {
    "@type": "gab:Workflow",
    "initialMode": { "@ref": "ctx:ContextLoadingMode" },
    "transitions": [
      {
        "from": { "@ref": "ctx:ContextLoadingMode" },
        "to": { "@ref": "ctx:ContextValidationMode" },
        "condition": "ctx:ContextConfidenceStateActor.initialConfidence >= 0.6"
      },
      {
        "from": { "@ref": "ctx:ContextValidationMode" },
        "to": { "@ref": "ctx:ContextPropagationMode" },
        "condition": "ctx:ContextConfidenceStateActor.validationConfidence >= 0.8"
      },
      {
        "from": { "@ref": "ctx:ContextPropagationMode" },
        "to": { "@ref": "ctx:ContextDeliveryMode" },
        "condition": "ctx:ContextConfidenceStateActor.propagationComplete == true"
      }
    ]
  },

  "invocationTrigger": "Session start OR directory change OR explicit /context-load command"
}
```

<!-- section_id: "39bf9caf-4efd-4398-9f9f-0ab1437fe8a4" -->
### 2.2 State Actor Definitions

**File**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/context_agents/context_state_actors.jsonld`

```jsonld
{
  "@context": {
    "@vocab": "https://aalang.org/",
    "gab": "https://aalang.org/gab/",
    "ctx": "https://layer-stage.dev/context/"
  },
  "@graph": [
    {
      "@id": "ctx:ContextLoadingStateActor",
      "@type": "gab:StateActor",
      "name": "Context Loading State Actor",
      "description": "Tracks which context files have been loaded in current session",
      "sessionConsistent": true,
      "state": {
        "loadedFiles": {
          "@type": "array",
          "items": {
            "path": "string",
            "loadedAt": "timestamp",
            "tokenCount": "integer",
            "priority": { "enum": ["absolute", "critical", "standard"] }
          }
        },
        "claudeMdChain": {
          "@type": "array",
          "description": "Ordered list of CLAUDE.md files from root to cwd"
        },
        "rulesLoaded": { "@type": "boolean" },
        "protocolsLoaded": { "@type": "boolean" },
        "knowledgeLoaded": { "@type": "boolean" }
      },
      "methods": {
        "recordLoad": "Add file to loadedFiles with timestamp",
        "isLoaded": "Check if file path already loaded",
        "getChainPosition": "Return current position in CLAUDE.md chain"
      }
    },

    {
      "@id": "ctx:ContextConfidenceStateActor",
      "@type": "gab:StateActor",
      "name": "Context Confidence State Actor",
      "description": "Tracks agent's confidence in current context understanding",
      "sessionConsistent": true,
      "state": {
        "layerIdentified": { "@type": "number", "min": 0, "max": 1 },
        "stageIdentified": { "@type": "number", "min": 0, "max": 1 },
        "rulesAwareness": { "@type": "number", "min": 0, "max": 1 },
        "requiredContextLoaded": { "@type": "number", "min": 0, "max": 1 },
        "overallConfidence": { "@type": "number", "min": 0, "max": 1 }
      },
      "calculation": {
        "overallConfidence": "(layerIdentified * 0.3) + (stageIdentified * 0.2) + (rulesAwareness * 0.3) + (requiredContextLoaded * 0.2)"
      },
      "thresholds": {
        "proceedToValidation": 0.6,
        "proceedToPropagation": 0.8,
        "proceedToDelivery": 0.9,
        "readyForWork": 0.8
      }
    },

    {
      "@id": "ctx:NavigationStateActor",
      "@type": "gab:StateActor",
      "name": "Navigation State Actor",
      "description": "Tracks current position in layer-stage hierarchy",
      "sessionConsistent": true,
      "state": {
        "currentLayer": { "@type": "integer", "description": "-1, 0, 1, etc." },
        "currentStage": { "@type": "string", "pattern": "^(0[1-9]|1[01])$" },
        "currentSubLayer": { "@type": "string" },
        "depth": { "@type": "integer", "description": "Nesting depth from root" },
        "path": { "@type": "string", "description": "Full path to current location" },
        "parent": { "@type": "string", "description": "Path to parent CLAUDE.md" },
        "children": { "@type": "array", "description": "Paths to child CLAUDE.md files" }
      },
      "methods": {
        "updatePosition": "Set current layer/stage/sub_layer based on cwd",
        "getAncestors": "Return all parent CLAUDE.md paths",
        "getSiblings": "Return sibling directories at same level"
      }
    },

    {
      "@id": "ctx:DebugContextStateActor",
      "@type": "gab:StateActor",
      "name": "Debug Context State Actor",
      "description": "Controls visibility of context loading details",
      "sessionConsistent": true,
      "state": {
        "debugMode": { "@type": "boolean", "default": false },
        "verboseLoading": { "@type": "boolean", "default": false },
        "showConfidenceScores": { "@type": "boolean", "default": false },
        "logDecisions": { "@type": "boolean", "default": true }
      },
      "triggers": {
        "enable": "/context-debug on",
        "disable": "/context-debug off"
      }
    }
  ]
}
```

<!-- section_id: "ca7326ab-2b78-4057-8093-95ce1ba7dc2c" -->
### 2.3 Mode Definitions

**File**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/context_agents/context_modes.jsonld`

```jsonld
{
  "@context": {
    "@vocab": "https://aalang.org/",
    "gab": "https://aalang.org/gab/",
    "ctx": "https://layer-stage.dev/context/"
  },
  "@graph": [
    {
      "@id": "ctx:ContextLoadingMode",
      "@type": "gab:Mode",
      "name": "Context Loading Mode",
      "description": "Phase 1: Load all context files in the chain",

      "entryActions": [
        "Initialize ContextLoadingStateActor",
        "Clear previous session context (if new session)"
      ],

      "responsibilities": [
        "Load ~/.claude/CLAUDE.md (if exists)",
        "Load ~/CLAUDE.md (if exists)",
        "Traverse upward from cwd loading all CLAUDE.md files",
        "Load .claude/rules/*.md files",
        "Load CLAUDE.local.md (if exists)",
        "Record each load in ContextLoadingStateActor",
        "Calculate initial confidence score"
      ],

      "exitCondition": "ContextConfidenceStateActor.overallConfidence >= 0.6",

      "isolatedState": {
        "filesToLoad": "array",
        "currentFileIndex": "integer",
        "loadErrors": "array"
      }
    },

    {
      "@id": "ctx:ContextValidationMode",
      "@type": "gab:Mode",
      "name": "Context Validation Mode",
      "description": "Phase 2: Validate context completeness and identify position",

      "entryActions": [
        "Read NavigationStateActor to determine position"
      ],

      "responsibilities": [
        "Identify current layer (0, 1, -1)",
        "Identify current stage (01-11, if applicable)",
        "Identify current sub_layer (if nested)",
        "Check if required context is loaded:",
        "  - sub_layer_0_04_rules (CRITICAL)",
        "  - sub_layer_0_05_protocols (at session start)",
        "  - Relevant knowledge files",
        "Update ContextConfidenceStateActor scores",
        "Flag missing required context"
      ],

      "exitCondition": "ContextConfidenceStateActor.overallConfidence >= 0.8",

      "fallbackAction": "If confidence < 0.8, identify gaps and load missing context"
    },

    {
      "@id": "ctx:ContextPropagationMode",
      "@type": "gab:Mode",
      "name": "Context Propagation Mode",
      "description": "Phase 3: Resolve priorities and propagate context",

      "responsibilities": [
        "Resolve context priority conflicts:",
        "  - absolute: Universal rules (layer_0/rules) - cannot be overridden",
        "  - critical: Project-specific rules - override standard",
        "  - standard: Knowledge, optional guidance - lowest priority",
        "Apply context transformations:",
        "  - Substitute path variables",
        "  - Resolve relative references",
        "  - Merge configurations",
        "Detect and flag contradictory rules",
        "Escalate unresolvable conflicts to user"
      ],

      "exitCondition": "All conflicts resolved OR escalated",

      "isolatedState": {
        "conflicts": "array",
        "resolutions": "array",
        "escalations": "array"
      }
    },

    {
      "@id": "ctx:ContextDeliveryMode",
      "@type": "gab:Mode",
      "name": "Context Delivery Mode",
      "description": "Phase 4: Present context and ready for work",

      "responsibilities": [
        "If DebugContextStateActor.debugMode:",
        "  - Present context summary to user",
        "  - Show files loaded",
        "  - Show current position",
        "  - Show confidence scores",
        "Confirm ready for task execution:",
        "  - All prerequisites satisfied",
        "  - Context confidence >= 0.8",
        "  - Agent knows position and applicable rules"
      ],

      "exitCondition": "User provides task OR timeout",

      "output": {
        "contextReady": "boolean",
        "position": "NavigationStateActor.state",
        "confidence": "ContextConfidenceStateActor.overallConfidence",
        "summary": "string (if debug mode)"
      }
    }
  ]
}
```

---

<!-- section_id: "a01603ff-4934-4c62-aaa4-da0c6c1e97f7" -->
## Part 3: CLAUDE.md Integration

<!-- section_id: "2b66783a-8e44-41a7-934a-bdfa03a344ce" -->
### 3.1 How CLAUDE.md Files Reference AALang Agents

Each CLAUDE.md in the chain should include an **AALang Integration** section:

```markdown
## AALang Integration

### Context Agent
This file is processed by: `@agent ctx:ContextLoadingAgent`

### Context Chain Position
- **Position**: [N of M]
- **Parent**: [path to parent CLAUDE.md]
- **Children**: [paths to child CLAUDE.md files]
- **Priority**: [absolute|critical|standard]

### State Actor Updates
When this file is loaded, update:
- `ctx:ContextLoadingStateActor.loadedFiles` += this file
- `ctx:NavigationStateActor.path` = this directory
- `ctx:ContextConfidenceStateActor.[relevant scores]`

### Required Reads
Before proceeding, agent MUST also load:
- [list of required files from this level]
```

<!-- section_id: "e3c47794-ca4a-45d8-b1dd-17d692807007" -->
### 3.2 Context Chain with AALang References

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  CONTEXT CHAIN WITH AALANG INTEGRATION                                          │
└─────────────────────────────────────────────────────────────────────────────────┘

~/.claude/CLAUDE.md ──────────────────────────────────────────────────────────────┐
│ ## AALang Integration                                                           │
│ @agent ctx:ContextLoadingAgent                                                  │
│ Position: 1/5 (User Global) | Priority: critical                                │
│ Parent: none | Children: ~/CLAUDE.md                                            │
│                                                                                 │
│ ## On Load                                                                      │
│ ctx:ContextLoadingStateActor.loadedFiles += "~/.claude/CLAUDE.md"               │
│ ctx:ContextConfidenceStateActor.rulesAwareness += 0.2                           │
│                                                                                 │
│ ## Required Reads                                                               │
│ - context_loading_protocol.md (when entering layer-stage system)                │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
~/CLAUDE.md ──────────────────────────────────────────────────────────────────────┐
│ ## AALang Integration                                                           │
│ @agent ctx:ContextLoadingAgent                                                  │
│ Position: 2/5 (User Root) | Priority: standard                                  │
│ Parent: ~/.claude/CLAUDE.md | Children: ~/dawson-workspace/CLAUDE.md            │
│                                                                                 │
│ ## On Load                                                                      │
│ ctx:ContextLoadingStateActor.loadedFiles += "~/CLAUDE.md"                       │
│ ctx:NavigationStateActor.depth = 1                                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
~/dawson-workspace/CLAUDE.md ─────────────────────────────────────────────────────┐
│ ## AALang Integration                                                           │
│ @agent ctx:ContextLoadingAgent                                                  │
│ Position: 3/5 (Workspace) | Priority: standard                                  │
│ Parent: ~/CLAUDE.md | Children: code/CLAUDE.md                                  │
│                                                                                 │
│ ## On Load                                                                      │
│ ctx:ContextLoadingStateActor.loadedFiles += "~/dawson-workspace/CLAUDE.md"      │
│ ctx:NavigationStateActor.depth = 2                                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
~/dawson-workspace/code/CLAUDE.md ────────────────────────────────────────────────┐
│ ## AALang Integration                                                           │
│ @agent ctx:ContextLoadingAgent                                                  │
│ Position: 4/5 (Code Root) | Priority: standard                                  │
│ Parent: ../CLAUDE.md | Children: 0_layer_universal/CLAUDE.md                    │
│                                                                                 │
│ ## On Load                                                                      │
│ ctx:ContextLoadingStateActor.loadedFiles += ".../code/CLAUDE.md"                │
│ ctx:NavigationStateActor.depth = 3                                              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
~/dawson-workspace/code/0_layer_universal/CLAUDE.md ──────────────────────────────┐
│ ## AALang Integration                                                           │
│ @agent ctx:ContextLoadingAgent                                                  │
│ Position: 5/5 (Layer-Stage Root) | Priority: absolute                           │
│ Parent: ../CLAUDE.md | Children: layer_0/, layer_1/, layer_-1_research/         │
│                                                                                 │
│ ## On Load                                                                      │
│ ctx:ContextLoadingStateActor.loadedFiles += ".../0_layer_universal/CLAUDE.md"   │
│ ctx:ContextLoadingStateActor.rulesLoaded = true (after loading sub_layer_04)    │
│ ctx:ContextLoadingStateActor.protocolsLoaded = true (after loading sub_layer_05)│
│ ctx:NavigationStateActor.currentLayer = 0                                       │
│ ctx:ContextConfidenceStateActor.layerIdentified = 1.0                           │
│                                                                                 │
│ ## Required Reads (CRITICAL)                                                    │
│ - layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/                           │
│ - layer_0/layer_0_03_sub_layers/sub_layer_0_05_protocols/                       │
│                                                                                 │
│ ## AALang System Reference                                                      │
│ Primary AI System: sub_layer_0_01_ai_system/                                    │
│ Context Agents: sub_layer_0_01_ai_system/context_agents/                        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

<!-- section_id: "1455fffd-e5a4-486c-96be-9946737225fd" -->
### 3.3 Bidirectional Integration

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│  BIDIRECTIONAL INTEGRATION: CLAUDE.md ↔ AALang Agents                           │
└─────────────────────────────────────────────────────────────────────────────────┘

DIRECTION 1: CLAUDE.md → AALang Agent
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLAUDE.md files INVOKE agents by:
  • @agent directive: `@agent ctx:ContextLoadingAgent`
  • State updates: `ctx:StateActor.property = value`
  • Required reads: Force agent to load additional files

Example in CLAUDE.md:
```markdown
@agent ctx:ContextLoadingAgent
@state ctx:NavigationStateActor.currentLayer = 0
@require sub_layer_0_04_rules/
```

DIRECTION 2: AALang Agent → CLAUDE.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Agents INFORM CLAUDE.md processing by:
  • Confidence gates: Don't proceed until confidence >= 0.8
  • Priority resolution: Which rules override which
  • Context injection: Add computed state to agent context

Example agent behavior:
```
if (ctx:ContextConfidenceStateActor.overallConfidence < 0.8) {
  HALT: "Insufficient context. Missing: [list gaps]"
  ACTION: Load missing files before proceeding
}
```

INTEGRATION POINTS:
━━━━━━━━━━━━━━━━━━━
1. Session Start → ContextLoadingAgent activated
2. Each CLAUDE.md load → State actors updated
3. Validation phase → Check required reads from CLAUDE.md
4. Propagation phase → Apply priorities from CLAUDE.md
5. Delivery phase → Agent confirms ready, provides summary
```

---

<!-- section_id: "1b8bf444-e93e-41de-8ff9-044631d7caa6" -->
## Part 4: GAB System Integration

<!-- section_id: "a444a4bb-4e79-4ee7-82b0-30839984641f" -->
### 4.1 Mapping GAB Concepts to Context System

| GAB Concept | Context System Equivalent |
|-------------|---------------------------|
| `gab:Clarification` | `ctx:ContextLoadingMode` - gather context |
| `gab:Discussion` | `ctx:ContextValidationMode` - verify completeness |
| `gab:Formalization` | `ctx:ContextPropagationMode` - resolve priorities |
| `gab:Generation` | `ctx:ContextDeliveryMode` - ready for work |
| `gab:UnderstandingIndicators` | `ctx:ContextConfidenceStateActor` |
| `gab:DebugMode` | `ctx:DebugContextStateActor` |
| `gab:DecisionLog` | Context loading audit trail |

<!-- section_id: "ceadce9b-0a3a-4a78-9faf-65db6c3570a9" -->
### 4.2 Using gab.jsonld Patterns

The context agents inherit patterns directly from gab.jsonld:

```jsonld
{
  "@id": "ctx:ContextLoadingAgent",
  "inheritsFrom": "gab:BaseAgent",

  "patterns": {
    "modeTransition": {
      "@ref": "gab:ModeTransitionPattern",
      "description": "Confidence-gated transitions between phases"
    },
    "stateIsolation": {
      "@ref": "gab:StateIsolationPattern",
      "description": "Each mode has private state, shared via actors"
    },
    "qualityChecklist": {
      "@ref": "gab:QualityChecklistPattern",
      "description": "Systematic verification before completion"
    }
  }
}
```

<!-- section_id: "ce94f141-cf79-4fe9-9d62-8816c8b93405" -->
### 4.3 GAB Quality Checklist for Context

Adapted from gab.jsonld's quality verification:

```markdown
## Context Quality Checklist (Before Task Execution)

### Loading Quality
- [ ] All CLAUDE.md files in chain loaded
- [ ] .claude/rules/*.md files loaded
- [ ] CLAUDE.local.md loaded (if exists)
- [ ] No load errors encountered

### Position Quality
- [ ] Current layer identified (0, 1, -1)
- [ ] Current stage identified (if applicable)
- [ ] Current sub_layer identified (if nested)
- [ ] Depth calculated correctly

### Rules Quality
- [ ] sub_layer_0_04_rules loaded
- [ ] Universal rules identified
- [ ] Priority conflicts resolved
- [ ] No contradictory rules unresolved

### Confidence Quality
- [ ] layerIdentified >= 0.8
- [ ] stageIdentified >= 0.8 (or N/A)
- [ ] rulesAwareness >= 0.8
- [ ] overallConfidence >= 0.8
```

---

<!-- section_id: "710d5312-f2c5-4e51-ad22-93894ff795c3" -->
## Part 5: Implementation Plan

<!-- section_id: "20e276f2-630f-40a7-b78c-ca692e5c87d5" -->
### 5.1 Files to Create

```
NEW FILES:
━━━━━━━━━━

layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/context_agents/
├── context_loading_agent.jsonld      # Main agent definition
├── context_state_actors.jsonld       # State actor definitions
├── context_modes.jsonld              # Mode definitions
└── README.md                         # Documentation

layer_0/layer_0_03_sub_layers/sub_layer_0_05_protocols/
├── context_loading_protocol.md       # Human-readable protocol
└── context_quality_checklist.md      # Quality verification

layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/
├── context_priority_rules.md         # Priority system
└── context_scope_boundaries.md       # Scope definitions
```

<!-- section_id: "cce1e7f3-fbc2-43b8-981f-9c4b2e6803cc" -->
### 5.2 Files to Update

```
CLAUDE.md CHAIN UPDATES:
━━━━━━━━━━━━━━━━━━━━━━━━

1. ~/.claude/CLAUDE.md
   + Add: ## AALang Integration section
   + Add: @agent ctx:ContextLoadingAgent
   + Add: Position: 1/5, Priority: critical

2. ~/CLAUDE.md
   + Add: ## AALang Integration section
   + Add: Position: 2/5, Priority: standard

3. ~/dawson-workspace/CLAUDE.md
   + Add: ## AALang Integration section
   + Add: Position: 3/5, Priority: standard

4. ~/dawson-workspace/code/CLAUDE.md
   + Add: ## AALang Integration section
   + Add: Position: 4/5, Priority: standard

5. ~/dawson-workspace/code/0_layer_universal/CLAUDE.md
   + Add: ## AALang Integration section
   + Add: Position: 5/5, Priority: absolute
   + Add: ## Required Reads (CRITICAL)
   + Add: ## AALang System Reference
```

<!-- section_id: "85c9c392-ac8e-48e3-9edd-57eeb91f52a9" -->
### 5.3 Implementation Phases

```
PHASE 1: Core Agent Definitions (This Session)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [ ] Create context_agents/ directory
- [ ] Create context_loading_agent.jsonld
- [ ] Create context_state_actors.jsonld
- [ ] Create context_modes.jsonld
- [ ] Create README.md for context_agents/

PHASE 2: Protocol Documentation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [ ] Create context_loading_protocol.md
- [ ] Create context_quality_checklist.md
- [ ] Create context_priority_rules.md
- [ ] Create context_scope_boundaries.md

PHASE 3: CLAUDE.md Chain Updates
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [ ] Update ~/.claude/CLAUDE.md
- [ ] Update ~/CLAUDE.md
- [ ] Update ~/dawson-workspace/CLAUDE.md
- [ ] Update ~/dawson-workspace/code/CLAUDE.md
- [ ] Update ~/dawson-workspace/code/0_layer_universal/CLAUDE.md

PHASE 4: Testing & Validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- [ ] Test context loading sequence
- [ ] Verify state actor updates
- [ ] Validate confidence calculations
- [ ] Test priority resolution
```

---

<!-- section_id: "ab6ac777-d8fa-4264-884c-457733b7a99f" -->
## Part 6: Open Questions

1. **Agent Execution Model**: How do AALang agents actually execute?
   - Option A: Purely declarative (inform agent behavior via patterns)
   - Option B: Active execution (custom runtime interprets JSON-LD)
   - Option C: Hybrid (declarative definitions, AI interprets at runtime)

2. **State Persistence**: How long do state actors persist?
   - Session-only (current approach)
   - Cross-session (requires persistent storage)
   - Configurable per actor

3. **Submodule Integration**: AALang is a git submodule. How do we:
   - Keep context_agents/ in our repo (not in submodule)?
   - Reference gab.jsonld patterns without modifying submodule?

4. **Confidence Thresholds**: Are the proposed thresholds correct?
   - 0.6 for loading → validation
   - 0.8 for validation → propagation
   - 0.9 for propagation → delivery
   - 0.8 for ready to work

---

<!-- section_id: "485437aa-faa9-4838-bdde-020dd3c90077" -->
## Part 7: Summary

This proposal creates a **living context system** powered by AALang agents:

1. **AALang Agents** (JSON-LD) define how context loading works
2. **State Actors** track what's loaded, confidence, position
3. **Modes** structure the 4-phase loading sequence
4. **CLAUDE.md files** reference agents and provide chain position
5. **Bidirectional integration** means agents inform CLAUDE.md and vice versa
6. **GAB patterns** (confidence gates, quality checklists) ensure reliability

The result: AI agents that **understand where they are** and **know what rules apply** before starting any work.

---

<!-- section_id: "f8dc9cc9-1ba4-46a9-8e3e-ae2b4091ef54" -->
## References

- **AALang/Gab Specification**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/gab.jsonld`
- **Context Problems Analysis**: `layer_-1_research/.../things_learned/01_context_problems.md`
- **Navigation System**: `layer_-1_research/.../layer_1_subx2_feature_navigation_system/index.jsonld`
- **Implementation Roadmap**: `layer_-1_research/.../outputs/overview/implementation_roadmap.md`
- **Official Claude Code Loading**: `layer_-1_research/.../diagrams/current/official_claude_code_loading.md`
- **Custom Layer-Stage Loading**: `layer_-1_research/.../diagrams/current/custom_layer_stage_loading.md`

---

*Proposal v2 - 2026-02-05*
*Ready for review and approval*
