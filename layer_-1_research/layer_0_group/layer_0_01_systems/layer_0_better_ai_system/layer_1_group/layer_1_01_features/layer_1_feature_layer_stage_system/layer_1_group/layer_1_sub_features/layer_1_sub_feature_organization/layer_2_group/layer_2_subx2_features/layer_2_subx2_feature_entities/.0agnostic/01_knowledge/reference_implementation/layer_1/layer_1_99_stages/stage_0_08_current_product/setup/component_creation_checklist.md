---
resource_id: "e66acf96-8494-4cc2-8f37-166d2b5f44d2"
resource_type: "knowledge"
resource_name: "component_creation_checklist"
---
# Component & Sub-Component Creation Checklist

**Purpose:** Detailed checklist for creating components and sub-components.

**Last Updated:** 2026-01-15

---

<!-- section_id: "895ec12e-873e-4fd4-8dce-fef60815677c" -->
## Pre-Creation

- [ ] Determine component name (use lowercase with hyphens or underscores)
- [ ] Identify parent entity (feature or component)
- [ ] Determine if this is a component or sub-component:
  - **Component:** Implementation unit inside a feature → `layer_N+1_component_<name>`
  - **Sub-component:** Component inside another component → `layer_N+1_sub_component_<name>`
- [ ] Calculate correct layer number (parent's layer + 1)

---

<!-- section_id: "cc0d9676-7d7d-4e7e-8900-88c98da0518e" -->
## Creation Steps

<!-- section_id: "e48a1df7-a0c1-4de5-9365-3dacc9985308" -->
### 1. Navigate to Parent's Components Folder

For **component** (inside a feature):
```bash
cd <feature>/layer_<N+1>/layer_<N+1>_components/
```

For **sub-component** (inside a component):
```bash
cd <parent_component>/layer_<N+1>/layer_<N+1>_sub_components/
```

- [ ] Navigated to correct parent folder

<!-- section_id: "ec5d0e73-15da-4aae-b23f-f584846e2084" -->
### 2. Copy Template

```bash
# Same template used for both components and sub-components
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_component_<name>/
# Or for sub-component:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_sub_component_<name>/
```

- [ ] Copied component template

<!-- section_id: "463421a2-30d3-4ccf-992f-fc893da9ff89" -->
### 3. Rename Layer Folders

Replace template `layer_N` with actual layer number:

```bash
cd layer_<N+1>_component_<name>/  # Or sub_component

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

<!-- section_id: "c7c1e11d-7d39-4055-bcd1-119e8a60bbaf" -->
### 4. Create Nested Content Folder

```bash
cd layer_<N+2>
mkdir -p layer_<N+2>_sub_components

# Add README
echo "# Sub-Components\n\nNested components go here." > layer_<N+2>_sub_components/README.md
```

**Note:** Components ONLY have `sub_components/` - no features or projects.

- [ ] Created `layer_<N+2>_sub_components/`
- [ ] Added README.md

<!-- section_id: "3d36b984-e7b9-4bd9-973e-85cde04bcf23" -->
### 5. Initialize Status File

```bash
cd layer_<N+1>/layer_<N+1>_99_stages/
cp status_template.json status_<N+1>.json
```

Edit `status_<N+1>.json`:
```json
{
  "layer_id": "layer_<N+1>_component_<name>",
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

<!-- section_id: "32222392-7ff3-4b73-a4e2-90b5df809304" -->
### 6. Create Component README

Create `README.md` at component root:

```markdown
# <Component Name>

## Overview
<Brief description of what this component implements>

## Structure
- `layer_<N+1>/` - Component internals (sub_layers, stages)
- `layer_<N+2>/` - Nested content (sub-components only)

## Current Stage
See `layer_<N+1>/layer_<N+1>_99_stages/status_<N+1>.json`

## Implementation Details
- (Key implementation notes)

## Dependencies
- (External dependencies)
- (Internal dependencies on other components)
```

- [ ] Created component README.md

<!-- section_id: "1edc7bc6-c134-4961-a6e8-e4ec4f467a75" -->
### 7. Populate Basic Prompts (sub_layer_N+1.01)

Create `component_init_prompt.md` in `layer_<N+1>/layer_<N+1>_02_sub_layers/sub_layer_<N+1>.01_basic_prompts/`:

```markdown
# <Component Name> - Component Init Prompt

## Component Overview
<Description of what this component does>

## Key Files
- (List main implementation files)

## Key Directories
- `layer_<N+1>/layer_<N+1>_02_sub_layers/` - Component context
- `layer_<N+1>/layer_<N+1>_99_stages/` - Workflow stages

## Current Focus
<What we're working on>

## Technical Notes
<Implementation details, gotchas, etc.>
```

- [ ] Created component_init_prompt.md
- [ ] Added component overview
- [ ] Listed key files/directories
- [ ] Documented current focus

<!-- section_id: "3a8ed5c1-bf45-4659-a567-47376959439b" -->
### 8. Initial Commit (if separate repo)

```bash
git add -A
git commit -m "Initialize <component_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

<!-- section_id: "03c50ce3-d783-4b32-a688-413ba2305309" -->
## Post-Creation Verification

- [ ] `layer_<N+1>/` folder exists with correct structure
- [ ] `layer_<N+2>/` folder exists with sub_components/
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Component README exists
- [ ] Basic prompts sub_layer has content

---

<!-- section_id: "7dcc2ae8-8425-4f3d-be6d-51ff84e5e4a3" -->
## Component vs Sub-Component Decision

| Question | Answer |
|----------|--------|
| Is parent a feature? | → **Component** (use `layer_N+1_component_<name>`) |
| Is parent a component? | → **Sub-component** (use `layer_N+1_sub_component_<name>`) |

**The "sub" prefix is ONLY for same-type nesting:**
- Feature containing component → `component` (no sub)
- Component containing component → `sub_component`

---

<!-- section_id: "b334c943-41ad-4408-a40e-7226ebc9d3ea" -->
## Layer Number Calculation

| Parent Type | Parent Layer | Component Layer | Component's Nested Content |
|-------------|--------------|-----------------|---------------------------|
| Feature at L2 | 2 | 3 | 4 |
| Feature at L3 | 3 | 4 | 5 |
| Component at L3 | 3 | 4 | 5 |
| Sub-component at L4 | 4 | 5 | 6 |

**Formula:** Component layer = Parent layer + 1

---

<!-- section_id: "fa5c6252-d6f3-441b-872c-c657bc6e6309" -->
## Component Types

Components are implementation units. Common types include:

| Type | Example | Description |
|------|---------|-------------|
| UI Component | `login_form` | User interface element |
| Service | `auth_service` | Backend service |
| Module | `data_parser` | Standalone module |
| Test Suite | `integration_tests` | Testing collection |
| Document | `user_guide` | Documentation artifact |
| Assignment | `homework_1` | Academic work item |

---

<!-- section_id: "fb383427-bc00-4eec-b5dc-fd2f5fbb5c65" -->
## Minimal vs Full Structure

<!-- section_id: "3f1fd8c3-f5fc-4e32-a1c7-910d7fe62d9a" -->
### Minimal Component (for small items)

```
layer_N+1_component_<name>/
├── README.md
├── layer_<N+1>/
│   ├── layer_<N+1>_02_sub_layers/
│   │   └── sub_layer_<N+1>.01_basic_prompts/
│   │       └── component_init_prompt.md
│   └── layer_<N+1>_99_stages/
│       └── status_<N+1>.json
└── layer_<N+2>/
    └── layer_<N+2>_sub_components/
        └── README.md
```

<!-- section_id: "0d7c15a5-9f29-4c42-8aad-a5faca17c38a" -->
### Full Component (for complex items)

Includes all standard sub_layers and stages.

---

<!-- section_id: "913f1380-d1e4-4a25-854d-f92ed6b60974" -->
## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer number | Check parent's layer, add 1 |
| Used "sub_component" for component in feature | Remove "sub_" prefix |
| Created features folder in component | Remove it - components only have sub-components |
| Overly deep nesting | Consider if sub-component is really needed |

---

<!-- section_id: "34f337e3-e5db-48b0-952f-f03c4d813bff" -->
## Related

- `instantiation_guide.md` - General instantiation guide
- `project_creation_checklist.md` - For creating projects
- `feature_creation_checklist.md` - For creating features
