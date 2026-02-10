# Context Architecture Diagram

**Purpose**: Answer "What context exists and where does it live?"
**Last Updated**: 2026-02-05

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CONTEXT ARCHITECTURE                                   │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                              CONTEXT TYPES                                       │
├─────────────────────────────────┬───────────────────────────────────────────────┤
│         STATIC CONTEXT          │            DYNAMIC CONTEXT                     │
│    (Doesn't change often)       │         (Changes per session)                  │
├─────────────────────────────────┼───────────────────────────────────────────────┤
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │       CLAUDE.md           │  │  │          status.json                  │    │
│  │  • Identity & role        │  │  │  • Current state                      │    │
│  │  • Navigation hints       │  │  │  • Active tasks                       │    │
│  │  • Key behaviors          │  │  │  • Last modified                      │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │      index.jsonld         │  │  │      hand_off_documents/              │    │
│  │  • Navigation graph       │  │  │  • incoming/from_above/               │    │
│  │  • Conventions            │  │  │  • incoming/from_below/               │    │
│  │  • Triggers               │  │  │  • outgoing/to_above/                 │    │
│  │  • Tree of needs links    │  │  │  • outgoing/to_below/                 │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │  ┌───────────────────────────────────────┐    │
│  │    sub_layer_0_04_rules/  │  │  │       session memory                  │    │
│  │  • Universal rules        │  │  │  • episodic/                          │    │
│  │  • Safety governance      │  │  │  • conversation history               │    │
│  │  • Protocols              │  │  │  • task progress                      │    │
│  └───────────────────────────┘  │  └───────────────────────────────────────┘    │
│                                 │                                                │
│  ┌───────────────────────────┐  │                                                │
│  │    .claude/skills/        │  │                                                │
│  │  • Workflow skills        │  │                                                │
│  │  • Entity creation        │  │                                                │
│  │  • Stage-specific         │  │                                                │
│  └───────────────────────────┘  │                                                │
│                                 │                                                │
└─────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## Context Sources

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                            CONTEXT SOURCES                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   LEVEL 1: Global                                                                │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  ~/.claude/CLAUDE.md                                                     │   │
│   │  • Machine-level rules                                                   │   │
│   │  • Universal behaviors                                                   │   │
│   │  • Global settings                                                       │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                              │                                                   │
│                              ▼                                                   │
│   LEVEL 2: User                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  ~/CLAUDE.md                                                             │   │
│   │  • User preferences                                                      │   │
│   │  • Workspace pointers                                                    │   │
│   │  • Inherits from global                                                  │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                              │                                                   │
│                              ▼                                                   │
│   LEVEL 3: Workspace                                                             │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  ~/dawson-workspace/CLAUDE.md                                            │   │
│   │  • Workspace conventions                                                 │   │
│   │  • Sync awareness                                                        │   │
│   │  • Inherits from user                                                    │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                              │                                                   │
│                              ▼                                                   │
│   LEVEL 4: Project                                                               │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  0_layer_universal/CLAUDE.md                                             │   │
│   │  • Layer-stage conventions                                               │   │
│   │  • Universal rules                                                       │   │
│   │  • Sub-layer navigation                                                  │   │
│   │  • Inherits from workspace                                               │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                              │                                                   │
│                              ▼                                                   │
│   LEVEL 5: Layer                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  layer_-1_research/CLAUDE.md                                             │   │
│   │  layer_-1_better_ai_system/CLAUDE.md                                     │   │
│   │  • Layer-specific context                                                │   │
│   │  • Project-specific context                                              │   │
│   │  • Inherits from project                                                 │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                              │                                                   │
│                              ▼                                                   │
│   LEVEL 6: Feature/Stage                                                         │
│   ┌─────────────────────────────────────────────────────────────────────────┐   │
│   │  layer_0_feature_*/CLAUDE.md                                             │   │
│   │  stage_-1_*/CLAUDE.md                                                    │   │
│   │  • Feature-specific behaviors                                            │   │
│   │  • Stage-specific workflows                                              │   │
│   │  • Inherits from layer                                                   │   │
│   └─────────────────────────────────────────────────────────────────────────┘   │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Context by Category

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                          CONTEXT BY CATEGORY                                     │
└─────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│      IDENTITY        │  │     NAVIGATION       │  │       RULES          │
│                      │  │                      │  │                      │
│  Source:             │  │  Source:             │  │  Source:             │
│  • CLAUDE.md         │  │  • index.jsonld      │  │  • sub_layer_0_04_   │
│                      │  │  • CLAUDE.md nav     │  │    rules/            │
│  Contains:           │  │                      │  │  • CLAUDE.md         │
│  • Role              │  │  Contains:           │  │                      │
│  • Scope             │  │  • nav:parent        │  │  Contains:           │
│  • Responsibilities  │  │  • nav:children      │  │  • Universal rules   │
│  • Key behaviors     │  │  • nav:siblings      │  │  • Protocols         │
│                      │  │  • nav:stages        │  │  • Safety governance │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘

┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│    CONVENTIONS       │  │      TRIGGERS        │  │       STATE          │
│                      │  │                      │  │                      │
│  Source:             │  │  Source:             │  │  Source:             │
│  • index.jsonld      │  │  • index.jsonld      │  │  • status.json       │
│    conventions       │  │    trigger:*         │  │  • hand_off_docs/    │
│                      │  │                      │  │                      │
│  Contains:           │  │  Contains:           │  │  Contains:           │
│  • childNaming       │  │  • onEntityCreation  │  │  • Current tasks     │
│  • entityTypes       │  │  • onStageEnter      │  │  • Progress          │
│  • layer numbers     │  │  • onSessionStart    │  │  • Handoffs          │
│                      │  │  • onNavigation      │  │  • History           │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘
```

---

## File Type Reference

| File | Type | Purpose | When Loaded |
|------|------|---------|-------------|
| `CLAUDE.md` | Static | Identity, navigation, behaviors | Session start, entering directory |
| `index.jsonld` | Static | Navigation graph, conventions, triggers | Entering directory, following links |
| `status.json` | Dynamic | Current state, tasks | Session start, task changes |
| `hand_off_documents/` | Dynamic | Communication between layers | Task delegation, results |
| `.claude/skills/` | Static | Workflow skills, validation | Triggered by actions |
| `sub_layer_0_04_rules/` | Static | Universal rules | Always (in context) |
