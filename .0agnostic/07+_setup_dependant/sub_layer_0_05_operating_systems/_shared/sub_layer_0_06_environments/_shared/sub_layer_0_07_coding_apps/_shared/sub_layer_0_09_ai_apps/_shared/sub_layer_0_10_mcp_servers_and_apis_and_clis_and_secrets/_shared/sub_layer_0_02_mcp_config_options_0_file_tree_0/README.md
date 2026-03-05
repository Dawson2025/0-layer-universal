---
resource_id: "bb3997d8-8bbf-4d5b-ad30-7cd87f239238"
resource_type: "readme
document"
resource_name: "README"
---
# 0.02 MCP Config Options (Traversable File Tree)

This folder is the **traversable MCP documentation file tree**. It is organized so you can always navigate:

`Operating System → AI App → MCP Server → general_issues_and_fixes`

<!-- section_id: "7c5b0d98-583b-40ac-9460-48073affcaf8" -->
## Canonical Tree

```text
0.02_mcp_config_options_0_file_tree_0/
└── 0.03_operating_systems/
    ├── _shared/                         # Cross-OS defaults
    │   └── 0.04_ai_apps/
    │       ├── _shared/                 # Cross-app canonical server docs
    │       │   └── 0.05_mcp_servers/
    │       │       ├── _mcp_core/       # Cross-server issues (tool exposure, env, limits)
    │       │       │   └── general_issues_and_fixes/
    │       │       ├── playwright-mcp/
    │       │       │   └── general_issues_and_fixes/
    │       │       └── ...
    │       └── <ai_app>/                # Cross-OS app runbooks (optional)
    │           └── 0.05_mcp_servers/    # Links to canonical server docs
    └── <os>/                            # OS-specific overrides and notes
        └── 0.04_ai_apps/
            └── <ai_app>/
                └── 0.05_mcp_servers/
                    └── <mcp_server>/
                        └── general_issues_and_fixes/
```

<!-- section_id: "549e3f70-301a-4bb7-8260-216df22c7678" -->
## How To Use This Tree

1. Start at `0.03_operating_systems/<os>/README.md`.
2. Go to `0.04_ai_apps/<ai_app>/README.md` for app-specific MCP config locations and quirks.
3. Go to `0.05_mcp_servers/<mcp_server>/` for server docs.
4. Put recurring problems, debugging steps, and known fixes in `general_issues_and_fixes/`.

<!-- section_id: "36720638-30c9-4c7f-835c-6787fbb40424" -->
## Notes

- Use `_shared/` when guidance is cross-platform or cross-app.
- `_mcp_core/` is a “pseudo-server” used to store issues and fixes that apply across many MCP servers.
