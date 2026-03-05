---
resource_id: "12d31769-2da8-400a-b90f-ef4c6bd08f13"
resource_type: "document"
resource_name: "wsl-ubuntu-environment"
---
# WSL Ubuntu Environment Standards
*Trickle-Down Level 0.5: Environment-Specific Standards*

<!-- section_id: "2c3ce9c5-4c8f-4467-ad2f-3268872a6f98" -->
## Environment Context

<!-- section_id: "139edfac-94ee-4b27-8cb7-415a4fdca4b9" -->
### Operating Environment
- **Host System**: Windows with WSL2 Ubuntu integration
- **Development Environment**: WSL Ubuntu file system exclusively
- **Working Location**: `/home/dawson/code/lang-trak-in-progress/`
- **Access Pattern**: Windows PowerShell accessing WSL Ubuntu via `\\wsl.localhost\Ubuntu\`

<!-- section_id: "d2b48aea-cc2f-4b94-9244-ab1fe06f8644" -->
### Environment-Specific Rules

**MANDATORY ENVIRONMENT REQUIREMENT**: All development activities for projects in this WSL Ubuntu environment must be performed exclusively within the WSL Ubuntu file system.

<!-- section_id: "8b210a7d-a190-4d2d-8ba5-0f684a50f1a6" -->
## File System Standards

<!-- section_id: "24e732b4-d630-4290-b3c1-1621a8c1ace5" -->
### Correct Path Usage
- **WSL Ubuntu Paths**: `/home/dawson/code/lang-trak-in-progress/`
- **Relative Paths**: `./docs/trickle-down-1-project/constitution.md`
- **Home Directory**: `~/code/lang-trak-in-progress/`

<!-- section_id: "546f1bb9-5aa7-448f-9a0d-bb5754b4daaa" -->
### Prohibited Path Usage
- ? Windows Drive Paths: `C:\Users\Dawson\Projects\lang-trak-in-progress\`
- ? Windows Long Paths: `\\?\C:\Users\Dawson\Projects\...`
- ? Mixed File System Operations
- ? Windows PowerShell direct file system access outside WSL

<!-- section_id: "f40fa79e-1095-4ebf-a086-400561c5994d" -->
## Development Tool Configuration

<!-- section_id: "54a53260-e8eb-4264-bd1f-ce6ed7acd3bd" -->
### Required WSL Ubuntu Setup
- **Python Environment**: Python 3.9+ installed in WSL Ubuntu
- **Node.js Environment**: Node.js 16+ via nvm in WSL Ubuntu
- **Firebase CLI**: Installed and configured within WSL Ubuntu
- **Git Configuration**: Git configured with proper credentials in WSL Ubuntu

<!-- section_id: "4b731233-bc97-4991-a51b-ef9c3c314fe1" -->
### Path Resolution Rules
- **Project Root**: Always reference from `/home/dawson/code/lang-trak-in-progress/`
- **Documentation**: `docs/` subdirectories using relative paths
- **Source Code**: All source files within WSL Ubuntu file system
- **Dependencies**: npm/pip packages installed in WSL Ubuntu environment

<!-- section_id: "490ce046-fae3-40a4-aab4-8fc06fb18b39" -->
## Access Patterns

<!-- section_id: "8955cda6-41c7-4666-9047-9fab49a85e7f" -->
### Correct Access Methods
- ? **PowerShell via WSL**: Commands executed through WSL Ubuntu shell context
- ? **Relative Paths**: Using `./` and `../` for navigation
- ? **WSL Ubuntu Commands**: Native Linux commands within WSL
- ? **Environment Variables**: WSL Ubuntu environment variables

<!-- section_id: "838ae2fa-b2a2-41b0-8f5b-947d52c36260" -->
### File Operations Standards
- **File Creation**: All new files created within WSL Ubuntu file system
- **File Editing**: All file modifications performed via WSL Ubuntu paths
- **File Movement**: All file operations respect WSL Ubuntu permissions
- **File References**: All code references use WSL Ubuntu path conventions

<!-- section_id: "f2b0c6b7-6f60-494b-8cb1-0753a1bfe810" -->
## Environment Benefits

<!-- section_id: "c69e0df2-9da0-4af1-9b78-14203cb6a7ec" -->
### Performance Advantages
- **Native Linux File System**: Optimal performance for development operations
- **Docker Integration**: Seamless Docker container operations
- **Package Management**: Native Linux package management (apt, npm, pip)
- **Symlink Support**: Full symbolic link support for development workflows

<!-- section_id: "0b295e9c-bd36-42b5-b0c7-c2c04e013921" -->
### Tool Integration
- **Firebase Emulators**: Optimal performance in Linux environment
- **SQLite Operations**: Native Linux SQLite performance
- **Python Development**: Full Linux Python environment capabilities
- **Node.js Tools**: Native Node.js development environment

<!-- section_id: "2c4a4a0c-4b23-474f-b598-0e12425a527d" -->
### Development Consistency
- **Team Alignment**: Consistent development environment across team members
- **CI/CD Compatibility**: Production environments mirror WSL Ubuntu setup
- **Tool Compatibility**: All development tools optimized for Linux environment
- **Path Consistency**: Uniform path handling across all operations

<!-- section_id: "bae17ad0-378b-4048-85a7-cf27e996e8b3" -->
## Environment Validation

<!-- section_id: "611d94de-b5bd-468b-84d8-82871198c4b5" -->
### Required Checks
Before any development work:
1. ? Verify current working directory is within WSL Ubuntu file system
2. ? Confirm all development tools are WSL Ubuntu versions
3. ? Validate file paths use WSL Ubuntu conventions
4. ? Ensure environment variables are set within WSL Ubuntu context

<!-- section_id: "bd3f131b-f6b4-4169-8db7-1b2d67c1c7d4" -->
### Environment Test Commands
```bash
# Verify WSL Ubuntu environment
pwd  # Should show /home/dawson/code/lang-trak-in-progress
which python3  # Should show WSL Ubuntu Python path
which node  # Should show WSL Ubuntu Node.js path
which firebase  # Should show WSL Ubuntu Firebase CLI path
```

<!-- section_id: "316c0693-b098-4b74-bb04-878432dc7cd8" -->
### File System Verification
```bash
# Verify file system access
ls -la docs/  # Should list documentation directories
file docs/trickle-down-0.5-environment/wsl-ubuntu-environment.md  # Should show text file
stat .  # Should show WSL Ubuntu file system details
```

<!-- section_id: "7f963723-0881-4c04-b70e-d4e765cc3ead" -->
## Migration Guidelines

<!-- section_id: "811187c0-c1fe-4637-b26f-c1d23e28eed1" -->
### Moving from Windows File System
If any project files exist on Windows file system:
1. **Copy to WSL Ubuntu**: `cp -r /mnt/c/Users/Dawson/Projects/project-name ~/code/`
2. **Update References**: Change all file references to WSL Ubuntu paths
3. **Reconfigure Tools**: Reinstall/reconfigure development tools in WSL Ubuntu
4. **Verify Operations**: Test all development operations in WSL Ubuntu environment

<!-- section_id: "c269dade-bded-4281-bee7-a9608df1a311" -->
### Environment Switching
- **From Windows PowerShell**: Access only via WSL Ubuntu context
- **Tool Installation**: Always install development tools within WSL Ubuntu
- **Configuration Files**: Store all config files in WSL Ubuntu home directory
- **Environment Variables**: Set all development environment variables in WSL Ubuntu

<!-- section_id: "40f4e962-d2cc-4923-a929-4191319512e8" -->
## Error Prevention

<!-- section_id: "eaf6e399-f894-44d1-8067-e14731842eab" -->
### Common Mistakes to Avoid
- ? Creating files with Windows PowerShell directly
- ? Using Windows paths in any development operations
- ? Installing development tools in Windows instead of WSL Ubuntu
- ? Mixing file operations between Windows and WSL Ubuntu file systems

<!-- section_id: "8af1f25c-4f52-4c10-a176-d44ba68b99a7" -->
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
