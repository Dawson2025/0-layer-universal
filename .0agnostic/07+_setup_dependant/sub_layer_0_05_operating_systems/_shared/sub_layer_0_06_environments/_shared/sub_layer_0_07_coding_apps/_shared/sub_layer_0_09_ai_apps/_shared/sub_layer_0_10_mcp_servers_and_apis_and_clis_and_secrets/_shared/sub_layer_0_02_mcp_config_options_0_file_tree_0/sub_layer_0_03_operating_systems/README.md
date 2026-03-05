---
resource_id: "0508fe95-5c7b-4683-80b1-fe2c3e310cce"
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

<!-- section_id: "01c888f5-c6d9-46a5-a121-5214f3297ccb" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "835634cf-cdd8-4fdc-bc5a-0c9a916e175b" -->
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

<!-- section_id: "8f7e4dfd-afca-4a50-b47d-7f469508232d" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns

---

<!-- section_id: "d30c9f9c-da14-4c19-b275-6ea09a052a76" -->
## Legacy MCP Source

# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "0af41387-a7d5-445a-8893-e832a38d6a13" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "b95559a1-4524-4a7f-8c66-fcec24359ba6" -->
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

<!-- section_id: "26b48433-ceaf-4b1f-acf5-663ee602e732" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns
