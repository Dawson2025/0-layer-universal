---
resource_id: "85cd43ec-137a-4065-ab8b-9677449ac1b1"
resource_type: "readme_document"
resource_name: "README"
---
# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "f7197af3-b20c-4b52-bcae-93def29c0456" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/dawson-workspace/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "7649f142-a071-496e-8f72-cdc119563425" -->
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

<!-- section_id: "64f82d31-940d-43f6-8763-77d3d94dee11" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns

---

<!-- section_id: "9eac96eb-55fb-4eeb-be2f-a315ada75550" -->
## Legacy MCP Source

# Operating System (MCP Setup)

This folder captures OS-specific requirements, quirks, and runbooks for MCP servers (especially browser automation).

Each OS folder includes:
- `README.md`: OS-level prerequisites and known issues.
- `0.04_ai_apps/`: app-specific MCP setup runbooks for that OS (Claude Code CLI, Gemini CLI, Codex CLI, Cursor).

Use this when a setup is sensitive to OS/display/runtime differences (e.g., WSLg headed browser).

---

<!-- section_id: "0412b462-7678-4f4d-8476-ef3fc87b4e74" -->
## Relationship to OS Variant and Quartet Pattern

This OS-specific MCP structure follows the broader **OS Variant Pattern** defined in the Ideal AI Manager Hierarchy System:

- **Normative Specification**: `/home/dawson/code/0_layer_universal/0_context/-1_research/-1.01_things_researched/ai_manager_hierarchy_system/things_learned/ideal_ai_manager_hierarchy_system/os_and_quartets.md`

<!-- section_id: "1877b89d-8b76-4ec5-80e1-a6ee6f4cdfab" -->
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

<!-- section_id: "a55f3623-82e5-48d3-8e8e-b506311032a4" -->
### Integration Points

- **MCP Setup**: Defines which MCP servers are available per OS/app combination
- **Agent Context**: Defines how agents should use those MCP servers in that OS
- **Tool Quartet**: CLAUDE.md, AGENTS.md, GEMINI.md reference MCP setup requirements

Agents should reference both:
1. This MCP OS setup documentation for MCP server configuration
2. The quartet context files for tool-specific execution patterns
