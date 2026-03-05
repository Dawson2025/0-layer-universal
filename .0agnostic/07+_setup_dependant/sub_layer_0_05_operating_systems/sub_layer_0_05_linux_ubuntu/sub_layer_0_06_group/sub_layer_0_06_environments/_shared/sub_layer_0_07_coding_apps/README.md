---
resource_id: "9d69d1b1-2bbf-4650-905f-789afaad02b0"
resource_type: "readme
document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

<!-- section_id: "a1a189dd-72dc-4f1d-99a7-f7e3fa0623d2" -->
## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

<!-- section_id: "ab694fad-437a-45d7-ae7c-685b402b8a25" -->
## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

<!-- section_id: "fba5462a-77ce-4fdf-9ce7-132fa4201dbd" -->
## Coding App-Specific Considerations

<!-- section_id: "ef6046b8-c16e-4916-a7c7-1050c3e46755" -->
### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

<!-- section_id: "330d6d40-d958-4204-935b-2edb3a275828" -->
### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

<!-- section_id: "1cf4370b-7843-4e13-bffc-096d3a0701e4" -->
### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

<!-- section_id: "b84ade22-858e-4078-a441-7cb1975eec2a" -->
### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

<!-- section_id: "90d42e1d-c3f5-4319-b17b-c09c9f86d44a" -->
## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
