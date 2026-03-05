---
resource_id: "97907507-dc83-43c7-9474-cd498f278cee"
resource_type: "document"
resource_name: "config"
---
# Claude Code CLI Configuration

## Environment
- **OS**: WSL (Windows Subsystem for Linux)
- **Environment**: Local development
- **Coding App**: Terminal
- **AI App**: Claude Code CLI

## Specific Settings

### Path Considerations
- WSL paths: `/home/<user>/...`
- Windows paths accessed via: `/mnt/c/...`
- Prefer Linux-native paths for performance

### Terminal Configuration
- Default shell: bash/zsh
- Command execution timeout: 120s default, 600s max
- Working directory preserved across commands

### Claude Code CLI Features
- File operations: Read, Write, Edit, Glob, Grep
- Bash command execution with sandbox
- Web fetch and search capabilities
- MCP server integrations

### Integration Notes
- Use absolute paths for file operations
- Avoid relative paths that may break across sessions
- Quote paths with spaces using double quotes

## Environment Variables
Common environment variables to consider:
- `$HOME` - User home directory
- `$PWD` - Current working directory
- `$PATH` - Executable search path
