---
resource_id: "053853ca-61f4-4219-a157-4d3c1490c0a1"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "acb29909-883f-4d90-9824-b1d3ceb52f96" -->
## Available Scripts

<!-- section_id: "6f382c93-8a13-4f32-a524-1caac318bc52" -->
### `sync-context-repos.sh`

**Purpose**: Synchronize the universal context and setup-hub repositories.

**Usage**:
```bash
/home/dawson/dawson-workspace/code/0-universal-context/0_context/trickle_down_0.75_universal_tools/0_instruction_docs/scripts/sync-context-repos.sh
```

Or create an alias:
```bash
alias sync-context='bash /home/dawson/dawson-workspace/code/0-universal-context/0_context/trickle_down_0.75_universal_tools/0_instruction_docs/scripts/sync-context-repos.sh'
```

**What it does**:
- Checks for uncommitted changes in both repositories
- Pulls latest changes from remote (origin/main or origin/master)
- Displays repository status and latest commit info

**Repositories synced**:
- `/home/dawson/dawson-workspace/code/0-universal-context`
- `/home/dawson/dawson-workspace/code/setup-hub`

**Note**: This script will warn you if there are uncommitted changes but won't commit or push them automatically. You should commit and push changes manually after reviewing them.

<!-- section_id: "ba2e2d30-38eb-404c-8d42-e190de6ea306" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "655af153-8383-4ca5-a9df-c6e5ba5f2f8a" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern

---

<!-- section_id: "1d6a520e-a773-42d3-8444-eb6ca31d645a" -->
## Legacy Universal Tools Source

# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "050486b3-bf5d-4848-96d6-a53b0a1e78b1" -->
## Available Scripts

<!-- section_id: "d6fcafde-3388-4599-be58-c309b669b18c" -->
### `sync-context-repos.sh`

**Purpose**: Synchronize the universal context and setup-hub repositories.

**Usage**:
```bash
/home/dawson/code/0-universal-context/0_context/trickle_down_0.75_universal_tools/0_instruction_docs/scripts/sync-context-repos.sh
```

Or create an alias:
```bash
alias sync-context='bash /home/dawson/code/0-universal-context/0_context/trickle_down_0.75_universal_tools/0_instruction_docs/scripts/sync-context-repos.sh'
```

**What it does**:
- Checks for uncommitted changes in both repositories
- Pulls latest changes from remote (origin/main or origin/master)
- Displays repository status and latest commit info

**Repositories synced**:
- `/home/dawson/code/0-universal-context`
- `/home/dawson/code/setup-hub`

**Note**: This script will warn you if there are uncommitted changes but won't commit or push them automatically. You should commit and push changes manually after reviewing them.

<!-- section_id: "11407814-e957-474d-b4d7-880fcb5b15bc" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "64ccac8d-8c41-46ce-8cb0-76096be7f3bb" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern
