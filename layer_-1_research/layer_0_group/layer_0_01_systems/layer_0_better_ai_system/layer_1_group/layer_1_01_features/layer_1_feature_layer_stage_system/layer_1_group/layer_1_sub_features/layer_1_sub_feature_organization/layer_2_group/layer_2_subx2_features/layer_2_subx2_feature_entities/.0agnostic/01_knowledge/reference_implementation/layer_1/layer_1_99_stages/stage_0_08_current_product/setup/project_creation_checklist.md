---
resource_id: "7fda05d1-967a-4f35-ae21-a82b39b00729"
resource_type: "knowledge"
resource_name: "project_creation_checklist"
---
# Project Creation Checklist

**Purpose:** Detailed checklist for creating a new project from scratch.

**Last Updated:** 2026-01-15

---

<!-- section_id: "f0526289-d1f4-4b9d-869d-2efd3a8fad0d" -->
## Pre-Creation

- [ ] Determine project name (use lowercase with hyphens or underscores)
- [ ] Determine if this is a top-level project or sub-project
- [ ] If sub-project, identify parent and nesting level (subx1, subx2, etc.)
- [ ] Decide if project will be a git submodule or part of parent repo

---

<!-- section_id: "d1a823e5-b787-4391-bd10-a6829d314f58" -->
## Creation Steps

<!-- section_id: "f40b4668-1a79-4296-94ab-f14d300f9008" -->
### 1. Repository Setup

For **top-level project**:
```bash
mkdir <N>_layer_<project_name>
cd <N>_layer_<project_name>
git init
```

For **sub-project** (in parent's sub-projects folder):
```bash
cd <parent>/layer_<N+1>/layer_<N+1>_sub*<X>_projects/
mkdir layer_<N+1>_sub*<X>_project_<name>
cd layer_<N+1>_sub*<X>_project_<name>
git init  # If separate repo
```

- [ ] Created project directory
- [ ] Initialized git (if needed)

<!-- section_id: "4df5c0b1-faff-46db-975c-e7ca76cf8bff" -->
### 2. Copy Template

```bash
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/* .
# Or for sub-project:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_sub_project_template/* .
```

- [ ] Copied appropriate template

<!-- section_id: "f07d65e3-436f-4c36-afda-186666e37c61" -->
### 3. Rename Layer Folders

Replace template `layer_N` with actual layer number:

```bash
# For a Layer 1 project:
mv layer_N layer_1
mv layer_N+1 layer_2

# Rename internal folders
cd layer_1
mv layer_N_00_ai_manager_system layer_1_00_ai_manager_system
mv layer_N_01_manager_handoff_documents layer_1_01_manager_handoff_documents
mv layer_N_02_sub_layers layer_1_02_sub_layers
mv layer_N_99_stages layer_1_99_stages

# Rename handoff subfolders
cd layer_1_01_manager_handoff_documents
mv layer_N_00_to_universal layer_1_00_to_universal
mv layer_N_01_to_specific layer_1_01_to_specific

# Rename sub_layers
cd ../layer_1_02_sub_layers
for d in sub_layer_N.*; do
  mv "$d" "${d/sub_layer_N./sub_layer_1.}"
done

# Rename stages
cd ../layer_1_99_stages
for d in stage_N.*; do
  mv "$d" "${d/stage_N./stage_1.}"
done
```

- [ ] Renamed `layer_N/` to `layer_<actual>/`
- [ ] Renamed `layer_N+1/` to `layer_<actual+1>/`
- [ ] Renamed all `layer_N_*` folders to `layer_<actual>_*`
- [ ] Renamed all `sub_layer_N.*` to `sub_layer_<actual>.*`
- [ ] Renamed all `stage_N.*` to `stage_<actual>.*`
- [ ] Renamed handoff subfolders

<!-- section_id: "f5476c55-6133-44d5-b7be-369495b337cb" -->
### 4. Create Nested Content Folders

```bash
cd layer_<N+1>
mkdir -p layer_<N+1>_sub*<X>_projects
mkdir -p layer_<N+1>_features
mkdir -p layer_<N+1>_components

# Add README to each
echo "# Sub-Projects\n\nNested projects go here." > layer_<N+1>_sub*<X>_projects/README.md
echo "# Features\n\nFeatures go here." > layer_<N+1>_features/README.md
echo "# Components\n\nComponents go here." > layer_<N+1>_components/README.md
```

- [ ] Created `layer_<N+1>_sub*<X>_projects/`
- [ ] Created `layer_<N+1>_features/`
- [ ] Created `layer_<N+1>_components/`
- [ ] Added README.md to each

<!-- section_id: "a869b72a-8a74-4600-876f-8c9b239a3805" -->
### 5. Initialize Status File

```bash
cd layer_<N>/layer_<N>_99_stages/
cp status_template.json status_<N>.json
```

Edit `status_<N>.json` to set initial state:
```json
{
  "layer_id": "layer_<N>_project_<name>",
  "current_stage": "<N>.01_instructions",
  "stages": {
    "<N>.01_instructions": { "state": "not_started" },
    "<N>.02_planning": { "state": "not_started" },
    ...
  }
}
```

- [ ] Copied status template
- [ ] Renamed to `status_<N>.json`
- [ ] Updated `layer_id` field
- [ ] Set `current_stage`

<!-- section_id: "79d357fa-c850-4ef1-b78c-7937d51b331c" -->
### 6. Create Project README

Create `README.md` at project root:

```markdown
# <Project Name>

## Overview
<Brief description>

## Structure
- `layer_<N>/` - Project internals (sub_layers, stages)
- `layer_<N+1>/` - Nested content (sub-projects, features, components)

## Current Stage
See `layer_<N>/layer_<N>_99_stages/status_<N>.json`

## Quick Start
1. Read `layer_<N>/layer_<N>_02_sub_layers/sub_layer_<N>.01_basic_prompts/`
2. Check current stage in status file
3. Navigate to active stage folder
```

- [ ] Created project README.md

<!-- section_id: "183fc882-a2e2-4415-8833-2fcfa7131701" -->
### 7. Populate Basic Prompts (sub_layer_N.01)

Create `project_init_prompt.md` in `layer_<N>/layer_<N>_02_sub_layers/sub_layer_<N>.01_basic_prompts/`:

```markdown
# <Project Name> - Project Init Prompt

## Project Overview
<Description>

## Key Directories
- `layer_<N>/layer_<N>_02_sub_layers/` - Project context
- `layer_<N>/layer_<N>_99_stages/` - Workflow stages
- `layer_<N+1>/layer_<N+1>_features/` - Features

## Current Focus
<What we're working on>

## Important Context
<Key information for agents>
```

- [ ] Created project_init_prompt.md
- [ ] Added project overview
- [ ] Listed key directories
- [ ] Documented current focus

<!-- section_id: "7ee0135c-e3e3-47cd-a404-9dd5a8b04dd4" -->
### 8. Git Submodule Setup (if applicable)

If this project will be a submodule of a parent:

```bash
# From parent directory
git submodule add <remote_url> <path_to_project>
git commit -m "Add <project_name> as submodule"
```

- [ ] Added as submodule (if needed)
- [ ] Updated parent's .gitmodules

<!-- section_id: "750d7a3b-d714-47a1-99e7-72704579e23e" -->
### 9. Initial Commit

```bash
git add -A
git commit -m "Initialize <project_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

<!-- section_id: "42f3e371-8d99-4c37-b120-aef504bb1809" -->
## Post-Creation Verification

- [ ] `layer_<N>/` folder exists with correct structure
- [ ] `layer_<N+1>/` folder exists with three nested folders
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Project README exists
- [ ] Basic prompts sub_layer has content
- [ ] Git is initialized and committed

---

<!-- section_id: "5a12f6e5-8d61-4783-8ea1-d39638822e18" -->
## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer numbers in folder names | Use find/sed to bulk rename |
| Missing nested content folders | Create all three (sub-projects, features, components) |
| Empty sub_layers | At minimum, populate sub_layer_N.01 with project_init_prompt.md |
| Forgot status file | Copy from template and customize |

---

<!-- section_id: "3161bd84-3cc0-4145-9c21-6d848f912fc4" -->
## Related

- `instantiation_guide.md` - General instantiation guide
- `../changes/restructuring_migration_protocol.md` - If restructuring later
