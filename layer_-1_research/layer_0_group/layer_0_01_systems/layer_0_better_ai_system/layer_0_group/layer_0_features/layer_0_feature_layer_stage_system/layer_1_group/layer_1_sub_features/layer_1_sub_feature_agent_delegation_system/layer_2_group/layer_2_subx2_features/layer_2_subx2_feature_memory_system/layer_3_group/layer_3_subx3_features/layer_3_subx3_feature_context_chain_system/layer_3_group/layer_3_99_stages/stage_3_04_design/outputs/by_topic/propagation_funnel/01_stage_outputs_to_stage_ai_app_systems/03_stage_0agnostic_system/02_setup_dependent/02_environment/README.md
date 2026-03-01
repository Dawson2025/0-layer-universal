# Environment (02_environment)

## What This Contains

Shell and system environment configuration for your machine. This layer defines shell type, PATH settings, environment variables, and shell customizations.

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

## Next Layer

After environment settings, the next layer is **03_coding_apps/** (IDE and code editor configurations).
