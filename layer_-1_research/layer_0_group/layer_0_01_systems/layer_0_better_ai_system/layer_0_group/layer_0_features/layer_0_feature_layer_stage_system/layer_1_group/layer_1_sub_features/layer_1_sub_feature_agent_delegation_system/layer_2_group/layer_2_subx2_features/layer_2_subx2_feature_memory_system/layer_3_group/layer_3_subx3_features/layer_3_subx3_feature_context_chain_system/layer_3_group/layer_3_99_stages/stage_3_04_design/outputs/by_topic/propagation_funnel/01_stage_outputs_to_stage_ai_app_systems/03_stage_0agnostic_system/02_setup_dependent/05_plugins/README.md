# Plugins (05_plugins)

## What This Contains

Extensions and plugins for both coding apps (IDE extensions) and AI apps (language model plugins). Plugins extend the functionality of your development and AI tools.

## Plugin Types

| Type | What | Examples |
|------|------|----------|
| Coding App Plugins | IDE extensions | VS Code extensions, Cursor extensions, NeoVim plugins |
| AI App Plugins | Language model integrations | Claude plugins, Perplexity integrations, custom tools |

## Coding App Plugins

### VS Code Extensions
```
05_plugins/vscode/
├── installed_extensions.md
├── extension_settings.md
└── recommended_extensions.md
```

### Cursor Extensions
```
05_plugins/cursor/
├── installed_extensions.md
└── extension_config.md
```

### NeoVim Plugins
```
05_plugins/neovim/
├── plugin_manager.md    # packer, vim-plug, lazy.nvim
├── installed_plugins.md
└── plugin_config.md
```

## AI App Plugins

### Claude Plugins
```
05_plugins/claude/
├── installed_plugins.md
├── custom_tools.md
└── integration_config.md
```

### Perplexity Integrations
```
05_plugins/perplexity/
├── integrations.md
└── custom_tools.md
```

## Compatibility Matrix

| Coding App | Compatible Plugins | Plugin Manager |
|------------|-------------------|-----------------|
| VS Code | VS Code Extension Marketplace | VS Code extensions |
| Cursor | VS Code Extension Marketplace | Built-in ext manager |
| NeoVim | Lua plugins | packer, vim-plug, lazy.nvim |

## Next Layer

After plugins, the next layer is **06_mcp_servers/** (Model Context Protocol server configurations).
