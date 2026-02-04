# Linux Ubuntu Setup

Setup documentation specific to Linux Ubuntu systems.

## Ubuntu-Specific Considerations

### Package Management
- Use `apt` for system packages
- Consider snap packages for certain applications
- PPA repositories for specialized software

### Permissions
- Use `sudo` for elevated permissions
- Configure sudoers for passwordless operations if needed
- File permissions (chmod, chown)

### Display Server
- X11 vs Wayland considerations
- WSLg for GUI apps in WSL environments

### MCP Servers on Linux
- Browser automation has special considerations (see MCP servers setup)
- Playwright requires explicit browser path specification
- Some tools may need display server configuration

## Common Ubuntu Versions
- Ubuntu 20.04 LTS (Focal Fossa)
- Ubuntu 22.04 LTS (Jammy Jellyfish)
- Ubuntu 24.04 LTS (Noble Numbat)

## Next Level

Navigate to `0.06_environments/` to continue setting up your environment.

## Links to Detailed Documentation

For detailed Linux Ubuntu setup, see:
- **sub_layer_0_05_os_setup/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_SETUP.md** (if exists)
