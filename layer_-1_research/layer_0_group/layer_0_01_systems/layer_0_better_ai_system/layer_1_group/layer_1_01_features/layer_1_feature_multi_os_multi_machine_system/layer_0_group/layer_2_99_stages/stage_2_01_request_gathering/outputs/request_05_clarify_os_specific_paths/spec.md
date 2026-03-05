---
resource_id: "37516164-647f-4849-ad76-7b229bd52950"
resource_type: "output"
resource_name: "spec"
---

# Request 05: Clarify OS-Specific vs. Agnostic Paths

<!-- section_id: "35dc27f6-3bfd-4945-ba75-09f7534ae3c3" -->
## 1. Problem

The current file structure inconsistently mixes OS-specific and OS-agnostic files and configurations. The `layer_0_01_ai_manager_system/specific/` directory, for example, contains a deeply nested and sparsely populated structure for OS-specific configurations, but the pattern is not applied consistently elsewhere. This makes it difficult to locate the correct configuration for a given OS and understand what is truly universal.

This was identified as a **MINOR** severity issue ("OS-Specific Paths Mixed with Agnostic") in the AI System Audit.

<!-- section_id: "a55c55e4-cbbf-43fd-a60e-e42cc6b33d03" -->
## 2. Request

Define and implement a clear, consistent, and well-documented strategy for organizing OS-specific and OS-agnostic files and configurations throughout the project.

<!-- section_id: "fcab22db-f7a7-4c1a-92a9-9a9b788c4722" -->
## 3. Scope

- **Define a Clear Naming Convention:**
    - Establish a clear and simple directory naming convention to distinguish between OS-specific and agnostic content. A proposed convention is:
        - `agnostic/` for universal files.
        - `specific/` as a container for OS-specific directories.
        - `specific/linux/`, `specific/windows/`, `specific/darwin/` for OS-specific files.
- **Restructure Key Directories:**
    - Apply this convention to key areas where the specific/agnostic split is most needed, such as `layer_0_01_ai_manager_system`.
    - Audit other areas of the codebase, such as `sub_layer_0_05+_setup_dependant`, to see if this pattern should be applied there as well.
- **Develop Override Mechanism:**
    - Document a clear override or inheritance pattern. Files in an `agnostic` directory apply to all systems, while files in a `specific/{os}` directory can be used to augment or override the agnostic configuration for that particular OS.
- **Update Documentation:**
    - The new structure and override logic must be clearly documented in a central location, such as the new `unified_cross_os_dev_patterns.md` guide (from Request 01).
- **Refactor Existing Files:**
    - Move existing files into the new structure. For example, files currently in `layer_0_01_ai_manager_system/specific/os/wsl/...` would be moved to a more streamlined path like `layer_0_01_ai_manager_system/specific/linux_wsl/...`.

<!-- section_id: "53ee5887-996a-4cb9-865a-0f54de0ad437" -->
## 4. Deliverables

1.  A document defining the official directory structure and naming conventions for OS-specific vs. agnostic files.
2.  A pull request/commit that refactors the existing file structure (primarily within `layer_0_01_ai_manager_system`) to conform to the new standard.
3.  Updated documentation that explains the new pattern to developers and AI agents.

<!-- section_id: "b1e5ea90-e484-4cd2-9e78-1c0eb5c85a4d" -->
## 5. Success Criteria

- Any developer or AI agent can immediately understand where to find OS-specific configurations versus universal ones.
- The file structure itself serves as a form of documentation.
- Adding a new OS-specific configuration is a matter of creating a file in the correct, predictable directory.
- The separation of concerns between universal and specific configurations is clear and reduces the risk of making OS-specific changes that unintentionally break other systems.
        