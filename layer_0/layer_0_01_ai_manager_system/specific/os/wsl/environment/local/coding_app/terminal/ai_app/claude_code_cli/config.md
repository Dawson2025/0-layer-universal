---
resource_id: "97907507-dc83-43c7-9474-cd498f278cee"
resource_type: "document"
resource_name: "config"
---
# Claude Code CLI Configuration

<!-- section_id: "51ff5f56-c743-4019-9bda-1d2af1d65f41" -->
## Environment
- **OS**: WSL (Windows Subsystem for Linux)
- **Environment**: Local development
- **Coding App**: Terminal
- **AI App**: Claude Code CLI

<!-- section_id: "da3fb670-a801-4ab1-a9aa-51ff1c665755" -->
## Specific Settings

<!-- section_id: "7e647af7-09df-47b7-b148-3d3da4f5e063" -->
### Path Considerations
- WSL paths: `/home/<user>/...`
- Windows paths accessed via: `/mnt/c/...`
- Prefer Linux-native paths for performance

<!-- section_id: "cff33278-9713-421f-8f41-a92a67068407" -->
### Terminal Configuration
- Default shell: bash/zsh
- Command execution timeout: 120s default, 600s max
- Working directory preserved across commands

<!-- section_id: "82d68c35-dfaa-4f9a-a194-d3785cc9fdca" -->
### Claude Code CLI Features
- File operations: Read, Write, Edit, Glob, Grep
- Bash command execution with sandbox
- Web fetch and search capabilities
- MCP server integrations

<!-- section_id: "447ae4a5-f71d-4372-b22a-933e05d449fc" -->
### Integration Notes
- Use absolute paths for file operations
- Avoid relative paths that may break across sessions
- Quote paths with spaces using double quotes

<!-- section_id: "a34b7770-bf4b-4abd-8ff9-789ea2fdb384" -->
## Environment Variables
Common environment variables to consider:
- `$HOME` - User home directory
- `$PWD` - Current working directory
- `$PATH` - Executable search path
