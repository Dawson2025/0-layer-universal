---
resource_id: "50b6ee7d-1f57-423c-a142-ee622fad29f6"
resource_type: "knowledge"
resource_name: "systemd_user_services"
---
# Systemd User Services

## Overview

Systemd manages both system-level and user-level services. User services run under `systemctl --user` and are specific to each logged-in user.

## Key Commands

```bash
# Check overall status
systemctl --user is-system-running    # "running" = healthy, "degraded" = failures

# List failed services
systemctl --user --failed

# Service management
systemctl --user status <service>
systemctl --user restart <service>
systemctl --user start <service>
systemctl --user stop <service>

# Reset failed state
systemctl --user reset-failed

# Mask/unmask services (prevent/allow starting)
systemctl --user mask <service>
systemctl --user unmask <service>

# View logs
journalctl --user -u <service> --no-pager
journalctl --user -u <service> --since "10 minutes ago"

# Reload after config changes
systemctl --user daemon-reload
```

## Environment Management

User services inherit environment from the session. Sometimes you need to import variables:

```bash
# Check current environment
systemctl --user show-environment

# Import variables from current shell
systemctl --user import-environment DISPLAY XAUTHORITY

# Set a variable
systemctl --user set-environment VAR=value
```

## Service Overrides

To customize a service without modifying the original:

```bash
# Create override directory
mkdir -p ~/.config/systemd/user/<service>.d/

# Create override file
cat > ~/.config/systemd/user/<service>.d/override.conf << 'EOF'
[Service]
Environment="DISPLAY=:0"
Environment="XAUTHORITY=/home/user/.Xauthority"
EOF

# Reload and restart
systemctl --user daemon-reload
systemctl --user restart <service>
```

## Common Desktop Services

| Service | Purpose |
|---------|---------|
| `xdg-desktop-portal.service` | Portal coordinator |
| `xdg-desktop-portal-gtk.service` | GTK portal backend |
| `xdg-desktop-portal-gnome.service` | GNOME portal backend |
| `pipewire.service` | Audio/video routing |
| `pulseaudio.service` | Audio server (legacy) |

## Troubleshooting

### Service Won't Start
1. Check logs: `journalctl --user -u <service>`
2. Check dependencies: `systemctl --user list-dependencies <service>`
3. Verify environment: `systemctl --user show-environment`

### "Degraded" State
1. Find failures: `systemctl --user --failed`
2. Check each failed service's logs
3. Fix or mask non-essential failing services

### Services Start Then Die
- Often missing D-Bus services they depend on
- Check for `org.gnome.SessionManager` availability
- Verify display access

## Related Documentation
- [Linux Fundamentals](../../linux_fundamentals/docs/)
- [Ubuntu Desktop](../../ubuntu_desktop/docs/)
