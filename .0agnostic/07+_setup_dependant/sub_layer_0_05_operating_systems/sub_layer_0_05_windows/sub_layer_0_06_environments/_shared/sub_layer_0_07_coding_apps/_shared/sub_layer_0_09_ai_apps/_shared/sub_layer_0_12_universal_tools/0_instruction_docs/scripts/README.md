---
resource_id: "1cad7fbb-6c44-4c66-bebd-da6abde4064c"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "c9445882-e0df-4b39-beba-6579f7d064c9" -->
## Available Scripts

<!-- section_id: "56589b9e-a275-4ae5-b6e7-be80e933e3d0" -->
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

<!-- section_id: "7c04a084-a361-4929-808e-222bf90f5529" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "1dfa370e-0bfc-49a7-b59c-04896a3cae4d" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern

---

<!-- section_id: "7539e730-664c-493e-a54f-fddba36a39f6" -->
## Legacy Universal Tools Source

# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "a0273e37-097b-4438-9617-312bafbbae39" -->
## Available Scripts

<!-- section_id: "31c68ff9-4c4e-4694-b5b1-b6b5b17a8c3b" -->
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

<!-- section_id: "6f11ce4c-d21f-4db9-8ab1-823d4c55fe0f" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "09f2214d-4a22-4c7f-826e-ae46750acb83" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern
