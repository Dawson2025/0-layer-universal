---
resource_id: "abcc7eda-cd89-48a0-9375-dc03805bcf3b"
resource_type: "document"
resource_name: "project_creation_checklist"
---
# Project Creation Checklist

**Purpose:** Detailed checklist for creating a new project from scratch.

**Last Updated:** 2026-01-15

---

<!-- section_id: "80580c0d-7f22-4158-9a48-dc59c4faaa27" -->
## Pre-Creation

- [ ] Determine project name (use lowercase with hyphens or underscores)
- [ ] Determine if this is a top-level project or sub-project
- [ ] If sub-project, identify parent and nesting level (subx1, subx2, etc.)
- [ ] Decide if project will be a git submodule or part of parent repo

---

<!-- section_id: "e7217e4f-34f6-45da-b484-5aded6239446" -->
## Creation Steps

<!-- section_id: "4df516d9-9fb0-460c-b254-a59979d648ff" -->
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

<!-- section_id: "ff936d46-fa55-4565-bd0d-7ffeddf400bd" -->
### 2. Copy Template

```bash
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/1_project_template/* .
# Or for sub-project:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_sub_project_template/* .
```

- [ ] Copied appropriate template

<!-- section_id: "e79dc8ad-f635-41d0-999f-5c45d4f4a57e" -->
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

<!-- section_id: "c81deb72-ae21-4661-8364-3b24cb0d6747" -->
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

<!-- section_id: "7d18f223-db8a-4286-9757-0e7591567170" -->
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

<!-- section_id: "eed76da5-b6af-4b90-b181-1d5410090519" -->
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

<!-- section_id: "93161c8f-cdcc-4cfc-b7ad-d1549395fd3a" -->
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

<!-- section_id: "de0e1c7d-5ec7-432b-b03f-356a46b1e638" -->
### 8. Git Submodule Setup (if applicable)

If this project will be a submodule of a parent:

```bash
# From parent directory
git submodule add <remote_url> <path_to_project>
git commit -m "Add <project_name> as submodule"
```

- [ ] Added as submodule (if needed)
- [ ] Updated parent's .gitmodules

<!-- section_id: "ec055795-234d-48be-88e3-8b72048435e4" -->
### 9. Initial Commit

```bash
git add -A
git commit -m "Initialize <project_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

<!-- section_id: "542dcb0a-b196-4fdd-8c72-1856f32dd423" -->
## Post-Creation Verification

- [ ] `layer_<N>/` folder exists with correct structure
- [ ] `layer_<N+1>/` folder exists with three nested folders
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Project README exists
- [ ] Basic prompts sub_layer has content
- [ ] Git is initialized and committed

---

<!-- section_id: "00af82de-98f6-4a4b-be6c-5c01af40cc7b" -->
## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer numbers in folder names | Use find/sed to bulk rename |
| Missing nested content folders | Create all three (sub-projects, features, components) |
| Empty sub_layers | At minimum, populate sub_layer_N.01 with project_init_prompt.md |
| Forgot status file | Copy from template and customize |

---

<!-- section_id: "f320a3fd-8a37-4764-99fb-d64809e683bf" -->
## Related

- `instantiation_guide.md` - General instantiation guide
- `../changes/restructuring_migration_protocol.md` - If restructuring later
