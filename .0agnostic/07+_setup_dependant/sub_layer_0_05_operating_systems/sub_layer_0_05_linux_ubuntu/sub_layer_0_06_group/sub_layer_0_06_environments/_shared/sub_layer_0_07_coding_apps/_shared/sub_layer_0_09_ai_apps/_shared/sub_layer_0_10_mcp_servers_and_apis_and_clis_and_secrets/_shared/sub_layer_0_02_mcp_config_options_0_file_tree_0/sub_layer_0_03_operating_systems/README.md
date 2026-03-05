---
resource_id: "96aa07be-b4ae-4a8b-820b-f1b0d88bb96f"
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

## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

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

### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns

---

## Legacy MCP Source

# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

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

### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns
