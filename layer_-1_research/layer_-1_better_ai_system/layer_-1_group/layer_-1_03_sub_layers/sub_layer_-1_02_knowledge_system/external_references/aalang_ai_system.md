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

## Relationship to Better AI System

This external AI system serves as a reference implementation and research resource for the better_ai_system project. It provides:

- AI language design patterns
- Compiler architecture insights
- Language specification approaches (JSON-LD based)

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
