---
resource_id: "be1005b3-eeef-4d05-9265-a7c4b545757c"
resource_type: "readme
document"
resource_name: "README"
---
# Stage Registry (Stable IDs)

**Purpose**: Make stage references stable even when numeric ordering changes.

**Updated**: 2026-01-25

<!-- section_id: "d614663c-ede3-47cb-afa7-5e27a5d60492" -->
## Current Stages (v2.0)

| Slug | Number | Name | Purpose |
|------|--------|------|---------|
| `request_gathering` | 00 | Request Gathering | Gather initial requirements |
| `research` | 01 | Research | Explore problem space, gather info |
| `instructions` | 02 | Instructions | Define what needs to be done |
| `planning` | 03 | Planning | Plan how to accomplish work |
| `design` | 04 | Design | Architecture decisions |
| `development` | 05 | Development | Implementation |
| `testing` | 06 | Testing | Verification |
| `criticism` | 07 | Criticism | Review and critique |
| `fixing` | 08 | Fixing | Address issues |
| `current_product` | 09 | Current Product | Working deliverable |
| `archives` | 10 | Archives | Historical records |

<!-- section_id: "d2607a7e-252d-4708-a23b-3f7d7be1696d" -->
## Version History

| Version | Stages | Changes |
|---------|--------|---------|
| v1.0 | 00-09 | Original 10 stages |
| v2.0 | 00-10 | Added `01_research` stage, renumbered 01-09 → 02-10 |

<!-- section_id: "3959fdf8-367a-4ed7-89ef-b57d82fce8e0" -->
## Problem

Stage numbers (e.g., `stage_1_05_development`) are **ordering labels**, not identifiers. If we insert/reorder stages, renumbering breaks every doc that hard-links to `stage_N_XX_*` paths.

<!-- section_id: "f61f8782-be98-48e9-9e78-776894449f0a" -->
## Solution

Use **stable slugs** (e.g., `development`) and resolve them via:

- Registry file: `stage_registry.yaml`
- Alias links: `aliases/<slug>.md` (these point to the current numbered folder)

When writing docs, prefer linking to:

```
layer_0/layer_0_99_stages/layer_0_00_stage_registry/aliases/<slug>.md
```

Instead of linking directly to:

```
layer_N/layer_N_99_stages/stage_N_XX_<slug>/...
```

<!-- section_id: "15632a28-810d-4fff-bb4f-e2cb1e671576" -->
## Stage Structure

Each stage directory contains:

```
stage_N_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes (reference outputs)
└── outputs/               # Stage artifacts
```

The `outputs/` folder allows handoff documents to remain concise by referencing artifacts rather than duplicating content inline.

<!-- section_id: "0118d2fa-2dee-41a1-8c69-aa16b575ebb8" -->
## Usage

<!-- section_id: "069f0e88-8277-43dc-ab2b-388825cc6339" -->
### Get stage by slug
```yaml
# In YAML configs or scripts
stage: research  # Instead of: stage_N_01_research
```

<!-- section_id: "4acc771d-0c9c-4dcc-b2fa-3e1f7c274716" -->
### Reference in documentation
```markdown
See the [research stage](aliases/research.md) for exploration guidelines.
```

<!-- section_id: "9bf6b5ad-ee34-4ee1-aca0-e750d12a8a40" -->
## Automation

Generate/update the registry + aliases:

```bash
python3 layer_0/layer_0_99_stages/layer_0_00_stage_registry/scripts/stage_registry.py generate
```

Check for hard-linked numeric references in docs:

```bash
python3 layer_0/layer_0_99_stages/layer_0_00_stage_registry/scripts/stage_registry.py check-hardlinks
```
