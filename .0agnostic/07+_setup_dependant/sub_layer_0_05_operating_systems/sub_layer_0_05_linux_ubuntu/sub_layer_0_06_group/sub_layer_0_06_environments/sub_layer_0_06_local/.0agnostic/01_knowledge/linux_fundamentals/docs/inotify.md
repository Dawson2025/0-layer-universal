---
resource_id: "4b233357-85d0-4ddf-bd11-3ad4ffac47e7"
resource_type: "knowledge"
resource_name: "inotify"
---
# Inotify - Linux File Watching System

<!-- section_id: "f39d97e7-6336-42d1-80aa-6505fa79f784" -->
## What is Inotify?

Inotify is a Linux kernel subsystem that monitors filesystem events. Applications use it to watch files and directories for changes (creation, modification, deletion, etc.).

<!-- section_id: "b2e02463-9747-42c6-8f6a-ee20bef52e5c" -->
## Key Concepts

<!-- section_id: "ef065696-072c-40f5-93a8-5ac99aaa33ac" -->
### Watches vs Instances
- **Watch**: Monitors a single file or directory
- **Instance**: A file descriptor opened by a process for inotify operations
- Each process can have multiple instances, each with multiple watches

<!-- section_id: "aad30848-d160-4212-bb68-6da5e0f308df" -->
### System Limits

| Parameter | Default | Location |
|-----------|---------|----------|
| `max_user_watches` | 65,536 | `/proc/sys/fs/inotify/max_user_watches` |
| `max_user_instances` | 128 | `/proc/sys/fs/inotify/max_user_instances` |

<!-- section_id: "4039ff2e-5eb0-4205-a07f-f2a6a0d300b7" -->
### Memory Usage
- Each watch consumes ~160-1000 bytes of kernel memory
- At 1M watches: ~160MB-1GB RAM dedicated to file watching

<!-- section_id: "2caf65f1-ce92-4428-a431-7144607100d0" -->
## Common Consumers

| Application Type | Inotify Usage |
|-----------------|---------------|
| IDEs (VS Code, Cursor, IntelliJ) | Heavy - watches all project files, node_modules |
| Electron apps | Heavy - each app runs Chromium + Node.js |
| Node.js hot-reload | Moderate - watches source files |
| File managers | Light - watches current directory |
| Desktop environments | Moderate - portals, settings daemons |

<!-- section_id: "82510137-1af4-449b-b63e-dfce073bb0d9" -->
## Symptoms of Exhaustion

When inotify limits are exhausted:
- Applications fail to start
- "No space left on device" errors (misleading - not disk space)
- Desktop services fail (media keys, file dialogs)
- IDE file watching breaks
- System enters "degraded" state

<!-- section_id: "f6989580-e847-4bf6-b998-b75c5e7e2816" -->
## Diagnostic Commands

```bash
# Check current limits
cat /proc/sys/fs/inotify/max_user_watches
cat /proc/sys/fs/inotify/max_user_instances

# Find processes using inotify
find /proc/*/fd -lname anon_inode:inotify 2>/dev/null | \
  cut -d/ -f3 | xargs -I '{}' -- ps --no-headers -o comm -p '{}' 2>/dev/null | \
  sort | uniq -c | sort -rn

# Check systemd user session status
systemctl --user is-system-running
systemctl --user --failed
```

<!-- section_id: "0af463b8-53d8-4ccc-8d02-335cc41ccf23" -->
## Related Documentation
- [Ubuntu Desktop](../../ubuntu_desktop/docs/)
- [System Services](../../system_services/docs/)
