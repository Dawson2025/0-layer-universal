---
resource_id: "e66acf96-8494-4cc2-8f37-166d2b5f44d2"
resource_type: "knowledge"
resource_name: "component_creation_checklist"
---
# Component & Sub-Component Creation Checklist

**Purpose:** Detailed checklist for creating components and sub-components.

**Last Updated:** 2026-01-15

---

## Pre-Creation

- [ ] Determine component name (use lowercase with hyphens or underscores)
- [ ] Identify parent entity (feature or component)
- [ ] Determine if this is a component or sub-component:
  - **Component:** Implementation unit inside a feature → `layer_N+1_component_<name>`
  - **Sub-component:** Component inside another component → `layer_N+1_sub_component_<name>`
- [ ] Calculate correct layer number (parent's layer + 1)

---

## Creation Steps

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

### 2. Copy Template

```bash
# Same template used for both components and sub-components
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_component_<name>/
# Or for sub-component:
cp -r <path_to>/layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers/3_component_template/ layer_<N+1>_sub_component_<name>/
```

- [ ] Copied component template

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

### 8. Initial Commit (if separate repo)

```bash
git add -A
git commit -m "Initialize <component_name> with layer/stage structure

Co-Authored-By: Claude <noreply@anthropic.com>"
```

- [ ] Staged all files
- [ ] Created initial commit

---

## Post-Creation Verification

- [ ] `layer_<N+1>/` folder exists with correct structure
- [ ] `layer_<N+2>/` folder exists with sub_components/
- [ ] All folder names use correct layer number
- [ ] Status file is initialized
- [ ] Component README exists
- [ ] Basic prompts sub_layer has content

---

## Component vs Sub-Component Decision

| Question | Answer |
|----------|--------|
| Is parent a feature? | → **Component** (use `layer_N+1_component_<name>`) |
| Is parent a component? | → **Sub-component** (use `layer_N+1_sub_component_<name>`) |

**The "sub" prefix is ONLY for same-type nesting:**
- Feature containing component → `component` (no sub)
- Component containing component → `sub_component`

---

## Layer Number Calculation

| Parent Type | Parent Layer | Component Layer | Component's Nested Content |
|-------------|--------------|-----------------|---------------------------|
| Feature at L2 | 2 | 3 | 4 |
| Feature at L3 | 3 | 4 | 5 |
| Component at L3 | 3 | 4 | 5 |
| Sub-component at L4 | 4 | 5 | 6 |

**Formula:** Component layer = Parent layer + 1

---

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

## Minimal vs Full Structure

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

### Full Component (for complex items)

Includes all standard sub_layers and stages.

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong layer number | Check parent's layer, add 1 |
| Used "sub_component" for component in feature | Remove "sub_" prefix |
| Created features folder in component | Remove it - components only have sub-components |
| Overly deep nesting | Consider if sub-component is really needed |

---

## Related

- `instantiation_guide.md` - General instantiation guide
- `project_creation_checklist.md` - For creating projects
- `feature_creation_checklist.md` - For creating features
