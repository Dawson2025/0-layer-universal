---
resource_id: "028f394a-5fe3-42b5-8f9c-cfb5ea6ac64b"
resource_type: "document"
resource_name: "WARP"
---
# WARP.md

This file provides guidance to Warp AI Assistant when working with the Language Tracker project.

<!-- section_id: "c47c7cc5-3ab6-4b4f-937d-d6dd6fe1cb44" -->
## Trickle-Down Documentation System

**MANDATORY:** Warp AI Assistant must use the hierarchical trickle-down documentation system for all operations.

<!-- section_id: "49e502a6-9495-427b-a2fb-f1aaa951071c" -->
### Context Loading Protocol for Warp

**Required Loading Order: TD0 ? TD0.5 ? TD1 ? TD2 ? TD3**

**Critical for Warp: TD0.5 Environment Standards**
- **Location**: `/docs/1_trickle_down/trickle-down-0.5-environment/wsl-ubuntu-environment.md`
- **Contains**: WSL Ubuntu file system requirements (MANDATORY)
- **Why Critical**: Warp operates at the file system level and must comply with environment standards

<!-- section_id: "bedfccdc-eccd-474a-9ec4-c77290a86595" -->
### Warp-Specific Requirements

**File System Operations:**
- ? All file operations must occur within WSL Ubuntu file system
- ? Use WSL Ubuntu paths: `/home/dawson/dawson-workspace/code/lang-trak-in-progress/`
- ? Respect WSL Ubuntu permissions and file ownership
- ? Never use Windows C:\ drive paths for development operations
- ? Never bypass WSL Ubuntu environment requirements

**Development Tool Integration:**
- Python: Use WSL Ubuntu Python installation
- Node.js: Use WSL Ubuntu Node.js via nvm
- Firebase CLI: Use WSL Ubuntu Firebase CLI installation
- Git: Use WSL Ubuntu Git configuration

<!-- section_id: "cba83da7-6073-43f1-8ebb-281b0f47ce3e" -->
### Trickle-Down Context Loading for Warp

**Before any file operations or code assistance:**

1. **TD0**: `/docs/1_trickle_down/trickle-down-0-universal/universal_instructions.md`
2. **TD0.5**: `/docs/1_trickle_down/trickle-down-0.5-environment/wsl-ubuntu-environment.md`
3. **TD1**: `/docs/1_trickle_down/trickle-down-1-project/constitution.md`
4. **TD2**: Relevant feature documentation (as needed)
5. **TD3**: Implementation details (as needed)

<!-- section_id: "113d1e50-bae4-48c6-80f3-6e178e6d8ec8" -->
### WSL Ubuntu Environment Compliance

**CRITICAL:** All Warp operations must comply with TD0.5 environment standards:
- All file operations within WSL Ubuntu file system
- No Windows C:\ drive operations
- Use WSL Ubuntu paths exclusively
- Respect environment tool configurations

---

**Warp Configuration Version**: 1.0
**Last Updated**: October 21, 2025
**Trickle-Down System**: TD0 ? TD0.5 ? TD1 ? TD2 ? TD3
