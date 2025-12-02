# Layer + Stage Framework

This repository uses two orthogonal systems to manage AI context and workflows. Numbering is zero-padded (two digits after the decimal) for lexicographic stability (e.g., 1.01, 1.10, 1.12).

- **Layer System (specificity)**: from universal → project → feature → component. Lower numbers are more universal and are prerequisites for higher numbers. Each layer stores its numbered slots inside a `*.01_sub_layers/` folder. Example universal 0.x band: 0.01 basic prompts, 0.02 SE knowledge, 0.03 principles, 0.04 rules, 0.05 OS setup, 0.06 coding app setup, 0.07 apps/browsers/extensions, 0.08 AI apps/tools, 0.09 AI models, 0.10 universal tools. Project (1.x), feature (2.x), and component (3.x) bands mirror the same pattern with their own numbering (e.g., 1.01–1.12).
- **Stage System (chronology)**: inside every layer, stages mirror the layer prefix: `L.01–L.08` (e.g., universal uses 0.01–0.08, project uses 1.01–1.08, etc.) covering: instructions, planning, design, development, testing, criticism, fixing, archives.

## Purpose (how context management works)
- **Deterministic navigation**: Each layer has numbered slots and a `*.99_stages` folder. Agents address work as (Layer, Stage) to load only what’s needed instead of fuzzy search.
- **Dependency clarity**: Higher layers depend on lower ones (e.g., models → tools → OS; features → project architecture → universal rules).
- **Handoff & audit**: Stages and per-layer status files support handoffs, progress tracking, and archival for replay/debug. This is the spine of the context management system.

## Templates here
This folder contains templates to scaffold layers:
- `0_universal_template/`
- `1_project_template/`
- `2_feature_template/`
- `3_component_template/`

Each template includes:
- Numbered slots for that layer (e.g., project 1.01–1.12, feature 2.01–2.12, component 3.01–3.12).
- A `*.99_stages/` folder with stage subfolders (0.01–0.08) and a `status_template.json`.

## How to instantiate for a real context
1) Copy the appropriate template to your context repo and rename (e.g., `layer_0_universal`, `layer_1_project`, `layer_2_feature_X`, `layer_3_component_Y`).
2) Populate the numbered slots with your actual content. Use lower numbers for more foundational items. Legacy material can live in a `legacy_import/` subfolder while you reorganize.
3) File artifacts by Stage inside `*.99_stages/` and keep the per-layer `status*.json` updated.
4) The manager/worker agents navigate by Layer + Stage (e.g., `layer_2_feature_checkout` + `0.04_development`) to load, work, and record status.

## How it works with sessions
- At session start, load the universal layer (`layer_0_universal`), then the relevant project (`layer_1_*`), feature (`layer_2_*`), and component (`layer_3_*`) layers as needed.
- Within each layer, operate in the current Stage (instructions/design/development/testing/criticism/fixing/archives) and update status on exit.

## Status tracking
- Each layer’s `*.99_stages/status*.json` tracks `current_stage` and per-stage state (`not_started | in_progress | blocked | done`).
- This enables dashboards and automated routing for agents.

## Why this structure
- Mirrors hierarchical memory best practices: scoped layers + typed, chronological stages.
- Git-friendly, human-readable, deterministic; complements search/RAG rather than replacing it.
- Scales across universal/project/feature/component without changing the mental model.
