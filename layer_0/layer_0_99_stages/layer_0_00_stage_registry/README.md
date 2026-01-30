# Stage Registry (Stable IDs)

**Purpose**: Make stage references stable even when numeric ordering changes.

**Updated**: 2026-01-25

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

## Version History

| Version | Stages | Changes |
|---------|--------|---------|
| v1.0 | 00-09 | Original 10 stages |
| v2.0 | 00-10 | Added `01_research` stage, renumbered 01-09 → 02-10 |

## Problem

Stage numbers (e.g., `stage_1_05_development`) are **ordering labels**, not identifiers. If we insert/reorder stages, renumbering breaks every doc that hard-links to `stage_N_XX_*` paths.

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

## Stage Structure

Each stage directory contains:

```
stage_N_XX_name/
├── ai_agent_system/       # Agent configuration
├── hand_off_documents/    # Concise handoff notes (reference outputs)
└── outputs/               # Stage artifacts
```

The `outputs/` folder allows handoff documents to remain concise by referencing artifacts rather than duplicating content inline.

## Usage

### Get stage by slug
```yaml
# In YAML configs or scripts
stage: research  # Instead of: stage_N_01_research
```

### Reference in documentation
```markdown
See the [research stage](aliases/research.md) for exploration guidelines.
```

## Automation

Generate/update the registry + aliases:

```bash
python3 layer_0/layer_0_99_stages/layer_0_00_stage_registry/scripts/stage_registry.py generate
```

Check for hard-linked numeric references in docs:

```bash
python3 layer_0/layer_0_99_stages/layer_0_00_stage_registry/scripts/stage_registry.py check-hardlinks
```
