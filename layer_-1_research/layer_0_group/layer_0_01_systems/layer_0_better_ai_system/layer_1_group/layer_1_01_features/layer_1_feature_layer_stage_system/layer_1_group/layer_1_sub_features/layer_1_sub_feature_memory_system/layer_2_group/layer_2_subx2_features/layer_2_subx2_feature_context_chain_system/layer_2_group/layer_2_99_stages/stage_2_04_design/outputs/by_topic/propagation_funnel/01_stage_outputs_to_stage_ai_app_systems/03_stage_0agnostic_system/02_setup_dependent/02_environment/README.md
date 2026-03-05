---
resource_id: "1d0b90a6-04b6-4992-993e-f558d0eae21f"
resource_type: "readme
output"
resource_name: "README"
---
# Environment (02_environment)

<!-- section_id: "41ad48ee-9f7c-4b0f-b539-aeefecfd7dd5" -->
## What This Contains

Shell and system environment configuration for your machine. This layer defines shell type, PATH settings, environment variables, and shell customizations.

<!-- section_id: "a0863add-3eb0-40ad-97b8-5a67fd0c8fb0" -->
## Categories

| Category | Content |
|----------|---------|
| Shell Type | bash, zsh, fish, powershell version/config |
| Configuration Files | ~/.bashrc, ~/.zshrc, ~/.config/fish/config.fish |
| PATH Configuration | PATH entries and precedence order |
| Environment Variables | HOME, USER, SHELL, EDITOR, custom vars |
| Shell Aliases | Commonly used command shortcuts |
| Shell Functions | Custom bash/zsh functions |
| Terminal Emulator | GNOME Terminal, iTerm2, Windows Terminal settings |
| SSH Keys | SSH key locations and configurations |
| Locale & Encoding | LANG, LC_*, timezone settings |

<!-- section_id: "81967449-8880-479d-b386-c8d5c76158a8" -->
## Example Structure

```
02_environment/
├── shell_type.md          # Which shell (bash 5.1, zsh 5.8, fish 3.4, etc.)
├── path_configuration.md  # PATH ordering and key directories
├── env_variables.md       # Environment variables specific to this machine
├── shell_aliases.md       # Commonly used aliases
├── shell_functions.md     # Custom shell functions
├── terminal_settings.md   # Terminal emulator configuration
└── ssh_configuration.md   # SSH keys and remote access setup
```

<!-- section_id: "315b4aa7-1af4-41c3-a4d4-0f2c3ae980a6" -->
## Next Layer

After environment settings, the next layer is **03_coding_apps/** (IDE and code editor configurations).
