---
resource_id: "cbdc921f-30e7-482b-bf27-152ba49d18b9"
resource_type: "readme_document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

<!-- section_id: "d9989d9b-93a5-4993-b9e5-abb49f87d23b" -->
## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

<!-- section_id: "6f109e41-8958-46cc-8b28-a8fc0d1e92c0" -->
## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

<!-- section_id: "0780221c-f480-4060-9df3-6cde5725cf04" -->
## Coding App-Specific Considerations

<!-- section_id: "fdb54c2a-ee83-4f5f-abce-57b3a9906fe1" -->
### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

<!-- section_id: "2ad418b4-57bf-434a-86dd-47a574314a7c" -->
### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

<!-- section_id: "94cb05f4-cb6b-4d08-96c7-186cce5e7366" -->
### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

<!-- section_id: "f45569e8-e7ef-4c2b-8fc0-87b224416994" -->
### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

<!-- section_id: "07c9df29-6363-44fd-b368-76571e428986" -->
## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
