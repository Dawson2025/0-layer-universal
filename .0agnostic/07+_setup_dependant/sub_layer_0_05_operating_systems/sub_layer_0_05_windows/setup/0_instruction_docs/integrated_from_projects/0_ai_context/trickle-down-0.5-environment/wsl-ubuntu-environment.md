---
resource_id: "93724a9f-824d-4a88-a4c5-e6e5d65f0a1c"
resource_type: "document"
resource_name: "wsl-ubuntu-environment"
---
# WSL Ubuntu Environment Standards
*Trickle-Down Level 0.5: Environment-Specific Standards*

<!-- section_id: "01171c92-04d3-472e-a2a6-ede3b0d9a092" -->
## Environment Context

<!-- section_id: "e53e6df9-5f8b-4dac-ba28-7187ffffca43" -->
### Operating Environment
- **Host System**: Windows with WSL2 Ubuntu integration
- **Development Environment**: WSL Ubuntu file system exclusively
- **Working Location**: `/home/dawson/code/lang-trak-in-progress/`
- **Access Pattern**: Windows PowerShell accessing WSL Ubuntu via `\\wsl.localhost\Ubuntu\`

<!-- section_id: "4dcebc6e-57c1-4306-88d2-43ef995379d7" -->
### Environment-Specific Rules

**MANDATORY ENVIRONMENT REQUIREMENT**: All development activities for projects in this WSL Ubuntu environment must be performed exclusively within the WSL Ubuntu file system.

<!-- section_id: "9710f488-7216-4f4c-bb01-f2dc78aadfca" -->
## File System Standards

<!-- section_id: "56b579a6-99af-44b0-99c6-b917b031f039" -->
### Correct Path Usage
- **WSL Ubuntu Paths**: `/home/dawson/code/lang-trak-in-progress/`
- **Relative Paths**: `./docs/trickle-down-1-project/constitution.md`
- **Home Directory**: `~/code/lang-trak-in-progress/`

<!-- section_id: "056f404a-98c9-45db-bad5-e026e199c250" -->
### Prohibited Path Usage
- ? Windows Drive Paths: `C:\Users\Dawson\Projects\lang-trak-in-progress\`
- ? Windows Long Paths: `\\?\C:\Users\Dawson\Projects\...`
- ? Mixed File System Operations
- ? Windows PowerShell direct file system access outside WSL

<!-- section_id: "789d6361-226a-4573-bb25-cb910e2745f4" -->
## Development Tool Configuration

<!-- section_id: "468dd6f9-c6bb-4deb-bb2b-89c395ef6b4f" -->
### Required WSL Ubuntu Setup
- **Python Environment**: Python 3.9+ installed in WSL Ubuntu
- **Node.js Environment**: Node.js 16+ via nvm in WSL Ubuntu
- **Firebase CLI**: Installed and configured within WSL Ubuntu
- **Git Configuration**: Git configured with proper credentials in WSL Ubuntu

<!-- section_id: "ff913bcc-1645-4ced-addc-236ccdec4938" -->
### Path Resolution Rules
- **Project Root**: Always reference from `/home/dawson/code/lang-trak-in-progress/`
- **Documentation**: `docs/` subdirectories using relative paths
- **Source Code**: All source files within WSL Ubuntu file system
- **Dependencies**: npm/pip packages installed in WSL Ubuntu environment

<!-- section_id: "6027e834-9939-41d0-b828-17b8657eb826" -->
## Access Patterns

<!-- section_id: "4cc9ae7a-be45-484e-833f-45cea2050183" -->
### Correct Access Methods
- ? **PowerShell via WSL**: Commands executed through WSL Ubuntu shell context
- ? **Relative Paths**: Using `./` and `../` for navigation
- ? **WSL Ubuntu Commands**: Native Linux commands within WSL
- ? **Environment Variables**: WSL Ubuntu environment variables

<!-- section_id: "f9418a7c-10c8-4f43-985e-8bfb4ee24381" -->
### File Operations Standards
- **File Creation**: All new files created within WSL Ubuntu file system
- **File Editing**: All file modifications performed via WSL Ubuntu paths
- **File Movement**: All file operations respect WSL Ubuntu permissions
- **File References**: All code references use WSL Ubuntu path conventions

<!-- section_id: "03abdc09-8584-4bf7-a29d-1605177e76fa" -->
## Environment Benefits

<!-- section_id: "320aa463-3513-4f03-8882-cb6cef1c9eec" -->
### Performance Advantages
- **Native Linux File System**: Optimal performance for development operations
- **Docker Integration**: Seamless Docker container operations
- **Package Management**: Native Linux package management (apt, npm, pip)
- **Symlink Support**: Full symbolic link support for development workflows

<!-- section_id: "ed0bb544-6e0e-43f5-bd7a-26d959ac07c5" -->
### Tool Integration
- **Firebase Emulators**: Optimal performance in Linux environment
- **SQLite Operations**: Native Linux SQLite performance
- **Python Development**: Full Linux Python environment capabilities
- **Node.js Tools**: Native Node.js development environment

<!-- section_id: "e7e747a9-acd9-4797-9305-b1a0b226c66b" -->
### Development Consistency
- **Team Alignment**: Consistent development environment across team members
- **CI/CD Compatibility**: Production environments mirror WSL Ubuntu setup
- **Tool Compatibility**: All development tools optimized for Linux environment
- **Path Consistency**: Uniform path handling across all operations

<!-- section_id: "7bdf176d-9f03-4b56-a2f7-b19a917ffd2a" -->
## Environment Validation

<!-- section_id: "b295e2b4-a500-496d-9058-bc6ef1c7ec70" -->
### Required Checks
Before any development work:
1. ? Verify current working directory is within WSL Ubuntu file system
2. ? Confirm all development tools are WSL Ubuntu versions
3. ? Validate file paths use WSL Ubuntu conventions
4. ? Ensure environment variables are set within WSL Ubuntu context

<!-- section_id: "f63212f4-faeb-4e9c-af3f-14707ad3be82" -->
### Environment Test Commands
```bash
# Verify WSL Ubuntu environment
pwd  # Should show /home/dawson/code/lang-trak-in-progress
which python3  # Should show WSL Ubuntu Python path
which node  # Should show WSL Ubuntu Node.js path
which firebase  # Should show WSL Ubuntu Firebase CLI path
```

<!-- section_id: "3f8824f5-edb3-4ad6-afa8-0b6fb3987e6c" -->
### File System Verification
```bash
# Verify file system access
ls -la docs/  # Should list documentation directories
file docs/trickle-down-0.5-environment/wsl-ubuntu-environment.md  # Should show text file
stat .  # Should show WSL Ubuntu file system details
```

<!-- section_id: "3fdc83c4-a79a-4f7e-a3ae-398869c3fa9f" -->
## Migration Guidelines

<!-- section_id: "e890748c-6c58-472b-9b4b-87b0173cd811" -->
### Moving from Windows File System
If any project files exist on Windows file system:
1. **Copy to WSL Ubuntu**: `cp -r /mnt/c/Users/Dawson/Projects/project-name ~/code/`
2. **Update References**: Change all file references to WSL Ubuntu paths
3. **Reconfigure Tools**: Reinstall/reconfigure development tools in WSL Ubuntu
4. **Verify Operations**: Test all development operations in WSL Ubuntu environment

<!-- section_id: "8d705ee0-47b9-4155-aac1-b59d39d4d54b" -->
### Environment Switching
- **From Windows PowerShell**: Access only via WSL Ubuntu context
- **Tool Installation**: Always install development tools within WSL Ubuntu
- **Configuration Files**: Store all config files in WSL Ubuntu home directory
- **Environment Variables**: Set all development environment variables in WSL Ubuntu

<!-- section_id: "49df94c2-d6a5-4b8b-bccc-fae4e6bca4de" -->
## Error Prevention

<!-- section_id: "014b0951-1c32-499e-aaf7-fe7ffa273f03" -->
### Common Mistakes to Avoid
- ? Creating files with Windows PowerShell directly
- ? Using Windows paths in any development operations
- ? Installing development tools in Windows instead of WSL Ubuntu
- ? Mixing file operations between Windows and WSL Ubuntu file systems

<!-- section_id: "ab31237f-0112-44ff-93df-bce1dcc8560a" -->
### Best Practices
- ? Always verify working directory before file operations
- ? Use WSL Ubuntu terminal for all development commands
- ? Keep all project assets within WSL Ubuntu file system
- ? Configure development tools exclusively in WSL Ubuntu environment

---

**Environment Level**: TD0.5  
**Scope**: WSL Ubuntu Development Environment  
**Applies To**: All projects developed within this WSL Ubuntu instance  
**Effective Date**: October 21, 2025

*This environment standard applies to all development work performed within the WSL Ubuntu environment and must be followed by all team members and AI assistants working on projects in this environment.*
