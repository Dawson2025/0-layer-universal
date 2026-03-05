---
resource_id: "3db5abd2-dd28-4dbb-8ae1-219a055075a0"
resource_type: "readme
document"
resource_name: "README"
---
# 0.02 MCP Config Options (Traversable File Tree)

This folder is the **traversable MCP documentation file tree**. It is organized so you can always navigate:

`Operating System → AI App → MCP Server → general_issues_and_fixes`

<!-- section_id: "3d061d10-c989-4fb7-ac5b-2499207b740f" -->
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

<!-- section_id: "c47ad2ce-0898-454c-9649-305c3357979c" -->
## How To Use This Tree

1. Start at `0.03_operating_systems/<os>/README.md`.
2. Go to `0.04_ai_apps/<ai_app>/README.md` for app-specific MCP config locations and quirks.
3. Go to `0.05_mcp_servers/<mcp_server>/` for server docs.
4. Put recurring problems, debugging steps, and known fixes in `general_issues_and_fixes/`.

<!-- section_id: "68fece47-721e-4120-b3ca-f8700cd0dd7e" -->
## Notes

- Use `_shared/` when guidance is cross-platform or cross-app.
- `_mcp_core/` is a “pseudo-server” used to store issues and fixes that apply across many MCP servers.
