---
resource_id: "8fc87b99-4425-41d6-8ffe-29209a63f998"
resource_type: "readme
document"
resource_name: "README"
---
# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "c6d2af88-0e22-474f-991a-2a6bf87a3d46" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "7981b4a5-0469-436d-820d-2f9b07264c98" -->
### How MCP OS Structure Maps to the Ideal Spec

The MCP server setup uses a similar OS separation pattern:

**MCP Setup (This Location)**:
```
0.03_operating_systems/
├── wsl/
│   ├── README.md
│   └── 0.04_ai_apps/
│       ├── claude_code_cli/
│       ├── gemini_cli/
│       ├── codex_cli/
│       └── cursor/
├── linux_ubuntu/
├── windows/
└── macos/
```

**Agent Context (Ideal Hierarchy Implementation)**:
```
stage_*.01_instructions/ai_agent_system/os/
├── wsl/
│   ├── CLAUDE.md
│   ├── AGENTS.md
│   └── GEMINI.md
├── linux_ubuntu/
├── windows/
└── macos/
```

<!-- section_id: "b86f3067-1f94-4996-b5b4-78ba2e21ee0a" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns

---

<!-- section_id: "dcdb5f1d-2074-461f-b8b1-1763af8c9629" -->
## Legacy MCP Source

# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "db38c88e-aec9-4ccd-9c24-b9d0229883c1" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "2b6df504-87fb-4c90-bd21-7fbda93dcf4c" -->
### How MCP OS Structure Maps to the Ideal Spec

The MCP server setup uses a similar OS separation pattern:

**MCP Setup (This Location)**:
```
0.03_operating_systems/
├── wsl/
│   ├── README.md
│   └── 0.04_ai_apps/
│       ├── claude_code_cli/
│       ├── gemini_cli/
│       ├── codex_cli/
│       └── cursor/
├── linux_ubuntu/
├── windows/
└── macos/
```

**Agent Context (Ideal Hierarchy Implementation)**:
```
stage_*.01_instructions/ai_agent_system/os/
├── wsl/
│   ├── CLAUDE.md
│   ├── AGENTS.md
│   └── GEMINI.md
├── linux_ubuntu/
├── windows/
└── macos/
```

<!-- section_id: "effe5fe2-fadb-4d76-bc3e-695de03f7d43" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns
