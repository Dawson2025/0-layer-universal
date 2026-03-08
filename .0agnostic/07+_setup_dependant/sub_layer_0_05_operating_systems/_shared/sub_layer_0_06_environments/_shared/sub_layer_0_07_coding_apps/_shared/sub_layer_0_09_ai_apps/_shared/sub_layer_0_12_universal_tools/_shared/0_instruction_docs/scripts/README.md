---
resource_id: "817e02c9-46dc-4c34-9e0a-1a42dfcdaa05"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "865aa8a6-ad90-4bc3-9bec-e5c14811af4b" -->
## Available Scripts

<!-- section_id: "2b54c152-d400-46f4-9288-adcdaa68e829" -->
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

<!-- section_id: "b2051163-dfbe-44ec-9fc2-2f3f07b62ab2" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "623b88b6-4f5c-4589-9418-90322f3f75ad" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern

