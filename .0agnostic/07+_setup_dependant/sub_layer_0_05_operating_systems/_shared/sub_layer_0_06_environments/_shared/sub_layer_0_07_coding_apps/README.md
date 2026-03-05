---
resource_id: "7a50f1ad-66de-442c-93fb-db412226902b"
resource_type: "readme
document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

<!-- section_id: "441f2830-d903-4bfc-8842-a8da4b82f171" -->
## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

<!-- section_id: "1652d5b2-0667-4598-a8e2-b0532c4b097a" -->
## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

<!-- section_id: "4dc330fa-c834-4552-9a93-b02726daeb89" -->
## Coding App-Specific Considerations

<!-- section_id: "93d7e4c9-7f99-452e-9209-4a80139ab922" -->
### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

<!-- section_id: "649501c8-93b3-4a88-a2cc-bbfdc7215125" -->
### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

<!-- section_id: "b1298ec5-797f-4143-b10e-f5c9b2c9e9dc" -->
### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

<!-- section_id: "e0820246-5761-4860-933a-1ad1dcb3b16f" -->
### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

<!-- section_id: "125055db-0faf-4253-86e9-1a7f8cff4c9d" -->
## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
