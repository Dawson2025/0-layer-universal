---
resource_id: "e42e6669-6065-4970-8511-b875f6a75fc9"
resource_type: "readme
document"
resource_name: "README"
---
# Operating Systems

This level organizes setup documentation by operating system.

## Available Operating Systems

- **_shared/** - Setup that works across all operating systems
- **linux_ubuntu/** - Ubuntu/Linux-specific setup
- **macos/** - macOS-specific setup
- **windows/** - Windows-specific setup
- **wsl/** - Windows Subsystem for Linux-specific setup

## How to Navigate

1. Choose your operating system directory
2. Navigate down to `0.06_environments/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all OSes

## OS-Specific Considerations

### Linux/Ubuntu
- Package management via apt
- Permission handling with sudo
- WSLg for GUI apps in WSL
- Display server considerations (X11, Wayland)

### macOS
- Package management via Homebrew
- Permissions and security (Gatekeeper, quarantine)
- Native ARM vs x86_64 considerations

### Windows
- Package management via winget/chocolatey
- Path separators and environment variables
- PowerShell vs CMD considerations

### WSL
- Hybrid Windows/Linux environment
- WSLg for GUI support
- Path translation between Windows and Linux
- Network and filesystem interop

## Links to Detailed Documentation

For detailed OS setup documentation, see:
- **sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/**
