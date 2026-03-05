---
resource_id: "9b3d61d3-5d08-4655-ba19-4c98865ada29"
resource_type: "readme
output"
resource_name: "README"
---
# Coding Apps (03_coding_apps)

<!-- section_id: "55250872-109d-427a-9bd1-b1940bc20621" -->
## What This Contains

IDE and code editor configurations specific to your coding environment. These are tools you use to write and edit code.

<!-- section_id: "3b0626f7-efe9-447c-9dd2-9fb27f9fad88" -->
## Supported Editors

| Editor | Location | Content |
|--------|----------|---------|
| Cursor | 03_coding_apps/cursor/ | Settings, keybindings, extensions |
| VS Code | 03_coding_apps/vscode/ | settings.json, keybindings, extensions |
| NeoVim | 03_coding_apps/neovim/ | init.lua, plugins, keybindings |
| Antigravity | 03_coding_apps/antigravity/ | Settings and configuration |
| Sublime | 03_coding_apps/sublime/ | Preferences and packages |
| Emacs | 03_coding_apps/emacs/ | .emacs, init.el, packages |

<!-- section_id: "61c97d2e-da5e-4813-b0b7-195f2ad24962" -->
## Example Structure

For Cursor:
```
03_coding_apps/cursor/
├── settings.md          # Cursor IDE settings
├── extensions.md        # Installed extensions
├── keybindings.md       # Custom keybindings
└── workspace.md         # Workspace-specific settings
```

For VS Code:
```
03_coding_apps/vscode/
├── settings.json        # Editor settings
├── keybindings.json     # Custom keybindings
├── extensions.md        # List of installed extensions
└── tasks.json           # Build and run tasks
```

<!-- section_id: "79b1c254-dcdb-4ef5-9558-e898dc30970b" -->
## Next Layer

After coding apps configuration, the next layer is **04_ai_apps/** (AI service CLI tools).
