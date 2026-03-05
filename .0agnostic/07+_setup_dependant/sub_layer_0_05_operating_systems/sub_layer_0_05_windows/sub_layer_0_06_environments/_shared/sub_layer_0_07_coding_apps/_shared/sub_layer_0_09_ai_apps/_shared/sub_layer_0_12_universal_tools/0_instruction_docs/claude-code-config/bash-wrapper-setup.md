---
resource_id: "15f834ff-42fd-4cf3-b696-e431dc998272"
resource_type: "document"
resource_name: "bash-wrapper-setup"
---
# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "9f044003-17eb-455b-976c-f6ed3b250e37" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "0d4de23f-fcce-4e02-9e93-5ee69d9d8c47" -->
## Why Use a Bash Wrapper?

<!-- section_id: "e399c167-8bcf-4acf-b544-8555b266210e" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "715ba073-1ac8-4598-94a0-ebe56c25454c" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "296c83de-6fb5-4192-a8bb-ca4166e219cb" -->
## Implementation

<!-- section_id: "6a4c29a6-dca8-4760-824c-d95360eb4677" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "73a82ea7-9123-4940-8c4b-3e2352a43285" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "646fb00e-724a-4d36-8e54-98da99320c5c" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "5599b027-6714-4c19-8f1a-bd5d5bd44ad7" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/dawson-workspace/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/dawson-workspace/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "6394fb61-55d4-4ad3-b4c4-7357d3aa638f" -->
## Advanced Configurations

<!-- section_id: "f9c0ce23-0908-4e05-8864-0b761dcb5d9c" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "f14eb50a-259e-4cb6-a310-d34cd4ee3bab" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "1e62c07a-900b-48ae-8b1d-c7464ba2dc3d" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "f69110ac-a914-49f6-9276-0fedaadcc610" -->
## Debugging

<!-- section_id: "e00f8490-abf4-4f97-9743-05c9d43e83d4" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "ba4639b6-8e10-4a99-952d-2c8d48a4c8db" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "8146b8c1-1f89-48a9-9a39-2b022aeddf63" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "9ab337a5-2b3c-4694-9bbd-e83c49591e3b" -->
## Removing the Wrapper

<!-- section_id: "99b4fec4-ccca-4b96-bc57-e13be15ac760" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "ed38f6b9-a68d-4c39-8ddf-44e26e902e8d" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "9329c2be-27a4-4676-96d5-b3def9d9d26a" -->
## Security Considerations

<!-- section_id: "68a8aeeb-84a5-4130-9d57-87f28069e5a7" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "9e39e4fa-c7f2-430f-a159-8e130b2d3516" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "74e5a858-dfdc-4d4e-a0ad-9b6b6e2bb4c4" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "05b99f18-afd3-4ce5-836a-142745b50da2" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "693d3bf8-3309-4931-bbfc-777bbb6bc2b7" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "694b8c1a-7fd5-47b1-9f1c-669dd59eaef8" -->
## Frequently Asked Questions

<!-- section_id: "9b3bf954-3d83-4ca4-bcd7-26aaa4ceebf5" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "8fc054f8-95e3-48e7-9b62-9637fc9afdd7" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "c62a804d-5e5b-4688-b234-b00d294441a9" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "822d46a3-aa05-45cd-af96-60141c4659c9" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "379e593b-13cf-4341-ae78-77f93ded07ae" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "9a8f707a-3f09-40c0-84df-5ff930e883a4" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "c0aabf5a-16a5-4f24-bedf-b6fc0441978d" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*

---

<!-- section_id: "62f9d0b9-b651-41b8-bf86-1f6a6fd05507" -->
## Legacy Universal Tools Source

# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "c211cbb1-bd62-447b-a2eb-a57d213e26cf" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "93b0cb76-1d1a-4d5c-81af-8f9515d79c92" -->
## Why Use a Bash Wrapper?

<!-- section_id: "b71c87af-54aa-4562-9e45-61e4f64e1c6c" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "81918abe-6363-4902-88e3-4bf41ac214dc" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "2eadc1f7-fed8-4e33-b860-61b82aaf4795" -->
## Implementation

<!-- section_id: "9148c872-f9a9-4aa5-bc99-faa7d2b9606b" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "0ba67436-e2c8-499f-896c-31679119c968" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "db35508b-b874-46d1-9383-d0109c8cdfa2" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "2ccdcaf8-a257-47a9-a97f-ed3c7f404e08" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "e0f4c228-7348-48df-8678-38df27ef563b" -->
## Advanced Configurations

<!-- section_id: "7bc604af-0728-4f03-8022-f21a17ba0f69" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "4d380029-73bb-4131-a88c-2635927d5661" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "aa6eed2f-49f9-4525-adb2-108c543731b8" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "7f35cd84-99f9-4e35-96aa-8d6f23991c98" -->
## Debugging

<!-- section_id: "698b2eba-e946-471e-b6c2-71bfd9243576" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "a46e29da-88f4-4d38-bc25-6ef68839aea3" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "777b0e0b-4dca-4fc6-9cf5-f3cb13b472bb" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "dc7d88ae-af32-4992-9206-2e4a7d8770bb" -->
## Removing the Wrapper

<!-- section_id: "34b18806-955a-4a6d-84fc-1df7751cdba8" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "0a2f7904-0d4a-4233-b435-fbd9d2aadc7b" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "ae8b68a1-bc42-4295-87c2-99185b5761a7" -->
## Security Considerations

<!-- section_id: "d061a185-ae98-4601-b17d-5f4cccc11a77" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "0f33c330-8a3a-4071-935c-6da428b98676" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "84a7f03c-29d7-4054-9964-12f55eeb2fc1" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "ab56f39b-947e-4218-a44b-069652761977" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "51f93b1d-32e4-4181-9538-deecbe18a236" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "f7a92eb4-c6ce-44b7-aa5c-c08bb7b13ebf" -->
## Frequently Asked Questions

<!-- section_id: "383f5053-5e8b-4e71-9fc8-c0f7cff387a5" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "bb999a7c-8659-4ad8-b035-26ea44e2ce6f" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "45f037e9-16fe-484a-aa4a-f1195fff1a21" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "7df99015-2e5a-4724-b4fa-7422a41c1a70" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "c4b9ab8b-1594-4567-a7e2-0fb2d4c51ea9" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "60eaecbb-7c0a-4112-aa82-e17af0141fed" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "ce386828-0e01-405a-b038-504c549eec92" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*
