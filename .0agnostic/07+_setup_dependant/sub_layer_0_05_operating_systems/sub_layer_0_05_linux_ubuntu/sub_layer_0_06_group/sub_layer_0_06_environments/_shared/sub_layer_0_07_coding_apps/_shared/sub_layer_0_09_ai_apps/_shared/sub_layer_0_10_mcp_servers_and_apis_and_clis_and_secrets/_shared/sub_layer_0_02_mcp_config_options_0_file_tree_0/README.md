---
resource_id: "9620ea5f-d6bc-47fe-8fad-0560d3277abc"
resource_type: "readme
document"
resource_name: "README"
---
# 0.02 MCP Config Options (Traversable File Tree)

This folder is the **traversable MCP documentation file tree**. It is organized so you can always navigate:

`Operating System → AI App → MCP Server → general_issues_and_fixes`

<!-- section_id: "9c88608b-4f4f-4cf5-bdeb-b631586f3ca6" -->
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

<!-- section_id: "8d7818ee-cf1a-45fa-ba2d-cd841bb19376" -->
## How To Use This Tree

1. Start at `0.03_operating_systems/<os>/README.md`.
2. Go to `0.04_ai_apps/<ai_app>/README.md` for app-specific MCP config locations and quirks.
3. Go to `0.05_mcp_servers/<mcp_server>/` for server docs.
4. Put recurring problems, debugging steps, and known fixes in `general_issues_and_fixes/`.

<!-- section_id: "6f742660-675c-44d7-97aa-71b3e3715a59" -->
## Notes

- Use `_shared/` when guidance is cross-platform or cross-app.
- `_mcp_core/` is a “pseudo-server” used to store issues and fixes that apply across many MCP servers.
