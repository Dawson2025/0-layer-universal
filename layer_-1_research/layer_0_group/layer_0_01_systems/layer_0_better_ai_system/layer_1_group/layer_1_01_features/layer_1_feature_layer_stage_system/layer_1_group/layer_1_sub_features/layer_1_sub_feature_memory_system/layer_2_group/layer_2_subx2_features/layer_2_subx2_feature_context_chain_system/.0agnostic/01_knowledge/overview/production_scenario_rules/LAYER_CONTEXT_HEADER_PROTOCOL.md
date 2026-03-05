---
resource_id: "08848442-96bf-4257-883c-1ec5d2ae7904"
resource_type: "knowledge"
resource_name: "LAYER_CONTEXT_HEADER_PROTOCOL"
---
# Layer Context Header Protocol

<!-- section_id: "61ad4b79-4100-4a73-9f7d-34377a816c1d" -->
## Overview

Every file within the layer system MUST include a standardized header that references the initialization prompts for all layers from L0 up to the file's current layer. This ensures every file has explicit access to its full contextual inheritance chain.

<!-- section_id: "7002a553-7f9b-495e-b0a3-77b85684d42b" -->
## Purpose

- **Context Inheritance**: Make layer cascade visible in every file
- **Dynamic References**: Allow init prompt files to be renamed/moved without breaking references
- **Self-Documentation**: Every file declares its layer and inherited context
- **Navigation**: Provide quick links to relevant layer documentation

<!-- section_id: "48bd4042-7c2e-48ab-8b86-4fddc5ff4472" -->
## Standard Header Format

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer N File: [Brief Description] -->
<!-- Context Cascade (L0 → L{N}): -->
<!-- - L0 Universal Init: ../../../layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- - L1 Project Init: ../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md (if exists) -->
<!-- - L2 Feature Init: ../layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md (if exists) -->
<!-- - L3 Component Init: ./layer_3_components/3.02_sub_layers/sub_layer_3.01_basic_prompts/component_init_prompt.md (if exists) -->
<!-- END LAYER CONTEXT HEADER -->
```

<!-- section_id: "51e99e01-7238-4faf-89cc-0acc90766fa4" -->
## Init Prompt Naming Convention

Each layer MUST maintain its init prompt at a standard location:

- **L0 (Universal)**: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md`
- **L1 (Project)**: `layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md`
- **L2 (Feature)**: `layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md`
- **L3 (Component)**: `layer_3_components/3.02_sub_layers/sub_layer_3.01_basic_prompts/component_init_prompt.md`
- **L4+ (Sub-component)**: `layer_N_*/N.02_sub_layers/sub_layer_N.01_basic_prompts/layer_N_init_prompt.md`

<!-- section_id: "1678209b-34ba-410e-86ba-0e47c35f90a4" -->
## Dynamic Path Resolution

Paths in headers are **relative to the file's location**. This ensures headers remain valid even if:
- Init prompt files are renamed (as long as naming convention is followed)
- Directory structure is refactored
- Repository is moved or cloned

<!-- section_id: "126451d5-b224-4b1c-940e-841f95cc09ce" -->
### Path Calculation Examples

**Example 1**: File at `layer_2_features/2.02_sub_layers/sub_layer_2.03_feature_knowledge/README.md`

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer 2 File: Feature Knowledge README -->
<!-- Context Cascade (L0 → L2): -->
<!-- - L0 Universal Init: ../../../layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- - L1 Project Init: ../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md -->
<!-- - L2 Feature Init: ../sub_layer_2.01_basic_prompts/feature_init_prompt.md -->
<!-- END LAYER CONTEXT HEADER -->
```

**Example 2**: File at `layer_0/0.02_sub_layers/sub_layer_0_11_universal_tools/TOOLS_INDEX.md`

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer 0 File: Universal Tools Index -->
<!-- Context Cascade (L0 only): -->
<!-- - L0 Universal Init: ../sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- END LAYER CONTEXT HEADER -->
```

**Example 3**: File at `layer_3_components/3.02_sub_layers/sub_layer_3.05_component_implementation/LoginForm.tsx`

```typescript
/**
 * LAYER CONTEXT HEADER
 * Layer 3 File: LoginForm Component
 * Context Cascade (L0 → L3):
 * - L0 Universal Init: ../../../layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md
 * - L1 Project Init: ../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md
 * - L2 Feature Init: ../../../layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md
 * - L3 Component Init: ../sub_layer_3.01_basic_prompts/component_init_prompt.md
 * END LAYER CONTEXT HEADER
 */

export const LoginForm = () => {
  // Component implementation
};
```

<!-- section_id: "244e7a38-7c09-4c1d-ad47-05c16408fc8b" -->
## Language-Specific Format

