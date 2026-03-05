---
resource_id: "a5ab71d9-6951-46b6-8ef3-8f7d0bd6ddfa"
resource_type: "readme
document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

<!-- section_id: "6fb30fdd-5eaa-4441-8b08-2a119af76904" -->
## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

<!-- section_id: "13cdc624-b4ed-4880-bb23-0d763ac334a2" -->
## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

<!-- section_id: "b30001cd-65c5-460a-9b1f-be0e0b368b5c" -->
## Coding App-Specific Considerations

<!-- section_id: "8a96e9f8-8b28-4b3b-b1da-157caad0addb" -->
### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

<!-- section_id: "521c5016-fc0e-4eb7-aca8-582b7c681a97" -->
### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

<!-- section_id: "bcff81c2-2f8e-4170-9940-95db3df79f90" -->
### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

<!-- section_id: "191410c2-6156-491e-a103-7bb84ef89e6e" -->
### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

<!-- section_id: "5602b83d-234a-47dd-93c3-933c5288fcc2" -->
## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
