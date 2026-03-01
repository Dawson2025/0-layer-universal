# Operating System (01_os)

## What This Contains

OS-specific context for your operating system. This is the foundational layer of setup-dependent context — all other setup layers build on top of OS-specific decisions.

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

## Next Layer

After OS-specific context, the next layer is **02_environment/** (shell configuration, environment variables, system settings).
