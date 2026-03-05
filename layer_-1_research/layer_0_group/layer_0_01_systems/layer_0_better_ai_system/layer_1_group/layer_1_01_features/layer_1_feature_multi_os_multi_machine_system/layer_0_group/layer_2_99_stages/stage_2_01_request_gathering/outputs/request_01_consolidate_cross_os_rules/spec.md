---
resource_id: "2d9c5fbb-526f-47e6-ad7f-49d985f12fdf"
resource_type: "output"
resource_name: "spec"
---

# Request 01: Consolidate Cross-OS Compatibility Rules

<!-- section_id: "cfe23740-26b5-4d38-91a8-e002523cd6f2" -->
## 1. Problem

Cross-OS compatibility rules and guidance are currently scattered across multiple locations, including:
- `sub_layer_0_04_rules/CROSS_OS_COMPATIBILITY_RULES.md`
- `sub_layer_0_05+_setup_dependant/.../operating_systems/`
- Various tool-specific configuration files.

This makes it difficult for developers and AI agents to find a single, authoritative source for cross-OS patterns, leading to inconsistent implementations and duplicated effort.

<!-- section_id: "8feb509c-53f0-490f-b2bd-12f5c2c86d30" -->
## 2. Request

Create a single, centralized, and authoritative guide for cross-OS compatibility. This guide should consolidate all existing rules and provide clear patterns for handling OS-specific configurations.

<!-- section_id: "57359fce-4fc6-48ed-b721-b0b88edb7a9f" -->
## 3. Scope

- **Analyze Existing Rules:** Systematically review all existing documentation and configuration files to identify all cross-OS compatibility rules.
- **Consolidate and De-duplicate:** Merge the scattered rules into a single document, removing redundant or conflicting information.
- **Define Clear Patterns:** Establish clear, documented patterns for common cross-OS challenges, such as:
    - Path handling (e.g., using variables or agnostic formats).
    - Environment variable management.
    - Tool availability checks and graceful degradation.
    - OS-specific script execution.
- **Location:** The new consolidated guide should be placed in a logical, easy-to-find location within the `sub_layer_0_04_rules` directory. The proposed location is `sub_layer_0_04_rules/00_unified_cross_os_dev_patterns.md`.
- **Update References:** All documentation or code that previously referenced the old, scattered rules should be updated to point to the new, centralized guide.

<!-- section_id: "84803ede-805f-4126-8989-67ad6f2d1b67" -->
## 4. Deliverables

1.  A single Markdown file containing the unified cross-OS compatibility guide.
2.  Pull request/commit updating all relevant files to reference the new guide.
3.  Deletion of the old, scattered rule files.

<!-- section_id: "4b79cc66-48bd-4415-a6e9-09db2baf7698" -->
## 5. Success Criteria

- A developer or AI agent can easily find all the information they need to write cross-OS compatible code by consulting a single document.
- Redundant or conflicting cross-OS guidance is eliminated from the codebase.
- The new guide is referenced correctly throughout the project.
        