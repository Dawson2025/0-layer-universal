---
resource_id: "b6f4d111-fa6d-476f-baf6-777494a1da7a"
resource_type: "readme_output"
resource_name: "README"
---
# Plugins (05_plugins)

<!-- section_id: "efe40cc2-f505-4bc9-a6d7-b480fa778750" -->
## What This Contains

Extensions and plugins for both coding apps (IDE extensions) and AI apps (language model plugins). Plugins extend the functionality of your development and AI tools.

<!-- section_id: "228c7fa6-eac4-4959-b981-48d03f27bde9" -->
## Plugin Types

| Type | What | Examples |
|------|------|----------|
| Coding App Plugins | IDE extensions | VS Code extensions, Cursor extensions, NeoVim plugins |
| AI App Plugins | Language model integrations | Claude plugins, Perplexity integrations, custom tools |

<!-- section_id: "0bcddb77-3b63-42df-8000-3c8f9a45137c" -->
## Coding App Plugins

<!-- section_id: "7b11b3c1-eb5d-406d-9249-cb7053c4f229" -->
### VS Code Extensions
```
05_plugins/vscode/
├── installed_extensions.md
├── extension_settings.md
└── recommended_extensions.md
```

<!-- section_id: "79c3abc6-e9a6-4ddb-ae54-0129ee66ea1f" -->
### Cursor Extensions
```
05_plugins/cursor/
├── installed_extensions.md
└── extension_config.md
```

<!-- section_id: "e6237808-0f25-4b1a-b180-6d10e5ad48f5" -->
### NeoVim Plugins
```
05_plugins/neovim/
├── plugin_manager.md    # packer, vim-plug, lazy.nvim
├── installed_plugins.md
└── plugin_config.md
```

<!-- section_id: "0040473d-c16c-4580-9215-37b44e11a5de" -->
## AI App Plugins

<!-- section_id: "5abdafb8-38e8-4784-9ee4-4950f27604e6" -->
### Claude Plugins
```
05_plugins/claude/
├── installed_plugins.md
├── custom_tools.md
└── integration_config.md
```

<!-- section_id: "6fd0d287-eb84-430c-b122-61a8caa77c76" -->
### Perplexity Integrations
```
05_plugins/perplexity/
├── integrations.md
└── custom_tools.md
```

<!-- section_id: "33b6af69-a474-4fb9-9997-aaf7ea87aacf" -->
## Compatibility Matrix

| Coding App | Compatible Plugins | Plugin Manager |
|------------|-------------------|-----------------|
| VS Code | VS Code Extension Marketplace | VS Code extensions |
| Cursor | VS Code Extension Marketplace | Built-in ext manager |
| NeoVim | Lua plugins | packer, vim-plug, lazy.nvim |

<!-- section_id: "59fb787e-74c6-4674-81e8-02a214d450fb" -->
## Next Layer

After plugins, the next layer is **06_mcp_servers/** (Model Context Protocol server configurations).
