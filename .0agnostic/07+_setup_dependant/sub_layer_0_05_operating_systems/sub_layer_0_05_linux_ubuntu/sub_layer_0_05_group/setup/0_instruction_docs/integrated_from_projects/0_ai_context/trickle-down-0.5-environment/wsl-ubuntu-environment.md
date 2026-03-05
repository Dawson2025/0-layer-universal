---
resource_id: "b0bee0b1-63f1-414a-bfb4-b3e1bd7e47e5"
resource_type: "document"
resource_name: "wsl-ubuntu-environment"
---
# WSL Ubuntu Environment Standards
*Trickle-Down Level 0.5: Environment-Specific Standards*

<!-- section_id: "4d383c01-525d-4887-be29-8aa2820c34e0" -->
## Environment Context

<!-- section_id: "a8ab1c23-fbab-4ef8-8b54-d880d50fe776" -->
### Operating Environment
- **Host System**: Windows with WSL2 Ubuntu integration
- **Development Environment**: WSL Ubuntu file system exclusively
- **Working Location**: `/home/dawson/code/lang-trak-in-progress/`
- **Access Pattern**: Windows PowerShell accessing WSL Ubuntu via `\\wsl.localhost\Ubuntu\`

<!-- section_id: "58b1defc-a6e2-4114-af0d-684ed428672e" -->
### Environment-Specific Rules

**MANDATORY ENVIRONMENT REQUIREMENT**: All development activities for projects in this WSL Ubuntu environment must be performed exclusively within the WSL Ubuntu file system.

<!-- section_id: "9f143146-b472-4a58-83cd-c54d5c7fc6bd" -->
## File System Standards

<!-- section_id: "1d8ea15b-e45e-4fd7-a185-ad7223fd002f" -->
### Correct Path Usage
- **WSL Ubuntu Paths**: `/home/dawson/code/lang-trak-in-progress/`
- **Relative Paths**: `./docs/trickle-down-1-project/constitution.md`
- **Home Directory**: `~/code/lang-trak-in-progress/`

<!-- section_id: "1e1d5051-9725-4ba3-aaed-d74c6e8a5449" -->
### Prohibited Path Usage
- ? Windows Drive Paths: `C:\Users\Dawson\Projects\lang-trak-in-progress\`
- ? Windows Long Paths: `\\?\C:\Users\Dawson\Projects\...`
- ? Mixed File System Operations
- ? Windows PowerShell direct file system access outside WSL

<!-- section_id: "b01c5e8b-ec07-45e5-beec-c9f70db0efb7" -->
## Development Tool Configuration

<!-- section_id: "2282d3e7-495a-4f32-a9d2-3d842e01fe88" -->
### Required WSL Ubuntu Setup
- **Python Environment**: Python 3.9+ installed in WSL Ubuntu
- **Node.js Environment**: Node.js 16+ via nvm in WSL Ubuntu
- **Firebase CLI**: Installed and configured within WSL Ubuntu
- **Git Configuration**: Git configured with proper credentials in WSL Ubuntu

<!-- section_id: "58a4eb50-2145-4b04-b72a-0b55f8182c70" -->
### Path Resolution Rules
- **Project Root**: Always reference from `/home/dawson/code/lang-trak-in-progress/`
- **Documentation**: `docs/` subdirectories using relative paths
- **Source Code**: All source files within WSL Ubuntu file system
- **Dependencies**: npm/pip packages installed in WSL Ubuntu environment

<!-- section_id: "3c08ae17-6400-475b-81a6-e6c466c6aa4a" -->
## Access Patterns

<!-- section_id: "41e1c4da-e230-4098-8d16-b66a4e1f4cd6" -->
### Correct Access Methods
- ? **PowerShell via WSL**: Commands executed through WSL Ubuntu shell context
- ? **Relative Paths**: Using `./` and `../` for navigation
- ? **WSL Ubuntu Commands**: Native Linux commands within WSL
- ? **Environment Variables**: WSL Ubuntu environment variables

<!-- section_id: "12382fbf-ea1c-40f1-8fa2-ca944d0727df" -->
### File Operations Standards
- **File Creation**: All new files created within WSL Ubuntu file system
- **File Editing**: All file modifications performed via WSL Ubuntu paths
- **File Movement**: All file operations respect WSL Ubuntu permissions
- **File References**: All code references use WSL Ubuntu path conventions

<!-- section_id: "3cf6b8d8-cd39-451f-957c-fd560e9d5032" -->
## Environment Benefits

<!-- section_id: "0526f117-759b-4a25-b5c6-cc6b60c35c82" -->
### Performance Advantages
- **Native Linux File System**: Optimal performance for development operations
- **Docker Integration**: Seamless Docker container operations
- **Package Management**: Native Linux package management (apt, npm, pip)
- **Symlink Support**: Full symbolic link support for development workflows

<!-- section_id: "d03fd9ce-f38a-412d-8eee-a2c7179317e6" -->
### Tool Integration
- **Firebase Emulators**: Optimal performance in Linux environment
- **SQLite Operations**: Native Linux SQLite performance
- **Python Development**: Full Linux Python environment capabilities
- **Node.js Tools**: Native Node.js development environment

<!-- section_id: "5adda052-30f4-413d-81ae-8a79f4db77bb" -->
### Development Consistency
- **Team Alignment**: Consistent development environment across team members
- **CI/CD Compatibility**: Production environments mirror WSL Ubuntu setup
- **Tool Compatibility**: All development tools optimized for Linux environment
- **Path Consistency**: Uniform path handling across all operations

<!-- section_id: "0d7282ac-ca9f-4f8d-8c98-d79bd47d114b" -->
## Environment Validation

<!-- section_id: "3ff33bc6-0748-4338-ba9c-3753527a66e3" -->
### Required Checks
Before any development work:
1. ? Verify current working directory is within WSL Ubuntu file system
2. ? Confirm all development tools are WSL Ubuntu versions
3. ? Validate file paths use WSL Ubuntu conventions
4. ? Ensure environment variables are set within WSL Ubuntu context

<!-- section_id: "ada05569-6d81-421f-a8a4-ebcbb34f66de" -->
### Environment Test Commands
```bash
# Verify WSL Ubuntu environment
pwd  # Should show /home/dawson/code/lang-trak-in-progress
which python3  # Should show WSL Ubuntu Python path
which node  # Should show WSL Ubuntu Node.js path
which firebase  # Should show WSL Ubuntu Firebase CLI path
```

<!-- section_id: "93003870-d409-4903-8ba2-c580f74c40b8" -->
### File System Verification
```bash
# Verify file system access
ls -la docs/  # Should list documentation directories
file docs/trickle-down-0.5-environment/wsl-ubuntu-environment.md  # Should show text file
stat .  # Should show WSL Ubuntu file system details
```

<!-- section_id: "eb1c48b0-2dfa-4f6f-83ed-9bac836d43d4" -->
## Migration Guidelines

<!-- section_id: "f9087bf3-01e4-4e46-9607-98d2a5329169" -->
### Moving from Windows File System
If any project files exist on Windows file system:
1. **Copy to WSL Ubuntu**: `cp -r /mnt/c/Users/Dawson/Projects/project-name ~/code/`
2. **Update References**: Change all file references to WSL Ubuntu paths
3. **Reconfigure Tools**: Reinstall/reconfigure development tools in WSL Ubuntu
4. **Verify Operations**: Test all development operations in WSL Ubuntu environment

<!-- section_id: "c2ed1047-4077-458d-9244-cccf5f1056a3" -->
### Environment Switching
- **From Windows PowerShell**: Access only via WSL Ubuntu context
- **Tool Installation**: Always install development tools within WSL Ubuntu
- **Configuration Files**: Store all config files in WSL Ubuntu home directory
- **Environment Variables**: Set all development environment variables in WSL Ubuntu

<!-- section_id: "4ff6e7a0-51d0-4a05-a2a8-dbd090baf094" -->
## Error Prevention

<!-- section_id: "1d4ced62-8ce5-4633-a852-688c1f71919c" -->
### Common Mistakes to Avoid
- ? Creating files with Windows PowerShell directly
- ? Using Windows paths in any development operations
- ? Installing development tools in Windows instead of WSL Ubuntu
- ? Mixing file operations between Windows and WSL Ubuntu file systems

<!-- section_id: "50859e54-09ca-417d-9bf4-77ba91f36736" -->
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
