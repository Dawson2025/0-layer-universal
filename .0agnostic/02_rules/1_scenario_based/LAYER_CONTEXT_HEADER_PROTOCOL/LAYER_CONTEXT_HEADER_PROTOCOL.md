---
resource_id: "1105f04d-ece0-4237-a824-0e2a41c93a73"
resource_type: "rule"
resource_name: "LAYER_CONTEXT_HEADER_PROTOCOL"
---
# Layer Context Header Protocol

<!-- section_id: "e8a7cffc-7960-46e9-ba67-6be5e4ac3867" -->
## Overview

Every file within the layer system MUST include a standardized header that references the initialization prompts for all layers from L0 up to the file's current layer. This ensures every file has explicit access to its full contextual inheritance chain.

<!-- section_id: "323235ca-a682-4a1a-81a3-4ff1dc252671" -->
## Purpose

- **Context Inheritance**: Make layer cascade visible in every file
- **Dynamic References**: Allow init prompt files to be renamed/moved without breaking references
- **Self-Documentation**: Every file declares its layer and inherited context
- **Navigation**: Provide quick links to relevant layer documentation

<!-- section_id: "433e8a07-b975-4376-acc5-8a9d6da37c44" -->
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

<!-- section_id: "a34681d5-82c9-4c95-ba7b-f9d11a1defc4" -->
## Init Prompt Naming Convention

Each layer MUST maintain its init prompt at a standard location:

- **L0 (Universal)**: `layer_0/0.02_sub_layers/sub_layer_0_01_basic_prompts_throughout/universal_init_prompt.md`
- **L1 (Project)**: `layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md`
- **L2 (Feature)**: `layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md`
- **L3 (Component)**: `layer_3_components/3.02_sub_layers/sub_layer_3.01_basic_prompts/component_init_prompt.md`
- **L4+ (Sub-component)**: `layer_N_*/N.02_sub_layers/sub_layer_N.01_basic_prompts/layer_N_init_prompt.md`

<!-- section_id: "01c40c1c-dea3-4e0c-b9f3-a2d2de4ea6b1" -->
## Dynamic Path Resolution

Paths in headers are **relative to the file's location**. This ensures headers remain valid even if:
- Init prompt files are renamed (as long as naming convention is followed)
- Directory structure is refactored
- Repository is moved or cloned

<!-- section_id: "a2be6420-3c1f-4191-bd6f-1c1603a72f8a" -->
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

<!-- section_id: "487c8507-7f6e-4c85-a045-0864ccbb46b3" -->
## Language-Specific Format

<!-- section_id: "cf391132-a3ed-4a0c-a853-fff36ebdd3a1" -->
### Markdown Files
```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- ... -->
<!-- END LAYER CONTEXT HEADER -->
```

<!-- section_id: "5340748d-76c9-472a-9dc7-3398331a9fb6" -->
### TypeScript/JavaScript Files
```typescript
/**
 * LAYER CONTEXT HEADER
 * ...
 * END LAYER CONTEXT HEADER
 */
```

<!-- section_id: "d0da6ae8-459a-45c1-a16a-1411f98320f1" -->
### Python Files
```python
"""
LAYER CONTEXT HEADER
...
END LAYER CONTEXT HEADER
"""
```

<!-- section_id: "7ef82718-7dae-41b7-852c-2efa06f7ada2" -->
### Shell Scripts
```bash
# LAYER CONTEXT HEADER
# ...
# END LAYER CONTEXT HEADER
```

<!-- section_id: "34d9b8cf-2901-49d1-8977-d45c61bd4569" -->
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

<!-- section_id: "df2e4ac0-0ad1-4fce-9285-b025e561d3cb" -->
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

<!-- section_id: "343755aa-9ef5-4632-baa9-688477c1c732" -->
## Migration Strategy

For existing files without headers:

1. **Phase 1**: Add headers to all template files in `layer_1/layer_1_features/layer_1_feature_layer_stage_system/layer_1/layer_1_02_sub_layers`
2. **Phase 2**: Add headers to all `README.md` files across all layers
3. **Phase 3**: Add headers to all `.md` documentation files
4. **Phase 4**: Add headers to all source code files (`.ts`, `.py`, `.sh`, etc.)
5. **Phase 5**: Add headers to configuration files (`.json`, `.yaml`, etc.) where appropriate

<!-- section_id: "0c0b16b4-6843-4ab9-937a-b8073ec6a619" -->
## Enforcement

- **Template Files**: All templates MUST include headers
- **New Files**: All new files MUST include headers
- **Existing Files**: Headers SHOULD be added during next significant edit
- **CI/CD**: Consider adding validation check to ensure headers exist

<!-- section_id: "5fdc97c5-c5b8-47d1-9793-5de1074bc3c8" -->
## Benefits

1. **Self-Documenting**: Every file declares its layer context
2. **Navigation**: Quick access to relevant init prompts
3. **Maintenance**: Relative paths remain valid across refactors
4. **Onboarding**: New developers/agents can immediately see context hierarchy
5. **Debugging**: Clear layer boundaries help identify constraint violations

<!-- section_id: "d9847ac9-a7e3-4f31-8724-109ceb4542d1" -->
## Examples in Practice

<!-- section_id: "113655ee-5175-4181-a8ba-ae3acd9f22b6" -->
### Scenario 1: Agent Reading a Feature File

An agent reading `layer_2_features/2.02_sub_layers/sub_layer_2.03_feature_knowledge/auth_system.md` can:

1. See it's a Layer 2 file via header
2. Follow links to read L0 universal init, L1 project init, and L2 feature init
3. Understand full constraint cascade without searching

<!-- section_id: "532252c6-e2ea-4db3-8536-b2bf1be41b81" -->
### Scenario 2: Refactoring Layer Structure

If the project renames `project_init_prompt.md` to `project_context.md`:

1. Update the naming convention documentation in this protocol
2. Rename the file
3. All relative paths still work because they point to the standard location

<!-- section_id: "fb20abd0-9ff9-42c9-931b-e970c753f223" -->
### Scenario 3: Adding a New Layer

When adding L4 (sub-component) layers:

1. Create `layer_4_subcomponents/4.02_sub_layers/sub_layer_4.01_basic_prompts/subcomponent_init_prompt.md`
2. Update this protocol with L4 naming convention
3. Add L4 reference to all L4 file headers

<!-- section_id: "c5da3b6a-c484-4392-a31d-115ac8201020" -->
## Related Protocols

- `MASTER_DOCUMENTATION_INDEX.md` - Overall documentation organization
- `SYSTEM_OVERVIEW.md` - Layer + Stage framework overview
- [AI Manager Hierarchy System](../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md) - Architectural foundation

<!-- section_id: "c72e385d-d218-4917-98da-b17f1e8dfd42" -->
## Version History

- **1.0.0** (2025-01-15): Initial protocol definition
