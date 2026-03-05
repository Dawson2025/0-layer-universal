---
resource_id: "3b0ece8f-4eff-443b-b816-29ee8054e73d"
resource_type: "document"
resource_name: "wsl-ubuntu-environment"
---
# WSL Ubuntu Environment Standards
*Trickle-Down Level 0.5: Environment-Specific Standards*

<!-- section_id: "44f6f80c-1849-4214-8731-a7592a6b04a5" -->
## Environment Context

<!-- section_id: "d5b106a1-70a7-4319-be8a-ddbf6bb5a984" -->
### Operating Environment
- **Host System**: Windows with WSL2 Ubuntu integration
- **Development Environment**: WSL Ubuntu file system exclusively
- **Working Location**: `/home/dawson/code/lang-trak-in-progress/`
- **Access Pattern**: Windows PowerShell accessing WSL Ubuntu via `\\wsl.localhost\Ubuntu\`

<!-- section_id: "5c2aa33d-7c38-4892-aeaf-cfe71dda1fcf" -->
### Environment-Specific Rules

**MANDATORY ENVIRONMENT REQUIREMENT**: All development activities for projects in this WSL Ubuntu environment must be performed exclusively within the WSL Ubuntu file system.

<!-- section_id: "52399092-b03a-45e2-a6c7-3bce3f2c5b5b" -->
## File System Standards

<!-- section_id: "63e4c2e3-082a-4687-a90a-07dabf2ea0fa" -->
### Correct Path Usage
- **WSL Ubuntu Paths**: `/home/dawson/code/lang-trak-in-progress/`
- **Relative Paths**: `./docs/trickle-down-1-project/constitution.md`
- **Home Directory**: `~/code/lang-trak-in-progress/`

<!-- section_id: "fda2d837-0a10-4464-a1a9-06763a8666cf" -->
### Prohibited Path Usage
- ? Windows Drive Paths: `C:\Users\Dawson\Projects\lang-trak-in-progress\`
- ? Windows Long Paths: `\\?\C:\Users\Dawson\Projects\...`
- ? Mixed File System Operations
- ? Windows PowerShell direct file system access outside WSL

<!-- section_id: "c5b7b616-0edf-45ba-bbf1-51e09ba877f6" -->
## Development Tool Configuration

<!-- section_id: "5030183f-fcc6-4be1-bff1-e68c4b29a0d8" -->
### Required WSL Ubuntu Setup
- **Python Environment**: Python 3.9+ installed in WSL Ubuntu
- **Node.js Environment**: Node.js 16+ via nvm in WSL Ubuntu
- **Firebase CLI**: Installed and configured within WSL Ubuntu
- **Git Configuration**: Git configured with proper credentials in WSL Ubuntu

<!-- section_id: "bad3ce21-3995-4171-8b20-e26b6db32d73" -->
### Path Resolution Rules
- **Project Root**: Always reference from `/home/dawson/code/lang-trak-in-progress/`
- **Documentation**: `docs/` subdirectories using relative paths
- **Source Code**: All source files within WSL Ubuntu file system
- **Dependencies**: npm/pip packages installed in WSL Ubuntu environment

<!-- section_id: "6c15df16-7129-41a7-8324-c3a6350720b5" -->
## Access Patterns

<!-- section_id: "6ba6d182-90a4-48fc-a731-71d7fb102d94" -->
### Correct Access Methods
- ? **PowerShell via WSL**: Commands executed through WSL Ubuntu shell context
- ? **Relative Paths**: Using `./` and `../` for navigation
- ? **WSL Ubuntu Commands**: Native Linux commands within WSL
- ? **Environment Variables**: WSL Ubuntu environment variables

<!-- section_id: "1a00a7ce-a03c-4de2-9925-5e7be89b5ce7" -->
### File Operations Standards
- **File Creation**: All new files created within WSL Ubuntu file system
- **File Editing**: All file modifications performed via WSL Ubuntu paths
- **File Movement**: All file operations respect WSL Ubuntu permissions
- **File References**: All code references use WSL Ubuntu path conventions

<!-- section_id: "fe5db8b9-ee62-41f3-b925-80c784abf330" -->
## Environment Benefits

<!-- section_id: "4749c9cf-13fd-458e-9e8d-41ac91936560" -->
### Performance Advantages
- **Native Linux File System**: Optimal performance for development operations
- **Docker Integration**: Seamless Docker container operations
- **Package Management**: Native Linux package management (apt, npm, pip)
- **Symlink Support**: Full symbolic link support for development workflows

<!-- section_id: "4ea325b9-6595-49a3-a452-c84f9badd807" -->
### Tool Integration
- **Firebase Emulators**: Optimal performance in Linux environment
- **SQLite Operations**: Native Linux SQLite performance
- **Python Development**: Full Linux Python environment capabilities
- **Node.js Tools**: Native Node.js development environment

<!-- section_id: "0018d1ba-3052-4c4b-a405-0789695d0e3c" -->
### Development Consistency
- **Team Alignment**: Consistent development environment across team members
- **CI/CD Compatibility**: Production environments mirror WSL Ubuntu setup
- **Tool Compatibility**: All development tools optimized for Linux environment
- **Path Consistency**: Uniform path handling across all operations

<!-- section_id: "c9fe7fe6-e758-4a3e-b1ee-2d54063c7199" -->
## Environment Validation

<!-- section_id: "1edb552c-5f1d-41ef-8c16-a2b1fa349e00" -->
### Required Checks
Before any development work:
1. ? Verify current working directory is within WSL Ubuntu file system
2. ? Confirm all development tools are WSL Ubuntu versions
3. ? Validate file paths use WSL Ubuntu conventions
4. ? Ensure environment variables are set within WSL Ubuntu context

<!-- section_id: "77e37a38-64da-4c89-9e8b-de41f518f143" -->
### Environment Test Commands
```bash
# Verify WSL Ubuntu environment
pwd  # Should show /home/dawson/code/lang-trak-in-progress
which python3  # Should show WSL Ubuntu Python path
which node  # Should show WSL Ubuntu Node.js path
which firebase  # Should show WSL Ubuntu Firebase CLI path
```

<!-- section_id: "d8da984a-4e31-4b7c-b5af-cad0835356c1" -->
### File System Verification
```bash
# Verify file system access
ls -la docs/  # Should list documentation directories
file docs/trickle-down-0.5-environment/wsl-ubuntu-environment.md  # Should show text file
stat .  # Should show WSL Ubuntu file system details
```

<!-- section_id: "73c71906-cac0-41bb-b7e0-56c8d7706291" -->
## Migration Guidelines

<!-- section_id: "cf64d880-a911-4506-aeff-6a44b35f4a6c" -->
### Moving from Windows File System
If any project files exist on Windows file system:
1. **Copy to WSL Ubuntu**: `cp -r /mnt/c/Users/Dawson/Projects/project-name ~/code/`
2. **Update References**: Change all file references to WSL Ubuntu paths
3. **Reconfigure Tools**: Reinstall/reconfigure development tools in WSL Ubuntu
4. **Verify Operations**: Test all development operations in WSL Ubuntu environment

<!-- section_id: "eafdeed8-4b5f-445d-aa36-1cb7a47dcfa0" -->
### Environment Switching
- **From Windows PowerShell**: Access only via WSL Ubuntu context
- **Tool Installation**: Always install development tools within WSL Ubuntu
- **Configuration Files**: Store all config files in WSL Ubuntu home directory
- **Environment Variables**: Set all development environment variables in WSL Ubuntu

<!-- section_id: "f6e147c8-9a1a-4a70-8b97-e7a3b8d533bb" -->
## Error Prevention

<!-- section_id: "08abe934-86f5-4768-8d42-2360c816c394" -->
### Common Mistakes to Avoid
- ? Creating files with Windows PowerShell directly
- ? Using Windows paths in any development operations
- ? Installing development tools in Windows instead of WSL Ubuntu
- ? Mixing file operations between Windows and WSL Ubuntu file systems

<!-- section_id: "b5a68de9-e7dc-4c63-a17d-7b86cf7d4445" -->
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
