# Layer + Stage Framework Templates

Use these templates to scaffold any new context (universal, project, feature, component).
- **Layers (specificity):** lower numbers are more universal and are prerequisites for higher numbers.
- **Stages (workflow):** numbered 0.0–0.7 inside each `.99_stages` folder.
- **Status:** each layer has a `status_template.json` in its `.99_stages` folder (copy and adapt per layer).

Structure per layer:
- 0/1/2/3.x subfolders hold the layer content (basic prompts, principles, rules, setup, architecture, tools).
- `.99_stages/` contains stage folders `0.0_instructions` through `0.7_archives` plus a status template.

To instantiate for a real project/feature/component:
1) Copy the appropriate template folder.
2) Rename it (e.g., `1_project_<name>`, `2_feature_<name>`, `3_component_<name>`).
3) Fill in the README placeholders and status file.
4) Populate the stage folders with the right docs.
