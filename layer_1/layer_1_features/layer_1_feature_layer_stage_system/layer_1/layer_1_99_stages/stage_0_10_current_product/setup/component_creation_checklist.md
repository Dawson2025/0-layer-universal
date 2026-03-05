---
resource_id: "c7bc8a78-34b0-43ec-a2bd-6ba1218182f4"
resource_type: "document"
resource_name: "component_creation_checklist"
---
# Component & Sub-Component Creation Checklist

**Purpose:** Detailed checklist for creating components and sub-components.

**Last Updated:** 2026-01-15

---

<!-- section_id: "f27a77e1-d525-4d62-8bb8-14398ecfafa1" -->
## Pre-Creation

- [ ] Determine component name (use lowercase with hyphens or underscores)
- [ ] Identify parent entity (feature or component)
- [ ] Determine if this is a component or sub-component:
  - **Component:** Implementation unit inside a feature → `layer_N+1_component_<name>`
  - **Sub-component:** Component inside another component → `layer_N+1_sub_component_<name>`
- [ ] Calculate correct layer number (parent's layer + 1)

---

<!-- section_id: "e68a7794-5fcc-4cfa-baed-bc00d860695a" -->
## Creation Steps

<!-- section_id: "7207b497-0edb-4ae3-bdbc-9023e025ee34" -->
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

<!-- section_id: "27d2bd77-94f7-42da-b88a-cb3decb3e262" -->
### 2. Copy Template

```bash
# Same template used for both components and sub-components
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_component_<name>/
# Or for sub-component:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_sub_component_<name>/
```

- [ ] Copied component template

<!-- section_id: "568ea701-471a-417d-a199-9990e8b5986a" -->
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

<!-- section_id: "8c64fdb7-7dbc-464d-bb70-aff53e4b9838" -->
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

<!-- section_id: "e235bf4a-6860-4395-a1ff-9ece255a12f7" -->
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

<!-- section_id: "48c93272-aeab-4be3-92b1-d49d73cf7899" -->
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

<!-- section_id: "15a8af92-8ae7-4cb9-b865-6c2ef5c8f216" -->
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

<!-- section_id: "13420b07-0255-4c96-8a1f-85f21b7f3ce3" -->
### 8. Initial Commit (if separate repo)

```bash
git add -A
git commit -m "Initialize <component_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

<!-- section_id: "1916d63a-1c88-4f30-9aac-6a1599e5da8a" -->
## Post-Creation Verification

- [ ] `layer_<N+1>/` folder exists with correct structure
- [ ] `layer_<N+2>/` folder exists with sub_components/
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Component README exists
- [ ] Basic prompts sub_layer has content

---

<!-- section_id: "69bda243-2d77-4174-9399-a153b0c2a5c1" -->
## Component vs Sub-Component Decision

| Question | Answer |
|----------|--------|
| Is parent a feature? | → **Component** (use `layer_N+1_component_<name>`) |
| Is parent a component? | → **Sub-component** (use `layer_N+1_sub_component_<name>`) |

**The "sub" prefix is ONLY for same-type nesting:**
- Feature containing component → `component` (no sub)
- Component containing component → `sub_component`

---

<!-- section_id: "2d330ff6-e5d3-408f-9018-4a3634cbe4b3" -->
## Layer Number Calculation

| Parent Type | Parent Layer | Component Layer | Component's Nested Content |
|-------------|--------------|-----------------|---------------------------|
| Feature at L2 | 2 | 3 | 4 |
| Feature at L3 | 3 | 4 | 5 |
| Component at L3 | 3 | 4 | 5 |
| Sub-component at L4 | 4 | 5 | 6 |

**Formula:** Component layer = Parent layer + 1

---

<!-- section_id: "2fc8b01d-0740-4fc0-a1b3-b9341e531fd9" -->
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

<!-- section_id: "23e887eb-4e91-4271-bb97-0741b873aec9" -->
## Minimal vs Full Structure

<!-- section_id: "943e460d-b573-447c-8f6c-7bb5c1cf4fc3" -->
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

<!-- section_id: "988b03aa-1b43-4951-8ca5-048f289c808b" -->
### Full Component (for complex items)

Includes all standard sub_layers and stages.

---

<!-- section_id: "db685f7e-cc4a-467b-b072-d5e7500192f9" -->
## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer number | Check parent's layer, add 1 |
| Used "sub_component" for component in feature | Remove "sub_" prefix |
| Created features folder in component | Remove it - components only have sub-components |
| Overly deep nesting | Consider if sub-component is really needed |

---

<!-- section_id: "45652909-dd35-4091-8b2b-2e766cf594ef" -->
## Related

- `instantiation_guide.md` - General instantiation guide
- `project_creation_checklist.md` - For creating projects
- `feature_creation_checklist.md` - For creating features
