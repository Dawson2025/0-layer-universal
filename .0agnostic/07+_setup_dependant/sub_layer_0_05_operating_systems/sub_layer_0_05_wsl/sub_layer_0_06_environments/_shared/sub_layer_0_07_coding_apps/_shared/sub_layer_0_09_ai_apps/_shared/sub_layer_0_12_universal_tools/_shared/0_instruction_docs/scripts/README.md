---
resource_id: "23fb560e-6ae1-49e3-988e-e1e70f83fdf7"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "9e33a196-424a-4633-bccb-1c98a67fdc82" -->
## Available Scripts

<!-- section_id: "847892bc-aa82-49d2-a5e6-c7df6c726e47" -->
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

<!-- section_id: "c0e21cc8-d424-478f-8e2f-18222a6a4917" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "cd760195-b656-4b52-baf9-e014caf712df" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern

