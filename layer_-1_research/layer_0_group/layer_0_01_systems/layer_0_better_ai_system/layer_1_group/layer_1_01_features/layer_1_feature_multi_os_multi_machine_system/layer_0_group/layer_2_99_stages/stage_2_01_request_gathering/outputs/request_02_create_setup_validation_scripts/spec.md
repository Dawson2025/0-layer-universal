---
resource_id: "ee2b54be-017c-4ce7-b819-5b55baed5cd6"
resource_type: "output"
resource_name: "spec"
---

# Request 02: Create Setup Validation Scripts

<!-- section_id: "1b99c935-b084-4786-a496-4fcc8e169d94" -->
## 1. Problem

The current setup process is manual and error-prone. There are no automated scripts to validate that the development environment is correctly configured. This leads to time-consuming debugging sessions when required files, directories, or tools are missing or misconfigured.

As identified in the AI System Audit, this is a **MAJOR** severity issue.

<!-- section_id: "f58f7556-450b-4e3c-9006-fd04d3b5f9c6" -->
## 2. Request

Develop a suite of setup validation scripts that can be run on-demand to ensure the integrity of the development environment across all supported operating systems (Linux, Windows/WSL, macOS).

<!-- section_id: "73d729d9-d094-429f-9f99-2fac78e90d42" -->
## 3. Scope

- **Master Validation Script:** Create a main script, `validate-setup.sh` (or similar), that acts as the entry point for running all validation checks.
- **Directory and File Structure Validation:**
    - The script should check for the existence of all critical directories and files required for the system to function.
    - This should be data-driven, likely from a configuration file that lists the expected structure.
- **Tool Availability Checks:**
    - The script should verify that all required command-line tools (e.g., `git`, `node`, `python`, `syncthing`, `termius`) are installed and available in the system's `PATH`.
    - It should check for minimum required versions where applicable.
- **Configuration Validation:**
    - The script should check key configuration files for correct formatting and essential values. For example, it could check that a JSON or YAML file is parsable and contains required keys.
- **OS-Specific Health Checks:**
    - The validation logic should be modular to allow for OS-specific checks. For example, checking for `apt` on Ubuntu or `brew` on macOS.
- **Output and Reporting:**
    - The script should provide clear, actionable output.
    - A successful run should report that the environment is valid.
    - A failed run should clearly list all the issues that were found, with guidance on how to fix them (e.g., "Tool `syncthing` not found. Please install it by following the instructions in [link-to-docs]").

<!-- section_id: "1f08931d-71f0-46f8-82c2-63c0449f9b3d" -->
## 4. Deliverables

1.  A master `validate-setup.sh` script located in a top-level `/scripts` directory.
2.  Supporting scripts or configuration files for the validation checks.
3.  Documentation in the main `CLAUDE.md` or a dedicated `SETUP.md` on how to run the validation script.

<!-- section_id: "d99f5fb4-b9f7-4f15-aa31-7e7c15faf940" -->
## 5. Success Criteria

- Running the `validate-setup.sh` script provides a clear pass/fail status of the environment's health.
- The script correctly identifies common setup problems like missing tools, files, or directories.
- The error messages are clear enough for a new developer or an AI agent to take corrective action.
- The script is easily extensible to add new validation checks as the system evolves.
        