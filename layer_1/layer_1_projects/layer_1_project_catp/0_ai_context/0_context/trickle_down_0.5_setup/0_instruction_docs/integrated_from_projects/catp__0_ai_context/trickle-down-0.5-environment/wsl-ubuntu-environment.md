---
resource_id: "03b534cd-3b94-4fce-99ef-ceede691b2db"
resource_type: "document"
resource_name: "wsl-ubuntu-environment"
---
# WSL Ubuntu Environment Standards
*Trickle-Down Level 0.5: Environment-Specific Standards*

<!-- section_id: "df09666c-582f-436b-a3d6-3aa331fc01ee" -->
## Environment Context

<!-- section_id: "8228b39f-7207-48d7-81d7-24ee561ea41d" -->
### Operating Environment
- **Host System**: Windows with WSL2 Ubuntu integration
- **Development Environment**: WSL Ubuntu file system exclusively
- **Working Location**: `/home/dawson/dawson-workspace/code/lang-trak-in-progress/`
- **Access Pattern**: Windows PowerShell accessing WSL Ubuntu via `\\wsl.localhost\Ubuntu\`

<!-- section_id: "ad793af8-a6ad-443a-8e46-4fad6056ade3" -->
### Environment-Specific Rules

**MANDATORY ENVIRONMENT REQUIREMENT**: All development activities for projects in this WSL Ubuntu environment must be performed exclusively within the WSL Ubuntu file system.

<!-- section_id: "47878e67-44e1-4fd2-9ed8-0007602628e0" -->
## File System Standards

<!-- section_id: "0ee1380b-e3eb-4998-af39-0f544350c24d" -->
### Correct Path Usage
- **WSL Ubuntu Paths**: `/home/dawson/dawson-workspace/code/lang-trak-in-progress/`
- **Relative Paths**: `./docs/trickle-down-1-project/constitution.md`
- **Home Directory**: `~/code/lang-trak-in-progress/`

<!-- section_id: "6235f769-79f5-469d-9a8f-0ef4f68d9d24" -->
### Prohibited Path Usage
- ? Windows Drive Paths: `C:\Users\Dawson\Projects\lang-trak-in-progress\`
- ? Windows Long Paths: `\\?\C:\Users\Dawson\Projects\...`
- ? Mixed File System Operations
- ? Windows PowerShell direct file system access outside WSL

<!-- section_id: "6062937d-cbad-41b5-90ea-6df29e0920ff" -->
## Development Tool Configuration

<!-- section_id: "98407e3d-f88e-4fe3-afe9-4a7aa7303735" -->
### Required WSL Ubuntu Setup
- **Python Environment**: Python 3.9+ installed in WSL Ubuntu
- **Node.js Environment**: Node.js 16+ via nvm in WSL Ubuntu
- **Firebase CLI**: Installed and configured within WSL Ubuntu
- **Git Configuration**: Git configured with proper credentials in WSL Ubuntu

<!-- section_id: "1d400226-c98e-43e1-be6e-a119c98a278d" -->
### Path Resolution Rules
- **Project Root**: Always reference from `/home/dawson/dawson-workspace/code/lang-trak-in-progress/`
- **Documentation**: `docs/` subdirectories using relative paths
- **Source Code**: All source files within WSL Ubuntu file system
- **Dependencies**: npm/pip packages installed in WSL Ubuntu environment

<!-- section_id: "ddfc8acf-2d85-4022-aa4d-8af0b87bfe7a" -->
## Access Patterns

<!-- section_id: "1b126762-9d18-4678-af01-5ac5a7c0a6b5" -->
### Correct Access Methods
- ? **PowerShell via WSL**: Commands executed through WSL Ubuntu shell context
- ? **Relative Paths**: Using `./` and `../` for navigation
- ? **WSL Ubuntu Commands**: Native Linux commands within WSL
- ? **Environment Variables**: WSL Ubuntu environment variables

<!-- section_id: "87bbc9e0-dcd6-43ae-817d-ce92131588b3" -->
### File Operations Standards
- **File Creation**: All new files created within WSL Ubuntu file system
- **File Editing**: All file modifications performed via WSL Ubuntu paths
- **File Movement**: All file operations respect WSL Ubuntu permissions
- **File References**: All code references use WSL Ubuntu path conventions

<!-- section_id: "538649bb-13d8-40f0-8775-68c5e5408621" -->
## Environment Benefits

<!-- section_id: "c1dcde80-f25c-4207-bd93-2b4d341cdfa7" -->
### Performance Advantages
- **Native Linux File System**: Optimal performance for development operations
- **Docker Integration**: Seamless Docker container operations
- **Package Management**: Native Linux package management (apt, npm, pip)
- **Symlink Support**: Full symbolic link support for development workflows

<!-- section_id: "d8bcd279-4d98-45d3-a14e-048581180bab" -->
### Tool Integration
- **Firebase Emulators**: Optimal performance in Linux environment
- **SQLite Operations**: Native Linux SQLite performance
- **Python Development**: Full Linux Python environment capabilities
- **Node.js Tools**: Native Node.js development environment

<!-- section_id: "f5a3b32e-0dc8-476d-8765-e2e0781458b8" -->
### Development Consistency
- **Team Alignment**: Consistent development environment across team members
- **CI/CD Compatibility**: Production environments mirror WSL Ubuntu setup
- **Tool Compatibility**: All development tools optimized for Linux environment
- **Path Consistency**: Uniform path handling across all operations

<!-- section_id: "01e4bcf0-072f-4181-a7db-140f55aa8f45" -->
## Environment Validation

<!-- section_id: "d87e39e2-3f09-45eb-9cc8-9e62426c37a1" -->
### Required Checks
Before any development work:
1. ? Verify current working directory is within WSL Ubuntu file system
2. ? Confirm all development tools are WSL Ubuntu versions
3. ? Validate file paths use WSL Ubuntu conventions
4. ? Ensure environment variables are set within WSL Ubuntu context

<!-- section_id: "47af9661-4072-4a71-ad18-ede7ed837681" -->
### Environment Test Commands
```bash
# Verify WSL Ubuntu environment
pwd  # Should show /home/dawson/dawson-workspace/code/lang-trak-in-progress
which python3  # Should show WSL Ubuntu Python path
which node  # Should show WSL Ubuntu Node.js path
which firebase  # Should show WSL Ubuntu Firebase CLI path
```

<!-- section_id: "e8ffb157-1f68-4b63-9028-17f1140cecc0" -->
### File System Verification
```bash
# Verify file system access
ls -la docs/  # Should list documentation directories
file docs/trickle-down-0.5-environment/wsl-ubuntu-environment.md  # Should show text file
stat .  # Should show WSL Ubuntu file system details
```

<!-- section_id: "dd333a2e-7622-4f05-8ee1-4f30d5ca4d8f" -->
## Migration Guidelines

<!-- section_id: "e132e83b-3a64-4ff4-9eaa-ca0772dadc35" -->
### Moving from Windows File System
If any project files exist on Windows file system:
1. **Copy to WSL Ubuntu**: `cp -r /mnt/c/Users/Dawson/Projects/project-name ~/code/`
2. **Update References**: Change all file references to WSL Ubuntu paths
3. **Reconfigure Tools**: Reinstall/reconfigure development tools in WSL Ubuntu
4. **Verify Operations**: Test all development operations in WSL Ubuntu environment

<!-- section_id: "d7be09b5-866c-40d5-9f36-7f8b71edd128" -->
### Environment Switching
- **From Windows PowerShell**: Access only via WSL Ubuntu context
- **Tool Installation**: Always install development tools within WSL Ubuntu
- **Configuration Files**: Store all config files in WSL Ubuntu home directory
- **Environment Variables**: Set all development environment variables in WSL Ubuntu

<!-- section_id: "c3f1b9f1-d85b-4874-bfe4-aa49430f8d5f" -->
## Error Prevention

<!-- section_id: "d4a4699f-9ca8-4e19-a445-5a98baab7f31" -->
### Common Mistakes to Avoid
- ? Creating files with Windows PowerShell directly
- ? Using Windows paths in any development operations
- ? Installing development tools in Windows instead of WSL Ubuntu
- ? Mixing file operations between Windows and WSL Ubuntu file systems

<!-- section_id: "a3eee84b-469f-410a-860f-700b6a4fd583" -->
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
