---
resource_id: "1a780bf5-1d6a-40ad-9f67-20f705fc821e"
resource_type: "readme
output"
resource_name: "README"
---
# Operating System (01_os)

<!-- section_id: "7c9956ed-ea2b-473c-b1c9-e70b968ff428" -->
## What This Contains

OS-specific context for your operating system. This is the foundational layer of setup-dependent context — all other setup layers build on top of OS-specific decisions.

<!-- section_id: "779675e9-77d5-42c5-bed8-8f3a53142d03" -->
## Categories

| Category | Content |
|----------|---------|
| Path Conventions | Linux/macOS `/home/user/`, Windows `C:\Users\user\` |
| Command Syntax | OS-specific commands (ls vs dir, apt vs brew) |
| System Utilities | Built-in tools available on this OS |
| Desktop Environment | GNOME, KDE, XFCE, Aqua, Windows Explorer |
| Package Managers | apt, brew, pacman, choco, winget, etc. |
| Shell Availability | bash, zsh, fish, powershell, cmd |
| Permission Model | Unix permissions vs Windows ACLs |
| File System | ext4, NTFS, APFS, case-sensitive vs case-insensitive |

<!-- section_id: "2247182f-60bd-4648-80e9-a249f21ab47a" -->
## Example Structure

For Linux:
- `linux/` — Linux-specific paths, commands, utilities
- `linux/ubuntu/` — Ubuntu-specific packages, GNOME settings
- `linux/fedora/` — Fedora-specific packages, SELinux

For macOS:
- `macos/` — macOS-specific paths, commands, utilities
- `macos/brew/` — Homebrew package management
- `macos/aqua/` — macOS GUI frameworks

For Windows:
- `windows/` — Windows-specific paths, commands, utilities
- `windows/powershell/` — PowerShell configuration
- `windows/wsl/` — Windows Subsystem for Linux settings

<!-- section_id: "7cb67cd4-3016-41ae-a2a9-969a067dd6fe" -->
## Next Layer

After OS-specific context, the next layer is **02_environment/** (shell configuration, environment variables, system settings).
