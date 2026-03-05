---
resource_id: "f850b3ac-e86d-465a-b903-85dc5bc23170"
resource_type: "readme
document"
resource_name: "README"
---
# Coding Apps / IDEs

This level organizes setup documentation by coding application or IDE.

<!-- section_id: "cbf97b09-b190-459a-a249-790dd18f63af" -->
## Available Coding Apps

- **_shared/** - Setup that works across all coding apps
- **vscode/** - Visual Studio Code setup
- **cursor/** - Cursor IDE setup
- **vim/** - Vim/NeoVim setup
- **emacs/** - Emacs setup

<!-- section_id: "7957b56e-a171-4013-8cf2-0b730b033df4" -->
## How to Navigate

1. Choose your coding app directory
2. Navigate down to `0.09_ai_apps/` to continue the setup hierarchy
3. Use `_shared/` when the setup applies to all coding apps

<!-- section_id: "ba4ce3b6-419a-45c5-b512-845d8564c552" -->
## Coding App-Specific Considerations

<!-- section_id: "8eeba6a8-77de-4100-93d5-c4375aa2460d" -->
### VS Code
- Extensions marketplace
- Settings.json configuration
- Workspace settings
- Keybindings

<!-- section_id: "7d34fcea-3fc4-4def-9de0-e3db9e0e0775" -->
### Cursor
- AI agent integration
- Chat interface
- Composer features
- MCP server configuration (via `.cursor/config.json` or `~/.cursor/config.json`)

<!-- section_id: "4e1c2038-8cbe-41ab-a660-3df09d86bf84" -->
### Vim/NeoVim
- Plugin managers (vim-plug, packer, lazy.nvim)
- .vimrc or init.lua configuration
- Terminal integration
- LSP setup

<!-- section_id: "33b25492-bb01-497c-90da-d91814e454a6" -->
### Emacs
- Package managers (use-package, straight.el)
- init.el configuration
- Org-mode setup
- Evil mode for Vim keybindings

<!-- section_id: "fe920447-1f3d-4bf5-9c4e-ff03710fe5f1" -->
## Links to Detailed Documentation

For detailed coding app setup, see:
- **sub_layer_0_07_coding_app_setup/trickle_down_0.5_setup/0_instruction_docs/**