<!-- section_id: "f68384e0-2f42-4b70-947f-de8dcca927c8" -->
### Markdown Files
```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- ... -->
<!-- END LAYER CONTEXT HEADER -->
```

<!-- section_id: "bebd0bbb-1adc-4ec9-b16b-1e8422de841c" -->
### TypeScript/JavaScript Files
```typescript
/**
 * LAYER CONTEXT HEADER
 * ...
 * END LAYER CONTEXT HEADER
 */
```

<!-- section_id: "4a072389-bf67-41dd-9c62-6e159b6e3cab" -->
### Python Files
```python
"""
LAYER CONTEXT HEADER
...
END LAYER CONTEXT HEADER
"""
```

<!-- section_id: "f59be600-0a9c-43a9-87c5-a8003b9adeb2" -->
### Shell Scripts
```bash
# LAYER CONTEXT HEADER
# ...
# END LAYER CONTEXT HEADER
```

<!-- section_id: "28ecaf9c-8303-4ca1-b0f8-2d0d1713e7ca" -->
### JSON Files
```json
{
  "_layerContext": {
    "layer": 2,
    "description": "Feature Configuration",
    "contextCascade": {
      "L0": "../../../layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md",
      "L1": "../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md",
      "L2": "../sub_layer_2.01_basic_prompts/feature_init_prompt.md"
    }
  }
}
```

<!-- section_id: "750489f7-f42f-4d0e-9f40-ffe93c1b369c" -->
## Automated Header Generation

A helper script SHOULD be provided to automatically generate and update headers:

```bash
# Generate header for a file
generate-layer-header /path/to/file.md

# Update all headers in a directory tree
update-layer-headers /path/to/layer_2_features --recursive

# Validate all headers in repository
validate-layer-headers /path/to/0_context
```

<!-- section_id: "2622a556-7e80-43b5-a398-6df2b01dc98c" -->
## Migration Strategy

For existing files without headers:

1. **Phase 1**: Add headers to all template files in `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers`
2. **Phase 2**: Add headers to all `README.md` files across all layers
3. **Phase 3**: Add headers to all `.md` documentation files
4. **Phase 4**: Add headers to all source code files (`.ts`, `.py`, `.sh`, etc.)
5. **Phase 5**: Add headers to configuration files (`.json`, `.yaml`, etc.) where appropriate

<!-- section_id: "d5a8b7f7-5bdf-4229-852d-b98ca7dd7b53" -->
## Enforcement

- **Template Files**: All templates MUST include headers
- **New Files**: All new files MUST include headers
- **Existing Files**: Headers SHOULD be added during next significant edit
- **CI/CD**: Consider adding validation check to ensure headers exist

<!-- section_id: "d9be070f-ef9d-4bc7-aeaf-89eebc095736" -->
## Benefits

1. **Self-Documenting**: Every file declares its layer context
2. **Navigation**: Quick access to relevant init prompts
3. **Maintenance**: Relative paths remain valid across refactors
4. **Onboarding**: New developers/agents can immediately see context hierarchy
5. **Debugging**: Clear layer boundaries help identify constraint violations

<!-- section_id: "e9ea272d-e6e3-4db0-97c5-8ff2adace57c" -->
## Examples in Practice

<!-- section_id: "92084149-3a81-4cba-a68b-9857991987dc" -->
### Scenario 1: Agent Reading a Feature File

An agent reading `layer_2_features/2.02_sub_layers/sub_layer_2.03_feature_knowledge/auth_system.md` can:

1. See it's a Layer 2 file via header
2. Follow links to read L0 universal init, L1 project init, and L2 feature init
3. Understand full constraint cascade without searching

<!-- section_id: "afe2fc14-05b0-4c9f-8695-c7ac986ea54d" -->
### Scenario 2: Refactoring Layer Structure

If the project renames `project_init_prompt.md` to `project_context.md`:

1. Update the naming convention documentation in this protocol
2. Rename the file
3. All relative paths still work because they point to the standard location

<!-- section_id: "67bd7334-cbdf-4da2-acca-93c616c2405d" -->
### Scenario 3: Adding a New Layer

When adding L4 (sub-component) layers:

1. Create `layer_4_subcomponents/4.02_sub_layers/sub_layer_4.01_basic_prompts/subcomponent_init_prompt.md`
2. Update this protocol with L4 naming convention
3. Add L4 reference to all L4 file headers

<!-- section_id: "ef6cab41-be77-4179-8ba4-fa1783580114" -->
## Related Protocols

- `MASTER_DOCUMENTATION_INDEX.md` - Overall documentation organization
- `SYSTEM_OVERVIEW.md` - Layer + Stage framework overview
- [AI Manager Hierarchy System](../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md) - Architectural foundation

<!-- section_id: "b4f9347c-ce32-4e5a-8cf9-9f063da2f4fc" -->
## Version History

- **1.0.0** (2025-01-15): Initial protocol definition
