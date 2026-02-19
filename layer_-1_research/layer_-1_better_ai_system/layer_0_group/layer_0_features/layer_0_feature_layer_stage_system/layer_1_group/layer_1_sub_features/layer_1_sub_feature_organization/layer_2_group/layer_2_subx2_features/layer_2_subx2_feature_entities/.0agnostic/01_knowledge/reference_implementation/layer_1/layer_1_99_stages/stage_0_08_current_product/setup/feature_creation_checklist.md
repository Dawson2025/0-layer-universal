# Feature & Sub-Feature Creation Checklist

**Purpose:** Detailed checklist for creating features and sub-features.

**Last Updated:** 2026-01-15

---

## Pre-Creation

- [ ] Determine feature name (use lowercase with hyphens or underscores)
- [ ] Identify parent entity (project or feature)
- [ ] Determine if this is a feature or sub-feature:
  - **Feature:** Capability inside a project → `layer_N+1_feature_<name>`
  - **Sub-feature:** Feature inside another feature → `layer_N+1_sub_feature_<name>`
- [ ] Calculate correct layer number (parent's layer + 1)

---

## Creation Steps

### 1. Navigate to Parent's Features Folder

For **feature** (inside a project):
```bash
cd <project>/layer_<N+1>/layer_<N+1>_features/
```

For **sub-feature** (inside a feature):
```bash
cd <parent_feature>/layer_<N+1>/layer_<N+1>_sub_features/
```

- [ ] Navigated to correct parent folder

### 2. Copy Template

```bash
# Same template used for both features and sub-features
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/ layer_<N+1>_feature_<name>/
# Or for sub-feature:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/2_feature_template/ layer_<N+1>_sub_feature_<name>/
```

- [ ] Copied feature template

### 3. Rename Layer Folders

Replace template `layer_N` with actual layer number:

```bash
cd layer_<N+1>_feature_<name>/  # Or sub_feature

# Rename grouping folders
mv layer_N layer_<N+1>
mv layer_N+1 layer_<N+2>

# Rename internal folders
cd layer_<N+1>
mv layer_N_00_ai_manager_system layer_<N+1>_00_ai_manager_system
mv layer_N_01_manager_handoff_documents layer_<N+1>_01_manager_handoff_documents
mv layer_N_02_sub_layers layer_<N+1>_02_sub_layers
mv layer_N_99_stages layer_<N+1>_99_stages

# Rename handoff subfolders
cd layer_<N+1>_01_manager_handoff_documents
mv layer_N_00_to_universal layer_<N+1>_00_to_universal
mv layer_N_01_to_specific layer_<N+1>_01_to_specific

# Rename sub_layers
cd ../layer_<N+1>_02_sub_layers
for d in sub_layer_N.*; do
  mv "$d" "${d/sub_layer_N./sub_layer_<N+1>.}"
done

# Rename stages
cd ../layer_<N+1>_99_stages
for d in stage_N.*; do
  mv "$d" "${d/stage_N./stage_<N+1>.}"
done
```

- [ ] Renamed `layer_N/` to `layer_<actual>/`
- [ ] Renamed `layer_N+1/` to `layer_<actual+1>/`
- [ ] Renamed all `layer_N_*` folders to `layer_<actual>_*`
- [ ] Renamed all `sub_layer_N.*` to `sub_layer_<actual>.*`
- [ ] Renamed all `stage_N.*` to `stage_<actual>.*`
- [ ] Renamed handoff subfolders

### 4. Create Nested Content Folders

```bash
cd layer_<N+2>
mkdir -p layer_<N+2>_sub_features
mkdir -p layer_<N+2>_components

# Add README to each
echo "# Sub-Features\n\nNested features go here." > layer_<N+2>_sub_features/README.md
echo "# Components\n\nComponents go here." > layer_<N+2>_components/README.md
```

**Note:** Features do NOT have `sub*X_projects/` - only projects can contain projects.

- [ ] Created `layer_<N+2>_sub_features/`
- [ ] Created `layer_<N+2>_components/`
- [ ] Added README.md to each

### 5. Initialize Status File

```bash
cd layer_<N+1>/layer_<N+1>_99_stages/
cp status_template.json status_<N+1>.json
```

Edit `status_<N+1>.json`:
```json
{
  "layer_id": "layer_<N+1>_feature_<name>",
  "current_stage": "<N+1>.01_instructions",
  "stages": {
    "<N+1>.01_instructions": { "state": "not_started" },
    "<N+1>.02_planning": { "state": "not_started" },
    ...
  }
}
```

- [ ] Copied status template
- [ ] Renamed to `status_<N+1>.json`
- [ ] Updated `layer_id` field
- [ ] Set `current_stage`

### 6. Create Feature README

Create `README.md` at feature root:

```markdown
# <Feature Name>

## Overview
<Brief description of what this feature does>

## Structure
- `layer_<N+1>/` - Feature internals (sub_layers, stages)
- `layer_<N+2>/` - Nested content (sub-features, components)

## Current Stage
See `layer_<N+1>/layer_<N+1>_99_stages/status_<N+1>.json`

## Components
- (List main components this feature contains)

## Dependencies
- (List other features this depends on)
```

- [ ] Created feature README.md

### 7. Populate Basic Prompts (sub_layer_N+1.01)

Create `feature_init_prompt.md` in `layer_<N+1>/layer_<N+1>_02_sub_layers/sub_layer_<N+1>.01_basic_prompts/`:

```markdown
# <Feature Name> - Feature Init Prompt

## Feature Overview
<Description>

## Key Directories
- `layer_<N+1>/layer_<N+1>_02_sub_layers/` - Feature context
- `layer_<N+1>/layer_<N+1>_99_stages/` - Workflow stages
- `layer_<N+2>/layer_<N+2>_components/` - Components

## Current Focus
<What we're working on>

## Important Context
<Key information for agents>
```

- [ ] Created feature_init_prompt.md
- [ ] Added feature overview
- [ ] Listed key directories
- [ ] Documented current focus

### 8. Initial Commit (if separate repo)

```bash
git add -A
git commit -m "Initialize <feature_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

## Post-Creation Verification

- [ ] `layer_<N+1>/` folder exists with correct structure
- [ ] `layer_<N+2>/` folder exists with sub_features/ and components/
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Feature README exists
- [ ] Basic prompts sub_layer has content

---

## Feature vs Sub-Feature Decision

| Question | Answer |
|----------|--------|
| Is parent a project? | → **Feature** (use `layer_N+1_feature_<name>`) |
| Is parent a feature? | → **Sub-feature** (use `layer_N+1_sub_feature_<name>`) |

**The "sub" prefix is ONLY for same-type nesting:**
- Project containing feature → `feature` (no sub)
- Feature containing feature → `sub_feature`

---

## Layer Number Calculation

| Parent Type | Parent Layer | Feature Layer | Feature's Nested Content |
|-------------|--------------|---------------|--------------------------|
| Project at L1 | 1 | 2 | 3 |
| Sub-project at L2 | 2 | 3 | 4 |
| Feature at L2 | 2 | 3 | 4 |
| Sub-feature at L3 | 3 | 4 | 5 |

**Formula:** Feature layer = Parent layer + 1

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer number | Check parent's layer, add 1 |
| Used "sub_feature" for feature in project | Remove "sub_" prefix |
| Missing components folder | Features always have components/ |
| Created sub*X_projects in feature | Remove it - only projects have sub-projects |

---

## Related

- `instantiation_guide.md` - General instantiation guide
- `project_creation_checklist.md` - For creating projects
- `component_creation_checklist.md` - For creating components
