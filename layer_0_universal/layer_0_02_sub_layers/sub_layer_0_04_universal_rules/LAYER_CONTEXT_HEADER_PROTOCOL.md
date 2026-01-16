# Layer Context Header Protocol

## Overview

Every file within the layer system MUST include a standardized header that references the initialization prompts for all layers from L0 up to the file's current layer. This ensures every file has explicit access to its full contextual inheritance chain.

## Purpose

- **Context Inheritance**: Make layer cascade visible in every file
- **Dynamic References**: Allow init prompt files to be renamed/moved without breaking references
- **Self-Documentation**: Every file declares its layer and inherited context
- **Navigation**: Provide quick links to relevant layer documentation

## Standard Header Format

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer N File: [Brief Description] -->
<!-- Context Cascade (L0 → L{N}): -->
<!-- - L0 Universal Init: ../../../layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- - L1 Project Init: ../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md (if exists) -->
<!-- - L2 Feature Init: ../layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md (if exists) -->
<!-- - L3 Component Init: ./layer_3_components/3.02_sub_layers/sub_layer_3.01_basic_prompts/component_init_prompt.md (if exists) -->
<!-- END LAYER CONTEXT HEADER -->
```

## Init Prompt Naming Convention

Each layer MUST maintain its init prompt at a standard location:

- **L0 (Universal)**: `layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md`
- **L1 (Project)**: `layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md`
- **L2 (Feature)**: `layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md`
- **L3 (Component)**: `layer_3_components/3.02_sub_layers/sub_layer_3.01_basic_prompts/component_init_prompt.md`
- **L4+ (Sub-component)**: `layer_N_*/N.02_sub_layers/sub_layer_N.01_basic_prompts/layer_N_init_prompt.md`

## Dynamic Path Resolution

Paths in headers are **relative to the file's location**. This ensures headers remain valid even if:
- Init prompt files are renamed (as long as naming convention is followed)
- Directory structure is refactored
- Repository is moved or cloned

### Path Calculation Examples

**Example 1**: File at `layer_2_features/2.02_sub_layers/sub_layer_2.03_feature_knowledge/README.md`

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer 2 File: Feature Knowledge README -->
<!-- Context Cascade (L0 → L2): -->
<!-- - L0 Universal Init: ../../../layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- - L1 Project Init: ../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md -->
<!-- - L2 Feature Init: ../sub_layer_2.01_basic_prompts/feature_init_prompt.md -->
<!-- END LAYER CONTEXT HEADER -->
```

**Example 2**: File at `layer_0_universal/0.02_sub_layers/sub_layer_0.11_universal_tools/TOOLS_INDEX.md`

```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- Layer 0 File: Universal Tools Index -->
<!-- Context Cascade (L0 only): -->
<!-- - L0 Universal Init: ../sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md -->
<!-- END LAYER CONTEXT HEADER -->
```

**Example 3**: File at `layer_3_components/3.02_sub_layers/sub_layer_3.05_component_implementation/LoginForm.tsx`

```typescript
/**
 * LAYER CONTEXT HEADER
 * Layer 3 File: LoginForm Component
 * Context Cascade (L0 → L3):
 * - L0 Universal Init: ../../../layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md
 * - L1 Project Init: ../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md
 * - L2 Feature Init: ../../../layer_2_features/2.02_sub_layers/sub_layer_2.01_basic_prompts/feature_init_prompt.md
 * - L3 Component Init: ../sub_layer_3.01_basic_prompts/component_init_prompt.md
 * END LAYER CONTEXT HEADER
 */

export const LoginForm = () => {
  // Component implementation
};
```

## Language-Specific Format

### Markdown Files
```markdown
<!-- LAYER CONTEXT HEADER -->
<!-- ... -->
<!-- END LAYER CONTEXT HEADER -->
```

### TypeScript/JavaScript Files
```typescript
/**
 * LAYER CONTEXT HEADER
 * ...
 * END LAYER CONTEXT HEADER
 */
```

### Python Files
```python
"""
LAYER CONTEXT HEADER
...
END LAYER CONTEXT HEADER
"""
```

### Shell Scripts
```bash
# LAYER CONTEXT HEADER
# ...
# END LAYER CONTEXT HEADER
```

### JSON Files
```json
{
  "_layerContext": {
    "layer": 2,
    "description": "Feature Configuration",
    "contextCascade": {
      "L0": "../../../layer_0_universal/0.02_sub_layers/sub_layer_0.01_basic_prompts_throughout/universal_init_prompt.md",
      "L1": "../../../layer_1_project/1.02_sub_layers/sub_layer_1.01_basic_prompts/project_init_prompt.md",
      "L2": "../sub_layer_2.01_basic_prompts/feature_init_prompt.md"
    }
  }
}
```

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

## Migration Strategy

For existing files without headers:

1. **Phase 1**: Add headers to all template files in `0.01_layer_stage_framework`
2. **Phase 2**: Add headers to all `README.md` files across all layers
3. **Phase 3**: Add headers to all `.md` documentation files
4. **Phase 4**: Add headers to all source code files (`.ts`, `.py`, `.sh`, etc.)
5. **Phase 5**: Add headers to configuration files (`.json`, `.yaml`, etc.) where appropriate

## Enforcement

- **Template Files**: All templates MUST include headers
- **New Files**: All new files MUST include headers
- **Existing Files**: Headers SHOULD be added during next significant edit
- **CI/CD**: Consider adding validation check to ensure headers exist

## Benefits

1. **Self-Documenting**: Every file declares its layer context
2. **Navigation**: Quick access to relevant init prompts
3. **Maintenance**: Relative paths remain valid across refactors
4. **Onboarding**: New developers/agents can immediately see context hierarchy
5. **Debugging**: Clear layer boundaries help identify constraint violations

## Examples in Practice

### Scenario 1: Agent Reading a Feature File

An agent reading `layer_2_features/2.02_sub_layers/sub_layer_2.03_feature_knowledge/auth_system.md` can:

1. See it's a Layer 2 file via header
2. Follow links to read L0 universal init, L1 project init, and L2 feature init
3. Understand full constraint cascade without searching

### Scenario 2: Refactoring Layer Structure

If the project renames `project_init_prompt.md` to `project_context.md`:

1. Update the naming convention documentation in this protocol
2. Rename the file
3. All relative paths still work because they point to the standard location

### Scenario 3: Adding a New Layer

When adding L4 (sub-component) layers:

1. Create `layer_4_subcomponents/4.02_sub_layers/sub_layer_4.01_basic_prompts/subcomponent_init_prompt.md`
2. Update this protocol with L4 naming convention
3. Add L4 reference to all L4 file headers

## Related Protocols

- `MASTER_DOCUMENTATION_INDEX.md` - Overall documentation organization
- `SYSTEM_OVERVIEW.md` - Layer + Stage framework overview
- [AI Manager Hierarchy System](../../../-1_research/-1.01_things_researched/ai_manager_hierarchy_system/overview/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md) - Architectural foundation

## Version History

- **1.0.0** (2025-01-15): Initial protocol definition
