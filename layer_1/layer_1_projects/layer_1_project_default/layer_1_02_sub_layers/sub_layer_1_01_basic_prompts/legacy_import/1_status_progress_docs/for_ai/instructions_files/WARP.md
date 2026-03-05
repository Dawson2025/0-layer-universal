---
resource_id: "78c3ef9c-c3e6-4145-85db-2e689993bba8"
resource_type: "document"
resource_name: "WARP"
---
# WARP.md

This file provides guidance to Warp AI Assistant when working with the Language Tracker project.

<!-- section_id: "2ce502f3-7524-4cc8-b6db-d17bc18b38fb" -->
## Trickle-Down Documentation System

**MANDATORY:** Warp AI Assistant must use the hierarchical trickle-down documentation system for all operations.

<!-- section_id: "f4e54d55-d54b-44f2-a8ac-0a7d7b3a6674" -->
### Context Loading Protocol for Warp

**Required Loading Order: TD0 ? TD0.5 ? TD1 ? TD2 ? TD3**

**Critical for Warp: TD0.5 Environment Standards**
- **Location**: `/docs/1_trickle_down/trickle-down-0.5-environment/wsl-ubuntu-environment.md`
- **Contains**: WSL Ubuntu file system requirements (MANDATORY)
- **Why Critical**: Warp operates at the file system level and must comply with environment standards

<!-- section_id: "dc98fb32-10ee-423b-a7b1-1facfe886088" -->
### Warp-Specific Requirements

**File System Operations:**
- ? All file operations must occur within WSL Ubuntu file system
- ? Use WSL Ubuntu paths: `/home/dawson/code/lang-trak-in-progress/`
- ? Respect WSL Ubuntu permissions and file ownership
- ? Never use Windows C:\ drive paths for development operations
- ? Never bypass WSL Ubuntu environment requirements

**Development Tool Integration:**
- Python: Use WSL Ubuntu Python installation
- Node.js: Use WSL Ubuntu Node.js via nvm
- Firebase CLI: Use WSL Ubuntu Firebase CLI installation
- Git: Use WSL Ubuntu Git configuration

<!-- section_id: "3c305de0-531b-4d01-8b2d-1d9d263360f0" -->
### Trickle-Down Context Loading for Warp

**Before any file operations or code assistance:**

1. **TD0**: `/docs/1_trickle_down/trickle-down-0-universal/universal_instructions.md`
2. **TD0.5**: `/docs/1_trickle_down/trickle-down-0.5-environment/wsl-ubuntu-environment.md`
3. **TD1**: `/docs/1_trickle_down/trickle-down-1-project/constitution.md`
4. **TD2**: Relevant feature documentation (as needed)
5. **TD3**: Implementation details (as needed)

<!-- section_id: "d8110b11-6c1c-4835-9818-e547a39a38ee" -->
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
