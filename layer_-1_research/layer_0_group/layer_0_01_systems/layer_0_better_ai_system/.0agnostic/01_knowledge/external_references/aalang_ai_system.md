---
resource_id: "631af721-b958-498e-a271-d9eda8566811"
resource_type: "knowledge"
resource_name: "aalang_ai_system"
---
# AALang AI System Reference

## Location

**Universal Layer**: `../../../../../../layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/`

**Full Path**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/`

## Repository

| Property | Value |
|----------|-------|
| **Your Fork** | https://github.com/Dawson2025/AALang-Gab.git |
| **Upstream (Original)** | https://github.com/yenrab/AALang-Gab.git |
| **Type** | Git submodule |
| **Tracked Branch** | `dawson` |

## Description

**PRIMARY AI SYSTEM** - Development of the AALang language and gab compiler. This is the main AI system we use for most everything. A Python-based project for AI language design.

## Branching Strategy

```
UPSTREAM (yenrab/AALang-Gab)
         │
         │ fetch/pull
         ▼
    main branch ──────── Review upstream changes here
         │
         │ merge/cherry-pick
         ▼
    dawson branch ─────── Personal customizations (WORKING BRANCH)
```

| Branch | Purpose |
|--------|---------|
| `main` | Sync with upstream for review. Pull upstream changes here. DO NOT work directly on main. |
| `dawson` | Personal customizations and development. This is the working branch. |

## Workflow

### Syncing with Upstream

```bash
# In the submodule directory
cd layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system

# Add upstream remote (one-time)
git remote add upstream https://github.com/yenrab/AALang-Gab.git

# Fetch and merge upstream into main
git fetch upstream
git checkout main
git merge upstream/main

# Review, then integrate into dawson
git checkout dawson
git merge main  # or cherry-pick specific commits
```

### Daily Development

```bash
git checkout dawson
# Make changes
git add . && git commit -m "message"
git push origin dawson
```

## Relationship to Layer-Stage System

**AALang is the primary way agents work within our entire layer-stage system.** It is not just a reference - it is the foundational AI system used at:

- **Every layer** (layer_0, layer_1, layer_-1, etc.)
- **Every stage** (01-11: request_gathering through archives)
- **Every sub_layer** (knowledge, principles, rules, protocols, setup)
- **Every sub_stage** and nested structure

When operating anywhere in the layer-stage hierarchy, agents use AALang as the underlying AI system.

## What AALang Provides

- AI language design patterns
- Compiler architecture (gab compiler)
- Language specification approaches (JSON-LD based)
- The foundational capabilities for how agents work

## Key Files in AALang

| File | Purpose |
|------|---------|
| `gab.jsonld` | Main language specification |
| `gab-runtime.jsonld` | Runtime specification |
| `gab-formats.jsonld` | Format definitions |
| `index.jsonld` | Navigation index |
| `CLAUDE.md` | Context chain integration (on dawson branch) |

## History

- **Date Added**: 2026-02-05
- **Position**: sub_layer_0_01_ai_system
- **Restructure**: prompts moved to 05_protocols to make room for ai_system at 01
