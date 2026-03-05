---
resource_id: "50b6ee7d-1f57-423c-a142-ee622fad29f6"
resource_type: "knowledge"
resource_name: "systemd_user_services"
---
# Systemd User Services

<!-- section_id: "58a907a8-dff4-40ea-88d6-c37051e58e3a" -->
## Overview

Systemd manages both system-level and user-level services. User services run under `systemctl --user` and are specific to each logged-in user.

<!-- section_id: "2987ccfb-2dc6-4777-b9c3-f7929e9fb6ca" -->
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

<!-- section_id: "1a4cbc1f-e266-4c87-8444-4d17d3671c44" -->
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

<!-- section_id: "c8a21817-6853-4fa6-997f-2f5f139d7b8b" -->
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

<!-- section_id: "c3b431bf-96d0-4dd7-84b0-921be55e4826" -->
## Common Desktop Services

| Service | Purpose |
|---------|---------|
| `xdg-desktop-portal.service` | Portal coordinator |
| `xdg-desktop-portal-gtk.service` | GTK portal backend |
| `xdg-desktop-portal-gnome.service` | GNOME portal backend |
| `pipewire.service` | Audio/video routing |
| `pulseaudio.service` | Audio server (legacy) |

<!-- section_id: "e4846c50-c3d5-40b6-8ca8-0cf56599488d" -->
## Troubleshooting

<!-- section_id: "16a37b09-5dd1-400d-812a-2fd90fa4bd30" -->
### Service Won't Start
1. Check logs: `journalctl --user -u <service>`
2. Check dependencies: `systemctl --user list-dependencies <service>`
3. Verify environment: `systemctl --user show-environment`

<!-- section_id: "967bdfd4-4d13-40e4-9d5e-00dfaf123d3c" -->
### "Degraded" State
1. Find failures: `systemctl --user --failed`
2. Check each failed service's logs
3. Fix or mask non-essential failing services

<!-- section_id: "1ec8eaa0-da07-4bac-bc3f-f1b8342c64ab" -->
### Services Start Then Die
- Often missing D-Bus services they depend on
- Check for `org.gnome.SessionManager` availability
- Verify display access

<!-- section_id: "f7391667-475a-48e7-be3c-dd372d53d107" -->
## Related Documentation
- [Linux Fundamentals](../../linux_fundamentals/docs/)
- [Ubuntu Desktop](../../ubuntu_desktop/docs/)
