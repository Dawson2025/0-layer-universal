---
resource_id: "631af721-b958-498e-a271-d9eda8566811"
resource_type: "knowledge"
resource_name: "aalang_ai_system"
---
# AALang AI System Reference

<!-- section_id: "9d4c2ba2-e7df-42a3-b155-af84a37ce4c4" -->
## Location

**Universal Layer**: `../../../../../../layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/`

**Full Path**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_03_sub_layers/sub_layer_0_01_ai_system/`

<!-- section_id: "da0f7baa-caa2-4ea4-84c3-f3f7e2956188" -->
## Repository

| Property | Value |
|----------|-------|
| **Your Fork** | https://github.com/Dawson2025/AALang-Gab.git |
| **Upstream (Original)** | https://github.com/yenrab/AALang-Gab.git |
| **Type** | Git submodule |
| **Tracked Branch** | `dawson` |

<!-- section_id: "c89a62a3-d189-4fd1-b6b8-9eb2f18a5b10" -->
## Description

**PRIMARY AI SYSTEM** - Development of the AALang language and gab compiler. This is the main AI system we use for most everything. A Python-based project for AI language design.

<!-- section_id: "1b32a198-dc45-403f-bdf3-92acdf438d45" -->
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

<!-- section_id: "45549756-f9ad-4bad-9b18-a8190d65d2f7" -->
## Workflow

<!-- section_id: "ebf0c2b7-fee9-4d3c-a7f5-e2b598c13084" -->
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

<!-- section_id: "46fb79ef-dac0-48c8-b347-7f09eae7c4fc" -->
### Daily Development

```bash
git checkout dawson
# Make changes
git add . && git commit -m "message"
git push origin dawson
```

<!-- section_id: "55a458f0-df2a-4c2c-8915-44c6236ef147" -->
## Relationship to Layer-Stage System

**AALang is the primary way agents work within our entire layer-stage system.** It is not just a reference - it is the foundational AI system used at:

- **Every layer** (layer_0, layer_1, layer_-1, etc.)
- **Every stage** (01-11: request_gathering through archives)
- **Every sub_layer** (knowledge, principles, rules, protocols, setup)
- **Every sub_stage** and nested structure

When operating anywhere in the layer-stage hierarchy, agents use AALang as the underlying AI system.

<!-- section_id: "b6740c10-8041-42da-9c6d-98d38627063e" -->
## What AALang Provides

- AI language design patterns
- Compiler architecture (gab compiler)
- Language specification approaches (JSON-LD based)
- The foundational capabilities for how agents work

<!-- section_id: "e40b623a-3562-4441-bfb7-715a0b041eaf" -->
## Key Files in AALang

| File | Purpose |
|------|---------|
| `gab.jsonld` | Main language specification |
| `gab-runtime.jsonld` | Runtime specification |
| `gab-formats.jsonld` | Format definitions |
| `index.jsonld` | Navigation index |
| `CLAUDE.md` | Context chain integration (on dawson branch) |

<!-- section_id: "44666382-0346-4879-8c1b-2f1cb182f130" -->
## History

- **Date Added**: 2026-02-05
- **Position**: sub_layer_0_01_ai_system
- **Restructure**: prompts moved to 05_protocols to make room for ai_system at 01
