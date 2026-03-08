---
resource_id: "e42e6669-6065-4970-8511-b875f6a75fc9"
resource_type: "readme_document"
resource_name: "README"
---
# Operating Systems

This level organizes setup documentation by operating system.

<!-- section_id: "815edd6b-d4d8-4ea3-9640-9d49abf71b95" -->
## Available Operating Systems

- **_shared/** - Setup that works across all operating systems
- **linux_ubuntu/** - Ubuntu/Linux-specific setup
- **macos/** - macOS-specific setup
- **windows/** - Windows-specific setup
- **wsl/** - Windows Subsystem for Linux-specific setup

<!-- section_id: "453c0982-de60-4fd3-93f1-5d89c9515231" -->
## How to Navigate

1. Choose your operating system directory
2. Navigate down to `0.06_environments/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all OSes

<!-- section_id: "bff5d361-66c6-4416-8e50-51fe7f6b2237" -->
## OS-Specific Considerations

<!-- section_id: "bd3902b4-b69d-4a52-8446-2c35029cdc28" -->
### Linux/Ubuntu
- Package management via apt
- Permission handling with sudo
- WSLg for GUI apps in WSL
- Display server considerations (X11, Wayland)

<!-- section_id: "f7f33847-2097-4105-ae81-3e4b912d2600" -->
### macOS
- Package management via Homebrew
- Permissions and security (Gatekeeper, quarantine)
- Native ARM vs x86_64 considerations

<!-- section_id: "0fa3b434-0139-4c12-9840-f675e74d021e" -->
### Windows
- Package management via winget/chocolatey
- Path separators and environment variables
- PowerShell vs CMD considerations

<!-- section_id: "fe30fc7b-9519-4f41-9d85-ae1b8d769491" -->
### WSL
- Hybrid Windows/Linux environment
- WSLg for GUI support
- Path translation between Windows and Linux
- Network and filesystem interop

<!-- section_id: "92af31d5-8b79-4128-828d-151d07443f18" -->
## Links to Detailed Documentation

For detailed OS setup documentation, see:
- **sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/**
