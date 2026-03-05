---
resource_id: "9d69d1b1-2bbf-4650-905f-789afaad02b0"
resource_type: "readme
document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

## Coding App-Specific Considerations

### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
