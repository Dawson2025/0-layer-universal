---
resource_id: "9e6d8f50-d0d8-4049-8090-46917c87af5d"
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

<!-- section_id: "5896fbbf-b8c6-4324-b240-ab48ec7e8543" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "49a6f7ee-d09b-4611-bae3-c74b3751e2ce" -->
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

<!-- section_id: "2e605c8d-a939-40a6-9a29-ce51e3536b43" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns

---

<!-- section_id: "4b2a785c-2f67-4499-9ea2-981d05a95b8f" -->
## Legacy MCP Source

# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "647c5ffc-ac8e-48cf-90eb-63c87d585cd9" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "95dcf856-b4c0-4501-b1ca-157ca249dafe" -->
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

<!-- section_id: "5dbf8db4-e5fc-454d-967a-4767fd540aa7" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns
