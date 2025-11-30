# Layer + Stage Framework

This repository uses two orthogonal systems to manage AI context and workflows. Numbering is zero-padded for lexicographic stability (e.g., 1.00, 1.10, 1.20).

- **Layer System (specificity)**: from universal → project → feature → component. Lower numbers are more universal and are prerequisites for higher numbers. Example universal 0.x band: 0.00 basic prompts, 0.10 SE knowledge, 0.20 principles, 0.30 rules, 0.40 OS setup, 0.50 coding app setup, 0.60 apps/browsers/extensions, 0.70 AI apps/tools, 0.80 AI models, 0.90 universal tools.
- **Stage System (chronology)**: inside every layer, stages 0.00–0.70 capture workflow time: 0.00 instructions, 0.10 planning, 0.20 design, 0.30 development, 0.40 testing, 0.50 criticism, 0.60 fixing, 0.70 archives.

## Purpose
- **Deterministic navigation**: Each layer has a root and numbered slots; each layer has a `*.99_stages` folder for the Stage System. This lets agents locate the exact context by Layer + Stage instead of fuzzy search.
- **Dependency clarity**: Higher layers depend on lower ones (e.g., models depend on tools depend on OS; features depend on project architecture depend on universal rules).
- **Handoff & audit**: Stages and per-layer status files support handoffs, progress tracking, and archival for replay/debug.

## Templates here
This folder contains templates to scaffold layers:
- `0_universal_template/`
- `1_project_template/`
- `2_feature_template/`
- `3_component_template/`

Each template includes:
- Numbered slots for that layer (e.g., 1.00–1.90 for project, 2.00–2.90 for feature, etc.).
- A `*.99_stages/` folder with stage subfolders (0.00–0.70) and a `status_template.json`.

## How to instantiate for a real context
1) Copy the appropriate template to your context repo and rename (e.g., `layer_0_universal`, `layer_1_project`, `layer_2_feature_X`, `layer_3_component_Y`).
2) Populate the numbered slots with your actual content. Use lower numbers for more foundational items.
3) Keep existing docs as-is or move them; you can place legacy material in a `legacy_import/` subfolder under the appropriate slot while you reorganize.
4) Use the Stage folders to file work artifacts by lifecycle, and update the `status.json` to track progress per layer.

## How it works with sessions
- At session start, load the universal layer (`layer_0_universal`), then the relevant project (`layer_1_*`), feature (`layer_2_*`), and component (`layer_3_*`) layers as needed.
- Within each layer, load the current Stage folders (e.g., instructions, design, development, testing) based on the task.
- The manager agent can address a point in the grid as (Layer, Stage), e.g., `(layer_2_feature_checkout, 0.3_development)`, to fetch the right docs and update status.

## Status tracking
- Each layer’s `*.99_stages/status*.json` tracks `current_stage` and per-stage state (`not_started | in_progress | blocked | done`).
- This enables dashboards and automated routing for agents.

## Why this structure
- Mirrors hierarchical memory best practices: scoped layers + typed, chronological stages.
- Git-friendly, human-readable, deterministic; complements search/RAG rather than replacing it.
- Scales across universal/project/feature/component without changing the mental model.
