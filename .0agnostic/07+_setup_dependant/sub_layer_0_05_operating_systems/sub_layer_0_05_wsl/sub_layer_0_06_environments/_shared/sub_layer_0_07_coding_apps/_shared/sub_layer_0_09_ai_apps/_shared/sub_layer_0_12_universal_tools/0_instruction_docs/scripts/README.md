---
resource_id: "29299bff-ee81-436d-8a1f-7f45e5e4e9b1"
resource_type: "readme_document"
resource_name: "README"
---
# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "47808f5d-075a-40f0-9e36-a80396248784" -->
## Available Scripts

<!-- section_id: "527f4d78-92d1-45e0-a661-b2eca2fed06c" -->
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

<!-- section_id: "4eda288a-49d1-4a4a-a4da-9123f3876faf" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "333bbdc1-b55b-46a9-a74b-b0be9c2b5baa" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern

---

<!-- section_id: "20acc2b0-7e2d-44e0-a54f-16baea760c72" -->
## Legacy Universal Tools Source

# Universal Scripts

This directory contains universal scripts that can be used across any project.

<!-- section_id: "b1df868b-e1e0-491f-8dfc-ff58e67f6857" -->
## Available Scripts

<!-- section_id: "20caaa9e-2d78-409b-8085-b4208afecf74" -->
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

<!-- section_id: "c97fa1cd-caeb-4abc-b35c-c2569f235040" -->
## Adding New Universal Scripts

When adding new universal scripts:

1. Place them in this `scripts/` directory
2. Make them executable: `chmod +x script-name.sh`
3. Document them in this README.md
4. Follow the universal documentation standards
5. Commit to the `0-universal-context` repository

<!-- section_id: "d5486a7b-44e3-4379-9d3a-6ef138d75993" -->
## Script Standards

- Use `#!/bin/bash` shebang
- Include error handling with `set -e`
- Add clear comments explaining what the script does
- Display helpful output messages
- Follow the trickle-down documentation pattern
