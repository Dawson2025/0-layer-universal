---
resource_id: "b4639622-743b-4ec4-a510-aec8ba8279a2"
resource_type: "output"
resource_name: "spec"
---

# Request 04: Archive Legacy Code and Documentation

<!-- section_id: "51ef5535-1533-4fb3-9912-39c549516f7d" -->
## 1. Problem

The codebase contains legacy code and documentation, specifically old sub-layer READMEs, that are no longer in use but have not been properly archived or removed. This creates confusion for both developers and AI agents, who may accidentally reference or rely on outdated information.

This was identified as a **MINOR** severity issue ("Legacy Code Not Cleaned Up") in the AI System Audit.

<!-- section_id: "5dfacdd6-eb6c-48df-a1e8-99573ad1dd69" -->
## 2. Request

Systematically identify, archive, and remove legacy code and documentation to reduce clutter and prevent confusion.

<!-- section_id: "51484b5e-73d5-42f2-9753-a76bd98d01ef" -->
## 3. Scope

- **Identify Legacy Artifacts:**
    - The primary location identified is `sub_layer_0_05+_setup_dependant/legacy_sublayer_readmes/`.
    - A full codebase audit should be performed to identify any other instances of legacy files. This includes:
        - Deprecated scripts.
        - Old migration reports that are no longer relevant.
        - README files for directories that have been moved or removed.
- **Archiving Strategy:**
    - A dedicated `archives` directory should be created at a logical level, for instance `layer_0_group/archives/`.
    - Legacy files should be moved into a subdirectory within `archives` that clearly indicates their origin and date of archival, e.g., `layer_0_group/archives/2026-01-25_legacy_sublayer_readmes/`.
    - The archived files should be compressed if they are large.
- **Update References:**
    - Before deleting the old files, the codebase must be searched for any references to them.
    - These references should either be removed or updated to point to current, relevant documentation.
- **Removal:**
    - Once all references are updated and the files are securely archived, the original legacy files and directories should be deleted from their active locations in the codebase.

<!-- section_id: "d827f077-31a9-4b7b-a413-f28dd3e92542" -->
## 4. Deliverables

1.  An `archives` directory containing the archived legacy files.
2.  A pull request/commit that:
    - Removes the original legacy files from the codebase.
    - Updates any code or documentation that referenced the legacy files.
3.  A summary document in the root of the `archives` directory explaining what was archived and why.

<!-- section_id: "ff83be56-9099-460c-b65d-5bf7836ce150" -->
## 5. Success Criteria

- The codebase no longer contains confusing or outdated legacy files in active development areas.
- It is clear to all developers and agents what is considered "legacy" and what is "current".
- Any developer or agent searching the codebase will not find references to the old, deprecated files.
- The risk of using outdated information is eliminated.
        