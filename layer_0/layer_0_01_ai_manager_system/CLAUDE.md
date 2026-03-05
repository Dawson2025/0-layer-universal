<!-- derived_from: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac" -->
# AI Manager System

## Identity

| Property | Value |
|----------|-------|
| **Layer** | 0 (Universal) |
| **Position** | `layer_0/layer_0_01_ai_manager_system/` |
| **Role** | **AI SYSTEM ROOT** - Contains both the AI language (professor) and personal orchestration system |

## Purpose

This directory contains the core AI systems that power agent execution:

1. **Professor** (`professor/`) - The AALang/GAB language and compiler
2. **Personal** (`personal/`) - Your custom orchestrator implementation

---

## Directory Structure

```
layer_0_01_ai_manager_system/
├── CLAUDE.md              ← You are here
├── professor/             ← AALang/GAB (git submodule)
│   ├── CLAUDE.md          ← Language context
│   ├── gab.jsonld         ← Main language spec
│   ├── gab-runtime.jsonld ← Runtime spec
│   ├── gab-formats.jsonld ← Format definitions
│   └── ...
├── personal/              ← Your orchestrator
│   ├── CLAUDE.md          ← Orchestrator context
│   ├── layer_0_orchestrator.gab.jsonld      ← Agent definition
│   ├── layer_0_orchestrator.integration.md  ← Readable summary (auto-generated)
│   ├── runtime/
│   │   └── orchestrator_runtime.jsonld
│   └── tests/
│       ├── orchestrator_runner.sh
│       └── integration_test.sh
├── agnostic/              ← Platform-agnostic resources
└── specific/              ← Platform-specific resources
```

---

## When to Load Each Subsystem

| Situation | Load |
|-----------|------|
| Understanding AALang patterns | `professor/CLAUDE.md` |
| Creating new agents | `professor/gab-formats.jsonld` |
| Multi-agent orchestration | `personal/CLAUDE.md` |
| Quick orchestrator reference | `personal/layer_0_orchestrator.integration.md` |
| Precise orchestrator constraints | `personal/layer_0_orchestrator.gab.jsonld` (via jq) |
| Task decomposition | `personal/runtime/orchestrator_runtime.jsonld` |

---

## Integration Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    AI MANAGER SYSTEM                        │
│                                                             │
│   ┌─────────────────────┐     ┌─────────────────────┐      │
│   │      PROFESSOR      │     │       PERSONAL      │      │
│   │   (AALang/GAB)      │     │   (Orchestrator)    │      │
│   │                     │     │                     │      │
│   │  Provides:          │     │  Uses:              │      │
│   │  • Language spec    │────►│  • 5-mode-15-actor  │      │
│   │  • Runtime model    │     │  • State actors     │      │
│   │  • Mode-Actor       │     │  • Spawn protocol   │      │
│   │    patterns         │     │  • Hand-off docs    │      │
│   └─────────────────────┘     └─────────────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Context Chain Position

- **Parent**: `layer_0/CLAUDE.md`
- **Children**:
  - `professor/CLAUDE.md` (AALang)
  - `personal/CLAUDE.md` (Orchestrator)

---

## AALang Integration

@agent ctx:ContextLoadingAgent

### On Load

When this file is loaded, update state actors:
- `ctx:ContextLoadingStateActor.loadedFiles` += layer_0_01_ai_manager_system/CLAUDE.md
- `ctx:NavigationStateActor.aiSystemRoot` = true

### Next Steps

Based on task type, load appropriate child context:
- **Language/pattern questions** → Load `professor/CLAUDE.md`
- **Orchestration/multi-agent** → Load `personal/CLAUDE.md`
